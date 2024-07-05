"""Contains shared errors types that can be raised from API functions"""


class UnexpectedStatus(Exception):
    """Raised by api functions when the response status an undocumented status and Client.raise_on_unexpected_status is True"""

    def __init__(self, status_code: int, content: bytes):
        self.status_code = status_code
        self.content = content

        super().__init__(
            f"Unexpected status code: {status_code}\n\nResponse content:\n{content.decode(errors='ignore')}"
        )

class BadRequest(Exception):
    """Raised by api functions when the response status is 400"""

    def __init__(self, response):
        self.status_code = 400
        self.content = response

        super().__init__(
            f"Response content:\n{response}"
        )

class Unauthorized(Exception):
    """Raised by api functions when the response status is 401"""

    def __init__(self, response):
        self.status_code = 401
        super().__init__(response)

class InternalServerError(Exception):
    """Raised by api functions when the response status is 500"""

    def __init__(self, response):
        self.status_code = 500
        super().__init__(response)

__all__ = ["UnexpectedStatus", "BadRequest", "Unauthorized", "InternalServerError"]
