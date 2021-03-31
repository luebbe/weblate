#
# Copyright © 2012 - 2021 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from typing import Dict

from django import template

from weblate.metrics.models import Metric
from weblate.trans.models import Component, Project, Translation

register = template.Library()


class MetricsWrapper:
    def __init__(self, scope: int, relation: int):
        self.scope = scope
        self.relation = relation
        self.current = Metric.objects.get_current(scope, relation)
        self.past_30 = Metric.objects.get_past(scope, relation, 30)
        self.past_60 = Metric.objects.get_past(scope, relation, 60)

    @property
    def all_words(self):
        return self.current["all_words"]

    @property
    def all(self):
        return self.current["all"]

    @property
    def translated_percent(self):
        return 100 * self.current["translated"] / self.all

    @property
    def contributors(self):
        return self.current["contributors"]

    def calculate_trend_percent(self, key, modkey, base: Dict, origin: Dict):
        total = base[key]
        if not total:
            return 0
        divisor = base[modkey]
        if not divisor:
            return 0
        total = 100 * total / divisor

        past = origin[key]
        if not past:
            return total

        divisor = origin[modkey]
        if not divisor:
            return total
        past = 100 * past / divisor
        return total - past

    def calculate_trend(self, key, base: Dict, origin: Dict):
        total = base[key]
        if not total:
            return 0
        return 100 * (total - origin[key]) / total

    @property
    def trend_30_all(self):
        return self.calculate_trend("all", self.current, self.past_30)

    @property
    def trend_30_all_words(self):
        return self.calculate_trend("all_words", self.current, self.past_30)

    @property
    def trend_30_contributors(self):
        return self.calculate_trend("contributors", self.current, self.past_30)

    @property
    def trend_30_translated_percent(self):
        return self.calculate_trend_percent(
            "translated", "all", self.current, self.past_30
        )

    @property
    def trend_60_all(self):
        return self.calculate_trend("all", self.past_30, self.past_60)

    @property
    def trend_60_all_words(self):
        return self.calculate_trend("all_words", self.past_30, self.past_60)

    @property
    def trend_60_contributors(self):
        return self.calculate_trend("contributors", self.past_30, self.past_60)

    @property
    def trend_60_translated_percent(self):
        return self.calculate_trend_percent(
            "translated", "all", self.past_30, self.past_60
        )


@register.filter
def metrics(obj):
    if isinstance(obj, Translation):
        return MetricsWrapper(Metric.SCOPE_TRANSLATION, obj.pk)
    if isinstance(obj, Component):
        return MetricsWrapper(Metric.SCOPE_COMPONENT, obj.pk)
    if isinstance(obj, Project):
        return MetricsWrapper(Metric.SCOPE_PROJECT, obj.pk)
    raise ValueError(f"Unsupported type for metrics: {obj!r}")
