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


class Camera(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'camera_type': 'str',
        'field_of_view_angle': 'float',
        'zoom': 'float',
        'x_rotation': 'float',
        'y_rotation': 'float',
        'z_rotation': 'float'
    }

    attribute_map = {
        'camera_type': 'cameraType',
        'field_of_view_angle': 'fieldOfViewAngle',
        'zoom': 'zoom',
        'x_rotation': 'xRotation',
        'y_rotation': 'yRotation',
        'z_rotation': 'zRotation'
    }

    type_determiners = {
    }

    def __init__(self, camera_type=None, field_of_view_angle=None, zoom=None, x_rotation=None, y_rotation=None, z_rotation=None):  # noqa: E501
        """Camera - a model defined in Swagger"""  # noqa: E501

        self._camera_type = None
        self._field_of_view_angle = None
        self._zoom = None
        self._x_rotation = None
        self._y_rotation = None
        self._z_rotation = None

        if camera_type is not None:
            self.camera_type = camera_type
        if field_of_view_angle is not None:
            self.field_of_view_angle = field_of_view_angle
        if zoom is not None:
            self.zoom = zoom
        if x_rotation is not None:
            self.x_rotation = x_rotation
        if y_rotation is not None:
            self.y_rotation = y_rotation
        if z_rotation is not None:
            self.z_rotation = z_rotation

    @property
    def camera_type(self):
        """Gets the camera_type of this Camera.  # noqa: E501

        Camera type  # noqa: E501

        :return: The camera_type of this Camera.  # noqa: E501
        :rtype: str
        """
        return self._camera_type

    @camera_type.setter
    def camera_type(self, camera_type):
        """Sets the camera_type of this Camera.

        Camera type  # noqa: E501

        :param camera_type: The camera_type of this Camera.  # noqa: E501
        :type: str
        """
        if camera_type is not None:
            allowed_values = ["IsometricBottomDown", "IsometricBottomUp", "IsometricLeftDown", "IsometricLeftUp", "IsometricOffAxis1Left", "IsometricOffAxis1Right", "IsometricOffAxis1Top", "IsometricOffAxis2Left", "IsometricOffAxis2Right", "IsometricOffAxis2Top", "IsometricOffAxis3Bottom", "IsometricOffAxis3Left", "IsometricOffAxis3Right", "IsometricOffAxis4Bottom", "IsometricOffAxis4Left", "IsometricOffAxis4Right", "IsometricRightDown", "IsometricRightUp", "IsometricTopDown", "IsometricTopUp", "LegacyObliqueBottom", "LegacyObliqueBottomLeft", "LegacyObliqueBottomRight", "LegacyObliqueFront", "LegacyObliqueLeft", "LegacyObliqueRight", "LegacyObliqueTop", "LegacyObliqueTopLeft", "LegacyObliqueTopRight", "LegacyPerspectiveBottom", "LegacyPerspectiveBottomLeft", "LegacyPerspectiveBottomRight", "LegacyPerspectiveFront", "LegacyPerspectiveLeft", "LegacyPerspectiveRight", "LegacyPerspectiveTop", "LegacyPerspectiveTopLeft", "LegacyPerspectiveTopRight", "ObliqueBottom", "ObliqueBottomLeft", "ObliqueBottomRight", "ObliqueLeft", "ObliqueRight", "ObliqueTop", "ObliqueTopLeft", "ObliqueTopRight", "OrthographicFront", "PerspectiveAbove", "PerspectiveAboveLeftFacing", "PerspectiveAboveRightFacing", "PerspectiveBelow", "PerspectiveContrastingLeftFacing", "PerspectiveContrastingRightFacing", "PerspectiveFront", "PerspectiveHeroicExtremeLeftFacing", "PerspectiveHeroicExtremeRightFacing", "PerspectiveHeroicLeftFacing", "PerspectiveHeroicRightFacing", "PerspectiveLeft", "PerspectiveRelaxed", "PerspectiveRelaxedModerately", "PerspectiveRight", "NotDefined"]  # noqa: E501
            if camera_type.isdigit():
                int_camera_type = int(camera_type)
                if int_camera_type < 0 or int_camera_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `camera_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(camera_type, allowed_values)
                    )
                self._camera_type = allowed_values[int_camera_type]
                return
            if camera_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `camera_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(camera_type, allowed_values)
                )
        self._camera_type = camera_type

    @property
    def field_of_view_angle(self):
        """Gets the field_of_view_angle of this Camera.  # noqa: E501

        Camera FOV  # noqa: E501

        :return: The field_of_view_angle of this Camera.  # noqa: E501
        :rtype: float
        """
        return self._field_of_view_angle

    @field_of_view_angle.setter
    def field_of_view_angle(self, field_of_view_angle):
        """Sets the field_of_view_angle of this Camera.

        Camera FOV  # noqa: E501

        :param field_of_view_angle: The field_of_view_angle of this Camera.  # noqa: E501
        :type: float
        """
        self._field_of_view_angle = field_of_view_angle

    @property
    def zoom(self):
        """Gets the zoom of this Camera.  # noqa: E501

        Camera zoom  # noqa: E501

        :return: The zoom of this Camera.  # noqa: E501
        :rtype: float
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """Sets the zoom of this Camera.

        Camera zoom  # noqa: E501

        :param zoom: The zoom of this Camera.  # noqa: E501
        :type: float
        """
        self._zoom = zoom

    @property
    def x_rotation(self):
        """Gets the x_rotation of this Camera.  # noqa: E501

        XRotation  # noqa: E501

        :return: The x_rotation of this Camera.  # noqa: E501
        :rtype: float
        """
        return self._x_rotation

    @x_rotation.setter
    def x_rotation(self, x_rotation):
        """Sets the x_rotation of this Camera.

        XRotation  # noqa: E501

        :param x_rotation: The x_rotation of this Camera.  # noqa: E501
        :type: float
        """
        self._x_rotation = x_rotation

    @property
    def y_rotation(self):
        """Gets the y_rotation of this Camera.  # noqa: E501

        YRotation  # noqa: E501

        :return: The y_rotation of this Camera.  # noqa: E501
        :rtype: float
        """
        return self._y_rotation

    @y_rotation.setter
    def y_rotation(self, y_rotation):
        """Sets the y_rotation of this Camera.

        YRotation  # noqa: E501

        :param y_rotation: The y_rotation of this Camera.  # noqa: E501
        :type: float
        """
        self._y_rotation = y_rotation

    @property
    def z_rotation(self):
        """Gets the z_rotation of this Camera.  # noqa: E501

        ZRotation  # noqa: E501

        :return: The z_rotation of this Camera.  # noqa: E501
        :rtype: float
        """
        return self._z_rotation

    @z_rotation.setter
    def z_rotation(self, z_rotation):
        """Sets the z_rotation of this Camera.

        ZRotation  # noqa: E501

        :param z_rotation: The z_rotation of this Camera.  # noqa: E501
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
        if not isinstance(other, Camera):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
