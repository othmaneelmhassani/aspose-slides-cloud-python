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

class BlurImageEffect(ImageTransformEffect):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'radius': 'float',
        'grow': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'radius': 'radius',
        'grow': 'grow'
    }

    type_determiners = {
        'type': 'Blur',
    }

    def __init__(self, type='Blur', radius=None, grow=None):  # noqa: E501
        """BlurImageEffect - a model defined in Swagger"""  # noqa: E501
        super(BlurImageEffect, self).__init__(type)

        self._radius = None
        self._grow = None
        self.type = 'Blur'

        self.radius = radius
        self.grow = grow

    @property
    def radius(self):
        """Gets the radius of this BlurImageEffect.  # noqa: E501

        Returns or sets blur radius.  # noqa: E501

        :return: The radius of this BlurImageEffect.  # noqa: E501
        :rtype: float
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this BlurImageEffect.

        Returns or sets blur radius.  # noqa: E501

        :param radius: The radius of this BlurImageEffect.  # noqa: E501
        :type: float
        """
        self._radius = radius

    @property
    def grow(self):
        """Gets the grow of this BlurImageEffect.  # noqa: E501

        Determines whether the bounds of the object should be grown as a result of the blurring. True indicates the bounds are grown while false indicates that they are not.  # noqa: E501

        :return: The grow of this BlurImageEffect.  # noqa: E501
        :rtype: bool
        """
        return self._grow

    @grow.setter
    def grow(self, grow):
        """Sets the grow of this BlurImageEffect.

        Determines whether the bounds of the object should be grown as a result of the blurring. True indicates the bounds are grown while false indicates that they are not.  # noqa: E501

        :param grow: The grow of this BlurImageEffect.  # noqa: E501
        :type: bool
        """
        self._grow = grow

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
        if not isinstance(other, BlurImageEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
