from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.location import Location


class ReportSubmittal(BaseModel):
    description: str
    location: Location


class Report(ReportSubmittal):
    id: str  # uuid
    created_date: Optional[datetime]
