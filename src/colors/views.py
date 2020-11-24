from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from src.repo.serializers import ErrorSerializer
import src.repo.generic_view as gview
from .models import Color
from .serializers import ColorSerializer


@swagger_auto_schema(
    methods=["post"],
    request_body=ColorSerializer,
    responses={
        status.HTTP_400_BAD_REQUEST: ErrorSerializer(),
        status.HTTP_422_UNPROCESSABLE_ENTITY: ErrorSerializer(),
        status.HTTP_409_CONFLICT: ErrorSerializer(),
    },
)
@swagger_auto_schema(
    methods=["get", "delete"]
)
@api_view(["POST", "GET", "DELETE"])
def create_get_delete(request):
    """ create, get or delete a or all color(s)
    request: contains json data
    """
    return gview.create_get_delete(request, Color, ColorSerializer)


@swagger_auto_schema(
    methods=["delete", "get"],
    responses={
        status.HTTP_400_BAD_REQUEST: "Bad Request",
        status.HTTP_404_NOT_FOUND: "Not Found",
    },
)
@swagger_auto_schema(
    methods=["put", "patch"],
    request_body=ColorSerializer,
    responses={
        status.HTTP_400_BAD_REQUEST: "Bad Request"
    },
)
@api_view(['GET', 'PUT', 'DELETE', "PATCH"])
def operation_by_index(request, foreign_key):
    """ function called in http operations by index
    request: contains json data
    foreign_key: foreingh key id
    """
    return gview.operation_by_index(request, foreign_key,
                                    Color, ColorSerializer)
