from pydantic import BaseModel


class RCodeRequest(BaseModel):
    code: str
