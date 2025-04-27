from pydantic import BaseModel, validator


class WriteDataRequest(BaseModel):
    phone: str
    address: str

    @validator("phone")
    def validate_phone(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Phone number cannot be empty")
        if not (v.isdigit() and len(v) == 11 and v.startswith("8")):
            raise ValueError(
                'Phone must be exactly 11 digits, contain only numbers, and start with "8"'
            )
        return v
