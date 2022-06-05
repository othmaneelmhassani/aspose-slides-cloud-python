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

class TintEffect(ImageTransformEffect):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'hue': 'float',
        'amount': 'float'
    }

    attribute_map = {
        'type': 'type',
        'hue': 'hue',
        'amount': 'amount'
    }

    type_determiners = {
        'type': 'Tint',
    }

    def __init__(self, type='Tint', hue=None, amount=None):  # noqa: E501
        """TintEffect - a model defined in Swagger"""  # noqa: E501
        super(TintEffect, self).__init__(type)

        self._hue = None
        self._amount = None
        self.type = 'Tint'

        self.hue = hue
        self.amount = amount

    @property
    def hue(self):
        """Gets the hue of this TintEffect.  # noqa: E501

        Hue  # noqa: E501

        :return: The hue of this TintEffect.  # noqa: E501
        :rtype: float
        """
        return self._hue

    @hue.setter
    def hue(self, hue):
        """Sets the hue of this TintEffect.

        Hue  # noqa: E501

        :param hue: The hue of this TintEffect.  # noqa: E501
        :type: float
        """
        self._hue = hue

    @property
    def amount(self):
        """Gets the amount of this TintEffect.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this TintEffect.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TintEffect.

        Amount  # noqa: E501

        :param amount: The amount of this TintEffect.  # noqa: E501
        :type: float
        """
        self._amount = amount

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
        if not isinstance(other, TintEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
