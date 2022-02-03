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

class MatrixElement(MathElement):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'hide_placeholders': 'bool',
        'base_justification': 'str',
        'min_column_width': 'int',
        'column_gap_rule': 'str',
        'column_gap': 'int',
        'row_gap_rule': 'str',
        'row_gap': 'int',
        'items': 'list[list[MathElement]]'
    }

    attribute_map = {
        'type': 'type',
        'hide_placeholders': 'hidePlaceholders',
        'base_justification': 'baseJustification',
        'min_column_width': 'minColumnWidth',
        'column_gap_rule': 'columnGapRule',
        'column_gap': 'columnGap',
        'row_gap_rule': 'rowGapRule',
        'row_gap': 'rowGap',
        'items': 'items'
    }

    type_determiners = {
        'type': 'Matrix',
    }

    def __init__(self, type='Matrix', hide_placeholders=None, base_justification=None, min_column_width=None, column_gap_rule=None, column_gap=None, row_gap_rule=None, row_gap=None, items=None):  # noqa: E501
        """MatrixElement - a model defined in Swagger"""  # noqa: E501
        super(MatrixElement, self).__init__(type)

        self._hide_placeholders = None
        self._base_justification = None
        self._min_column_width = None
        self._column_gap_rule = None
        self._column_gap = None
        self._row_gap_rule = None
        self._row_gap = None
        self._items = None
        self.type = 'Matrix'

        if hide_placeholders is not None:
            self.hide_placeholders = hide_placeholders
        if base_justification is not None:
            self.base_justification = base_justification
        if min_column_width is not None:
            self.min_column_width = min_column_width
        if column_gap_rule is not None:
            self.column_gap_rule = column_gap_rule
        if column_gap is not None:
            self.column_gap = column_gap
        if row_gap_rule is not None:
            self.row_gap_rule = row_gap_rule
        if row_gap is not None:
            self.row_gap = row_gap
        if items is not None:
            self.items = items

    @property
    def hide_placeholders(self):
        """Gets the hide_placeholders of this MatrixElement.  # noqa: E501

        Hide the placeholders for empty matrix elements  # noqa: E501

        :return: The hide_placeholders of this MatrixElement.  # noqa: E501
        :rtype: bool
        """
        return self._hide_placeholders

    @hide_placeholders.setter
    def hide_placeholders(self, hide_placeholders):
        """Sets the hide_placeholders of this MatrixElement.

        Hide the placeholders for empty matrix elements  # noqa: E501

        :param hide_placeholders: The hide_placeholders of this MatrixElement.  # noqa: E501
        :type: bool
        """
        self._hide_placeholders = hide_placeholders

    @property
    def base_justification(self):
        """Gets the base_justification of this MatrixElement.  # noqa: E501

        Specifies the vertical justification respect to surrounding text.   # noqa: E501

        :return: The base_justification of this MatrixElement.  # noqa: E501
        :rtype: str
        """
        return self._base_justification

    @base_justification.setter
    def base_justification(self, base_justification):
        """Sets the base_justification of this MatrixElement.

        Specifies the vertical justification respect to surrounding text.   # noqa: E501

        :param base_justification: The base_justification of this MatrixElement.  # noqa: E501
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
    def min_column_width(self):
        """Gets the min_column_width of this MatrixElement.  # noqa: E501

        Minimum column width in twips (1/20th of a point)  # noqa: E501

        :return: The min_column_width of this MatrixElement.  # noqa: E501
        :rtype: int
        """
        return self._min_column_width

    @min_column_width.setter
    def min_column_width(self, min_column_width):
        """Sets the min_column_width of this MatrixElement.

        Minimum column width in twips (1/20th of a point)  # noqa: E501

        :param min_column_width: The min_column_width of this MatrixElement.  # noqa: E501
        :type: int
        """
        self._min_column_width = min_column_width

    @property
    def column_gap_rule(self):
        """Gets the column_gap_rule of this MatrixElement.  # noqa: E501

        The type of horizontal spacing between columns of a matrix.  # noqa: E501

        :return: The column_gap_rule of this MatrixElement.  # noqa: E501
        :rtype: str
        """
        return self._column_gap_rule

    @column_gap_rule.setter
    def column_gap_rule(self, column_gap_rule):
        """Sets the column_gap_rule of this MatrixElement.

        The type of horizontal spacing between columns of a matrix.  # noqa: E501

        :param column_gap_rule: The column_gap_rule of this MatrixElement.  # noqa: E501
        :type: str
        """
        if column_gap_rule is not None:
            allowed_values = ["SingleSpacingGap", "OneAndHalfSpacingGap", "DoubleSpacingGap", "Exactly", "Multiple"]  # noqa: E501
            if column_gap_rule.isdigit():
                int_column_gap_rule = int(column_gap_rule)
                if int_column_gap_rule < 0 or int_column_gap_rule >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `column_gap_rule` ({0}), must be one of {1}"  # noqa: E501
                        .format(column_gap_rule, allowed_values)
                    )
                self._column_gap_rule = allowed_values[int_column_gap_rule]
                return
            if column_gap_rule not in allowed_values:
                raise ValueError(
                    "Invalid value for `column_gap_rule` ({0}), must be one of {1}"  # noqa: E501
                    .format(column_gap_rule, allowed_values)
                )
        self._column_gap_rule = column_gap_rule

    @property
    def column_gap(self):
        """Gets the column_gap of this MatrixElement.  # noqa: E501

        The value of horizontal spacing between columns of a matrix  # noqa: E501

        :return: The column_gap of this MatrixElement.  # noqa: E501
        :rtype: int
        """
        return self._column_gap

    @column_gap.setter
    def column_gap(self, column_gap):
        """Sets the column_gap of this MatrixElement.

        The value of horizontal spacing between columns of a matrix  # noqa: E501

        :param column_gap: The column_gap of this MatrixElement.  # noqa: E501
        :type: int
        """
        self._column_gap = column_gap

    @property
    def row_gap_rule(self):
        """Gets the row_gap_rule of this MatrixElement.  # noqa: E501

        The type of vertical spacing between rows of a matrix  # noqa: E501

        :return: The row_gap_rule of this MatrixElement.  # noqa: E501
        :rtype: str
        """
        return self._row_gap_rule

    @row_gap_rule.setter
    def row_gap_rule(self, row_gap_rule):
        """Sets the row_gap_rule of this MatrixElement.

        The type of vertical spacing between rows of a matrix  # noqa: E501

        :param row_gap_rule: The row_gap_rule of this MatrixElement.  # noqa: E501
        :type: str
        """
        if row_gap_rule is not None:
            allowed_values = ["SingleSpacingGap", "OneAndHalfSpacingGap", "DoubleSpacingGap", "Exactly", "Multiple"]  # noqa: E501
            if row_gap_rule.isdigit():
                int_row_gap_rule = int(row_gap_rule)
                if int_row_gap_rule < 0 or int_row_gap_rule >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `row_gap_rule` ({0}), must be one of {1}"  # noqa: E501
                        .format(row_gap_rule, allowed_values)
                    )
                self._row_gap_rule = allowed_values[int_row_gap_rule]
                return
            if row_gap_rule not in allowed_values:
                raise ValueError(
                    "Invalid value for `row_gap_rule` ({0}), must be one of {1}"  # noqa: E501
                    .format(row_gap_rule, allowed_values)
                )
        self._row_gap_rule = row_gap_rule

    @property
    def row_gap(self):
        """Gets the row_gap of this MatrixElement.  # noqa: E501

        The value of vertical spacing between rows of a matrix;               # noqa: E501

        :return: The row_gap of this MatrixElement.  # noqa: E501
        :rtype: int
        """
        return self._row_gap

    @row_gap.setter
    def row_gap(self, row_gap):
        """Sets the row_gap of this MatrixElement.

        The value of vertical spacing between rows of a matrix;               # noqa: E501

        :param row_gap: The row_gap of this MatrixElement.  # noqa: E501
        :type: int
        """
        self._row_gap = row_gap

    @property
    def items(self):
        """Gets the items of this MatrixElement.  # noqa: E501

        Matrix items  # noqa: E501

        :return: The items of this MatrixElement.  # noqa: E501
        :rtype: list[list[MathElement]]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this MatrixElement.

        Matrix items  # noqa: E501

        :param items: The items of this MatrixElement.  # noqa: E501
        :type: list[list[MathElement]]
        """
        self._items = items

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
        if not isinstance(other, MatrixElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
