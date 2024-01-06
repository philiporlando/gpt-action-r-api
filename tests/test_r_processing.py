import pytest
from app.utils.r_utils import process_r_output


def test_process_r_output():
    # Mock raw rpy2 output
    mock_r_output = ['[1] "Hello, R!"\n', '[1] "More text"\n']

    # Call the function with the mock output
    result = process_r_output(mock_r_output)

    # Expected result after processing
    expected_result = '"Hello, R!""More text"'

    # Assert that the processed output matches the expected result
    assert result == expected_result
