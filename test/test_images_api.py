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
from asposeslidescloud.apis.images_api import ImagesApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestImagesApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.images_api.ImagesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_slides_image_with_format(self):
        """Test case for get_slides_image_with_format
        """
        request = self.__prepare_get_slides_image_with_format_request()
        self.initialize('get_slides_image_with_format', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_image_with_format')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_get_slides_image_with_format_invalid_name(self):
        """Test case for get_slides_image_with_format with invalid name
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_image_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'name')

    def test_get_slides_image_with_format_invalid_index(self):
        """Test case for get_slides_image_with_format with invalid index
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.index = self.get_invalid_test_value('index', request.index, 'int')
        self.initialize('get_slides_image_with_format', 'index', request.index)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'index', request.index)
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'index')

    def test_get_slides_image_with_format_invalid_format(self):
        """Test case for get_slides_image_with_format with invalid format
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('get_slides_image_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'format', request.format)
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'format')

    def test_get_slides_image_with_format_invalid_password(self):
        """Test case for get_slides_image_with_format with invalid password
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_image_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'password')

    def test_get_slides_image_with_format_invalid_folder(self):
        """Test case for get_slides_image_with_format with invalid folder
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_image_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'folder')

    def test_get_slides_image_with_format_invalid_storage(self):
        """Test case for get_slides_image_with_format with invalid storage
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_image_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'storage')

    def __prepare_get_slides_image_with_format_request(self):
        name = self.get_test_value('get_slides_image_with_format', 'name', 'str')
        index = self.get_test_value('get_slides_image_with_format', 'index', 'int')
        format = self.get_test_value('get_slides_image_with_format', 'format', 'str')
        password = self.get_test_value('get_slides_image_with_format', 'password', 'str')
        folder = self.get_test_value('get_slides_image_with_format', 'folder', 'str')
        storage = self.get_test_value('get_slides_image_with_format', 'storage', 'str')
        return asposeslidescloud.models.requests.images_api_requests.GetSlidesImageWithFormatRequest(name, index, format, password, folder, storage)

    def test_get_slides_images(self):
        """Test case for get_slides_images
        """
        request = self.__prepare_get_slides_images_request()
        self.initialize('get_slides_images', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_images')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_images_invalid_name(self):
        """Test case for get_slides_images with invalid name
        """
        request = self.__prepare_get_slides_images_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_images', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_images', 'name')

    def test_get_slides_images_invalid_password(self):
        """Test case for get_slides_images with invalid password
        """
        request = self.__prepare_get_slides_images_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_images', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_images', 'password')

    def test_get_slides_images_invalid_folder(self):
        """Test case for get_slides_images with invalid folder
        """
        request = self.__prepare_get_slides_images_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_images', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_images', 'folder')

    def test_get_slides_images_invalid_storage(self):
        """Test case for get_slides_images with invalid storage
        """
        request = self.__prepare_get_slides_images_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_images', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_images', 'storage')

    def __prepare_get_slides_images_request(self):
        name = self.get_test_value('get_slides_images', 'name', 'str')
        password = self.get_test_value('get_slides_images', 'password', 'str')
        folder = self.get_test_value('get_slides_images', 'folder', 'str')
        storage = self.get_test_value('get_slides_images', 'storage', 'str')
        return asposeslidescloud.models.requests.images_api_requests.GetSlidesImagesRequest(name, password, folder, storage)

    def test_get_slides_slide_images(self):
        """Test case for get_slides_slide_images
        """
        request = self.__prepare_get_slides_slide_images_request()
        self.initialize('get_slides_slide_images', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_slide_images')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_slide_images_invalid_name(self):
        """Test case for get_slides_slide_images with invalid name
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_slide_images', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'name')

    def test_get_slides_slide_images_invalid_slide_index(self):
        """Test case for get_slides_slide_images with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_images', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'slide_index')

    def test_get_slides_slide_images_invalid_password(self):
        """Test case for get_slides_slide_images with invalid password
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_slide_images', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'password')

    def test_get_slides_slide_images_invalid_folder(self):
        """Test case for get_slides_slide_images with invalid folder
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_slide_images', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'folder')

    def test_get_slides_slide_images_invalid_storage(self):
        """Test case for get_slides_slide_images with invalid storage
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_slide_images', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'storage')

    def __prepare_get_slides_slide_images_request(self):
        name = self.get_test_value('get_slides_slide_images', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_images', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide_images', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_images', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_images', 'storage', 'str')
        return asposeslidescloud.models.requests.images_api_requests.GetSlidesSlideImagesRequest(name, slide_index, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
