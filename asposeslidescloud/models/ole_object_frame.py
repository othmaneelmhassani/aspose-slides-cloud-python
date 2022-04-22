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

from asposeslidescloud.models.shape_base import ShapeBase

class OleObjectFrame(ShapeBase):


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
        'type': 'str',
        'is_object_icon': 'bool',
        'substitute_picture_title': 'str',
        'substitute_picture_format': 'PictureFill',
        'object_name': 'str',
        'embedded_file_base64_data': 'str',
        'embedded_file_extension': 'str',
        'object_prog_id': 'str',
        'link_path': 'str',
        'update_automatic': 'bool'
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
        'type': 'type',
        'is_object_icon': 'isObjectIcon',
        'substitute_picture_title': 'substitutePictureTitle',
        'substitute_picture_format': 'substitutePictureFormat',
        'object_name': 'objectName',
        'embedded_file_base64_data': 'embeddedFileBase64Data',
        'embedded_file_extension': 'embeddedFileExtension',
        'object_prog_id': 'objectProgId',
        'link_path': 'linkPath',
        'update_automatic': 'updateAutomatic'
    }

    type_determiners = {
        'type': 'OleObjectFrame',
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, width=None, height=None, alternative_text=None, alternative_text_title=None, hidden=None, x=None, y=None, z_order_position=None, fill_format=None, effect_format=None, three_d_format=None, line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, type='OleObjectFrame', is_object_icon=None, substitute_picture_title=None, substitute_picture_format=None, object_name=None, embedded_file_base64_data=None, embedded_file_extension=None, object_prog_id=None, link_path=None, update_automatic=None):  # noqa: E501
        """OleObjectFrame - a model defined in Swagger"""  # noqa: E501
        super(OleObjectFrame, self).__init__(self_uri, alternate_links, name, width, height, alternative_text, alternative_text_title, hidden, x, y, z_order_position, fill_format, effect_format, three_d_format, line_format, hyperlink_click, hyperlink_mouse_over, type)

        self._is_object_icon = None
        self._substitute_picture_title = None
        self._substitute_picture_format = None
        self._object_name = None
        self._embedded_file_base64_data = None
        self._embedded_file_extension = None
        self._object_prog_id = None
        self._link_path = None
        self._update_automatic = None
        self.type = 'OleObjectFrame'

        self.is_object_icon = is_object_icon
        if substitute_picture_title is not None:
            self.substitute_picture_title = substitute_picture_title
        if substitute_picture_format is not None:
            self.substitute_picture_format = substitute_picture_format
        if object_name is not None:
            self.object_name = object_name
        if embedded_file_base64_data is not None:
            self.embedded_file_base64_data = embedded_file_base64_data
        if embedded_file_extension is not None:
            self.embedded_file_extension = embedded_file_extension
        if object_prog_id is not None:
            self.object_prog_id = object_prog_id
        if link_path is not None:
            self.link_path = link_path
        if update_automatic is not None:
            self.update_automatic = update_automatic

    @property
    def is_object_icon(self):
        """Gets the is_object_icon of this OleObjectFrame.  # noqa: E501

        True if an object is visible as icon.  # noqa: E501

        :return: The is_object_icon of this OleObjectFrame.  # noqa: E501
        :rtype: bool
        """
        return self._is_object_icon

    @is_object_icon.setter
    def is_object_icon(self, is_object_icon):
        """Sets the is_object_icon of this OleObjectFrame.

        True if an object is visible as icon.  # noqa: E501

        :param is_object_icon: The is_object_icon of this OleObjectFrame.  # noqa: E501
        :type: bool
        """
        self._is_object_icon = is_object_icon

    @property
    def substitute_picture_title(self):
        """Gets the substitute_picture_title of this OleObjectFrame.  # noqa: E501

        The title for OleObject icon.               # noqa: E501

        :return: The substitute_picture_title of this OleObjectFrame.  # noqa: E501
        :rtype: str
        """
        return self._substitute_picture_title

    @substitute_picture_title.setter
    def substitute_picture_title(self, substitute_picture_title):
        """Sets the substitute_picture_title of this OleObjectFrame.

        The title for OleObject icon.               # noqa: E501

        :param substitute_picture_title: The substitute_picture_title of this OleObjectFrame.  # noqa: E501
        :type: str
        """
        self._substitute_picture_title = substitute_picture_title

    @property
    def substitute_picture_format(self):
        """Gets the substitute_picture_format of this OleObjectFrame.  # noqa: E501

        OleObject image fill properties.  # noqa: E501

        :return: The substitute_picture_format of this OleObjectFrame.  # noqa: E501
        :rtype: PictureFill
        """
        return self._substitute_picture_format

    @substitute_picture_format.setter
    def substitute_picture_format(self, substitute_picture_format):
        """Sets the substitute_picture_format of this OleObjectFrame.

        OleObject image fill properties.  # noqa: E501

        :param substitute_picture_format: The substitute_picture_format of this OleObjectFrame.  # noqa: E501
        :type: PictureFill
        """
        self._substitute_picture_format = substitute_picture_format

    @property
    def object_name(self):
        """Gets the object_name of this OleObjectFrame.  # noqa: E501

        Returns or sets the name of an object.  # noqa: E501

        :return: The object_name of this OleObjectFrame.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this OleObjectFrame.

        Returns or sets the name of an object.  # noqa: E501

        :param object_name: The object_name of this OleObjectFrame.  # noqa: E501
        :type: str
        """
        self._object_name = object_name

    @property
    def embedded_file_base64_data(self):
        """Gets the embedded_file_base64_data of this OleObjectFrame.  # noqa: E501

        File data of embedded OLE object.   # noqa: E501

        :return: The embedded_file_base64_data of this OleObjectFrame.  # noqa: E501
        :rtype: str
        """
        return self._embedded_file_base64_data

    @embedded_file_base64_data.setter
    def embedded_file_base64_data(self, embedded_file_base64_data):
        """Sets the embedded_file_base64_data of this OleObjectFrame.

        File data of embedded OLE object.   # noqa: E501

        :param embedded_file_base64_data: The embedded_file_base64_data of this OleObjectFrame.  # noqa: E501
        :type: str
        """
        self._embedded_file_base64_data = embedded_file_base64_data

    @property
    def embedded_file_extension(self):
        """Gets the embedded_file_extension of this OleObjectFrame.  # noqa: E501

        File extension for the current embedded OLE object  # noqa: E501

        :return: The embedded_file_extension of this OleObjectFrame.  # noqa: E501
        :rtype: str
        """
        return self._embedded_file_extension

    @embedded_file_extension.setter
    def embedded_file_extension(self, embedded_file_extension):
        """Sets the embedded_file_extension of this OleObjectFrame.

        File extension for the current embedded OLE object  # noqa: E501

        :param embedded_file_extension: The embedded_file_extension of this OleObjectFrame.  # noqa: E501
        :type: str
        """
        self._embedded_file_extension = embedded_file_extension

    @property
    def object_prog_id(self):
        """Gets the object_prog_id of this OleObjectFrame.  # noqa: E501

        ProgID of an object.  # noqa: E501

        :return: The object_prog_id of this OleObjectFrame.  # noqa: E501
        :rtype: str
        """
        return self._object_prog_id

    @object_prog_id.setter
    def object_prog_id(self, object_prog_id):
        """Sets the object_prog_id of this OleObjectFrame.

        ProgID of an object.  # noqa: E501

        :param object_prog_id: The object_prog_id of this OleObjectFrame.  # noqa: E501
        :type: str
        """
        self._object_prog_id = object_prog_id

    @property
    def link_path(self):
        """Gets the link_path of this OleObjectFrame.  # noqa: E501

        Full path to a linked file.  # noqa: E501

        :return: The link_path of this OleObjectFrame.  # noqa: E501
        :rtype: str
        """
        return self._link_path

    @link_path.setter
    def link_path(self, link_path):
        """Sets the link_path of this OleObjectFrame.

        Full path to a linked file.  # noqa: E501

        :param link_path: The link_path of this OleObjectFrame.  # noqa: E501
        :type: str
        """
        self._link_path = link_path

    @property
    def update_automatic(self):
        """Gets the update_automatic of this OleObjectFrame.  # noqa: E501

        Determines if the linked embedded object is automatically updated when the presentation is opened or printed. Read/write Boolean.  # noqa: E501

        :return: The update_automatic of this OleObjectFrame.  # noqa: E501
        :rtype: bool
        """
        return self._update_automatic

    @update_automatic.setter
    def update_automatic(self, update_automatic):
        """Sets the update_automatic of this OleObjectFrame.

        Determines if the linked embedded object is automatically updated when the presentation is opened or printed. Read/write Boolean.  # noqa: E501

        :param update_automatic: The update_automatic of this OleObjectFrame.  # noqa: E501
        :type: bool
        """
        self._update_automatic = update_automatic

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
        if not isinstance(other, OleObjectFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
