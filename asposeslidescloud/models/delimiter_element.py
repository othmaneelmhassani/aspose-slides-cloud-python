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

class DelimiterElement(MathElement):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'arguments': 'list[MathElement]',
        'beginning_character': 'str',
        'separator_character': 'str',
        'ending_character': 'str',
        'grow_to_match_operand_height': 'bool',
        'delimiter_shape': 'str'
    }

    attribute_map = {
        'type': 'type',
        'arguments': 'arguments',
        'beginning_character': 'beginningCharacter',
        'separator_character': 'separatorCharacter',
        'ending_character': 'endingCharacter',
        'grow_to_match_operand_height': 'growToMatchOperandHeight',
        'delimiter_shape': 'delimiterShape'
    }

    type_determiners = {
        'type': 'Delimiter',
    }

    def __init__(self, type='Delimiter', arguments=None, beginning_character=None, separator_character=None, ending_character=None, grow_to_match_operand_height=None, delimiter_shape=None):  # noqa: E501
        """DelimiterElement - a model defined in Swagger"""  # noqa: E501
        super(DelimiterElement, self).__init__(type)

        self._arguments = None
        self._beginning_character = None
        self._separator_character = None
        self._ending_character = None
        self._grow_to_match_operand_height = None
        self._delimiter_shape = None
        self.type = 'Delimiter'

        if arguments is not None:
            self.arguments = arguments
        if beginning_character is not None:
            self.beginning_character = beginning_character
        if separator_character is not None:
            self.separator_character = separator_character
        if ending_character is not None:
            self.ending_character = ending_character
        if grow_to_match_operand_height is not None:
            self.grow_to_match_operand_height = grow_to_match_operand_height
        if delimiter_shape is not None:
            self.delimiter_shape = delimiter_shape

    @property
    def arguments(self):
        """Gets the arguments of this DelimiterElement.  # noqa: E501

        Arguments  # noqa: E501

        :return: The arguments of this DelimiterElement.  # noqa: E501
        :rtype: list[MathElement]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this DelimiterElement.

        Arguments  # noqa: E501

        :param arguments: The arguments of this DelimiterElement.  # noqa: E501
        :type: list[MathElement]
        """
        self._arguments = arguments

    @property
    def beginning_character(self):
        """Gets the beginning_character of this DelimiterElement.  # noqa: E501

        Beginning character  # noqa: E501

        :return: The beginning_character of this DelimiterElement.  # noqa: E501
        :rtype: str
        """
        return self._beginning_character

    @beginning_character.setter
    def beginning_character(self, beginning_character):
        """Sets the beginning_character of this DelimiterElement.

        Beginning character  # noqa: E501

        :param beginning_character: The beginning_character of this DelimiterElement.  # noqa: E501
        :type: str
        """
        self._beginning_character = beginning_character

    @property
    def separator_character(self):
        """Gets the separator_character of this DelimiterElement.  # noqa: E501

        Separator character  # noqa: E501

        :return: The separator_character of this DelimiterElement.  # noqa: E501
        :rtype: str
        """
        return self._separator_character

    @separator_character.setter
    def separator_character(self, separator_character):
        """Sets the separator_character of this DelimiterElement.

        Separator character  # noqa: E501

        :param separator_character: The separator_character of this DelimiterElement.  # noqa: E501
        :type: str
        """
        self._separator_character = separator_character

    @property
    def ending_character(self):
        """Gets the ending_character of this DelimiterElement.  # noqa: E501

        Ending character  # noqa: E501

        :return: The ending_character of this DelimiterElement.  # noqa: E501
        :rtype: str
        """
        return self._ending_character

    @ending_character.setter
    def ending_character(self, ending_character):
        """Sets the ending_character of this DelimiterElement.

        Ending character  # noqa: E501

        :param ending_character: The ending_character of this DelimiterElement.  # noqa: E501
        :type: str
        """
        self._ending_character = ending_character

    @property
    def grow_to_match_operand_height(self):
        """Gets the grow_to_match_operand_height of this DelimiterElement.  # noqa: E501

        Grow to match operand height  # noqa: E501

        :return: The grow_to_match_operand_height of this DelimiterElement.  # noqa: E501
        :rtype: bool
        """
        return self._grow_to_match_operand_height

    @grow_to_match_operand_height.setter
    def grow_to_match_operand_height(self, grow_to_match_operand_height):
        """Sets the grow_to_match_operand_height of this DelimiterElement.

        Grow to match operand height  # noqa: E501

        :param grow_to_match_operand_height: The grow_to_match_operand_height of this DelimiterElement.  # noqa: E501
        :type: bool
        """
        self._grow_to_match_operand_height = grow_to_match_operand_height

    @property
    def delimiter_shape(self):
        """Gets the delimiter_shape of this DelimiterElement.  # noqa: E501

        Delimiter shape  # noqa: E501

        :return: The delimiter_shape of this DelimiterElement.  # noqa: E501
        :rtype: str
        """
        return self._delimiter_shape

    @delimiter_shape.setter
    def delimiter_shape(self, delimiter_shape):
        """Sets the delimiter_shape of this DelimiterElement.

        Delimiter shape  # noqa: E501

        :param delimiter_shape: The delimiter_shape of this DelimiterElement.  # noqa: E501
        :type: str
        """
        if delimiter_shape is not None:
            allowed_values = ["Centered", "Match"]  # noqa: E501
            if delimiter_shape.isdigit():
                int_delimiter_shape = int(delimiter_shape)
                if int_delimiter_shape < 0 or int_delimiter_shape >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `delimiter_shape` ({0}), must be one of {1}"  # noqa: E501
                        .format(delimiter_shape, allowed_values)
                    )
                self._delimiter_shape = allowed_values[int_delimiter_shape]
                return
            if delimiter_shape not in allowed_values:
                raise ValueError(
                    "Invalid value for `delimiter_shape` ({0}), must be one of {1}"  # noqa: E501
                    .format(delimiter_shape, allowed_values)
                )
        self._delimiter_shape = delimiter_shape

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
        if not isinstance(other, DelimiterElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
