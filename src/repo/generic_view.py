import logging
from typing import Callable
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .commons import treat_error_response_http

LOGGER = logging.getLogger(__name__)


def _get_entity_serializer(entity_serializer) -> Callable:
    """ get Entity Serializer if callable """
    if callable(entity_serializer):
        return entity_serializer
    return None


def _get_all(entity_model, entity_serializer, entity_name):
    """ get all entities from entity model table
    entity_model (model): entity model
    entity_serializer (serializer): entity serializer
    entity_name (str): entity table name
    """
    entity = entity_model.objects.all()
    serializer = entity_serializer(entity, many=True)
    return Response({entity_name: serializer.data})


def _register_entity(request, entity_serializer, entity_name):
    """ register entity in database
    request: request that contains data
    entity_serializer (serializer): entity serializer
    entity_name (str): entity table name
    """
    serializer = entity_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        LOGGER.info("Entity model %s was saved", entity_name)
        return JsonResponse(
            serializer.data, status=status.HTTP_201_CREATED
        )
    response = treat_error_response_http(serializer.errors)
    LOGGER.error("Request data %s is not valid because %s",
                 entity_name,
                 response)
    return JsonResponse(response["body"], status=response["status"])


def _update_entity(request, foreign_key, entity,
                   entity_serializer, entity_name):
    """ update entity by id
    request: request that contains data
    foreign_key (int): id of entity to be updated
    entity (model): entity model
    entity_serializer (serializer): entity serializer
    entity_name (str): entity table name
    """
    LOGGER.info("Start update entity %s which index is %s",
                entity_name, foreign_key)
    serializer = entity_serializer(
        entity, data=request.data, partial=request.method == "PATCH")
    if serializer.is_valid():
        serializer.save()
        LOGGER.info("Entity model %s was updated", entity_name)
        return Response({entity_name: serializer.data})
    LOGGER.error("Some error occour: %s", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_get_delete(request, entity_model, entity_serializer):
    """ create, get or delete a or all color(s) in db
    request: contains json data
    """
    entity_name = entity_model._meta.db_table.lower()

    entity_serializer = _get_entity_serializer(entity_serializer)
    if request.method == 'GET':
        LOGGER.info("Start get all %s", entity_name)
        return _get_all(entity_model, entity_serializer, entity_name)

    if request.method == "DELETE":
        entity_model.objects.all().delete()
        LOGGER.info("Start delete all %s", entity_name)
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "POST":
        return _register_entity(request,
                                entity_serializer,
                                entity_name)
    LOGGER.error("Some error occour")
    return Response(status.HTTP_400_BAD_REQUEST)


def operation_by_index(request, foreign_key, entity_model, entity_serializer):
    """ function called in http operations by index
    request: contains json data
    foreign_key: foreingh key id
    """
    try:
        entity_serializer = _get_entity_serializer(entity_serializer)

        entity = entity_model.objects.get(pk=foreign_key)
        entity_name = entity_model._meta.db_table.lower()

    except entity_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = entity_serializer(entity)
        LOGGER.info("Start get %s by index %s", entity_name, foreign_key)
        return Response({entity_name: serializer.data})

    if request.method in ['PUT', "PATCH"]:
        return _update_entity(request, foreign_key,
                              entity, entity_serializer,
                              entity_name)

    if request.method == 'DELETE':
        LOGGER.info("Start delete %s by index %s", entity_name, foreign_key)
        entity.delete()
        LOGGER.info("Entity model %s was deleted", entity_name)

        return Response(status=status.HTTP_204_NO_CONTENT)
    LOGGER.error("Some error occour")
    return Response(status=status.HTTP_400_BAD_REQUEST)
