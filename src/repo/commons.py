import logging
from rest_framework import status

LOGGER = logging.getLogger(__name__)


def treat_error_response_http(errors):
    """ Responsible by treat erros to appropriate http response """
    LOGGER.info("Start treat error fot http response")
    errors_type = []
    fields_with_error = [*errors]
    for field in fields_with_error:
        errors_type.append(errors[field][0].__dict__["code"])
    if "unique" in errors_type:
        return {"body": errors, "status": status.HTTP_409_CONFLICT}
    if ("null" in errors_type or
            "invalid" in errors_type or
            "min_value" in errors_type):
        return {"body": errors, "status": status.HTTP_422_UNPROCESSABLE_ENTITY}
    if "required" in errors_type:
        return {"body": errors, "status": status.HTTP_412_PRECONDITION_FAILED}
    return {"body": errors, "status": status.HTTP_400_BAD_REQUEST}


def create_data_to_bulk_insert(csv_content):
    """ csv_content: pandas dataframe
    return list of data to bulk insert
    """
    LOGGER.info("Start create data to bulk insert")
    each_data = {}
    bulk_data = []
    for index in range(len(csv_content[[*csv_content][0]])):
        for key in csv_content.keys():
            each_data.update({key: csv_content[key][index]})
        bulk_data.append(each_data)
        each_data = {}
    return bulk_data
