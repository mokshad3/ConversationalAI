class CustomResponse:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return {
            "status": 200,
            "message": "",
            "success": True,
            "data": self.data,
            "errorCode": "",
            "stackTrace": ""
        }
