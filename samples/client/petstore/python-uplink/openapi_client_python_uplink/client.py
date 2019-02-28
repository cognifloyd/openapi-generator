# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from uplink.session import Session

from openapi_client_python_uplink import openapi_client_python_uplink.api

__all__ = ["ApiClient"]


class ApiClient:
    """
    Contains lazy initialized api_clients for the various api classes.
    It should have the same signature as uplink.interfaces.Consumer

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.
    """

    session = None  # type: Session
    api_class_kwargs = {}

    def __init__(
        self,
        base_url=None,
        client=None,
        converters=(),
        auth=None,
        hooks=(),
        **kwargs
    ):
        """Pass these args on to all of the api_class instances"""
        self.api_class_kwargs = {}
        if base_url is not None:
            self.api_class_kwargs["base_url"] = base_url
        if client is not None:
            self.api_class_kwargs["client"] = client
        if converters:
            self.api_class_kwargs["converters"] = converters
        if auth is not None:
            self.api_class_kwargs["auth"] = auth
        if hooks:
            self.api_class_kwargs["hooks"] = hooks
        if kwargs:
            self.api_class_kwargs.update(kwargs)

    class ApiDescriptor:
        def __init__(self, name, api_class):
            self._name = name
            self._api_class = api_class

        def __get__(self, instance, owner):
            if self._name in instance.__dict__:
                return instance.__dict__[self._name]
            attr = instance.__dict__[self._name] = self._api_class(
                **instance.api_class_kwargs
            )
            # TODO: This might not be threadsafe
            if instance.session:
                attr.__dict__["__session"] = instance.session
            else:
                instance.session = attr.__dict__["__session"]
            return attr

        def __set__(self, instance, value):
            if not isinstance(value, self._api_class.__class__):
                raise TypeError("%s must be a %s. Got %s." % (self._name, self._api_class.__name__, type(value)))
            instance.__dict__[self._name] = value

    pet_api = ApiDescriptor("pet_api", openapi_client_python_uplink.api.pet_api.PetApi)

    store_api = ApiDescriptor("store_api", openapi_client_python_uplink.api.store_api.StoreApi)

    user_api = ApiDescriptor("user_api", openapi_client_python_uplink.api.user_api.UserApi)


