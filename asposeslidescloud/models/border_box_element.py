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

class BorderBoxElement(MathElement):


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
        'hide_top': 'bool',
        'hide_bottom': 'bool',
        'hide_left': 'bool',
        'hide_right': 'bool',
        'strikethrough_horizontal': 'bool',
        'strikethrough_vertical': 'bool',
        'strikethrough_bottom_left_to_top_right': 'bool',
        'strikethrough_top_left_to_bottom_right': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'base': 'base',
        'hide_top': 'hideTop',
        'hide_bottom': 'hideBottom',
        'hide_left': 'hideLeft',
        'hide_right': 'hideRight',
        'strikethrough_horizontal': 'strikethroughHorizontal',
        'strikethrough_vertical': 'strikethroughVertical',
        'strikethrough_bottom_left_to_top_right': 'strikethroughBottomLeftToTopRight',
        'strikethrough_top_left_to_bottom_right': 'strikethroughTopLeftToBottomRight'
    }

    type_determiners = {
        'type': 'BorderBox',
    }

    def __init__(self, type='BorderBox', base=None, hide_top=None, hide_bottom=None, hide_left=None, hide_right=None, strikethrough_horizontal=None, strikethrough_vertical=None, strikethrough_bottom_left_to_top_right=None, strikethrough_top_left_to_bottom_right=None):  # noqa: E501
        """BorderBoxElement - a model defined in Swagger"""  # noqa: E501
        super(BorderBoxElement, self).__init__(type)

        self._base = None
        self._hide_top = None
        self._hide_bottom = None
        self._hide_left = None
        self._hide_right = None
        self._strikethrough_horizontal = None
        self._strikethrough_vertical = None
        self._strikethrough_bottom_left_to_top_right = None
        self._strikethrough_top_left_to_bottom_right = None
        self.type = 'BorderBox'

        if base is not None:
            self.base = base
        if hide_top is not None:
            self.hide_top = hide_top
        if hide_bottom is not None:
            self.hide_bottom = hide_bottom
        if hide_left is not None:
            self.hide_left = hide_left
        if hide_right is not None:
            self.hide_right = hide_right
        if strikethrough_horizontal is not None:
            self.strikethrough_horizontal = strikethrough_horizontal
        if strikethrough_vertical is not None:
            self.strikethrough_vertical = strikethrough_vertical
        if strikethrough_bottom_left_to_top_right is not None:
            self.strikethrough_bottom_left_to_top_right = strikethrough_bottom_left_to_top_right
        if strikethrough_top_left_to_bottom_right is not None:
            self.strikethrough_top_left_to_bottom_right = strikethrough_top_left_to_bottom_right

    @property
    def base(self):
        """Gets the base of this BorderBoxElement.  # noqa: E501

        Base  # noqa: E501

        :return: The base of this BorderBoxElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this BorderBoxElement.

        Base  # noqa: E501

        :param base: The base of this BorderBoxElement.  # noqa: E501
        :type: MathElement
        """
        self._base = base

    @property
    def hide_top(self):
        """Gets the hide_top of this BorderBoxElement.  # noqa: E501

        Hide Top Edge  # noqa: E501

        :return: The hide_top of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_top

    @hide_top.setter
    def hide_top(self, hide_top):
        """Sets the hide_top of this BorderBoxElement.

        Hide Top Edge  # noqa: E501

        :param hide_top: The hide_top of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._hide_top = hide_top

    @property
    def hide_bottom(self):
        """Gets the hide_bottom of this BorderBoxElement.  # noqa: E501

        Hide Bottom Edge  # noqa: E501

        :return: The hide_bottom of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_bottom

    @hide_bottom.setter
    def hide_bottom(self, hide_bottom):
        """Sets the hide_bottom of this BorderBoxElement.

        Hide Bottom Edge  # noqa: E501

        :param hide_bottom: The hide_bottom of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._hide_bottom = hide_bottom

    @property
    def hide_left(self):
        """Gets the hide_left of this BorderBoxElement.  # noqa: E501

        Hide Left Edge  # noqa: E501

        :return: The hide_left of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_left

    @hide_left.setter
    def hide_left(self, hide_left):
        """Sets the hide_left of this BorderBoxElement.

        Hide Left Edge  # noqa: E501

        :param hide_left: The hide_left of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._hide_left = hide_left

    @property
    def hide_right(self):
        """Gets the hide_right of this BorderBoxElement.  # noqa: E501

        Hide Right Edge  # noqa: E501

        :return: The hide_right of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_right

    @hide_right.setter
    def hide_right(self, hide_right):
        """Sets the hide_right of this BorderBoxElement.

        Hide Right Edge  # noqa: E501

        :param hide_right: The hide_right of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._hide_right = hide_right

    @property
    def strikethrough_horizontal(self):
        """Gets the strikethrough_horizontal of this BorderBoxElement.  # noqa: E501

        Strikethrough Horizontal  # noqa: E501

        :return: The strikethrough_horizontal of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._strikethrough_horizontal

    @strikethrough_horizontal.setter
    def strikethrough_horizontal(self, strikethrough_horizontal):
        """Sets the strikethrough_horizontal of this BorderBoxElement.

        Strikethrough Horizontal  # noqa: E501

        :param strikethrough_horizontal: The strikethrough_horizontal of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._strikethrough_horizontal = strikethrough_horizontal

    @property
    def strikethrough_vertical(self):
        """Gets the strikethrough_vertical of this BorderBoxElement.  # noqa: E501

        Strikethrough Vertical  # noqa: E501

        :return: The strikethrough_vertical of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._strikethrough_vertical

    @strikethrough_vertical.setter
    def strikethrough_vertical(self, strikethrough_vertical):
        """Sets the strikethrough_vertical of this BorderBoxElement.

        Strikethrough Vertical  # noqa: E501

        :param strikethrough_vertical: The strikethrough_vertical of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._strikethrough_vertical = strikethrough_vertical

    @property
    def strikethrough_bottom_left_to_top_right(self):
        """Gets the strikethrough_bottom_left_to_top_right of this BorderBoxElement.  # noqa: E501

        Strikethrough Bottom-Left to Top-Right  # noqa: E501

        :return: The strikethrough_bottom_left_to_top_right of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._strikethrough_bottom_left_to_top_right

    @strikethrough_bottom_left_to_top_right.setter
    def strikethrough_bottom_left_to_top_right(self, strikethrough_bottom_left_to_top_right):
        """Sets the strikethrough_bottom_left_to_top_right of this BorderBoxElement.

        Strikethrough Bottom-Left to Top-Right  # noqa: E501

        :param strikethrough_bottom_left_to_top_right: The strikethrough_bottom_left_to_top_right of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._strikethrough_bottom_left_to_top_right = strikethrough_bottom_left_to_top_right

    @property
    def strikethrough_top_left_to_bottom_right(self):
        """Gets the strikethrough_top_left_to_bottom_right of this BorderBoxElement.  # noqa: E501

        Strikethrough Top-Left to Bottom-Right.  # noqa: E501

        :return: The strikethrough_top_left_to_bottom_right of this BorderBoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._strikethrough_top_left_to_bottom_right

    @strikethrough_top_left_to_bottom_right.setter
    def strikethrough_top_left_to_bottom_right(self, strikethrough_top_left_to_bottom_right):
        """Sets the strikethrough_top_left_to_bottom_right of this BorderBoxElement.

        Strikethrough Top-Left to Bottom-Right.  # noqa: E501

        :param strikethrough_top_left_to_bottom_right: The strikethrough_top_left_to_bottom_right of this BorderBoxElement.  # noqa: E501
        :type: bool
        """
        self._strikethrough_top_left_to_bottom_right = strikethrough_top_left_to_bottom_right

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
        if not isinstance(other, BorderBoxElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
