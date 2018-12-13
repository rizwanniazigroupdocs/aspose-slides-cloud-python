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
from asposeslidescloud.apis.layout_slides_api import LayoutSlidesApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestLayoutSlidesApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.layout_slides_api.LayoutSlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_layout_slide(self):
        """Test case for get_layout_slide
        """
        request = self.__prepare_get_layout_slide_request()
        self.initialize('get_layout_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_layout_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_layout_slide_invalid_name(self):
        """Test case for get_layout_slide with invalid name
        """
        request = self.__prepare_get_layout_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_layout_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('get_layout_slide', 'name')

    def test_get_layout_slide_invalid_slide_index(self):
        """Test case for get_layout_slide with invalid slide_index
        """
        request = self.__prepare_get_layout_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_layout_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_layout_slide', 'slide_index')

    def test_get_layout_slide_invalid_password(self):
        """Test case for get_layout_slide with invalid password
        """
        request = self.__prepare_get_layout_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_layout_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('get_layout_slide', 'password')

    def test_get_layout_slide_invalid_folder(self):
        """Test case for get_layout_slide with invalid folder
        """
        request = self.__prepare_get_layout_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_layout_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_layout_slide', 'folder')

    def test_get_layout_slide_invalid_storage(self):
        """Test case for get_layout_slide with invalid storage
        """
        request = self.__prepare_get_layout_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_layout_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_layout_slide', 'storage')

    def __prepare_get_layout_slide_request(self):
        name = self.get_test_value('get_layout_slide', 'name', 'str')
        slide_index = self.get_test_value('get_layout_slide', 'slide_index', 'int')
        password = self.get_test_value('get_layout_slide', 'password', 'str')
        folder = self.get_test_value('get_layout_slide', 'folder', 'str')
        storage = self.get_test_value('get_layout_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.layout_slides_api_requests.GetLayoutSlideRequest(name, slide_index, password, folder, storage)

    def test_get_layout_slides_list(self):
        """Test case for get_layout_slides_list
        """
        request = self.__prepare_get_layout_slides_list_request()
        self.initialize('get_layout_slides_list', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_layout_slides_list')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_layout_slides_list_invalid_name(self):
        """Test case for get_layout_slides_list with invalid name
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_layout_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'name', request.name)
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'name')

    def test_get_layout_slides_list_invalid_password(self):
        """Test case for get_layout_slides_list with invalid password
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_layout_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'password', request.password)
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'password')

    def test_get_layout_slides_list_invalid_folder(self):
        """Test case for get_layout_slides_list with invalid folder
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_layout_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'folder')

    def test_get_layout_slides_list_invalid_storage(self):
        """Test case for get_layout_slides_list with invalid storage
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_layout_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'storage')

    def __prepare_get_layout_slides_list_request(self):
        name = self.get_test_value('get_layout_slides_list', 'name', 'str')
        password = self.get_test_value('get_layout_slides_list', 'password', 'str')
        folder = self.get_test_value('get_layout_slides_list', 'folder', 'str')
        storage = self.get_test_value('get_layout_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.layout_slides_api_requests.GetLayoutSlidesListRequest(name, password, folder, storage)

    def test_post_copy_layout_slide_from_source_presentation(self):
        """Test case for post_copy_layout_slide_from_source_presentation
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        self.initialize('post_copy_layout_slide_from_source_presentation', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_copy_layout_slide_from_source_presentation')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_copy_layout_slide_from_source_presentation_invalid_name(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid name
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'name', request.name)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'name', request.name)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'name')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from = self.get_invalid_test_value('clone_from', request.clone_from, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from', request.clone_from)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from', request.clone_from)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from_position(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from_position
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from_position = self.get_invalid_test_value('clone_from_position', request.clone_from_position, 'int')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from_position', request.clone_from_position)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from_position', request.clone_from_position)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from_position')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from_password(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from_password
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from_password = self.get_invalid_test_value('clone_from_password', request.clone_from_password, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from_password', request.clone_from_password)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from_password', request.clone_from_password)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from_password')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from_storage(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from_storage
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from_storage = self.get_invalid_test_value('clone_from_storage', request.clone_from_storage, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from_storage')

    def test_post_copy_layout_slide_from_source_presentation_invalid_password(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid password
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'password', request.password)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'password', request.password)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'password')

    def test_post_copy_layout_slide_from_source_presentation_invalid_folder(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid folder
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'folder', request.folder)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'folder')

    def test_post_copy_layout_slide_from_source_presentation_invalid_storage(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid storage
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'storage', request.storage)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'storage')

    def __prepare_post_copy_layout_slide_from_source_presentation_request(self):
        name = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'name', 'str')
        clone_from = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from', 'str')
        clone_from_position = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_position', 'int')
        clone_from_password = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_password', 'str')
        clone_from_storage = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_storage', 'str')
        password = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'password', 'str')
        folder = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'folder', 'str')
        storage = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'storage', 'str')
        return asposeslidescloud.models.requests.layout_slides_api_requests.PostCopyLayoutSlideFromSourcePresentationRequest(name, clone_from, clone_from_position, clone_from_password, clone_from_storage, password, folder, storage)

    def test_put_layout_slide(self):
        """Test case for put_layout_slide
        """
        request = self.__prepare_put_layout_slide_request()
        self.initialize('put_layout_slide', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_layout_slide')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_layout_slide_invalid_name(self):
        """Test case for put_layout_slide with invalid name
        """
        request = self.__prepare_put_layout_slide_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_layout_slide', 'name', request.name)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'name', request.name)
        if ok:
            self.assert_no_exception('put_layout_slide', 'name')

    def test_put_layout_slide_invalid_slide_index(self):
        """Test case for put_layout_slide with invalid slide_index
        """
        request = self.__prepare_put_layout_slide_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_layout_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_layout_slide', 'slide_index')

    def test_put_layout_slide_invalid_slide_dto(self):
        """Test case for put_layout_slide with invalid slide_dto
        """
        request = self.__prepare_put_layout_slide_request()
        request.slide_dto = self.get_invalid_test_value('slide_dto', request.slide_dto, 'LayoutSlide')
        self.initialize('put_layout_slide', 'slide_dto', request.slide_dto)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'slide_dto', request.slide_dto)
        if ok:
            self.assert_no_exception('put_layout_slide', 'slide_dto')

    def test_put_layout_slide_invalid_password(self):
        """Test case for put_layout_slide with invalid password
        """
        request = self.__prepare_put_layout_slide_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_layout_slide', 'password', request.password)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'password', request.password)
        if ok:
            self.assert_no_exception('put_layout_slide', 'password')

    def test_put_layout_slide_invalid_folder(self):
        """Test case for put_layout_slide with invalid folder
        """
        request = self.__prepare_put_layout_slide_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_layout_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_layout_slide', 'folder')

    def test_put_layout_slide_invalid_storage(self):
        """Test case for put_layout_slide with invalid storage
        """
        request = self.__prepare_put_layout_slide_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_layout_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_layout_slide', 'storage')

    def __prepare_put_layout_slide_request(self):
        name = self.get_test_value('put_layout_slide', 'name', 'str')
        slide_index = self.get_test_value('put_layout_slide', 'slide_index', 'int')
        slide_dto = self.get_test_value('put_layout_slide', 'slide_dto', 'LayoutSlide')
        password = self.get_test_value('put_layout_slide', 'password', 'str')
        folder = self.get_test_value('put_layout_slide', 'folder', 'str')
        storage = self.get_test_value('put_layout_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.layout_slides_api_requests.PutLayoutSlideRequest(name, slide_index, slide_dto, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
