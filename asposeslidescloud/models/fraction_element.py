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

from asposeslidescloud.models.math_element import MathElement

class FractionElement(MathElement):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'fraction_type': 'str',
        'numerator': 'MathElement',
        'denominator': 'MathElement'
    }

    attribute_map = {
        'type': 'type',
        'fraction_type': 'fractionType',
        'numerator': 'numerator',
        'denominator': 'denominator'
    }

    type_determiners = {
        'type': 'Fraction',
    }

    def __init__(self, type='Fraction', fraction_type=None, numerator=None, denominator=None):  # noqa: E501
        """FractionElement - a model defined in Swagger"""  # noqa: E501
        super(FractionElement, self).__init__(type)

        self._fraction_type = None
        self._numerator = None
        self._denominator = None
        self.type = 'Fraction'

        if fraction_type is not None:
            self.fraction_type = fraction_type
        if numerator is not None:
            self.numerator = numerator
        if denominator is not None:
            self.denominator = denominator

    @property
    def fraction_type(self):
        """Gets the fraction_type of this FractionElement.  # noqa: E501

        Fraction type  # noqa: E501

        :return: The fraction_type of this FractionElement.  # noqa: E501
        :rtype: str
        """
        return self._fraction_type

    @fraction_type.setter
    def fraction_type(self, fraction_type):
        """Sets the fraction_type of this FractionElement.

        Fraction type  # noqa: E501

        :param fraction_type: The fraction_type of this FractionElement.  # noqa: E501
        :type: str
        """
        if fraction_type is not None:
            allowed_values = ["Bar", "Skewed", "Linear", "NoBar"]  # noqa: E501
            if fraction_type.isdigit():
                int_fraction_type = int(fraction_type)
                if int_fraction_type < 0 or int_fraction_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `fraction_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(fraction_type, allowed_values)
                    )
                self._fraction_type = allowed_values[int_fraction_type]
                return
            if fraction_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `fraction_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(fraction_type, allowed_values)
                )
        self._fraction_type = fraction_type

    @property
    def numerator(self):
        """Gets the numerator of this FractionElement.  # noqa: E501

        Numerator  # noqa: E501

        :return: The numerator of this FractionElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        """Sets the numerator of this FractionElement.

        Numerator  # noqa: E501

        :param numerator: The numerator of this FractionElement.  # noqa: E501
        :type: MathElement
        """
        self._numerator = numerator

    @property
    def denominator(self):
        """Gets the denominator of this FractionElement.  # noqa: E501

        Denominator  # noqa: E501

        :return: The denominator of this FractionElement.  # noqa: E501
        :rtype: MathElement
        """
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        """Sets the denominator of this FractionElement.

        Denominator  # noqa: E501

        :param denominator: The denominator of this FractionElement.  # noqa: E501
        :type: MathElement
        """
        self._denominator = denominator

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
        if not isinstance(other, FractionElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
