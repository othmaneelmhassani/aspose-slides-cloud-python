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

class Html5ExportOptions(ExportOptions):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_regular_font': 'str',
        'font_fallback_rules': 'list[FontFallbackRule]',
        'font_subst_rules': 'list[FontSubstRule]',
        'format': 'str',
        'animate_transitions': 'bool',
        'animate_shapes': 'bool'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'animate_transitions': 'animateTransitions',
        'animate_shapes': 'animateShapes'
    }

    type_determiners = {
        'format': 'html5',
    }

    def __init__(self, default_regular_font=None, font_fallback_rules=None, font_subst_rules=None, format='html5', animate_transitions=None, animate_shapes=None):  # noqa: E501
        """Html5ExportOptions - a model defined in Swagger"""  # noqa: E501
        super(Html5ExportOptions, self).__init__(default_regular_font, font_fallback_rules, font_subst_rules, format)

        self._animate_transitions = None
        self._animate_shapes = None
        self.format = 'html5'

        if animate_transitions is not None:
            self.animate_transitions = animate_transitions
        if animate_shapes is not None:
            self.animate_shapes = animate_shapes

    @property
    def animate_transitions(self):
        """Gets the animate_transitions of this Html5ExportOptions.  # noqa: E501

        Gets or sets transitions animation option.  # noqa: E501

        :return: The animate_transitions of this Html5ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._animate_transitions

    @animate_transitions.setter
    def animate_transitions(self, animate_transitions):
        """Sets the animate_transitions of this Html5ExportOptions.

        Gets or sets transitions animation option.  # noqa: E501

        :param animate_transitions: The animate_transitions of this Html5ExportOptions.  # noqa: E501
        :type: bool
        """
        self._animate_transitions = animate_transitions

    @property
    def animate_shapes(self):
        """Gets the animate_shapes of this Html5ExportOptions.  # noqa: E501

        Gets or sets shapes animation option.  # noqa: E501

        :return: The animate_shapes of this Html5ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._animate_shapes

    @animate_shapes.setter
    def animate_shapes(self, animate_shapes):
        """Sets the animate_shapes of this Html5ExportOptions.

        Gets or sets shapes animation option.  # noqa: E501

        :param animate_shapes: The animate_shapes of this Html5ExportOptions.  # noqa: E501
        :type: bool
        """
        self._animate_shapes = animate_shapes

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
        if not isinstance(other, Html5ExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
