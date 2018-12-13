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
from asposeslidescloud.apis.document_api import DocumentApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestDocumentApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.document_api.DocumentApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_slides_api_info(self):
        """Test case for get_slides_api_info
        """
        
        self.initialize('get_slides_api_info', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_api_info()
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_api_info')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)


    def test_get_slides_document(self):
        """Test case for get_slides_document
        """
        request = self.__prepare_get_slides_document_request()
        self.initialize('get_slides_document', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_document')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_get_slides_document_invalid_name(self):
        """Test case for get_slides_document with invalid name
        """
        request = self.__prepare_get_slides_document_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_document', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_document', 'name')

    def test_get_slides_document_invalid_password(self):
        """Test case for get_slides_document with invalid password
        """
        request = self.__prepare_get_slides_document_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_document', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_document', 'password')

    def test_get_slides_document_invalid_storage(self):
        """Test case for get_slides_document with invalid storage
        """
        request = self.__prepare_get_slides_document_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_document', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_document', 'storage')

    def test_get_slides_document_invalid_folder(self):
        """Test case for get_slides_document with invalid folder
        """
        request = self.__prepare_get_slides_document_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_document', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_document', 'folder')

    def __prepare_get_slides_document_request(self):
        name = self.get_test_value('get_slides_document', 'name', 'str')
        password = self.get_test_value('get_slides_document', 'password', 'str')
        storage = self.get_test_value('get_slides_document', 'storage', 'str')
        folder = self.get_test_value('get_slides_document', 'folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.GetSlidesDocumentRequest(name, password, storage, folder)

    def test_get_slides_document_with_format(self):
        """Test case for get_slides_document_with_format
        """
        request = self.__prepare_get_slides_document_with_format_request()
        self.initialize('get_slides_document_with_format', None, None)
        response = None
        ok = False
        try:
            response = self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'get_slides_document_with_format')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_get_slides_document_with_format_invalid_name(self):
        """Test case for get_slides_document_with_format with invalid name
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('get_slides_document_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'name', request.name)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'name')

    def test_get_slides_document_with_format_invalid_format(self):
        """Test case for get_slides_document_with_format with invalid format
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('get_slides_document_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'format', request.format)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'format')

    def test_get_slides_document_with_format_invalid_jpeg_quality(self):
        """Test case for get_slides_document_with_format with invalid jpeg_quality
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.jpeg_quality = self.get_invalid_test_value('jpeg_quality', request.jpeg_quality, 'int')
        self.initialize('get_slides_document_with_format', 'jpeg_quality', request.jpeg_quality)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'jpeg_quality', request.jpeg_quality)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'jpeg_quality')

    def test_get_slides_document_with_format_invalid_password(self):
        """Test case for get_slides_document_with_format with invalid password
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('get_slides_document_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'password', request.password)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'password')

    def test_get_slides_document_with_format_invalid_storage(self):
        """Test case for get_slides_document_with_format with invalid storage
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('get_slides_document_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'storage', request.storage)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'storage')

    def test_get_slides_document_with_format_invalid_folder(self):
        """Test case for get_slides_document_with_format with invalid folder
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('get_slides_document_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'folder', request.folder)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'folder')

    def test_get_slides_document_with_format_invalid_out_path(self):
        """Test case for get_slides_document_with_format with invalid out_path
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('get_slides_document_with_format', 'out_path', request.out_path)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'out_path')

    def test_get_slides_document_with_format_invalid_fonts_folder(self):
        """Test case for get_slides_document_with_format with invalid fonts_folder
        """
        request = self.__prepare_get_slides_document_with_format_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('get_slides_document_with_format', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.get_slides_document_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_with_format', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('get_slides_document_with_format', 'fonts_folder')

    def __prepare_get_slides_document_with_format_request(self):
        name = self.get_test_value('get_slides_document_with_format', 'name', 'str')
        format = self.get_test_value('get_slides_document_with_format', 'format', 'str')
        jpeg_quality = self.get_test_value('get_slides_document_with_format', 'jpeg_quality', 'int')
        password = self.get_test_value('get_slides_document_with_format', 'password', 'str')
        storage = self.get_test_value('get_slides_document_with_format', 'storage', 'str')
        folder = self.get_test_value('get_slides_document_with_format', 'folder', 'str')
        out_path = self.get_test_value('get_slides_document_with_format', 'out_path', 'str')
        fonts_folder = self.get_test_value('get_slides_document_with_format', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.GetSlidesDocumentWithFormatRequest(name, format, jpeg_quality, password, storage, folder, out_path, fonts_folder)

    def test_post_slides_document(self):
        """Test case for post_slides_document
        """
        request = self.__prepare_post_slides_document_request()
        self.initialize('post_slides_document', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_document')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_document_invalid_name(self):
        """Test case for post_slides_document with invalid name
        """
        request = self.__prepare_post_slides_document_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_document', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_document', 'name')

    def test_post_slides_document_invalid_data(self):
        """Test case for post_slides_document with invalid data
        """
        request = self.__prepare_post_slides_document_request()
        request.data = self.get_invalid_test_value('data', request.data, 'str')
        self.initialize('post_slides_document', 'data', request.data)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'data', request.data)
        if ok:
            self.assert_no_exception('post_slides_document', 'data')

    def test_post_slides_document_invalid_template_path(self):
        """Test case for post_slides_document with invalid template_path
        """
        request = self.__prepare_post_slides_document_request()
        request.template_path = self.get_invalid_test_value('template_path', request.template_path, 'str')
        self.initialize('post_slides_document', 'template_path', request.template_path)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'template_path', request.template_path)
        if ok:
            self.assert_no_exception('post_slides_document', 'template_path')

    def test_post_slides_document_invalid_template_storage(self):
        """Test case for post_slides_document with invalid template_storage
        """
        request = self.__prepare_post_slides_document_request()
        request.template_storage = self.get_invalid_test_value('template_storage', request.template_storage, 'str')
        self.initialize('post_slides_document', 'template_storage', request.template_storage)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'template_storage', request.template_storage)
        if ok:
            self.assert_no_exception('post_slides_document', 'template_storage')

    def test_post_slides_document_invalid_is_image_data_embedded(self):
        """Test case for post_slides_document with invalid is_image_data_embedded
        """
        request = self.__prepare_post_slides_document_request()
        request.is_image_data_embedded = self.get_invalid_test_value('is_image_data_embedded', request.is_image_data_embedded, 'bool')
        self.initialize('post_slides_document', 'is_image_data_embedded', request.is_image_data_embedded)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'is_image_data_embedded', request.is_image_data_embedded)
        if ok:
            self.assert_no_exception('post_slides_document', 'is_image_data_embedded')

    def test_post_slides_document_invalid_password(self):
        """Test case for post_slides_document with invalid password
        """
        request = self.__prepare_post_slides_document_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_document', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_document', 'password')

    def test_post_slides_document_invalid_storage(self):
        """Test case for post_slides_document with invalid storage
        """
        request = self.__prepare_post_slides_document_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_document', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_document', 'storage')

    def test_post_slides_document_invalid_folder(self):
        """Test case for post_slides_document with invalid folder
        """
        request = self.__prepare_post_slides_document_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_document', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_document', 'folder')

    def __prepare_post_slides_document_request(self):
        name = self.get_test_value('post_slides_document', 'name', 'str')
        data = self.get_test_value('post_slides_document', 'data', 'str')
        template_path = self.get_test_value('post_slides_document', 'template_path', 'str')
        template_storage = self.get_test_value('post_slides_document', 'template_storage', 'str')
        is_image_data_embedded = self.get_test_value('post_slides_document', 'is_image_data_embedded', 'bool')
        password = self.get_test_value('post_slides_document', 'password', 'str')
        storage = self.get_test_value('post_slides_document', 'storage', 'str')
        folder = self.get_test_value('post_slides_document', 'folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PostSlidesDocumentRequest(name, data, template_path, template_storage, is_image_data_embedded, password, storage, folder)

    def test_post_slides_pipeline(self):
        """Test case for post_slides_pipeline
        """
        request = self.__prepare_post_slides_pipeline_request()
        self.initialize('post_slides_pipeline', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_pipeline(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_pipeline')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_post_slides_pipeline_invalid_pipeline(self):
        """Test case for post_slides_pipeline with invalid pipeline
        """
        request = self.__prepare_post_slides_pipeline_request()
        request.pipeline = self.get_invalid_test_value('pipeline', request.pipeline, 'Pipeline')
        self.initialize('post_slides_pipeline', 'pipeline', request.pipeline)
        ok = False
        try:
            self.api.post_slides_pipeline(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_pipeline', 'pipeline', request.pipeline)
        if ok:
            self.assert_no_exception('post_slides_pipeline', 'pipeline')

    def test_post_slides_pipeline_invalid_files(self):
        """Test case for post_slides_pipeline with invalid files
        """
        request = self.__prepare_post_slides_pipeline_request()
        request.files = self.get_invalid_test_value('files', request.files, 'dict')
        self.initialize('post_slides_pipeline', 'files', request.files)
        ok = False
        try:
            self.api.post_slides_pipeline(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_pipeline', 'files', request.files)
        if ok:
            self.assert_no_exception('post_slides_pipeline', 'files')

    def __prepare_post_slides_pipeline_request(self):
        pipeline = self.get_test_value('post_slides_pipeline', 'pipeline', 'Pipeline')
        files = self.get_test_value('post_slides_pipeline', 'files', 'dict')
        return asposeslidescloud.models.requests.document_api_requests.PostSlidesPipelineRequest(pipeline, files)

    def test_post_slides_save_as(self):
        """Test case for post_slides_save_as
        """
        request = self.__prepare_post_slides_save_as_request()
        self.initialize('post_slides_save_as', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_save_as')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_post_slides_save_as_invalid_name(self):
        """Test case for post_slides_save_as with invalid name
        """
        request = self.__prepare_post_slides_save_as_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'name')

    def test_post_slides_save_as_invalid_format(self):
        """Test case for post_slides_save_as with invalid format
        """
        request = self.__prepare_post_slides_save_as_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('post_slides_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'format', request.format)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'format')

    def test_post_slides_save_as_invalid_options(self):
        """Test case for post_slides_save_as with invalid options
        """
        request = self.__prepare_post_slides_save_as_request()
        request.options = self.get_invalid_test_value('options', request.options, 'ExportOptions')
        self.initialize('post_slides_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'options', request.options)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'options')

    def test_post_slides_save_as_invalid_password(self):
        """Test case for post_slides_save_as with invalid password
        """
        request = self.__prepare_post_slides_save_as_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'password')

    def test_post_slides_save_as_invalid_storage(self):
        """Test case for post_slides_save_as with invalid storage
        """
        request = self.__prepare_post_slides_save_as_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'storage')

    def test_post_slides_save_as_invalid_folder(self):
        """Test case for post_slides_save_as with invalid folder
        """
        request = self.__prepare_post_slides_save_as_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'folder')

    def test_post_slides_save_as_invalid_out_path(self):
        """Test case for post_slides_save_as with invalid out_path
        """
        request = self.__prepare_post_slides_save_as_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('post_slides_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'out_path')

    def test_post_slides_save_as_invalid_fonts_folder(self):
        """Test case for post_slides_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_slides_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_slides_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('post_slides_save_as', 'fonts_folder')

    def __prepare_post_slides_save_as_request(self):
        name = self.get_test_value('post_slides_save_as', 'name', 'str')
        format = self.get_test_value('post_slides_save_as', 'format', 'str')
        options = self.get_test_value('post_slides_save_as', 'options', 'ExportOptions')
        password = self.get_test_value('post_slides_save_as', 'password', 'str')
        storage = self.get_test_value('post_slides_save_as', 'storage', 'str')
        folder = self.get_test_value('post_slides_save_as', 'folder', 'str')
        out_path = self.get_test_value('post_slides_save_as', 'out_path', 'str')
        fonts_folder = self.get_test_value('post_slides_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PostSlidesSaveAsRequest(name, format, options, password, storage, folder, out_path, fonts_folder)

    def test_post_slides_split(self):
        """Test case for post_slides_split
        """
        request = self.__prepare_post_slides_split_request()
        self.initialize('post_slides_split', None, None)
        response = None
        ok = False
        try:
            response = self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'post_slides_split')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_post_slides_split_invalid_name(self):
        """Test case for post_slides_split with invalid name
        """
        request = self.__prepare_post_slides_split_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('post_slides_split', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'name', request.name)
        if ok:
            self.assert_no_exception('post_slides_split', 'name')

    def test_post_slides_split_invalid_options(self):
        """Test case for post_slides_split with invalid options
        """
        request = self.__prepare_post_slides_split_request()
        request.options = self.get_invalid_test_value('options', request.options, 'ExportOptions')
        self.initialize('post_slides_split', 'options', request.options)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'options', request.options)
        if ok:
            self.assert_no_exception('post_slides_split', 'options')

    def test_post_slides_split_invalid_format(self):
        """Test case for post_slides_split with invalid format
        """
        request = self.__prepare_post_slides_split_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('post_slides_split', 'format', request.format)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'format', request.format)
        if ok:
            self.assert_no_exception('post_slides_split', 'format')

    def test_post_slides_split_invalid_width(self):
        """Test case for post_slides_split with invalid width
        """
        request = self.__prepare_post_slides_split_request()
        request.width = self.get_invalid_test_value('width', request.width, 'int')
        self.initialize('post_slides_split', 'width', request.width)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'width', request.width)
        if ok:
            self.assert_no_exception('post_slides_split', 'width')

    def test_post_slides_split_invalid_height(self):
        """Test case for post_slides_split with invalid height
        """
        request = self.__prepare_post_slides_split_request()
        request.height = self.get_invalid_test_value('height', request.height, 'int')
        self.initialize('post_slides_split', 'height', request.height)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'height', request.height)
        if ok:
            self.assert_no_exception('post_slides_split', 'height')

    def test_post_slides_split_invalid_to(self):
        """Test case for post_slides_split with invalid to
        """
        request = self.__prepare_post_slides_split_request()
        request.to = self.get_invalid_test_value('to', request.to, 'int')
        self.initialize('post_slides_split', 'to', request.to)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'to', request.to)
        if ok:
            self.assert_no_exception('post_slides_split', 'to')

    def test_post_slides_split_invalid__from(self):
        """Test case for post_slides_split with invalid _from
        """
        request = self.__prepare_post_slides_split_request()
        request._from = self.get_invalid_test_value('_from', request._from, 'int')
        self.initialize('post_slides_split', '_from', request._from)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', '_from', request._from)
        if ok:
            self.assert_no_exception('post_slides_split', '_from')

    def test_post_slides_split_invalid_dest_folder(self):
        """Test case for post_slides_split with invalid dest_folder
        """
        request = self.__prepare_post_slides_split_request()
        request.dest_folder = self.get_invalid_test_value('dest_folder', request.dest_folder, 'str')
        self.initialize('post_slides_split', 'dest_folder', request.dest_folder)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'dest_folder', request.dest_folder)
        if ok:
            self.assert_no_exception('post_slides_split', 'dest_folder')

    def test_post_slides_split_invalid_password(self):
        """Test case for post_slides_split with invalid password
        """
        request = self.__prepare_post_slides_split_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('post_slides_split', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'password', request.password)
        if ok:
            self.assert_no_exception('post_slides_split', 'password')

    def test_post_slides_split_invalid_storage(self):
        """Test case for post_slides_split with invalid storage
        """
        request = self.__prepare_post_slides_split_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('post_slides_split', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'storage', request.storage)
        if ok:
            self.assert_no_exception('post_slides_split', 'storage')

    def test_post_slides_split_invalid_folder(self):
        """Test case for post_slides_split with invalid folder
        """
        request = self.__prepare_post_slides_split_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('post_slides_split', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'folder', request.folder)
        if ok:
            self.assert_no_exception('post_slides_split', 'folder')

    def __prepare_post_slides_split_request(self):
        name = self.get_test_value('post_slides_split', 'name', 'str')
        options = self.get_test_value('post_slides_split', 'options', 'ExportOptions')
        format = self.get_test_value('post_slides_split', 'format', 'str')
        width = self.get_test_value('post_slides_split', 'width', 'int')
        height = self.get_test_value('post_slides_split', 'height', 'int')
        to = self.get_test_value('post_slides_split', 'to', 'int')
        _from = self.get_test_value('post_slides_split', '_from', 'int')
        dest_folder = self.get_test_value('post_slides_split', 'dest_folder', 'str')
        password = self.get_test_value('post_slides_split', 'password', 'str')
        storage = self.get_test_value('post_slides_split', 'storage', 'str')
        folder = self.get_test_value('post_slides_split', 'folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PostSlidesSplitRequest(name, options, format, width, height, to, _from, dest_folder, password, storage, folder)

    def test_put_new_presentation(self):
        """Test case for put_new_presentation
        """
        request = self.__prepare_put_new_presentation_request()
        self.initialize('put_new_presentation', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_new_presentation')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_new_presentation_invalid_name(self):
        """Test case for put_new_presentation with invalid name
        """
        request = self.__prepare_put_new_presentation_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_new_presentation', 'name', request.name)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'name', request.name)
        if ok:
            self.assert_no_exception('put_new_presentation', 'name')

    def test_put_new_presentation_invalid_stream(self):
        """Test case for put_new_presentation with invalid stream
        """
        request = self.__prepare_put_new_presentation_request()
        request.stream = self.get_invalid_test_value('stream', request.stream, 'Stream')
        self.initialize('put_new_presentation', 'stream', request.stream)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'stream', request.stream)
        if ok:
            self.assert_no_exception('put_new_presentation', 'stream')

    def test_put_new_presentation_invalid_template_path(self):
        """Test case for put_new_presentation with invalid template_path
        """
        request = self.__prepare_put_new_presentation_request()
        request.template_path = self.get_invalid_test_value('template_path', request.template_path, 'str')
        self.initialize('put_new_presentation', 'template_path', request.template_path)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'template_path', request.template_path)
        if ok:
            self.assert_no_exception('put_new_presentation', 'template_path')

    def test_put_new_presentation_invalid_template_password(self):
        """Test case for put_new_presentation with invalid template_password
        """
        request = self.__prepare_put_new_presentation_request()
        request.template_password = self.get_invalid_test_value('template_password', request.template_password, 'str')
        self.initialize('put_new_presentation', 'template_password', request.template_password)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'template_password', request.template_password)
        if ok:
            self.assert_no_exception('put_new_presentation', 'template_password')

    def test_put_new_presentation_invalid_template_storage(self):
        """Test case for put_new_presentation with invalid template_storage
        """
        request = self.__prepare_put_new_presentation_request()
        request.template_storage = self.get_invalid_test_value('template_storage', request.template_storage, 'str')
        self.initialize('put_new_presentation', 'template_storage', request.template_storage)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'template_storage', request.template_storage)
        if ok:
            self.assert_no_exception('put_new_presentation', 'template_storage')

    def test_put_new_presentation_invalid_password(self):
        """Test case for put_new_presentation with invalid password
        """
        request = self.__prepare_put_new_presentation_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_new_presentation', 'password', request.password)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'password', request.password)
        if ok:
            self.assert_no_exception('put_new_presentation', 'password')

    def test_put_new_presentation_invalid_storage(self):
        """Test case for put_new_presentation with invalid storage
        """
        request = self.__prepare_put_new_presentation_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_new_presentation', 'storage', request.storage)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_new_presentation', 'storage')

    def test_put_new_presentation_invalid_folder(self):
        """Test case for put_new_presentation with invalid folder
        """
        request = self.__prepare_put_new_presentation_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_new_presentation', 'folder', request.folder)
        ok = False
        try:
            self.api.put_new_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_new_presentation', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_new_presentation', 'folder')

    def __prepare_put_new_presentation_request(self):
        name = self.get_test_value('put_new_presentation', 'name', 'str')
        stream = self.get_test_value('put_new_presentation', 'stream', 'Stream')
        template_path = self.get_test_value('put_new_presentation', 'template_path', 'str')
        template_password = self.get_test_value('put_new_presentation', 'template_password', 'str')
        template_storage = self.get_test_value('put_new_presentation', 'template_storage', 'str')
        password = self.get_test_value('put_new_presentation', 'password', 'str')
        storage = self.get_test_value('put_new_presentation', 'storage', 'str')
        folder = self.get_test_value('put_new_presentation', 'folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PutNewPresentationRequest(name, stream, template_path, template_password, template_storage, password, storage, folder)

    def test_put_slides_convert(self):
        """Test case for put_slides_convert
        """
        request = self.__prepare_put_slides_convert_request()
        self.initialize('put_slides_convert', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slides_convert')
        if ok:
            self.assertTrue(isinstance(response, str))
            self.assertTrue(len(response) > 0)

    def test_put_slides_convert_invalid_format(self):
        """Test case for put_slides_convert with invalid format
        """
        request = self.__prepare_put_slides_convert_request()
        request.format = self.get_invalid_test_value('format', request.format, 'str')
        self.initialize('put_slides_convert', 'format', request.format)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'format', request.format)
        if ok:
            self.assert_no_exception('put_slides_convert', 'format')

    def test_put_slides_convert_invalid_document(self):
        """Test case for put_slides_convert with invalid document
        """
        request = self.__prepare_put_slides_convert_request()
        request.document = self.get_invalid_test_value('document', request.document, 'Stream')
        self.initialize('put_slides_convert', 'document', request.document)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'document', request.document)
        if ok:
            self.assert_no_exception('put_slides_convert', 'document')

    def test_put_slides_convert_invalid_password(self):
        """Test case for put_slides_convert with invalid password
        """
        request = self.__prepare_put_slides_convert_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slides_convert', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slides_convert', 'password')

    def test_put_slides_convert_invalid_out_path(self):
        """Test case for put_slides_convert with invalid out_path
        """
        request = self.__prepare_put_slides_convert_request()
        request.out_path = self.get_invalid_test_value('out_path', request.out_path, 'str')
        self.initialize('put_slides_convert', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'out_path', request.out_path)
        if ok:
            self.assert_no_exception('put_slides_convert', 'out_path')

    def test_put_slides_convert_invalid_fonts_folder(self):
        """Test case for put_slides_convert with invalid fonts_folder
        """
        request = self.__prepare_put_slides_convert_request()
        request.fonts_folder = self.get_invalid_test_value('fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_slides_convert', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'fonts_folder', request.fonts_folder)
        if ok:
            self.assert_no_exception('put_slides_convert', 'fonts_folder')

    def __prepare_put_slides_convert_request(self):
        format = self.get_test_value('put_slides_convert', 'format', 'str')
        document = self.get_test_value('put_slides_convert', 'document', 'Stream')
        password = self.get_test_value('put_slides_convert', 'password', 'str')
        out_path = self.get_test_value('put_slides_convert', 'out_path', 'str')
        fonts_folder = self.get_test_value('put_slides_convert', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PutSlidesConvertRequest(format, document, password, out_path, fonts_folder)

    def test_put_slides_document_from_html(self):
        """Test case for put_slides_document_from_html
        """
        request = self.__prepare_put_slides_document_from_html_request()
        self.initialize('put_slides_document_from_html', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slides_document_from_html')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_slides_document_from_html_invalid_name(self):
        """Test case for put_slides_document_from_html with invalid name
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_slides_document_from_html', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'name', request.name)
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'name')

    def test_put_slides_document_from_html_invalid_html(self):
        """Test case for put_slides_document_from_html with invalid html
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.html = self.get_invalid_test_value('html', request.html, 'str')
        self.initialize('put_slides_document_from_html', 'html', request.html)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'html', request.html)
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'html')

    def test_put_slides_document_from_html_invalid_password(self):
        """Test case for put_slides_document_from_html with invalid password
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slides_document_from_html', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'password')

    def test_put_slides_document_from_html_invalid_storage(self):
        """Test case for put_slides_document_from_html with invalid storage
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_slides_document_from_html', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'storage')

    def test_put_slides_document_from_html_invalid_folder(self):
        """Test case for put_slides_document_from_html with invalid folder
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_slides_document_from_html', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'folder')

    def __prepare_put_slides_document_from_html_request(self):
        name = self.get_test_value('put_slides_document_from_html', 'name', 'str')
        html = self.get_test_value('put_slides_document_from_html', 'html', 'str')
        password = self.get_test_value('put_slides_document_from_html', 'password', 'str')
        storage = self.get_test_value('put_slides_document_from_html', 'storage', 'str')
        folder = self.get_test_value('put_slides_document_from_html', 'folder', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PutSlidesDocumentFromHtmlRequest(name, html, password, storage, folder)

    def test_put_slides_slide_size(self):
        """Test case for put_slides_slide_size
        """
        request = self.__prepare_put_slides_slide_size_request()
        self.initialize('put_slides_slide_size', None, None)
        response = None
        ok = False
        try:
            response = self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_successful_exception(ex, 'put_slides_slide_size')
        if ok:
            self.assertTrue(response.code == 200 or response.code == 201)

    def test_put_slides_slide_size_invalid_name(self):
        """Test case for put_slides_slide_size with invalid name
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.name = self.get_invalid_test_value('name', request.name, 'str')
        self.initialize('put_slides_slide_size', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'name', request.name)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'name')

    def test_put_slides_slide_size_invalid_password(self):
        """Test case for put_slides_slide_size with invalid password
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.password = self.get_invalid_test_value('password', request.password, 'str')
        self.initialize('put_slides_slide_size', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'password', request.password)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'password')

    def test_put_slides_slide_size_invalid_storage(self):
        """Test case for put_slides_slide_size with invalid storage
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.storage = self.get_invalid_test_value('storage', request.storage, 'str')
        self.initialize('put_slides_slide_size', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'storage', request.storage)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'storage')

    def test_put_slides_slide_size_invalid_folder(self):
        """Test case for put_slides_slide_size with invalid folder
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.folder = self.get_invalid_test_value('folder', request.folder, 'str')
        self.initialize('put_slides_slide_size', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'folder', request.folder)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'folder')

    def test_put_slides_slide_size_invalid_width(self):
        """Test case for put_slides_slide_size with invalid width
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.width = self.get_invalid_test_value('width', request.width, 'int')
        self.initialize('put_slides_slide_size', 'width', request.width)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'width', request.width)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'width')

    def test_put_slides_slide_size_invalid_height(self):
        """Test case for put_slides_slide_size with invalid height
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.height = self.get_invalid_test_value('height', request.height, 'int')
        self.initialize('put_slides_slide_size', 'height', request.height)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'height', request.height)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'height')

    def test_put_slides_slide_size_invalid_size_type(self):
        """Test case for put_slides_slide_size with invalid size_type
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.size_type = self.get_invalid_test_value('size_type', request.size_type, 'str')
        self.initialize('put_slides_slide_size', 'size_type', request.size_type)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'size_type', request.size_type)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'size_type')

    def test_put_slides_slide_size_invalid_scale_type(self):
        """Test case for put_slides_slide_size with invalid scale_type
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.scale_type = self.get_invalid_test_value('scale_type', request.scale_type, 'str')
        self.initialize('put_slides_slide_size', 'scale_type', request.scale_type)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'scale_type', request.scale_type)
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'scale_type')

    def __prepare_put_slides_slide_size_request(self):
        name = self.get_test_value('put_slides_slide_size', 'name', 'str')
        password = self.get_test_value('put_slides_slide_size', 'password', 'str')
        storage = self.get_test_value('put_slides_slide_size', 'storage', 'str')
        folder = self.get_test_value('put_slides_slide_size', 'folder', 'str')
        width = self.get_test_value('put_slides_slide_size', 'width', 'int')
        height = self.get_test_value('put_slides_slide_size', 'height', 'int')
        size_type = self.get_test_value('put_slides_slide_size', 'size_type', 'str')
        scale_type = self.get_test_value('put_slides_slide_size', 'scale_type', 'str')
        return asposeslidescloud.models.requests.document_api_requests.PutSlidesSlideSizeRequest(name, password, storage, folder, width, height, size_type, scale_type)


if __name__ == '__main__':
    unittest.main()
