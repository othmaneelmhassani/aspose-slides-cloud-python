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

class BoxElement(MathElement):


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
        'operator_emulator': 'bool',
        'no_break': 'bool',
        'differential': 'bool',
        'alignment_point': 'bool',
        'explicit_break': 'int'
    }

    attribute_map = {
        'type': 'type',
        'base': 'base',
        'operator_emulator': 'operatorEmulator',
        'no_break': 'noBreak',
        'differential': 'differential',
        'alignment_point': 'alignmentPoint',
        'explicit_break': 'explicitBreak'
    }

    type_determiners = {
        'type': 'Box',
    }

    def __init__(self, type='Box', base=None, operator_emulator=None, no_break=None, differential=None, alignment_point=None, explicit_break=None):  # noqa: E501
        """BoxElement - a model defined in Swagger"""  # noqa: E501
        super(BoxElement, self).__init__(type)

        self._base = None
        self._operator_emulator = None
        self._no_break = None
        self._differential = None
        self._alignment_point = None
        self._explicit_break = None
        self.type = 'Box'

        if base is not None:
            self.base = base
        if operator_emulator is not None:
            self.operator_emulator = operator_emulator
        if no_break is not None:
            self.no_break = no_break
        if differential is not None:
            self.differential = differential
        if alignment_point is not None:
            self.alignment_point = alignment_point
        if explicit_break is not None:
            self.explicit_break = explicit_break

    @property
    def base(self):
        """Gets the base of this BoxElement.  # noqa: E501

        Base  # noqa: E501

        :return: The base of this BoxElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this BoxElement.

        Base  # noqa: E501

        :param base: The base of this BoxElement.  # noqa: E501
        :type: MathElement
        """
        self._base = base

    @property
    def operator_emulator(self):
        """Gets the operator_emulator of this BoxElement.  # noqa: E501

        Operator emulator  # noqa: E501

        :return: The operator_emulator of this BoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._operator_emulator

    @operator_emulator.setter
    def operator_emulator(self, operator_emulator):
        """Sets the operator_emulator of this BoxElement.

        Operator emulator  # noqa: E501

        :param operator_emulator: The operator_emulator of this BoxElement.  # noqa: E501
        :type: bool
        """
        self._operator_emulator = operator_emulator

    @property
    def no_break(self):
        """Gets the no_break of this BoxElement.  # noqa: E501

        No break  # noqa: E501

        :return: The no_break of this BoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._no_break

    @no_break.setter
    def no_break(self, no_break):
        """Sets the no_break of this BoxElement.

        No break  # noqa: E501

        :param no_break: The no_break of this BoxElement.  # noqa: E501
        :type: bool
        """
        self._no_break = no_break

    @property
    def differential(self):
        """Gets the differential of this BoxElement.  # noqa: E501

        Differential  # noqa: E501

        :return: The differential of this BoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._differential

    @differential.setter
    def differential(self, differential):
        """Sets the differential of this BoxElement.

        Differential  # noqa: E501

        :param differential: The differential of this BoxElement.  # noqa: E501
        :type: bool
        """
        self._differential = differential

    @property
    def alignment_point(self):
        """Gets the alignment_point of this BoxElement.  # noqa: E501

        Alignment point  # noqa: E501

        :return: The alignment_point of this BoxElement.  # noqa: E501
        :rtype: bool
        """
        return self._alignment_point

    @alignment_point.setter
    def alignment_point(self, alignment_point):
        """Sets the alignment_point of this BoxElement.

        Alignment point  # noqa: E501

        :param alignment_point: The alignment_point of this BoxElement.  # noqa: E501
        :type: bool
        """
        self._alignment_point = alignment_point

    @property
    def explicit_break(self):
        """Gets the explicit_break of this BoxElement.  # noqa: E501

        Explicit break  # noqa: E501

        :return: The explicit_break of this BoxElement.  # noqa: E501
        :rtype: int
        """
        return self._explicit_break

    @explicit_break.setter
    def explicit_break(self, explicit_break):
        """Sets the explicit_break of this BoxElement.

        Explicit break  # noqa: E501

        :param explicit_break: The explicit_break of this BoxElement.  # noqa: E501
        :type: int
        """
        self._explicit_break = explicit_break

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
        if not isinstance(other, BoxElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
