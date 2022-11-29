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

from asposeslidescloud.models.shape_base import ShapeBase

class Chart(ShapeBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'self_uri': 'ResourceUri',
        'alternate_links': 'list[ResourceUri]',
        'name': 'str',
        'width': 'float',
        'height': 'float',
        'alternative_text': 'str',
        'alternative_text_title': 'str',
        'hidden': 'bool',
        'x': 'float',
        'y': 'float',
        'z_order_position': 'int',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'three_d_format': 'ThreeDFormat',
        'line_format': 'LineFormat',
        'hyperlink_click': 'Hyperlink',
        'hyperlink_mouse_over': 'Hyperlink',
        'type': 'str',
        'chart_type': 'str',
        'show_data_labels_over_maximum': 'bool',
        'series': 'list[Series]',
        'categories': 'list[ChartCategory]',
        'data_source_for_categories': 'DataSource',
        'title': 'ChartTitle',
        'back_wall': 'ChartWall',
        'side_wall': 'ChartWall',
        'floor': 'ChartWall',
        'legend': 'Legend',
        'axes': 'Axes',
        'plot_area': 'PlotArea',
        'has_rounded_corners': 'bool',
        'series_groups': 'list[ChartSeriesGroup]'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'name': 'name',
        'width': 'width',
        'height': 'height',
        'alternative_text': 'alternativeText',
        'alternative_text_title': 'alternativeTextTitle',
        'hidden': 'hidden',
        'x': 'x',
        'y': 'y',
        'z_order_position': 'zOrderPosition',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'three_d_format': 'threeDFormat',
        'line_format': 'lineFormat',
        'hyperlink_click': 'hyperlinkClick',
        'hyperlink_mouse_over': 'hyperlinkMouseOver',
        'type': 'type',
        'chart_type': 'chartType',
        'show_data_labels_over_maximum': 'showDataLabelsOverMaximum',
        'series': 'series',
        'categories': 'categories',
        'data_source_for_categories': 'dataSourceForCategories',
        'title': 'title',
        'back_wall': 'backWall',
        'side_wall': 'sideWall',
        'floor': 'floor',
        'legend': 'legend',
        'axes': 'axes',
        'plot_area': 'plotArea',
        'has_rounded_corners': 'hasRoundedCorners',
        'series_groups': 'seriesGroups'
    }

    type_determiners = {
        'type': 'Chart',
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, width=None, height=None, alternative_text=None, alternative_text_title=None, hidden=None, x=None, y=None, z_order_position=None, fill_format=None, effect_format=None, three_d_format=None, line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, type='Chart', chart_type=None, show_data_labels_over_maximum=None, series=None, categories=None, data_source_for_categories=None, title=None, back_wall=None, side_wall=None, floor=None, legend=None, axes=None, plot_area=None, has_rounded_corners=None, series_groups=None):  # noqa: E501
        """Chart - a model defined in Swagger"""  # noqa: E501
        super(Chart, self).__init__(self_uri, alternate_links, name, width, height, alternative_text, alternative_text_title, hidden, x, y, z_order_position, fill_format, effect_format, three_d_format, line_format, hyperlink_click, hyperlink_mouse_over, type)

        self._chart_type = None
        self._show_data_labels_over_maximum = None
        self._series = None
        self._categories = None
        self._data_source_for_categories = None
        self._title = None
        self._back_wall = None
        self._side_wall = None
        self._floor = None
        self._legend = None
        self._axes = None
        self._plot_area = None
        self._has_rounded_corners = None
        self._series_groups = None
        self.type = 'Chart'

        self.chart_type = chart_type
        if show_data_labels_over_maximum is not None:
            self.show_data_labels_over_maximum = show_data_labels_over_maximum
        if series is not None:
            self.series = series
        if categories is not None:
            self.categories = categories
        if data_source_for_categories is not None:
            self.data_source_for_categories = data_source_for_categories
        if title is not None:
            self.title = title
        if back_wall is not None:
            self.back_wall = back_wall
        if side_wall is not None:
            self.side_wall = side_wall
        if floor is not None:
            self.floor = floor
        if legend is not None:
            self.legend = legend
        if axes is not None:
            self.axes = axes
        if plot_area is not None:
            self.plot_area = plot_area
        if has_rounded_corners is not None:
            self.has_rounded_corners = has_rounded_corners
        if series_groups is not None:
            self.series_groups = series_groups

    @property
    def chart_type(self):
        """Gets the chart_type of this Chart.  # noqa: E501

        Gets or sets the type of the chart.  # noqa: E501

        :return: The chart_type of this Chart.  # noqa: E501
        :rtype: str
        """
        return self._chart_type

    @chart_type.setter
    def chart_type(self, chart_type):
        """Sets the chart_type of this Chart.

        Gets or sets the type of the chart.  # noqa: E501

        :param chart_type: The chart_type of this Chart.  # noqa: E501
        :type: str
        """
        if chart_type is not None:
            allowed_values = ["ClusteredColumn", "StackedColumn", "PercentsStackedColumn", "ClusteredColumn3D", "StackedColumn3D", "PercentsStackedColumn3D", "Column3D", "ClusteredCylinder", "StackedCylinder", "PercentsStackedCylinder", "Cylinder3D", "ClusteredCone", "StackedCone", "PercentsStackedCone", "Cone3D", "ClusteredPyramid", "StackedPyramid", "PercentsStackedPyramid", "Pyramid3D", "Line", "StackedLine", "PercentsStackedLine", "LineWithMarkers", "StackedLineWithMarkers", "PercentsStackedLineWithMarkers", "Line3D", "Pie", "Pie3D", "PieOfPie", "ExplodedPie", "ExplodedPie3D", "BarOfPie", "PercentsStackedBar", "ClusteredBar3D", "ClusteredBar", "StackedBar", "StackedBar3D", "PercentsStackedBar3D", "ClusteredHorizontalCylinder", "StackedHorizontalCylinder", "PercentsStackedHorizontalCylinder", "ClusteredHorizontalCone", "StackedHorizontalCone", "PercentsStackedHorizontalCone", "ClusteredHorizontalPyramid", "StackedHorizontalPyramid", "PercentsStackedHorizontalPyramid", "Area", "StackedArea", "PercentsStackedArea", "Area3D", "StackedArea3D", "PercentsStackedArea3D", "ScatterWithMarkers", "ScatterWithSmoothLinesAndMarkers", "ScatterWithSmoothLines", "ScatterWithStraightLinesAndMarkers", "ScatterWithStraightLines", "HighLowClose", "OpenHighLowClose", "VolumeHighLowClose", "VolumeOpenHighLowClose", "Surface3D", "WireframeSurface3D", "Contour", "WireframeContour", "Doughnut", "ExplodedDoughnut", "Bubble", "BubbleWith3D", "Radar", "RadarWithMarkers", "FilledRadar", "SeriesOfMixedTypes", "Treemap", "Sunburst", "Histogram", "ParetoLine", "BoxAndWhisker", "Waterfall", "Funnel", "Map"]  # noqa: E501
            if chart_type.isdigit():
                int_chart_type = int(chart_type)
                if int_chart_type < 0 or int_chart_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `chart_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(chart_type, allowed_values)
                    )
                self._chart_type = allowed_values[int_chart_type]
                return
            if chart_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `chart_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(chart_type, allowed_values)
                )
        self._chart_type = chart_type

    @property
    def show_data_labels_over_maximum(self):
        """Gets the show_data_labels_over_maximum of this Chart.  # noqa: E501

        True if data labels over the maximum of the chart shall be shown.  # noqa: E501

        :return: The show_data_labels_over_maximum of this Chart.  # noqa: E501
        :rtype: bool
        """
        return self._show_data_labels_over_maximum

    @show_data_labels_over_maximum.setter
    def show_data_labels_over_maximum(self, show_data_labels_over_maximum):
        """Sets the show_data_labels_over_maximum of this Chart.

        True if data labels over the maximum of the chart shall be shown.  # noqa: E501

        :param show_data_labels_over_maximum: The show_data_labels_over_maximum of this Chart.  # noqa: E501
        :type: bool
        """
        self._show_data_labels_over_maximum = show_data_labels_over_maximum

    @property
    def series(self):
        """Gets the series of this Chart.  # noqa: E501

        Gets or sets the series of chart data values.  # noqa: E501

        :return: The series of this Chart.  # noqa: E501
        :rtype: list[Series]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this Chart.

        Gets or sets the series of chart data values.  # noqa: E501

        :param series: The series of this Chart.  # noqa: E501
        :type: list[Series]
        """
        self._series = series

    @property
    def categories(self):
        """Gets the categories of this Chart.  # noqa: E501

        Gets or sets the categories for chart data  # noqa: E501

        :return: The categories of this Chart.  # noqa: E501
        :rtype: list[ChartCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Chart.

        Gets or sets the categories for chart data  # noqa: E501

        :param categories: The categories of this Chart.  # noqa: E501
        :type: list[ChartCategory]
        """
        self._categories = categories

    @property
    def data_source_for_categories(self):
        """Gets the data_source_for_categories of this Chart.  # noqa: E501

        Data source type for categories.  # noqa: E501

        :return: The data_source_for_categories of this Chart.  # noqa: E501
        :rtype: DataSource
        """
        return self._data_source_for_categories

    @data_source_for_categories.setter
    def data_source_for_categories(self, data_source_for_categories):
        """Sets the data_source_for_categories of this Chart.

        Data source type for categories.  # noqa: E501

        :param data_source_for_categories: The data_source_for_categories of this Chart.  # noqa: E501
        :type: DataSource
        """
        self._data_source_for_categories = data_source_for_categories

    @property
    def title(self):
        """Gets the title of this Chart.  # noqa: E501

        Gets or sets the title.  # noqa: E501

        :return: The title of this Chart.  # noqa: E501
        :rtype: ChartTitle
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Chart.

        Gets or sets the title.  # noqa: E501

        :param title: The title of this Chart.  # noqa: E501
        :type: ChartTitle
        """
        self._title = title

    @property
    def back_wall(self):
        """Gets the back_wall of this Chart.  # noqa: E501

        Gets or sets the back wall.  # noqa: E501

        :return: The back_wall of this Chart.  # noqa: E501
        :rtype: ChartWall
        """
        return self._back_wall

    @back_wall.setter
    def back_wall(self, back_wall):
        """Sets the back_wall of this Chart.

        Gets or sets the back wall.  # noqa: E501

        :param back_wall: The back_wall of this Chart.  # noqa: E501
        :type: ChartWall
        """
        self._back_wall = back_wall

    @property
    def side_wall(self):
        """Gets the side_wall of this Chart.  # noqa: E501

        Gets or sets the side wall.  # noqa: E501

        :return: The side_wall of this Chart.  # noqa: E501
        :rtype: ChartWall
        """
        return self._side_wall

    @side_wall.setter
    def side_wall(self, side_wall):
        """Sets the side_wall of this Chart.

        Gets or sets the side wall.  # noqa: E501

        :param side_wall: The side_wall of this Chart.  # noqa: E501
        :type: ChartWall
        """
        self._side_wall = side_wall

    @property
    def floor(self):
        """Gets the floor of this Chart.  # noqa: E501

        Gets or sets the floor.  # noqa: E501

        :return: The floor of this Chart.  # noqa: E501
        :rtype: ChartWall
        """
        return self._floor

    @floor.setter
    def floor(self, floor):
        """Sets the floor of this Chart.

        Gets or sets the floor.  # noqa: E501

        :param floor: The floor of this Chart.  # noqa: E501
        :type: ChartWall
        """
        self._floor = floor

    @property
    def legend(self):
        """Gets the legend of this Chart.  # noqa: E501

        Gets or sets the legend.  # noqa: E501

        :return: The legend of this Chart.  # noqa: E501
        :rtype: Legend
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this Chart.

        Gets or sets the legend.  # noqa: E501

        :param legend: The legend of this Chart.  # noqa: E501
        :type: Legend
        """
        self._legend = legend

    @property
    def axes(self):
        """Gets the axes of this Chart.  # noqa: E501

        Gets or sets the axes.  # noqa: E501

        :return: The axes of this Chart.  # noqa: E501
        :rtype: Axes
        """
        return self._axes

    @axes.setter
    def axes(self, axes):
        """Sets the axes of this Chart.

        Gets or sets the axes.  # noqa: E501

        :param axes: The axes of this Chart.  # noqa: E501
        :type: Axes
        """
        self._axes = axes

    @property
    def plot_area(self):
        """Gets the plot_area of this Chart.  # noqa: E501

        Gets or sets the plot area.  # noqa: E501

        :return: The plot_area of this Chart.  # noqa: E501
        :rtype: PlotArea
        """
        return self._plot_area

    @plot_area.setter
    def plot_area(self, plot_area):
        """Sets the plot_area of this Chart.

        Gets or sets the plot area.  # noqa: E501

        :param plot_area: The plot_area of this Chart.  # noqa: E501
        :type: PlotArea
        """
        self._plot_area = plot_area

    @property
    def has_rounded_corners(self):
        """Gets the has_rounded_corners of this Chart.  # noqa: E501

        Specifies the chart area shall have rounded corners.  # noqa: E501

        :return: The has_rounded_corners of this Chart.  # noqa: E501
        :rtype: bool
        """
        return self._has_rounded_corners

    @has_rounded_corners.setter
    def has_rounded_corners(self, has_rounded_corners):
        """Sets the has_rounded_corners of this Chart.

        Specifies the chart area shall have rounded corners.  # noqa: E501

        :param has_rounded_corners: The has_rounded_corners of this Chart.  # noqa: E501
        :type: bool
        """
        self._has_rounded_corners = has_rounded_corners

    @property
    def series_groups(self):
        """Gets the series_groups of this Chart.  # noqa: E501

        Gets groups of series.   # noqa: E501

        :return: The series_groups of this Chart.  # noqa: E501
        :rtype: list[ChartSeriesGroup]
        """
        return self._series_groups

    @series_groups.setter
    def series_groups(self, series_groups):
        """Sets the series_groups of this Chart.

        Gets groups of series.   # noqa: E501

        :param series_groups: The series_groups of this Chart.  # noqa: E501
        :type: list[ChartSeriesGroup]
        """
        self._series_groups = series_groups

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
        if not isinstance(other, Chart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
