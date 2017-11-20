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


class ServiceNowLinkedService(LinkedService):
    """ServiceNow server linked service.

    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param endpoint: The endpoint of the ServiceNow server. (i.e.
     ServiceNowData.com)
    :type endpoint: object
    :param authentication_type: The authentication type to use. Possible
     values include: 'Basic', 'OAuth2'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.ServiceNowAuthenticationType
    :param username: The user name used to connect to the ServiceNow server
     for Basic and OAuth2 authentication.
    :type username: object
    :param password: The password corresponding to the user name for Basic and
     OAuth2 authentication.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param client_id: The client id for OAuth2 authentication.
    :type client_id: object
    :param client_secret: The client secret for OAuth2 authentication.
    :type client_secret: ~azure.mgmt.datafactory.models.SecretBase
    :param use_encrypted_endpoints: Specifies whether the data source
     endpoints are encrypted using HTTPS. The default value is true.
    :type use_encrypted_endpoints: object
    :param use_host_verification: Specifies whether to require the host name
     in the server's certificate to match the host name of the server when
     connecting over SSL. The default value is true.
    :type use_host_verification: object
    :param use_peer_verification: Specifies whether to verify the identity of
     the server when connecting over SSL. The default value is true.
    :type use_peer_verification: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'endpoint': {'required': True},
        'authentication_type': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'endpoint': {'key': 'typeProperties.endpoint', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'client_id': {'key': 'typeProperties.clientId', 'type': 'object'},
        'client_secret': {'key': 'typeProperties.clientSecret', 'type': 'SecretBase'},
        'use_encrypted_endpoints': {'key': 'typeProperties.useEncryptedEndpoints', 'type': 'object'},
        'use_host_verification': {'key': 'typeProperties.useHostVerification', 'type': 'object'},
        'use_peer_verification': {'key': 'typeProperties.usePeerVerification', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, endpoint, authentication_type, connect_via=None, description=None, username=None, password=None, client_id=None, client_secret=None, use_encrypted_endpoints=None, use_host_verification=None, use_peer_verification=None, encrypted_credential=None):
        super(ServiceNowLinkedService, self).__init__(connect_via=connect_via, description=description)
        self.endpoint = endpoint
        self.authentication_type = authentication_type
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.use_encrypted_endpoints = use_encrypted_endpoints
        self.use_host_verification = use_host_verification
        self.use_peer_verification = use_peer_verification
        self.encrypted_credential = encrypted_credential
        self.type = 'ServiceNow'
