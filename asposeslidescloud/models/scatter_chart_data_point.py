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

class ScatterChartDataPoint(DataPoint):


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
        'x_value': 'float',
        'y_value': 'float',
        'x_value_formula': 'str',
        'y_value_formula': 'str'
    }

    attribute_map = {
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'three_d_format': 'threeDFormat',
        'line_format': 'lineFormat',
        'type': 'type',
        'x_value': 'xValue',
        'y_value': 'yValue',
        'x_value_formula': 'xValueFormula',
        'y_value_formula': 'yValueFormula'
    }

    type_determiners = {
        'type': 'Scatter',
    }

    def __init__(self, fill_format=None, effect_format=None, three_d_format=None, line_format=None, type='Scatter', x_value=None, y_value=None, x_value_formula=None, y_value_formula=None):  # noqa: E501
        """ScatterChartDataPoint - a model defined in Swagger"""  # noqa: E501
        super(ScatterChartDataPoint, self).__init__(fill_format, effect_format, three_d_format, line_format, type)

        self._x_value = None
        self._y_value = None
        self._x_value_formula = None
        self._y_value_formula = None
        self.type = 'Scatter'

        if x_value is not None:
            self.x_value = x_value
        if y_value is not None:
            self.y_value = y_value
        if x_value_formula is not None:
            self.x_value_formula = x_value_formula
        if y_value_formula is not None:
            self.y_value_formula = y_value_formula

    @property
    def x_value(self):
        """Gets the x_value of this ScatterChartDataPoint.  # noqa: E501

        X-value  # noqa: E501

        :return: The x_value of this ScatterChartDataPoint.  # noqa: E501
        :rtype: float
        """
        return self._x_value

    @x_value.setter
    def x_value(self, x_value):
        """Sets the x_value of this ScatterChartDataPoint.

        X-value  # noqa: E501

        :param x_value: The x_value of this ScatterChartDataPoint.  # noqa: E501
        :type: float
        """
        self._x_value = x_value

    @property
    def y_value(self):
        """Gets the y_value of this ScatterChartDataPoint.  # noqa: E501

        Y-value  # noqa: E501

        :return: The y_value of this ScatterChartDataPoint.  # noqa: E501
        :rtype: float
        """
        return self._y_value

    @y_value.setter
    def y_value(self, y_value):
        """Sets the y_value of this ScatterChartDataPoint.

        Y-value  # noqa: E501

        :param y_value: The y_value of this ScatterChartDataPoint.  # noqa: E501
        :type: float
        """
        self._y_value = y_value

    @property
    def x_value_formula(self):
        """Gets the x_value_formula of this ScatterChartDataPoint.  # noqa: E501

        Spreadsheet formula in A1-style.  # noqa: E501

        :return: The x_value_formula of this ScatterChartDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._x_value_formula

    @x_value_formula.setter
    def x_value_formula(self, x_value_formula):
        """Sets the x_value_formula of this ScatterChartDataPoint.

        Spreadsheet formula in A1-style.  # noqa: E501

        :param x_value_formula: The x_value_formula of this ScatterChartDataPoint.  # noqa: E501
        :type: str
        """
        self._x_value_formula = x_value_formula

    @property
    def y_value_formula(self):
        """Gets the y_value_formula of this ScatterChartDataPoint.  # noqa: E501

        Spreadsheet formula in A1-style.  # noqa: E501

        :return: The y_value_formula of this ScatterChartDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._y_value_formula

    @y_value_formula.setter
    def y_value_formula(self, y_value_formula):
        """Sets the y_value_formula of this ScatterChartDataPoint.

        Spreadsheet formula in A1-style.  # noqa: E501

        :param y_value_formula: The y_value_formula of this ScatterChartDataPoint.  # noqa: E501
        :type: str
        """
        self._y_value_formula = y_value_formula

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
        if not isinstance(other, ScatterChartDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
