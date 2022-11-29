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
        'data_source_for_series_name': 'DataSource',
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
        'number_format_of_values': 'str',
        'data_source_for_values': 'DataSource',
        'show_connector_lines': 'bool',
        'quartile_method': 'str',
        'show_inner_points': 'bool',
        'show_mean_line': 'bool',
        'show_mean_markers': 'bool',
        'show_outlier_points': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'data_source_for_series_name': 'dataSourceForSeriesName',
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
        'number_format_of_values': 'numberFormatOfValues',
        'data_source_for_values': 'dataSourceForValues',
        'show_connector_lines': 'showConnectorLines',
        'quartile_method': 'quartileMethod',
        'show_inner_points': 'showInnerPoints',
        'show_mean_line': 'showMeanLine',
        'show_mean_markers': 'showMeanMarkers',
        'show_outlier_points': 'showOutlierPoints'
    }

    type_determiners = {
        'dataPointType': 'OneValue',
    }

    def __init__(self, type=None, name=None, data_source_for_series_name=None, is_color_varied=None, inverted_solid_fill_color=None, smooth=None, plot_on_second_axis=None, order=None, invert_if_negative=None, explosion=None, marker=None, fill_format=None, effect_format=None, line_format=None, data_point_type='OneValue', data_points=None, number_format_of_values=None, data_source_for_values=None, show_connector_lines=None, quartile_method=None, show_inner_points=None, show_mean_line=None, show_mean_markers=None, show_outlier_points=None):  # noqa: E501
        """OneValueSeries - a model defined in Swagger"""  # noqa: E501
        super(OneValueSeries, self).__init__(type, name, data_source_for_series_name, is_color_varied, inverted_solid_fill_color, smooth, plot_on_second_axis, order, invert_if_negative, explosion, marker, fill_format, effect_format, line_format, data_point_type)

        self._data_points = None
        self._number_format_of_values = None
        self._data_source_for_values = None
        self._show_connector_lines = None
        self._quartile_method = None
        self._show_inner_points = None
        self._show_mean_line = None
        self._show_mean_markers = None
        self._show_outlier_points = None
        self.data_point_type = 'OneValue'

        if data_points is not None:
            self.data_points = data_points
        if number_format_of_values is not None:
            self.number_format_of_values = number_format_of_values
        if data_source_for_values is not None:
            self.data_source_for_values = data_source_for_values
        if show_connector_lines is not None:
            self.show_connector_lines = show_connector_lines
        if quartile_method is not None:
            self.quartile_method = quartile_method
        if show_inner_points is not None:
            self.show_inner_points = show_inner_points
        if show_mean_line is not None:
            self.show_mean_line = show_mean_line
        if show_mean_markers is not None:
            self.show_mean_markers = show_mean_markers
        if show_outlier_points is not None:
            self.show_outlier_points = show_outlier_points

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

    @property
    def data_source_for_values(self):
        """Gets the data_source_for_values of this OneValueSeries.  # noqa: E501

        Data source type for values.  # noqa: E501

        :return: The data_source_for_values of this OneValueSeries.  # noqa: E501
        :rtype: DataSource
        """
        return self._data_source_for_values

    @data_source_for_values.setter
    def data_source_for_values(self, data_source_for_values):
        """Sets the data_source_for_values of this OneValueSeries.

        Data source type for values.  # noqa: E501

        :param data_source_for_values: The data_source_for_values of this OneValueSeries.  # noqa: E501
        :type: DataSource
        """
        self._data_source_for_values = data_source_for_values

    @property
    def show_connector_lines(self):
        """Gets the show_connector_lines of this OneValueSeries.  # noqa: E501

        True if inner points are shown. Applied to Waterfall series only.  # noqa: E501

        :return: The show_connector_lines of this OneValueSeries.  # noqa: E501
        :rtype: bool
        """
        return self._show_connector_lines

    @show_connector_lines.setter
    def show_connector_lines(self, show_connector_lines):
        """Sets the show_connector_lines of this OneValueSeries.

        True if inner points are shown. Applied to Waterfall series only.  # noqa: E501

        :param show_connector_lines: The show_connector_lines of this OneValueSeries.  # noqa: E501
        :type: bool
        """
        self._show_connector_lines = show_connector_lines

    @property
    def quartile_method(self):
        """Gets the quartile_method of this OneValueSeries.  # noqa: E501

        Quartile method. Applied to BoxAndWhisker series only.  # noqa: E501

        :return: The quartile_method of this OneValueSeries.  # noqa: E501
        :rtype: str
        """
        return self._quartile_method

    @quartile_method.setter
    def quartile_method(self, quartile_method):
        """Sets the quartile_method of this OneValueSeries.

        Quartile method. Applied to BoxAndWhisker series only.  # noqa: E501

        :param quartile_method: The quartile_method of this OneValueSeries.  # noqa: E501
        :type: str
        """
        if quartile_method is not None:
            allowed_values = ["Exclusive", "Inclusive"]  # noqa: E501
            if quartile_method.isdigit():
                int_quartile_method = int(quartile_method)
                if int_quartile_method < 0 or int_quartile_method >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `quartile_method` ({0}), must be one of {1}"  # noqa: E501
                        .format(quartile_method, allowed_values)
                    )
                self._quartile_method = allowed_values[int_quartile_method]
                return
            if quartile_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `quartile_method` ({0}), must be one of {1}"  # noqa: E501
                    .format(quartile_method, allowed_values)
                )
        self._quartile_method = quartile_method

    @property
    def show_inner_points(self):
        """Gets the show_inner_points of this OneValueSeries.  # noqa: E501

        True if inner points are shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :return: The show_inner_points of this OneValueSeries.  # noqa: E501
        :rtype: bool
        """
        return self._show_inner_points

    @show_inner_points.setter
    def show_inner_points(self, show_inner_points):
        """Sets the show_inner_points of this OneValueSeries.

        True if inner points are shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :param show_inner_points: The show_inner_points of this OneValueSeries.  # noqa: E501
        :type: bool
        """
        self._show_inner_points = show_inner_points

    @property
    def show_mean_line(self):
        """Gets the show_mean_line of this OneValueSeries.  # noqa: E501

        True if mean line is shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :return: The show_mean_line of this OneValueSeries.  # noqa: E501
        :rtype: bool
        """
        return self._show_mean_line

    @show_mean_line.setter
    def show_mean_line(self, show_mean_line):
        """Sets the show_mean_line of this OneValueSeries.

        True if mean line is shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :param show_mean_line: The show_mean_line of this OneValueSeries.  # noqa: E501
        :type: bool
        """
        self._show_mean_line = show_mean_line

    @property
    def show_mean_markers(self):
        """Gets the show_mean_markers of this OneValueSeries.  # noqa: E501

        True if mean markers are shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :return: The show_mean_markers of this OneValueSeries.  # noqa: E501
        :rtype: bool
        """
        return self._show_mean_markers

    @show_mean_markers.setter
    def show_mean_markers(self, show_mean_markers):
        """Sets the show_mean_markers of this OneValueSeries.

        True if mean markers are shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :param show_mean_markers: The show_mean_markers of this OneValueSeries.  # noqa: E501
        :type: bool
        """
        self._show_mean_markers = show_mean_markers

    @property
    def show_outlier_points(self):
        """Gets the show_outlier_points of this OneValueSeries.  # noqa: E501

        True if outlier points are shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :return: The show_outlier_points of this OneValueSeries.  # noqa: E501
        :rtype: bool
        """
        return self._show_outlier_points

    @show_outlier_points.setter
    def show_outlier_points(self, show_outlier_points):
        """Sets the show_outlier_points of this OneValueSeries.

        True if outlier points are shown. Applied to BoxAndWhisker series only.  # noqa: E501

        :param show_outlier_points: The show_outlier_points of this OneValueSeries.  # noqa: E501
        :type: bool
        """
        self._show_outlier_points = show_outlier_points

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
