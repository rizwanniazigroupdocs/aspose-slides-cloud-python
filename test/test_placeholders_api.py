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
from asposeslidescloud.apis.placeholders_api import PlaceholdersApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestPlaceholdersApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.placeholders_api.PlaceholdersApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_slides_placeholder(self):
        """Test case for get_slides_placeholder
        """
        request = self.__prepare_get_slides_placeholder_request()
        self.initialize('get_slides_placeholder', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_placeholder')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_placeholder_invalid_name(self):
        """Test case for get_slides_placeholder with invalid name
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_placeholder', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'name')

    def test_get_slides_placeholder_invalid_slide_index(self):
        """Test case for get_slides_placeholder with invalid slide_index
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_placeholder', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'slide_index')

    def test_get_slides_placeholder_invalid_placeholder_index(self):
        """Test case for get_slides_placeholder with invalid placeholder_index
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.placeholder_index = self.get_invalid_test_value('placeholder_index', request.placeholder_index, 'int')
        self.initialize('get_slides_placeholder', 'placeholder_index', request.placeholder_index)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'placeholder_index', request.placeholder_index)
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'placeholder_index')

    def test_get_slides_placeholder_invalid_password(self):
        """Test case for get_slides_placeholder with invalid password
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_placeholder', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'password')

    def test_get_slides_placeholder_invalid_folder(self):
        """Test case for get_slides_placeholder with invalid folder
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_placeholder', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'folder')

    def test_get_slides_placeholder_invalid_storage(self):
        """Test case for get_slides_placeholder with invalid storage
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_placeholder', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'storage')

    def __prepare_get_slides_placeholder_request(self):
        name = self.get_test_value('get_slides_placeholder', 'name', 'str')
        slide_index = self.get_test_value('get_slides_placeholder', 'slide_index', 'int')
        placeholder_index = self.get_test_value('get_slides_placeholder', 'placeholder_index', 'int')
        password = self.get_test_value('get_slides_placeholder', 'password', 'str')
        folder = self.get_test_value('get_slides_placeholder', 'folder', 'str')
        storage = self.get_test_value('get_slides_placeholder', 'storage', 'str')
        return asposeslidescloud.models.requests.placeholders_api_requests.GetSlidesPlaceholderRequest(name, slide_index, placeholder_index, password, folder, storage)

    def test_get_slides_placeholders(self):
        """Test case for get_slides_placeholders
        """
        request = self.__prepare_get_slides_placeholders_request()
        self.initialize('get_slides_placeholders', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_placeholders')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_placeholders_invalid_name(self):
        """Test case for get_slides_placeholders with invalid name
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_placeholders', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'name')

    def test_get_slides_placeholders_invalid_slide_index(self):
        """Test case for get_slides_placeholders with invalid slide_index
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_placeholders', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'slide_index')

    def test_get_slides_placeholders_invalid_password(self):
        """Test case for get_slides_placeholders with invalid password
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_placeholders', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'password')

    def test_get_slides_placeholders_invalid_folder(self):
        """Test case for get_slides_placeholders with invalid folder
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_placeholders', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'folder')

    def test_get_slides_placeholders_invalid_storage(self):
        """Test case for get_slides_placeholders with invalid storage
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_placeholders', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'storage')

    def __prepare_get_slides_placeholders_request(self):
        name = self.get_test_value('get_slides_placeholders', 'name', 'str')
        slide_index = self.get_test_value('get_slides_placeholders', 'slide_index', 'int')
        password = self.get_test_value('get_slides_placeholders', 'password', 'str')
        folder = self.get_test_value('get_slides_placeholders', 'folder', 'str')
        storage = self.get_test_value('get_slides_placeholders', 'storage', 'str')
        return asposeslidescloud.models.requests.placeholders_api_requests.GetSlidesPlaceholdersRequest(name, slide_index, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
