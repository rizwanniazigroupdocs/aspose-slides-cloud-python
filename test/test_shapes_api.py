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
from asposeslidescloud.apis.shapes_api import ShapesApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestShapesApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.shapes_api.ShapesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_paragraph(self):
        """Test case for delete_paragraph
        """
        request = self.__prepare_delete_paragraph_request()
        self.initialize('delete_paragraph', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_paragraph')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_paragraph_invalid_name(self):
        """Test case for delete_paragraph with invalid name
        """
        request = self.__prepare_delete_paragraph_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_paragraph', 'name')

    def test_delete_paragraph_invalid_slide_index(self):
        """Test case for delete_paragraph with invalid slide_index
        """
        request = self.__prepare_delete_paragraph_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_paragraph', 'slide_index')

    def test_delete_paragraph_invalid_shape_index(self):
        """Test case for delete_paragraph with invalid shape_index
        """
        request = self.__prepare_delete_paragraph_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('delete_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('delete_paragraph', 'shape_index')

    def test_delete_paragraph_invalid_paragraph_index(self):
        """Test case for delete_paragraph with invalid paragraph_index
        """
        request = self.__prepare_delete_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('delete_paragraph', 'paragraph_index')

    def test_delete_paragraph_invalid_path(self):
        """Test case for delete_paragraph with invalid path
        """
        request = self.__prepare_delete_paragraph_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('delete_paragraph', 'path', request.path)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'path', request.path)
        if ok:
            self.assert_no_exception('delete_paragraph', 'path')

    def test_delete_paragraph_invalid_password(self):
        """Test case for delete_paragraph with invalid password
        """
        request = self.__prepare_delete_paragraph_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_paragraph', 'password')

    def test_delete_paragraph_invalid_folder(self):
        """Test case for delete_paragraph with invalid folder
        """
        request = self.__prepare_delete_paragraph_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_paragraph', 'folder')

    def test_delete_paragraph_invalid_storage(self):
        """Test case for delete_paragraph with invalid storage
        """
        request = self.__prepare_delete_paragraph_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_paragraph', 'storage')

    def __prepare_delete_paragraph_request(self):
        name = self.get_test_value('delete_paragraph', 'name', 'str')
        slide_index = self.get_test_value('delete_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_paragraph', 'paragraph_index', 'int')
        path = self.get_test_value('delete_paragraph', 'path', 'str')
        password = self.get_test_value('delete_paragraph', 'password', 'str')
        folder = self.get_test_value('delete_paragraph', 'folder', 'str')
        storage = self.get_test_value('delete_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.DeleteParagraphRequest(name, slide_index, shape_index, paragraph_index, path, password, folder, storage)

    def test_delete_paragraphs(self):
        """Test case for delete_paragraphs
        """
        request = self.__prepare_delete_paragraphs_request()
        self.initialize('delete_paragraphs', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_paragraphs')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_paragraphs_invalid_name(self):
        """Test case for delete_paragraphs with invalid name
        """
        request = self.__prepare_delete_paragraphs_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'name')

    def test_delete_paragraphs_invalid_slide_index(self):
        """Test case for delete_paragraphs with invalid slide_index
        """
        request = self.__prepare_delete_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'slide_index')

    def test_delete_paragraphs_invalid_shape_index(self):
        """Test case for delete_paragraphs with invalid shape_index
        """
        request = self.__prepare_delete_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('delete_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'shape_index')

    def test_delete_paragraphs_invalid_path(self):
        """Test case for delete_paragraphs with invalid path
        """
        request = self.__prepare_delete_paragraphs_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('delete_paragraphs', 'path', request.path)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'path', request.path)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'path')

    def test_delete_paragraphs_invalid_paragraphs(self):
        """Test case for delete_paragraphs with invalid paragraphs
        """
        request = self.__prepare_delete_paragraphs_request()
        request.paragraphs = self.get_invalid_test_value('paragraphs', request.paragraphs, 'list[int]')
        self.initialize('delete_paragraphs', 'paragraphs', request.paragraphs)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'paragraphs', request.paragraphs)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'paragraphs')

    def test_delete_paragraphs_invalid_password(self):
        """Test case for delete_paragraphs with invalid password
        """
        request = self.__prepare_delete_paragraphs_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'password')

    def test_delete_paragraphs_invalid_folder(self):
        """Test case for delete_paragraphs with invalid folder
        """
        request = self.__prepare_delete_paragraphs_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'folder')

    def test_delete_paragraphs_invalid_storage(self):
        """Test case for delete_paragraphs with invalid storage
        """
        request = self.__prepare_delete_paragraphs_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_paragraphs', 'storage')

    def __prepare_delete_paragraphs_request(self):
        name = self.get_test_value('delete_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('delete_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_paragraphs', 'shape_index', 'int')
        path = self.get_test_value('delete_paragraphs', 'path', 'str')
        paragraphs = self.get_test_value('delete_paragraphs', 'paragraphs', 'list[int]')
        password = self.get_test_value('delete_paragraphs', 'password', 'str')
        folder = self.get_test_value('delete_paragraphs', 'folder', 'str')
        storage = self.get_test_value('delete_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.DeleteParagraphsRequest(name, slide_index, shape_index, path, paragraphs, password, folder, storage)

    def test_delete_portion(self):
        """Test case for delete_portion
        """
        request = self.__prepare_delete_portion_request()
        self.initialize('delete_portion', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_portion')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_portion_invalid_name(self):
        """Test case for delete_portion with invalid name
        """
        request = self.__prepare_delete_portion_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_portion', 'name', request.name)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_portion', 'name')

    def test_delete_portion_invalid_slide_index(self):
        """Test case for delete_portion with invalid slide_index
        """
        request = self.__prepare_delete_portion_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_portion', 'slide_index')

    def test_delete_portion_invalid_shape_index(self):
        """Test case for delete_portion with invalid shape_index
        """
        request = self.__prepare_delete_portion_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('delete_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('delete_portion', 'shape_index')

    def test_delete_portion_invalid_paragraph_index(self):
        """Test case for delete_portion with invalid paragraph_index
        """
        request = self.__prepare_delete_portion_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('delete_portion', 'paragraph_index')

    def test_delete_portion_invalid_portion_index(self):
        """Test case for delete_portion with invalid portion_index
        """
        request = self.__prepare_delete_portion_request()
        request.portion_index = self.get_invalid_test_value('portion_index', request.portion_index, 'int')
        self.initialize('delete_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'portion_index', request.portion_index)
        if ok:
            self.assert_no_exception('delete_portion', 'portion_index')

    def test_delete_portion_invalid_path(self):
        """Test case for delete_portion with invalid path
        """
        request = self.__prepare_delete_portion_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('delete_portion', 'path', request.path)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'path', request.path)
        if ok:
            self.assert_no_exception('delete_portion', 'path')

    def test_delete_portion_invalid_password(self):
        """Test case for delete_portion with invalid password
        """
        request = self.__prepare_delete_portion_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_portion', 'password', request.password)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_portion', 'password')

    def test_delete_portion_invalid_folder(self):
        """Test case for delete_portion with invalid folder
        """
        request = self.__prepare_delete_portion_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_portion', 'folder')

    def test_delete_portion_invalid_storage(self):
        """Test case for delete_portion with invalid storage
        """
        request = self.__prepare_delete_portion_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_portion', 'storage')

    def __prepare_delete_portion_request(self):
        name = self.get_test_value('delete_portion', 'name', 'str')
        slide_index = self.get_test_value('delete_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('delete_portion', 'portion_index', 'int')
        path = self.get_test_value('delete_portion', 'path', 'str')
        password = self.get_test_value('delete_portion', 'password', 'str')
        folder = self.get_test_value('delete_portion', 'folder', 'str')
        storage = self.get_test_value('delete_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.DeletePortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, path, password, folder, storage)

    def test_delete_portions(self):
        """Test case for delete_portions
        """
        request = self.__prepare_delete_portions_request()
        self.initialize('delete_portions', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_portions')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_portions_invalid_name(self):
        """Test case for delete_portions with invalid name
        """
        request = self.__prepare_delete_portions_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_portions', 'name', request.name)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_portions', 'name')

    def test_delete_portions_invalid_slide_index(self):
        """Test case for delete_portions with invalid slide_index
        """
        request = self.__prepare_delete_portions_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_portions', 'slide_index')

    def test_delete_portions_invalid_shape_index(self):
        """Test case for delete_portions with invalid shape_index
        """
        request = self.__prepare_delete_portions_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('delete_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('delete_portions', 'shape_index')

    def test_delete_portions_invalid_paragraph_index(self):
        """Test case for delete_portions with invalid paragraph_index
        """
        request = self.__prepare_delete_portions_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('delete_portions', 'paragraph_index')

    def test_delete_portions_invalid_path(self):
        """Test case for delete_portions with invalid path
        """
        request = self.__prepare_delete_portions_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('delete_portions', 'path', request.path)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'path', request.path)
        if ok:
            self.assert_no_exception('delete_portions', 'path')

    def test_delete_portions_invalid_portions(self):
        """Test case for delete_portions with invalid portions
        """
        request = self.__prepare_delete_portions_request()
        request.portions = self.get_invalid_test_value('portions', request.portions, 'list[int]')
        self.initialize('delete_portions', 'portions', request.portions)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'portions', request.portions)
        if ok:
            self.assert_no_exception('delete_portions', 'portions')

    def test_delete_portions_invalid_password(self):
        """Test case for delete_portions with invalid password
        """
        request = self.__prepare_delete_portions_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_portions', 'password', request.password)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_portions', 'password')

    def test_delete_portions_invalid_folder(self):
        """Test case for delete_portions with invalid folder
        """
        request = self.__prepare_delete_portions_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_portions', 'folder')

    def test_delete_portions_invalid_storage(self):
        """Test case for delete_portions with invalid storage
        """
        request = self.__prepare_delete_portions_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_portions', 'storage')

    def __prepare_delete_portions_request(self):
        name = self.get_test_value('delete_portions', 'name', 'str')
        slide_index = self.get_test_value('delete_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_portions', 'paragraph_index', 'int')
        path = self.get_test_value('delete_portions', 'path', 'str')
        portions = self.get_test_value('delete_portions', 'portions', 'list[int]')
        password = self.get_test_value('delete_portions', 'password', 'str')
        folder = self.get_test_value('delete_portions', 'folder', 'str')
        storage = self.get_test_value('delete_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.DeletePortionsRequest(name, slide_index, shape_index, paragraph_index, path, portions, password, folder, storage)

    def test_delete_slide_shape(self):
        """Test case for delete_slide_shape
        """
        request = self.__prepare_delete_slide_shape_request()
        self.initialize('delete_slide_shape', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slide_shape')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slide_shape_invalid_name(self):
        """Test case for delete_slide_shape with invalid name
        """
        request = self.__prepare_delete_slide_shape_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'name')

    def test_delete_slide_shape_invalid_slide_index(self):
        """Test case for delete_slide_shape with invalid slide_index
        """
        request = self.__prepare_delete_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'slide_index')

    def test_delete_slide_shape_invalid_shape_index(self):
        """Test case for delete_slide_shape with invalid shape_index
        """
        request = self.__prepare_delete_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('delete_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'shape_index')

    def test_delete_slide_shape_invalid_path(self):
        """Test case for delete_slide_shape with invalid path
        """
        request = self.__prepare_delete_slide_shape_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('delete_slide_shape', 'path', request.path)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'path', request.path)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'path')

    def test_delete_slide_shape_invalid_password(self):
        """Test case for delete_slide_shape with invalid password
        """
        request = self.__prepare_delete_slide_shape_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'password')

    def test_delete_slide_shape_invalid_folder(self):
        """Test case for delete_slide_shape with invalid folder
        """
        request = self.__prepare_delete_slide_shape_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'folder')

    def test_delete_slide_shape_invalid_storage(self):
        """Test case for delete_slide_shape with invalid storage
        """
        request = self.__prepare_delete_slide_shape_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slide_shape', 'storage')

    def __prepare_delete_slide_shape_request(self):
        name = self.get_test_value('delete_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_slide_shape', 'shape_index', 'int')
        path = self.get_test_value('delete_slide_shape', 'path', 'str')
        password = self.get_test_value('delete_slide_shape', 'password', 'str')
        folder = self.get_test_value('delete_slide_shape', 'folder', 'str')
        storage = self.get_test_value('delete_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.DeleteSlideShapeRequest(name, slide_index, shape_index, path, password, folder, storage)

    def test_delete_slide_shapes(self):
        """Test case for delete_slide_shapes
        """
        request = self.__prepare_delete_slide_shapes_request()
        self.initialize('delete_slide_shapes', None, None)
        response = None
        ok = False
        try:
            response = self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'delete_slide_shapes')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_delete_slide_shapes_invalid_name(self):
        """Test case for delete_slide_shapes with invalid name
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('delete_slide_shapes', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'name', request.name)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'name')

    def test_delete_slide_shapes_invalid_slide_index(self):
        """Test case for delete_slide_shapes with invalid slide_index
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_shapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'slide_index')

    def test_delete_slide_shapes_invalid_path(self):
        """Test case for delete_slide_shapes with invalid path
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('delete_slide_shapes', 'path', request.path)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'path', request.path)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'path')

    def test_delete_slide_shapes_invalid_shapes(self):
        """Test case for delete_slide_shapes with invalid shapes
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.shapes = self.get_invalid_test_value('shapes', request.shapes, 'list[int]')
        self.initialize('delete_slide_shapes', 'shapes', request.shapes)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'shapes', request.shapes)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'shapes')

    def test_delete_slide_shapes_invalid_password(self):
        """Test case for delete_slide_shapes with invalid password
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('delete_slide_shapes', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'password', request.password)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'password')

    def test_delete_slide_shapes_invalid_folder(self):
        """Test case for delete_slide_shapes with invalid folder
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('delete_slide_shapes', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'folder', request.folder)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'folder')

    def test_delete_slide_shapes_invalid_storage(self):
        """Test case for delete_slide_shapes with invalid storage
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('delete_slide_shapes', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'storage', request.storage)
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'storage')

    def __prepare_delete_slide_shapes_request(self):
        name = self.get_test_value('delete_slide_shapes', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_shapes', 'slide_index', 'int')
        path = self.get_test_value('delete_slide_shapes', 'path', 'str')
        shapes = self.get_test_value('delete_slide_shapes', 'shapes', 'list[int]')
        password = self.get_test_value('delete_slide_shapes', 'password', 'str')
        folder = self.get_test_value('delete_slide_shapes', 'folder', 'str')
        storage = self.get_test_value('delete_slide_shapes', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.DeleteSlideShapesRequest(name, slide_index, path, shapes, password, folder, storage)

    def test_get_paragraph_portion(self):
        """Test case for get_paragraph_portion
        """
        request = self.__prepare_get_paragraph_portion_request()
        self.initialize('get_paragraph_portion', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_paragraph_portion')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_paragraph_portion_invalid_name(self):
        """Test case for get_paragraph_portion with invalid name
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_paragraph_portion', 'name', request.name)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'name', request.name)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'name')

    def test_get_paragraph_portion_invalid_slide_index(self):
        """Test case for get_paragraph_portion with invalid slide_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_paragraph_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'slide_index')

    def test_get_paragraph_portion_invalid_shape_index(self):
        """Test case for get_paragraph_portion with invalid shape_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('get_paragraph_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'shape_index')

    def test_get_paragraph_portion_invalid_paragraph_index(self):
        """Test case for get_paragraph_portion with invalid paragraph_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_paragraph_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'paragraph_index')

    def test_get_paragraph_portion_invalid_portion_index(self):
        """Test case for get_paragraph_portion with invalid portion_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.portion_index = self.get_invalid_test_value('portion_index', request.portion_index, 'int')
        self.initialize('get_paragraph_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'portion_index', request.portion_index)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'portion_index')

    def test_get_paragraph_portion_invalid_path(self):
        """Test case for get_paragraph_portion with invalid path
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('get_paragraph_portion', 'path', request.path)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'path', request.path)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'path')

    def test_get_paragraph_portion_invalid_password(self):
        """Test case for get_paragraph_portion with invalid password
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_paragraph_portion', 'password', request.password)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'password', request.password)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'password')

    def test_get_paragraph_portion_invalid_folder(self):
        """Test case for get_paragraph_portion with invalid folder
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_paragraph_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'folder')

    def test_get_paragraph_portion_invalid_storage(self):
        """Test case for get_paragraph_portion with invalid storage
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_paragraph_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'storage')

    def __prepare_get_paragraph_portion_request(self):
        name = self.get_test_value('get_paragraph_portion', 'name', 'str')
        slide_index = self.get_test_value('get_paragraph_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('get_paragraph_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_paragraph_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('get_paragraph_portion', 'portion_index', 'int')
        path = self.get_test_value('get_paragraph_portion', 'path', 'str')
        password = self.get_test_value('get_paragraph_portion', 'password', 'str')
        folder = self.get_test_value('get_paragraph_portion', 'folder', 'str')
        storage = self.get_test_value('get_paragraph_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetParagraphPortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, path, password, folder, storage)

    def test_get_paragraph_portions(self):
        """Test case for get_paragraph_portions
        """
        request = self.__prepare_get_paragraph_portions_request()
        self.initialize('get_paragraph_portions', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_paragraph_portions')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_paragraph_portions_invalid_name(self):
        """Test case for get_paragraph_portions with invalid name
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_paragraph_portions', 'name', request.name)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'name', request.name)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'name')

    def test_get_paragraph_portions_invalid_slide_index(self):
        """Test case for get_paragraph_portions with invalid slide_index
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_paragraph_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'slide_index')

    def test_get_paragraph_portions_invalid_shape_index(self):
        """Test case for get_paragraph_portions with invalid shape_index
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('get_paragraph_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'shape_index')

    def test_get_paragraph_portions_invalid_paragraph_index(self):
        """Test case for get_paragraph_portions with invalid paragraph_index
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_paragraph_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'paragraph_index')

    def test_get_paragraph_portions_invalid_path(self):
        """Test case for get_paragraph_portions with invalid path
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('get_paragraph_portions', 'path', request.path)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'path', request.path)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'path')

    def test_get_paragraph_portions_invalid_password(self):
        """Test case for get_paragraph_portions with invalid password
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_paragraph_portions', 'password', request.password)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'password', request.password)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'password')

    def test_get_paragraph_portions_invalid_folder(self):
        """Test case for get_paragraph_portions with invalid folder
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_paragraph_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'folder')

    def test_get_paragraph_portions_invalid_storage(self):
        """Test case for get_paragraph_portions with invalid storage
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_paragraph_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'storage')

    def __prepare_get_paragraph_portions_request(self):
        name = self.get_test_value('get_paragraph_portions', 'name', 'str')
        slide_index = self.get_test_value('get_paragraph_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('get_paragraph_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_paragraph_portions', 'paragraph_index', 'int')
        path = self.get_test_value('get_paragraph_portions', 'path', 'str')
        password = self.get_test_value('get_paragraph_portions', 'password', 'str')
        folder = self.get_test_value('get_paragraph_portions', 'folder', 'str')
        storage = self.get_test_value('get_paragraph_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetParagraphPortionsRequest(name, slide_index, shape_index, paragraph_index, path, password, folder, storage)

    def test_get_shape_paragraph(self):
        """Test case for get_shape_paragraph
        """
        request = self.__prepare_get_shape_paragraph_request()
        self.initialize('get_shape_paragraph', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_shape_paragraph')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_shape_paragraph_invalid_name(self):
        """Test case for get_shape_paragraph with invalid name
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_shape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'name', request.name)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'name')

    def test_get_shape_paragraph_invalid_slide_index(self):
        """Test case for get_shape_paragraph with invalid slide_index
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_shape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'slide_index')

    def test_get_shape_paragraph_invalid_shape_index(self):
        """Test case for get_shape_paragraph with invalid shape_index
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('get_shape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'shape_index')

    def test_get_shape_paragraph_invalid_paragraph_index(self):
        """Test case for get_shape_paragraph with invalid paragraph_index
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_shape_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'paragraph_index')

    def test_get_shape_paragraph_invalid_path(self):
        """Test case for get_shape_paragraph with invalid path
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('get_shape_paragraph', 'path', request.path)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'path', request.path)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'path')

    def test_get_shape_paragraph_invalid_password(self):
        """Test case for get_shape_paragraph with invalid password
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_shape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'password', request.password)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'password')

    def test_get_shape_paragraph_invalid_folder(self):
        """Test case for get_shape_paragraph with invalid folder
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_shape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'folder')

    def test_get_shape_paragraph_invalid_storage(self):
        """Test case for get_shape_paragraph with invalid storage
        """
        request = self.__prepare_get_shape_paragraph_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_shape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.get_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_paragraph', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_shape_paragraph', 'storage')

    def __prepare_get_shape_paragraph_request(self):
        name = self.get_test_value('get_shape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('get_shape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('get_shape_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_shape_paragraph', 'paragraph_index', 'int')
        path = self.get_test_value('get_shape_paragraph', 'path', 'str')
        password = self.get_test_value('get_shape_paragraph', 'password', 'str')
        folder = self.get_test_value('get_shape_paragraph', 'folder', 'str')
        storage = self.get_test_value('get_shape_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetShapeParagraphRequest(name, slide_index, shape_index, paragraph_index, path, password, folder, storage)

    def test_get_shape_with_format(self):
        """Test case for get_shape_with_format
        """
        request = self.__prepare_get_shape_with_format_request()
        self.initialize('get_shape_with_format', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_shape_with_format')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_get_shape_with_format_invalid_name(self):
        """Test case for get_shape_with_format with invalid name
        """
        request = self.__prepare_get_shape_with_format_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_shape_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'name', request.name)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'name')

    def test_get_shape_with_format_invalid_slide_index(self):
        """Test case for get_shape_with_format with invalid slide_index
        """
        request = self.__prepare_get_shape_with_format_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_shape_with_format', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'slide_index')

    def test_get_shape_with_format_invalid_shape_index(self):
        """Test case for get_shape_with_format with invalid shape_index
        """
        request = self.__prepare_get_shape_with_format_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('get_shape_with_format', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'shape_index')

    def test_get_shape_with_format_invalid_format(self):
        """Test case for get_shape_with_format with invalid format
        """
        request = self.__prepare_get_shape_with_format_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('get_shape_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'format', request.format)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'format')

    def test_get_shape_with_format_invalid_password(self):
        """Test case for get_shape_with_format with invalid password
        """
        request = self.__prepare_get_shape_with_format_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_shape_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'password', request.password)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'password')

    def test_get_shape_with_format_invalid_folder(self):
        """Test case for get_shape_with_format with invalid folder
        """
        request = self.__prepare_get_shape_with_format_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_shape_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'folder')

    def test_get_shape_with_format_invalid_storage(self):
        """Test case for get_shape_with_format with invalid storage
        """
        request = self.__prepare_get_shape_with_format_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_shape_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'storage')

    def test_get_shape_with_format_invalid_scale_x(self):
        """Test case for get_shape_with_format with invalid scale_x
        """
        request = self.__prepare_get_shape_with_format_request()
        request.scale_x = self.get_invalid_test_value('scale_x', request.scale_x, 'float')
        self.initialize('get_shape_with_format', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'scale_x', request.scale_x)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'scale_x')

    def test_get_shape_with_format_invalid_scale_y(self):
        """Test case for get_shape_with_format with invalid scale_y
        """
        request = self.__prepare_get_shape_with_format_request()
        request.scale_y = self.get_invalid_test_value('scale_y', request.scale_y, 'float')
        self.initialize('get_shape_with_format', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'scale_y', request.scale_y)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'scale_y')

    def test_get_shape_with_format_invalid_bounds(self):
        """Test case for get_shape_with_format with invalid bounds
        """
        request = self.__prepare_get_shape_with_format_request()
        request.bounds = self.get_invalid_test_value('bounds', request.bounds, 'str')
        self.initialize('get_shape_with_format', 'bounds', request.bounds)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'bounds', request.bounds)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'bounds')

    def test_get_shape_with_format_invalid_out_path(self):
        """Test case for get_shape_with_format with invalid out_path
        """
        request = self.__prepare_get_shape_with_format_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('get_shape_with_format', 'out_path', request.out_path)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'out_path')

    def test_get_shape_with_format_invalid_fonts_folder(self):
        """Test case for get_shape_with_format with invalid fonts_folder
        """
        request = self.__prepare_get_shape_with_format_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('get_shape_with_format', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.get_shape_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_shape_with_format', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('get_shape_with_format', 'fonts_folder')

    def __prepare_get_shape_with_format_request(self):
        name = self.get_test_value('get_shape_with_format', 'name', 'str')
        slide_index = self.get_test_value('get_shape_with_format', 'slide_index', 'int')
        shape_index = self.get_test_value('get_shape_with_format', 'shape_index', 'int')
        format = self.get_test_value('get_shape_with_format', 'format', 'str')
        password = self.get_test_value('get_shape_with_format', 'password', 'str')
        folder = self.get_test_value('get_shape_with_format', 'folder', 'str')
        storage = self.get_test_value('get_shape_with_format', 'storage', 'str')
        scale_x = self.get_test_value('get_shape_with_format', 'scale_x', 'float')
        scale_y = self.get_test_value('get_shape_with_format', 'scale_y', 'float')
        bounds = self.get_test_value('get_shape_with_format', 'bounds', 'str')
        out_path = self.get_test_value('get_shape_with_format', 'out_path', 'str')
        fonts_folder = self.get_test_value('get_shape_with_format', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetShapeWithFormatRequest(name, slide_index, shape_index, format, password, folder, storage, scale_x, scale_y, bounds, out_path, fonts_folder)

    def test_get_slide_shape(self):
        """Test case for get_slide_shape
        """
        request = self.__prepare_get_slide_shape_request()
        self.initialize('get_slide_shape', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slide_shape')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slide_shape_invalid_name(self):
        """Test case for get_slide_shape with invalid name
        """
        request = self.__prepare_get_slide_shape_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slide_shape', 'name')

    def test_get_slide_shape_invalid_slide_index(self):
        """Test case for get_slide_shape with invalid slide_index
        """
        request = self.__prepare_get_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slide_shape', 'slide_index')

    def test_get_slide_shape_invalid_shape_index(self):
        """Test case for get_slide_shape with invalid shape_index
        """
        request = self.__prepare_get_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('get_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('get_slide_shape', 'shape_index')

    def test_get_slide_shape_invalid_path(self):
        """Test case for get_slide_shape with invalid path
        """
        request = self.__prepare_get_slide_shape_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('get_slide_shape', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'path', request.path)
        if ok:
            self.assert_no_exception('get_slide_shape', 'path')

    def test_get_slide_shape_invalid_password(self):
        """Test case for get_slide_shape with invalid password
        """
        request = self.__prepare_get_slide_shape_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slide_shape', 'password')

    def test_get_slide_shape_invalid_folder(self):
        """Test case for get_slide_shape with invalid folder
        """
        request = self.__prepare_get_slide_shape_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slide_shape', 'folder')

    def test_get_slide_shape_invalid_storage(self):
        """Test case for get_slide_shape with invalid storage
        """
        request = self.__prepare_get_slide_shape_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slide_shape', 'storage')

    def __prepare_get_slide_shape_request(self):
        name = self.get_test_value('get_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_shape', 'shape_index', 'int')
        path = self.get_test_value('get_slide_shape', 'path', 'str')
        password = self.get_test_value('get_slide_shape', 'password', 'str')
        folder = self.get_test_value('get_slide_shape', 'folder', 'str')
        storage = self.get_test_value('get_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetSlideShapeRequest(name, slide_index, shape_index, path, password, folder, storage)

    def test_get_slide_shape_paragraphs(self):
        """Test case for get_slide_shape_paragraphs
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        self.initialize('get_slide_shape_paragraphs', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slide_shape_paragraphs')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slide_shape_paragraphs_invalid_name(self):
        """Test case for get_slide_shape_paragraphs with invalid name
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slide_shape_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'name')

    def test_get_slide_shape_paragraphs_invalid_slide_index(self):
        """Test case for get_slide_shape_paragraphs with invalid slide_index
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shape_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'slide_index')

    def test_get_slide_shape_paragraphs_invalid_shape_index(self):
        """Test case for get_slide_shape_paragraphs with invalid shape_index
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('get_slide_shape_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'shape_index')

    def test_get_slide_shape_paragraphs_invalid_path(self):
        """Test case for get_slide_shape_paragraphs with invalid path
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('get_slide_shape_paragraphs', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'path', request.path)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'path')

    def test_get_slide_shape_paragraphs_invalid_password(self):
        """Test case for get_slide_shape_paragraphs with invalid password
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slide_shape_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'password')

    def test_get_slide_shape_paragraphs_invalid_folder(self):
        """Test case for get_slide_shape_paragraphs with invalid folder
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slide_shape_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'folder')

    def test_get_slide_shape_paragraphs_invalid_storage(self):
        """Test case for get_slide_shape_paragraphs with invalid storage
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slide_shape_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'storage')

    def __prepare_get_slide_shape_paragraphs_request(self):
        name = self.get_test_value('get_slide_shape_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shape_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_shape_paragraphs', 'shape_index', 'int')
        path = self.get_test_value('get_slide_shape_paragraphs', 'path', 'str')
        password = self.get_test_value('get_slide_shape_paragraphs', 'password', 'str')
        folder = self.get_test_value('get_slide_shape_paragraphs', 'folder', 'str')
        storage = self.get_test_value('get_slide_shape_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetSlideShapeParagraphsRequest(name, slide_index, shape_index, path, password, folder, storage)

    def test_get_slide_shapes(self):
        """Test case for get_slide_shapes
        """
        request = self.__prepare_get_slide_shapes_request()
        self.initialize('get_slide_shapes', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slide_shapes')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slide_shapes_invalid_name(self):
        """Test case for get_slide_shapes with invalid name
        """
        request = self.__prepare_get_slide_shapes_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slide_shapes', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slide_shapes', 'name')

    def test_get_slide_shapes_invalid_slide_index(self):
        """Test case for get_slide_shapes with invalid slide_index
        """
        request = self.__prepare_get_slide_shapes_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('get_slide_shapes', 'slide_index')

    def test_get_slide_shapes_invalid_path(self):
        """Test case for get_slide_shapes with invalid path
        """
        request = self.__prepare_get_slide_shapes_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('get_slide_shapes', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'path', request.path)
        if ok:
            self.assert_no_exception('get_slide_shapes', 'path')

    def test_get_slide_shapes_invalid_password(self):
        """Test case for get_slide_shapes with invalid password
        """
        request = self.__prepare_get_slide_shapes_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slide_shapes', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slide_shapes', 'password')

    def test_get_slide_shapes_invalid_folder(self):
        """Test case for get_slide_shapes with invalid folder
        """
        request = self.__prepare_get_slide_shapes_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slide_shapes', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slide_shapes', 'folder')

    def test_get_slide_shapes_invalid_storage(self):
        """Test case for get_slide_shapes with invalid storage
        """
        request = self.__prepare_get_slide_shapes_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slide_shapes', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slide_shapes', 'storage')

    def __prepare_get_slide_shapes_request(self):
        name = self.get_test_value('get_slide_shapes', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shapes', 'slide_index', 'int')
        path = self.get_test_value('get_slide_shapes', 'path', 'str')
        password = self.get_test_value('get_slide_shapes', 'password', 'str')
        folder = self.get_test_value('get_slide_shapes', 'folder', 'str')
        storage = self.get_test_value('get_slide_shapes', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.GetSlideShapesRequest(name, slide_index, path, password, folder, storage)

    def test_post_add_new_paragraph(self):
        """Test case for post_add_new_paragraph
        """
        request = self.__prepare_post_add_new_paragraph_request()
        self.initialize('post_add_new_paragraph', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_add_new_paragraph')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_add_new_paragraph_invalid_name(self):
        """Test case for post_add_new_paragraph with invalid name
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_add_new_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'name', request.name)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'name')

    def test_post_add_new_paragraph_invalid_slide_index(self):
        """Test case for post_add_new_paragraph with invalid slide_index
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'slide_index')

    def test_post_add_new_paragraph_invalid_shape_index(self):
        """Test case for post_add_new_paragraph with invalid shape_index
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('post_add_new_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'shape_index')

    def test_post_add_new_paragraph_invalid_path(self):
        """Test case for post_add_new_paragraph with invalid path
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('post_add_new_paragraph', 'path', request.path)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'path', request.path)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'path')

    def test_post_add_new_paragraph_invalid_dto(self):
        """Test case for post_add_new_paragraph with invalid dto
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'Paragraph')
        self.initialize('post_add_new_paragraph', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'dto', request.dto)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'dto')

    def test_post_add_new_paragraph_invalid_password(self):
        """Test case for post_add_new_paragraph with invalid password
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_add_new_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'password', request.password)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'password')

    def test_post_add_new_paragraph_invalid_folder(self):
        """Test case for post_add_new_paragraph with invalid folder
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_add_new_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'folder')

    def test_post_add_new_paragraph_invalid_storage(self):
        """Test case for post_add_new_paragraph with invalid storage
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_add_new_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'storage')

    def test_post_add_new_paragraph_invalid_position(self):
        """Test case for post_add_new_paragraph with invalid position
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.position = self.get_invalid_test_value('position', request.position, 'int')
        self.initialize('post_add_new_paragraph', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'position', request.position)
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'position')

    def __prepare_post_add_new_paragraph_request(self):
        name = self.get_test_value('post_add_new_paragraph', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('post_add_new_paragraph', 'shape_index', 'int')
        path = self.get_test_value('post_add_new_paragraph', 'path', 'str')
        dto = self.get_test_value('post_add_new_paragraph', 'dto', 'Paragraph')
        password = self.get_test_value('post_add_new_paragraph', 'password', 'str')
        folder = self.get_test_value('post_add_new_paragraph', 'folder', 'str')
        storage = self.get_test_value('post_add_new_paragraph', 'storage', 'str')
        position = self.get_test_value('post_add_new_paragraph', 'position', 'int')
        return asposeslidescloud.models.requests.shapes_api_requests.PostAddNewParagraphRequest(name, slide_index, shape_index, path, dto, password, folder, storage, position)

    def test_post_add_new_portion(self):
        """Test case for post_add_new_portion
        """
        request = self.__prepare_post_add_new_portion_request()
        self.initialize('post_add_new_portion', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_add_new_portion')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_add_new_portion_invalid_name(self):
        """Test case for post_add_new_portion with invalid name
        """
        request = self.__prepare_post_add_new_portion_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_add_new_portion', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'name', request.name)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'name')

    def test_post_add_new_portion_invalid_slide_index(self):
        """Test case for post_add_new_portion with invalid slide_index
        """
        request = self.__prepare_post_add_new_portion_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'slide_index')

    def test_post_add_new_portion_invalid_shape_index(self):
        """Test case for post_add_new_portion with invalid shape_index
        """
        request = self.__prepare_post_add_new_portion_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('post_add_new_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'shape_index')

    def test_post_add_new_portion_invalid_paragraph_index(self):
        """Test case for post_add_new_portion with invalid paragraph_index
        """
        request = self.__prepare_post_add_new_portion_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('post_add_new_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'paragraph_index')

    def test_post_add_new_portion_invalid_path(self):
        """Test case for post_add_new_portion with invalid path
        """
        request = self.__prepare_post_add_new_portion_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('post_add_new_portion', 'path', request.path)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'path', request.path)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'path')

    def test_post_add_new_portion_invalid_dto(self):
        """Test case for post_add_new_portion with invalid dto
        """
        request = self.__prepare_post_add_new_portion_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'Portion')
        self.initialize('post_add_new_portion', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'dto', request.dto)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'dto')

    def test_post_add_new_portion_invalid_password(self):
        """Test case for post_add_new_portion with invalid password
        """
        request = self.__prepare_post_add_new_portion_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_add_new_portion', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'password', request.password)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'password')

    def test_post_add_new_portion_invalid_folder(self):
        """Test case for post_add_new_portion with invalid folder
        """
        request = self.__prepare_post_add_new_portion_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_add_new_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'folder')

    def test_post_add_new_portion_invalid_storage(self):
        """Test case for post_add_new_portion with invalid storage
        """
        request = self.__prepare_post_add_new_portion_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_add_new_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'storage')

    def test_post_add_new_portion_invalid_position(self):
        """Test case for post_add_new_portion with invalid position
        """
        request = self.__prepare_post_add_new_portion_request()
        request.position = self.get_invalid_test_value('position', request.position, 'int')
        self.initialize('post_add_new_portion', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'position', request.position)
        if ok:
            self.assert_no_exception('post_add_new_portion', 'position')

    def __prepare_post_add_new_portion_request(self):
        name = self.get_test_value('post_add_new_portion', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('post_add_new_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('post_add_new_portion', 'paragraph_index', 'int')
        path = self.get_test_value('post_add_new_portion', 'path', 'str')
        dto = self.get_test_value('post_add_new_portion', 'dto', 'Portion')
        password = self.get_test_value('post_add_new_portion', 'password', 'str')
        folder = self.get_test_value('post_add_new_portion', 'folder', 'str')
        storage = self.get_test_value('post_add_new_portion', 'storage', 'str')
        position = self.get_test_value('post_add_new_portion', 'position', 'int')
        return asposeslidescloud.models.requests.shapes_api_requests.PostAddNewPortionRequest(name, slide_index, shape_index, paragraph_index, path, dto, password, folder, storage, position)

    def test_post_add_new_shape(self):
        """Test case for post_add_new_shape
        """
        request = self.__prepare_post_add_new_shape_request()
        self.initialize('post_add_new_shape', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_add_new_shape')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_add_new_shape_invalid_name(self):
        """Test case for post_add_new_shape with invalid name
        """
        request = self.__prepare_post_add_new_shape_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_add_new_shape', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'name', request.name)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'name')

    def test_post_add_new_shape_invalid_slide_index(self):
        """Test case for post_add_new_shape with invalid slide_index
        """
        request = self.__prepare_post_add_new_shape_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'slide_index')

    def test_post_add_new_shape_invalid_path(self):
        """Test case for post_add_new_shape with invalid path
        """
        request = self.__prepare_post_add_new_shape_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('post_add_new_shape', 'path', request.path)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'path', request.path)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'path')

    def test_post_add_new_shape_invalid_dto(self):
        """Test case for post_add_new_shape with invalid dto
        """
        request = self.__prepare_post_add_new_shape_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'ShapeBase')
        self.initialize('post_add_new_shape', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'dto', request.dto)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'dto')

    def test_post_add_new_shape_invalid_password(self):
        """Test case for post_add_new_shape with invalid password
        """
        request = self.__prepare_post_add_new_shape_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_add_new_shape', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'password', request.password)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'password')

    def test_post_add_new_shape_invalid_folder(self):
        """Test case for post_add_new_shape with invalid folder
        """
        request = self.__prepare_post_add_new_shape_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_add_new_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'folder')

    def test_post_add_new_shape_invalid_storage(self):
        """Test case for post_add_new_shape with invalid storage
        """
        request = self.__prepare_post_add_new_shape_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_add_new_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'storage')

    def test_post_add_new_shape_invalid_shape_to_clone(self):
        """Test case for post_add_new_shape with invalid shape_to_clone
        """
        request = self.__prepare_post_add_new_shape_request()
        request.shape_to_clone = self.get_invalid_test_value('shape_to_clone', request.shape_to_clone, 'int')
        self.initialize('post_add_new_shape', 'shape_to_clone', request.shape_to_clone)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'shape_to_clone', request.shape_to_clone)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'shape_to_clone')

    def test_post_add_new_shape_invalid_position(self):
        """Test case for post_add_new_shape with invalid position
        """
        request = self.__prepare_post_add_new_shape_request()
        request.position = self.get_invalid_test_value('position', request.position, 'int')
        self.initialize('post_add_new_shape', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'position', request.position)
        if ok:
            self.assert_no_exception('post_add_new_shape', 'position')

    def __prepare_post_add_new_shape_request(self):
        name = self.get_test_value('post_add_new_shape', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_shape', 'slide_index', 'int')
        path = self.get_test_value('post_add_new_shape', 'path', 'str')
        dto = self.get_test_value('post_add_new_shape', 'dto', 'ShapeBase')
        password = self.get_test_value('post_add_new_shape', 'password', 'str')
        folder = self.get_test_value('post_add_new_shape', 'folder', 'str')
        storage = self.get_test_value('post_add_new_shape', 'storage', 'str')
        shape_to_clone = self.get_test_value('post_add_new_shape', 'shape_to_clone', 'int')
        position = self.get_test_value('post_add_new_shape', 'position', 'int')
        return asposeslidescloud.models.requests.shapes_api_requests.PostAddNewShapeRequest(name, slide_index, path, dto, password, folder, storage, shape_to_clone, position)

    def test_post_shape_save_as(self):
        """Test case for post_shape_save_as
        """
        request = self.__prepare_post_shape_save_as_request()
        self.initialize('post_shape_save_as', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_shape_save_as')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_post_shape_save_as_invalid_name(self):
        """Test case for post_shape_save_as with invalid name
        """
        request = self.__prepare_post_shape_save_as_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_shape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'name', request.name)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'name')

    def test_post_shape_save_as_invalid_slide_index(self):
        """Test case for post_shape_save_as with invalid slide_index
        """
        request = self.__prepare_post_shape_save_as_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('post_shape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'slide_index')

    def test_post_shape_save_as_invalid_shape_index(self):
        """Test case for post_shape_save_as with invalid shape_index
        """
        request = self.__prepare_post_shape_save_as_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('post_shape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'shape_index')

    def test_post_shape_save_as_invalid_format(self):
        """Test case for post_shape_save_as with invalid format
        """
        request = self.__prepare_post_shape_save_as_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('post_shape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'format', request.format)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'format')

    def test_post_shape_save_as_invalid_options(self):
        """Test case for post_shape_save_as with invalid options
        """
        request = self.__prepare_post_shape_save_as_request()
        request.options = self.get_invalid_test_value('options', request.options, 'IShapeExportOptions')
        self.initialize('post_shape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'options', request.options)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'options')

    def test_post_shape_save_as_invalid_password(self):
        """Test case for post_shape_save_as with invalid password
        """
        request = self.__prepare_post_shape_save_as_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_shape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'password', request.password)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'password')

    def test_post_shape_save_as_invalid_folder(self):
        """Test case for post_shape_save_as with invalid folder
        """
        request = self.__prepare_post_shape_save_as_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_shape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'folder')

    def test_post_shape_save_as_invalid_storage(self):
        """Test case for post_shape_save_as with invalid storage
        """
        request = self.__prepare_post_shape_save_as_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_shape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'storage')

    def test_post_shape_save_as_invalid_scale_x(self):
        """Test case for post_shape_save_as with invalid scale_x
        """
        request = self.__prepare_post_shape_save_as_request()
        request.scale_x = self.get_invalid_test_value('scale_x', request.scale_x, 'float')
        self.initialize('post_shape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'scale_x', request.scale_x)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'scale_x')

    def test_post_shape_save_as_invalid_scale_y(self):
        """Test case for post_shape_save_as with invalid scale_y
        """
        request = self.__prepare_post_shape_save_as_request()
        request.scale_y = self.get_invalid_test_value('scale_y', request.scale_y, 'float')
        self.initialize('post_shape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'scale_y', request.scale_y)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'scale_y')

    def test_post_shape_save_as_invalid_bounds(self):
        """Test case for post_shape_save_as with invalid bounds
        """
        request = self.__prepare_post_shape_save_as_request()
        request.bounds = self.get_invalid_test_value('bounds', request.bounds, 'str')
        self.initialize('post_shape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'bounds', request.bounds)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'bounds')

    def test_post_shape_save_as_invalid_out_path(self):
        """Test case for post_shape_save_as with invalid out_path
        """
        request = self.__prepare_post_shape_save_as_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('post_shape_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'out_path')

    def test_post_shape_save_as_invalid_fonts_folder(self):
        """Test case for post_shape_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_shape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_shape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('post_shape_save_as', 'fonts_folder')

    def __prepare_post_shape_save_as_request(self):
        name = self.get_test_value('post_shape_save_as', 'name', 'str')
        slide_index = self.get_test_value('post_shape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('post_shape_save_as', 'shape_index', 'int')
        format = self.get_test_value('post_shape_save_as', 'format', 'str')
        options = self.get_test_value('post_shape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('post_shape_save_as', 'password', 'str')
        folder = self.get_test_value('post_shape_save_as', 'folder', 'str')
        storage = self.get_test_value('post_shape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('post_shape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('post_shape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('post_shape_save_as', 'bounds', 'str')
        out_path = self.get_test_value('post_shape_save_as', 'out_path', 'str')
        fonts_folder = self.get_test_value('post_shape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.PostShapeSaveAsRequest(name, slide_index, shape_index, format, options, password, folder, storage, scale_x, scale_y, bounds, out_path, fonts_folder)

    def test_put_set_paragraph_portion_properties(self):
        """Test case for put_set_paragraph_portion_properties
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        self.initialize('put_set_paragraph_portion_properties', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_set_paragraph_portion_properties')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_set_paragraph_portion_properties_invalid_name(self):
        """Test case for put_set_paragraph_portion_properties with invalid name
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'name', request.name)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'name')

    def test_put_set_paragraph_portion_properties_invalid_slide_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid slide_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'slide_index')

    def test_put_set_paragraph_portion_properties_invalid_shape_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid shape_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'shape_index')

    def test_put_set_paragraph_portion_properties_invalid_paragraph_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid paragraph_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'paragraph_index')

    def test_put_set_paragraph_portion_properties_invalid_portion_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid portion_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.portion_index = self.get_invalid_test_value('portion_index', request.portion_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'portion_index', request.portion_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'portion_index')

    def test_put_set_paragraph_portion_properties_invalid_path(self):
        """Test case for put_set_paragraph_portion_properties with invalid path
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'path', request.path)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'path', request.path)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'path')

    def test_put_set_paragraph_portion_properties_invalid_dto(self):
        """Test case for put_set_paragraph_portion_properties with invalid dto
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'Portion')
        self.initialize('put_set_paragraph_portion_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'dto', request.dto)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'dto')

    def test_put_set_paragraph_portion_properties_invalid_password(self):
        """Test case for put_set_paragraph_portion_properties with invalid password
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'password', request.password)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'password')

    def test_put_set_paragraph_portion_properties_invalid_folder(self):
        """Test case for put_set_paragraph_portion_properties with invalid folder
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'folder')

    def test_put_set_paragraph_portion_properties_invalid_storage(self):
        """Test case for put_set_paragraph_portion_properties with invalid storage
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'storage')

    def __prepare_put_set_paragraph_portion_properties_request(self):
        name = self.get_test_value('put_set_paragraph_portion_properties', 'name', 'str')
        slide_index = self.get_test_value('put_set_paragraph_portion_properties', 'slide_index', 'int')
        shape_index = self.get_test_value('put_set_paragraph_portion_properties', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_set_paragraph_portion_properties', 'paragraph_index', 'int')
        portion_index = self.get_test_value('put_set_paragraph_portion_properties', 'portion_index', 'int')
        path = self.get_test_value('put_set_paragraph_portion_properties', 'path', 'str')
        dto = self.get_test_value('put_set_paragraph_portion_properties', 'dto', 'Portion')
        password = self.get_test_value('put_set_paragraph_portion_properties', 'password', 'str')
        folder = self.get_test_value('put_set_paragraph_portion_properties', 'folder', 'str')
        storage = self.get_test_value('put_set_paragraph_portion_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.PutSetParagraphPortionPropertiesRequest(name, slide_index, shape_index, paragraph_index, portion_index, path, dto, password, folder, storage)

    def test_put_set_paragraph_properties(self):
        """Test case for put_set_paragraph_properties
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        self.initialize('put_set_paragraph_properties', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_set_paragraph_properties')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_set_paragraph_properties_invalid_name(self):
        """Test case for put_set_paragraph_properties with invalid name
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_set_paragraph_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'name', request.name)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'name')

    def test_put_set_paragraph_properties_invalid_slide_index(self):
        """Test case for put_set_paragraph_properties with invalid slide_index
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_set_paragraph_properties', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'slide_index')

    def test_put_set_paragraph_properties_invalid_shape_index(self):
        """Test case for put_set_paragraph_properties with invalid shape_index
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('put_set_paragraph_properties', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'shape_index')

    def test_put_set_paragraph_properties_invalid_paragraph_index(self):
        """Test case for put_set_paragraph_properties with invalid paragraph_index
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.paragraph_index = self.get_invalid_test_value('paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_set_paragraph_properties', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'paragraph_index', request.paragraph_index)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'paragraph_index')

    def test_put_set_paragraph_properties_invalid_path(self):
        """Test case for put_set_paragraph_properties with invalid path
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('put_set_paragraph_properties', 'path', request.path)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'path', request.path)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'path')

    def test_put_set_paragraph_properties_invalid_dto(self):
        """Test case for put_set_paragraph_properties with invalid dto
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'Paragraph')
        self.initialize('put_set_paragraph_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'dto', request.dto)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'dto')

    def test_put_set_paragraph_properties_invalid_password(self):
        """Test case for put_set_paragraph_properties with invalid password
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_set_paragraph_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'password', request.password)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'password')

    def test_put_set_paragraph_properties_invalid_folder(self):
        """Test case for put_set_paragraph_properties with invalid folder
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_set_paragraph_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'folder')

    def test_put_set_paragraph_properties_invalid_storage(self):
        """Test case for put_set_paragraph_properties with invalid storage
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_set_paragraph_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'storage')

    def __prepare_put_set_paragraph_properties_request(self):
        name = self.get_test_value('put_set_paragraph_properties', 'name', 'str')
        slide_index = self.get_test_value('put_set_paragraph_properties', 'slide_index', 'int')
        shape_index = self.get_test_value('put_set_paragraph_properties', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_set_paragraph_properties', 'paragraph_index', 'int')
        path = self.get_test_value('put_set_paragraph_properties', 'path', 'str')
        dto = self.get_test_value('put_set_paragraph_properties', 'dto', 'Paragraph')
        password = self.get_test_value('put_set_paragraph_properties', 'password', 'str')
        folder = self.get_test_value('put_set_paragraph_properties', 'folder', 'str')
        storage = self.get_test_value('put_set_paragraph_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.PutSetParagraphPropertiesRequest(name, slide_index, shape_index, paragraph_index, path, dto, password, folder, storage)

    def test_put_slide_shape_info(self):
        """Test case for put_slide_shape_info
        """
        request = self.__prepare_put_slide_shape_info_request()
        self.initialize('put_slide_shape_info', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slide_shape_info')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_slide_shape_info_invalid_name(self):
        """Test case for put_slide_shape_info with invalid name
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_slide_shape_info', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'name', request.name)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'name')

    def test_put_slide_shape_info_invalid_slide_index(self):
        """Test case for put_slide_shape_info with invalid slide_index
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.slide_index = self.get_invalid_test_value('slide_index', request.slide_index, 'int')
        self.initialize('put_slide_shape_info', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'slide_index', request.slide_index)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'slide_index')

    def test_put_slide_shape_info_invalid_shape_index(self):
        """Test case for put_slide_shape_info with invalid shape_index
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.shape_index = self.get_invalid_test_value('shape_index', request.shape_index, 'int')
        self.initialize('put_slide_shape_info', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'shape_index', request.shape_index)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'shape_index')

    def test_put_slide_shape_info_invalid_path(self):
        """Test case for put_slide_shape_info with invalid path
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.path = self.get_invalid_test_value('path', request.path, 'str')
        self.initialize('put_slide_shape_info', 'path', request.path)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'path', request.path)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'path')

    def test_put_slide_shape_info_invalid_dto(self):
        """Test case for put_slide_shape_info with invalid dto
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.dto = self.get_invalid_test_value('dto', request.dto, 'ShapeBase')
        self.initialize('put_slide_shape_info', 'dto', request.dto)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'dto', request.dto)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'dto')

    def test_put_slide_shape_info_invalid_password(self):
        """Test case for put_slide_shape_info with invalid password
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slide_shape_info', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'password')

    def test_put_slide_shape_info_invalid_folder(self):
        """Test case for put_slide_shape_info with invalid folder
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_slide_shape_info', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'folder')

    def test_put_slide_shape_info_invalid_storage(self):
        """Test case for put_slide_shape_info with invalid storage
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_slide_shape_info', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'storage')

    def __prepare_put_slide_shape_info_request(self):
        name = self.get_test_value('put_slide_shape_info', 'name', 'str')
        slide_index = self.get_test_value('put_slide_shape_info', 'slide_index', 'int')
        shape_index = self.get_test_value('put_slide_shape_info', 'shape_index', 'int')
        path = self.get_test_value('put_slide_shape_info', 'path', 'str')
        dto = self.get_test_value('put_slide_shape_info', 'dto', 'ShapeBase')
        password = self.get_test_value('put_slide_shape_info', 'password', 'str')
        folder = self.get_test_value('put_slide_shape_info', 'folder', 'str')
        storage = self.get_test_value('put_slide_shape_info', 'storage', 'str')
        return asposeslidescloud.models.requests.shapes_api_requests.PutSlideShapeInfoRequest(name, slide_index, shape_index, path, dto, password, folder, storage)


if __name__ == '__main__':
    unittest.main()
