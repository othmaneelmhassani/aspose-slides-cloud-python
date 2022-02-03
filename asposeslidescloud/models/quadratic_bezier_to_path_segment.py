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

from asposeslidescloud.models.path_segment import PathSegment

class QuadraticBezierToPathSegment(PathSegment):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'x1': 'float',
        'y1': 'float',
        'x2': 'float',
        'y2': 'float'
    }

    attribute_map = {
        'type': 'type',
        'x1': 'x1',
        'y1': 'y1',
        'x2': 'x2',
        'y2': 'y2'
    }

    type_determiners = {
        'type': 'QuadBezierTo',
    }

    def __init__(self, type='QuadBezierTo', x1=None, y1=None, x2=None, y2=None):  # noqa: E501
        """QuadraticBezierToPathSegment - a model defined in Swagger"""  # noqa: E501
        super(QuadraticBezierToPathSegment, self).__init__(type)

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.type = 'QuadBezierTo'

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def x1(self):
        """Gets the x1 of this QuadraticBezierToPathSegment.  # noqa: E501

        X coordinate of direction point  # noqa: E501

        :return: The x1 of this QuadraticBezierToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._x1

    @x1.setter
    def x1(self, x1):
        """Sets the x1 of this QuadraticBezierToPathSegment.

        X coordinate of direction point  # noqa: E501

        :param x1: The x1 of this QuadraticBezierToPathSegment.  # noqa: E501
        :type: float
        """
        self._x1 = x1

    @property
    def y1(self):
        """Gets the y1 of this QuadraticBezierToPathSegment.  # noqa: E501

        Y coordinate of direction point  # noqa: E501

        :return: The y1 of this QuadraticBezierToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._y1

    @y1.setter
    def y1(self, y1):
        """Sets the y1 of this QuadraticBezierToPathSegment.

        Y coordinate of direction point  # noqa: E501

        :param y1: The y1 of this QuadraticBezierToPathSegment.  # noqa: E501
        :type: float
        """
        self._y1 = y1

    @property
    def x2(self):
        """Gets the x2 of this QuadraticBezierToPathSegment.  # noqa: E501

        X coordinate of end point  # noqa: E501

        :return: The x2 of this QuadraticBezierToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._x2

    @x2.setter
    def x2(self, x2):
        """Sets the x2 of this QuadraticBezierToPathSegment.

        X coordinate of end point  # noqa: E501

        :param x2: The x2 of this QuadraticBezierToPathSegment.  # noqa: E501
        :type: float
        """
        self._x2 = x2

    @property
    def y2(self):
        """Gets the y2 of this QuadraticBezierToPathSegment.  # noqa: E501

        Y coordinate of end point  # noqa: E501

        :return: The y2 of this QuadraticBezierToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._y2

    @y2.setter
    def y2(self, y2):
        """Sets the y2 of this QuadraticBezierToPathSegment.

        Y coordinate of end point  # noqa: E501

        :param y2: The y2 of this QuadraticBezierToPathSegment.  # noqa: E501
        :type: float
        """
        self._y2 = y2

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
        if not isinstance(other, QuadraticBezierToPathSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
