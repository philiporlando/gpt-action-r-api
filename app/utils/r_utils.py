def process_r_output(raw_result):
    """
    Process the raw output from rpy2, removing the R output index and formatting it into a readable string.

    :param raw_result: The raw output from rpy2 execution.
    :return: Formatted string.
    """
    # Join the output, remove R index [1], extra quotes, and newlines
    formatted_result = "".join(raw_result)
    formatted_result = formatted_result.replace("[1] ", "").replace('\\"', '"').strip()

    return formatted_result
