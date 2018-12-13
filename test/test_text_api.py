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
from asposeslidescloud.apis.text_api import TextApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestTextApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.text_api.TextApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_slides_presentation_text_items(self):
        """Test case for get_slides_presentation_text_items
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        self.initialize('get_slides_presentation_text_items', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_presentation_text_items')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_presentation_text_items_invalid_name(self):
        """Test case for get_slides_presentation_text_items with invalid name
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_presentation_text_items', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'name')

    def test_get_slides_presentation_text_items_invalid_with_empty(self):
        """Test case for get_slides_presentation_text_items with invalid with_empty
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.with_empty = self.get_invalid_test_value('with_empty', request.with_empty, 'bool')
        self.initialize('get_slides_presentation_text_items', 'with_empty', request.with_empty)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'with_empty', request.with_empty)
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'with_empty')

    def test_get_slides_presentation_text_items_invalid_password(self):
        """Test case for get_slides_presentation_text_items with invalid password
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_presentation_text_items', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'password')

    def test_get_slides_presentation_text_items_invalid_folder(self):
        """Test case for get_slides_presentation_text_items with invalid folder
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_presentation_text_items', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'folder')

    def test_get_slides_presentation_text_items_invalid_storage(self):
        """Test case for get_slides_presentation_text_items with invalid storage
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_presentation_text_items', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'storage')

    def __prepare_get_slides_presentation_text_items_request(self):
        name = self.get_test_value('get_slides_presentation_text_items', 'name', 'str')
        with_empty = self.get_test_value('get_slides_presentation_text_items', 'with_empty', 'bool')
        password = self.get_test_value('get_slides_presentation_text_items', 'password', 'str')
        folder = self.get_test_value('get_slides_presentation_text_items', 'folder', 'str')
        storage = self.get_test_value('get_slides_presentation_text_items', 'storage', 'str')
        return asposeslidescloud.models.requests.text_api_requests.GetSlidesPresentationTextItemsRequest(name, with_empty, password, folder, storage)

    def test_get_slides_slide_text_items(self):
        """Test case for get_slides_slide_text_items
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        self.initialize('get_slides_slide_text_items', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_slide_text_items')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_slide_text_items_invalid_name(self):
        """Test case for get_slides_slide_text_items with invalid name
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_slide_text_items', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'name')

    def test_get_slides_slide_text_items_invalid_slide_index(self):
        """Test case for get_slides_slide_text_items with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_text_items', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'slide_index')

    def test_get_slides_slide_text_items_invalid_with_empty(self):
        """Test case for get_slides_slide_text_items with invalid with_empty
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.with_empty = self.get_invalid_test_value('with_empty', request.with_empty, 'bool')
        self.initialize('get_slides_slide_text_items', 'with_empty', request.with_empty)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'with_empty', request.with_empty)
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'with_empty')

    def test_get_slides_slide_text_items_invalid_password(self):
        """Test case for get_slides_slide_text_items with invalid password
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_slide_text_items', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'password')

    def test_get_slides_slide_text_items_invalid_folder(self):
        """Test case for get_slides_slide_text_items with invalid folder
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_slide_text_items', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'folder')

    def test_get_slides_slide_text_items_invalid_storage(self):
        """Test case for get_slides_slide_text_items with invalid storage
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_slide_text_items', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'storage')

    def __prepare_get_slides_slide_text_items_request(self):
        name = self.get_test_value('get_slides_slide_text_items', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_text_items', 'slide_index', 'int')
        with_empty = self.get_test_value('get_slides_slide_text_items', 'with_empty', 'bool')
        password = self.get_test_value('get_slides_slide_text_items', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_text_items', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_text_items', 'storage', 'str')
        return asposeslidescloud.models.requests.text_api_requests.GetSlidesSlideTextItemsRequest(name, slide_index, with_empty, password, folder, storage)

    def test_post_slides_presentation_replace_text(self):
        """Test case for post_slides_presentation_replace_text
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        self.initialize('post_slides_presentation_replace_text', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_presentation_replace_text')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_presentation_replace_text_invalid_name(self):
        """Test case for post_slides_presentation_replace_text with invalid name
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_presentation_replace_text', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'name')

    def test_post_slides_presentation_replace_text_invalid_old_value(self):
        """Test case for post_slides_presentation_replace_text with invalid old_value
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.old_value = self.get_invalid_test_value('old_value', request.old_value, 'str')
        self.initialize('post_slides_presentation_replace_text', 'old_value', request.old_value)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'old_value', request.old_value)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'old_value')

    def test_post_slides_presentation_replace_text_invalid_new_value(self):
        """Test case for post_slides_presentation_replace_text with invalid new_value
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.new_value = self.get_invalid_test_value('new_value', request.new_value, 'str')
        self.initialize('post_slides_presentation_replace_text', 'new_value', request.new_value)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'new_value', request.new_value)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'new_value')

    def test_post_slides_presentation_replace_text_invalid_ignore_case(self):
        """Test case for post_slides_presentation_replace_text with invalid ignore_case
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.ignore_case = self.get_invalid_test_value('ignore_case', request.ignore_case, 'bool')
        self.initialize('post_slides_presentation_replace_text', 'ignore_case', request.ignore_case)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'ignore_case', request.ignore_case)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'ignore_case')

    def test_post_slides_presentation_replace_text_invalid_password(self):
        """Test case for post_slides_presentation_replace_text with invalid password
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_presentation_replace_text', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'password')

    def test_post_slides_presentation_replace_text_invalid_folder(self):
        """Test case for post_slides_presentation_replace_text with invalid folder
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_presentation_replace_text', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'folder')

    def test_post_slides_presentation_replace_text_invalid_storage(self):
        """Test case for post_slides_presentation_replace_text with invalid storage
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_presentation_replace_text', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'storage')

    def __prepare_post_slides_presentation_replace_text_request(self):
        name = self.get_test_value('post_slides_presentation_replace_text', 'name', 'str')
        old_value = self.get_test_value('post_slides_presentation_replace_text', 'old_value', 'str')
        new_value = self.get_test_value('post_slides_presentation_replace_text', 'new_value', 'str')
        ignore_case = self.get_test_value('post_slides_presentation_replace_text', 'ignore_case', 'bool')
        password = self.get_test_value('post_slides_presentation_replace_text', 'password', 'str')
        folder = self.get_test_value('post_slides_presentation_replace_text', 'folder', 'str')
        storage = self.get_test_value('post_slides_presentation_replace_text', 'storage', 'str')
        return asposeslidescloud.models.requests.text_api_requests.PostSlidesPresentationReplaceTextRequest(name, old_value, new_value, ignore_case, password, folder, storage)

    def test_post_slides_slide_replace_text(self):
        """Test case for post_slides_slide_replace_text
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        self.initialize('post_slides_slide_replace_text', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_slide_replace_text')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_slide_replace_text_invalid_name(self):
        """Test case for post_slides_slide_replace_text with invalid name
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_slide_replace_text', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'name')

    def test_post_slides_slide_replace_text_invalid_slide_index(self):
        """Test case for post_slides_slide_replace_text with invalid slide_index
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_slides_slide_replace_text', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'slide_index')

    def test_post_slides_slide_replace_text_invalid_old_value(self):
        """Test case for post_slides_slide_replace_text with invalid old_value
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.old_value = self.get_invalid_test_value('old_value', request.old_value, 'str')
        self.initialize('post_slides_slide_replace_text', 'old_value', request.old_value)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'old_value', request.old_value)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'old_value')

    def test_post_slides_slide_replace_text_invalid_new_value(self):
        """Test case for post_slides_slide_replace_text with invalid new_value
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.new_value = self.get_invalid_test_value('new_value', request.new_value, 'str')
        self.initialize('post_slides_slide_replace_text', 'new_value', request.new_value)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'new_value', request.new_value)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'new_value')

    def test_post_slides_slide_replace_text_invalid_ignore_case(self):
        """Test case for post_slides_slide_replace_text with invalid ignore_case
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.ignore_case = self.get_invalid_test_value('ignore_case', request.ignore_case, 'bool')
        self.initialize('post_slides_slide_replace_text', 'ignore_case', request.ignore_case)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'ignore_case', request.ignore_case)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'ignore_case')

    def test_post_slides_slide_replace_text_invalid_password(self):
        """Test case for post_slides_slide_replace_text with invalid password
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_slide_replace_text', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'password')

    def test_post_slides_slide_replace_text_invalid_folder(self):
        """Test case for post_slides_slide_replace_text with invalid folder
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_slide_replace_text', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'folder')

    def test_post_slides_slide_replace_text_invalid_storage(self):
        """Test case for post_slides_slide_replace_text with invalid storage
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_slide_replace_text', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'storage')

    def __prepare_post_slides_slide_replace_text_request(self):
        name = self.get_test_value('post_slides_slide_replace_text', 'name', 'str')
        slide_index = self.get_test_value('post_slides_slide_replace_text', 'slide_index', 'int')
        old_value = self.get_test_value('post_slides_slide_replace_text', 'old_value', 'str')
        new_value = self.get_test_value('post_slides_slide_replace_text', 'new_value', 'str')
        ignore_case = self.get_test_value('post_slides_slide_replace_text', 'ignore_case', 'bool')
        password = self.get_test_value('post_slides_slide_replace_text', 'password', 'str')
        folder = self.get_test_value('post_slides_slide_replace_text', 'folder', 'str')
        storage = self.get_test_value('post_slides_slide_replace_text', 'storage', 'str')
        return asposeslidescloud.models.requests.text_api_requests.PostSlidesSlideReplaceTextRequest(name, slide_index, old_value, new_value, ignore_case, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
