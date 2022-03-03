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

from asposeslidescloud.models.series import Series

class OneValueSeries(Series):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'name': 'str',
        'is_color_varied': 'bool',
        'inverted_solid_fill_color': 'str',
        'smooth': 'bool',
        'plot_on_second_axis': 'bool',
        'order': 'int',
        'invert_if_negative': 'bool',
        'explosion': 'int',
        'marker': 'SeriesMarker',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'line_format': 'LineFormat',
        'data_point_type': 'str',
        'data_points': 'list[OneValueChartDataPoint]',
        'number_format_of_values': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'is_color_varied': 'isColorVaried',
        'inverted_solid_fill_color': 'invertedSolidFillColor',
        'smooth': 'smooth',
        'plot_on_second_axis': 'plotOnSecondAxis',
        'order': 'order',
        'invert_if_negative': 'invertIfNegative',
        'explosion': 'explosion',
        'marker': 'marker',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'line_format': 'lineFormat',
        'data_point_type': 'dataPointType',
        'data_points': 'dataPoints',
        'number_format_of_values': 'numberFormatOfValues'
    }

    type_determiners = {
        'dataPointType': 'OneValue',
    }

    def __init__(self, type=None, name=None, is_color_varied=None, inverted_solid_fill_color=None, smooth=None, plot_on_second_axis=None, order=None, invert_if_negative=None, explosion=None, marker=None, fill_format=None, effect_format=None, line_format=None, data_point_type='OneValue', data_points=None, number_format_of_values=None):  # noqa: E501
        """OneValueSeries - a model defined in Swagger"""  # noqa: E501
        super(OneValueSeries, self).__init__(type, name, is_color_varied, inverted_solid_fill_color, smooth, plot_on_second_axis, order, invert_if_negative, explosion, marker, fill_format, effect_format, line_format, data_point_type)

        self._data_points = None
        self._number_format_of_values = None
        self.data_point_type = 'OneValue'

        if data_points is not None:
            self.data_points = data_points
        if number_format_of_values is not None:
            self.number_format_of_values = number_format_of_values

    @property
    def data_points(self):
        """Gets the data_points of this OneValueSeries.  # noqa: E501

        Gets or sets the values.  # noqa: E501

        :return: The data_points of this OneValueSeries.  # noqa: E501
        :rtype: list[OneValueChartDataPoint]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this OneValueSeries.

        Gets or sets the values.  # noqa: E501

        :param data_points: The data_points of this OneValueSeries.  # noqa: E501
        :type: list[OneValueChartDataPoint]
        """
        self._data_points = data_points

    @property
    def number_format_of_values(self):
        """Gets the number_format_of_values of this OneValueSeries.  # noqa: E501

        The number format for the series values.  # noqa: E501

        :return: The number_format_of_values of this OneValueSeries.  # noqa: E501
        :rtype: str
        """
        return self._number_format_of_values

    @number_format_of_values.setter
    def number_format_of_values(self, number_format_of_values):
        """Sets the number_format_of_values of this OneValueSeries.

        The number format for the series values.  # noqa: E501

        :param number_format_of_values: The number_format_of_values of this OneValueSeries.  # noqa: E501
        :type: str
        """
        self._number_format_of_values = number_format_of_values

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
        if not isinstance(other, OneValueSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
