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


class AccessPermissions(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'print_document': 'bool',
        'modify_content': 'bool',
        'copy_text_and_graphics': 'bool',
        'add_or_modify_fields': 'bool',
        'fill_existing_fields': 'bool',
        'extract_text_and_graphics': 'bool',
        'assemble_document': 'bool',
        'high_quality_print': 'bool'
    }

    attribute_map = {
        'print_document': 'printDocument',
        'modify_content': 'modifyContent',
        'copy_text_and_graphics': 'copyTextAndGraphics',
        'add_or_modify_fields': 'addOrModifyFields',
        'fill_existing_fields': 'fillExistingFields',
        'extract_text_and_graphics': 'extractTextAndGraphics',
        'assemble_document': 'assembleDocument',
        'high_quality_print': 'highQualityPrint'
    }

    type_determiners = {
    }

    def __init__(self, print_document=None, modify_content=None, copy_text_and_graphics=None, add_or_modify_fields=None, fill_existing_fields=None, extract_text_and_graphics=None, assemble_document=None, high_quality_print=None):  # noqa: E501
        """AccessPermissions - a model defined in Swagger"""  # noqa: E501

        self._print_document = None
        self._modify_content = None
        self._copy_text_and_graphics = None
        self._add_or_modify_fields = None
        self._fill_existing_fields = None
        self._extract_text_and_graphics = None
        self._assemble_document = None
        self._high_quality_print = None

        self.print_document = print_document
        self.modify_content = modify_content
        self.copy_text_and_graphics = copy_text_and_graphics
        self.add_or_modify_fields = add_or_modify_fields
        self.fill_existing_fields = fill_existing_fields
        self.extract_text_and_graphics = extract_text_and_graphics
        self.assemble_document = assemble_document
        self.high_quality_print = high_quality_print

    @property
    def print_document(self):
        """Gets the print_document of this AccessPermissions.  # noqa: E501

        The user may print the document (possibly not at the highest quality level, depending on whether bit HighQualityPrint is also set).  # noqa: E501

        :return: The print_document of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._print_document

    @print_document.setter
    def print_document(self, print_document):
        """Sets the print_document of this AccessPermissions.

        The user may print the document (possibly not at the highest quality level, depending on whether bit HighQualityPrint is also set).  # noqa: E501

        :param print_document: The print_document of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._print_document = print_document

    @property
    def modify_content(self):
        """Gets the modify_content of this AccessPermissions.  # noqa: E501

        The user may modify the contents of the document by operations other than those controlled by bits AddOrModifyFields, FillExistingFields, AssembleDocument.  # noqa: E501

        :return: The modify_content of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._modify_content

    @modify_content.setter
    def modify_content(self, modify_content):
        """Sets the modify_content of this AccessPermissions.

        The user may modify the contents of the document by operations other than those controlled by bits AddOrModifyFields, FillExistingFields, AssembleDocument.  # noqa: E501

        :param modify_content: The modify_content of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._modify_content = modify_content

    @property
    def copy_text_and_graphics(self):
        """Gets the copy_text_and_graphics of this AccessPermissions.  # noqa: E501

        The user may copy or otherwise extract text and graphics from the document by operations other than that controlled by bit ExtractTextAndGraphics.  # noqa: E501

        :return: The copy_text_and_graphics of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._copy_text_and_graphics

    @copy_text_and_graphics.setter
    def copy_text_and_graphics(self, copy_text_and_graphics):
        """Sets the copy_text_and_graphics of this AccessPermissions.

        The user may copy or otherwise extract text and graphics from the document by operations other than that controlled by bit ExtractTextAndGraphics.  # noqa: E501

        :param copy_text_and_graphics: The copy_text_and_graphics of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._copy_text_and_graphics = copy_text_and_graphics

    @property
    def add_or_modify_fields(self):
        """Gets the add_or_modify_fields of this AccessPermissions.  # noqa: E501

        The user may add or modify text annotations, fill in interactive form fields, and, if bit ModifyContent is also set, create or modify interactive form fields (including signature fields).  # noqa: E501

        :return: The add_or_modify_fields of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._add_or_modify_fields

    @add_or_modify_fields.setter
    def add_or_modify_fields(self, add_or_modify_fields):
        """Sets the add_or_modify_fields of this AccessPermissions.

        The user may add or modify text annotations, fill in interactive form fields, and, if bit ModifyContent is also set, create or modify interactive form fields (including signature fields).  # noqa: E501

        :param add_or_modify_fields: The add_or_modify_fields of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._add_or_modify_fields = add_or_modify_fields

    @property
    def fill_existing_fields(self):
        """Gets the fill_existing_fields of this AccessPermissions.  # noqa: E501

        The user may fill in existing interactive form fields (including signature fields), even if bit AddOrModifyFields is clear.  # noqa: E501

        :return: The fill_existing_fields of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._fill_existing_fields

    @fill_existing_fields.setter
    def fill_existing_fields(self, fill_existing_fields):
        """Sets the fill_existing_fields of this AccessPermissions.

        The user may fill in existing interactive form fields (including signature fields), even if bit AddOrModifyFields is clear.  # noqa: E501

        :param fill_existing_fields: The fill_existing_fields of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._fill_existing_fields = fill_existing_fields

    @property
    def extract_text_and_graphics(self):
        """Gets the extract_text_and_graphics of this AccessPermissions.  # noqa: E501

        The user may extract text and graphics in support of accessibility to users with disabilities or for other purposes.  # noqa: E501

        :return: The extract_text_and_graphics of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._extract_text_and_graphics

    @extract_text_and_graphics.setter
    def extract_text_and_graphics(self, extract_text_and_graphics):
        """Sets the extract_text_and_graphics of this AccessPermissions.

        The user may extract text and graphics in support of accessibility to users with disabilities or for other purposes.  # noqa: E501

        :param extract_text_and_graphics: The extract_text_and_graphics of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._extract_text_and_graphics = extract_text_and_graphics

    @property
    def assemble_document(self):
        """Gets the assemble_document of this AccessPermissions.  # noqa: E501

        The user may assemble the document (insert, rotate, or delete pages and create bookmarks or thumbnail images), even if bit ModifyContent is clear.  # noqa: E501

        :return: The assemble_document of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._assemble_document

    @assemble_document.setter
    def assemble_document(self, assemble_document):
        """Sets the assemble_document of this AccessPermissions.

        The user may assemble the document (insert, rotate, or delete pages and create bookmarks or thumbnail images), even if bit ModifyContent is clear.  # noqa: E501

        :param assemble_document: The assemble_document of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._assemble_document = assemble_document

    @property
    def high_quality_print(self):
        """Gets the high_quality_print of this AccessPermissions.  # noqa: E501

        The user may print the document to a representation from which a faithful digital copy of the PDF content could be generated. When this bit is clear (and bit PrintDocument is set), printing is limited to a low-level representation of the appearance, possibly of degraded quality.  # noqa: E501

        :return: The high_quality_print of this AccessPermissions.  # noqa: E501
        :rtype: bool
        """
        return self._high_quality_print

    @high_quality_print.setter
    def high_quality_print(self, high_quality_print):
        """Sets the high_quality_print of this AccessPermissions.

        The user may print the document to a representation from which a faithful digital copy of the PDF content could be generated. When this bit is clear (and bit PrintDocument is set), printing is limited to a low-level representation of the appearance, possibly of degraded quality.  # noqa: E501

        :param high_quality_print: The high_quality_print of this AccessPermissions.  # noqa: E501
        :type: bool
        """
        self._high_quality_print = high_quality_print

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
        if not isinstance(other, AccessPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
