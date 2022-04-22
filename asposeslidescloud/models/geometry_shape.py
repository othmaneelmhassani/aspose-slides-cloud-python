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

class GeometryShape(ShapeBase):


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
        'shape_type': 'str'
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
        'shape_type': 'shapeType'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, width=None, height=None, alternative_text=None, alternative_text_title=None, hidden=None, x=None, y=None, z_order_position=None, fill_format=None, effect_format=None, three_d_format=None, line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, type=None, shape_type=None):  # noqa: E501
        """GeometryShape - a model defined in Swagger"""  # noqa: E501
        super(GeometryShape, self).__init__(self_uri, alternate_links, name, width, height, alternative_text, alternative_text_title, hidden, x, y, z_order_position, fill_format, effect_format, three_d_format, line_format, hyperlink_click, hyperlink_mouse_over, type)

        self._shape_type = None

        self.shape_type = shape_type

    @property
    def shape_type(self):
        """Gets the shape_type of this GeometryShape.  # noqa: E501

        Combined shape type.  # noqa: E501

        :return: The shape_type of this GeometryShape.  # noqa: E501
        :rtype: str
        """
        return self._shape_type

    @shape_type.setter
    def shape_type(self, shape_type):
        """Sets the shape_type of this GeometryShape.

        Combined shape type.  # noqa: E501

        :param shape_type: The shape_type of this GeometryShape.  # noqa: E501
        :type: str
        """
        if shape_type is not None:
            allowed_values = ["Custom", "Line", "LineInverse", "Triangle", "RightTriangle", "Rectangle", "Diamond", "Parallelogram", "Trapezoid", "NonIsoscelesTrapezoid", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Decagon", "Dodecagon", "FourPointedStar", "FivePointedStar", "SixPointedStar", "SevenPointedStar", "EightPointedStar", "TenPointedStar", "TwelvePointedStar", "SixteenPointedStar", "TwentyFourPointedStar", "ThirtyTwoPointedStar", "RoundCornerRectangle", "OneRoundCornerRectangle", "TwoSamesideRoundCornerRectangle", "TwoDiagonalRoundCornerRectangle", "OneSnipOneRoundCornerRectangle", "OneSnipCornerRectangle", "TwoSamesideSnipCornerRectangle", "TwoDiagonalSnipCornerRectangle", "Plaque", "Ellipse", "Teardrop", "HomePlate", "Chevron", "PieWedge", "Pie", "BlockArc", "Donut", "NoSmoking", "RightArrow", "LeftArrow", "UpArrow", "DownArrow", "StripedRightArrow", "NotchedRightArrow", "BentUpArrow", "LeftRightArrow", "UpDownArrow", "LeftUpArrow", "LeftRightUpArrow", "QuadArrow", "CalloutLeftArrow", "CalloutRightArrow", "CalloutUpArrow", "CalloutDownArrow", "CalloutLeftRightArrow", "CalloutUpDownArrow", "CalloutQuadArrow", "BentArrow", "UTurnArrow", "CircularArrow", "LeftCircularArrow", "LeftRightCircularArrow", "CurvedRightArrow", "CurvedLeftArrow", "CurvedUpArrow", "CurvedDownArrow", "SwooshArrow", "Cube", "Can", "LightningBolt", "Heart", "Sun", "Moon", "SmileyFace", "IrregularSeal1", "IrregularSeal2", "FoldedCorner", "Bevel", "Frame", "HalfFrame", "Corner", "DiagonalStripe", "Chord", "CurvedArc", "LeftBracket", "RightBracket", "LeftBrace", "RightBrace", "BracketPair", "BracePair", "StraightConnector1", "BentConnector2", "BentConnector3", "BentConnector4", "BentConnector5", "CurvedConnector2", "CurvedConnector3", "CurvedConnector4", "CurvedConnector5", "Callout1", "Callout2", "Callout3", "Callout1WithAccent", "Callout2WithAccent", "Callout3WithAccent", "Callout1WithBorder", "Callout2WithBorder", "Callout3WithBorder", "Callout1WithBorderAndAccent", "Callout2WithBorderAndAccent", "Callout3WithBorderAndAccent", "CalloutWedgeRectangle", "CalloutWedgeRoundRectangle", "CalloutWedgeEllipse", "CalloutCloud", "Cloud", "Ribbon", "Ribbon2", "EllipseRibbon", "EllipseRibbon2", "LeftRightRibbon", "VerticalScroll", "HorizontalScroll", "Wave", "DoubleWave", "Plus", "ProcessFlow", "DecisionFlow", "InputOutputFlow", "PredefinedProcessFlow", "InternalStorageFlow", "DocumentFlow", "MultiDocumentFlow", "TerminatorFlow", "PreparationFlow", "ManualInputFlow", "ManualOperationFlow", "ConnectorFlow", "PunchedCardFlow", "PunchedTapeFlow", "SummingJunctionFlow", "OrFlow", "CollateFlow", "SortFlow", "ExtractFlow", "MergeFlow", "OfflineStorageFlow", "OnlineStorageFlow", "MagneticTapeFlow", "MagneticDiskFlow", "MagneticDrumFlow", "DisplayFlow", "DelayFlow", "AlternateProcessFlow", "OffPageConnectorFlow", "BlankButton", "HomeButton", "HelpButton", "InformationButton", "ForwardOrNextButton", "BackOrPreviousButton", "EndButton", "BeginningButton", "ReturnButton", "DocumentButton", "SoundButton", "MovieButton", "Gear6", "Gear9", "Funnel", "PlusMath", "MinusMath", "MultiplyMath", "DivideMath", "EqualMath", "NotEqualMath", "CornerTabs", "SquareTabs", "PlaqueTabs", "ChartX", "ChartStar", "ChartPlus", "NotDefined"]  # noqa: E501
            if shape_type.isdigit():
                int_shape_type = int(shape_type)
                if int_shape_type < 0 or int_shape_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `shape_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(shape_type, allowed_values)
                    )
                self._shape_type = allowed_values[int_shape_type]
                return
            if shape_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `shape_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(shape_type, allowed_values)
                )
        self._shape_type = shape_type

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
        if not isinstance(other, GeometryShape):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
