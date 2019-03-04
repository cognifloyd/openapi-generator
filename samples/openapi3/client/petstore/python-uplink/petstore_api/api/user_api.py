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

from petstore_api.api.consumer import BaseApiConsumer
from petstore_api.decorators import *  # http methods, security, media_type
from petstore_api.models.user import User  # TODO: fix Schema import

__all__ = ['UserApi']


class UserApi(BaseApiConsumer):
    """
    Operations that work with user tag

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.
    """

    @security()
    @mime_type(
        content_type=['application/json'],
    )
    @returns
    @POST('/user', args={
        'user': Body
    })
    def create_user(
            self,
            user
    ):
        """
        Create user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501

        :param User user: Created user object (required)
        :return: None
        """


    @security()
    @mime_type(
        content_type=['application/json'],
    )
    @returns
    @POST('/user/createWithArray', args={
        'user': Body
    })
    def create_users_with_array_input(
            self,
            user
    ):
        """
        Creates list of users with given input array  # noqa: E501


        :param list[User] user: List of user object (required)
        :return: None
        """


    @security()
    @mime_type(
        content_type=['application/json'],
    )
    @returns
    @POST('/user/createWithList', args={
        'user': Body
    })
    def create_users_with_list_input(
            self,
            user
    ):
        """
        Creates list of users with given input array  # noqa: E501


        :param list[User] user: List of user object (required)
        :return: None
        """


    @security()
    @mime_type(
    )
    @returns
    @DELETE('/user/{username}', args={
    })
    def delete_user(
            self,
            username
    ):
        """
        Delete user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501

        :param str username: The name that needs to be deleted (required)
        :return: None
        """


    @security()
    @mime_type(
        accept=['application/xml', 'application/json'],
    )
    @returns(User)
    @GET('/user/{username}', args={
    })
    def get_user_by_name(
            self,
            username
    ):
        """
        Get user by user name  # noqa: E501


        :param str username: The name that needs to be fetched. Use user1 for testing. (required)
        :return: User
        """


    @security()
    @mime_type(
        accept=['application/xml', 'application/json'],
    )
    @returns(str)
    @GET('/user/login', args={
        'username': Query,
        'password': Query
    })
    def login_user(
            self,
            username,
            password
    ):
        """
        Logs user into the system  # noqa: E501


        :param str username: The user name for login (required)
        :param str password: The password for login in clear text (required)
        :return: str
        """


    @security()
    @mime_type(
    )
    @returns
    @GET('/user/logout', args={
    })
    def logout_user(
            self,
    ):
        """
        Logs out current logged in user session  # noqa: E501


        :return: None
        """


    @security()
    @mime_type(
        content_type=['application/json'],
    )
    @returns
    @PUT('/user/{username}', args={
        'user': Body
    })
    def update_user(
            self,
            username,
            user
    ):
        """
        Updated user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501

        :param str username: name that need to be deleted (required)
        :param User user: Updated user object (required)
        :return: None
        """

