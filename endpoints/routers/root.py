from fastapi import APIRouter
from endpoints.methods.get_methods import get_root_message

router = APIRouter()


@router.get("/root")
async def root():
    return {"message": get_root_message()}
