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

from asposeslidescloud.models.scatter_chart_data_point import ScatterChartDataPoint

class BubbleChartDataPoint(ScatterChartDataPoint):


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
        'y_value_formula': 'str',
        'bubble_size': 'float',
        'bubble_size_formula': 'str'
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
        'y_value_formula': 'yValueFormula',
        'bubble_size': 'bubbleSize',
        'bubble_size_formula': 'bubbleSizeFormula'
    }

    type_determiners = {
        'type': 'Bubble',
    }

    def __init__(self, fill_format=None, effect_format=None, three_d_format=None, line_format=None, type='Bubble', x_value=None, y_value=None, x_value_formula=None, y_value_formula=None, bubble_size=None, bubble_size_formula=None):  # noqa: E501
        """BubbleChartDataPoint - a model defined in Swagger"""  # noqa: E501
        super(BubbleChartDataPoint, self).__init__(fill_format, effect_format, three_d_format, line_format, type, x_value, y_value, x_value_formula, y_value_formula)

        self._bubble_size = None
        self._bubble_size_formula = None
        self.type = 'Bubble'

        if bubble_size is not None:
            self.bubble_size = bubble_size
        if bubble_size_formula is not None:
            self.bubble_size_formula = bubble_size_formula

    @property
    def bubble_size(self):
        """Gets the bubble_size of this BubbleChartDataPoint.  # noqa: E501

        Bubble size.  # noqa: E501

        :return: The bubble_size of this BubbleChartDataPoint.  # noqa: E501
        :rtype: float
        """
        return self._bubble_size

    @bubble_size.setter
    def bubble_size(self, bubble_size):
        """Sets the bubble_size of this BubbleChartDataPoint.

        Bubble size.  # noqa: E501

        :param bubble_size: The bubble_size of this BubbleChartDataPoint.  # noqa: E501
        :type: float
        """
        self._bubble_size = bubble_size

    @property
    def bubble_size_formula(self):
        """Gets the bubble_size_formula of this BubbleChartDataPoint.  # noqa: E501

        Spreadsheet formula in A1-style.  # noqa: E501

        :return: The bubble_size_formula of this BubbleChartDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._bubble_size_formula

    @bubble_size_formula.setter
    def bubble_size_formula(self, bubble_size_formula):
        """Sets the bubble_size_formula of this BubbleChartDataPoint.

        Spreadsheet formula in A1-style.  # noqa: E501

        :param bubble_size_formula: The bubble_size_formula of this BubbleChartDataPoint.  # noqa: E501
        :type: str
        """
        self._bubble_size_formula = bubble_size_formula

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
        if not isinstance(other, BubbleChartDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
