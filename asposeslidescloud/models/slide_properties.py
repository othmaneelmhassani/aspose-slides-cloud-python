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

class SlideProperties(ResourceBase):


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
        'first_slide_number': 'int',
        'orientation': 'str',
        'scale_type': 'str',
        'size_type': 'str',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'first_slide_number': 'firstSlideNumber',
        'orientation': 'orientation',
        'scale_type': 'scaleType',
        'size_type': 'sizeType',
        'width': 'width',
        'height': 'height'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, first_slide_number=None, orientation=None, scale_type=None, size_type=None, width=None, height=None):  # noqa: E501
        """SlideProperties - a model defined in Swagger"""  # noqa: E501
        super(SlideProperties, self).__init__(self_uri, alternate_links)

        self._first_slide_number = None
        self._orientation = None
        self._scale_type = None
        self._size_type = None
        self._width = None
        self._height = None

        if first_slide_number is not None:
            self.first_slide_number = first_slide_number
        if orientation is not None:
            self.orientation = orientation
        if scale_type is not None:
            self.scale_type = scale_type
        if size_type is not None:
            self.size_type = size_type
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def first_slide_number(self):
        """Gets the first_slide_number of this SlideProperties.  # noqa: E501

        First slide number.  # noqa: E501

        :return: The first_slide_number of this SlideProperties.  # noqa: E501
        :rtype: int
        """
        return self._first_slide_number

    @first_slide_number.setter
    def first_slide_number(self, first_slide_number):
        """Sets the first_slide_number of this SlideProperties.

        First slide number.  # noqa: E501

        :param first_slide_number: The first_slide_number of this SlideProperties.  # noqa: E501
        :type: int
        """
        self._first_slide_number = first_slide_number

    @property
    def orientation(self):
        """Gets the orientation of this SlideProperties.  # noqa: E501

        Slide orientation.  # noqa: E501

        :return: The orientation of this SlideProperties.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this SlideProperties.

        Slide orientation.  # noqa: E501

        :param orientation: The orientation of this SlideProperties.  # noqa: E501
        :type: str
        """
        if orientation is not None:
            allowed_values = ["Landscape", "Portrait"]  # noqa: E501
            if orientation.isdigit():
                int_orientation = int(orientation)
                if int_orientation < 0 or int_orientation >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                        .format(orientation, allowed_values)
                    )
                self._orientation = allowed_values[int_orientation]
                return
            if orientation not in allowed_values:
                raise ValueError(
                    "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                    .format(orientation, allowed_values)
                )
        self._orientation = orientation

    @property
    def scale_type(self):
        """Gets the scale_type of this SlideProperties.  # noqa: E501

        Scale type.  # noqa: E501

        :return: The scale_type of this SlideProperties.  # noqa: E501
        :rtype: str
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type):
        """Sets the scale_type of this SlideProperties.

        Scale type.  # noqa: E501

        :param scale_type: The scale_type of this SlideProperties.  # noqa: E501
        :type: str
        """
        if scale_type is not None:
            allowed_values = ["DoNotScale", "EnsureFit", "Maximize"]  # noqa: E501
            if scale_type.isdigit():
                int_scale_type = int(scale_type)
                if int_scale_type < 0 or int_scale_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `scale_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(scale_type, allowed_values)
                    )
                self._scale_type = allowed_values[int_scale_type]
                return
            if scale_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `scale_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(scale_type, allowed_values)
                )
        self._scale_type = scale_type

    @property
    def size_type(self):
        """Gets the size_type of this SlideProperties.  # noqa: E501

        Size type.  # noqa: E501

        :return: The size_type of this SlideProperties.  # noqa: E501
        :rtype: str
        """
        return self._size_type

    @size_type.setter
    def size_type(self, size_type):
        """Sets the size_type of this SlideProperties.

        Size type.  # noqa: E501

        :param size_type: The size_type of this SlideProperties.  # noqa: E501
        :type: str
        """
        if size_type is not None:
            allowed_values = ["OnScreen", "LetterPaper", "A4Paper", "Slide35mm", "Overhead", "Banner", "Custom", "Ledger", "A3Paper", "B4IsoPaper", "B5IsoPaper", "B4JisPaper", "B5JisPaper", "HagakiCard", "OnScreen16x9", "OnScreen16x10", "Widescreen"]  # noqa: E501
            if size_type.isdigit():
                int_size_type = int(size_type)
                if int_size_type < 0 or int_size_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `size_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(size_type, allowed_values)
                    )
                self._size_type = allowed_values[int_size_type]
                return
            if size_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `size_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(size_type, allowed_values)
                )
        self._size_type = size_type

    @property
    def width(self):
        """Gets the width of this SlideProperties.  # noqa: E501

        Width.  # noqa: E501

        :return: The width of this SlideProperties.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this SlideProperties.

        Width.  # noqa: E501

        :param width: The width of this SlideProperties.  # noqa: E501
        :type: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this SlideProperties.  # noqa: E501

        Height.  # noqa: E501

        :return: The height of this SlideProperties.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this SlideProperties.

        Height.  # noqa: E501

        :param height: The height of this SlideProperties.  # noqa: E501
        :type: int
        """
        self._height = height

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
        if not isinstance(other, SlideProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
