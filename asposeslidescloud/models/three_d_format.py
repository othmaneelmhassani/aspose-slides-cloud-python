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


class ThreeDFormat(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bevel_bottom': 'ShapeBevel',
        'bevel_top': 'ShapeBevel',
        'camera': 'Camera',
        'contour_color': 'str',
        'contour_width': 'float',
        'depth': 'float',
        'extrusion_color': 'str',
        'extrusion_height': 'float',
        'light_rig': 'LightRig',
        'material': 'str'
    }

    attribute_map = {
        'bevel_bottom': 'bevelBottom',
        'bevel_top': 'bevelTop',
        'camera': 'camera',
        'contour_color': 'contourColor',
        'contour_width': 'contourWidth',
        'depth': 'depth',
        'extrusion_color': 'extrusionColor',
        'extrusion_height': 'extrusionHeight',
        'light_rig': 'lightRig',
        'material': 'material'
    }

    type_determiners = {
    }

    def __init__(self, bevel_bottom=None, bevel_top=None, camera=None, contour_color=None, contour_width=None, depth=None, extrusion_color=None, extrusion_height=None, light_rig=None, material=None):  # noqa: E501
        """ThreeDFormat - a model defined in Swagger"""  # noqa: E501

        self._bevel_bottom = None
        self._bevel_top = None
        self._camera = None
        self._contour_color = None
        self._contour_width = None
        self._depth = None
        self._extrusion_color = None
        self._extrusion_height = None
        self._light_rig = None
        self._material = None

        if bevel_bottom is not None:
            self.bevel_bottom = bevel_bottom
        if bevel_top is not None:
            self.bevel_top = bevel_top
        if camera is not None:
            self.camera = camera
        if contour_color is not None:
            self.contour_color = contour_color
        if contour_width is not None:
            self.contour_width = contour_width
        if depth is not None:
            self.depth = depth
        if extrusion_color is not None:
            self.extrusion_color = extrusion_color
        if extrusion_height is not None:
            self.extrusion_height = extrusion_height
        if light_rig is not None:
            self.light_rig = light_rig
        if material is not None:
            self.material = material

    @property
    def bevel_bottom(self):
        """Gets the bevel_bottom of this ThreeDFormat.  # noqa: E501

        Type of a bottom 3D bevel.               # noqa: E501

        :return: The bevel_bottom of this ThreeDFormat.  # noqa: E501
        :rtype: ShapeBevel
        """
        return self._bevel_bottom

    @bevel_bottom.setter
    def bevel_bottom(self, bevel_bottom):
        """Sets the bevel_bottom of this ThreeDFormat.

        Type of a bottom 3D bevel.               # noqa: E501

        :param bevel_bottom: The bevel_bottom of this ThreeDFormat.  # noqa: E501
        :type: ShapeBevel
        """
        self._bevel_bottom = bevel_bottom

    @property
    def bevel_top(self):
        """Gets the bevel_top of this ThreeDFormat.  # noqa: E501

        Type of a top 3D bevel.               # noqa: E501

        :return: The bevel_top of this ThreeDFormat.  # noqa: E501
        :rtype: ShapeBevel
        """
        return self._bevel_top

    @bevel_top.setter
    def bevel_top(self, bevel_top):
        """Sets the bevel_top of this ThreeDFormat.

        Type of a top 3D bevel.               # noqa: E501

        :param bevel_top: The bevel_top of this ThreeDFormat.  # noqa: E501
        :type: ShapeBevel
        """
        self._bevel_top = bevel_top

    @property
    def camera(self):
        """Gets the camera of this ThreeDFormat.  # noqa: E501

        Camera  # noqa: E501

        :return: The camera of this ThreeDFormat.  # noqa: E501
        :rtype: Camera
        """
        return self._camera

    @camera.setter
    def camera(self, camera):
        """Sets the camera of this ThreeDFormat.

        Camera  # noqa: E501

        :param camera: The camera of this ThreeDFormat.  # noqa: E501
        :type: Camera
        """
        self._camera = camera

    @property
    def contour_color(self):
        """Gets the contour_color of this ThreeDFormat.  # noqa: E501

        Contour color  # noqa: E501

        :return: The contour_color of this ThreeDFormat.  # noqa: E501
        :rtype: str
        """
        return self._contour_color

    @contour_color.setter
    def contour_color(self, contour_color):
        """Sets the contour_color of this ThreeDFormat.

        Contour color  # noqa: E501

        :param contour_color: The contour_color of this ThreeDFormat.  # noqa: E501
        :type: str
        """
        self._contour_color = contour_color

    @property
    def contour_width(self):
        """Gets the contour_width of this ThreeDFormat.  # noqa: E501

        Contour width  # noqa: E501

        :return: The contour_width of this ThreeDFormat.  # noqa: E501
        :rtype: float
        """
        return self._contour_width

    @contour_width.setter
    def contour_width(self, contour_width):
        """Sets the contour_width of this ThreeDFormat.

        Contour width  # noqa: E501

        :param contour_width: The contour_width of this ThreeDFormat.  # noqa: E501
        :type: float
        """
        self._contour_width = contour_width

    @property
    def depth(self):
        """Gets the depth of this ThreeDFormat.  # noqa: E501

        Depth  # noqa: E501

        :return: The depth of this ThreeDFormat.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this ThreeDFormat.

        Depth  # noqa: E501

        :param depth: The depth of this ThreeDFormat.  # noqa: E501
        :type: float
        """
        self._depth = depth

    @property
    def extrusion_color(self):
        """Gets the extrusion_color of this ThreeDFormat.  # noqa: E501

        Extrusion color  # noqa: E501

        :return: The extrusion_color of this ThreeDFormat.  # noqa: E501
        :rtype: str
        """
        return self._extrusion_color

    @extrusion_color.setter
    def extrusion_color(self, extrusion_color):
        """Sets the extrusion_color of this ThreeDFormat.

        Extrusion color  # noqa: E501

        :param extrusion_color: The extrusion_color of this ThreeDFormat.  # noqa: E501
        :type: str
        """
        self._extrusion_color = extrusion_color

    @property
    def extrusion_height(self):
        """Gets the extrusion_height of this ThreeDFormat.  # noqa: E501

        Extrusion height  # noqa: E501

        :return: The extrusion_height of this ThreeDFormat.  # noqa: E501
        :rtype: float
        """
        return self._extrusion_height

    @extrusion_height.setter
    def extrusion_height(self, extrusion_height):
        """Sets the extrusion_height of this ThreeDFormat.

        Extrusion height  # noqa: E501

        :param extrusion_height: The extrusion_height of this ThreeDFormat.  # noqa: E501
        :type: float
        """
        self._extrusion_height = extrusion_height

    @property
    def light_rig(self):
        """Gets the light_rig of this ThreeDFormat.  # noqa: E501

        Light rig  # noqa: E501

        :return: The light_rig of this ThreeDFormat.  # noqa: E501
        :rtype: LightRig
        """
        return self._light_rig

    @light_rig.setter
    def light_rig(self, light_rig):
        """Sets the light_rig of this ThreeDFormat.

        Light rig  # noqa: E501

        :param light_rig: The light_rig of this ThreeDFormat.  # noqa: E501
        :type: LightRig
        """
        self._light_rig = light_rig

    @property
    def material(self):
        """Gets the material of this ThreeDFormat.  # noqa: E501

        Material  # noqa: E501

        :return: The material of this ThreeDFormat.  # noqa: E501
        :rtype: str
        """
        return self._material

    @material.setter
    def material(self, material):
        """Sets the material of this ThreeDFormat.

        Material  # noqa: E501

        :param material: The material of this ThreeDFormat.  # noqa: E501
        :type: str
        """
        if material is not None:
            allowed_values = ["Clear", "DkEdge", "Flat", "LegacyMatte", "LegacyMetal", "LegacyPlastic", "LegacyWireframe", "Matte", "Metal", "Plastic", "Powder", "SoftEdge", "Softmetal", "TranslucentPowder", "WarmMatte", "NotDefined"]  # noqa: E501
            if material.isdigit():
                int_material = int(material)
                if int_material < 0 or int_material >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `material` ({0}), must be one of {1}"  # noqa: E501
                        .format(material, allowed_values)
                    )
                self._material = allowed_values[int_material]
                return
            if material not in allowed_values:
                raise ValueError(
                    "Invalid value for `material` ({0}), must be one of {1}"  # noqa: E501
                    .format(material, allowed_values)
                )
        self._material = material

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
        if not isinstance(other, ThreeDFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
