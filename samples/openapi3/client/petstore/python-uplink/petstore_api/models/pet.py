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

from petstore_api.models.category import Category
from petstore_api.models.category import CategorySchema
from petstore_api.models.tag import Tag
from petstore_api.models.tag import TagSchema

__all__ = [
    'Pet', 'PetSchema',
]


Pet = namedtuple('Pet', field_names=['id', 'category', 'name', 'photo_urls', 'tags', 'status'])


class PetSchema(SchemaBase):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech
    Do not edit the class manually.
    """
    __model__ = Pet

    id = fields.Integer()
    """id: int"""

    category = fields.Nested(CategorySchema, )
    """category: Category"""

    name = fields.String(required=True, )
    """name: str (server side default: 'doggie')"""

    photo_urls = fields.List(fields.String(), required=True, )
    """photoUrls: list[str]"""

    tags = fields.List(fields.Nested(TagSchema, ), )
    """tags: list[Tag]"""

    status = fields.String()
    """status: str"""


