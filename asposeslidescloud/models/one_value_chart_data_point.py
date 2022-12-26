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

from asposeslidescloud.models.data_point import DataPoint

class OneValueChartDataPoint(DataPoint):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'three_d_format': 'ThreeDFormat',
        'line_format': 'LineFormat',
        'type': 'str',
        'value': 'float',
        'value_formula': 'str',
        'set_as_total': 'bool',
        'invert_if_negative': 'bool'
    }

    attribute_map = {
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'three_d_format': 'threeDFormat',
        'line_format': 'lineFormat',
        'type': 'type',
        'value': 'value',
        'value_formula': 'valueFormula',
        'set_as_total': 'setAsTotal',
        'invert_if_negative': 'invertIfNegative'
    }

    type_determiners = {
        'type': 'OneValue',
    }

    def __init__(self, fill_format=None, effect_format=None, three_d_format=None, line_format=None, type='OneValue', value=None, value_formula=None, set_as_total=None, invert_if_negative=None):  # noqa: E501
        """OneValueChartDataPoint - a model defined in Swagger"""  # noqa: E501
        super(OneValueChartDataPoint, self).__init__(fill_format, effect_format, three_d_format, line_format, type)

        self._value = None
        self._value_formula = None
        self._set_as_total = None
        self._invert_if_negative = None
        self.type = 'OneValue'

        if value is not None:
            self.value = value
        if value_formula is not None:
            self.value_formula = value_formula
        if set_as_total is not None:
            self.set_as_total = set_as_total
        if invert_if_negative is not None:
            self.invert_if_negative = invert_if_negative

    @property
    def value(self):
        """Gets the value of this OneValueChartDataPoint.  # noqa: E501

        Value.  # noqa: E501

        :return: The value of this OneValueChartDataPoint.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneValueChartDataPoint.

        Value.  # noqa: E501

        :param value: The value of this OneValueChartDataPoint.  # noqa: E501
        :type: float
        """
        self._value = value

    @property
    def value_formula(self):
        """Gets the value_formula of this OneValueChartDataPoint.  # noqa: E501

        Spreadsheet formula in A1-style.  # noqa: E501

        :return: The value_formula of this OneValueChartDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._value_formula

    @value_formula.setter
    def value_formula(self, value_formula):
        """Sets the value_formula of this OneValueChartDataPoint.

        Spreadsheet formula in A1-style.  # noqa: E501

        :param value_formula: The value_formula of this OneValueChartDataPoint.  # noqa: E501
        :type: str
        """
        self._value_formula = value_formula

    @property
    def set_as_total(self):
        """Gets the set_as_total of this OneValueChartDataPoint.  # noqa: E501

        SetAsTotal. Applied to Waterfall data points only.  # noqa: E501

        :return: The set_as_total of this OneValueChartDataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._set_as_total

    @set_as_total.setter
    def set_as_total(self, set_as_total):
        """Sets the set_as_total of this OneValueChartDataPoint.

        SetAsTotal. Applied to Waterfall data points only.  # noqa: E501

        :param set_as_total: The set_as_total of this OneValueChartDataPoint.  # noqa: E501
        :type: bool
        """
        self._set_as_total = set_as_total

    @property
    def invert_if_negative(self):
        """Gets the invert_if_negative of this OneValueChartDataPoint.  # noqa: E501

        True if the data point shall invert its colors if the value is negative. Applies to bar, column and bubble series.  # noqa: E501

        :return: The invert_if_negative of this OneValueChartDataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._invert_if_negative

    @invert_if_negative.setter
    def invert_if_negative(self, invert_if_negative):
        """Sets the invert_if_negative of this OneValueChartDataPoint.

        True if the data point shall invert its colors if the value is negative. Applies to bar, column and bubble series.  # noqa: E501

        :param invert_if_negative: The invert_if_negative of this OneValueChartDataPoint.  # noqa: E501
        :type: bool
        """
        self._invert_if_negative = invert_if_negative

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
        if not isinstance(other, OneValueChartDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
