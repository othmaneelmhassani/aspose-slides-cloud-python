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

from asposeslidescloud.models.image_export_options_base import ImageExportOptionsBase

class GifExportOptions(ImageExportOptionsBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_regular_font': 'str',
        'font_fallback_rules': 'list[FontFallbackRule]',
        'font_subst_rules': 'list[FontSubstRule]',
        'format': 'str',
        'height': 'int',
        'width': 'int',
        'export_hidden_slides': 'bool',
        'transition_fps': 'int',
        'default_delay': 'int'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'height': 'height',
        'width': 'width',
        'export_hidden_slides': 'exportHiddenSlides',
        'transition_fps': 'transitionFps',
        'default_delay': 'defaultDelay'
    }

    type_determiners = {
        'format': 'gif',
    }

    def __init__(self, default_regular_font=None, font_fallback_rules=None, font_subst_rules=None, format='gif', height=None, width=None, export_hidden_slides=None, transition_fps=None, default_delay=None):  # noqa: E501
        """GifExportOptions - a model defined in Swagger"""  # noqa: E501
        super(GifExportOptions, self).__init__(default_regular_font, font_fallback_rules, font_subst_rules, format, height, width)

        self._export_hidden_slides = None
        self._transition_fps = None
        self._default_delay = None
        self.format = 'gif'

        if export_hidden_slides is not None:
            self.export_hidden_slides = export_hidden_slides
        if transition_fps is not None:
            self.transition_fps = transition_fps
        if default_delay is not None:
            self.default_delay = default_delay

    @property
    def export_hidden_slides(self):
        """Gets the export_hidden_slides of this GifExportOptions.  # noqa: E501

        Determines whether hidden slides will be exported.  # noqa: E501

        :return: The export_hidden_slides of this GifExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._export_hidden_slides

    @export_hidden_slides.setter
    def export_hidden_slides(self, export_hidden_slides):
        """Sets the export_hidden_slides of this GifExportOptions.

        Determines whether hidden slides will be exported.  # noqa: E501

        :param export_hidden_slides: The export_hidden_slides of this GifExportOptions.  # noqa: E501
        :type: bool
        """
        self._export_hidden_slides = export_hidden_slides

    @property
    def transition_fps(self):
        """Gets the transition_fps of this GifExportOptions.  # noqa: E501

        Gets or sets transition FPS [frames/sec]  # noqa: E501

        :return: The transition_fps of this GifExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._transition_fps

    @transition_fps.setter
    def transition_fps(self, transition_fps):
        """Sets the transition_fps of this GifExportOptions.

        Gets or sets transition FPS [frames/sec]  # noqa: E501

        :param transition_fps: The transition_fps of this GifExportOptions.  # noqa: E501
        :type: int
        """
        self._transition_fps = transition_fps

    @property
    def default_delay(self):
        """Gets the default_delay of this GifExportOptions.  # noqa: E501

        Gets or sets default delay time [ms].  # noqa: E501

        :return: The default_delay of this GifExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._default_delay

    @default_delay.setter
    def default_delay(self, default_delay):
        """Sets the default_delay of this GifExportOptions.

        Gets or sets default delay time [ms].  # noqa: E501

        :param default_delay: The default_delay of this GifExportOptions.  # noqa: E501
        :type: int
        """
        self._default_delay = default_delay

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
        if not isinstance(other, GifExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
