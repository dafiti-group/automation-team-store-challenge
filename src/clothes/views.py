import logging
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import pandas as pd
from src.repo.serializers import ErrorSerializer
from src.repo.commons import create_data_to_bulk_insert
import src.repo.generic_view as gview
from .models import Clothes
from .serializers import ClothesSerializer

LOGGER = logging.getLogger(__name__)


@swagger_auto_schema(
    methods=["post"],
    request_body=ClothesSerializer,
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
    """ create, get or delete a or all promotional campaign(s)
    request: contains json data
    """
    return gview.create_get_delete(request, Clothes, ClothesSerializer)


@swagger_auto_schema(
    methods=["delete", "get"],
    responses={
        status.HTTP_400_BAD_REQUEST: "Bad Request",
        status.HTTP_404_NOT_FOUND: "Not Found",
    },
)
@swagger_auto_schema(
    methods=["put", "patch"],
    request_body=ClothesSerializer,
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
                                    Clothes,
                                    ClothesSerializer)


# pylint: disable=no-member
# pylint: disable=no-self-argument
# https://github.com/axnsan12/drf-yasg/issues/624
class FileUploadView(APIView):
    """ Class for urls that require file uploads
    Wasn't possible upload csv file in swagger because its feature
    not really supported with OpenApi
    https://github.com/axnsan12/drf-yasg/issues/624
    """
    @swagger_auto_schema(
        methods=["post"],
        request_body=openapi.Schema(
            name="file",
            in_="csv",
            type=openapi.TYPE_FILE,
            description="csv to bulk insert in clothes table"),
        responses={
            status.HTTP_400_BAD_REQUEST: ErrorSerializer(),
        },
    )
    @api_view(["POST"])
    def create_by_csv_file(request):
        """ make a bulk insert to create clothes by csv upload
        request: contains csv file instance
        """
        if request.method == "POST":
            LOGGER.info("Register clothes by csv file")
            file = BytesIO(request.FILES['file'].read())
            csv_content = pd.read_csv(file, delimiter=";", index_col=False)
            data = create_data_to_bulk_insert(csv_content)
            clothes_serializer = ClothesSerializer(data=data, many=True)
            if clothes_serializer.is_valid():
                clothes_serializer.save()
                LOGGER.info("Clothes by csv was created")
                return Response(clothes_serializer.data,
                                status=status.HTTP_201_CREATED)
            LOGGER.error("Some error occour: %s", clothes_serializer.errors)
            return Response(clothes_serializer.errors,
                            status.HTTP_400_BAD_REQUEST)
        LOGGER.error("Some error occour: %s")
        return Response(status.HTTP_400_BAD_REQUEST)
