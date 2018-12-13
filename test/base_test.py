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

import asposestoragecloud
import json
import os
import unittest

from asposeslidescloud.configuration import Configuration
from asposeslidescloud.models.combined_shape_type import CombinedShapeType
from asposeslidescloud.models.document_properties import DocumentProperties
from asposeslidescloud.models.document_property import DocumentProperty
from asposeslidescloud.models.geometry_shape_type import GeometryShapeType
from asposeslidescloud.models.layout_slide import LayoutSlide
from asposeslidescloud.models.notes_slide import NotesSlide
from asposeslidescloud.models.pipeline import Pipeline
from asposeslidescloud.models.presentations_merge_request import PresentationsMergeRequest
from asposeslidescloud.models.resource_uri import ResourceUri
from asposeslidescloud.models.resource_uri_element import ResourceUriElement
from asposeslidescloud.models.shape import Shape
from asposeslidescloud.models.shape_type import ShapeType
from asposeslidescloud.models.slide import Slide

class BaseTest(unittest.TestCase):

    __test__ = False
    
    configuration = None
    storage_api = None
    
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)

        self.test_data_path = "TestData"
        self.folder_name = "TempSlidesSDK"
        self.changed_file_name = "changedtest.ppt"
        self.file_name = "test.ppt"
        self.file_password = "password"

        if not BaseTest.storage_api:
            with open('testconfig.json') as f:
                config = json.loads(f.read())
            BaseTest.configuration = Configuration()
            BaseTest.configuration.app_sid = config['AppSid']
            BaseTest.configuration.app_key = config['AppKey']
            BaseTest.configuration.base_url = config['BaseUrl']
            BaseTest.configuration.debug = config['Debug']

            api_client = asposestoragecloud.ApiClient(BaseTest.configuration.app_key, BaseTest.configuration.app_sid)
            BaseTest.storage_api = asposestoragecloud.StorageApi(api_client)
            BaseTest.storage_api.api_client.configuration.base_url = BaseTest.configuration.base_url + '/' + BaseTest.configuration.version

    def initialize(self, function_name, invalid_parameter_name, invalid_parameter_value):
        if function_name == "delete_slides_clean_slides_list" or function_name == "put_slides_slide":
            with open(os.path.join(self.test_data_path, "test-unprotected.ppt"), 'rb') as f:
                file = f.read()
            BaseTest.storage_api.put_create(os.path.join(self.folder_name, "test-unprotected.ppt"), file)

        with open(os.path.join(self.test_data_path, self.file_name), 'rb') as f:
            file = f.read()
        BaseTest.storage_api.put_create(os.path.join(self.folder_name, self.file_name), file)

        if function_name == "post_slides_document":
            BaseTest.storage_api.delete_file(os.path.join(self.folder_name, self.file_name))
        if invalid_parameter_name == "folder":
            BaseTest.storage_api.delete_file(os.path.join(invalid_parameter_value, self.file_name))
        if function_name == "put_new_presentation":
            BaseTest.storage_api.delete_file(os.path.join(self.folder_name + "invalid", self.changed_file_name))
            BaseTest.storage_api.delete_file(os.path.join(self.folder_name, self.changed_file_name))

    def get_test_value(self, function_name, field_name, field_type):
        if field_type == 'int':
            if field_name == "shape_to_clone":
                return None
            if field_name == "shape_index":
                return 3
            return 1
        if field_type == 'list[int]':
            return None
        if field_name.endswith('storage') \
            or field_name == 'out_path' \
            or field_name == 'jpeg_quality' \
            or field_name == 'files' \
            or field_name == 'options' \
            or field_name == 'is_image_data_embeded':
            return None
        if field_name == 'path':
            return ""
        if field_name == 'folder':
            return self.folder_name
        if field_name == 'name':
            if function_name == 'put_new_presentation':
                return self.changed_file_name
            if function_name == 'delete_slides_clean_slides_list' or function_name == "put_slides_slide":
                return "test-unprotected.ppt"
            return self.file_name
        if field_name == 'property_name':
            return "testProperty"
        if field_name == "template_path" or field_name == "clone_from":
            return self.folder_name + "/" + self.file_name
        if field_name.endswith('password'):
            if function_name == 'delete_slides_clean_slides_list' or function_name == "put_slides_slide":
                return None
            return self.file_password
        if field_name == 'format':
            if function_name == "get_notes_slide_shape_with_format" \
                or function_name == "get_notes_slide_with_format" \
                or function_name == "get_slides_image_with_format" \
                or function_name == "get_shape_with_format" \
                or function_name == "post_shape_save_as" \
                or function_name == "post_notes_slide_shape_save_as":
                return "png"
            return 'pdf'
        if field_name == "color":
            return "#FF0000dd"
        if field_name == 'data':
            return "<staff><person><name>John Doe</name><address><line1>10 Downing Street</line1><line2>London</line2></address><phone>+457 123456</phone><bio>Hi, I'm John and this is my CV</bio><skills><skill><title>C#</title><level>Excellent</level></skill><skill><title>C++</title><level>Good</level></skill><skill><title>Java</title><level>Average</level></skill></skills></person></staff>";
        if field_name == 'stream' or field_name == 'document':
            with open(self.test_data_path + "/" + self.file_name, "rb") as bf:
                return bf.read()
        if field_name == 'pipeline':
            return Pipeline()
        if field_name == "request":
            return PresentationsMergeRequest()
        if field_name == "dto":
            if function_name.endswith("add_new_shape"):
                shape = Shape()
                shape.text = "testShape"
                shape.type = ShapeType.SHAPE
                shape.shape_type = CombinedShapeType.BENTARROW
                shape.geometry_shape_type = GeometryShapeType.RECTANGLE
                return shape
            notes_slide = NotesSlide()
            notes_slide.text = "testNote"
            return notes_slide
        if field_name == "slide_dto":
            if function_name == "put_slides_slide":
                slide = Slide()
                layout_slide_uri = ResourceUriElement()
                uri = ResourceUri()
                uri.href = "TitleOnly"
                layout_slide_uri.uri = uri
                slide.layout_slide = layout_slide_uri
                print(slide)
                return slide
            layout_slide = LayoutSlide()
            master_slide_uri = ResourceUriElement()
            uri = ResourceUri()
            uri.href = "masterSlides/2"
            master_slide_uri.uri = uri
            layout_slide.master_slide = master_slide_uri
            return layout_slide
        if field_name == "properties":
            properties = DocumentProperties()
            properties.list = []
            return properties
        if field_name == "_property":
            _property = DocumentProperty()
            _property.name = "testProperty001"
            _property.value = "testValue002"
            return _property

        return 'test' + field_name

    def get_invalid_test_value(self, field_name, field_value, field_type):
        if field_type == 'list[int]':
            return [1, 593]
        if field_type == 'int':
            return 593
        if not field_name == 'files' and field_value is None:
            return 'invalid'
        if isinstance(field_value, str):
            return field_value + 'invalid'
        return None

    def assert_exception(self, ex, function_name, field_name, field_value):
        if function_name != "post_slides_document":
            if field_name == 'path' and function_name.endswith("add_new_shape"):
                self.assertEqual(405, ex.status)
            elif field_name == 'options':
                self.assertEqual(500, ex.status)
            elif (field_name == 'name' or field_name == 'property_name' or field_name == 'folder' or field_name == 'clone_from') \
                and not (function_name == 'put_new_presentation' \
                    or function_name == 'put_slides_document_from_html' \
                    or function_name == 'post_add_notes_slide'):
                self.assertEqual(404, ex.status)
                if field_name == "property_name":
                    self.assertTrue(ex.body.startswith("Property " + field_value + " not found"))
                else:
                    self.assertTrue(ex.body.startswith("AmazonS3 exception: Error 'The specified key does not exist.'"))
            else:
                self.assertEqual(400, ex.status)
                if field_name == 'storage':
                    if not (function_name == 'put_new_presentation' \
                        or function_name == 'put_slides_document_from_html' \
                        or function_name == 'post_add_notes_slide'):
                        self.assertTrue(ex.body.startswith("The specified storage was not found or is not associated with the application."))
                    else:
                        self.assertTrue(ex.body.startswith("Object reference not set to an instance of an object"))
                elif field_name == "clone_from_storage":
                    self.assertTrue(ex.body.startswith("The specified storage was not found or is not associated with the application."))
                elif field_name.endswith('password'):
                    if function_name == 'put_slides_document_from_html' \
                        or function_name == 'post_add_notes_slide' \
                        or (function_name == 'put_new_presentation' and field_name == 'template_password'):
                        self.assertTrue(ex.body.startswith("Object reference not set to an instance of an object"))
                    elif function_name == 'delete_slides_clean_slides_list' or function_name == "put_slides_slide":
                        self.assertTrue(ex.body.startswith("An attempt was made to move the position before the beginning of the stream."))
                    else:
                        self.assertTrue(ex.body.startswith("Invalid password."))
                elif field_name == 'to':
                    self.assertTrue(ex.body.startswith("Invalid 'to' parameter"))
                elif (field_name == 'slide_index' \
                        and (function_name.startswith('get_notes_slide') and not function_name.startswith('get_notes_slide_shape')) \
                        or function_name == "get_slides_slide_comments") \
                    or field_name == 'clone_from_position' \
                    or field_name == 'shape_to_clone':
                    self.assertTrue(ex.body.startswith("Invalid index"))
                elif field_name == 'index':
                    self.assertTrue(ex.body.startswith("Specified argument was out of the range of valid values."))
                elif field_name == 'slide_index' or field_name == 'slides':
                    self.assertTrue(ex.body.startswith("Wrong slide index."))
                elif field_name == 'shape_index' or field_name == 'shapes':
                    self.assertTrue(ex.body.startswith("Wrong shape index."))
                elif field_name == 'paragraph_index' or field_name == 'paragraphs':
                    self.assertTrue(ex.body.startswith("Wrong paragraph index."))
                elif field_name == 'portion_index' or field_name == 'portions':
                    self.assertTrue(ex.body.startswith("Wrong portion index."))
                elif field_name == 'placeholder_index':
                    self.assertTrue(ex.body.startswith("Placeholder with specified index doesn't exist"))
                elif field_name == 'position':
                    self.assertTrue(ex.body.startswith("Index must be within the bounds of the List"))
                elif field_name == 'new_position':
                    self.assertTrue(ex.body.startswith("Specified argument was out of the range of valid values"))
                elif field_name == 'old_position':
                    self.assertTrue(ex.body.startswith("Index was out of range"))
                elif field_name == 'color':
                    self.assertTrue(ex.body.startswith("Color must be in format"))
                elif field_name == 'path':
                    if function_name.endswith("shapes"):
                        self.assertTrue(ex.body.startswith("The request is invalid"))
                    else:
                        self.assertTrue(ex.body.startswith("The HTTP resource that matches the request URI"))
                elif field_name == 'format':
                    self.assertTrue(ex.body.startswith("Format " + field_value + " is not supported."))
                elif field_name == 'pipeline':
                    #TODO: correct spelling error
                    self.assertTrue(ex.body.startswith("Pipeline dto expected."))
                elif field_name == 'dto':
                    if function_name.endswith('add_new_paragraph') \
                        or function_name.endswith('set_paragraph_properties') \
                        or function_name.endswith('set_paragraph_portion_properties') \
                        or function_name.endswith('slide_shape_info') \
                        or function_name.endswith('add_new_paragraph') \
                        or function_name.startswith('put_update_notes_slide_shape'):
                        self.assertTrue(ex.body.startswith("Shape dto is not specified"))
                    elif function_name.endswith('add_new_portion') or function_name.endswith('add_new_shape'):
                        self.assertTrue(ex.body.startswith("Invalid shape's path."))
                    else:
                        self.assertTrue(ex.body.startswith("Value cannot be null"))
                elif field_name == 'slide_dto':
                    self.assertTrue(ex.body.startswith("DTO of the slide expected in request body"))
                elif field_name == 'document':
                    self.assertTrue(ex.body.startswith("The stream is empty."))
                else:
                    self.assertTrue(ex.body.startswith("Object reference not set to an instance of an object"))

    def assert_no_exception(self, function_name, field_name):
        if field_name != 'fonts_folder' \
            and field_name != 'dest_folder' \
            and field_name != 'stream' \
            and field_name != 'html' \
            and field_name != 'files' \
            and field_name != 'jpeg_quality' \
            and field_name != 'out_path' \
            and field_name != 'options' \
            and field_name != '_from' \
            and field_name != 'width' \
            and field_name != 'height' \
            and field_name != 'scale_type' \
            and field_name != 'size_type' \
            and field_name != "scale_x" \
            and field_name != "scale_y" \
            and field_name != "bounds" \
            and field_name != 'slide_to_copy' \
            and field_name != 'source' \
            and field_name != "background" \
            and field_name != "layout_alias" \
            and field_name != 'apply_to_all' \
            and field_name != 'with_empty' \
            and field_name != 'ignore_case' \
            and field_name != 'old_value' \
            and field_name != 'new_value' \
            and not (function_name == 'put_slides_set_document_property' and field_name == 'property_name') \
            and not (function_name == 'put_new_presentation' and (field_name == 'password' or field_name == 'folder')) \
            and not (function_name == 'put_slides_document_from_html' and field_name == 'folder') \
            and not (function_name == 'post_add_notes_slide' and field_name == 'dto') \
            and not (function_name == 'post_slides_reorder_position' and (field_name == 'position' or field_name == 'slide_to_clone')):
            self.fail("Must have failed")

    def assert_successful_exception(self, ex, function_name):
        if function_name != "post_slides_document":
            raise ex
