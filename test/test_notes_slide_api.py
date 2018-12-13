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
from asposeslidescloud.apis.notes_slide_api import NotesSlideApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestNotesSlideApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.notes_slide_api.NotesSlideApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_notes_slide(self):
        """Test case for delete_notes_slide
        """
        request = self.__prepare_delete_notes_slide_request()
        self.initialize('delete_notes_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_notes_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_notes_slide_invalid_name(self):
        """Test case for delete_notes_slide with invalid name
        """
        request = self.__prepare_delete_notes_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_notes_slide', 'name')

    def test_delete_notes_slide_invalid_slide_index(self):
        """Test case for delete_notes_slide with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_notes_slide', 'slide_index')

    def test_delete_notes_slide_invalid_password(self):
        """Test case for delete_notes_slide with invalid password
        """
        request = self.__prepare_delete_notes_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_notes_slide', 'password')

    def test_delete_notes_slide_invalid_folder(self):
        """Test case for delete_notes_slide with invalid folder
        """
        request = self.__prepare_delete_notes_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_notes_slide', 'folder')

    def test_delete_notes_slide_invalid_storage(self):
        """Test case for delete_notes_slide with invalid storage
        """
        request = self.__prepare_delete_notes_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_notes_slide', 'storage')

    def __prepare_delete_notes_slide_request(self):
        name = self.get_test_value('delete_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide', 'slide_index', 'int')
        password = self.get_test_value('delete_notes_slide', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.notes_slide_api_requests.DeleteNotesSlideRequest(name, slide_index, password, folder, storage)

    def test_get_notes_slide(self):
        """Test case for get_notes_slide
        """
        request = self.__prepare_get_notes_slide_request()
        self.initialize('get_notes_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_notes_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_notes_slide_invalid_name(self):
        """Test case for get_notes_slide with invalid name
        """
        request = self.__prepare_get_notes_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('get_notes_slide', 'name')

    def test_get_notes_slide_invalid_slide_index(self):
        """Test case for get_notes_slide with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_notes_slide', 'slide_index')

    def test_get_notes_slide_invalid_password(self):
        """Test case for get_notes_slide with invalid password
        """
        request = self.__prepare_get_notes_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('get_notes_slide', 'password')

    def test_get_notes_slide_invalid_folder(self):
        """Test case for get_notes_slide with invalid folder
        """
        request = self.__prepare_get_notes_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_notes_slide', 'folder')

    def test_get_notes_slide_invalid_storage(self):
        """Test case for get_notes_slide with invalid storage
        """
        request = self.__prepare_get_notes_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_notes_slide', 'storage')

    def __prepare_get_notes_slide_request(self):
        name = self.get_test_value('get_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide', 'slide_index', 'int')
        password = self.get_test_value('get_notes_slide', 'password', 'str')
        folder = self.get_test_value('get_notes_slide', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.notes_slide_api_requests.GetNotesSlideRequest(name, slide_index, password, folder, storage)

    def test_get_notes_slide_with_format(self):
        """Test case for get_notes_slide_with_format
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        self.initialize('get_notes_slide_with_format', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_notes_slide_with_format')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_get_notes_slide_with_format_invalid_name(self):
        """Test case for get_notes_slide_with_format with invalid name
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_notes_slide_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'name', request.name)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'name')

    def test_get_notes_slide_with_format_invalid_slide_index(self):
        """Test case for get_notes_slide_with_format with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_with_format', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'slide_index')

    def test_get_notes_slide_with_format_invalid_format(self):
        """Test case for get_notes_slide_with_format with invalid format
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('get_notes_slide_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'format', request.format)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'format')

    def test_get_notes_slide_with_format_invalid_width(self):
        """Test case for get_notes_slide_with_format with invalid width
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.width = self.get_invalid_test_value('width', request.width, 'int')
        self.initialize('get_notes_slide_with_format', 'width', request.width)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'width', request.width)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'width')

    def test_get_notes_slide_with_format_invalid_height(self):
        """Test case for get_notes_slide_with_format with invalid height
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.height = self.get_invalid_test_value('height', request.height, 'int')
        self.initialize('get_notes_slide_with_format', 'height', request.height)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'height', request.height)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'height')

    def test_get_notes_slide_with_format_invalid_password(self):
        """Test case for get_notes_slide_with_format with invalid password
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_notes_slide_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'password', request.password)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'password')

    def test_get_notes_slide_with_format_invalid_folder(self):
        """Test case for get_notes_slide_with_format with invalid folder
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_notes_slide_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'folder')

    def test_get_notes_slide_with_format_invalid_storage(self):
        """Test case for get_notes_slide_with_format with invalid storage
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_notes_slide_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'storage')

    def __prepare_get_notes_slide_with_format_request(self):
        name = self.get_test_value('get_notes_slide_with_format', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_with_format', 'slide_index', 'int')
        format = self.get_test_value('get_notes_slide_with_format', 'format', 'str')
        width = self.get_test_value('get_notes_slide_with_format', 'width', 'int')
        height = self.get_test_value('get_notes_slide_with_format', 'height', 'int')
        password = self.get_test_value('get_notes_slide_with_format', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_with_format', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_with_format', 'storage', 'str')
        return asposeslidescloud.models.requests.notes_slide_api_requests.GetNotesSlideWithFormatRequest(name, slide_index, format, width, height, password, folder, storage)

    def test_post_add_notes_slide(self):
        """Test case for post_add_notes_slide
        """
        request = self.__prepare_post_add_notes_slide_request()
        self.initialize('post_add_notes_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_add_notes_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_add_notes_slide_invalid_name(self):
        """Test case for post_add_notes_slide with invalid name
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_add_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'name')

    def test_post_add_notes_slide_invalid_slide_index(self):
        """Test case for post_add_notes_slide with invalid slide_index
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_add_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'slide_index')

    def test_post_add_notes_slide_invalid_dto(self):
        """Test case for post_add_notes_slide with invalid dto
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'NotesSlide')
        self.initialize('post_add_notes_slide', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'dto', request.dto)
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'dto')

    def test_post_add_notes_slide_invalid_password(self):
        """Test case for post_add_notes_slide with invalid password
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_add_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'password')

    def test_post_add_notes_slide_invalid_folder(self):
        """Test case for post_add_notes_slide with invalid folder
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_add_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'folder')

    def test_post_add_notes_slide_invalid_storage(self):
        """Test case for post_add_notes_slide with invalid storage
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_add_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'storage')

    def __prepare_post_add_notes_slide_request(self):
        name = self.get_test_value('post_add_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('post_add_notes_slide', 'slide_index', 'int')
        dto = self.get_test_value('post_add_notes_slide', 'dto', 'NotesSlide')
        password = self.get_test_value('post_add_notes_slide', 'password', 'str')
        folder = self.get_test_value('post_add_notes_slide', 'folder', 'str')
        storage = self.get_test_value('post_add_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.notes_slide_api_requests.PostAddNotesSlideRequest(name, slide_index, dto, password, folder, storage)

    def test_put_update_notes_slide(self):
        """Test case for put_update_notes_slide
        """
        request = self.__prepare_put_update_notes_slide_request()
        self.initialize('put_update_notes_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_update_notes_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_update_notes_slide_invalid_name(self):
        """Test case for put_update_notes_slide with invalid name
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_update_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'name')

    def test_put_update_notes_slide_invalid_slide_index(self):
        """Test case for put_update_notes_slide with invalid slide_index
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_update_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'slide_index')

    def test_put_update_notes_slide_invalid_dto(self):
        """Test case for put_update_notes_slide with invalid dto
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'NotesSlide')
        self.initialize('put_update_notes_slide', 'dto', request.dto)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'dto', request.dto)
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'dto')

    def test_put_update_notes_slide_invalid_password(self):
        """Test case for put_update_notes_slide with invalid password
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_update_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'password')

    def test_put_update_notes_slide_invalid_folder(self):
        """Test case for put_update_notes_slide with invalid folder
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_update_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'folder')

    def test_put_update_notes_slide_invalid_storage(self):
        """Test case for put_update_notes_slide with invalid storage
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_update_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'storage')

    def __prepare_put_update_notes_slide_request(self):
        name = self.get_test_value('put_update_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('put_update_notes_slide', 'slide_index', 'int')
        dto = self.get_test_value('put_update_notes_slide', 'dto', 'NotesSlide')
        password = self.get_test_value('put_update_notes_slide', 'password', 'str')
        folder = self.get_test_value('put_update_notes_slide', 'folder', 'str')
        storage = self.get_test_value('put_update_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.notes_slide_api_requests.PutUpdateNotesSlideRequest(name, slide_index, dto, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
