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

from .copy_source import CopySource


class ServiceNowSource(CopySource):
    """A copy activity ServiceNow server source.

    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param type: Constant filled by server.
    :type type: str
    :param query: A query to retrieve data from source. Type: string (or
     Expression with resultType string).
    :type query: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'query': {'key': 'query', 'type': 'object'},
    }

    def __init__(self, source_retry_count=None, source_retry_wait=None, query=None):
        super(ServiceNowSource, self).__init__(source_retry_count=source_retry_count, source_retry_wait=source_retry_wait)
        self.query = query
        self.type = 'ServiceNowSource'
