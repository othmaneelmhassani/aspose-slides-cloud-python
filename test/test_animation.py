from __future__ import absolute_import

from asposeslidescloud import SlideAnimation, Effect, InteractiveSequence
from test.base_test import BaseTest
import asposeslidescloud

class TestAnimation(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_animation_get(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        slide_index = 1
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        animation = BaseTest.slides_api.get_animation(file_name, slide_index, None, None, password, folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

        animation = BaseTest.slides_api.get_animation(file_name, slide_index, 3, None, password, folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

        animation = BaseTest.slides_api.get_animation(file_name, slide_index, 3, 1, password, folder_name)
        self.assertEqual(0, len(animation.main_sequence))

    def test_animation_set(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = SlideAnimation()

        effect1 = Effect()
        effect1.type = "Blink"
        effect1.shape_index = 2
        effect1.paragraph_index = 1

        effect2 = Effect()
        effect2.type = "Box"
        effect2.subtype = "In"
        effect2.preset_class_type = "Entrance"
        effect2.shape_index = 4
        dto.main_sequence = [ effect1, effect2 ]
        dto.interactive_sequences = []
        animation = BaseTest.slides_api.set_animation(file_name, 1, dto, "password", folder_name)
        self.assertEqual(len(dto.main_sequence), len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_animation_create_effect(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.create_animation_effect(file_name, 1, dto, "password", folder_name)
        self.assertEqual(2, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_animation_create_interactive_sequence(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = InteractiveSequence()
        dto.trigger_shape_index = 2
        effect = Effect()
        effect.type = "Blast"
        effect.shape_index = 3
        dto.effects = [ effect ]
        animation = BaseTest.slides_api.create_animation_interactive_sequence(file_name, 1, dto, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(2, len(animation.interactive_sequences))

    def test_animation_create_interactive_sequence_effect(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.create_animation_interactive_sequence_effect(file_name, 1, 1, dto, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_animation_update_effect(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.update_animation_effect(file_name, 1, 1, dto, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_animation_update_interactive_sequence_effect(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)

        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.update_animation_interactive_sequence_effect(file_name, 1, 1, 1, dto, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_animation_delete(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        animation = BaseTest.slides_api.delete_animation(file_name, 1, "password", folder_name)
        self.assertEqual(0, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_animation_delete_main_sequence(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        animation = BaseTest.slides_api.delete_animation_main_sequence(file_name, 1, "password", folder_name)
        self.assertEqual(0, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_animation_delete_main_sequence_effect(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        animation = BaseTest.slides_api.delete_animation_effect(file_name, 1, 1, "password", folder_name)
        self.assertEqual(0, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_animation_delete_interactive_sequences(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        animation = BaseTest.slides_api.delete_animation_interactive_sequences(file_name, 1, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_animation_delete_interactive_sequence(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        animation = BaseTest.slides_api.delete_animation_interactive_sequence(file_name, 1, 1, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_animation_delete_interactive_sequence_effect(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        animation = BaseTest.slides_api.delete_animation_interactive_sequence_effect(file_name, 1, 1, 1, "password", folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))