from pydantic import BaseModel, field_validator


class ContactMessageCreateSchema(BaseModel):
    name: str
    message: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, val):
        if "mitko" in str(val).lower():
            raise ValueError("mitko is not allowed")
        return val
