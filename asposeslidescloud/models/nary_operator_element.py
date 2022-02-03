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

class NaryOperatorElement(MathElement):


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
        'subscript': 'MathElement',
        'superscript': 'MathElement',
        'operator': 'str',
        'limit_location': 'str',
        'grow_to_match_operand_height': 'bool',
        'hide_subscript': 'bool',
        'hide_superscript': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'base': 'base',
        'subscript': 'subscript',
        'superscript': 'superscript',
        'operator': 'operator',
        'limit_location': 'limitLocation',
        'grow_to_match_operand_height': 'growToMatchOperandHeight',
        'hide_subscript': 'hideSubscript',
        'hide_superscript': 'hideSuperscript'
    }

    type_determiners = {
        'type': 'NaryOperator',
    }

    def __init__(self, type='NaryOperator', base=None, subscript=None, superscript=None, operator=None, limit_location=None, grow_to_match_operand_height=None, hide_subscript=None, hide_superscript=None):  # noqa: E501
        """NaryOperatorElement - a model defined in Swagger"""  # noqa: E501
        super(NaryOperatorElement, self).__init__(type)

        self._base = None
        self._subscript = None
        self._superscript = None
        self._operator = None
        self._limit_location = None
        self._grow_to_match_operand_height = None
        self._hide_subscript = None
        self._hide_superscript = None
        self.type = 'NaryOperator'

        if base is not None:
            self.base = base
        if subscript is not None:
            self.subscript = subscript
        if superscript is not None:
            self.superscript = superscript
        if operator is not None:
            self.operator = operator
        if limit_location is not None:
            self.limit_location = limit_location
        if grow_to_match_operand_height is not None:
            self.grow_to_match_operand_height = grow_to_match_operand_height
        if hide_subscript is not None:
            self.hide_subscript = hide_subscript
        if hide_superscript is not None:
            self.hide_superscript = hide_superscript

    @property
    def base(self):
        """Gets the base of this NaryOperatorElement.  # noqa: E501

        Base argument  # noqa: E501

        :return: The base of this NaryOperatorElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this NaryOperatorElement.

        Base argument  # noqa: E501

        :param base: The base of this NaryOperatorElement.  # noqa: E501
        :type: MathElement
        """
        self._base = base

    @property
    def subscript(self):
        """Gets the subscript of this NaryOperatorElement.  # noqa: E501

        Subscript argument  # noqa: E501

        :return: The subscript of this NaryOperatorElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._subscript

    @subscript.setter
    def subscript(self, subscript):
        """Sets the subscript of this NaryOperatorElement.

        Subscript argument  # noqa: E501

        :param subscript: The subscript of this NaryOperatorElement.  # noqa: E501
        :type: MathElement
        """
        self._subscript = subscript

    @property
    def superscript(self):
        """Gets the superscript of this NaryOperatorElement.  # noqa: E501

        Superscript argument  # noqa: E501

        :return: The superscript of this NaryOperatorElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._superscript

    @superscript.setter
    def superscript(self, superscript):
        """Sets the superscript of this NaryOperatorElement.

        Superscript argument  # noqa: E501

        :param superscript: The superscript of this NaryOperatorElement.  # noqa: E501
        :type: MathElement
        """
        self._superscript = superscript

    @property
    def operator(self):
        """Gets the operator of this NaryOperatorElement.  # noqa: E501

        Nary Operator Character  # noqa: E501

        :return: The operator of this NaryOperatorElement.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this NaryOperatorElement.

        Nary Operator Character  # noqa: E501

        :param operator: The operator of this NaryOperatorElement.  # noqa: E501
        :type: str
        """
        self._operator = operator

    @property
    def limit_location(self):
        """Gets the limit_location of this NaryOperatorElement.  # noqa: E501

        The location of limits (subscript and superscript)  # noqa: E501

        :return: The limit_location of this NaryOperatorElement.  # noqa: E501
        :rtype: str
        """
        return self._limit_location

    @limit_location.setter
    def limit_location(self, limit_location):
        """Sets the limit_location of this NaryOperatorElement.

        The location of limits (subscript and superscript)  # noqa: E501

        :param limit_location: The limit_location of this NaryOperatorElement.  # noqa: E501
        :type: str
        """
        if limit_location is not None:
            allowed_values = ["NotDefined", "UnderOver", "SubscriptSuperscript"]  # noqa: E501
            if limit_location.isdigit():
                int_limit_location = int(limit_location)
                if int_limit_location < 0 or int_limit_location >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `limit_location` ({0}), must be one of {1}"  # noqa: E501
                        .format(limit_location, allowed_values)
                    )
                self._limit_location = allowed_values[int_limit_location]
                return
            if limit_location not in allowed_values:
                raise ValueError(
                    "Invalid value for `limit_location` ({0}), must be one of {1}"  # noqa: E501
                    .format(limit_location, allowed_values)
                )
        self._limit_location = limit_location

    @property
    def grow_to_match_operand_height(self):
        """Gets the grow_to_match_operand_height of this NaryOperatorElement.  # noqa: E501

        Operator Character grows vertically to match its operand height  # noqa: E501

        :return: The grow_to_match_operand_height of this NaryOperatorElement.  # noqa: E501
        :rtype: bool
        """
        return self._grow_to_match_operand_height

    @grow_to_match_operand_height.setter
    def grow_to_match_operand_height(self, grow_to_match_operand_height):
        """Sets the grow_to_match_operand_height of this NaryOperatorElement.

        Operator Character grows vertically to match its operand height  # noqa: E501

        :param grow_to_match_operand_height: The grow_to_match_operand_height of this NaryOperatorElement.  # noqa: E501
        :type: bool
        """
        self._grow_to_match_operand_height = grow_to_match_operand_height

    @property
    def hide_subscript(self):
        """Gets the hide_subscript of this NaryOperatorElement.  # noqa: E501

        Hide Subscript  # noqa: E501

        :return: The hide_subscript of this NaryOperatorElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_subscript

    @hide_subscript.setter
    def hide_subscript(self, hide_subscript):
        """Sets the hide_subscript of this NaryOperatorElement.

        Hide Subscript  # noqa: E501

        :param hide_subscript: The hide_subscript of this NaryOperatorElement.  # noqa: E501
        :type: bool
        """
        self._hide_subscript = hide_subscript

    @property
    def hide_superscript(self):
        """Gets the hide_superscript of this NaryOperatorElement.  # noqa: E501

        Hide Superscript  # noqa: E501

        :return: The hide_superscript of this NaryOperatorElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_superscript

    @hide_superscript.setter
    def hide_superscript(self, hide_superscript):
        """Sets the hide_superscript of this NaryOperatorElement.

        Hide Superscript  # noqa: E501

        :param hide_superscript: The hide_superscript of this NaryOperatorElement.  # noqa: E501
        :type: bool
        """
        self._hide_superscript = hide_superscript

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
        if not isinstance(other, NaryOperatorElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
