from fastapi import APIRouter, HTTPException
import rpy2.robjects as robjects
from rpy2.rinterface_lib.embedded import RRuntimeError
from app.models import RCodeRequest
from app.utils.r_utils import process_r_output


router = APIRouter()


@router.post("/execute-r")
async def execute_r_code(request: RCodeRequest):
    try:
        # Execute the R code and capture the output
        raw_result = robjects.r(f"capture.output({request.code})")
        result = process_r_output(raw_result)
        return {"result": str(result)}
    except RRuntimeError as e:
        raise HTTPException(status_code=400, detail="Invalid R code")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
