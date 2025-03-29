import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.etsi_qkd_sdn_node_qkd_node_get200_response import EtsiQkdSdnNodeQkdNodeGet200Response  # noqa: E501
from openapi_server.models.etsi_qkd_sdn_node_qkd_node_put_request import EtsiQkdSdnNodeQkdNodePutRequest  # noqa: E501
from openapi_server import util


def etsi_qkd_sdn_node_qkd_node_get():  # noqa: E501
    """View detail on qkd_node

    Top module describing a software-defined QKD node (SD-QKD node). # noqa: E501


    :rtype: Union[EtsiQkdSdnNodeQkdNodeGet200Response, Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int], Tuple[EtsiQkdSdnNodeQkdNodeGet200Response, int, Dict[str, str]]
    """
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
