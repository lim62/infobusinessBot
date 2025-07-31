from pydantic import BaseModel
from environs import Env

class BotConfig(BaseModel):
    TOKEN: str
    ADMINS_IDS: list[int]

class LogConfig(BaseModel):
    LEVEL: str
    FORMAT: str

class RedisConfig(BaseModel):
    HOST: str
    PORT: int

class Config(BaseModel):
    bot: BotConfig
    log: LogConfig
    redis: RedisConfig

def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path, override=True)
    return Config(
        bot=BotConfig(
            TOKEN=env('TOKEN'),
            ADMINS_IDS=env.list('ADMINS_IDS')  
        ),
        log=LogConfig(
            LEVEL=env('LEVEL'),
            FORMAT=env('FORMAT')
        ),
        redis=RedisConfig(
            HOST=env('REDIS_HOST'),
            PORT=env.int('REDIS_PORT')
        )
    )