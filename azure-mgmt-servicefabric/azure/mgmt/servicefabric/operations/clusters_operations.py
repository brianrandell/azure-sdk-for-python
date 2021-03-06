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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_operation import AzureOperationPoller

from .. import models


class ClustersOperations(object):
    """ClustersOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: The version of the ServiceFabric resouce provider api. Constant value: "2016-09-01".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2016-09-01"

        self.config = config

    def update(
            self, resource_group_name, cluster_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Update cluster configuration.

        :param resource_group_name: The name of the resource group to which
         the resource belongs or get created
        :type resource_group_name: str
        :param cluster_name: The name of the cluster resource
        :type cluster_name: str
        :param parameters: The parameters which contains the property value
         and property name which used to update the cluster configuration
        :type parameters: :class:`ClusterUpdateParameters
         <azure.mgmt.servicefabric.models.ClusterUpdateParameters>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`Cluster
         <azure.mgmt.servicefabric.models.Cluster>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         or :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorModelException<azure.mgmt.servicefabric.models.ErrorModelException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ClusterUpdateParameters')

        # Construct and send request
        def long_running_send():

            request = self._client.patch(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ErrorModelException(self._deserialize, response)

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('Cluster', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def get(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, **operation_config):
        """Get cluster resource.

        :param resource_group_name: The name of the resource group to which
         the resource belongs or get created
        :type resource_group_name: str
        :param cluster_name: The name of the cluster resource
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: :class:`Cluster <azure.mgmt.servicefabric.models.Cluster>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: :class:`Cluster <azure.mgmt.servicefabric.models.Cluster>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorModelException<azure.mgmt.servicefabric.models.ErrorModelException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorModelException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Cluster', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, resource_group_name, cluster_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Create cluster resource.

        :param resource_group_name: The name of the resource group to which
         the resource belongs or get created
        :type resource_group_name: str
        :param cluster_name: The name of the cluster resource
        :type cluster_name: str
        :param parameters: Put Request
        :type parameters: :class:`Cluster
         <azure.mgmt.servicefabric.models.Cluster>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`Cluster
         <azure.mgmt.servicefabric.models.Cluster>` or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         or :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorModelException<azure.mgmt.servicefabric.models.ErrorModelException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'Cluster')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ErrorModelException(self._deserialize, response)

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('Cluster', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def delete(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, **operation_config):
        """Delete cluster resource.

        :param resource_group_name: The name of the resource group to which
         the resource belongs or get created
        :type resource_group_name: str
        :param cluster_name: The name of the cluster resource
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorModelException<azure.mgmt.servicefabric.models.ErrorModelException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorModelException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list_by_resource_group(
            self, resource_group_name, custom_headers=None, raw=False, **operation_config):
        """List cluster resource by resource group.

        :param resource_group_name: The name of the resource group to which
         the resource belongs or get created
        :type resource_group_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`Cluster
         <azure.mgmt.servicefabric.models.Cluster>`
        :rtype: :class:`ClusterPaged
         <azure.mgmt.servicefabric.models.ClusterPaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters'
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ClusterPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ClusterPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def list(
            self, custom_headers=None, raw=False, **operation_config):
        """List cluster resource.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`Cluster
         <azure.mgmt.servicefabric.models.Cluster>`
        :rtype: :class:`ClusterPaged
         <azure.mgmt.servicefabric.models.ClusterPaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/clusters'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ClusterPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ClusterPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
