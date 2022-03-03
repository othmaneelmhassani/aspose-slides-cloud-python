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


class TextFrameFormat(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'three_d_format': 'ThreeDFormat',
        'transform': 'str'
    }

    attribute_map = {
        'three_d_format': 'threeDFormat',
        'transform': 'transform'
    }

    type_determiners = {
    }

    def __init__(self, three_d_format=None, transform=None):  # noqa: E501
        """TextFrameFormat - a model defined in Swagger"""  # noqa: E501

        self._three_d_format = None
        self._transform = None

        if three_d_format is not None:
            self.three_d_format = three_d_format
        if transform is not None:
            self.transform = transform

    @property
    def three_d_format(self):
        """Gets the three_d_format of this TextFrameFormat.  # noqa: E501

        Represents 3d effect properties for a text.  # noqa: E501

        :return: The three_d_format of this TextFrameFormat.  # noqa: E501
        :rtype: ThreeDFormat
        """
        return self._three_d_format

    @three_d_format.setter
    def three_d_format(self, three_d_format):
        """Sets the three_d_format of this TextFrameFormat.

        Represents 3d effect properties for a text.  # noqa: E501

        :param three_d_format: The three_d_format of this TextFrameFormat.  # noqa: E501
        :type: ThreeDFormat
        """
        self._three_d_format = three_d_format

    @property
    def transform(self):
        """Gets the transform of this TextFrameFormat.  # noqa: E501

        Gets or sets text wrapping shape.  # noqa: E501

        :return: The transform of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this TextFrameFormat.

        Gets or sets text wrapping shape.  # noqa: E501

        :param transform: The transform of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if transform is not None:
            allowed_values = ["None", "Plain", "Stop", "Triangle", "TriangleInverted", "Chevron", "ChevronInverted", "RingInside", "RingOutside", "ArchUp", "ArchDown", "Circle", "Button", "ArchUpPour", "ArchDownPour", "CirclePour", "ButtonPour", "CurveUp", "CurveDown", "CanUp", "CanDown", "Wave1", "Wave2", "DoubleWave1", "Wave4", "Inflate", "Deflate", "InflateBottom", "DeflateBottom", "InflateTop", "DeflateTop", "DeflateInflate", "DeflateInflateDeflate", "FadeRight", "FadeLeft", "FadeUp", "FadeDown", "SlantUp", "SlantDown", "CascadeUp", "CascadeDown", "Custom", "NotDefined"]  # noqa: E501
            if transform.isdigit():
                int_transform = int(transform)
                if int_transform < 0 or int_transform >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `transform` ({0}), must be one of {1}"  # noqa: E501
                        .format(transform, allowed_values)
                    )
                self._transform = allowed_values[int_transform]
                return
            if transform not in allowed_values:
                raise ValueError(
                    "Invalid value for `transform` ({0}), must be one of {1}"  # noqa: E501
                    .format(transform, allowed_values)
                )
        self._transform = transform

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
        if not isinstance(other, TextFrameFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
