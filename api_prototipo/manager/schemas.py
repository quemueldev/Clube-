from ninja import Schema

class FormSchema(Schema):
    student_id : int
    name: str
    description: str

class UserResponseSchema(Schema):
    id: int
    enrollment: str
    first_name:str
    role:str

class IdSchema(Schema):
    id: int