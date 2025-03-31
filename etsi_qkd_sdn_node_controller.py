import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.errorallofschema import ERRORALLOFSCHEMA  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_get200_response import EtsiQkdSdnNodeQkdNodeGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_put_request import EtsiQkdSdnNodeQkdNodePutRequest  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_applications_get200_response import EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_qos_get200_response import EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_get200_response import EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_end_time_get200_response import EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_get200_response import EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_interfaces_get200_response import EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_get200_response import EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_att_point_get200_response import EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_capabilities_get200_response import EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_links_get200_response import EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_get200_response import EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_put_request import EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdPutRequest  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_local_get200_response import EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_performance_get200_response import EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_remote_get200_response import EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_qkdn_capabilities_get200_response import EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def etsi_qkd_sdn_node_qkd_node_delete():  # noqa: E501
    """Delete qkd_node from etsi-qkd-sdn-node

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_get():  # noqa: E501
    """View detail on qkd_node

    Top module describing a software-defined QKD node (SD-QKD node). # noqa: E501


    :rtype: Union[EtsiQkdSdnNodeQkdNodeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_patch(body=None):  # noqa: E501
    """Merge details on qkd_node

     # noqa: E501

    :param qkd_node: Top module describing a software-defined QKD node (SD-QKD node).
    :type qkd_node: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int, Dict[str, str]]
    """
    qkd_node = body
    if connexion.request.is_json:
        qkd_node = EtsiQkdSdnNodeQkdNodePutRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_put(body=None):  # noqa: E501
    """Update details on qkd_node

     # noqa: E501

    :param qkd_node: Top module describing a software-defined QKD node (SD-QKD node).
    :type qkd_node: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int, Dict[str, str]]
    """
    qkd_node = body
    if connexion.request.is_json:
        qkd_node = EtsiQkdSdnNodeQkdNodePutRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_delete():  # noqa: E501
    """Delete qkd_applications from qkd_node

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_get():  # noqa: E501
    """View detail on qkd_applications

    List of applications container. # noqa: E501


    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_patch(body=None):  # noqa: E501
    """Merge details on qkd_applications

     # noqa: E501

    :param qkd_applications: List of applications container.
    :type qkd_applications: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, int, Dict[str, str]]
    """
    qkd_applications = body
    if connexion.request.is_json:
        qkd_applications = EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_put(body=None):  # noqa: E501
    """Update details on qkd_applications

     # noqa: E501

    :param qkd_applications: List of applications container.
    :type qkd_applications: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response, int, Dict[str, str]]
    """
    qkd_applications = body
    if connexion.request.is_json:
        qkd_applications = EtsiQkdSdnNodeQkdNodeQkdApplicationsGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_qos_delete(app_id):  # noqa: E501
    """Delete app_qos from qkd_app

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_qos_get(app_id):  # noqa: E501
    """View detail on app_qos

    Requested Quality of Service. # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_qos_patch(app_id, body=None):  # noqa: E501
    """Merge details on app_qos

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param app_qos: Requested Quality of Service.
    :type app_qos: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, int, Dict[str, str]]
    """
    app_qos = body
    if connexion.request.is_json:
        app_qos = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_qos_put(app_id, body=None):  # noqa: E501
    """Update details on app_qos

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param app_qos: Requested Quality of Service.
    :type app_qos: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response, int, Dict[str, str]]
    """
    app_qos = body
    if connexion.request.is_json:
        app_qos = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppQosGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_delete(app_id):  # noqa: E501
    """Delete app_statistics from qkd_app

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_get(app_id):  # noqa: E501
    """View detail on app_statistics

    Statistical information relating to a specific statistic period of time. # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_patch(app_id, body=None):  # noqa: E501
    """Merge details on app_statistics

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param app_statistics: Statistical information relating to a specific statistic period of time.
    :type app_statistics: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, int, Dict[str, str]]
    """
    app_statistics = body
    if connexion.request.is_json:
        app_statistics = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_put(app_id, body=None):  # noqa: E501
    """Update details on app_statistics

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param app_statistics: Statistical information relating to a specific statistic period of time.
    :type app_statistics: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response, int, Dict[str, str]]
    """
    app_statistics = body
    if connexion.request.is_json:
        app_statistics = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_end_time_delete(end_time, app_id):  # noqa: E501
    """Delete statistics from app_statistics

     # noqa: E501

    :param end_time: End time for the statistic period.
    :type end_time: str
    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_end_time_get(end_time, app_id):  # noqa: E501
    """View detail on statistics

    List of statistics. # noqa: E501

    :param end_time: End time for the statistic period.
    :type end_time: str
    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_end_time_patch(end_time, app_id, body=None):  # noqa: E501
    """Merge details on statistics

     # noqa: E501

    :param end_time: End time for the statistic period.
    :type end_time: str
    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param statistics: List of statistics.
    :type statistics: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, int, Dict[str, str]]
    """
    statistics = body
    if connexion.request.is_json:
        statistics = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_end_time_put(end_time, app_id, body=None):  # noqa: E501
    """Update details on statistics

     # noqa: E501

    :param end_time: End time for the statistic period.
    :type end_time: str
    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param statistics: List of statistics.
    :type statistics: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response, int, Dict[str, str]]
    """
    statistics = body
    if connexion.request.is_json:
        statistics = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdAppStatisticsStatisticsEndTimeGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_get(app_id):  # noqa: E501
    """List all statisticss from app_statistics

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_patch(app_id, body=None):  # noqa: E501
    """Merge items into the statistics collection

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param statistics: List of statistics.
    :type statistics: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    statistics = body
    if connexion.request.is_json:
        statistics = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_post(app_id, body=None):  # noqa: E501
    """Creates one or more new statistics in app_statistics

    List of statistics. # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param statistics: List of statistics.
    :type statistics: dict | bytes

    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    statistics = body
    if connexion.request.is_json:
        statistics = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_app_statistics_statistics_put(app_id, body=None):  # noqa: E501
    """Replace the entire statistics collection

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param statistics: List of statistics.
    :type statistics: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    statistics = body
    if connexion.request.is_json:
        statistics = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_delete(app_id):  # noqa: E501
    """Delete qkd_app from qkd_applications

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_get(app_id):  # noqa: E501
    """View detail on qkd_app

    List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application. # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_patch(app_id, body=None):  # noqa: E501
    """Merge details on qkd_app

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param qkd_app: List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application.
    :type qkd_app: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, int, Dict[str, str]]
    """
    qkd_app = body
    if connexion.request.is_json:
        qkd_app = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_app_id_put(app_id, body=None):  # noqa: E501
    """Update details on qkd_app

     # noqa: E501

    :param app_id: Unique ID that identifies a QKD application consisting of a set of entities that are allowed to receive keys shared with each other from the SD-QKD nodes they connect to. This value is similar to a key ID or key handle.
    :type app_id: str
    :param qkd_app: List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application.
    :type qkd_app: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response, int, Dict[str, str]]
    """
    qkd_app = body
    if connexion.request.is_json:
        qkd_app = EtsiQkdSdnNodeQkdNodeQkdApplicationsQkdAppAppIdGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_get():  # noqa: E501
    """List all qkd_apps from qkd_applications

     # noqa: E501


    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_patch(body=None):  # noqa: E501
    """Merge items into the qkd_app collection

     # noqa: E501

    :param qkd_app: List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application.
    :type qkd_app: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    qkd_app = body
    if connexion.request.is_json:
        qkd_app = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_post(body=None):  # noqa: E501
    """Creates one or more new qkd_app in qkd_applications

    List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application. # noqa: E501

    :param qkd_app: List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application.
    :type qkd_app: dict | bytes

    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    qkd_app = body
    if connexion.request.is_json:
        qkd_app = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_applications_qkd_app_put(body=None):  # noqa: E501
    """Replace the entire qkd_app collection

     # noqa: E501

    :param qkd_app: List of applications that are currently registered in the SD-QKD node. Any entity consuming QKD-derived keys (either for internal or external purposes) is considered an application.
    :type qkd_app: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    qkd_app = body
    if connexion.request.is_json:
        qkd_app = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_delete():  # noqa: E501
    """Delete qkd_interfaces from qkd_node

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_get():  # noqa: E501
    """View detail on qkd_interfaces

    List of interfaces container. # noqa: E501


    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_patch(body=None):  # noqa: E501
    """Merge details on qkd_interfaces

     # noqa: E501

    :param qkd_interfaces: List of interfaces container.
    :type qkd_interfaces: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, int, Dict[str, str]]
    """
    qkd_interfaces = body
    if connexion.request.is_json:
        qkd_interfaces = EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_put(body=None):  # noqa: E501
    """Update details on qkd_interfaces

     # noqa: E501

    :param qkd_interfaces: List of interfaces container.
    :type qkd_interfaces: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response, int, Dict[str, str]]
    """
    qkd_interfaces = body
    if connexion.request.is_json:
        qkd_interfaces = EtsiQkdSdnNodeQkdNodeQkdInterfacesGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_get():  # noqa: E501
    """List all qkd_interfaces from qkd_interfaces

     # noqa: E501


    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_patch(body=None):  # noqa: E501
    """Merge items into the qkd_interface collection

     # noqa: E501

    :param qkd_interface: List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node.
    :type qkd_interface: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    qkd_interface = body
    if connexion.request.is_json:
        qkd_interface = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_post(body=None):  # noqa: E501
    """Creates one or more new qkd_interface in qkd_interfaces

    List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node. # noqa: E501

    :param qkd_interface: List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node.
    :type qkd_interface: dict | bytes

    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    qkd_interface = body
    if connexion.request.is_json:
        qkd_interface = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_put(body=None):  # noqa: E501
    """Replace the entire qkd_interface collection

     # noqa: E501

    :param qkd_interface: List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node.
    :type qkd_interface: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    qkd_interface = body
    if connexion.request.is_json:
        qkd_interface = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_delete(qkdi_id):  # noqa: E501
    """Delete qkd_interface from qkd_interfaces

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_get(qkdi_id):  # noqa: E501
    """View detail on qkd_interface

    List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node. # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_patch(qkdi_id, body=None):  # noqa: E501
    """Merge details on qkd_interface

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int
    :param qkd_interface: List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node.
    :type qkd_interface: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, int, Dict[str, str]]
    """
    qkd_interface = body
    if connexion.request.is_json:
        qkd_interface = EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_put(qkdi_id, body=None):  # noqa: E501
    """Update details on qkd_interface

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int
    :param qkd_interface: List of physical QKD modules in a secure location, abstracted as interfaces of the SD-QKD node.
    :type qkd_interface: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response, int, Dict[str, str]]
    """
    qkd_interface = body
    if connexion.request.is_json:
        qkd_interface = EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_att_point_delete(qkdi_id):  # noqa: E501
    """Delete qkdi_att_point from qkd_interface

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_att_point_get(qkdi_id):  # noqa: E501
    """View detail on qkdi_att_point

    Interface attachment point to an optical switch. # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_att_point_patch(qkdi_id, body=None):  # noqa: E501
    """Merge details on qkdi_att_point

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int
    :param qkdi_att_point: Interface attachment point to an optical switch.
    :type qkdi_att_point: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, int, Dict[str, str]]
    """
    qkdi_att_point = body
    if connexion.request.is_json:
        qkdi_att_point = EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_att_point_put(qkdi_id, body=None):  # noqa: E501
    """Update details on qkdi_att_point

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int
    :param qkdi_att_point: Interface attachment point to an optical switch.
    :type qkdi_att_point: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response, int, Dict[str, str]]
    """
    qkdi_att_point = body
    if connexion.request.is_json:
        qkdi_att_point = EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiAttPointGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_capabilities_delete(qkdi_id):  # noqa: E501
    """Delete qkdi_capabilities from qkd_interface

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_capabilities_get(qkdi_id):  # noqa: E501
    """View detail on qkdi_capabilities

    Capabilities of the QKD system (interface). # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_capabilities_patch(qkdi_id, body=None):  # noqa: E501
    """Merge details on qkdi_capabilities

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int
    :param qkdi_capabilities: Capabilities of the QKD system (interface).
    :type qkdi_capabilities: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, int, Dict[str, str]]
    """
    qkdi_capabilities = body
    if connexion.request.is_json:
        qkdi_capabilities = EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_interfaces_qkd_interface_qkdi_id_qkdi_capabilities_put(qkdi_id, body=None):  # noqa: E501
    """Update details on qkdi_capabilities

     # noqa: E501

    :param qkdi_id: Interface id. It is described as a locally unique number, which is globally unique when combined with the SD-QKD node ID.
    :type qkdi_id: int
    :param qkdi_capabilities: Capabilities of the QKD system (interface).
    :type qkdi_capabilities: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response, int, Dict[str, str]]
    """
    qkdi_capabilities = body
    if connexion.request.is_json:
        qkdi_capabilities = EtsiQkdSdnNodeQkdNodeQkdInterfacesQkdInterfaceQkdiIdQkdiCapabilitiesGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_delete():  # noqa: E501
    """Delete qkd_links from qkd_node

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_get():  # noqa: E501
    """View detail on qkd_links

    List of links container # noqa: E501


    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_patch(body=None):  # noqa: E501
    """Merge details on qkd_links

     # noqa: E501

    :param qkd_links: List of links container
    :type qkd_links: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, int, Dict[str, str]]
    """
    qkd_links = body
    if connexion.request.is_json:
        qkd_links = EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_put(body=None):  # noqa: E501
    """Update details on qkd_links

     # noqa: E501

    :param qkd_links: List of links container
    :type qkd_links: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response, int, Dict[str, str]]
    """
    qkd_links = body
    if connexion.request.is_json:
        qkd_links = EtsiQkdSdnNodeQkdNodeQkdLinksGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_get():  # noqa: E501
    """List all qkd_links from qkd_links

     # noqa: E501


    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_patch(body=None):  # noqa: E501
    """Merge items into the qkd_link collection

     # noqa: E501

    :param qkd_link: List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes.
    :type qkd_link: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    qkd_link = body
    if connexion.request.is_json:
        qkd_link = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_post(body=None):  # noqa: E501
    """Creates one or more new qkd_link in qkd_links

    List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes. # noqa: E501

    :param qkd_link: List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes.
    :type qkd_link: dict | bytes

    :rtype: Union[ERRORALLOFSCHEMA, Tuple[ERRORALLOFSCHEMA, int], Tuple[ERRORALLOFSCHEMA, int, Dict[str, str]]
    """
    qkd_link = body
    if connexion.request.is_json:
        qkd_link = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_put(body=None):  # noqa: E501
    """Replace the entire qkd_link collection

     # noqa: E501

    :param qkd_link: List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes.
    :type qkd_link: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    qkd_link = body
    if connexion.request.is_json:
        qkd_link = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_delete(qkdl_id):  # noqa: E501
    """Delete qkd_link from qkd_links

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_get(qkdl_id):  # noqa: E501
    """View detail on qkd_link

    List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes. # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_patch(qkdl_id, body=None):  # noqa: E501
    """Merge details on qkd_link

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkd_link: List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes.
    :type qkd_link: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, int, Dict[str, str]]
    """
    qkd_link = body
    if connexion.request.is_json:
        qkd_link = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdPutRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_put(qkdl_id, body=None):  # noqa: E501
    """Update details on qkd_link

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkd_link: List of (key association) links to other SD-QKD nodes in the network. The links can be physical (direct quantum channel) or virtual multi-hop connection doing key-relay through several nodes.
    :type qkd_link: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdGet200Response, int, Dict[str, str]]
    """
    qkd_link = body
    if connexion.request.is_json:
        qkd_link = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdPutRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_local_delete(qkdl_id):  # noqa: E501
    """Delete qkdl_local from qkd_link

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_local_get(qkdl_id):  # noqa: E501
    """View detail on qkdl_local

    Source (local) node of the SD-QKD link. # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_local_patch(qkdl_id, body=None):  # noqa: E501
    """Merge details on qkdl_local

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkdl_local: Source (local) node of the SD-QKD link.
    :type qkdl_local: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, int, Dict[str, str]]
    """
    qkdl_local = body
    if connexion.request.is_json:
        qkdl_local = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_local_put(qkdl_id, body=None):  # noqa: E501
    """Update details on qkdl_local

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkdl_local: Source (local) node of the SD-QKD link.
    :type qkdl_local: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response, int, Dict[str, str]]
    """
    qkdl_local = body
    if connexion.request.is_json:
        qkdl_local = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlLocalGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_performance_delete(qkdl_id):  # noqa: E501
    """Delete qkdl_performance from qkd_link

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_performance_get(qkdl_id):  # noqa: E501
    """View detail on qkdl_performance

    Container of link&#39;s performace parameters. # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_performance_patch(qkdl_id, body=None):  # noqa: E501
    """Merge details on qkdl_performance

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkdl_performance: Container of link&#39;s performace parameters.
    :type qkdl_performance: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, int, Dict[str, str]]
    """
    qkdl_performance = body
    if connexion.request.is_json:
        qkdl_performance = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_performance_put(qkdl_id, body=None):  # noqa: E501
    """Update details on qkdl_performance

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkdl_performance: Container of link&#39;s performace parameters.
    :type qkdl_performance: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response, int, Dict[str, str]]
    """
    qkdl_performance = body
    if connexion.request.is_json:
        qkdl_performance = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlPerformanceGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_remote_delete(qkdl_id):  # noqa: E501
    """Delete qkdl_remote from qkd_link

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_remote_get(qkdl_id):  # noqa: E501
    """View detail on qkdl_remote

    Destination (remote) unique SD-QKD node. # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_remote_patch(qkdl_id, body=None):  # noqa: E501
    """Merge details on qkdl_remote

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkdl_remote: Destination (remote) unique SD-QKD node.
    :type qkdl_remote: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, int, Dict[str, str]]
    """
    qkdl_remote = body
    if connexion.request.is_json:
        qkdl_remote = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkd_links_qkd_link_qkdl_id_qkdl_remote_put(qkdl_id, body=None):  # noqa: E501
    """Update details on qkdl_remote

     # noqa: E501

    :param qkdl_id: Unique ID of the QKD link (key association).
    :type qkdl_id: str
    :param qkdl_remote: Destination (remote) unique SD-QKD node.
    :type qkdl_remote: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response, int, Dict[str, str]]
    """
    qkdl_remote = body
    if connexion.request.is_json:
        qkdl_remote = EtsiQkdSdnNodeQkdNodeQkdLinksQkdLinkQkdlIdQkdlRemoteGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkdn_capabilities_delete():  # noqa: E501
    """Delete qkdn_capabilities from qkd_node

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkdn_capabilities_get():  # noqa: E501
    """View detail on qkdn_capabilities

    Capabilities of the SD-QKD node. # noqa: E501


    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkdn_capabilities_patch(body=None):  # noqa: E501
    """Merge details on qkdn_capabilities

     # noqa: E501

    :param qkdn_capabilities: Capabilities of the SD-QKD node.
    :type qkdn_capabilities: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, int, Dict[str, str]]
    """
    qkdn_capabilities = body
    if connexion.request.is_json:
        qkdn_capabilities = EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def etsi_qkd_sdn_node_qkd_node_qkdn_capabilities_put(body=None):  # noqa: E501
    """Update details on qkdn_capabilities

     # noqa: E501

    :param qkdn_capabilities: Capabilities of the SD-QKD node.
    :type qkdn_capabilities: dict | bytes

    :rtype: Union[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response, int, Dict[str, str]]
    """
    qkdn_capabilities = body
    if connexion.request.is_json:
        qkdn_capabilities = EtsiQkdSdnNodeQkdNodeQkdnCapabilitiesGet200Response.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
