import pytest
from fastapi import HTTPException
import rpy2.robjects as robjects
from app.utils.r_utils import run_r_code


def test_run_r_code_success():
    stdout, stderr, result = run_r_code("2 + 2")
    assert result[0] == 4, "The result is not equal to 4"


def test_run_r_code_failure():
    with pytest.raises(HTTPException) as exc_info:
        # Attempt to run invalid R code
        run_r_code("import this")

    # Check the raised exception
    exception = exc_info.value
    assert exception.status_code == 400
    assert exception.detail == "Invalid R code"


def test_run_r_code_with_package():
    # Test R code that uses a specific package
    stdout, stderr, result = run_r_code(
        "library(dplyr); data(mtcars); mtcars %>% group_by(mpg)"
    )
    # Assert based on the expected result of the R code
    r_class = robjects.r["class"](result)[0]
    assert r_class == "grouped_df"
