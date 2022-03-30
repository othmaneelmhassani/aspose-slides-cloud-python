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

from asposeslidescloud.models.export_options import ExportOptions

class VideoExportOptions(ExportOptions):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_regular_font': 'str',
        'height': 'int',
        'width': 'int',
        'font_fallback_rules': 'list[FontFallbackRule]',
        'format': 'str',
        'transition_duration': 'int',
        'video_resolution_type': 'str'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'height': 'height',
        'width': 'width',
        'font_fallback_rules': 'fontFallbackRules',
        'format': 'format',
        'transition_duration': 'transitionDuration',
        'video_resolution_type': 'videoResolutionType'
    }

    type_determiners = {
        'format': 'mpeg4',
    }

    def __init__(self, default_regular_font=None, height=None, width=None, font_fallback_rules=None, format='mpeg4', transition_duration=None, video_resolution_type=None):  # noqa: E501
        """VideoExportOptions - a model defined in Swagger"""  # noqa: E501
        super(VideoExportOptions, self).__init__(default_regular_font, height, width, font_fallback_rules, format)

        self._transition_duration = None
        self._video_resolution_type = None
        self.format = 'mpeg4'

        if transition_duration is not None:
            self.transition_duration = transition_duration
        if video_resolution_type is not None:
            self.video_resolution_type = video_resolution_type

    @property
    def transition_duration(self):
        """Gets the transition_duration of this VideoExportOptions.  # noqa: E501

        Transition duration.  # noqa: E501

        :return: The transition_duration of this VideoExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._transition_duration

    @transition_duration.setter
    def transition_duration(self, transition_duration):
        """Sets the transition_duration of this VideoExportOptions.

        Transition duration.  # noqa: E501

        :param transition_duration: The transition_duration of this VideoExportOptions.  # noqa: E501
        :type: int
        """
        self._transition_duration = transition_duration

    @property
    def video_resolution_type(self):
        """Gets the video_resolution_type of this VideoExportOptions.  # noqa: E501

        Video resolution type  # noqa: E501

        :return: The video_resolution_type of this VideoExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._video_resolution_type

    @video_resolution_type.setter
    def video_resolution_type(self, video_resolution_type):
        """Sets the video_resolution_type of this VideoExportOptions.

        Video resolution type  # noqa: E501

        :param video_resolution_type: The video_resolution_type of this VideoExportOptions.  # noqa: E501
        :type: str
        """
        if video_resolution_type is not None:
            allowed_values = ["FullHD", "SD", "HD", "QHD"]  # noqa: E501
            if video_resolution_type.isdigit():
                int_video_resolution_type = int(video_resolution_type)
                if int_video_resolution_type < 0 or int_video_resolution_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `video_resolution_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(video_resolution_type, allowed_values)
                    )
                self._video_resolution_type = allowed_values[int_video_resolution_type]
                return
            if video_resolution_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `video_resolution_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(video_resolution_type, allowed_values)
                )
        self._video_resolution_type = video_resolution_type

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
        if not isinstance(other, VideoExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
