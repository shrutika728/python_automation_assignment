from exceptions import APIValidationError


class ApiValidator:
  
    def validate_status_code(self, actual, expected):
        if actual != expected:
            raise APIValidationError(
                f"Status Code Mismatch: expected {expected}, got {actual}"
            )

    def validate_key_present(self, response_json, key):
        if key not in response_json:
            raise APIValidationError(
                f"Missing expected key in response: {key}"
            )

    def validate_response_time(self, actual_time, max_time):
        if actual_time > max_time:
            raise APIValidationError(
                f"Response time too high: {actual_time}s > {max_time}s"
            )  
    def validate_field_value(self, response_json, field, expected):
        actual = response_json.get(field)
        if actual != expected:
            raise APIValidationError(
                f"Field value mismatch for {field}: expected {expected}, got {actual}"
            )
    
