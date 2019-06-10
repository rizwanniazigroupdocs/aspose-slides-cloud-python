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

import pprint
import re  # noqa: F401

import six

from asposeslidescloud.models.resource_base import ResourceBase

class SlideAnimation(ResourceBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'self_uri': 'ResourceUri',
        'alternate_links': 'list[ResourceUri]',
        'main_sequence': 'list[Effect]',
        'interactive_sequences': 'list[InteractiveSequence]'
    }

    attribute_map = {
        'self_uri': 'SelfUri',
        'alternate_links': 'AlternateLinks',
        'main_sequence': 'MainSequence',
        'interactive_sequences': 'InteractiveSequences'
    }

    def __init__(self, self_uri=None, alternate_links=None, main_sequence=None, interactive_sequences=None):  # noqa: E501
        """SlideAnimation - a model defined in Swagger"""  # noqa: E501
        super(SlideAnimation, self).__init__(self_uri, alternate_links)

        self._main_sequence = None
        self._interactive_sequences = None

        if main_sequence is not None:
            self.main_sequence = main_sequence
        if interactive_sequences is not None:
            self.interactive_sequences = interactive_sequences

    @property
    def main_sequence(self):
        """Gets the main_sequence of this SlideAnimation.  # noqa: E501


        :return: The main_sequence of this SlideAnimation.  # noqa: E501
        :rtype: list[Effect]
        """
        return self._main_sequence

    @main_sequence.setter
    def main_sequence(self, main_sequence):
        """Sets the main_sequence of this SlideAnimation.


        :param main_sequence: The main_sequence of this SlideAnimation.  # noqa: E501
        :type: list[Effect]
        """
        self._main_sequence = main_sequence

    @property
    def interactive_sequences(self):
        """Gets the interactive_sequences of this SlideAnimation.  # noqa: E501


        :return: The interactive_sequences of this SlideAnimation.  # noqa: E501
        :rtype: list[InteractiveSequence]
        """
        return self._interactive_sequences

    @interactive_sequences.setter
    def interactive_sequences(self, interactive_sequences):
        """Sets the interactive_sequences of this SlideAnimation.


        :param interactive_sequences: The interactive_sequences of this SlideAnimation.  # noqa: E501
        :type: list[InteractiveSequence]
        """
        self._interactive_sequences = interactive_sequences

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SlideAnimation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
