from ninja import Schema

class SingInSchema(Schema):
    enrollment: str
    name: str
    password: str
    
class LoginSchema(Schema):
    enrollment: str
    password: str

class LoginResponseSchema(Schema):
    access_token: str