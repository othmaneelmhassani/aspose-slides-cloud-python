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

class ArcToPathSegment(PathSegment):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'width': 'float',
        'height': 'float',
        'start_angle': 'float',
        'sweep_angle': 'float'
    }

    attribute_map = {
        'type': 'type',
        'width': 'width',
        'height': 'height',
        'start_angle': 'startAngle',
        'sweep_angle': 'sweepAngle'
    }

    type_determiners = {
        'type': 'ArcTo',
    }

    def __init__(self, type='ArcTo', width=None, height=None, start_angle=None, sweep_angle=None):  # noqa: E501
        """ArcToPathSegment - a model defined in Swagger"""  # noqa: E501
        super(ArcToPathSegment, self).__init__(type)

        self._width = None
        self._height = None
        self._start_angle = None
        self._sweep_angle = None
        self.type = 'ArcTo'

        self.width = width
        self.height = height
        self.start_angle = start_angle
        self.sweep_angle = sweep_angle

    @property
    def width(self):
        """Gets the width of this ArcToPathSegment.  # noqa: E501

        Width of the rectangle  # noqa: E501

        :return: The width of this ArcToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ArcToPathSegment.

        Width of the rectangle  # noqa: E501

        :param width: The width of this ArcToPathSegment.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ArcToPathSegment.  # noqa: E501

        Height of the rectangle  # noqa: E501

        :return: The height of this ArcToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ArcToPathSegment.

        Height of the rectangle  # noqa: E501

        :param height: The height of this ArcToPathSegment.  # noqa: E501
        :type: float
        """
        self._height = height

    @property
    def start_angle(self):
        """Gets the start_angle of this ArcToPathSegment.  # noqa: E501

        Start angle  # noqa: E501

        :return: The start_angle of this ArcToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._start_angle

    @start_angle.setter
    def start_angle(self, start_angle):
        """Sets the start_angle of this ArcToPathSegment.

        Start angle  # noqa: E501

        :param start_angle: The start_angle of this ArcToPathSegment.  # noqa: E501
        :type: float
        """
        self._start_angle = start_angle

    @property
    def sweep_angle(self):
        """Gets the sweep_angle of this ArcToPathSegment.  # noqa: E501

        Sweep angle  # noqa: E501

        :return: The sweep_angle of this ArcToPathSegment.  # noqa: E501
        :rtype: float
        """
        return self._sweep_angle

    @sweep_angle.setter
    def sweep_angle(self, sweep_angle):
        """Sets the sweep_angle of this ArcToPathSegment.

        Sweep angle  # noqa: E501

        :param sweep_angle: The sweep_angle of this ArcToPathSegment.  # noqa: E501
        :type: float
        """
        self._sweep_angle = sweep_angle

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
        if not isinstance(other, ArcToPathSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
