# coding=utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from collections import namedtuple

from marshmallow import fields, validate

from petstore_api.models._schema import SchemaBase
from petstore_api.models import _validate


__all__ = [
    'Category', 'CategorySchema',
]


Category = namedtuple('Category', field_names=['id', 'name'])


class CategorySchema(SchemaBase):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.
    """
    __model__ = Category

    id = fields.Integer()
    """id: int"""

    name = fields.String()
    """name: str"""


