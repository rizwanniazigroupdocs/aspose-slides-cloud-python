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
from asposeslidescloud.apis.slides_api import SlidesApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestSlidesApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_slide_by_index(self):
        """Test case for delete_slide_by_index
        """
        request = self.__prepare_delete_slide_by_index_request()
        self.initialize('delete_slide_by_index', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slide_by_index')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slide_by_index_invalid_name(self):
        """Test case for delete_slide_by_index with invalid name
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slide_by_index', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'name')

    def test_delete_slide_by_index_invalid_slide_index(self):
        """Test case for delete_slide_by_index with invalid slide_index
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_by_index', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'slide_index')

    def test_delete_slide_by_index_invalid_password(self):
        """Test case for delete_slide_by_index with invalid password
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slide_by_index', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'password')

    def test_delete_slide_by_index_invalid_folder(self):
        """Test case for delete_slide_by_index with invalid folder
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slide_by_index', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'folder')

    def test_delete_slide_by_index_invalid_storage(self):
        """Test case for delete_slide_by_index with invalid storage
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slide_by_index', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'storage')

    def __prepare_delete_slide_by_index_request(self):
        name = self.get_test_value('delete_slide_by_index', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_by_index', 'slide_index', 'int')
        password = self.get_test_value('delete_slide_by_index', 'password', 'str')
        folder = self.get_test_value('delete_slide_by_index', 'folder', 'str')
        storage = self.get_test_value('delete_slide_by_index', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideByIndexRequest(name, slide_index, password, folder, storage)

    def test_delete_slides_clean_slides_list(self):
        """Test case for delete_slides_clean_slides_list
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        self.initialize('delete_slides_clean_slides_list', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slides_clean_slides_list')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slides_clean_slides_list_invalid_name(self):
        """Test case for delete_slides_clean_slides_list with invalid name
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slides_clean_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'name')

    def test_delete_slides_clean_slides_list_invalid_slides(self):
        """Test case for delete_slides_clean_slides_list with invalid slides
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.slides = self.get_invalid_test_value('slides', request.slides, 'list[int]')
        self.initialize('delete_slides_clean_slides_list', 'slides', request.slides)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'slides', request.slides)
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'slides')

    def test_delete_slides_clean_slides_list_invalid_password(self):
        """Test case for delete_slides_clean_slides_list with invalid password
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slides_clean_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'password')

    def test_delete_slides_clean_slides_list_invalid_folder(self):
        """Test case for delete_slides_clean_slides_list with invalid folder
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slides_clean_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'folder')

    def test_delete_slides_clean_slides_list_invalid_storage(self):
        """Test case for delete_slides_clean_slides_list with invalid storage
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slides_clean_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'storage')

    def __prepare_delete_slides_clean_slides_list_request(self):
        name = self.get_test_value('delete_slides_clean_slides_list', 'name', 'str')
        slides = self.get_test_value('delete_slides_clean_slides_list', 'slides', 'list[int]')
        password = self.get_test_value('delete_slides_clean_slides_list', 'password', 'str')
        folder = self.get_test_value('delete_slides_clean_slides_list', 'folder', 'str')
        storage = self.get_test_value('delete_slides_clean_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlidesCleanSlidesListRequest(name, slides, password, folder, storage)

    def test_delete_slides_slide_background(self):
        """Test case for delete_slides_slide_background
        """
        request = self.__prepare_delete_slides_slide_background_request()
        self.initialize('delete_slides_slide_background', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slides_slide_background')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slides_slide_background_invalid_name(self):
        """Test case for delete_slides_slide_background with invalid name
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slides_slide_background', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'name')

    def test_delete_slides_slide_background_invalid_slide_index(self):
        """Test case for delete_slides_slide_background with invalid slide_index
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_slides_slide_background', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'slide_index')

    def test_delete_slides_slide_background_invalid_password(self):
        """Test case for delete_slides_slide_background with invalid password
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slides_slide_background', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'password')

    def test_delete_slides_slide_background_invalid_folder(self):
        """Test case for delete_slides_slide_background with invalid folder
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slides_slide_background', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'folder')

    def test_delete_slides_slide_background_invalid_storage(self):
        """Test case for delete_slides_slide_background with invalid storage
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slides_slide_background', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'storage')

    def __prepare_delete_slides_slide_background_request(self):
        name = self.get_test_value('delete_slides_slide_background', 'name', 'str')
        slide_index = self.get_test_value('delete_slides_slide_background', 'slide_index', 'int')
        password = self.get_test_value('delete_slides_slide_background', 'password', 'str')
        folder = self.get_test_value('delete_slides_slide_background', 'folder', 'str')
        storage = self.get_test_value('delete_slides_slide_background', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlidesSlideBackgroundRequest(name, slide_index, password, folder, storage)

    def test_get_slide_with_format(self):
        """Test case for get_slide_with_format
        """
        request = self.__prepare_get_slide_with_format_request()
        self.initialize('get_slide_with_format', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slide_with_format')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_get_slide_with_format_invalid_name(self):
        """Test case for get_slide_with_format with invalid name
        """
        request = self.__prepare_get_slide_with_format_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slide_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'name')

    def test_get_slide_with_format_invalid_slide_index(self):
        """Test case for get_slide_with_format with invalid slide_index
        """
        request = self.__prepare_get_slide_with_format_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slide_with_format', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'slide_index')

    def test_get_slide_with_format_invalid_format(self):
        """Test case for get_slide_with_format with invalid format
        """
        request = self.__prepare_get_slide_with_format_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('get_slide_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'format', request.format)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'format')

    def test_get_slide_with_format_invalid_width(self):
        """Test case for get_slide_with_format with invalid width
        """
        request = self.__prepare_get_slide_with_format_request()
        request.width = self.get_invalid_test_value('width', request.width, 'int')
        self.initialize('get_slide_with_format', 'width', request.width)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'width', request.width)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'width')

    def test_get_slide_with_format_invalid_height(self):
        """Test case for get_slide_with_format with invalid height
        """
        request = self.__prepare_get_slide_with_format_request()
        request.height = self.get_invalid_test_value('height', request.height, 'int')
        self.initialize('get_slide_with_format', 'height', request.height)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'height', request.height)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'height')

    def test_get_slide_with_format_invalid_password(self):
        """Test case for get_slide_with_format with invalid password
        """
        request = self.__prepare_get_slide_with_format_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slide_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'password')

    def test_get_slide_with_format_invalid_folder(self):
        """Test case for get_slide_with_format with invalid folder
        """
        request = self.__prepare_get_slide_with_format_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slide_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'folder')

    def test_get_slide_with_format_invalid_storage(self):
        """Test case for get_slide_with_format with invalid storage
        """
        request = self.__prepare_get_slide_with_format_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slide_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'storage')

    def test_get_slide_with_format_invalid_out_path(self):
        """Test case for get_slide_with_format with invalid out_path
        """
        request = self.__prepare_get_slide_with_format_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('get_slide_with_format', 'out_path', request.out_path)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'out_path')

    def test_get_slide_with_format_invalid_fonts_folder(self):
        """Test case for get_slide_with_format with invalid fonts_folder
        """
        request = self.__prepare_get_slide_with_format_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('get_slide_with_format', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.get_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_with_format', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('get_slide_with_format', 'fonts_folder')

    def __prepare_get_slide_with_format_request(self):
        name = self.get_test_value('get_slide_with_format', 'name', 'str')
        slide_index = self.get_test_value('get_slide_with_format', 'slide_index', 'int')
        format = self.get_test_value('get_slide_with_format', 'format', 'str')
        width = self.get_test_value('get_slide_with_format', 'width', 'int')
        height = self.get_test_value('get_slide_with_format', 'height', 'int')
        password = self.get_test_value('get_slide_with_format', 'password', 'str')
        folder = self.get_test_value('get_slide_with_format', 'folder', 'str')
        storage = self.get_test_value('get_slide_with_format', 'storage', 'str')
        out_path = self.get_test_value('get_slide_with_format', 'out_path', 'str')
        fonts_folder = self.get_test_value('get_slide_with_format', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideWithFormatRequest(name, slide_index, format, width, height, password, folder, storage, out_path, fonts_folder)

    def test_get_slides_slide(self):
        """Test case for get_slides_slide
        """
        request = self.__prepare_get_slides_slide_request()
        self.initialize('get_slides_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_slide_invalid_name(self):
        """Test case for get_slides_slide with invalid name
        """
        request = self.__prepare_get_slides_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_slide', 'name')

    def test_get_slides_slide_invalid_slide_index(self):
        """Test case for get_slides_slide with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_slide', 'slide_index')

    def test_get_slides_slide_invalid_password(self):
        """Test case for get_slides_slide with invalid password
        """
        request = self.__prepare_get_slides_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_slide', 'password')

    def test_get_slides_slide_invalid_folder(self):
        """Test case for get_slides_slide with invalid folder
        """
        request = self.__prepare_get_slides_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_slide', 'folder')

    def test_get_slides_slide_invalid_storage(self):
        """Test case for get_slides_slide with invalid storage
        """
        request = self.__prepare_get_slides_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_slide', 'storage')

    def __prepare_get_slides_slide_request(self):
        name = self.get_test_value('get_slides_slide', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide', 'password', 'str')
        folder = self.get_test_value('get_slides_slide', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slide_background(self):
        """Test case for get_slides_slide_background
        """
        request = self.__prepare_get_slides_slide_background_request()
        self.initialize('get_slides_slide_background', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_slide_background')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_slide_background_invalid_name(self):
        """Test case for get_slides_slide_background with invalid name
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_slide_background', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'name')

    def test_get_slides_slide_background_invalid_slide_index(self):
        """Test case for get_slides_slide_background with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_background', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'slide_index')

    def test_get_slides_slide_background_invalid_password(self):
        """Test case for get_slides_slide_background with invalid password
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_slide_background', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'password')

    def test_get_slides_slide_background_invalid_folder(self):
        """Test case for get_slides_slide_background with invalid folder
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_slide_background', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'folder')

    def test_get_slides_slide_background_invalid_storage(self):
        """Test case for get_slides_slide_background with invalid storage
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_slide_background', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'storage')

    def __prepare_get_slides_slide_background_request(self):
        name = self.get_test_value('get_slides_slide_background', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_background', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide_background', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_background', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_background', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideBackgroundRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slide_comments(self):
        """Test case for get_slides_slide_comments
        """
        request = self.__prepare_get_slides_slide_comments_request()
        self.initialize('get_slides_slide_comments', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_slide_comments')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_slide_comments_invalid_name(self):
        """Test case for get_slides_slide_comments with invalid name
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_slide_comments', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'name')

    def test_get_slides_slide_comments_invalid_slide_index(self):
        """Test case for get_slides_slide_comments with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_comments', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'slide_index')

    def test_get_slides_slide_comments_invalid_password(self):
        """Test case for get_slides_slide_comments with invalid password
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_slide_comments', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'password')

    def test_get_slides_slide_comments_invalid_folder(self):
        """Test case for get_slides_slide_comments with invalid folder
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_slide_comments', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'folder')

    def test_get_slides_slide_comments_invalid_storage(self):
        """Test case for get_slides_slide_comments with invalid storage
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_slide_comments', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'storage')

    def __prepare_get_slides_slide_comments_request(self):
        name = self.get_test_value('get_slides_slide_comments', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_comments', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide_comments', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_comments', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_comments', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideCommentsRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slides_list(self):
        """Test case for get_slides_slides_list
        """
        request = self.__prepare_get_slides_slides_list_request()
        self.initialize('get_slides_slides_list', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_slides_list')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_slides_list_invalid_name(self):
        """Test case for get_slides_slides_list with invalid name
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'name')

    def test_get_slides_slides_list_invalid_password(self):
        """Test case for get_slides_slides_list with invalid password
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'password')

    def test_get_slides_slides_list_invalid_folder(self):
        """Test case for get_slides_slides_list with invalid folder
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'folder')

    def test_get_slides_slides_list_invalid_storage(self):
        """Test case for get_slides_slides_list with invalid storage
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'storage')

    def __prepare_get_slides_slides_list_request(self):
        name = self.get_test_value('get_slides_slides_list', 'name', 'str')
        password = self.get_test_value('get_slides_slides_list', 'password', 'str')
        folder = self.get_test_value('get_slides_slides_list', 'folder', 'str')
        storage = self.get_test_value('get_slides_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlidesListRequest(name, password, folder, storage)

    def test_post_slide_save_as(self):
        """Test case for post_slide_save_as
        """
        request = self.__prepare_post_slide_save_as_request()
        self.initialize('post_slide_save_as', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slide_save_as')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_post_slide_save_as_invalid_name(self):
        """Test case for post_slide_save_as with invalid name
        """
        request = self.__prepare_post_slide_save_as_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slide_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'name')

    def test_post_slide_save_as_invalid_slide_index(self):
        """Test case for post_slide_save_as with invalid slide_index
        """
        request = self.__prepare_post_slide_save_as_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_slide_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'slide_index')

    def test_post_slide_save_as_invalid_format(self):
        """Test case for post_slide_save_as with invalid format
        """
        request = self.__prepare_post_slide_save_as_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('post_slide_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'format', request.format)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'format')

    def test_post_slide_save_as_invalid_options(self):
        """Test case for post_slide_save_as with invalid options
        """
        request = self.__prepare_post_slide_save_as_request()
        request.options = self.get_invalid_test_value('options', request.options, 'ExportOptions')
        self.initialize('post_slide_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'options', request.options)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'options')

    def test_post_slide_save_as_invalid_width(self):
        """Test case for post_slide_save_as with invalid width
        """
        request = self.__prepare_post_slide_save_as_request()
        request.width = self.get_invalid_test_value('width', request.width, 'int')
        self.initialize('post_slide_save_as', 'width', request.width)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'width', request.width)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'width')

    def test_post_slide_save_as_invalid_height(self):
        """Test case for post_slide_save_as with invalid height
        """
        request = self.__prepare_post_slide_save_as_request()
        request.height = self.get_invalid_test_value('height', request.height, 'int')
        self.initialize('post_slide_save_as', 'height', request.height)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'height', request.height)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'height')

    def test_post_slide_save_as_invalid_password(self):
        """Test case for post_slide_save_as with invalid password
        """
        request = self.__prepare_post_slide_save_as_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slide_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'password')

    def test_post_slide_save_as_invalid_folder(self):
        """Test case for post_slide_save_as with invalid folder
        """
        request = self.__prepare_post_slide_save_as_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slide_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'folder')

    def test_post_slide_save_as_invalid_storage(self):
        """Test case for post_slide_save_as with invalid storage
        """
        request = self.__prepare_post_slide_save_as_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slide_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'storage')

    def test_post_slide_save_as_invalid_out_path(self):
        """Test case for post_slide_save_as with invalid out_path
        """
        request = self.__prepare_post_slide_save_as_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('post_slide_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'out_path')

    def test_post_slide_save_as_invalid_fonts_folder(self):
        """Test case for post_slide_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_slide_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_slide_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('post_slide_save_as', 'fonts_folder')

    def __prepare_post_slide_save_as_request(self):
        name = self.get_test_value('post_slide_save_as', 'name', 'str')
        slide_index = self.get_test_value('post_slide_save_as', 'slide_index', 'int')
        format = self.get_test_value('post_slide_save_as', 'format', 'str')
        options = self.get_test_value('post_slide_save_as', 'options', 'ExportOptions')
        width = self.get_test_value('post_slide_save_as', 'width', 'int')
        height = self.get_test_value('post_slide_save_as', 'height', 'int')
        password = self.get_test_value('post_slide_save_as', 'password', 'str')
        folder = self.get_test_value('post_slide_save_as', 'folder', 'str')
        storage = self.get_test_value('post_slide_save_as', 'storage', 'str')
        out_path = self.get_test_value('post_slide_save_as', 'out_path', 'str')
        fonts_folder = self.get_test_value('post_slide_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlideSaveAsRequest(name, slide_index, format, options, width, height, password, folder, storage, out_path, fonts_folder)

    def test_post_slides_add(self):
        """Test case for post_slides_add
        """
        request = self.__prepare_post_slides_add_request()
        self.initialize('post_slides_add', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_add')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_add_invalid_name(self):
        """Test case for post_slides_add with invalid name
        """
        request = self.__prepare_post_slides_add_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_add', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_add', 'name')

    def test_post_slides_add_invalid_position(self):
        """Test case for post_slides_add with invalid position
        """
        request = self.__prepare_post_slides_add_request()
        request.position = self.get_invalid_test_value('position', request.position, 'int')
        self.initialize('post_slides_add', 'position', request.position)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'position', request.position)
        if ok:
            self.assert_no_exception('post_slides_add', 'position')

    def test_post_slides_add_invalid_password(self):
        """Test case for post_slides_add with invalid password
        """
        request = self.__prepare_post_slides_add_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_add', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_add', 'password')

    def test_post_slides_add_invalid_folder(self):
        """Test case for post_slides_add with invalid folder
        """
        request = self.__prepare_post_slides_add_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_add', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_add', 'folder')

    def test_post_slides_add_invalid_storage(self):
        """Test case for post_slides_add with invalid storage
        """
        request = self.__prepare_post_slides_add_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_add', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_add', 'storage')

    def test_post_slides_add_invalid_layout_alias(self):
        """Test case for post_slides_add with invalid layout_alias
        """
        request = self.__prepare_post_slides_add_request()
        request.layout_alias = self.get_invalid_test_value('layout_alias', request.layout_alias, 'str')
        self.initialize('post_slides_add', 'layout_alias', request.layout_alias)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'layout_alias', request.layout_alias)
        if ok:
            self.assert_no_exception('post_slides_add', 'layout_alias')

    def __prepare_post_slides_add_request(self):
        name = self.get_test_value('post_slides_add', 'name', 'str')
        position = self.get_test_value('post_slides_add', 'position', 'int')
        password = self.get_test_value('post_slides_add', 'password', 'str')
        folder = self.get_test_value('post_slides_add', 'folder', 'str')
        storage = self.get_test_value('post_slides_add', 'storage', 'str')
        layout_alias = self.get_test_value('post_slides_add', 'layout_alias', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesAddRequest(name, position, password, folder, storage, layout_alias)

    def test_post_slides_copy(self):
        """Test case for post_slides_copy
        """
        request = self.__prepare_post_slides_copy_request()
        self.initialize('post_slides_copy', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_copy')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_copy_invalid_name(self):
        """Test case for post_slides_copy with invalid name
        """
        request = self.__prepare_post_slides_copy_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_copy', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_copy', 'name')

    def test_post_slides_copy_invalid_slide_to_copy(self):
        """Test case for post_slides_copy with invalid slide_to_copy
        """
        request = self.__prepare_post_slides_copy_request()
        request.slide_to_copy = self.get_invalid_test_value('slide_to_copy', request.slide_to_copy, 'int')
        self.initialize('post_slides_copy', 'slide_to_copy', request.slide_to_copy)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'slide_to_copy', request.slide_to_copy)
        if ok:
            self.assert_no_exception('post_slides_copy', 'slide_to_copy')

    def test_post_slides_copy_invalid_position(self):
        """Test case for post_slides_copy with invalid position
        """
        request = self.__prepare_post_slides_copy_request()
        request.position = self.get_invalid_test_value('position', request.position, 'int')
        self.initialize('post_slides_copy', 'position', request.position)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'position', request.position)
        if ok:
            self.assert_no_exception('post_slides_copy', 'position')

    def test_post_slides_copy_invalid_source(self):
        """Test case for post_slides_copy with invalid source
        """
        request = self.__prepare_post_slides_copy_request()
        request.source = self.get_invalid_test_value('source', request.source, 'str')
        self.initialize('post_slides_copy', 'source', request.source)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'source', request.source)
        if ok:
            self.assert_no_exception('post_slides_copy', 'source')

    def test_post_slides_copy_invalid_source_password(self):
        """Test case for post_slides_copy with invalid source_password
        """
        request = self.__prepare_post_slides_copy_request()
        request.source_password = self.get_invalid_test_value('source_password', request.source_password, 'str')
        self.initialize('post_slides_copy', 'source_password', request.source_password)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'source_password', request.source_password)
        if ok:
            self.assert_no_exception('post_slides_copy', 'source_password')

    def test_post_slides_copy_invalid_password(self):
        """Test case for post_slides_copy with invalid password
        """
        request = self.__prepare_post_slides_copy_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_copy', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_copy', 'password')

    def test_post_slides_copy_invalid_folder(self):
        """Test case for post_slides_copy with invalid folder
        """
        request = self.__prepare_post_slides_copy_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_copy', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_copy', 'folder')

    def test_post_slides_copy_invalid_storage(self):
        """Test case for post_slides_copy with invalid storage
        """
        request = self.__prepare_post_slides_copy_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_copy', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_copy', 'storage')

    def __prepare_post_slides_copy_request(self):
        name = self.get_test_value('post_slides_copy', 'name', 'str')
        slide_to_copy = self.get_test_value('post_slides_copy', 'slide_to_copy', 'int')
        position = self.get_test_value('post_slides_copy', 'position', 'int')
        source = self.get_test_value('post_slides_copy', 'source', 'str')
        source_password = self.get_test_value('post_slides_copy', 'source_password', 'str')
        password = self.get_test_value('post_slides_copy', 'password', 'str')
        folder = self.get_test_value('post_slides_copy', 'folder', 'str')
        storage = self.get_test_value('post_slides_copy', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesCopyRequest(name, slide_to_copy, position, source, source_password, password, folder, storage)

    def test_post_slides_reorder(self):
        """Test case for post_slides_reorder
        """
        request = self.__prepare_post_slides_reorder_request()
        self.initialize('post_slides_reorder', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_reorder')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_reorder_invalid_name(self):
        """Test case for post_slides_reorder with invalid name
        """
        request = self.__prepare_post_slides_reorder_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_reorder', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_reorder', 'name')

    def test_post_slides_reorder_invalid_slide_index(self):
        """Test case for post_slides_reorder with invalid slide_index
        """
        request = self.__prepare_post_slides_reorder_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_slides_reorder', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_slides_reorder', 'slide_index')

    def test_post_slides_reorder_invalid_new_position(self):
        """Test case for post_slides_reorder with invalid new_position
        """
        request = self.__prepare_post_slides_reorder_request()
        request.new_position = self.get_invalid_test_value('new_position', request.new_position, 'int')
        self.initialize('post_slides_reorder', 'new_position', request.new_position)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'new_position', request.new_position)
        if ok:
            self.assert_no_exception('post_slides_reorder', 'new_position')

    def test_post_slides_reorder_invalid_password(self):
        """Test case for post_slides_reorder with invalid password
        """
        request = self.__prepare_post_slides_reorder_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_reorder', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_reorder', 'password')

    def test_post_slides_reorder_invalid_folder(self):
        """Test case for post_slides_reorder with invalid folder
        """
        request = self.__prepare_post_slides_reorder_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_reorder', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_reorder', 'folder')

    def test_post_slides_reorder_invalid_storage(self):
        """Test case for post_slides_reorder with invalid storage
        """
        request = self.__prepare_post_slides_reorder_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_reorder', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_reorder', 'storage')

    def __prepare_post_slides_reorder_request(self):
        name = self.get_test_value('post_slides_reorder', 'name', 'str')
        slide_index = self.get_test_value('post_slides_reorder', 'slide_index', 'int')
        new_position = self.get_test_value('post_slides_reorder', 'new_position', 'int')
        password = self.get_test_value('post_slides_reorder', 'password', 'str')
        folder = self.get_test_value('post_slides_reorder', 'folder', 'str')
        storage = self.get_test_value('post_slides_reorder', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesReorderRequest(name, slide_index, new_position, password, folder, storage)

    def test_post_slides_reorder_many(self):
        """Test case for post_slides_reorder_many
        """
        request = self.__prepare_post_slides_reorder_many_request()
        self.initialize('post_slides_reorder_many', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_reorder_many')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_reorder_many_invalid_name(self):
        """Test case for post_slides_reorder_many with invalid name
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_reorder_many', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'name')

    def test_post_slides_reorder_many_invalid_old_positions(self):
        """Test case for post_slides_reorder_many with invalid old_positions
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.old_positions = self.get_invalid_test_value('old_positions', request.old_positions, 'list[int]')
        self.initialize('post_slides_reorder_many', 'old_positions', request.old_positions)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'old_positions', request.old_positions)
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'old_positions')

    def test_post_slides_reorder_many_invalid_new_positions(self):
        """Test case for post_slides_reorder_many with invalid new_positions
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.new_positions = self.get_invalid_test_value('new_positions', request.new_positions, 'list[int]')
        self.initialize('post_slides_reorder_many', 'new_positions', request.new_positions)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'new_positions', request.new_positions)
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'new_positions')

    def test_post_slides_reorder_many_invalid_password(self):
        """Test case for post_slides_reorder_many with invalid password
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_reorder_many', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'password')

    def test_post_slides_reorder_many_invalid_folder(self):
        """Test case for post_slides_reorder_many with invalid folder
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_reorder_many', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'folder')

    def test_post_slides_reorder_many_invalid_storage(self):
        """Test case for post_slides_reorder_many with invalid storage
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_reorder_many', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'storage')

    def __prepare_post_slides_reorder_many_request(self):
        name = self.get_test_value('post_slides_reorder_many', 'name', 'str')
        old_positions = self.get_test_value('post_slides_reorder_many', 'old_positions', 'list[int]')
        new_positions = self.get_test_value('post_slides_reorder_many', 'new_positions', 'list[int]')
        password = self.get_test_value('post_slides_reorder_many', 'password', 'str')
        folder = self.get_test_value('post_slides_reorder_many', 'folder', 'str')
        storage = self.get_test_value('post_slides_reorder_many', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesReorderManyRequest(name, old_positions, new_positions, password, folder, storage)

    def test_post_slides_reorder_position(self):
        """Test case for post_slides_reorder_position
        """
        request = self.__prepare_post_slides_reorder_position_request()
        self.initialize('post_slides_reorder_position', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_reorder_position')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_reorder_position_invalid_name(self):
        """Test case for post_slides_reorder_position with invalid name
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_reorder_position', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'name')

    def test_post_slides_reorder_position_invalid_old_position(self):
        """Test case for post_slides_reorder_position with invalid old_position
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.old_position = self.get_invalid_test_value('old_position', request.old_position, 'int')
        self.initialize('post_slides_reorder_position', 'old_position', request.old_position)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'old_position', request.old_position)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'old_position')

    def test_post_slides_reorder_position_invalid_new_position(self):
        """Test case for post_slides_reorder_position with invalid new_position
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.new_position = self.get_invalid_test_value('new_position', request.new_position, 'int')
        self.initialize('post_slides_reorder_position', 'new_position', request.new_position)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'new_position', request.new_position)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'new_position')

    def test_post_slides_reorder_position_invalid_old_positions(self):
        """Test case for post_slides_reorder_position with invalid old_positions
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.old_positions = self.get_invalid_test_value('old_positions', request.old_positions, 'list[int]')
        self.initialize('post_slides_reorder_position', 'old_positions', request.old_positions)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'old_positions', request.old_positions)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'old_positions')

    def test_post_slides_reorder_position_invalid_new_positions(self):
        """Test case for post_slides_reorder_position with invalid new_positions
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.new_positions = self.get_invalid_test_value('new_positions', request.new_positions, 'list[int]')
        self.initialize('post_slides_reorder_position', 'new_positions', request.new_positions)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'new_positions', request.new_positions)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'new_positions')

    def test_post_slides_reorder_position_invalid_slide_to_copy(self):
        """Test case for post_slides_reorder_position with invalid slide_to_copy
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.slide_to_copy = self.get_invalid_test_value('slide_to_copy', request.slide_to_copy, 'int')
        self.initialize('post_slides_reorder_position', 'slide_to_copy', request.slide_to_copy)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'slide_to_copy', request.slide_to_copy)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'slide_to_copy')

    def test_post_slides_reorder_position_invalid_position(self):
        """Test case for post_slides_reorder_position with invalid position
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.position = self.get_invalid_test_value('position', request.position, 'int')
        self.initialize('post_slides_reorder_position', 'position', request.position)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'position', request.position)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'position')

    def test_post_slides_reorder_position_invalid_slide_to_clone(self):
        """Test case for post_slides_reorder_position with invalid slide_to_clone
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.slide_to_clone = self.get_invalid_test_value('slide_to_clone', request.slide_to_clone, 'int')
        self.initialize('post_slides_reorder_position', 'slide_to_clone', request.slide_to_clone)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'slide_to_clone', request.slide_to_clone)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'slide_to_clone')

    def test_post_slides_reorder_position_invalid_source(self):
        """Test case for post_slides_reorder_position with invalid source
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.source = self.get_invalid_test_value('source', request.source, 'str')
        self.initialize('post_slides_reorder_position', 'source', request.source)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'source', request.source)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'source')

    def test_post_slides_reorder_position_invalid_password(self):
        """Test case for post_slides_reorder_position with invalid password
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_reorder_position', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'password')

    def test_post_slides_reorder_position_invalid_folder(self):
        """Test case for post_slides_reorder_position with invalid folder
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_reorder_position', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'folder')

    def test_post_slides_reorder_position_invalid_storage(self):
        """Test case for post_slides_reorder_position with invalid storage
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_reorder_position', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'storage')

    def test_post_slides_reorder_position_invalid_layout_alias(self):
        """Test case for post_slides_reorder_position with invalid layout_alias
        """
        request = self.__prepare_post_slides_reorder_position_request()
        request.layout_alias = self.get_invalid_test_value('layout_alias', request.layout_alias, 'str')
        self.initialize('post_slides_reorder_position', 'layout_alias', request.layout_alias)
        ok = False
        try:
            self.api.post_slides_reorder_position(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_position', 'layout_alias', request.layout_alias)
        if ok:
            self.assert_no_exception('post_slides_reorder_position', 'layout_alias')

    def __prepare_post_slides_reorder_position_request(self):
        name = self.get_test_value('post_slides_reorder_position', 'name', 'str')
        old_position = self.get_test_value('post_slides_reorder_position', 'old_position', 'int')
        new_position = self.get_test_value('post_slides_reorder_position', 'new_position', 'int')
        old_positions = self.get_test_value('post_slides_reorder_position', 'old_positions', 'list[int]')
        new_positions = self.get_test_value('post_slides_reorder_position', 'new_positions', 'list[int]')
        slide_to_copy = self.get_test_value('post_slides_reorder_position', 'slide_to_copy', 'int')
        position = self.get_test_value('post_slides_reorder_position', 'position', 'int')
        slide_to_clone = self.get_test_value('post_slides_reorder_position', 'slide_to_clone', 'int')
        source = self.get_test_value('post_slides_reorder_position', 'source', 'str')
        password = self.get_test_value('post_slides_reorder_position', 'password', 'str')
        folder = self.get_test_value('post_slides_reorder_position', 'folder', 'str')
        storage = self.get_test_value('post_slides_reorder_position', 'storage', 'str')
        layout_alias = self.get_test_value('post_slides_reorder_position', 'layout_alias', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesReorderPositionRequest(name, old_position, new_position, old_positions, new_positions, slide_to_copy, position, slide_to_clone, source, password, folder, storage, layout_alias)

    def test_put_slides_slide(self):
        """Test case for put_slides_slide
        """
        request = self.__prepare_put_slides_slide_request()
        self.initialize('put_slides_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slides_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_slides_slide_invalid_name(self):
        """Test case for put_slides_slide with invalid name
        """
        request = self.__prepare_put_slides_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_slides_slide', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('put_slides_slide', 'name')

    def test_put_slides_slide_invalid_slide_index(self):
        """Test case for put_slides_slide with invalid slide_index
        """
        request = self.__prepare_put_slides_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_slides_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_slides_slide', 'slide_index')

    def test_put_slides_slide_invalid_slide_dto(self):
        """Test case for put_slides_slide with invalid slide_dto
        """
        request = self.__prepare_put_slides_slide_request()
        request.slide_dto = self.get_invalid_test_value('slide_dto', request.slide_dto, 'Slide')
        self.initialize('put_slides_slide', 'slide_dto', request.slide_dto)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'slide_dto', request.slide_dto)
        if ok:
            self.assert_no_exception('put_slides_slide', 'slide_dto')

    def test_put_slides_slide_invalid_password(self):
        """Test case for put_slides_slide with invalid password
        """
        request = self.__prepare_put_slides_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slides_slide', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slides_slide', 'password')

    def test_put_slides_slide_invalid_folder(self):
        """Test case for put_slides_slide with invalid folder
        """
        request = self.__prepare_put_slides_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_slides_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_slides_slide', 'folder')

    def test_put_slides_slide_invalid_storage(self):
        """Test case for put_slides_slide with invalid storage
        """
        request = self.__prepare_put_slides_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_slides_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_slides_slide', 'storage')

    def __prepare_put_slides_slide_request(self):
        name = self.get_test_value('put_slides_slide', 'name', 'str')
        slide_index = self.get_test_value('put_slides_slide', 'slide_index', 'int')
        slide_dto = self.get_test_value('put_slides_slide', 'slide_dto', 'Slide')
        password = self.get_test_value('put_slides_slide', 'password', 'str')
        folder = self.get_test_value('put_slides_slide', 'folder', 'str')
        storage = self.get_test_value('put_slides_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSlideRequest(name, slide_index, slide_dto, password, folder, storage)

    def test_put_slides_slide_background(self):
        """Test case for put_slides_slide_background
        """
        request = self.__prepare_put_slides_slide_background_request()
        self.initialize('put_slides_slide_background', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slides_slide_background')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_slides_slide_background_invalid_name(self):
        """Test case for put_slides_slide_background with invalid name
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_slides_slide_background', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'name', request.name)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'name')

    def test_put_slides_slide_background_invalid_slide_index(self):
        """Test case for put_slides_slide_background with invalid slide_index
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_slides_slide_background', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'slide_index')

    def test_put_slides_slide_background_invalid_background(self):
        """Test case for put_slides_slide_background with invalid background
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.background = self.get_invalid_test_value('background', request.background, 'SlideBackground')
        self.initialize('put_slides_slide_background', 'background', request.background)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'background', request.background)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'background')

    def test_put_slides_slide_background_invalid_folder(self):
        """Test case for put_slides_slide_background with invalid folder
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_slides_slide_background', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'folder')

    def test_put_slides_slide_background_invalid_password(self):
        """Test case for put_slides_slide_background with invalid password
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slides_slide_background', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'password')

    def test_put_slides_slide_background_invalid_storage(self):
        """Test case for put_slides_slide_background with invalid storage
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_slides_slide_background', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'storage')

    def test_put_slides_slide_background_invalid_color(self):
        """Test case for put_slides_slide_background with invalid color
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.color = self.get_invalid_test_value('color', request.color, 'str')
        self.initialize('put_slides_slide_background', 'color', request.color)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'color', request.color)
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'color')

    def __prepare_put_slides_slide_background_request(self):
        name = self.get_test_value('put_slides_slide_background', 'name', 'str')
        slide_index = self.get_test_value('put_slides_slide_background', 'slide_index', 'int')
        background = self.get_test_value('put_slides_slide_background', 'background', 'SlideBackground')
        folder = self.get_test_value('put_slides_slide_background', 'folder', 'str')
        password = self.get_test_value('put_slides_slide_background', 'password', 'str')
        storage = self.get_test_value('put_slides_slide_background', 'storage', 'str')
        color = self.get_test_value('put_slides_slide_background', 'color', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSlideBackgroundRequest(name, slide_index, background, folder, password, storage, color)


if __name__ == '__main__':
    unittest.main()
