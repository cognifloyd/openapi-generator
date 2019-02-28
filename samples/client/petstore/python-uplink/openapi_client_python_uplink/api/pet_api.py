# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# noinspection PyUnresolvedReferences
import re
# noinspection PyUnresolvedReferences
import six

import uplink
from uplink import returns  # decorators to declare return type
from uplink.arguments import *  # type hints for arguments
from uplink.decorators import *  # request decorators
from uplink.types import *  # type hints for return types

from openapi_client_python_uplink.api.consumer import BaseApiConsumer
from openapi_client_python_uplink.decorators import *  # http methods, security, media_type
from openapi_client_python_uplink.models.api_response import ApiResponse  # TODO: fix Schema import
from openapi_client_python_uplink.models.pet import Pet  # TODO: fix Schema import

__all__ = ['PetApi']


class PetApi(BaseApiConsumer):
    """
    Operations that work with pet tag

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.
    """

    @security('petstore_auth')
    @json  # serialization
    @mime_type(
        content_type=['application/json', 'application/xml'],
    )
    @returns
    @POST('/pet', args={
        'body': Body
    })
    def add_pet(
            self,
            body
    ):
        """
        Add a new pet to the store  # noqa: E501


        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
        """


    @security('petstore_auth')
    @json  # serialization
    @mime_type(
    )
    @returns
    @DELETE('/pet/{petId}', args={
        'api_key': Header
    })
    def delete_pet(
            self,
            pet_id,
            api_key
    ):
        """
        Deletes a pet  # noqa: E501


        :param int pet_id: Pet id to delete (required)
        :param str api_key:
        :return: None
        """


    @security('petstore_auth')
    @json  # serialization
    @mime_type(
        accept=['application/xml', 'application/json'],
    )
    @returns(list[Pet])
    @GET('/pet/findByStatus', args={
        'status': Query
    })
    def find_pets_by_status(
            self,
            status
    ):
        """
        Finds Pets by status  # noqa: E501

        Multiple status values can be provided with comma separated strings  # noqa: E501

        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
        """


    @security('petstore_auth')
    @json  # serialization
    @mime_type(
        accept=['application/xml', 'application/json'],
    )
    @returns(list[Pet])
    @GET('/pet/findByTags', args={
        'tags': Query
    })
    def find_pets_by_tags(
            self,
            tags
    ):
        """
        Finds Pets by tags  # noqa: E501

        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.  # noqa: E501

        :param list[str] tags: Tags to filter by (required)
        :return: list[Pet]
        """


    @security('api_key')
    @json  # serialization
    @mime_type(
        accept=['application/xml', 'application/json'],
    )
    @returns(Pet)
    @GET('/pet/{petId}', args={
    })
    def get_pet_by_id(
            self,
            pet_id
    ):
        """
        Find pet by ID  # noqa: E501

        Returns a single pet  # noqa: E501

        :param int pet_id: ID of pet to return (required)
        :return: Pet
        """


    @security('petstore_auth')
    @json  # serialization
    @mime_type(
        content_type=['application/json', 'application/xml'],
    )
    @returns
    @PUT('/pet', args={
        'body': Body
    })
    def update_pet(
            self,
            body
    ):
        """
        Update an existing pet  # noqa: E501


        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
        """


    @security('petstore_auth')
    @form_url_encoded  # serialization
    @mime_type(
        content_type=['application/x-www-form-urlencoded'],
    )
    @returns
    @POST('/pet/{petId}', args={
        'name': ,
        'status': 
    })
    def update_pet_with_form(
            self,
            pet_id,
            name,
            status
    ):
        """
        Updates a pet in the store with form data  # noqa: E501


        :param int pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet
        :param str status: Updated status of the pet
        :return: None
        """


    @security('petstore_auth')
    @multipart  # serialization
    @mime_type(
        content_type=['multipart/form-data'],
        accept=['application/json'],
    )
    @returns(ApiResponse)
    @POST('/pet/{petId}/uploadImage', args={
        'additional_metadata': ,
        'file': 
    })
    def upload_file(
            self,
            pet_id,
            additional_metadata,
            file
    ):
        """
        uploads an image  # noqa: E501


        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server
        :param file file: file to upload
        :return: ApiResponse
        """

