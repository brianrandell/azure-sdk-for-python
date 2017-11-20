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

from .linked_service import LinkedService


class QuickBooksLinkedService(LinkedService):
    """QuickBooks server linked service.

    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param endpoint: The endpoint of the QuickBooks server. (i.e.
     quickbooks.api.intuit.com)
    :type endpoint: object
    :param company_id: The company ID of the QuickBooks company to authorize.
    :type company_id: object
    :param access_token: The access token for OAuth 1.0 authentication.
    :type access_token: ~azure.mgmt.datafactory.models.SecretBase
    :param access_token_secret: The access token secret for OAuth 1.0
     authentication.
    :type access_token_secret: ~azure.mgmt.datafactory.models.SecretBase
    :param use_encrypted_endpoints: Specifies whether the data source
     endpoints are encrypted using HTTPS. The default value is true.
    :type use_encrypted_endpoints: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'endpoint': {'required': True},
        'company_id': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'endpoint': {'key': 'typeProperties.endpoint', 'type': 'object'},
        'company_id': {'key': 'typeProperties.companyId', 'type': 'object'},
        'access_token': {'key': 'typeProperties.accessToken', 'type': 'SecretBase'},
        'access_token_secret': {'key': 'typeProperties.accessTokenSecret', 'type': 'SecretBase'},
        'use_encrypted_endpoints': {'key': 'typeProperties.useEncryptedEndpoints', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, endpoint, company_id, connect_via=None, description=None, access_token=None, access_token_secret=None, use_encrypted_endpoints=None, encrypted_credential=None):
        super(QuickBooksLinkedService, self).__init__(connect_via=connect_via, description=description)
        self.endpoint = endpoint
        self.company_id = company_id
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.use_encrypted_endpoints = use_encrypted_endpoints
        self.encrypted_credential = encrypted_credential
        self.type = 'QuickBooks'
