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

class LimitElement(MathElement):


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
        'limit': 'MathElement',
        'upper_limit': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'base': 'base',
        'limit': 'limit',
        'upper_limit': 'upperLimit'
    }

    type_determiners = {
        'type': 'Limit',
    }

    def __init__(self, type='Limit', base=None, limit=None, upper_limit=None):  # noqa: E501
        """LimitElement - a model defined in Swagger"""  # noqa: E501
        super(LimitElement, self).__init__(type)

        self._base = None
        self._limit = None
        self._upper_limit = None
        self.type = 'Limit'

        if base is not None:
            self.base = base
        if limit is not None:
            self.limit = limit
        if upper_limit is not None:
            self.upper_limit = upper_limit

    @property
    def base(self):
        """Gets the base of this LimitElement.  # noqa: E501

        Base  # noqa: E501

        :return: The base of this LimitElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this LimitElement.

        Base  # noqa: E501

        :param base: The base of this LimitElement.  # noqa: E501
        :type: MathElement
        """
        self._base = base

    @property
    def limit(self):
        """Gets the limit of this LimitElement.  # noqa: E501

        Limit  # noqa: E501

        :return: The limit of this LimitElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this LimitElement.

        Limit  # noqa: E501

        :param limit: The limit of this LimitElement.  # noqa: E501
        :type: MathElement
        """
        self._limit = limit

    @property
    def upper_limit(self):
        """Gets the upper_limit of this LimitElement.  # noqa: E501

        Specifies upper or lower limit  # noqa: E501

        :return: The upper_limit of this LimitElement.  # noqa: E501
        :rtype: bool
        """
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, upper_limit):
        """Sets the upper_limit of this LimitElement.

        Specifies upper or lower limit  # noqa: E501

        :param upper_limit: The upper_limit of this LimitElement.  # noqa: E501
        :type: bool
        """
        self._upper_limit = upper_limit

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
        if not isinstance(other, LimitElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
