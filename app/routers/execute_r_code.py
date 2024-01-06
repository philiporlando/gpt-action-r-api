from fastapi import APIRouter, HTTPException
from app.models import RCodeRequest
from app.utils.r_utils import run_r_code


router = APIRouter()


@router.post("/execute-r")
async def execute_r_route(request: RCodeRequest):
    try:
        stdout, stderr, result = run_r_code(request.code)
        if stderr:
            raise HTTPException(status_code=400, detail=stderr)
        return {"message": "R code executed successfully", "result": result[0]}
    except HTTPException as http_exception:
        raise http_exception  # Reraise the HTTPException with its original status code and detail
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
