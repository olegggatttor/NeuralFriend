from pydantic import BaseModel


class SimpleModelParamsChanger(BaseModel):
    user_id: int
    inc: int
    message: str
