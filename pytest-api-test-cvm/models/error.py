from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ErrorResponse(BaseModel):
    code: str
    description: str
    origin: Optional[str] = None
    timestamp: datetime
    data: Optional[str] = None
