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
from asposeslidescloud.apis.theme_api import ThemeApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestThemeApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.theme_api.ThemeApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_slides_theme(self):
        """Test case for get_slides_theme
        """
        request = self.__prepare_get_slides_theme_request()
        self.initialize('get_slides_theme', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_theme')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_theme_invalid_name(self):
        """Test case for get_slides_theme with invalid name
        """
        request = self.__prepare_get_slides_theme_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_theme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_theme', 'name')

    def test_get_slides_theme_invalid_slide_index(self):
        """Test case for get_slides_theme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_theme', 'slide_index')

    def test_get_slides_theme_invalid_password(self):
        """Test case for get_slides_theme with invalid password
        """
        request = self.__prepare_get_slides_theme_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_theme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_theme', 'password')

    def test_get_slides_theme_invalid_folder(self):
        """Test case for get_slides_theme with invalid folder
        """
        request = self.__prepare_get_slides_theme_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_theme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_theme', 'folder')

    def test_get_slides_theme_invalid_storage(self):
        """Test case for get_slides_theme with invalid storage
        """
        request = self.__prepare_get_slides_theme_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_theme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_theme', 'storage')

    def __prepare_get_slides_theme_request(self):
        name = self.get_test_value('get_slides_theme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme', 'storage', 'str')
        return asposeslidescloud.models.requests.theme_api_requests.GetSlidesThemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_theme_color_scheme(self):
        """Test case for get_slides_theme_color_scheme
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        self.initialize('get_slides_theme_color_scheme', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_theme_color_scheme')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_theme_color_scheme_invalid_name(self):
        """Test case for get_slides_theme_color_scheme with invalid name
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_theme_color_scheme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'name')

    def test_get_slides_theme_color_scheme_invalid_slide_index(self):
        """Test case for get_slides_theme_color_scheme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme_color_scheme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'slide_index')

    def test_get_slides_theme_color_scheme_invalid_password(self):
        """Test case for get_slides_theme_color_scheme with invalid password
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_theme_color_scheme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'password')

    def test_get_slides_theme_color_scheme_invalid_folder(self):
        """Test case for get_slides_theme_color_scheme with invalid folder
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_theme_color_scheme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'folder')

    def test_get_slides_theme_color_scheme_invalid_storage(self):
        """Test case for get_slides_theme_color_scheme with invalid storage
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_theme_color_scheme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'storage')

    def __prepare_get_slides_theme_color_scheme_request(self):
        name = self.get_test_value('get_slides_theme_color_scheme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme_color_scheme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme_color_scheme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme_color_scheme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme_color_scheme', 'storage', 'str')
        return asposeslidescloud.models.requests.theme_api_requests.GetSlidesThemeColorSchemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_theme_font_scheme(self):
        """Test case for get_slides_theme_font_scheme
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        self.initialize('get_slides_theme_font_scheme', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_theme_font_scheme')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_theme_font_scheme_invalid_name(self):
        """Test case for get_slides_theme_font_scheme with invalid name
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_theme_font_scheme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'name')

    def test_get_slides_theme_font_scheme_invalid_slide_index(self):
        """Test case for get_slides_theme_font_scheme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme_font_scheme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'slide_index')

    def test_get_slides_theme_font_scheme_invalid_password(self):
        """Test case for get_slides_theme_font_scheme with invalid password
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_theme_font_scheme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'password')

    def test_get_slides_theme_font_scheme_invalid_folder(self):
        """Test case for get_slides_theme_font_scheme with invalid folder
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_theme_font_scheme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'folder')

    def test_get_slides_theme_font_scheme_invalid_storage(self):
        """Test case for get_slides_theme_font_scheme with invalid storage
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_theme_font_scheme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'storage')

    def __prepare_get_slides_theme_font_scheme_request(self):
        name = self.get_test_value('get_slides_theme_font_scheme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme_font_scheme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme_font_scheme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme_font_scheme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme_font_scheme', 'storage', 'str')
        return asposeslidescloud.models.requests.theme_api_requests.GetSlidesThemeFontSchemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_theme_format_scheme(self):
        """Test case for get_slides_theme_format_scheme
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        self.initialize('get_slides_theme_format_scheme', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_theme_format_scheme')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_theme_format_scheme_invalid_name(self):
        """Test case for get_slides_theme_format_scheme with invalid name
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_theme_format_scheme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'name')

    def test_get_slides_theme_format_scheme_invalid_slide_index(self):
        """Test case for get_slides_theme_format_scheme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme_format_scheme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'slide_index')

    def test_get_slides_theme_format_scheme_invalid_password(self):
        """Test case for get_slides_theme_format_scheme with invalid password
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_theme_format_scheme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'password')

    def test_get_slides_theme_format_scheme_invalid_folder(self):
        """Test case for get_slides_theme_format_scheme with invalid folder
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_theme_format_scheme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'folder')

    def test_get_slides_theme_format_scheme_invalid_storage(self):
        """Test case for get_slides_theme_format_scheme with invalid storage
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_theme_format_scheme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'storage')

    def __prepare_get_slides_theme_format_scheme_request(self):
        name = self.get_test_value('get_slides_theme_format_scheme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme_format_scheme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme_format_scheme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme_format_scheme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme_format_scheme', 'storage', 'str')
        return asposeslidescloud.models.requests.theme_api_requests.GetSlidesThemeFormatSchemeRequest(name, slide_index, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
