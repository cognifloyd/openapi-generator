# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import petstore_api
from petstore_api.models.pet import Pet, PetSchema


class TestPet(unittest.TestCase):
    """Pet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPet(self):
        """Test Pet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = petstore_api.models.pet.Pet()
        pass


class TestPetSchema(unittest.TestCase):
    """PetSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPetSchema(self):
        """Test PetSchema"""
        # FIXME: construct object with mandatory attributes with example values
        # model = petstore_api.models.pet.Pet()
        pass


if __name__ == '__main__':
    unittest.main()
