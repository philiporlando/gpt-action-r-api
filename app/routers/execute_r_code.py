from fastapi import APIRouter, HTTPException
from app.models import RCodeRequest
import rpy2.robjects as robjects
from rpy2.rinterface_lib.embedded import RRuntimeError


router = APIRouter()


@router.post("/execute-r")
async def execute_r_code(request: RCodeRequest):
    try:
        # Execute the R code
        robjects.r(request.code)
        return {"message": "R code executed successfully"}
    except RRuntimeError as e:
        # Handle R runtime errors specifically
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle other errors more generally
        raise HTTPException(status_code=400, detail="Invalid R code")
