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

from asposeslidescloud.models.resource_base import ResourceBase

class Portion(ResourceBase):


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
        'text': 'str',
        'math_paragraph': 'MathParagraph',
        'font_bold': 'str',
        'font_italic': 'str',
        'font_underline': 'str',
        'strikethrough_type': 'str',
        'text_cap_type': 'str',
        'escapement': 'float',
        'spacing': 'float',
        'font_color': 'str',
        'highlight_color': 'str',
        'font_height': 'float',
        'normalise_height': 'str',
        'proof_disabled': 'str',
        'smart_tag_clean': 'bool',
        'kerning_minimal_size': 'float',
        'kumimoji': 'str',
        'language_id': 'str',
        'alternative_language_id': 'str',
        'is_hard_underline_fill': 'str',
        'is_hard_underline_line': 'str',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'line_format': 'LineFormat',
        'underline_fill_format': 'FillFormat',
        'underline_line_format': 'LineFormat',
        'hyperlink_click': 'Hyperlink',
        'hyperlink_mouse_over': 'Hyperlink',
        'latin_font': 'str',
        'east_asian_font': 'str',
        'complex_script_font': 'str'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'text': 'text',
        'math_paragraph': 'mathParagraph',
        'font_bold': 'fontBold',
        'font_italic': 'fontItalic',
        'font_underline': 'fontUnderline',
        'strikethrough_type': 'strikethroughType',
        'text_cap_type': 'textCapType',
        'escapement': 'escapement',
        'spacing': 'spacing',
        'font_color': 'fontColor',
        'highlight_color': 'highlightColor',
        'font_height': 'fontHeight',
        'normalise_height': 'normaliseHeight',
        'proof_disabled': 'proofDisabled',
        'smart_tag_clean': 'smartTagClean',
        'kerning_minimal_size': 'kerningMinimalSize',
        'kumimoji': 'kumimoji',
        'language_id': 'languageId',
        'alternative_language_id': 'alternativeLanguageId',
        'is_hard_underline_fill': 'isHardUnderlineFill',
        'is_hard_underline_line': 'isHardUnderlineLine',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'line_format': 'lineFormat',
        'underline_fill_format': 'underlineFillFormat',
        'underline_line_format': 'underlineLineFormat',
        'hyperlink_click': 'hyperlinkClick',
        'hyperlink_mouse_over': 'hyperlinkMouseOver',
        'latin_font': 'latinFont',
        'east_asian_font': 'eastAsianFont',
        'complex_script_font': 'complexScriptFont'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, text=None, math_paragraph=None, font_bold=None, font_italic=None, font_underline=None, strikethrough_type=None, text_cap_type=None, escapement=None, spacing=None, font_color=None, highlight_color=None, font_height=None, normalise_height=None, proof_disabled=None, smart_tag_clean=None, kerning_minimal_size=None, kumimoji=None, language_id=None, alternative_language_id=None, is_hard_underline_fill=None, is_hard_underline_line=None, fill_format=None, effect_format=None, line_format=None, underline_fill_format=None, underline_line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, latin_font=None, east_asian_font=None, complex_script_font=None):  # noqa: E501
        """Portion - a model defined in Swagger"""  # noqa: E501
        super(Portion, self).__init__(self_uri, alternate_links)

        self._text = None
        self._math_paragraph = None
        self._font_bold = None
        self._font_italic = None
        self._font_underline = None
        self._strikethrough_type = None
        self._text_cap_type = None
        self._escapement = None
        self._spacing = None
        self._font_color = None
        self._highlight_color = None
        self._font_height = None
        self._normalise_height = None
        self._proof_disabled = None
        self._smart_tag_clean = None
        self._kerning_minimal_size = None
        self._kumimoji = None
        self._language_id = None
        self._alternative_language_id = None
        self._is_hard_underline_fill = None
        self._is_hard_underline_line = None
        self._fill_format = None
        self._effect_format = None
        self._line_format = None
        self._underline_fill_format = None
        self._underline_line_format = None
        self._hyperlink_click = None
        self._hyperlink_mouse_over = None
        self._latin_font = None
        self._east_asian_font = None
        self._complex_script_font = None

        if text is not None:
            self.text = text
        if math_paragraph is not None:
            self.math_paragraph = math_paragraph
        if font_bold is not None:
            self.font_bold = font_bold
        if font_italic is not None:
            self.font_italic = font_italic
        if font_underline is not None:
            self.font_underline = font_underline
        if strikethrough_type is not None:
            self.strikethrough_type = strikethrough_type
        if text_cap_type is not None:
            self.text_cap_type = text_cap_type
        if escapement is not None:
            self.escapement = escapement
        if spacing is not None:
            self.spacing = spacing
        if font_color is not None:
            self.font_color = font_color
        if highlight_color is not None:
            self.highlight_color = highlight_color
        if font_height is not None:
            self.font_height = font_height
        if normalise_height is not None:
            self.normalise_height = normalise_height
        if proof_disabled is not None:
            self.proof_disabled = proof_disabled
        if smart_tag_clean is not None:
            self.smart_tag_clean = smart_tag_clean
        if kerning_minimal_size is not None:
            self.kerning_minimal_size = kerning_minimal_size
        if kumimoji is not None:
            self.kumimoji = kumimoji
        if language_id is not None:
            self.language_id = language_id
        if alternative_language_id is not None:
            self.alternative_language_id = alternative_language_id
        if is_hard_underline_fill is not None:
            self.is_hard_underline_fill = is_hard_underline_fill
        if is_hard_underline_line is not None:
            self.is_hard_underline_line = is_hard_underline_line
        if fill_format is not None:
            self.fill_format = fill_format
        if effect_format is not None:
            self.effect_format = effect_format
        if line_format is not None:
            self.line_format = line_format
        if underline_fill_format is not None:
            self.underline_fill_format = underline_fill_format
        if underline_line_format is not None:
            self.underline_line_format = underline_line_format
        if hyperlink_click is not None:
            self.hyperlink_click = hyperlink_click
        if hyperlink_mouse_over is not None:
            self.hyperlink_mouse_over = hyperlink_mouse_over
        if latin_font is not None:
            self.latin_font = latin_font
        if east_asian_font is not None:
            self.east_asian_font = east_asian_font
        if complex_script_font is not None:
            self.complex_script_font = complex_script_font

    @property
    def text(self):
        """Gets the text of this Portion.  # noqa: E501

        Text.  # noqa: E501

        :return: The text of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Portion.

        Text.  # noqa: E501

        :param text: The text of this Portion.  # noqa: E501
        :type: str
        """
        self._text = text

    @property
    def math_paragraph(self):
        """Gets the math_paragraph of this Portion.  # noqa: E501

        Math paragraph.  # noqa: E501

        :return: The math_paragraph of this Portion.  # noqa: E501
        :rtype: MathParagraph
        """
        return self._math_paragraph

    @math_paragraph.setter
    def math_paragraph(self, math_paragraph):
        """Sets the math_paragraph of this Portion.

        Math paragraph.  # noqa: E501

        :param math_paragraph: The math_paragraph of this Portion.  # noqa: E501
        :type: MathParagraph
        """
        self._math_paragraph = math_paragraph

    @property
    def font_bold(self):
        """Gets the font_bold of this Portion.  # noqa: E501

        True for bold font.  # noqa: E501

        :return: The font_bold of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._font_bold

    @font_bold.setter
    def font_bold(self, font_bold):
        """Sets the font_bold of this Portion.

        True for bold font.  # noqa: E501

        :param font_bold: The font_bold of this Portion.  # noqa: E501
        :type: str
        """
        if font_bold is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if font_bold.isdigit():
                int_font_bold = int(font_bold)
                if int_font_bold < 0 or int_font_bold >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `font_bold` ({0}), must be one of {1}"  # noqa: E501
                        .format(font_bold, allowed_values)
                    )
                self._font_bold = allowed_values[int_font_bold]
                return
            if font_bold not in allowed_values:
                raise ValueError(
                    "Invalid value for `font_bold` ({0}), must be one of {1}"  # noqa: E501
                    .format(font_bold, allowed_values)
                )
        self._font_bold = font_bold

    @property
    def font_italic(self):
        """Gets the font_italic of this Portion.  # noqa: E501

        True for italic font.  # noqa: E501

        :return: The font_italic of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._font_italic

    @font_italic.setter
    def font_italic(self, font_italic):
        """Sets the font_italic of this Portion.

        True for italic font.  # noqa: E501

        :param font_italic: The font_italic of this Portion.  # noqa: E501
        :type: str
        """
        if font_italic is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if font_italic.isdigit():
                int_font_italic = int(font_italic)
                if int_font_italic < 0 or int_font_italic >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `font_italic` ({0}), must be one of {1}"  # noqa: E501
                        .format(font_italic, allowed_values)
                    )
                self._font_italic = allowed_values[int_font_italic]
                return
            if font_italic not in allowed_values:
                raise ValueError(
                    "Invalid value for `font_italic` ({0}), must be one of {1}"  # noqa: E501
                    .format(font_italic, allowed_values)
                )
        self._font_italic = font_italic

    @property
    def font_underline(self):
        """Gets the font_underline of this Portion.  # noqa: E501

        Text underline type.  # noqa: E501

        :return: The font_underline of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._font_underline

    @font_underline.setter
    def font_underline(self, font_underline):
        """Sets the font_underline of this Portion.

        Text underline type.  # noqa: E501

        :param font_underline: The font_underline of this Portion.  # noqa: E501
        :type: str
        """
        if font_underline is not None:
            allowed_values = ["None", "Words", "Single", "Double", "Heavy", "Dotted", "HeavyDotted", "Dashed", "HeavyDashed", "LongDashed", "HeavyLongDashed", "DotDash", "HeavyDotDash", "DotDotDash", "HeavyDotDotDash", "Wavy", "HeavyWavy", "DoubleWavy", "NotDefined"]  # noqa: E501
            if font_underline.isdigit():
                int_font_underline = int(font_underline)
                if int_font_underline < 0 or int_font_underline >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `font_underline` ({0}), must be one of {1}"  # noqa: E501
                        .format(font_underline, allowed_values)
                    )
                self._font_underline = allowed_values[int_font_underline]
                return
            if font_underline not in allowed_values:
                raise ValueError(
                    "Invalid value for `font_underline` ({0}), must be one of {1}"  # noqa: E501
                    .format(font_underline, allowed_values)
                )
        self._font_underline = font_underline

    @property
    def strikethrough_type(self):
        """Gets the strikethrough_type of this Portion.  # noqa: E501

        Text strikethrough type.  # noqa: E501

        :return: The strikethrough_type of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._strikethrough_type

    @strikethrough_type.setter
    def strikethrough_type(self, strikethrough_type):
        """Sets the strikethrough_type of this Portion.

        Text strikethrough type.  # noqa: E501

        :param strikethrough_type: The strikethrough_type of this Portion.  # noqa: E501
        :type: str
        """
        if strikethrough_type is not None:
            allowed_values = ["None", "Single", "Double", "NotDefined"]  # noqa: E501
            if strikethrough_type.isdigit():
                int_strikethrough_type = int(strikethrough_type)
                if int_strikethrough_type < 0 or int_strikethrough_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `strikethrough_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(strikethrough_type, allowed_values)
                    )
                self._strikethrough_type = allowed_values[int_strikethrough_type]
                return
            if strikethrough_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `strikethrough_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(strikethrough_type, allowed_values)
                )
        self._strikethrough_type = strikethrough_type

    @property
    def text_cap_type(self):
        """Gets the text_cap_type of this Portion.  # noqa: E501

        Text capitalization type.  # noqa: E501

        :return: The text_cap_type of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._text_cap_type

    @text_cap_type.setter
    def text_cap_type(self, text_cap_type):
        """Sets the text_cap_type of this Portion.

        Text capitalization type.  # noqa: E501

        :param text_cap_type: The text_cap_type of this Portion.  # noqa: E501
        :type: str
        """
        if text_cap_type is not None:
            allowed_values = ["None", "Small", "All", "NotDefined"]  # noqa: E501
            if text_cap_type.isdigit():
                int_text_cap_type = int(text_cap_type)
                if int_text_cap_type < 0 or int_text_cap_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `text_cap_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(text_cap_type, allowed_values)
                    )
                self._text_cap_type = allowed_values[int_text_cap_type]
                return
            if text_cap_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `text_cap_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(text_cap_type, allowed_values)
                )
        self._text_cap_type = text_cap_type

    @property
    def escapement(self):
        """Gets the escapement of this Portion.  # noqa: E501

        Superscript or subscript of the text.  # noqa: E501

        :return: The escapement of this Portion.  # noqa: E501
        :rtype: float
        """
        return self._escapement

    @escapement.setter
    def escapement(self, escapement):
        """Sets the escapement of this Portion.

        Superscript or subscript of the text.  # noqa: E501

        :param escapement: The escapement of this Portion.  # noqa: E501
        :type: float
        """
        self._escapement = escapement

    @property
    def spacing(self):
        """Gets the spacing of this Portion.  # noqa: E501

        Intercharacter spacing increment.  # noqa: E501

        :return: The spacing of this Portion.  # noqa: E501
        :rtype: float
        """
        return self._spacing

    @spacing.setter
    def spacing(self, spacing):
        """Sets the spacing of this Portion.

        Intercharacter spacing increment.  # noqa: E501

        :param spacing: The spacing of this Portion.  # noqa: E501
        :type: float
        """
        self._spacing = spacing

    @property
    def font_color(self):
        """Gets the font_color of this Portion.  # noqa: E501

        Font color.  # noqa: E501

        :return: The font_color of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this Portion.

        Font color.  # noqa: E501

        :param font_color: The font_color of this Portion.  # noqa: E501
        :type: str
        """
        self._font_color = font_color

    @property
    def highlight_color(self):
        """Gets the highlight_color of this Portion.  # noqa: E501

        Highlight color.  # noqa: E501

        :return: The highlight_color of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._highlight_color

    @highlight_color.setter
    def highlight_color(self, highlight_color):
        """Sets the highlight_color of this Portion.

        Highlight color.  # noqa: E501

        :param highlight_color: The highlight_color of this Portion.  # noqa: E501
        :type: str
        """
        self._highlight_color = highlight_color

    @property
    def font_height(self):
        """Gets the font_height of this Portion.  # noqa: E501

        Font height.  # noqa: E501

        :return: The font_height of this Portion.  # noqa: E501
        :rtype: float
        """
        return self._font_height

    @font_height.setter
    def font_height(self, font_height):
        """Sets the font_height of this Portion.

        Font height.  # noqa: E501

        :param font_height: The font_height of this Portion.  # noqa: E501
        :type: float
        """
        self._font_height = font_height

    @property
    def normalise_height(self):
        """Gets the normalise_height of this Portion.  # noqa: E501

        True to normalize the text.  # noqa: E501

        :return: The normalise_height of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._normalise_height

    @normalise_height.setter
    def normalise_height(self, normalise_height):
        """Sets the normalise_height of this Portion.

        True to normalize the text.  # noqa: E501

        :param normalise_height: The normalise_height of this Portion.  # noqa: E501
        :type: str
        """
        if normalise_height is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if normalise_height.isdigit():
                int_normalise_height = int(normalise_height)
                if int_normalise_height < 0 or int_normalise_height >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `normalise_height` ({0}), must be one of {1}"  # noqa: E501
                        .format(normalise_height, allowed_values)
                    )
                self._normalise_height = allowed_values[int_normalise_height]
                return
            if normalise_height not in allowed_values:
                raise ValueError(
                    "Invalid value for `normalise_height` ({0}), must be one of {1}"  # noqa: E501
                    .format(normalise_height, allowed_values)
                )
        self._normalise_height = normalise_height

    @property
    def proof_disabled(self):
        """Gets the proof_disabled of this Portion.  # noqa: E501

        True if the text proof should be disabled.  # noqa: E501

        :return: The proof_disabled of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._proof_disabled

    @proof_disabled.setter
    def proof_disabled(self, proof_disabled):
        """Sets the proof_disabled of this Portion.

        True if the text proof should be disabled.  # noqa: E501

        :param proof_disabled: The proof_disabled of this Portion.  # noqa: E501
        :type: str
        """
        if proof_disabled is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if proof_disabled.isdigit():
                int_proof_disabled = int(proof_disabled)
                if int_proof_disabled < 0 or int_proof_disabled >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `proof_disabled` ({0}), must be one of {1}"  # noqa: E501
                        .format(proof_disabled, allowed_values)
                    )
                self._proof_disabled = allowed_values[int_proof_disabled]
                return
            if proof_disabled not in allowed_values:
                raise ValueError(
                    "Invalid value for `proof_disabled` ({0}), must be one of {1}"  # noqa: E501
                    .format(proof_disabled, allowed_values)
                )
        self._proof_disabled = proof_disabled

    @property
    def smart_tag_clean(self):
        """Gets the smart_tag_clean of this Portion.  # noqa: E501

        True if smart tag should be cleaned.  # noqa: E501

        :return: The smart_tag_clean of this Portion.  # noqa: E501
        :rtype: bool
        """
        return self._smart_tag_clean

    @smart_tag_clean.setter
    def smart_tag_clean(self, smart_tag_clean):
        """Sets the smart_tag_clean of this Portion.

        True if smart tag should be cleaned.  # noqa: E501

        :param smart_tag_clean: The smart_tag_clean of this Portion.  # noqa: E501
        :type: bool
        """
        self._smart_tag_clean = smart_tag_clean

    @property
    def kerning_minimal_size(self):
        """Gets the kerning_minimal_size of this Portion.  # noqa: E501

        Minimal font size for kerning.  # noqa: E501

        :return: The kerning_minimal_size of this Portion.  # noqa: E501
        :rtype: float
        """
        return self._kerning_minimal_size

    @kerning_minimal_size.setter
    def kerning_minimal_size(self, kerning_minimal_size):
        """Sets the kerning_minimal_size of this Portion.

        Minimal font size for kerning.  # noqa: E501

        :param kerning_minimal_size: The kerning_minimal_size of this Portion.  # noqa: E501
        :type: float
        """
        self._kerning_minimal_size = kerning_minimal_size

    @property
    def kumimoji(self):
        """Gets the kumimoji of this Portion.  # noqa: E501

        True if numbers should ignore East-Asian specific vertical text layout.  # noqa: E501

        :return: The kumimoji of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._kumimoji

    @kumimoji.setter
    def kumimoji(self, kumimoji):
        """Sets the kumimoji of this Portion.

        True if numbers should ignore East-Asian specific vertical text layout.  # noqa: E501

        :param kumimoji: The kumimoji of this Portion.  # noqa: E501
        :type: str
        """
        if kumimoji is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if kumimoji.isdigit():
                int_kumimoji = int(kumimoji)
                if int_kumimoji < 0 or int_kumimoji >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `kumimoji` ({0}), must be one of {1}"  # noqa: E501
                        .format(kumimoji, allowed_values)
                    )
                self._kumimoji = allowed_values[int_kumimoji]
                return
            if kumimoji not in allowed_values:
                raise ValueError(
                    "Invalid value for `kumimoji` ({0}), must be one of {1}"  # noqa: E501
                    .format(kumimoji, allowed_values)
                )
        self._kumimoji = kumimoji

    @property
    def language_id(self):
        """Gets the language_id of this Portion.  # noqa: E501

        Proving language ID.  # noqa: E501

        :return: The language_id of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """Sets the language_id of this Portion.

        Proving language ID.  # noqa: E501

        :param language_id: The language_id of this Portion.  # noqa: E501
        :type: str
        """
        self._language_id = language_id

    @property
    def alternative_language_id(self):
        """Gets the alternative_language_id of this Portion.  # noqa: E501

        Alternative proving language ID.  # noqa: E501

        :return: The alternative_language_id of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._alternative_language_id

    @alternative_language_id.setter
    def alternative_language_id(self, alternative_language_id):
        """Sets the alternative_language_id of this Portion.

        Alternative proving language ID.  # noqa: E501

        :param alternative_language_id: The alternative_language_id of this Portion.  # noqa: E501
        :type: str
        """
        self._alternative_language_id = alternative_language_id

    @property
    def is_hard_underline_fill(self):
        """Gets the is_hard_underline_fill of this Portion.  # noqa: E501

        True if underline style has own FillFormat properties.  # noqa: E501

        :return: The is_hard_underline_fill of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._is_hard_underline_fill

    @is_hard_underline_fill.setter
    def is_hard_underline_fill(self, is_hard_underline_fill):
        """Sets the is_hard_underline_fill of this Portion.

        True if underline style has own FillFormat properties.  # noqa: E501

        :param is_hard_underline_fill: The is_hard_underline_fill of this Portion.  # noqa: E501
        :type: str
        """
        if is_hard_underline_fill is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if is_hard_underline_fill.isdigit():
                int_is_hard_underline_fill = int(is_hard_underline_fill)
                if int_is_hard_underline_fill < 0 or int_is_hard_underline_fill >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `is_hard_underline_fill` ({0}), must be one of {1}"  # noqa: E501
                        .format(is_hard_underline_fill, allowed_values)
                    )
                self._is_hard_underline_fill = allowed_values[int_is_hard_underline_fill]
                return
            if is_hard_underline_fill not in allowed_values:
                raise ValueError(
                    "Invalid value for `is_hard_underline_fill` ({0}), must be one of {1}"  # noqa: E501
                    .format(is_hard_underline_fill, allowed_values)
                )
        self._is_hard_underline_fill = is_hard_underline_fill

    @property
    def is_hard_underline_line(self):
        """Gets the is_hard_underline_line of this Portion.  # noqa: E501

        True if underline style has own LineFormat properties.  # noqa: E501

        :return: The is_hard_underline_line of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._is_hard_underline_line

    @is_hard_underline_line.setter
    def is_hard_underline_line(self, is_hard_underline_line):
        """Sets the is_hard_underline_line of this Portion.

        True if underline style has own LineFormat properties.  # noqa: E501

        :param is_hard_underline_line: The is_hard_underline_line of this Portion.  # noqa: E501
        :type: str
        """
        if is_hard_underline_line is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if is_hard_underline_line.isdigit():
                int_is_hard_underline_line = int(is_hard_underline_line)
                if int_is_hard_underline_line < 0 or int_is_hard_underline_line >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `is_hard_underline_line` ({0}), must be one of {1}"  # noqa: E501
                        .format(is_hard_underline_line, allowed_values)
                    )
                self._is_hard_underline_line = allowed_values[int_is_hard_underline_line]
                return
            if is_hard_underline_line not in allowed_values:
                raise ValueError(
                    "Invalid value for `is_hard_underline_line` ({0}), must be one of {1}"  # noqa: E501
                    .format(is_hard_underline_line, allowed_values)
                )
        self._is_hard_underline_line = is_hard_underline_line

    @property
    def fill_format(self):
        """Gets the fill_format of this Portion.  # noqa: E501

        Fill format.  # noqa: E501

        :return: The fill_format of this Portion.  # noqa: E501
        :rtype: FillFormat
        """
        return self._fill_format

    @fill_format.setter
    def fill_format(self, fill_format):
        """Sets the fill_format of this Portion.

        Fill format.  # noqa: E501

        :param fill_format: The fill_format of this Portion.  # noqa: E501
        :type: FillFormat
        """
        self._fill_format = fill_format

    @property
    def effect_format(self):
        """Gets the effect_format of this Portion.  # noqa: E501

        Effect format.  # noqa: E501

        :return: The effect_format of this Portion.  # noqa: E501
        :rtype: EffectFormat
        """
        return self._effect_format

    @effect_format.setter
    def effect_format(self, effect_format):
        """Sets the effect_format of this Portion.

        Effect format.  # noqa: E501

        :param effect_format: The effect_format of this Portion.  # noqa: E501
        :type: EffectFormat
        """
        self._effect_format = effect_format

    @property
    def line_format(self):
        """Gets the line_format of this Portion.  # noqa: E501

        Line format.  # noqa: E501

        :return: The line_format of this Portion.  # noqa: E501
        :rtype: LineFormat
        """
        return self._line_format

    @line_format.setter
    def line_format(self, line_format):
        """Sets the line_format of this Portion.

        Line format.  # noqa: E501

        :param line_format: The line_format of this Portion.  # noqa: E501
        :type: LineFormat
        """
        self._line_format = line_format

    @property
    def underline_fill_format(self):
        """Gets the underline_fill_format of this Portion.  # noqa: E501

        Underline fill format.  # noqa: E501

        :return: The underline_fill_format of this Portion.  # noqa: E501
        :rtype: FillFormat
        """
        return self._underline_fill_format

    @underline_fill_format.setter
    def underline_fill_format(self, underline_fill_format):
        """Sets the underline_fill_format of this Portion.

        Underline fill format.  # noqa: E501

        :param underline_fill_format: The underline_fill_format of this Portion.  # noqa: E501
        :type: FillFormat
        """
        self._underline_fill_format = underline_fill_format

    @property
    def underline_line_format(self):
        """Gets the underline_line_format of this Portion.  # noqa: E501

        Underline line format.  # noqa: E501

        :return: The underline_line_format of this Portion.  # noqa: E501
        :rtype: LineFormat
        """
        return self._underline_line_format

    @underline_line_format.setter
    def underline_line_format(self, underline_line_format):
        """Sets the underline_line_format of this Portion.

        Underline line format.  # noqa: E501

        :param underline_line_format: The underline_line_format of this Portion.  # noqa: E501
        :type: LineFormat
        """
        self._underline_line_format = underline_line_format

    @property
    def hyperlink_click(self):
        """Gets the hyperlink_click of this Portion.  # noqa: E501

        Hyperlink defined for mouse click.  # noqa: E501

        :return: The hyperlink_click of this Portion.  # noqa: E501
        :rtype: Hyperlink
        """
        return self._hyperlink_click

    @hyperlink_click.setter
    def hyperlink_click(self, hyperlink_click):
        """Sets the hyperlink_click of this Portion.

        Hyperlink defined for mouse click.  # noqa: E501

        :param hyperlink_click: The hyperlink_click of this Portion.  # noqa: E501
        :type: Hyperlink
        """
        self._hyperlink_click = hyperlink_click

    @property
    def hyperlink_mouse_over(self):
        """Gets the hyperlink_mouse_over of this Portion.  # noqa: E501

        Hyperlink defined for mouse over.  # noqa: E501

        :return: The hyperlink_mouse_over of this Portion.  # noqa: E501
        :rtype: Hyperlink
        """
        return self._hyperlink_mouse_over

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, hyperlink_mouse_over):
        """Sets the hyperlink_mouse_over of this Portion.

        Hyperlink defined for mouse over.  # noqa: E501

        :param hyperlink_mouse_over: The hyperlink_mouse_over of this Portion.  # noqa: E501
        :type: Hyperlink
        """
        self._hyperlink_mouse_over = hyperlink_mouse_over

    @property
    def latin_font(self):
        """Gets the latin_font of this Portion.  # noqa: E501

        Returns or sets the Latin font info.  # noqa: E501

        :return: The latin_font of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._latin_font

    @latin_font.setter
    def latin_font(self, latin_font):
        """Sets the latin_font of this Portion.

        Returns or sets the Latin font info.  # noqa: E501

        :param latin_font: The latin_font of this Portion.  # noqa: E501
        :type: str
        """
        self._latin_font = latin_font

    @property
    def east_asian_font(self):
        """Gets the east_asian_font of this Portion.  # noqa: E501

        Returns or sets the East Asian font info.  # noqa: E501

        :return: The east_asian_font of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._east_asian_font

    @east_asian_font.setter
    def east_asian_font(self, east_asian_font):
        """Sets the east_asian_font of this Portion.

        Returns or sets the East Asian font info.  # noqa: E501

        :param east_asian_font: The east_asian_font of this Portion.  # noqa: E501
        :type: str
        """
        self._east_asian_font = east_asian_font

    @property
    def complex_script_font(self):
        """Gets the complex_script_font of this Portion.  # noqa: E501

        Returns or sets the complex script font info.  # noqa: E501

        :return: The complex_script_font of this Portion.  # noqa: E501
        :rtype: str
        """
        return self._complex_script_font

    @complex_script_font.setter
    def complex_script_font(self, complex_script_font):
        """Sets the complex_script_font of this Portion.

        Returns or sets the complex script font info.  # noqa: E501

        :param complex_script_font: The complex_script_font of this Portion.  # noqa: E501
        :type: str
        """
        self._complex_script_font = complex_script_font

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
        if not isinstance(other, Portion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
