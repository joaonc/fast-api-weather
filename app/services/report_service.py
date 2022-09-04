import uuid
from datetime import datetime
from typing import List

from app.models.location import Location
from app.models.report import Report

__reports: List[Report] = []


async def get_reports() -> List[Report]:
    # Would be an async call here
    return __reports.copy()


async def add_report(description: str, location: Location) -> Report:
    now = datetime.now()
    report = Report(
        id=str(uuid.uuid4()), description=description, location=location, created_date=now
    )

    # Simulate saving to DB
    # Would be an async call here
    __reports.append(report)

    __reports.sort(key=lambda x: x.created_date, reverse=True)

    return report
