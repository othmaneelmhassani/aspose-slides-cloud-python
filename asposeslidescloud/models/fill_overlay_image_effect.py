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

from asposeslidescloud.models.image_transform_effect import ImageTransformEffect

class FillOverlayImageEffect(ImageTransformEffect):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'blend': 'str',
        'fill_format': 'FillFormat'
    }

    attribute_map = {
        'type': 'type',
        'blend': 'blend',
        'fill_format': 'fillFormat'
    }

    type_determiners = {
        'type': 'FillOverlay',
    }

    def __init__(self, type='FillOverlay', blend=None, fill_format=None):  # noqa: E501
        """FillOverlayImageEffect - a model defined in Swagger"""  # noqa: E501
        super(FillOverlayImageEffect, self).__init__(type)

        self._blend = None
        self._fill_format = None
        self.type = 'FillOverlay'

        self.blend = blend
        if fill_format is not None:
            self.fill_format = fill_format

    @property
    def blend(self):
        """Gets the blend of this FillOverlayImageEffect.  # noqa: E501

        FillBlendMode.  # noqa: E501

        :return: The blend of this FillOverlayImageEffect.  # noqa: E501
        :rtype: str
        """
        return self._blend

    @blend.setter
    def blend(self, blend):
        """Sets the blend of this FillOverlayImageEffect.

        FillBlendMode.  # noqa: E501

        :param blend: The blend of this FillOverlayImageEffect.  # noqa: E501
        :type: str
        """
        if blend is not None:
            allowed_values = ["Darken", "Lighten", "Multiply", "Overlay", "Screen"]  # noqa: E501
            if blend.isdigit():
                int_blend = int(blend)
                if int_blend < 0 or int_blend >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `blend` ({0}), must be one of {1}"  # noqa: E501
                        .format(blend, allowed_values)
                    )
                self._blend = allowed_values[int_blend]
                return
            if blend not in allowed_values:
                raise ValueError(
                    "Invalid value for `blend` ({0}), must be one of {1}"  # noqa: E501
                    .format(blend, allowed_values)
                )
        self._blend = blend

    @property
    def fill_format(self):
        """Gets the fill_format of this FillOverlayImageEffect.  # noqa: E501

        Fill format.  # noqa: E501

        :return: The fill_format of this FillOverlayImageEffect.  # noqa: E501
        :rtype: FillFormat
        """
        return self._fill_format

    @fill_format.setter
    def fill_format(self, fill_format):
        """Sets the fill_format of this FillOverlayImageEffect.

        Fill format.  # noqa: E501

        :param fill_format: The fill_format of this FillOverlayImageEffect.  # noqa: E501
        :type: FillFormat
        """
        self._fill_format = fill_format

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
        if not isinstance(other, FillOverlayImageEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
