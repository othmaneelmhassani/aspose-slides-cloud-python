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


class ExportOptions(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_regular_font': 'str',
        'height': 'int',
        'width': 'int',
        'font_fallback_rules': 'list[FontFallbackRule]',
        'format': 'str'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'height': 'height',
        'width': 'width',
        'font_fallback_rules': 'fontFallbackRules',
        'format': 'format'
    }

    type_determiners = {
    }

    def __init__(self, default_regular_font=None, height=None, width=None, font_fallback_rules=None, format=None):  # noqa: E501
        """ExportOptions - a model defined in Swagger"""  # noqa: E501

        self._default_regular_font = None
        self._height = None
        self._width = None
        self._font_fallback_rules = None
        self._format = None

        if default_regular_font is not None:
            self.default_regular_font = default_regular_font
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if font_fallback_rules is not None:
            self.font_fallback_rules = font_fallback_rules
        if format is not None:
            self.format = format

    @property
    def default_regular_font(self):
        """Gets the default_regular_font of this ExportOptions.  # noqa: E501

        Default regular font for rendering the presentation.   # noqa: E501

        :return: The default_regular_font of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._default_regular_font

    @default_regular_font.setter
    def default_regular_font(self, default_regular_font):
        """Sets the default_regular_font of this ExportOptions.

        Default regular font for rendering the presentation.   # noqa: E501

        :param default_regular_font: The default_regular_font of this ExportOptions.  # noqa: E501
        :type: str
        """
        self._default_regular_font = default_regular_font

    @property
    def height(self):
        """Gets the height of this ExportOptions.  # noqa: E501

        Gets or sets the height of slides in the output format, e.g. image size, pdf page size etc.  # noqa: E501

        :return: The height of this ExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ExportOptions.

        Gets or sets the height of slides in the output format, e.g. image size, pdf page size etc.  # noqa: E501

        :param height: The height of this ExportOptions.  # noqa: E501
        :type: int
        """
        self._height = height

    @property
    def width(self):
        """Gets the width of this ExportOptions.  # noqa: E501

        Gets or sets the height of slides in the output format, e.g. image size, pdf page size etc.  # noqa: E501

        :return: The width of this ExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ExportOptions.

        Gets or sets the height of slides in the output format, e.g. image size, pdf page size etc.  # noqa: E501

        :param width: The width of this ExportOptions.  # noqa: E501
        :type: int
        """
        self._width = width

    @property
    def font_fallback_rules(self):
        """Gets the font_fallback_rules of this ExportOptions.  # noqa: E501

        Gets of sets list of font fallback rules.  # noqa: E501

        :return: The font_fallback_rules of this ExportOptions.  # noqa: E501
        :rtype: list[FontFallbackRule]
        """
        return self._font_fallback_rules

    @font_fallback_rules.setter
    def font_fallback_rules(self, font_fallback_rules):
        """Sets the font_fallback_rules of this ExportOptions.

        Gets of sets list of font fallback rules.  # noqa: E501

        :param font_fallback_rules: The font_fallback_rules of this ExportOptions.  # noqa: E501
        :type: list[FontFallbackRule]
        """
        self._font_fallback_rules = font_fallback_rules

    @property
    def format(self):
        """Gets the format of this ExportOptions.  # noqa: E501


        :return: The format of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ExportOptions.


        :param format: The format of this ExportOptions.  # noqa: E501
        :type: str
        """
        self._format = format

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
        if not isinstance(other, ExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
