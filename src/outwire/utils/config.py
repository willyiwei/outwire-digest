from pydantic_settings import BaseSettings


class Config(BaseSettings):
    anthropic_api_key: str = ""
    substack_sid: str = ""
    gmail_username: str = ""
    gmail_app_password: str = ""
    dry_run: bool = False
    no_llm: bool = False
    no_email: bool = False
    top_n: int = 10
    min_score: int = 6
    publish_send_email: bool = True

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}
