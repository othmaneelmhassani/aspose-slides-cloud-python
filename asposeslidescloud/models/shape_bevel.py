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


class ShapeBevel(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bevel_type': 'str',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'bevel_type': 'bevelType',
        'width': 'width',
        'height': 'height'
    }

    type_determiners = {
    }

    def __init__(self, bevel_type=None, width=None, height=None):  # noqa: E501
        """ShapeBevel - a model defined in Swagger"""  # noqa: E501

        self._bevel_type = None
        self._width = None
        self._height = None

        if bevel_type is not None:
            self.bevel_type = bevel_type
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def bevel_type(self):
        """Gets the bevel_type of this ShapeBevel.  # noqa: E501

        Bevel type  # noqa: E501

        :return: The bevel_type of this ShapeBevel.  # noqa: E501
        :rtype: str
        """
        return self._bevel_type

    @bevel_type.setter
    def bevel_type(self, bevel_type):
        """Sets the bevel_type of this ShapeBevel.

        Bevel type  # noqa: E501

        :param bevel_type: The bevel_type of this ShapeBevel.  # noqa: E501
        :type: str
        """
        if bevel_type is not None:
            allowed_values = ["Angle", "ArtDeco", "Circle", "Convex", "CoolSlant", "Cross", "Divot", "HardEdge", "RelaxedInset", "Riblet", "Slope", "SoftRound", "NotDefined"]  # noqa: E501
            if bevel_type.isdigit():
                int_bevel_type = int(bevel_type)
                if int_bevel_type < 0 or int_bevel_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `bevel_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(bevel_type, allowed_values)
                    )
                self._bevel_type = allowed_values[int_bevel_type]
                return
            if bevel_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `bevel_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(bevel_type, allowed_values)
                )
        self._bevel_type = bevel_type

    @property
    def width(self):
        """Gets the width of this ShapeBevel.  # noqa: E501

        Bevel width  # noqa: E501

        :return: The width of this ShapeBevel.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ShapeBevel.

        Bevel width  # noqa: E501

        :param width: The width of this ShapeBevel.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ShapeBevel.  # noqa: E501

        Bevel height  # noqa: E501

        :return: The height of this ShapeBevel.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ShapeBevel.

        Bevel height  # noqa: E501

        :param height: The height of this ShapeBevel.  # noqa: E501
        :type: float
        """
        self._height = height

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
        if not isinstance(other, ShapeBevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
