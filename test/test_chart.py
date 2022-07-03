
from __future__ import absolute_import

from asposeslidescloud import OneValueSeries, Chart, OneValueChartDataPoint, ChartCategory, Axis, ChartLinesFormat, \
    LineFormat, NoFill, SolidFill, GradientFill, GradientFillStop, Axes
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest
import asposeslidescloud


class TestChart(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_chart(self):
        chart = Chart()
        self.assertEqual("Chart", chart.type)

    def test_chart_get(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = BaseTest.slides_api.get_shape(file_name, 3, 1, "password", folder_name)
        self.assertEqual(3, len(chart.series))
        self.assertEqual(4, len(chart.categories))

    def test_chart_create(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300
        series1 = OneValueSeries()
        series1.name = "Series1"
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value = 70
        series1.data_points = [point11, point12, point13]
        series2 = OneValueSeries()
        series2.name = "Series2"
        point21 = OneValueChartDataPoint()
        point21.value = 55
        point22 = OneValueChartDataPoint()
        point22.value = 35
        point23 = OneValueChartDataPoint()
        point23.value = 90
        series2.data_points = [point21, point22, point23]
        chart.series = [series1, series2]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.create_shape(file_name, 3, chart, None, None, "password", folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(3, len(result.categories))

    def test_chart_update(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300
        series1 = OneValueSeries()
        series1.name = "Series1"
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value = 70
        series1.data_points = [point11, point12, point13]
        series2 = OneValueSeries()
        series2.name = "Series2"
        point21 = OneValueChartDataPoint()
        point21.value = 55
        point22 = OneValueChartDataPoint()
        point22.value = 35
        point23 = OneValueChartDataPoint()
        point23.value = 90
        series2.data_points = [point21, point22, point23]
        chart.series = [series1, series2]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.update_shape(file_name, 3, 1, chart, "password", folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(3, len(result.categories))

    def test_chart_series_create(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        series = OneValueSeries()
        series.name = "Series3"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        point4 = OneValueChartDataPoint()
        point4.value = 70
        series.data_points = [point1, point2, point3, point4]
        result = BaseTest.slides_api.create_chart_series(file_name, 3, 1, series, "password", folder_name)
        self.assertEqual(4, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_chart_series_update(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        series = OneValueSeries()
        series.name = "Series3"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        point4 = OneValueChartDataPoint()
        point4.value = 70
        series.data_points = [point1, point2, point3, point4]
        result = BaseTest.slides_api.update_chart_series(file_name, 3, 1, 2, series, "password", folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_chart_series_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_chart_series(file_name, 3, 1, 2, "password", folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_chart_category_create(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        category = ChartCategory()
        category.value = "NewCategory"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        category.data_points = [point1, point2, point3]
        result = BaseTest.slides_api.create_chart_category(file_name, 3, 1, category, "password", folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(5, len(result.categories))
        self.assertEqual(5, len(result.series[0].data_points))
        self.assertEqual(category.data_points[0].value, result.series[0].data_points[4].value)

    def test_chart_category_update(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        category = ChartCategory()
        category.value = "NewCategory"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        category.data_points = [point1, point2, point3]
        result = BaseTest.slides_api.update_chart_category(file_name, 3, 1, 2, category, "password", folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))
        self.assertEqual(4, len(result.series[0].data_points))
        self.assertEqual(category.data_points[0].value, result.series[0].data_points[1].value)

    def test_chart_category_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_chart_category(file_name, 3, 1, 2, "password", folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(3, len(result.categories))
        self.assertEqual(3, len(result.series[0].data_points))

    def test_chart_data_point_create(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        point = OneValueChartDataPoint()
        point.value = 40
        try:
            BaseTest.slides_api.create_chart_data_point(file_name, 3, 1, 2, point, "password", folder_name)
            self.fail("Must have failed because adding data points only works with Scatter & Bubble charts")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_chart_data_point_update(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        point = OneValueChartDataPoint()
        point.value = 40
        result = BaseTest.slides_api.update_chart_data_point(file_name, 3, 1, 2, 2, point, "password", folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))
        self.assertEqual(4, len(result.series[1].data_points))
        self.assertEqual(point.value, result.series[1].data_points[1].value)

    def test_chart_data_point_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        result = BaseTest.slides_api.delete_chart_data_point(file_name, 3, 1, 2, 2, "password", folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))
        self.assertIsNone(result.series[1].data_points[1])

    def test_chart_sunburst(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = Chart()
        chart.chart_type = 'Sunburst'
        chart.width = 400
        chart.height = 300
        series1 = OneValueSeries()
        series1.name = "Series1"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 70
        point4 = OneValueChartDataPoint()
        point4.value = 60
        series1.data_points = [point1, point2, point3, point4]
        chart.series = [series1]
        category1 = ChartCategory()
        category1.value = "Leaf1"
        category1.level = 3
        category1.parent_categories = ["Branch1", "Stem1"]
        category2 = ChartCategory()
        category2.value = "Leaf2"
        category2.level = 3
        category2.parent_categories = ["Branch1", "Stem1"]
        category3 = ChartCategory()
        category3.value = "Branch2"
        category3.level = 2
        category3.parent_categories = ["Stem1"]
        category4 = ChartCategory()
        category4.value = "Stem2"
        category4.level = 1
        chart.categories = [category1, category2, category3, category4]
        result = BaseTest.slides_api.create_shape(file_name, 3, chart, None, None, "password", folder_name)
        self.assertEqual(1, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_multilevel_category_axis(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = Chart()
        chart.chart_type = "ClusteredColumn"
        chart.x = 100
        chart.y = 100
        chart.width = 500
        chart.height = 400

        series = OneValueSeries()
        series.type = "ClusteredColumn"
        point1 = OneValueChartDataPoint()
        point1.value = 1
        point2 = OneValueChartDataPoint()
        point2.value = 2
        point3 = OneValueChartDataPoint()
        point3.value = 3
        point4 = OneValueChartDataPoint()
        point4.value = 4
        point5 = OneValueChartDataPoint()
        point5.value = 5
        point6 = OneValueChartDataPoint()
        point6.value = 6
        point7 = OneValueChartDataPoint()
        point7.value = 7
        point8 = OneValueChartDataPoint()
        point8.value = 8
        series.data_points = [point1, point2, point3, point4, point5, point6, point7, point8]

        category1 = ChartCategory()
        category1.value = "Category 1"
        category1.parent_categories = ["Sub-category 1", "Root 1"]
        category2 = ChartCategory()
        category2.value = "Category 2"
        category3 = ChartCategory()
        category3.parent_categories = ["Sub-category 2"]
        category4 = ChartCategory()
        category4.value = "Category 4"
        category5 = ChartCategory()
        category5.value = "Category 5"
        category5.parent_categories = ["Sub-category 3", "Root 2"]
        category6 = ChartCategory()
        category6.value = "Category 6"
        category7 = ChartCategory()
        category7.value = "Category 7"
        category7.parent_categories = ["Sub-category 4"]
        category8 = ChartCategory()
        category8.value = "Category 8"

        slide_index = 3
        chart.categories = [category1, category2, category3, category4, category5, category6, category7, category8]
        result = BaseTest.slides_api.create_shape(file_name, slide_index, chart, None, None, "password", folder_name)
        self.assertEqual("ClusteredColumn", result.chart_type)

    def test_hide_chart_legend(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        slide_index = 3
        shape_index = 1

        chart = BaseTest.slides_api.get_shape(file_name, slide_index, shape_index, "password", folder_name)
        chart.legend.has_legend = False
        chart = BaseTest.slides_api.update_shape(file_name, slide_index, shape_index, chart, "password", folder_name)
        self.assertEqual(False, chart.legend.has_legend)

    def test_chart_grid_lines_format(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        slide_index = 3
        shape_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = BaseTest.slides_api.get_shape(file_name, slide_index, shape_index, "password", folder_name)

        horizontal_axis = Axis()
        horizontal_axis.major_grid_lines_format = ChartLinesFormat()
        horizontal_axis.major_grid_lines_format.line_format = LineFormat()
        horizontal_axis.major_grid_lines_format.line_format.fill_format = NoFill()

        horizontal_axis.minor_grid_lines_format = ChartLinesFormat()
        horizontal_axis.minor_grid_lines_format.line_format = LineFormat()
        horizontal_axis.minor_grid_lines_format.line_format.fill_format = SolidFill()
        horizontal_axis.minor_grid_lines_format.line_format.fill_format.color = "Black"

        vertical_axis = Axis()
        vertical_axis.major_grid_lines_format = ChartLinesFormat()
        vertical_axis.major_grid_lines_format.line_format = LineFormat()
        gradient_fill = GradientFill()
        gradient_fill.direction = "FromCorner1"
        stop1 = GradientFillStop()
        stop1.color = "White"
        stop1.position = 0
        stop2 = GradientFillStop()
        stop2.color = "Black"
        stop2.position = 1
        gradient_fill.stops = [stop1, stop2]
        vertical_axis.major_grid_lines_format.line_format.fill_format = gradient_fill

        vertical_axis.minor_grid_lines_format = ChartLinesFormat()
        vertical_axis.minor_grid_lines_format.line_format = LineFormat()
        vertical_axis.minor_grid_lines_format.line_format.fill_format = NoFill()

        chart.axes = Axes()
        chart.axes.horizontal_axis = horizontal_axis
        chart.axes.vertical_axis = vertical_axis
        chart = BaseTest.slides_api.update_shape(file_name, slide_index, shape_index, chart, "password", folder_name)

        self.assertEqual("NoFill", chart.axes.horizontal_axis.major_grid_lines_format.line_format.fill_format.type)
        self.assertEqual("Solid", chart.axes.horizontal_axis.minor_grid_lines_format.line_format.fill_format.type)
        self.assertEqual("Gradient", chart.axes.vertical_axis.major_grid_lines_format.line_format.fill_format.type)
        self.assertEqual("NoFill", chart.axes.vertical_axis.minor_grid_lines_format.line_format.fill_format.type)

    def test_chart_series_groups(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        chart = BaseTest.slides_api.get_shape(file_name, 3, 1, "password", folder_name)
        self.assertEqual(1, len(chart.series_groups))
        chart.series_groups[0].overlap = 10
        chart = BaseTest.slides_api.update_chart_series_group(file_name, 3, 1, 1, chart.series_groups[0], "password",
                                                              folder_name)
        self.assertEqual(10, chart.series_groups[0].overlap)
