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


class GeometryPath(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fill_mode': 'str',
        'stroke': 'bool',
        'path_data': 'list[PathSegment]'
    }

    attribute_map = {
        'fill_mode': 'fillMode',
        'stroke': 'stroke',
        'path_data': 'pathData'
    }

    type_determiners = {
    }

    def __init__(self, fill_mode=None, stroke=None, path_data=None):  # noqa: E501
        """GeometryPath - a model defined in Swagger"""  # noqa: E501

        self._fill_mode = None
        self._stroke = None
        self._path_data = None

        if fill_mode is not None:
            self.fill_mode = fill_mode
        if stroke is not None:
            self.stroke = stroke
        if path_data is not None:
            self.path_data = path_data

    @property
    def fill_mode(self):
        """Gets the fill_mode of this GeometryPath.  # noqa: E501

        Path fill mode  # noqa: E501

        :return: The fill_mode of this GeometryPath.  # noqa: E501
        :rtype: str
        """
        return self._fill_mode

    @fill_mode.setter
    def fill_mode(self, fill_mode):
        """Sets the fill_mode of this GeometryPath.

        Path fill mode  # noqa: E501

        :param fill_mode: The fill_mode of this GeometryPath.  # noqa: E501
        :type: str
        """
        if fill_mode is not None:
            allowed_values = ["None", "Normal", "Lighten", "LightenLess", "Darken", "DarkenLess"]  # noqa: E501
            if fill_mode.isdigit():
                int_fill_mode = int(fill_mode)
                if int_fill_mode < 0 or int_fill_mode >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `fill_mode` ({0}), must be one of {1}"  # noqa: E501
                        .format(fill_mode, allowed_values)
                    )
                self._fill_mode = allowed_values[int_fill_mode]
                return
            if fill_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `fill_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(fill_mode, allowed_values)
                )
        self._fill_mode = fill_mode

    @property
    def stroke(self):
        """Gets the stroke of this GeometryPath.  # noqa: E501

        Stroke  # noqa: E501

        :return: The stroke of this GeometryPath.  # noqa: E501
        :rtype: bool
        """
        return self._stroke

    @stroke.setter
    def stroke(self, stroke):
        """Sets the stroke of this GeometryPath.

        Stroke  # noqa: E501

        :param stroke: The stroke of this GeometryPath.  # noqa: E501
        :type: bool
        """
        self._stroke = stroke

    @property
    def path_data(self):
        """Gets the path_data of this GeometryPath.  # noqa: E501

        List of PathSegmen objects  # noqa: E501

        :return: The path_data of this GeometryPath.  # noqa: E501
        :rtype: list[PathSegment]
        """
        return self._path_data

    @path_data.setter
    def path_data(self, path_data):
        """Sets the path_data of this GeometryPath.

        List of PathSegmen objects  # noqa: E501

        :param path_data: The path_data of this GeometryPath.  # noqa: E501
        :type: list[PathSegment]
        """
        self._path_data = path_data

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
        if not isinstance(other, GeometryPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
