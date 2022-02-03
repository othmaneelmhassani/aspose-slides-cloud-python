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

class ArrayElement(MathElement):


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
        'base_justification': 'str',
        'maximum_distribution': 'bool',
        'object_distribution': 'bool',
        'row_spacing_rule': 'str',
        'row_spacing': 'int'
    }

    attribute_map = {
        'type': 'type',
        'arguments': 'arguments',
        'base_justification': 'baseJustification',
        'maximum_distribution': 'maximumDistribution',
        'object_distribution': 'objectDistribution',
        'row_spacing_rule': 'rowSpacingRule',
        'row_spacing': 'rowSpacing'
    }

    type_determiners = {
        'type': 'Array',
    }

    def __init__(self, type='Array', arguments=None, base_justification=None, maximum_distribution=None, object_distribution=None, row_spacing_rule=None, row_spacing=None):  # noqa: E501
        """ArrayElement - a model defined in Swagger"""  # noqa: E501
        super(ArrayElement, self).__init__(type)

        self._arguments = None
        self._base_justification = None
        self._maximum_distribution = None
        self._object_distribution = None
        self._row_spacing_rule = None
        self._row_spacing = None
        self.type = 'Array'

        if arguments is not None:
            self.arguments = arguments
        if base_justification is not None:
            self.base_justification = base_justification
        if maximum_distribution is not None:
            self.maximum_distribution = maximum_distribution
        if object_distribution is not None:
            self.object_distribution = object_distribution
        if row_spacing_rule is not None:
            self.row_spacing_rule = row_spacing_rule
        if row_spacing is not None:
            self.row_spacing = row_spacing

    @property
    def arguments(self):
        """Gets the arguments of this ArrayElement.  # noqa: E501

        Arguments  # noqa: E501

        :return: The arguments of this ArrayElement.  # noqa: E501
        :rtype: list[MathElement]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ArrayElement.

        Arguments  # noqa: E501

        :param arguments: The arguments of this ArrayElement.  # noqa: E501
        :type: list[MathElement]
        """
        self._arguments = arguments

    @property
    def base_justification(self):
        """Gets the base_justification of this ArrayElement.  # noqa: E501

        Specifies alignment of the array relative to surrounding text  # noqa: E501

        :return: The base_justification of this ArrayElement.  # noqa: E501
        :rtype: str
        """
        return self._base_justification

    @base_justification.setter
    def base_justification(self, base_justification):
        """Sets the base_justification of this ArrayElement.

        Specifies alignment of the array relative to surrounding text  # noqa: E501

        :param base_justification: The base_justification of this ArrayElement.  # noqa: E501
        :type: str
        """
        if base_justification is not None:
            allowed_values = ["NotDefined", "Top", "Center", "Bottom"]  # noqa: E501
            if base_justification.isdigit():
                int_base_justification = int(base_justification)
                if int_base_justification < 0 or int_base_justification >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `base_justification` ({0}), must be one of {1}"  # noqa: E501
                        .format(base_justification, allowed_values)
                    )
                self._base_justification = allowed_values[int_base_justification]
                return
            if base_justification not in allowed_values:
                raise ValueError(
                    "Invalid value for `base_justification` ({0}), must be one of {1}"  # noqa: E501
                    .format(base_justification, allowed_values)
                )
        self._base_justification = base_justification

    @property
    def maximum_distribution(self):
        """Gets the maximum_distribution of this ArrayElement.  # noqa: E501

        Maximum Distribution  # noqa: E501

        :return: The maximum_distribution of this ArrayElement.  # noqa: E501
        :rtype: bool
        """
        return self._maximum_distribution

    @maximum_distribution.setter
    def maximum_distribution(self, maximum_distribution):
        """Sets the maximum_distribution of this ArrayElement.

        Maximum Distribution  # noqa: E501

        :param maximum_distribution: The maximum_distribution of this ArrayElement.  # noqa: E501
        :type: bool
        """
        self._maximum_distribution = maximum_distribution

    @property
    def object_distribution(self):
        """Gets the object_distribution of this ArrayElement.  # noqa: E501

        Object Distribution  # noqa: E501

        :return: The object_distribution of this ArrayElement.  # noqa: E501
        :rtype: bool
        """
        return self._object_distribution

    @object_distribution.setter
    def object_distribution(self, object_distribution):
        """Sets the object_distribution of this ArrayElement.

        Object Distribution  # noqa: E501

        :param object_distribution: The object_distribution of this ArrayElement.  # noqa: E501
        :type: bool
        """
        self._object_distribution = object_distribution

    @property
    def row_spacing_rule(self):
        """Gets the row_spacing_rule of this ArrayElement.  # noqa: E501

        The type of vertical spacing between array elements  # noqa: E501

        :return: The row_spacing_rule of this ArrayElement.  # noqa: E501
        :rtype: str
        """
        return self._row_spacing_rule

    @row_spacing_rule.setter
    def row_spacing_rule(self, row_spacing_rule):
        """Sets the row_spacing_rule of this ArrayElement.

        The type of vertical spacing between array elements  # noqa: E501

        :param row_spacing_rule: The row_spacing_rule of this ArrayElement.  # noqa: E501
        :type: str
        """
        if row_spacing_rule is not None:
            allowed_values = ["SingleLineGap", "OneAndAHalfLineGap", "TwoLineGap", "Exactly", "Multiple"]  # noqa: E501
            if row_spacing_rule.isdigit():
                int_row_spacing_rule = int(row_spacing_rule)
                if int_row_spacing_rule < 0 or int_row_spacing_rule >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `row_spacing_rule` ({0}), must be one of {1}"  # noqa: E501
                        .format(row_spacing_rule, allowed_values)
                    )
                self._row_spacing_rule = allowed_values[int_row_spacing_rule]
                return
            if row_spacing_rule not in allowed_values:
                raise ValueError(
                    "Invalid value for `row_spacing_rule` ({0}), must be one of {1}"  # noqa: E501
                    .format(row_spacing_rule, allowed_values)
                )
        self._row_spacing_rule = row_spacing_rule

    @property
    def row_spacing(self):
        """Gets the row_spacing of this ArrayElement.  # noqa: E501

        Spacing between rows of an array  # noqa: E501

        :return: The row_spacing of this ArrayElement.  # noqa: E501
        :rtype: int
        """
        return self._row_spacing

    @row_spacing.setter
    def row_spacing(self, row_spacing):
        """Sets the row_spacing of this ArrayElement.

        Spacing between rows of an array  # noqa: E501

        :param row_spacing: The row_spacing of this ArrayElement.  # noqa: E501
        :type: int
        """
        self._row_spacing = row_spacing

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
        if not isinstance(other, ArrayElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
