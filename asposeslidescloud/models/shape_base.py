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

from asposeslidescloud.models.resource_base import ResourceBase

class ShapeBase(ResourceBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'self_uri': 'ResourceUri',
        'alternate_links': 'list[ResourceUri]',
        'name': 'str',
        'width': 'float',
        'height': 'float',
        'alternative_text': 'str',
        'alternative_text_title': 'str',
        'hidden': 'bool',
        'x': 'float',
        'y': 'float',
        'z_order_position': 'int',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'three_d_format': 'ThreeDFormat',
        'line_format': 'LineFormat',
        'hyperlink_click': 'Hyperlink',
        'hyperlink_mouse_over': 'Hyperlink',
        'type': 'str'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'name': 'name',
        'width': 'width',
        'height': 'height',
        'alternative_text': 'alternativeText',
        'alternative_text_title': 'alternativeTextTitle',
        'hidden': 'hidden',
        'x': 'x',
        'y': 'y',
        'z_order_position': 'zOrderPosition',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'three_d_format': 'threeDFormat',
        'line_format': 'lineFormat',
        'hyperlink_click': 'hyperlinkClick',
        'hyperlink_mouse_over': 'hyperlinkMouseOver',
        'type': 'type'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, width=None, height=None, alternative_text=None, alternative_text_title=None, hidden=None, x=None, y=None, z_order_position=None, fill_format=None, effect_format=None, three_d_format=None, line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, type=None):  # noqa: E501
        """ShapeBase - a model defined in Swagger"""  # noqa: E501
        super(ShapeBase, self).__init__(self_uri, alternate_links)

        self._name = None
        self._width = None
        self._height = None
        self._alternative_text = None
        self._alternative_text_title = None
        self._hidden = None
        self._x = None
        self._y = None
        self._z_order_position = None
        self._fill_format = None
        self._effect_format = None
        self._three_d_format = None
        self._line_format = None
        self._hyperlink_click = None
        self._hyperlink_mouse_over = None
        self._type = None

        if name is not None:
            self.name = name
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if alternative_text is not None:
            self.alternative_text = alternative_text
        if alternative_text_title is not None:
            self.alternative_text_title = alternative_text_title
        if hidden is not None:
            self.hidden = hidden
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        self.z_order_position = z_order_position
        if fill_format is not None:
            self.fill_format = fill_format
        if effect_format is not None:
            self.effect_format = effect_format
        if three_d_format is not None:
            self.three_d_format = three_d_format
        if line_format is not None:
            self.line_format = line_format
        if hyperlink_click is not None:
            self.hyperlink_click = hyperlink_click
        if hyperlink_mouse_over is not None:
            self.hyperlink_mouse_over = hyperlink_mouse_over
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this ShapeBase.  # noqa: E501

        Gets or sets the name.  # noqa: E501

        :return: The name of this ShapeBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShapeBase.

        Gets or sets the name.  # noqa: E501

        :param name: The name of this ShapeBase.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def width(self):
        """Gets the width of this ShapeBase.  # noqa: E501

        Gets or sets the width.  # noqa: E501

        :return: The width of this ShapeBase.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ShapeBase.

        Gets or sets the width.  # noqa: E501

        :param width: The width of this ShapeBase.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ShapeBase.  # noqa: E501

        Gets or sets the height.  # noqa: E501

        :return: The height of this ShapeBase.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ShapeBase.

        Gets or sets the height.  # noqa: E501

        :param height: The height of this ShapeBase.  # noqa: E501
        :type: float
        """
        self._height = height

    @property
    def alternative_text(self):
        """Gets the alternative_text of this ShapeBase.  # noqa: E501

        Gets or sets the alternative text.  # noqa: E501

        :return: The alternative_text of this ShapeBase.  # noqa: E501
        :rtype: str
        """
        return self._alternative_text

    @alternative_text.setter
    def alternative_text(self, alternative_text):
        """Sets the alternative_text of this ShapeBase.

        Gets or sets the alternative text.  # noqa: E501

        :param alternative_text: The alternative_text of this ShapeBase.  # noqa: E501
        :type: str
        """
        self._alternative_text = alternative_text

    @property
    def alternative_text_title(self):
        """Gets the alternative_text_title of this ShapeBase.  # noqa: E501

        The title of alternative text associated with the shape.  # noqa: E501

        :return: The alternative_text_title of this ShapeBase.  # noqa: E501
        :rtype: str
        """
        return self._alternative_text_title

    @alternative_text_title.setter
    def alternative_text_title(self, alternative_text_title):
        """Sets the alternative_text_title of this ShapeBase.

        The title of alternative text associated with the shape.  # noqa: E501

        :param alternative_text_title: The alternative_text_title of this ShapeBase.  # noqa: E501
        :type: str
        """
        self._alternative_text_title = alternative_text_title

    @property
    def hidden(self):
        """Gets the hidden of this ShapeBase.  # noqa: E501

        Gets or sets a value indicating whether this ShapeBase is hidden.  # noqa: E501

        :return: The hidden of this ShapeBase.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ShapeBase.

        Gets or sets a value indicating whether this ShapeBase is hidden.  # noqa: E501

        :param hidden: The hidden of this ShapeBase.  # noqa: E501
        :type: bool
        """
        self._hidden = hidden

    @property
    def x(self):
        """Gets the x of this ShapeBase.  # noqa: E501

        Gets or sets the X  # noqa: E501

        :return: The x of this ShapeBase.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ShapeBase.

        Gets or sets the X  # noqa: E501

        :param x: The x of this ShapeBase.  # noqa: E501
        :type: float
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this ShapeBase.  # noqa: E501

        Gets or sets the Y.  # noqa: E501

        :return: The y of this ShapeBase.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ShapeBase.

        Gets or sets the Y.  # noqa: E501

        :param y: The y of this ShapeBase.  # noqa: E501
        :type: float
        """
        self._y = y

    @property
    def z_order_position(self):
        """Gets the z_order_position of this ShapeBase.  # noqa: E501

        Gets z-order position of shape  # noqa: E501

        :return: The z_order_position of this ShapeBase.  # noqa: E501
        :rtype: int
        """
        return self._z_order_position

    @z_order_position.setter
    def z_order_position(self, z_order_position):
        """Sets the z_order_position of this ShapeBase.

        Gets z-order position of shape  # noqa: E501

        :param z_order_position: The z_order_position of this ShapeBase.  # noqa: E501
        :type: int
        """
        self._z_order_position = z_order_position

    @property
    def fill_format(self):
        """Gets the fill_format of this ShapeBase.  # noqa: E501

        Gets or sets the fill format.  # noqa: E501

        :return: The fill_format of this ShapeBase.  # noqa: E501
        :rtype: FillFormat
        """
        return self._fill_format

    @fill_format.setter
    def fill_format(self, fill_format):
        """Sets the fill_format of this ShapeBase.

        Gets or sets the fill format.  # noqa: E501

        :param fill_format: The fill_format of this ShapeBase.  # noqa: E501
        :type: FillFormat
        """
        self._fill_format = fill_format

    @property
    def effect_format(self):
        """Gets the effect_format of this ShapeBase.  # noqa: E501

        Gets or sets the effect format.  # noqa: E501

        :return: The effect_format of this ShapeBase.  # noqa: E501
        :rtype: EffectFormat
        """
        return self._effect_format

    @effect_format.setter
    def effect_format(self, effect_format):
        """Sets the effect_format of this ShapeBase.

        Gets or sets the effect format.  # noqa: E501

        :param effect_format: The effect_format of this ShapeBase.  # noqa: E501
        :type: EffectFormat
        """
        self._effect_format = effect_format

    @property
    def three_d_format(self):
        """Gets the three_d_format of this ShapeBase.  # noqa: E501

        Gets or sets the 3D format  # noqa: E501

        :return: The three_d_format of this ShapeBase.  # noqa: E501
        :rtype: ThreeDFormat
        """
        return self._three_d_format

    @three_d_format.setter
    def three_d_format(self, three_d_format):
        """Sets the three_d_format of this ShapeBase.

        Gets or sets the 3D format  # noqa: E501

        :param three_d_format: The three_d_format of this ShapeBase.  # noqa: E501
        :type: ThreeDFormat
        """
        self._three_d_format = three_d_format

    @property
    def line_format(self):
        """Gets the line_format of this ShapeBase.  # noqa: E501

        Gets or sets the line format.  # noqa: E501

        :return: The line_format of this ShapeBase.  # noqa: E501
        :rtype: LineFormat
        """
        return self._line_format

    @line_format.setter
    def line_format(self, line_format):
        """Sets the line_format of this ShapeBase.

        Gets or sets the line format.  # noqa: E501

        :param line_format: The line_format of this ShapeBase.  # noqa: E501
        :type: LineFormat
        """
        self._line_format = line_format

    @property
    def hyperlink_click(self):
        """Gets the hyperlink_click of this ShapeBase.  # noqa: E501

        Hyperlink defined for mouse click.  # noqa: E501

        :return: The hyperlink_click of this ShapeBase.  # noqa: E501
        :rtype: Hyperlink
        """
        return self._hyperlink_click

    @hyperlink_click.setter
    def hyperlink_click(self, hyperlink_click):
        """Sets the hyperlink_click of this ShapeBase.

        Hyperlink defined for mouse click.  # noqa: E501

        :param hyperlink_click: The hyperlink_click of this ShapeBase.  # noqa: E501
        :type: Hyperlink
        """
        self._hyperlink_click = hyperlink_click

    @property
    def hyperlink_mouse_over(self):
        """Gets the hyperlink_mouse_over of this ShapeBase.  # noqa: E501

        Hyperlink defined for mouse over.  # noqa: E501

        :return: The hyperlink_mouse_over of this ShapeBase.  # noqa: E501
        :rtype: Hyperlink
        """
        return self._hyperlink_mouse_over

    @hyperlink_mouse_over.setter
    def hyperlink_mouse_over(self, hyperlink_mouse_over):
        """Sets the hyperlink_mouse_over of this ShapeBase.

        Hyperlink defined for mouse over.  # noqa: E501

        :param hyperlink_mouse_over: The hyperlink_mouse_over of this ShapeBase.  # noqa: E501
        :type: Hyperlink
        """
        self._hyperlink_mouse_over = hyperlink_mouse_over

    @property
    def type(self):
        """Gets the type of this ShapeBase.  # noqa: E501


        :return: The type of this ShapeBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShapeBase.


        :param type: The type of this ShapeBase.  # noqa: E501
        :type: str
        """
        if type is not None:
            allowed_values = ["Shape", "Chart", "Table", "PictureFrame", "VideoFrame", "AudioFrame", "SmartArt", "OleObjectFrame", "GroupShape", "GraphicalObject", "Connector", "SmartArtShape", "ZoomFrame", "SectionZoomFrame", "SummaryZoomFrame", "SummaryZoomSection"]  # noqa: E501
            if type.isdigit():
                int_type = int(type)
                if int_type < 0 or int_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                        .format(type, allowed_values)
                    )
                self._type = allowed_values[int_type]
                return
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values)
                )
        self._type = type

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
        if not isinstance(other, ShapeBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
