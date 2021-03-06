# coding: utf-8

"""
    Ory Kratos

    Welcome to the ORY Kratos HTTP API documentation!  # noqa: E501

    The version of the OpenAPI document: v0.4.6-alpha.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_kratos_client.configuration import Configuration


class CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'request_id': 'str',
        'traits': 'object'
    }

    attribute_map = {
        'request_id': 'request_id',
        'traits': 'traits'
    }

    def __init__(self, request_id=None, traits=None, local_vars_configuration=None):  # noqa: E501
        """CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_id = None
        self._traits = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        self.traits = traits

    @property
    def request_id(self):
        """Gets the request_id of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.  # noqa: E501

        RequestID is request ID.  in: query  # noqa: E501

        :return: The request_id of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.

        RequestID is request ID.  in: query  # noqa: E501

        :param request_id: The request_id of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def traits(self):
        """Gets the traits of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.  # noqa: E501

        Traits contains all of the identity's traits.  type: string format: binary  # noqa: E501

        :return: The traits of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.  # noqa: E501
        :rtype: object
        """
        return self._traits

    @traits.setter
    def traits(self, traits):
        """Sets the traits of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.

        Traits contains all of the identity's traits.  type: string format: binary  # noqa: E501

        :param traits: The traits of this CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and traits is None:  # noqa: E501
            raise ValueError("Invalid value for `traits`, must not be `None`")  # noqa: E501

        self._traits = traits

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompleteSelfServiceBrowserSettingsStrategyProfileFlowPayload):
            return True

        return self.to_dict() != other.to_dict()
