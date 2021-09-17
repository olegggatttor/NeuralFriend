from fastapi import APIRouter, HTTPException

from data_storages.params_storages import SimpleModelParamsChanger
from endpoints.get_queries import predictor

router = APIRouter(prefix='/change_inc')


@router.post("/")
async def change_inc(params: SimpleModelParamsChanger):
    try:
        predictor.set_value(params.inc)
        return "Thanks, {}! You set new inc value for model: {}. Your reversed message: {}".format(
            params.user_id, params.inc, params.message[::-1]
        )
    except ValueError as e:
        raise HTTPException(404, str(e))
