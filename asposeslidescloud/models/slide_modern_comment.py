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

from asposeslidescloud.models.slide_comment_base import SlideCommentBase

class SlideModernComment(SlideCommentBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'author': 'str',
        'text': 'str',
        'created_time': 'str',
        'child_comments': 'list[SlideCommentBase]',
        'type': 'str',
        'text_selection_start': 'int',
        'text_selection_length': 'int',
        'status': 'str'
    }

    attribute_map = {
        'author': 'author',
        'text': 'text',
        'created_time': 'createdTime',
        'child_comments': 'childComments',
        'type': 'type',
        'text_selection_start': 'textSelectionStart',
        'text_selection_length': 'textSelectionLength',
        'status': 'status'
    }

    type_determiners = {
        'type': 'Modern',
    }

    def __init__(self, author=None, text=None, created_time=None, child_comments=None, type='Modern', text_selection_start=None, text_selection_length=None, status=None):  # noqa: E501
        """SlideModernComment - a model defined in Swagger"""  # noqa: E501
        super(SlideModernComment, self).__init__(author, text, created_time, child_comments, type)

        self._text_selection_start = None
        self._text_selection_length = None
        self._status = None
        self.type = 'Modern'

        if text_selection_start is not None:
            self.text_selection_start = text_selection_start
        if text_selection_length is not None:
            self.text_selection_length = text_selection_length
        if status is not None:
            self.status = status

    @property
    def text_selection_start(self):
        """Gets the text_selection_start of this SlideModernComment.  # noqa: E501

        Returns or sets starting position of text selection in text frame if the comment associated with AutoShape. Read/write Int32.  # noqa: E501

        :return: The text_selection_start of this SlideModernComment.  # noqa: E501
        :rtype: int
        """
        return self._text_selection_start

    @text_selection_start.setter
    def text_selection_start(self, text_selection_start):
        """Sets the text_selection_start of this SlideModernComment.

        Returns or sets starting position of text selection in text frame if the comment associated with AutoShape. Read/write Int32.  # noqa: E501

        :param text_selection_start: The text_selection_start of this SlideModernComment.  # noqa: E501
        :type: int
        """
        self._text_selection_start = text_selection_start

    @property
    def text_selection_length(self):
        """Gets the text_selection_length of this SlideModernComment.  # noqa: E501

        Returns or sets text selection length in text frame if the comment associated with AutoShape. Read/write Int32.  # noqa: E501

        :return: The text_selection_length of this SlideModernComment.  # noqa: E501
        :rtype: int
        """
        return self._text_selection_length

    @text_selection_length.setter
    def text_selection_length(self, text_selection_length):
        """Sets the text_selection_length of this SlideModernComment.

        Returns or sets text selection length in text frame if the comment associated with AutoShape. Read/write Int32.  # noqa: E501

        :param text_selection_length: The text_selection_length of this SlideModernComment.  # noqa: E501
        :type: int
        """
        self._text_selection_length = text_selection_length

    @property
    def status(self):
        """Gets the status of this SlideModernComment.  # noqa: E501

        Returns or sets the status of the comment. Read/write ModernCommentStatus.  # noqa: E501

        :return: The status of this SlideModernComment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SlideModernComment.

        Returns or sets the status of the comment. Read/write ModernCommentStatus.  # noqa: E501

        :param status: The status of this SlideModernComment.  # noqa: E501
        :type: str
        """
        if status is not None:
            allowed_values = ["NotDefined", "Active", "Resolved", "Closed"]  # noqa: E501
            if status.isdigit():
                int_status = int(status)
                if int_status < 0 or int_status >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                        .format(status, allowed_values)
                    )
                self._status = allowed_values[int_status]
                return
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                    .format(status, allowed_values)
                )
        self._status = status

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
        if not isinstance(other, SlideModernComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
