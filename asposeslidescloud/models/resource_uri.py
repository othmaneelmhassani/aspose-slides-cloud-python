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


class ResourceUri(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'relation': 'str',
        'link_type': 'str',
        'title': 'str',
        'slide_index': 'int',
        'shape_index': 'int'
    }

    attribute_map = {
        'href': 'href',
        'relation': 'relation',
        'link_type': 'linkType',
        'title': 'title',
        'slide_index': 'slideIndex',
        'shape_index': 'shapeIndex'
    }

    type_determiners = {
    }

    def __init__(self, href=None, relation=None, link_type=None, title=None, slide_index=None, shape_index=None):  # noqa: E501
        """ResourceUri - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._relation = None
        self._link_type = None
        self._title = None
        self._slide_index = None
        self._shape_index = None

        if href is not None:
            self.href = href
        if relation is not None:
            self.relation = relation
        if link_type is not None:
            self.link_type = link_type
        if title is not None:
            self.title = title
        if slide_index is not None:
            self.slide_index = slide_index
        if shape_index is not None:
            self.shape_index = shape_index

    @property
    def href(self):
        """Gets the href of this ResourceUri.  # noqa: E501

        Gets or sets the href.  # noqa: E501

        :return: The href of this ResourceUri.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ResourceUri.

        Gets or sets the href.  # noqa: E501

        :param href: The href of this ResourceUri.  # noqa: E501
        :type: str
        """
        self._href = href

    @property
    def relation(self):
        """Gets the relation of this ResourceUri.  # noqa: E501

        Gets or sets the relation.  # noqa: E501

        :return: The relation of this ResourceUri.  # noqa: E501
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this ResourceUri.

        Gets or sets the relation.  # noqa: E501

        :param relation: The relation of this ResourceUri.  # noqa: E501
        :type: str
        """
        self._relation = relation

    @property
    def link_type(self):
        """Gets the link_type of this ResourceUri.  # noqa: E501

        Gets or sets the type of link.  # noqa: E501

        :return: The link_type of this ResourceUri.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this ResourceUri.

        Gets or sets the type of link.  # noqa: E501

        :param link_type: The link_type of this ResourceUri.  # noqa: E501
        :type: str
        """
        self._link_type = link_type

    @property
    def title(self):
        """Gets the title of this ResourceUri.  # noqa: E501

        Gets or sets the title of link.  # noqa: E501

        :return: The title of this ResourceUri.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResourceUri.

        Gets or sets the title of link.  # noqa: E501

        :param title: The title of this ResourceUri.  # noqa: E501
        :type: str
        """
        self._title = title

    @property
    def slide_index(self):
        """Gets the slide_index of this ResourceUri.  # noqa: E501

        Resource slide index.  # noqa: E501

        :return: The slide_index of this ResourceUri.  # noqa: E501
        :rtype: int
        """
        return self._slide_index

    @slide_index.setter
    def slide_index(self, slide_index):
        """Sets the slide_index of this ResourceUri.

        Resource slide index.  # noqa: E501

        :param slide_index: The slide_index of this ResourceUri.  # noqa: E501
        :type: int
        """
        self._slide_index = slide_index

    @property
    def shape_index(self):
        """Gets the shape_index of this ResourceUri.  # noqa: E501

        Resource shape index.  # noqa: E501

        :return: The shape_index of this ResourceUri.  # noqa: E501
        :rtype: int
        """
        return self._shape_index

    @shape_index.setter
    def shape_index(self, shape_index):
        """Sets the shape_index of this ResourceUri.

        Resource shape index.  # noqa: E501

        :param shape_index: The shape_index of this ResourceUri.  # noqa: E501
        :type: int
        """
        self._shape_index = shape_index

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
        if not isinstance(other, ResourceUri):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
