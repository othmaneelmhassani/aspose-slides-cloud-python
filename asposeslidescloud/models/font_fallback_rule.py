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


class FontFallbackRule(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'range_start_index': 'int',
        'range_end_index': 'int',
        'fallback_font_list': 'list[str]'
    }

    attribute_map = {
        'range_start_index': 'rangeStartIndex',
        'range_end_index': 'rangeEndIndex',
        'fallback_font_list': 'fallbackFontList'
    }

    type_determiners = {
    }

    def __init__(self, range_start_index=None, range_end_index=None, fallback_font_list=None):  # noqa: E501
        """FontFallbackRule - a model defined in Swagger"""  # noqa: E501

        self._range_start_index = None
        self._range_end_index = None
        self._fallback_font_list = None

        self.range_start_index = range_start_index
        self.range_end_index = range_end_index
        if fallback_font_list is not None:
            self.fallback_font_list = fallback_font_list

    @property
    def range_start_index(self):
        """Gets the range_start_index of this FontFallbackRule.  # noqa: E501

        First index of continuous unicode range.  # noqa: E501

        :return: The range_start_index of this FontFallbackRule.  # noqa: E501
        :rtype: int
        """
        return self._range_start_index

    @range_start_index.setter
    def range_start_index(self, range_start_index):
        """Sets the range_start_index of this FontFallbackRule.

        First index of continuous unicode range.  # noqa: E501

        :param range_start_index: The range_start_index of this FontFallbackRule.  # noqa: E501
        :type: int
        """
        self._range_start_index = range_start_index

    @property
    def range_end_index(self):
        """Gets the range_end_index of this FontFallbackRule.  # noqa: E501

        Last index of continuous unicode range.  # noqa: E501

        :return: The range_end_index of this FontFallbackRule.  # noqa: E501
        :rtype: int
        """
        return self._range_end_index

    @range_end_index.setter
    def range_end_index(self, range_end_index):
        """Sets the range_end_index of this FontFallbackRule.

        Last index of continuous unicode range.  # noqa: E501

        :param range_end_index: The range_end_index of this FontFallbackRule.  # noqa: E501
        :type: int
        """
        self._range_end_index = range_end_index

    @property
    def fallback_font_list(self):
        """Gets the fallback_font_list of this FontFallbackRule.  # noqa: E501

        List of fallback font links.  # noqa: E501

        :return: The fallback_font_list of this FontFallbackRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._fallback_font_list

    @fallback_font_list.setter
    def fallback_font_list(self, fallback_font_list):
        """Sets the fallback_font_list of this FontFallbackRule.

        List of fallback font links.  # noqa: E501

        :param fallback_font_list: The fallback_font_list of this FontFallbackRule.  # noqa: E501
        :type: list[str]
        """
        self._fallback_font_list = fallback_font_list

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
        if not isinstance(other, FontFallbackRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
