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


class FontData(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'font_name': 'str',
        'is_embedded': 'bool'
    }

    attribute_map = {
        'font_name': 'fontName',
        'is_embedded': 'isEmbedded'
    }

    type_determiners = {
    }

    def __init__(self, font_name=None, is_embedded=None):  # noqa: E501
        """FontData - a model defined in Swagger"""  # noqa: E501

        self._font_name = None
        self._is_embedded = None

        if font_name is not None:
            self.font_name = font_name
        if is_embedded is not None:
            self.is_embedded = is_embedded

    @property
    def font_name(self):
        """Gets the font_name of this FontData.  # noqa: E501

        Font name  # noqa: E501

        :return: The font_name of this FontData.  # noqa: E501
        :rtype: str
        """
        return self._font_name

    @font_name.setter
    def font_name(self, font_name):
        """Sets the font_name of this FontData.

        Font name  # noqa: E501

        :param font_name: The font_name of this FontData.  # noqa: E501
        :type: str
        """
        self._font_name = font_name

    @property
    def is_embedded(self):
        """Gets the is_embedded of this FontData.  # noqa: E501

        Returns true if font is embedded.  # noqa: E501

        :return: The is_embedded of this FontData.  # noqa: E501
        :rtype: bool
        """
        return self._is_embedded

    @is_embedded.setter
    def is_embedded(self, is_embedded):
        """Sets the is_embedded of this FontData.

        Returns true if font is embedded.  # noqa: E501

        :param is_embedded: The is_embedded of this FontData.  # noqa: E501
        :type: bool
        """
        self._is_embedded = is_embedded

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
        if not isinstance(other, FontData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
