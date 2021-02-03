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

class ProtectionProperties(ResourceBase):


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
        'encrypt_document_properties': 'bool',
        'read_only_recommended': 'bool'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'encrypt_document_properties': 'encryptDocumentProperties',
        'read_only_recommended': 'readOnlyRecommended'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, encrypt_document_properties=None, read_only_recommended=None):  # noqa: E501
        """ProtectionProperties - a model defined in Swagger"""  # noqa: E501
        super(ProtectionProperties, self).__init__(self_uri, alternate_links)

        self._encrypt_document_properties = None
        self._read_only_recommended = None

        if encrypt_document_properties is not None:
            self.encrypt_document_properties = encrypt_document_properties
        if read_only_recommended is not None:
            self.read_only_recommended = read_only_recommended

    @property
    def encrypt_document_properties(self):
        """Gets the encrypt_document_properties of this ProtectionProperties.  # noqa: E501

        True if document properties are encrypted. Has effect only for password protected presentations.  # noqa: E501

        :return: The encrypt_document_properties of this ProtectionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt_document_properties

    @encrypt_document_properties.setter
    def encrypt_document_properties(self, encrypt_document_properties):
        """Sets the encrypt_document_properties of this ProtectionProperties.

        True if document properties are encrypted. Has effect only for password protected presentations.  # noqa: E501

        :param encrypt_document_properties: The encrypt_document_properties of this ProtectionProperties.  # noqa: E501
        :type: bool
        """
        self._encrypt_document_properties = encrypt_document_properties

    @property
    def read_only_recommended(self):
        """Gets the read_only_recommended of this ProtectionProperties.  # noqa: E501

        True if the document should be opened as read-only.  # noqa: E501

        :return: The read_only_recommended of this ProtectionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_recommended

    @read_only_recommended.setter
    def read_only_recommended(self, read_only_recommended):
        """Sets the read_only_recommended of this ProtectionProperties.

        True if the document should be opened as read-only.  # noqa: E501

        :param read_only_recommended: The read_only_recommended of this ProtectionProperties.  # noqa: E501
        :type: bool
        """
        self._read_only_recommended = read_only_recommended

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
        if not isinstance(other, ProtectionProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
