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

class SlideShowProperties(ResourceBase):


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
        'loop': 'bool',
        'start_slide': 'int',
        'end_slide': 'int',
        'pen_color': 'str',
        'show_animation': 'bool',
        'show_narration': 'bool',
        'use_timings': 'bool',
        'slide_show_type': 'str',
        'show_scrollbar': 'bool'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'loop': 'loop',
        'start_slide': 'startSlide',
        'end_slide': 'endSlide',
        'pen_color': 'penColor',
        'show_animation': 'showAnimation',
        'show_narration': 'showNarration',
        'use_timings': 'useTimings',
        'slide_show_type': 'slideShowType',
        'show_scrollbar': 'showScrollbar'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, loop=None, start_slide=None, end_slide=None, pen_color=None, show_animation=None, show_narration=None, use_timings=None, slide_show_type=None, show_scrollbar=None):  # noqa: E501
        """SlideShowProperties - a model defined in Swagger"""  # noqa: E501
        super(SlideShowProperties, self).__init__(self_uri, alternate_links)

        self._loop = None
        self._start_slide = None
        self._end_slide = None
        self._pen_color = None
        self._show_animation = None
        self._show_narration = None
        self._use_timings = None
        self._slide_show_type = None
        self._show_scrollbar = None

        if loop is not None:
            self.loop = loop
        if start_slide is not None:
            self.start_slide = start_slide
        if end_slide is not None:
            self.end_slide = end_slide
        if pen_color is not None:
            self.pen_color = pen_color
        if show_animation is not None:
            self.show_animation = show_animation
        if show_narration is not None:
            self.show_narration = show_narration
        if use_timings is not None:
            self.use_timings = use_timings
        if slide_show_type is not None:
            self.slide_show_type = slide_show_type
        if show_scrollbar is not None:
            self.show_scrollbar = show_scrollbar

    @property
    def loop(self):
        """Gets the loop of this SlideShowProperties.  # noqa: E501

        Loop slide show.  # noqa: E501

        :return: The loop of this SlideShowProperties.  # noqa: E501
        :rtype: bool
        """
        return self._loop

    @loop.setter
    def loop(self, loop):
        """Sets the loop of this SlideShowProperties.

        Loop slide show.  # noqa: E501

        :param loop: The loop of this SlideShowProperties.  # noqa: E501
        :type: bool
        """
        self._loop = loop

    @property
    def start_slide(self):
        """Gets the start_slide of this SlideShowProperties.  # noqa: E501

        Start slide in the slide show.  # noqa: E501

        :return: The start_slide of this SlideShowProperties.  # noqa: E501
        :rtype: int
        """
        return self._start_slide

    @start_slide.setter
    def start_slide(self, start_slide):
        """Sets the start_slide of this SlideShowProperties.

        Start slide in the slide show.  # noqa: E501

        :param start_slide: The start_slide of this SlideShowProperties.  # noqa: E501
        :type: int
        """
        self._start_slide = start_slide

    @property
    def end_slide(self):
        """Gets the end_slide of this SlideShowProperties.  # noqa: E501

        End slides in the slide show.  # noqa: E501

        :return: The end_slide of this SlideShowProperties.  # noqa: E501
        :rtype: int
        """
        return self._end_slide

    @end_slide.setter
    def end_slide(self, end_slide):
        """Sets the end_slide of this SlideShowProperties.

        End slides in the slide show.  # noqa: E501

        :param end_slide: The end_slide of this SlideShowProperties.  # noqa: E501
        :type: int
        """
        self._end_slide = end_slide

    @property
    def pen_color(self):
        """Gets the pen_color of this SlideShowProperties.  # noqa: E501

        Pen color.  # noqa: E501

        :return: The pen_color of this SlideShowProperties.  # noqa: E501
        :rtype: str
        """
        return self._pen_color

    @pen_color.setter
    def pen_color(self, pen_color):
        """Sets the pen_color of this SlideShowProperties.

        Pen color.  # noqa: E501

        :param pen_color: The pen_color of this SlideShowProperties.  # noqa: E501
        :type: str
        """
        self._pen_color = pen_color

    @property
    def show_animation(self):
        """Gets the show_animation of this SlideShowProperties.  # noqa: E501

        Show animation.  # noqa: E501

        :return: The show_animation of this SlideShowProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_animation

    @show_animation.setter
    def show_animation(self, show_animation):
        """Sets the show_animation of this SlideShowProperties.

        Show animation.  # noqa: E501

        :param show_animation: The show_animation of this SlideShowProperties.  # noqa: E501
        :type: bool
        """
        self._show_animation = show_animation

    @property
    def show_narration(self):
        """Gets the show_narration of this SlideShowProperties.  # noqa: E501

        Show narrration.  # noqa: E501

        :return: The show_narration of this SlideShowProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_narration

    @show_narration.setter
    def show_narration(self, show_narration):
        """Sets the show_narration of this SlideShowProperties.

        Show narrration.  # noqa: E501

        :param show_narration: The show_narration of this SlideShowProperties.  # noqa: E501
        :type: bool
        """
        self._show_narration = show_narration

    @property
    def use_timings(self):
        """Gets the use_timings of this SlideShowProperties.  # noqa: E501

        Use timings.  # noqa: E501

        :return: The use_timings of this SlideShowProperties.  # noqa: E501
        :rtype: bool
        """
        return self._use_timings

    @use_timings.setter
    def use_timings(self, use_timings):
        """Sets the use_timings of this SlideShowProperties.

        Use timings.  # noqa: E501

        :param use_timings: The use_timings of this SlideShowProperties.  # noqa: E501
        :type: bool
        """
        self._use_timings = use_timings

    @property
    def slide_show_type(self):
        """Gets the slide_show_type of this SlideShowProperties.  # noqa: E501

        Slide show type.  # noqa: E501

        :return: The slide_show_type of this SlideShowProperties.  # noqa: E501
        :rtype: str
        """
        return self._slide_show_type

    @slide_show_type.setter
    def slide_show_type(self, slide_show_type):
        """Sets the slide_show_type of this SlideShowProperties.

        Slide show type.  # noqa: E501

        :param slide_show_type: The slide_show_type of this SlideShowProperties.  # noqa: E501
        :type: str
        """
        if slide_show_type is not None:
            allowed_values = ["BrowsedAtKiosk", "BrowsedByIndividual", "PresentedBySpeaker"]  # noqa: E501
            if slide_show_type.isdigit():
                int_slide_show_type = int(slide_show_type)
                if int_slide_show_type < 0 or int_slide_show_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `slide_show_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(slide_show_type, allowed_values)
                    )
                self._slide_show_type = allowed_values[int_slide_show_type]
                return
            if slide_show_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `slide_show_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(slide_show_type, allowed_values)
                )
        self._slide_show_type = slide_show_type

    @property
    def show_scrollbar(self):
        """Gets the show_scrollbar of this SlideShowProperties.  # noqa: E501

        Show scroll bar. Applied with BrowsedByIndividual slide show type.  # noqa: E501

        :return: The show_scrollbar of this SlideShowProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_scrollbar

    @show_scrollbar.setter
    def show_scrollbar(self, show_scrollbar):
        """Sets the show_scrollbar of this SlideShowProperties.

        Show scroll bar. Applied with BrowsedByIndividual slide show type.  # noqa: E501

        :param show_scrollbar: The show_scrollbar of this SlideShowProperties.  # noqa: E501
        :type: bool
        """
        self._show_scrollbar = show_scrollbar

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
        if not isinstance(other, SlideShowProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
