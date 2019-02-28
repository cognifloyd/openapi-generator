# coding=utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re

from six import string_types

# noinspection PyProtectedMember
from uplink.decorators import MethodAnnotation
from uplink.hooks import RequestAuditor
# noinspection PyPep8Naming
from uplink import get as GET, head as HEAD, put as PUT, post as POST, patch as PATCH, delete as DELETE

__all__ = ['security', 'media_type', 'GET', 'HEAD', 'PUT', 'POST', 'PATCH', 'DELETE']


# noinspection PyPep8Naming
class security(MethodAnnotation):
    """
    A decorator that adds security/auth info for API calls.

    .. code-block:: python

        @security('BasicAuth')
        @get('/user')
        def get_user(self):
            \"""Get the current user\"""

    When used as a class decorator, :py:class:`security` applies to
    all consumer methods bound to the class:

    .. code-block:: python

        @security('BasicAuth')
        class PetStoreApi(Consumer):
            ...

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    Args:
        *args: A list of security type names (where a security type is an auth-style request modifier class)
    """

    def __init__(self, *args):
        self._security = args

    def modify_request(self, request_builder):
        """Updates request using auth objects."""
        request_builder.add_transaction_hook(self._hook)

    def inject_request_auth(self, consumer, request_builder):
        """

        :param uplink.Consumer consumer:
        :param helpers.RequestBuilder request_builder:
        :return:
        """
        security_methods = getattr(consumer, 'security', {})
        for auth_type in self._security:
            if auth_type in security_methods:
                security_methods[auth_type](request_builder)

    @property
    def _hook(self):
        if self.__hook is None:
            self.__hook = RequestAuditor(self.inject_request_auth, requires_consumer=True)
        return self.__hook


# noinspection PyPep8Naming
class media_type(MethodAnnotation):
    """
    A decorator that adds Accepts and Content-Type headers to API requests

    .. code-block:: python

        @media_type(content_type=['application/json'], accept=['application/vnd.example.v3+json', 'application/json'])
        @get("/user")
        def get_user(self):
            \"""Get the current user\"""

    When used as a class decorator, :py:class:`media_type` applies to
    all consumer methods bound to the class:

    .. code-block:: python

        @media_type(content_type=['application/json'], accept=['application/vnd.example.v3+json', 'application/json'])
        class PetStoreApi(Consumer):
            ...

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    Args:
        content_type: A list of possible mime types for use in Content-Type header
        accept: A list of possible mime types for use in Accept header
    """

    # expects already lowercase mime types
    _json_mime_pattern = re.compile(r"application/(vnd\..+)json(;.*)?")

    def __init__(self, content_type=None, accept=None):
        """
        :param list content_type:
        :param list accept:
        """
        if isinstance(content_type, string_types):
            content_type = [content_type]
        if isinstance(accept, string_types):
            accept = [accept]
        self._content_type = self.select_header_content_type(content_type)
        self._accept = self.select_header_accept(accept)

    def modify_request(self, request_builder):
        """Inject Accept and Content-Type headers."""
        if self._content_type:
            request_builder.info['headers']['Content-Type'] = self._content_type
        if self._accept:
            request_builder.info['headers']['Accept'] = self._accept

    def select_header_content_type(self, content_types):
        """
        Returns `Content-Type` based on an array of content_types provided.
        Based on method from openapi-generator original python client

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [mime.lower() for mime in content_types]
        json_types = [mime for mime in content_types if self._json_mime_pattern.match(mime)]

        if json_types:
            return json_types[0]
        elif '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def select_header_accept(self, accepts):
        """
        Returns `Accept` based on an array of accepts provided.
        Based on method from openapi-generator original python client

        :param accepts: List of mime types
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        accepts = [mime.lower() for mime in accepts]
        json_types = [mime for mime in accepts if self._json_mime_pattern.match(mime)]

        if json_types:
            return ', '.join(json_types)
        else:
            return ', '.join(accepts)
