valid_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "lat": {"type": "number"},
        "lon": {"type": "number"},
        "color": {"type": ["string", "null"]},
        "created_at": {"type": "string", "format": "data-time"}
    },
    "required": ["id", "title", "lat", "lon", "color", "created_at"]
}
error_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        'message': {"type": "string"}
    }
}
