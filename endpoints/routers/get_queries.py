from fastapi import APIRouter, Path
from endpoints.methods.get_methods import format_prediction_message, get_prediction

router = APIRouter(prefix='/get')


@router.get("/")
async def get(x: int = 0):
    return format_prediction_message(x, get_prediction(x))


@router.get("/{x}")
async def get(x: int = Path(0)):
    return format_prediction_message(x, get_prediction(x))
