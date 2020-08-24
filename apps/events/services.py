import datetime
import uuid
from typing import Iterable
from datetime import timezone
from django.db.models import Q
from schedule.models import Event

from apps.events.data_classes import EventData
from apps.utils.datetime import get_naive_datetime


def get_event_occurrences(
    start: datetime, end: datetime, ministry_id: int
) -> Iterable[EventData]:
    start = get_naive_datetime(start)
    end = get_naive_datetime(end)
    events = Event.objects.all().prefetch_related("ministries")
    if ministry_id:
        events = events.filter(ministries__id=ministry_id)

    events = events.filter(start__lte=end.replace(tzinfo=timezone.utc)).filter(
        Q(end_recurring_period__gte=start.replace(tzinfo=timezone.utc))
        | Q(end_recurring_period__isnull=True)
    )

    for event in events:
        occurrences = event.get_occurrences(start, end)
        for occurrence in occurrences:
            if occurrence.event.end_recurring_period:
                recur_period_end = occurrence.event.end_recurring_period.replace(
                    tzinfo=timezone.utc
                )
            else:
                recur_period_end = None

            yield EventData(
                id=str(uuid.uuid4()),
                title=occurrence.title,
                start=occurrence.start.replace(tzinfo=timezone.utc),
                end=occurrence.end.replace(tzinfo=timezone.utc),
                existed=True if occurrence.id else False,
                event_id=occurrence.event.id,
                color=occurrence.event.color_event,
                description=occurrence.description,
                rule=occurrence.event.rule.name if occurrence.event.rule else None,
                end_recurring_period=recur_period_end,
                ministries=list(event.ministries.all()),
                cancelled=occurrence.cancelled,
            )
