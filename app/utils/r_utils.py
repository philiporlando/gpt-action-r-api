import rpy2.robjects as robjects
from rpy2.rinterface_lib.embedded import RRuntimeError
import contextlib
import io
from fastapi import HTTPException


def run_r_code(code):
    try:
        # Parse the R code
        parsed_code = robjects.r.parse(text=code)

        # Evaluate the parsed R code
        with io.StringIO() as stdout, io.StringIO() as stderr:
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = robjects.r.eval(parsed_code)

            output, error = stdout.getvalue(), stderr.getvalue()

        return output, error, result
    except RRuntimeError as e:
        raise HTTPException(status_code=400, detail="Invalid R code")
