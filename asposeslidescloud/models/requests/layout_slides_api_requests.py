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

class GetLayoutSlideRequest(object):

    def __init__(self, name, slide_index, password = None, folder = None, storage = None):
        self.name = name
        self.slide_index = slide_index
        self.password = password
        self.folder = folder
        self.storage = storage

class GetLayoutSlidesListRequest(object):

    def __init__(self, name, password = None, folder = None, storage = None):
        self.name = name
        self.password = password
        self.folder = folder
        self.storage = storage

class PostCopyLayoutSlideFromSourcePresentationRequest(object):

    def __init__(self, name, clone_from, clone_from_position, clone_from_password = None, clone_from_storage = None, password = None, folder = None, storage = None):
        self.name = name
        self.clone_from = clone_from
        self.clone_from_position = clone_from_position
        self.clone_from_password = clone_from_password
        self.clone_from_storage = clone_from_storage
        self.password = password
        self.folder = folder
        self.storage = storage

class PutLayoutSlideRequest(object):

    def __init__(self, name, slide_index, slide_dto = None, password = None, folder = None, storage = None):
        self.name = name
        self.slide_index = slide_index
        self.slide_dto = slide_dto
        self.password = password
        self.folder = folder
        self.storage = storage

