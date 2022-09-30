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


class FontSubstRule(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_font': 'str',
        'target_font': 'str',
        'not_found_only': 'bool'
    }

    attribute_map = {
        'source_font': 'sourceFont',
        'target_font': 'targetFont',
        'not_found_only': 'notFoundOnly'
    }

    type_determiners = {
    }

    def __init__(self, source_font=None, target_font=None, not_found_only=None):  # noqa: E501
        """FontSubstRule - a model defined in Swagger"""  # noqa: E501

        self._source_font = None
        self._target_font = None
        self._not_found_only = None

        if source_font is not None:
            self.source_font = source_font
        if target_font is not None:
            self.target_font = target_font
        if not_found_only is not None:
            self.not_found_only = not_found_only

    @property
    def source_font(self):
        """Gets the source_font of this FontSubstRule.  # noqa: E501

        Font to substitute.  # noqa: E501

        :return: The source_font of this FontSubstRule.  # noqa: E501
        :rtype: str
        """
        return self._source_font

    @source_font.setter
    def source_font(self, source_font):
        """Sets the source_font of this FontSubstRule.

        Font to substitute.  # noqa: E501

        :param source_font: The source_font of this FontSubstRule.  # noqa: E501
        :type: str
        """
        self._source_font = source_font

    @property
    def target_font(self):
        """Gets the target_font of this FontSubstRule.  # noqa: E501

        Substitution font.  # noqa: E501

        :return: The target_font of this FontSubstRule.  # noqa: E501
        :rtype: str
        """
        return self._target_font

    @target_font.setter
    def target_font(self, target_font):
        """Sets the target_font of this FontSubstRule.

        Substitution font.  # noqa: E501

        :param target_font: The target_font of this FontSubstRule.  # noqa: E501
        :type: str
        """
        self._target_font = target_font

    @property
    def not_found_only(self):
        """Gets the not_found_only of this FontSubstRule.  # noqa: E501

        Substitute when font is not found. Default: true.  # noqa: E501

        :return: The not_found_only of this FontSubstRule.  # noqa: E501
        :rtype: bool
        """
        return self._not_found_only

    @not_found_only.setter
    def not_found_only(self, not_found_only):
        """Sets the not_found_only of this FontSubstRule.

        Substitute when font is not found. Default: true.  # noqa: E501

        :param not_found_only: The not_found_only of this FontSubstRule.  # noqa: E501
        :type: bool
        """
        self._not_found_only = not_found_only

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
        if not isinstance(other, FontSubstRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
