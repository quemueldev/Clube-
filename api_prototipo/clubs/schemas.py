from ninja import Schema
from datetime import datetime
from typing import List

class _UserSchema(Schema):
    id:int
    first_name:str
    enrollment:str

class ClubSchemaOut(Schema):
    id: int
    student: _UserSchema
    name: str
    description: str
    activity_days: list[str] | None
    created_at: datetime

class DescriptionSchemaIn(Schema):
    newDes: str

class DaysSchemaIn(Schema):
    days: List[str]