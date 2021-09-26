from fastapi import APIRouter, HTTPException

from data_storages.params_storages import SimpleModelParamsChanger
from endpoints.methods.post_methods import update_model

router = APIRouter(prefix='/change_inc')


@router.post("/")
async def change_inc(params: SimpleModelParamsChanger):
    try:
        return update_model(params.user_id, params.inc, params.message)
    except ValueError as e:
        raise HTTPException(404, str(e))
