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

from asposeslidescloud.models.math_element import MathElement

class SuperscriptElement(MathElement):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'base': 'MathElement',
        'superscript': 'MathElement'
    }

    attribute_map = {
        'type': 'type',
        'base': 'base',
        'superscript': 'superscript'
    }

    type_determiners = {
        'type': 'SuperscriptElement',
    }

    def __init__(self, type='SuperscriptElement', base=None, superscript=None):  # noqa: E501
        """SuperscriptElement - a model defined in Swagger"""  # noqa: E501
        super(SuperscriptElement, self).__init__(type)

        self._base = None
        self._superscript = None
        self.type = 'SuperscriptElement'

        if base is not None:
            self.base = base
        if superscript is not None:
            self.superscript = superscript

    @property
    def base(self):
        """Gets the base of this SuperscriptElement.  # noqa: E501

        Base argument  # noqa: E501

        :return: The base of this SuperscriptElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this SuperscriptElement.

        Base argument  # noqa: E501

        :param base: The base of this SuperscriptElement.  # noqa: E501
        :type: MathElement
        """
        self._base = base

    @property
    def superscript(self):
        """Gets the superscript of this SuperscriptElement.  # noqa: E501

        Superscript  # noqa: E501

        :return: The superscript of this SuperscriptElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._superscript

    @superscript.setter
    def superscript(self, superscript):
        """Sets the superscript of this SuperscriptElement.

        Superscript  # noqa: E501

        :param superscript: The superscript of this SuperscriptElement.  # noqa: E501
        :type: MathElement
        """
        self._superscript = superscript

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
        if not isinstance(other, SuperscriptElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
