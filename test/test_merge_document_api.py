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
from asposeslidescloud.apis.merge_document_api import MergeDocumentApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestMergeDocumentApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.merge_document_api.MergeDocumentApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_post_presentation_merge(self):
        """Test case for post_presentation_merge
        """
        request = self.__prepare_post_presentation_merge_request()
        self.initialize('post_presentation_merge', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_presentation_merge')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_presentation_merge_invalid_name(self):
        """Test case for post_presentation_merge with invalid name
        """
        request = self.__prepare_post_presentation_merge_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_presentation_merge', 'name', request.name)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'name', request.name)
        if ok:
            self.assert_no_exception('post_presentation_merge', 'name')

    def test_post_presentation_merge_invalid_request(self):
        """Test case for post_presentation_merge with invalid request
        """
        request = self.__prepare_post_presentation_merge_request()
        request.request = self.get_invalid_test_value('request', request.request, 'PresentationsMergeRequest')
        self.initialize('post_presentation_merge', 'request', request.request)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'request', request.request)
        if ok:
            self.assert_no_exception('post_presentation_merge', 'request')

    def test_post_presentation_merge_invalid_password(self):
        """Test case for post_presentation_merge with invalid password
        """
        request = self.__prepare_post_presentation_merge_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_presentation_merge', 'password', request.password)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'password', request.password)
        if ok:
            self.assert_no_exception('post_presentation_merge', 'password')

    def test_post_presentation_merge_invalid_storage(self):
        """Test case for post_presentation_merge with invalid storage
        """
        request = self.__prepare_post_presentation_merge_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_presentation_merge', 'storage', request.storage)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_presentation_merge', 'storage')

    def test_post_presentation_merge_invalid_folder(self):
        """Test case for post_presentation_merge with invalid folder
        """
        request = self.__prepare_post_presentation_merge_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_presentation_merge', 'folder', request.folder)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_presentation_merge', 'folder')

    def __prepare_post_presentation_merge_request(self):
        name = self.get_test_value('post_presentation_merge', 'name', 'str')
        request = self.get_test_value('post_presentation_merge', 'request', 'PresentationsMergeRequest')
        password = self.get_test_value('post_presentation_merge', 'password', 'str')
        storage = self.get_test_value('post_presentation_merge', 'storage', 'str')
        folder = self.get_test_value('post_presentation_merge', 'folder', 'str')
        return asposeslidescloud.models.requests.merge_document_api_requests.PostPresentationMergeRequest(name, request, password, storage, folder)

    def test_put_presentation_merge(self):
        """Test case for put_presentation_merge
        """
        request = self.__prepare_put_presentation_merge_request()
        self.initialize('put_presentation_merge', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_presentation_merge')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_presentation_merge_invalid_name(self):
        """Test case for put_presentation_merge with invalid name
        """
        request = self.__prepare_put_presentation_merge_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_presentation_merge', 'name', request.name)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'name', request.name)
        if ok:
            self.assert_no_exception('put_presentation_merge', 'name')

    def test_put_presentation_merge_invalid_request(self):
        """Test case for put_presentation_merge with invalid request
        """
        request = self.__prepare_put_presentation_merge_request()
        request.request = self.get_invalid_test_value('request', request.request, 'OrderedMergeRequest')
        self.initialize('put_presentation_merge', 'request', request.request)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'request', request.request)
        if ok:
            self.assert_no_exception('put_presentation_merge', 'request')

    def test_put_presentation_merge_invalid_password(self):
        """Test case for put_presentation_merge with invalid password
        """
        request = self.__prepare_put_presentation_merge_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_presentation_merge', 'password', request.password)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'password', request.password)
        if ok:
            self.assert_no_exception('put_presentation_merge', 'password')

    def test_put_presentation_merge_invalid_storage(self):
        """Test case for put_presentation_merge with invalid storage
        """
        request = self.__prepare_put_presentation_merge_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_presentation_merge', 'storage', request.storage)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_presentation_merge', 'storage')

    def test_put_presentation_merge_invalid_folder(self):
        """Test case for put_presentation_merge with invalid folder
        """
        request = self.__prepare_put_presentation_merge_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_presentation_merge', 'folder', request.folder)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_presentation_merge', 'folder')

    def __prepare_put_presentation_merge_request(self):
        name = self.get_test_value('put_presentation_merge', 'name', 'str')
        request = self.get_test_value('put_presentation_merge', 'request', 'OrderedMergeRequest')
        password = self.get_test_value('put_presentation_merge', 'password', 'str')
        storage = self.get_test_value('put_presentation_merge', 'storage', 'str')
        folder = self.get_test_value('put_presentation_merge', 'folder', 'str')
        return asposeslidescloud.models.requests.merge_document_api_requests.PutPresentationMergeRequest(name, request, password, storage, folder)


if __name__ == '__main__':
    unittest.main()
