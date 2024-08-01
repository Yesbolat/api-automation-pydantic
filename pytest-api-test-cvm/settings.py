from pydantic_settings import BaseSettings, SettingsConfigDict


class TestUser(BaseSettings):
    email: str = ""
    password: str = ""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    port: str
    stream: str
    domain: str
    subdomain: str
    admin_login: str
    admin_password: str
    pem_path: str

    @property
    def base_url(self) -> str:
        return f"https://{self.subdomain}{self.stream}.{self.domain}:{self.port}"

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'


base_settings = Settings()
