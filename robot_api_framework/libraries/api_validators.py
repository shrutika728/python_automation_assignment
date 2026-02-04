from exceptions import APIValidationError


def validate_status_code(actual, expected):
    """Validate status code of response.

    Accepts either a requests.Response object or a raw status code.
    """
    actual_status = actual
    if hasattr(actual, "status_code"):
        actual_status = actual.status_code
    elif hasattr(actual, "status"):
        actual_status = actual.status

    try:
        expected_int = int(expected)
    except Exception:
        expected_int = expected

    if actual_status != expected_int:
        raise APIValidationError(
            f"Status Code Mismatch: expected {expected_int}, got {actual_status}"
        )


def validate_key_present(response, *args):
    """Validate that a key is present in the response JSON.

    Usage:
    - validate_key_present(response, key)
    - validate_key_present(response, index, key)  # for list responses
    """
    if hasattr(response, "json") and callable(response.json):
        resp_json = response.json()
    else:
        resp_json = response

    if len(args) == 1:
        key = args[0]
        if isinstance(resp_json, dict):
            if key not in resp_json:
                raise APIValidationError(f"Missing expected key in response: {key}")
        else:
            if not any(isinstance(item, dict) and key in item for item in resp_json):
                raise APIValidationError(f"Missing expected key in response list: {key}")
    elif len(args) == 2:
        index, key = args
        try:
            index = int(index)
        except Exception:
            raise APIValidationError(f"Invalid index provided for response list: {index}")
        try:
            item = resp_json[index]
        except Exception:
            raise APIValidationError(f"Response list has no item at index {index}")
        if not isinstance(item, dict) or key not in item:
            raise APIValidationError(f"Missing expected key in response item at index {index}: {key}")
    else:
        raise APIValidationError("validate_key_present expects 2 or 3 arguments: response, [index], key")


def validate_response_time(actual_time, max_time):
    if actual_time > max_time:
        raise APIValidationError(
            f"Response time too high: {actual_time}s > {max_time}s"
        )


def validate_field_value(response_json, field, expected):
    actual = response_json.get(field)
    if actual != expected:
        raise APIValidationError(
            f"Field value mismatch for {field}: expected {expected}, got {actual}"
        )
