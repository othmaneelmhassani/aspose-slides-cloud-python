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
        'read_only_recommended': 'bool',
        'read_password': 'str',
        'write_password': 'str',
        'is_write_protected': 'bool',
        'is_encrypted': 'bool'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'encrypt_document_properties': 'encryptDocumentProperties',
        'read_only_recommended': 'readOnlyRecommended',
        'read_password': 'readPassword',
        'write_password': 'writePassword',
        'is_write_protected': 'isWriteProtected',
        'is_encrypted': 'isEncrypted'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, encrypt_document_properties=None, read_only_recommended=None, read_password=None, write_password=None, is_write_protected=None, is_encrypted=None):  # noqa: E501
        """ProtectionProperties - a model defined in Swagger"""  # noqa: E501
        super(ProtectionProperties, self).__init__(self_uri, alternate_links)

        self._encrypt_document_properties = None
        self._read_only_recommended = None
        self._read_password = None
        self._write_password = None
        self._is_write_protected = None
        self._is_encrypted = None

        if encrypt_document_properties is not None:
            self.encrypt_document_properties = encrypt_document_properties
        if read_only_recommended is not None:
            self.read_only_recommended = read_only_recommended
        if read_password is not None:
            self.read_password = read_password
        if write_password is not None:
            self.write_password = write_password
        self.is_write_protected = is_write_protected
        self.is_encrypted = is_encrypted

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

    @property
    def read_password(self):
        """Gets the read_password of this ProtectionProperties.  # noqa: E501

        Password for read protection.  # noqa: E501

        :return: The read_password of this ProtectionProperties.  # noqa: E501
        :rtype: str
        """
        return self._read_password

    @read_password.setter
    def read_password(self, read_password):
        """Sets the read_password of this ProtectionProperties.

        Password for read protection.  # noqa: E501

        :param read_password: The read_password of this ProtectionProperties.  # noqa: E501
        :type: str
        """
        self._read_password = read_password

    @property
    def write_password(self):
        """Gets the write_password of this ProtectionProperties.  # noqa: E501

        Password for write protection.  # noqa: E501

        :return: The write_password of this ProtectionProperties.  # noqa: E501
        :rtype: str
        """
        return self._write_password

    @write_password.setter
    def write_password(self, write_password):
        """Sets the write_password of this ProtectionProperties.

        Password for write protection.  # noqa: E501

        :param write_password: The write_password of this ProtectionProperties.  # noqa: E501
        :type: str
        """
        self._write_password = write_password

    @property
    def is_write_protected(self):
        """Gets the is_write_protected of this ProtectionProperties.  # noqa: E501

        Returns true if the presentation protected for editing.   # noqa: E501

        :return: The is_write_protected of this ProtectionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._is_write_protected

    @is_write_protected.setter
    def is_write_protected(self, is_write_protected):
        """Sets the is_write_protected of this ProtectionProperties.

        Returns true if the presentation protected for editing.   # noqa: E501

        :param is_write_protected: The is_write_protected of this ProtectionProperties.  # noqa: E501
        :type: bool
        """
        self._is_write_protected = is_write_protected

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this ProtectionProperties.  # noqa: E501

        Returns true if the presentation protected for reading.   # noqa: E501

        :return: The is_encrypted of this ProtectionProperties.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this ProtectionProperties.

        Returns true if the presentation protected for reading.   # noqa: E501

        :param is_encrypted: The is_encrypted of this ProtectionProperties.  # noqa: E501
        :type: bool
        """
        self._is_encrypted = is_encrypted

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
