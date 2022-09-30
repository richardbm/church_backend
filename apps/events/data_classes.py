from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class EventData:
    id: str
    title: str
    start: datetime
    end: datetime
    existed: bool
    event_id: int
    color: str
    cancelled: bool
    description: str = None
    rule: str = None
    end_recurring_period: datetime = None
    ministries: List = None
