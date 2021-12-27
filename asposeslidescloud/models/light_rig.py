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


class LightRig(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'direction': 'str',
        'light_type': 'str',
        'x_rotation': 'float',
        'y_rotation': 'float',
        'z_rotation': 'float'
    }

    attribute_map = {
        'direction': 'direction',
        'light_type': 'lightType',
        'x_rotation': 'xRotation',
        'y_rotation': 'yRotation',
        'z_rotation': 'zRotation'
    }

    type_determiners = {
    }

    def __init__(self, direction=None, light_type=None, x_rotation=None, y_rotation=None, z_rotation=None):  # noqa: E501
        """LightRig - a model defined in Swagger"""  # noqa: E501

        self._direction = None
        self._light_type = None
        self._x_rotation = None
        self._y_rotation = None
        self._z_rotation = None

        if direction is not None:
            self.direction = direction
        if light_type is not None:
            self.light_type = light_type
        if x_rotation is not None:
            self.x_rotation = x_rotation
        if y_rotation is not None:
            self.y_rotation = y_rotation
        if z_rotation is not None:
            self.z_rotation = z_rotation

    @property
    def direction(self):
        """Gets the direction of this LightRig.  # noqa: E501

        Light direction  # noqa: E501

        :return: The direction of this LightRig.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this LightRig.

        Light direction  # noqa: E501

        :param direction: The direction of this LightRig.  # noqa: E501
        :type: str
        """
        if direction is not None:
            allowed_values = ["TopLeft", "Top", "TopRight", "Right", "BottomRight", "Bottom", "BottomLeft", "Left", "NotDefined"]  # noqa: E501
            if direction.isdigit():
                int_direction = int(direction)
                if int_direction < 0 or int_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(direction, allowed_values)
                    )
                self._direction = allowed_values[int_direction]
                return
            if direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(direction, allowed_values)
                )
        self._direction = direction

    @property
    def light_type(self):
        """Gets the light_type of this LightRig.  # noqa: E501

        Light type  # noqa: E501

        :return: The light_type of this LightRig.  # noqa: E501
        :rtype: str
        """
        return self._light_type

    @light_type.setter
    def light_type(self, light_type):
        """Sets the light_type of this LightRig.

        Light type  # noqa: E501

        :param light_type: The light_type of this LightRig.  # noqa: E501
        :type: str
        """
        if light_type is not None:
            allowed_values = ["Balanced", "BrightRoom", "Chilly", "Contrasting", "Flat", "Flood", "Freezing", "Glow", "Harsh", "LegacyFlat1", "LegacyFlat2", "LegacyFlat3", "LegacyFlat4", "LegacyHarsh1", "LegacyHarsh2", "LegacyHarsh3", "LegacyHarsh4", "LegacyNormal1", "LegacyNormal2", "LegacyNormal3", "LegacyNormal4", "Morning", "Soft", "Sunrise", "Sunset", "ThreePt", "TwoPt", "NotDefined"]  # noqa: E501
            if light_type.isdigit():
                int_light_type = int(light_type)
                if int_light_type < 0 or int_light_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `light_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(light_type, allowed_values)
                    )
                self._light_type = allowed_values[int_light_type]
                return
            if light_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `light_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(light_type, allowed_values)
                )
        self._light_type = light_type

    @property
    def x_rotation(self):
        """Gets the x_rotation of this LightRig.  # noqa: E501

        XRotation  # noqa: E501

        :return: The x_rotation of this LightRig.  # noqa: E501
        :rtype: float
        """
        return self._x_rotation

    @x_rotation.setter
    def x_rotation(self, x_rotation):
        """Sets the x_rotation of this LightRig.

        XRotation  # noqa: E501

        :param x_rotation: The x_rotation of this LightRig.  # noqa: E501
        :type: float
        """
        self._x_rotation = x_rotation

    @property
    def y_rotation(self):
        """Gets the y_rotation of this LightRig.  # noqa: E501

        YRotation  # noqa: E501

        :return: The y_rotation of this LightRig.  # noqa: E501
        :rtype: float
        """
        return self._y_rotation

    @y_rotation.setter
    def y_rotation(self, y_rotation):
        """Sets the y_rotation of this LightRig.

        YRotation  # noqa: E501

        :param y_rotation: The y_rotation of this LightRig.  # noqa: E501
        :type: float
        """
        self._y_rotation = y_rotation

    @property
    def z_rotation(self):
        """Gets the z_rotation of this LightRig.  # noqa: E501

        ZRotation  # noqa: E501

        :return: The z_rotation of this LightRig.  # noqa: E501
        :rtype: float
        """
        return self._z_rotation

    @z_rotation.setter
    def z_rotation(self, z_rotation):
        """Sets the z_rotation of this LightRig.

        ZRotation  # noqa: E501

        :param z_rotation: The z_rotation of this LightRig.  # noqa: E501
        :type: float
        """
        self._z_rotation = z_rotation

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
        if not isinstance(other, LightRig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
