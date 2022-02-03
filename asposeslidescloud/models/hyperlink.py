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


class Hyperlink(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_disabled': 'bool',
        'action_type': 'str',
        'external_url': 'str',
        'target_slide_index': 'int',
        'target_frame': 'str',
        'tooltip': 'str',
        'history': 'bool',
        'highlight_click': 'bool',
        'stop_sound_on_click': 'bool',
        'color_source': 'str'
    }

    attribute_map = {
        'is_disabled': 'isDisabled',
        'action_type': 'actionType',
        'external_url': 'externalUrl',
        'target_slide_index': 'targetSlideIndex',
        'target_frame': 'targetFrame',
        'tooltip': 'tooltip',
        'history': 'history',
        'highlight_click': 'highlightClick',
        'stop_sound_on_click': 'stopSoundOnClick',
        'color_source': 'colorSource'
    }

    type_determiners = {
    }

    def __init__(self, is_disabled=None, action_type=None, external_url=None, target_slide_index=None, target_frame=None, tooltip=None, history=None, highlight_click=None, stop_sound_on_click=None, color_source=None):  # noqa: E501
        """Hyperlink - a model defined in Swagger"""  # noqa: E501

        self._is_disabled = None
        self._action_type = None
        self._external_url = None
        self._target_slide_index = None
        self._target_frame = None
        self._tooltip = None
        self._history = None
        self._highlight_click = None
        self._stop_sound_on_click = None
        self._color_source = None

        if is_disabled is not None:
            self.is_disabled = is_disabled
        self.action_type = action_type
        if external_url is not None:
            self.external_url = external_url
        if target_slide_index is not None:
            self.target_slide_index = target_slide_index
        if target_frame is not None:
            self.target_frame = target_frame
        if tooltip is not None:
            self.tooltip = tooltip
        if history is not None:
            self.history = history
        if highlight_click is not None:
            self.highlight_click = highlight_click
        if stop_sound_on_click is not None:
            self.stop_sound_on_click = stop_sound_on_click
        if color_source is not None:
            self.color_source = color_source

    @property
    def is_disabled(self):
        """Gets the is_disabled of this Hyperlink.  # noqa: E501

        If true Hypelink is not applied.   # noqa: E501

        :return: The is_disabled of this Hyperlink.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this Hyperlink.

        If true Hypelink is not applied.   # noqa: E501

        :param is_disabled: The is_disabled of this Hyperlink.  # noqa: E501
        :type: bool
        """
        self._is_disabled = is_disabled

    @property
    def action_type(self):
        """Gets the action_type of this Hyperlink.  # noqa: E501

        Type of HyperLink action               # noqa: E501

        :return: The action_type of this Hyperlink.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this Hyperlink.

        Type of HyperLink action               # noqa: E501

        :param action_type: The action_type of this Hyperlink.  # noqa: E501
        :type: str
        """
        if action_type is not None:
            allowed_values = ["NoAction", "Hyperlink", "JumpFirstSlide", "JumpPreviousSlide", "JumpNextSlide", "JumpLastSlide", "JumpEndShow", "JumpLastViewedSlide", "JumpSpecificSlide", "StartCustomSlideShow", "OpenFile", "OpenPresentation", "StartStopMedia", "StartMacro", "StartProgram", "Unknown"]  # noqa: E501
            if action_type.isdigit():
                int_action_type = int(action_type)
                if int_action_type < 0 or int_action_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(action_type, allowed_values)
                    )
                self._action_type = allowed_values[int_action_type]
                return
            if action_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(action_type, allowed_values)
                )
        self._action_type = action_type

    @property
    def external_url(self):
        """Gets the external_url of this Hyperlink.  # noqa: E501

        Specifies the external URL  # noqa: E501

        :return: The external_url of this Hyperlink.  # noqa: E501
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """Sets the external_url of this Hyperlink.

        Specifies the external URL  # noqa: E501

        :param external_url: The external_url of this Hyperlink.  # noqa: E501
        :type: str
        """
        self._external_url = external_url

    @property
    def target_slide_index(self):
        """Gets the target_slide_index of this Hyperlink.  # noqa: E501

        Index of the target slide  # noqa: E501

        :return: The target_slide_index of this Hyperlink.  # noqa: E501
        :rtype: int
        """
        return self._target_slide_index

    @target_slide_index.setter
    def target_slide_index(self, target_slide_index):
        """Sets the target_slide_index of this Hyperlink.

        Index of the target slide  # noqa: E501

        :param target_slide_index: The target_slide_index of this Hyperlink.  # noqa: E501
        :type: int
        """
        self._target_slide_index = target_slide_index

    @property
    def target_frame(self):
        """Gets the target_frame of this Hyperlink.  # noqa: E501

        Target frame  # noqa: E501

        :return: The target_frame of this Hyperlink.  # noqa: E501
        :rtype: str
        """
        return self._target_frame

    @target_frame.setter
    def target_frame(self, target_frame):
        """Sets the target_frame of this Hyperlink.

        Target frame  # noqa: E501

        :param target_frame: The target_frame of this Hyperlink.  # noqa: E501
        :type: str
        """
        self._target_frame = target_frame

    @property
    def tooltip(self):
        """Gets the tooltip of this Hyperlink.  # noqa: E501

        Hyperlink tooltip  # noqa: E501

        :return: The tooltip of this Hyperlink.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this Hyperlink.

        Hyperlink tooltip  # noqa: E501

        :param tooltip: The tooltip of this Hyperlink.  # noqa: E501
        :type: str
        """
        self._tooltip = tooltip

    @property
    def history(self):
        """Gets the history of this Hyperlink.  # noqa: E501

        Makes hyperlink viewed when it is invoked.               # noqa: E501

        :return: The history of this Hyperlink.  # noqa: E501
        :rtype: bool
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this Hyperlink.

        Makes hyperlink viewed when it is invoked.               # noqa: E501

        :param history: The history of this Hyperlink.  # noqa: E501
        :type: bool
        """
        self._history = history

    @property
    def highlight_click(self):
        """Gets the highlight_click of this Hyperlink.  # noqa: E501

        Determines whether the hyperlink should be highlighted on click.  # noqa: E501

        :return: The highlight_click of this Hyperlink.  # noqa: E501
        :rtype: bool
        """
        return self._highlight_click

    @highlight_click.setter
    def highlight_click(self, highlight_click):
        """Sets the highlight_click of this Hyperlink.

        Determines whether the hyperlink should be highlighted on click.  # noqa: E501

        :param highlight_click: The highlight_click of this Hyperlink.  # noqa: E501
        :type: bool
        """
        self._highlight_click = highlight_click

    @property
    def stop_sound_on_click(self):
        """Gets the stop_sound_on_click of this Hyperlink.  # noqa: E501

        Determines whether the sound should be stopped on hyperlink click  # noqa: E501

        :return: The stop_sound_on_click of this Hyperlink.  # noqa: E501
        :rtype: bool
        """
        return self._stop_sound_on_click

    @stop_sound_on_click.setter
    def stop_sound_on_click(self, stop_sound_on_click):
        """Sets the stop_sound_on_click of this Hyperlink.

        Determines whether the sound should be stopped on hyperlink click  # noqa: E501

        :param stop_sound_on_click: The stop_sound_on_click of this Hyperlink.  # noqa: E501
        :type: bool
        """
        self._stop_sound_on_click = stop_sound_on_click

    @property
    def color_source(self):
        """Gets the color_source of this Hyperlink.  # noqa: E501

        Represents the source of hyperlink color  # noqa: E501

        :return: The color_source of this Hyperlink.  # noqa: E501
        :rtype: str
        """
        return self._color_source

    @color_source.setter
    def color_source(self, color_source):
        """Sets the color_source of this Hyperlink.

        Represents the source of hyperlink color  # noqa: E501

        :param color_source: The color_source of this Hyperlink.  # noqa: E501
        :type: str
        """
        if color_source is not None:
            allowed_values = ["Styles", "PortionFormat"]  # noqa: E501
            if color_source.isdigit():
                int_color_source = int(color_source)
                if int_color_source < 0 or int_color_source >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `color_source` ({0}), must be one of {1}"  # noqa: E501
                        .format(color_source, allowed_values)
                    )
                self._color_source = allowed_values[int_color_source]
                return
            if color_source not in allowed_values:
                raise ValueError(
                    "Invalid value for `color_source` ({0}), must be one of {1}"  # noqa: E501
                    .format(color_source, allowed_values)
                )
        self._color_source = color_source

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
        if not isinstance(other, Hyperlink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
