def validate(request_json):
    # validate request_json
    if 'person' not in request_json and 'driver' not in request_json:
        return False
    if 'vehicle' not in request_json:
        return False
    if 'coverage' not in request_json:
        return False
    return True

