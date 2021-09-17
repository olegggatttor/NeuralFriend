from fastapi import APIRouter, Path

from model.simple_model import SimpleModel

router = APIRouter(prefix='/get')
predictor = SimpleModel()


@router.get("/")
async def get(x: int = 0):
    return 'Predicted y={} for x={}'.format(predictor.predict(x), x)


@router.get("/{x}")
async def get(x: int = Path(0)):
    return 'Predicted y={} for x={}'.format(predictor.predict(x), x)
