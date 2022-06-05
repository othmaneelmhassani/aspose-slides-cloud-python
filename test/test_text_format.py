from __future__ import absolute_import

from asposeslidescloud import Shape, TextFrameFormat, ThreeDFormat, ShapeBevel, LightRig, Camera
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestTextFormat(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_text_format_3d(self):
        dto = Shape()
        dto.shape_type = "Rectangle"
        dto.x = 100
        dto.y = 100
        dto.height = 100
        dto.width = 200
        dto.text = "Sample text"

        bevel_bottom = ShapeBevel()
        bevel_bottom.bevel_type = "Circle"
        bevel_bottom.height = 3.5
        bevel_bottom.width = 3.5

        bevel_top = ShapeBevel()
        bevel_top.bevel_type = "Circle"
        bevel_top.height = 4
        bevel_top.width = 4

        light_rig = LightRig()
        light_rig.light_type = "Balanced"
        light_rig.direction = "Top"
        light_rig.x_rotation = 0
        light_rig.y_rotation = 0
        light_rig.z_rotation = 40

        camera = Camera()
        camera.camera_type = "PerspectiveContrastingRightFacing"

        three_d_format = ThreeDFormat()
        three_d_format.bevel_top = bevel_top
        three_d_format.bevel_bottom = bevel_bottom
        three_d_format.extrusion_color = "#FF008000"
        three_d_format.extrusion_height = 6
        three_d_format.contour_color = "#FF25353D"
        three_d_format.contour_width = 1.5
        three_d_format.depth = 3
        three_d_format.material = "Plastic"
        three_d_format.light_rig = light_rig
        three_d_format.camera = camera

        text_frame_format = TextFrameFormat()
        text_frame_format.transform = "ArchUpPour"
        text_frame_format.three_d_format = three_d_format

        dto.text_frame_format = text_frame_format

        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 1
        shape = BaseTest.slides_api.create_shape(constant.FILE_NAME, slide_index, dto, None, None, constant.PASSWORD,
                                                 constant.FOLDER_NAME)
        self.assertTrue(isinstance(shape, Shape))