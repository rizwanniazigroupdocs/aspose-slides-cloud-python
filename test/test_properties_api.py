# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

from __future__ import absolute_import

import unittest

from test.base_test import BaseTest

import asposeslidescloud
from asposeslidescloud.apis.properties_api import PropertiesApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestPropertiesApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.properties_api.PropertiesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_slides_document_properties(self):
        """Test case for delete_slides_document_properties
        """
        request = self.__prepare_delete_slides_document_properties_request()
        self.initialize('delete_slides_document_properties', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slides_document_properties')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slides_document_properties_invalid_name(self):
        """Test case for delete_slides_document_properties with invalid name
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slides_document_properties', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'name')

    def test_delete_slides_document_properties_invalid_password(self):
        """Test case for delete_slides_document_properties with invalid password
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slides_document_properties', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'password')

    def test_delete_slides_document_properties_invalid_folder(self):
        """Test case for delete_slides_document_properties with invalid folder
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slides_document_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'folder')

    def test_delete_slides_document_properties_invalid_storage(self):
        """Test case for delete_slides_document_properties with invalid storage
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slides_document_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'storage')

    def __prepare_delete_slides_document_properties_request(self):
        name = self.get_test_value('delete_slides_document_properties', 'name', 'str')
        password = self.get_test_value('delete_slides_document_properties', 'password', 'str')
        folder = self.get_test_value('delete_slides_document_properties', 'folder', 'str')
        storage = self.get_test_value('delete_slides_document_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.properties_api_requests.DeleteSlidesDocumentPropertiesRequest(name, password, folder, storage)

    def test_delete_slides_document_property(self):
        """Test case for delete_slides_document_property
        """
        request = self.__prepare_delete_slides_document_property_request()
        self.initialize('delete_slides_document_property', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slides_document_property')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slides_document_property_invalid_name(self):
        """Test case for delete_slides_document_property with invalid name
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slides_document_property', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'name')

    def test_delete_slides_document_property_invalid_property_name(self):
        """Test case for delete_slides_document_property with invalid property_name
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.property_name = self.get_invalid_test_value('property_name', request.property_name, 'str')
        self.initialize('delete_slides_document_property', 'property_name', request.property_name)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'property_name', request.property_name)
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'property_name')

    def test_delete_slides_document_property_invalid_password(self):
        """Test case for delete_slides_document_property with invalid password
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slides_document_property', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'password')

    def test_delete_slides_document_property_invalid_folder(self):
        """Test case for delete_slides_document_property with invalid folder
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slides_document_property', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'folder')

    def test_delete_slides_document_property_invalid_storage(self):
        """Test case for delete_slides_document_property with invalid storage
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slides_document_property', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'storage')

    def __prepare_delete_slides_document_property_request(self):
        name = self.get_test_value('delete_slides_document_property', 'name', 'str')
        property_name = self.get_test_value('delete_slides_document_property', 'property_name', 'str')
        password = self.get_test_value('delete_slides_document_property', 'password', 'str')
        folder = self.get_test_value('delete_slides_document_property', 'folder', 'str')
        storage = self.get_test_value('delete_slides_document_property', 'storage', 'str')
        return asposeslidescloud.models.requests.properties_api_requests.DeleteSlidesDocumentPropertyRequest(name, property_name, password, folder, storage)

    def test_get_slides_document_properties(self):
        """Test case for get_slides_document_properties
        """
        request = self.__prepare_get_slides_document_properties_request()
        self.initialize('get_slides_document_properties', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_document_properties')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_document_properties_invalid_name(self):
        """Test case for get_slides_document_properties with invalid name
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_document_properties', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'name')

    def test_get_slides_document_properties_invalid_password(self):
        """Test case for get_slides_document_properties with invalid password
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_document_properties', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'password')

    def test_get_slides_document_properties_invalid_folder(self):
        """Test case for get_slides_document_properties with invalid folder
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_document_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'folder')

    def test_get_slides_document_properties_invalid_storage(self):
        """Test case for get_slides_document_properties with invalid storage
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_document_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'storage')

    def __prepare_get_slides_document_properties_request(self):
        name = self.get_test_value('get_slides_document_properties', 'name', 'str')
        password = self.get_test_value('get_slides_document_properties', 'password', 'str')
        folder = self.get_test_value('get_slides_document_properties', 'folder', 'str')
        storage = self.get_test_value('get_slides_document_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.properties_api_requests.GetSlidesDocumentPropertiesRequest(name, password, folder, storage)

    def test_get_slides_document_property(self):
        """Test case for get_slides_document_property
        """
        request = self.__prepare_get_slides_document_property_request()
        self.initialize('get_slides_document_property', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_document_property')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_document_property_invalid_name(self):
        """Test case for get_slides_document_property with invalid name
        """
        request = self.__prepare_get_slides_document_property_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_document_property', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_document_property', 'name')

    def test_get_slides_document_property_invalid_property_name(self):
        """Test case for get_slides_document_property with invalid property_name
        """
        request = self.__prepare_get_slides_document_property_request()
        request.property_name = self.get_invalid_test_value('property_name', request.property_name, 'str')
        self.initialize('get_slides_document_property', 'property_name', request.property_name)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'property_name', request.property_name)
        if ok:
            self.assert_no_exception('get_slides_document_property', 'property_name')

    def test_get_slides_document_property_invalid_password(self):
        """Test case for get_slides_document_property with invalid password
        """
        request = self.__prepare_get_slides_document_property_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_document_property', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_document_property', 'password')

    def test_get_slides_document_property_invalid_folder(self):
        """Test case for get_slides_document_property with invalid folder
        """
        request = self.__prepare_get_slides_document_property_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_document_property', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_document_property', 'folder')

    def test_get_slides_document_property_invalid_storage(self):
        """Test case for get_slides_document_property with invalid storage
        """
        request = self.__prepare_get_slides_document_property_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_document_property', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_document_property', 'storage')

    def __prepare_get_slides_document_property_request(self):
        name = self.get_test_value('get_slides_document_property', 'name', 'str')
        property_name = self.get_test_value('get_slides_document_property', 'property_name', 'str')
        password = self.get_test_value('get_slides_document_property', 'password', 'str')
        folder = self.get_test_value('get_slides_document_property', 'folder', 'str')
        storage = self.get_test_value('get_slides_document_property', 'storage', 'str')
        return asposeslidescloud.models.requests.properties_api_requests.GetSlidesDocumentPropertyRequest(name, property_name, password, folder, storage)

    def test_post_slides_set_document_properties(self):
        """Test case for post_slides_set_document_properties
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        self.initialize('post_slides_set_document_properties', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_set_document_properties')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_set_document_properties_invalid_name(self):
        """Test case for post_slides_set_document_properties with invalid name
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_set_document_properties', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'name')

    def test_post_slides_set_document_properties_invalid_properties(self):
        """Test case for post_slides_set_document_properties with invalid properties
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.properties = self.get_invalid_test_value('properties', request.properties, 'DocumentProperties')
        self.initialize('post_slides_set_document_properties', 'properties', request.properties)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'properties', request.properties)
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'properties')

    def test_post_slides_set_document_properties_invalid_password(self):
        """Test case for post_slides_set_document_properties with invalid password
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_set_document_properties', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'password')

    def test_post_slides_set_document_properties_invalid_folder(self):
        """Test case for post_slides_set_document_properties with invalid folder
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_set_document_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'folder')

    def test_post_slides_set_document_properties_invalid_storage(self):
        """Test case for post_slides_set_document_properties with invalid storage
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_set_document_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'storage')

    def __prepare_post_slides_set_document_properties_request(self):
        name = self.get_test_value('post_slides_set_document_properties', 'name', 'str')
        properties = self.get_test_value('post_slides_set_document_properties', 'properties', 'DocumentProperties')
        password = self.get_test_value('post_slides_set_document_properties', 'password', 'str')
        folder = self.get_test_value('post_slides_set_document_properties', 'folder', 'str')
        storage = self.get_test_value('post_slides_set_document_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.properties_api_requests.PostSlidesSetDocumentPropertiesRequest(name, properties, password, folder, storage)

    def test_put_slides_set_document_property(self):
        """Test case for put_slides_set_document_property
        """
        request = self.__prepare_put_slides_set_document_property_request()
        self.initialize('put_slides_set_document_property', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slides_set_document_property')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_slides_set_document_property_invalid_name(self):
        """Test case for put_slides_set_document_property with invalid name
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_slides_set_document_property', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'name', request.name)
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'name')

    def test_put_slides_set_document_property_invalid_property_name(self):
        """Test case for put_slides_set_document_property with invalid property_name
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.property_name = self.get_invalid_test_value('property_name', request.property_name, 'str')
        self.initialize('put_slides_set_document_property', 'property_name', request.property_name)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'property_name', request.property_name)
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'property_name')

    def test_put_slides_set_document_property_invalid__property(self):
        """Test case for put_slides_set_document_property with invalid _property
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request._property = self.get_invalid_test_value('_property', request._property, 'DocumentProperty')
        self.initialize('put_slides_set_document_property', '_property', request._property)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', '_property', request._property)
        if ok:
            self.assert_no_exception('put_slides_set_document_property', '_property')

    def test_put_slides_set_document_property_invalid_password(self):
        """Test case for put_slides_set_document_property with invalid password
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slides_set_document_property', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'password')

    def test_put_slides_set_document_property_invalid_folder(self):
        """Test case for put_slides_set_document_property with invalid folder
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_slides_set_document_property', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'folder')

    def test_put_slides_set_document_property_invalid_storage(self):
        """Test case for put_slides_set_document_property with invalid storage
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_slides_set_document_property', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'storage')

    def __prepare_put_slides_set_document_property_request(self):
        name = self.get_test_value('put_slides_set_document_property', 'name', 'str')
        property_name = self.get_test_value('put_slides_set_document_property', 'property_name', 'str')
        _property = self.get_test_value('put_slides_set_document_property', '_property', 'DocumentProperty')
        password = self.get_test_value('put_slides_set_document_property', 'password', 'str')
        folder = self.get_test_value('put_slides_set_document_property', 'folder', 'str')
        storage = self.get_test_value('put_slides_set_document_property', 'storage', 'str')
        return asposeslidescloud.models.requests.properties_api_requests.PutSlidesSetDocumentPropertyRequest(name, property_name, _property, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
