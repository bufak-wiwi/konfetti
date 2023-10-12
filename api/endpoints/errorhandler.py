from fastapi import HTTPException, status


"""Error handler

Raises:
    HTTPException: Different HTTPstatuscodes depending on the error
"""
def errorhandler(exception):
    exception_type = type(exception)

    match (exception_type):
        case ValueError.__class__:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"")
        case KeyError.__class__:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"")
        case _:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An unexpected error occurred. Report this message to support: {exception}")