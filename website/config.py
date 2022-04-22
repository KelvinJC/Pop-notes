from pydantic import BaseSettings

class Settings(BaseSettings):
    '''
    A pydantic model to help validate incoming environment variables.
    Pydantic is case insensitive
    '''
    database_name: str
    secret_key: str
    algorithm: str
    

    class Config:
        env_file=".env"



settings = Settings()