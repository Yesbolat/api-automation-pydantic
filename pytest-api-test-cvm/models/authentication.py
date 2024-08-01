from pydantic import BaseModel, Field, model_validator
from settings import base_settings


class AdminAuthUser(BaseModel):
    username: str = Field(default=base_settings.admin_login)
    password: str = Field(default=base_settings.admin_password)


class Authentication(BaseModel):
    auth_token: str | None = None
    user: AdminAuthUser | None = None

    @model_validator(mode='after')
    def validate_root(self) -> 'Authentication':
        if (not self.auth_token) and (not self.user):
            raise ValueError(
                'Please provide "username" and "password" or "auth_token"'
            )

        return self
