
class InvalidToken(Exception):
    """token无效"""
    message = "Invalid token"


class EmptyToken(InvalidToken):
    """没有token"""
    message = "Empty token"


class ExpiredToken(InvalidToken):
    """token过期"""
    message = "Invalid token"
