from typing import Optional, Literal
from uuid import UUID
from pydantic import BaseModel, EmailStr, ConfigDict, Field, SecretStr

class SignupRequest(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=8)
    full_name: Optional[str] = Field(default=None, max_length=255)

    def normalized_email(self) -> str:
        return self.email.strip().lower()


class LoginRequest(BaseModel):
    email: EmailStr
    password: SecretStr

    def normalized_email(self) -> str:
        return self.email.strip().lower()


class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    full_name: Optional[str] = None
    auth_provider: Literal["local", "google", "local+google"]

    model_config = ConfigDict(from_attributes=True)
