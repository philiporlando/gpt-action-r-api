import pytest
from fastapi import HTTPException
from app.utils.r_utils import run_r_code


def test_run_r_code_success():
    stdout, stderr, result = run_r_code("2 + 2")
    assert result[0] == 4, "The result is not equal to 4"


def test_run_r_code_failure():
    with pytest.raises(HTTPException) as exc_info:
        # Attempt to run invalid R code
        run_r_code("invalid R code")

    # Check the raised exception
    exception = exc_info.value
    assert exception.status_code == 400
    assert exception.detail == "Invalid R code"


def test_run_r_code_with_package():
    # Test R code that uses a specific package
    result = run_r_code("library(ggplot2); ggplot2::qplot(1:10, 1:10)")
    # Assert based on the expected result of the R code
    # ...
