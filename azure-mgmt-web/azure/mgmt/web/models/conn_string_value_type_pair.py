# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConnStringValueTypePair(Model):
    """Database connection string value to type pair.

    :param value: Value of pair.
    :type value: str
    :param type: Type of database. Possible values include: 'MySql',
     'SQLServer', 'SQLAzure', 'Custom', 'NotificationHub', 'ServiceBus',
     'EventHub', 'ApiHub', 'DocDb', 'RedisCache', 'PostgreSQL'
    :type type: str or ~azure.mgmt.web.models.ConnectionStringType
    """

    _validation = {
        'value': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ConnectionStringType'},
    }

    def __init__(self, value, type):
        self.value = value
        self.type = type
