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


class ChartSeriesGroup(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'gap_width': 'int',
        'gap_depth': 'int',
        'first_slice_angle': 'int',
        'is_color_varied': 'bool',
        'has_series_lines': 'bool',
        'overlap': 'int',
        'second_pie_size': 'int',
        'pie_split_position': 'float',
        'pie_split_by': 'str',
        'doughnut_hole_size': 'int',
        'bubble_size_scale': 'int',
        'hi_low_lines_format': 'ChartLinesFormat',
        'bubble_size_representation': 'str'
    }

    attribute_map = {
        'type': 'type',
        'gap_width': 'gapWidth',
        'gap_depth': 'gapDepth',
        'first_slice_angle': 'firstSliceAngle',
        'is_color_varied': 'isColorVaried',
        'has_series_lines': 'hasSeriesLines',
        'overlap': 'overlap',
        'second_pie_size': 'secondPieSize',
        'pie_split_position': 'pieSplitPosition',
        'pie_split_by': 'pieSplitBy',
        'doughnut_hole_size': 'doughnutHoleSize',
        'bubble_size_scale': 'bubbleSizeScale',
        'hi_low_lines_format': 'hiLowLinesFormat',
        'bubble_size_representation': 'bubbleSizeRepresentation'
    }

    type_determiners = {
    }

    def __init__(self, type=None, gap_width=None, gap_depth=None, first_slice_angle=None, is_color_varied=None, has_series_lines=None, overlap=None, second_pie_size=None, pie_split_position=None, pie_split_by=None, doughnut_hole_size=None, bubble_size_scale=None, hi_low_lines_format=None, bubble_size_representation=None):  # noqa: E501
        """ChartSeriesGroup - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._gap_width = None
        self._gap_depth = None
        self._first_slice_angle = None
        self._is_color_varied = None
        self._has_series_lines = None
        self._overlap = None
        self._second_pie_size = None
        self._pie_split_position = None
        self._pie_split_by = None
        self._doughnut_hole_size = None
        self._bubble_size_scale = None
        self._hi_low_lines_format = None
        self._bubble_size_representation = None

        if type is not None:
            self.type = type
        if gap_width is not None:
            self.gap_width = gap_width
        if gap_depth is not None:
            self.gap_depth = gap_depth
        if first_slice_angle is not None:
            self.first_slice_angle = first_slice_angle
        if is_color_varied is not None:
            self.is_color_varied = is_color_varied
        if has_series_lines is not None:
            self.has_series_lines = has_series_lines
        if overlap is not None:
            self.overlap = overlap
        if second_pie_size is not None:
            self.second_pie_size = second_pie_size
        if pie_split_position is not None:
            self.pie_split_position = pie_split_position
        if pie_split_by is not None:
            self.pie_split_by = pie_split_by
        if doughnut_hole_size is not None:
            self.doughnut_hole_size = doughnut_hole_size
        if bubble_size_scale is not None:
            self.bubble_size_scale = bubble_size_scale
        if hi_low_lines_format is not None:
            self.hi_low_lines_format = hi_low_lines_format
        if bubble_size_representation is not None:
            self.bubble_size_representation = bubble_size_representation

    @property
    def type(self):
        """Gets the type of this ChartSeriesGroup.  # noqa: E501

        Returns a type of this series group.  # noqa: E501

        :return: The type of this ChartSeriesGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChartSeriesGroup.

        Returns a type of this series group.  # noqa: E501

        :param type: The type of this ChartSeriesGroup.  # noqa: E501
        :type: str
        """
        if type is not None:
            allowed_values = ["BarOfPieChart", "PieOfPieChart", "DoughnutChart", "PieChart", "AreaChartArea", "AreaChartPercentsStackedArea", "AreaChartStackedArea", "BarChartHorizClustered", "BarChartHorizStacked", "BarChartHorizPercentsStacked", "BarChartVertClustered", "BarChartVertStacked", "BarChartVertPercentsStacked", "LineChartLine", "LineChartStackedLine", "LineChartPercentsStackedLine", "RadarChart", "FilledRadarChart", "StockHighLowClose", "StockOpenHighLowClose", "StockVolumeHighLowClose", "StockVolumeOpenHighLowClose", "ScatterStraightMarker", "ScatterSmoothMarker", "AreaChartArea3D", "AreaChartStackedArea3D", "AreaChartPercentsStackedArea3D", "Line3DChart", "Pie3DChart", "Bar3DChartVert", "Bar3DChartVertClustered", "Bar3DChartVertPercentsStackedColumn3D", "Bar3DChartVertPercentsStackedCone", "Bar3DChartVertPercentsStackedCylinder", "Bar3DChartVertPercentsStackedPyramid", "Bar3DChartVertStackedColumn3D", "Bar3DChartVertStackedCone", "Bar3DChartVertStackedCylinder", "Bar3DChartVertStackedPyramid", "Bar3DChartHorizClustered", "Bar3DChartHorizStackedBar3D", "Bar3DChartHorizStackedCone", "Bar3DChartHorizStackedCylinder", "Bar3DChartHorizStackedPyramid", "Bar3DChartHorizPercentsStackedBar3D", "Bar3DChartHorizPercentsStackedCone", "Bar3DChartHorizPercentsStackedCylinder", "Bar3DChartHorizPercentsStackedPyramid", "SurfaceChartContour", "SurfaceChartWireframeContour", "SurfaceChartSurface3D", "SurfaceChartWireframeSurface3D", "BubbleChart", "HistogramChart", "ParetoLineChart", "BoxAndWhiskerChart", "WaterfallChart", "FunnelChart", "TreemapChart", "MapChart", "SunburstChart"]  # noqa: E501
            if type.isdigit():
                int_type = int(type)
                if int_type < 0 or int_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                        .format(type, allowed_values)
                    )
                self._type = allowed_values[int_type]
                return
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values)
                )
        self._type = type

    @property
    def gap_width(self):
        """Gets the gap_width of this ChartSeriesGroup.  # noqa: E501

        Specifies the space between bar or column clusters, as a percentage of the bar or column width.  # noqa: E501

        :return: The gap_width of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._gap_width

    @gap_width.setter
    def gap_width(self, gap_width):
        """Sets the gap_width of this ChartSeriesGroup.

        Specifies the space between bar or column clusters, as a percentage of the bar or column width.  # noqa: E501

        :param gap_width: The gap_width of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._gap_width = gap_width

    @property
    def gap_depth(self):
        """Gets the gap_depth of this ChartSeriesGroup.  # noqa: E501

        Returns or sets the distance, as a percentage of the marker width, between the data series in a 3D chart.  # noqa: E501

        :return: The gap_depth of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._gap_depth

    @gap_depth.setter
    def gap_depth(self, gap_depth):
        """Sets the gap_depth of this ChartSeriesGroup.

        Returns or sets the distance, as a percentage of the marker width, between the data series in a 3D chart.  # noqa: E501

        :param gap_depth: The gap_depth of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._gap_depth = gap_depth

    @property
    def first_slice_angle(self):
        """Gets the first_slice_angle of this ChartSeriesGroup.  # noqa: E501

        Gets or sets the angle of the first pie or doughnut chart slice,  in degrees (clockwise from up, from 0 to 360 degrees).  # noqa: E501

        :return: The first_slice_angle of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._first_slice_angle

    @first_slice_angle.setter
    def first_slice_angle(self, first_slice_angle):
        """Sets the first_slice_angle of this ChartSeriesGroup.

        Gets or sets the angle of the first pie or doughnut chart slice,  in degrees (clockwise from up, from 0 to 360 degrees).  # noqa: E501

        :param first_slice_angle: The first_slice_angle of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._first_slice_angle = first_slice_angle

    @property
    def is_color_varied(self):
        """Gets the is_color_varied of this ChartSeriesGroup.  # noqa: E501

        Specifies that each data marker in the series has a different color.  # noqa: E501

        :return: The is_color_varied of this ChartSeriesGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_color_varied

    @is_color_varied.setter
    def is_color_varied(self, is_color_varied):
        """Sets the is_color_varied of this ChartSeriesGroup.

        Specifies that each data marker in the series has a different color.  # noqa: E501

        :param is_color_varied: The is_color_varied of this ChartSeriesGroup.  # noqa: E501
        :type: bool
        """
        self._is_color_varied = is_color_varied

    @property
    def has_series_lines(self):
        """Gets the has_series_lines of this ChartSeriesGroup.  # noqa: E501

        True if chart has series lines. Applied to stacked bar and OfPie charts.  # noqa: E501

        :return: The has_series_lines of this ChartSeriesGroup.  # noqa: E501
        :rtype: bool
        """
        return self._has_series_lines

    @has_series_lines.setter
    def has_series_lines(self, has_series_lines):
        """Sets the has_series_lines of this ChartSeriesGroup.

        True if chart has series lines. Applied to stacked bar and OfPie charts.  # noqa: E501

        :param has_series_lines: The has_series_lines of this ChartSeriesGroup.  # noqa: E501
        :type: bool
        """
        self._has_series_lines = has_series_lines

    @property
    def overlap(self):
        """Gets the overlap of this ChartSeriesGroup.  # noqa: E501

        Specifies how much bars and columns shall overlap on 2-D charts (from -100 to 100).  # noqa: E501

        :return: The overlap of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._overlap

    @overlap.setter
    def overlap(self, overlap):
        """Sets the overlap of this ChartSeriesGroup.

        Specifies how much bars and columns shall overlap on 2-D charts (from -100 to 100).  # noqa: E501

        :param overlap: The overlap of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._overlap = overlap

    @property
    def second_pie_size(self):
        """Gets the second_pie_size of this ChartSeriesGroup.  # noqa: E501

        Specifies the size of the second pie or bar of a pie-of-pie chart or  a bar-of-pie chart, as a percentage of the size of the first pie (can  be between 5 and 200 percents).  # noqa: E501

        :return: The second_pie_size of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._second_pie_size

    @second_pie_size.setter
    def second_pie_size(self, second_pie_size):
        """Sets the second_pie_size of this ChartSeriesGroup.

        Specifies the size of the second pie or bar of a pie-of-pie chart or  a bar-of-pie chart, as a percentage of the size of the first pie (can  be between 5 and 200 percents).  # noqa: E501

        :param second_pie_size: The second_pie_size of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._second_pie_size = second_pie_size

    @property
    def pie_split_position(self):
        """Gets the pie_split_position of this ChartSeriesGroup.  # noqa: E501

        Specifies a value that shall be used to determine which data points  are in the second pie or bar on a pie-of-pie or bar-of-pie chart.  Is used together with PieSplitBy property.  # noqa: E501

        :return: The pie_split_position of this ChartSeriesGroup.  # noqa: E501
        :rtype: float
        """
        return self._pie_split_position

    @pie_split_position.setter
    def pie_split_position(self, pie_split_position):
        """Sets the pie_split_position of this ChartSeriesGroup.

        Specifies a value that shall be used to determine which data points  are in the second pie or bar on a pie-of-pie or bar-of-pie chart.  Is used together with PieSplitBy property.  # noqa: E501

        :param pie_split_position: The pie_split_position of this ChartSeriesGroup.  # noqa: E501
        :type: float
        """
        self._pie_split_position = pie_split_position

    @property
    def pie_split_by(self):
        """Gets the pie_split_by of this ChartSeriesGroup.  # noqa: E501

        Specifies how to determine which data points are in the second pie or bar  on a pie-of-pie or bar-of-pie chart.  # noqa: E501

        :return: The pie_split_by of this ChartSeriesGroup.  # noqa: E501
        :rtype: str
        """
        return self._pie_split_by

    @pie_split_by.setter
    def pie_split_by(self, pie_split_by):
        """Sets the pie_split_by of this ChartSeriesGroup.

        Specifies how to determine which data points are in the second pie or bar  on a pie-of-pie or bar-of-pie chart.  # noqa: E501

        :param pie_split_by: The pie_split_by of this ChartSeriesGroup.  # noqa: E501
        :type: str
        """
        if pie_split_by is not None:
            allowed_values = ["Default", "Custom", "ByPercentage", "ByPos", "ByValue"]  # noqa: E501
            if pie_split_by.isdigit():
                int_pie_split_by = int(pie_split_by)
                if int_pie_split_by < 0 or int_pie_split_by >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `pie_split_by` ({0}), must be one of {1}"  # noqa: E501
                        .format(pie_split_by, allowed_values)
                    )
                self._pie_split_by = allowed_values[int_pie_split_by]
                return
            if pie_split_by not in allowed_values:
                raise ValueError(
                    "Invalid value for `pie_split_by` ({0}), must be one of {1}"  # noqa: E501
                    .format(pie_split_by, allowed_values)
                )
        self._pie_split_by = pie_split_by

    @property
    def doughnut_hole_size(self):
        """Gets the doughnut_hole_size of this ChartSeriesGroup.  # noqa: E501

        Specifies the size of the hole in a doughnut chart (can be between 10 and 90 percents  of the size of the plot area.).  # noqa: E501

        :return: The doughnut_hole_size of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._doughnut_hole_size

    @doughnut_hole_size.setter
    def doughnut_hole_size(self, doughnut_hole_size):
        """Sets the doughnut_hole_size of this ChartSeriesGroup.

        Specifies the size of the hole in a doughnut chart (can be between 10 and 90 percents  of the size of the plot area.).  # noqa: E501

        :param doughnut_hole_size: The doughnut_hole_size of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._doughnut_hole_size = doughnut_hole_size

    @property
    def bubble_size_scale(self):
        """Gets the bubble_size_scale of this ChartSeriesGroup.  # noqa: E501

        Specifies the scale factor for the bubble chart (can be  between 0 and 300 percents of the default size). Read/write Int32.  # noqa: E501

        :return: The bubble_size_scale of this ChartSeriesGroup.  # noqa: E501
        :rtype: int
        """
        return self._bubble_size_scale

    @bubble_size_scale.setter
    def bubble_size_scale(self, bubble_size_scale):
        """Sets the bubble_size_scale of this ChartSeriesGroup.

        Specifies the scale factor for the bubble chart (can be  between 0 and 300 percents of the default size). Read/write Int32.  # noqa: E501

        :param bubble_size_scale: The bubble_size_scale of this ChartSeriesGroup.  # noqa: E501
        :type: int
        """
        self._bubble_size_scale = bubble_size_scale

    @property
    def hi_low_lines_format(self):
        """Gets the hi_low_lines_format of this ChartSeriesGroup.  # noqa: E501

        Specifies HiLowLines format.  HiLowLines applied with HiLowClose, OpenHiLowClose, VolumeHiLowClose and VolumeOpenHiLowClose chart types.  # noqa: E501

        :return: The hi_low_lines_format of this ChartSeriesGroup.  # noqa: E501
        :rtype: ChartLinesFormat
        """
        return self._hi_low_lines_format

    @hi_low_lines_format.setter
    def hi_low_lines_format(self, hi_low_lines_format):
        """Sets the hi_low_lines_format of this ChartSeriesGroup.

        Specifies HiLowLines format.  HiLowLines applied with HiLowClose, OpenHiLowClose, VolumeHiLowClose and VolumeOpenHiLowClose chart types.  # noqa: E501

        :param hi_low_lines_format: The hi_low_lines_format of this ChartSeriesGroup.  # noqa: E501
        :type: ChartLinesFormat
        """
        self._hi_low_lines_format = hi_low_lines_format

    @property
    def bubble_size_representation(self):
        """Gets the bubble_size_representation of this ChartSeriesGroup.  # noqa: E501

        Specifies how the bubble size values are represented on the bubble chart. Read/write BubbleSizeRepresentationType.  # noqa: E501

        :return: The bubble_size_representation of this ChartSeriesGroup.  # noqa: E501
        :rtype: str
        """
        return self._bubble_size_representation

    @bubble_size_representation.setter
    def bubble_size_representation(self, bubble_size_representation):
        """Sets the bubble_size_representation of this ChartSeriesGroup.

        Specifies how the bubble size values are represented on the bubble chart. Read/write BubbleSizeRepresentationType.  # noqa: E501

        :param bubble_size_representation: The bubble_size_representation of this ChartSeriesGroup.  # noqa: E501
        :type: str
        """
        if bubble_size_representation is not None:
            allowed_values = ["Area", "Width"]  # noqa: E501
            if bubble_size_representation.isdigit():
                int_bubble_size_representation = int(bubble_size_representation)
                if int_bubble_size_representation < 0 or int_bubble_size_representation >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `bubble_size_representation` ({0}), must be one of {1}"  # noqa: E501
                        .format(bubble_size_representation, allowed_values)
                    )
                self._bubble_size_representation = allowed_values[int_bubble_size_representation]
                return
            if bubble_size_representation not in allowed_values:
                raise ValueError(
                    "Invalid value for `bubble_size_representation` ({0}), must be one of {1}"  # noqa: E501
                    .format(bubble_size_representation, allowed_values)
                )
        self._bubble_size_representation = bubble_size_representation

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
        if not isinstance(other, ChartSeriesGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
