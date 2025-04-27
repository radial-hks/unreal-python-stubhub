## SlateColor Objects

```python
class SlateColor(StructBase)
```

A Slate color can be a directly specified value, or the color can be pulled from a WidgetStyle.

**C++ Source:**

- **Module**: SlateCore
- **File**: SlateColor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_use_rule`` (SlateColorStylingMode):  [Read-Write] The rule for which color to pick.
- ``specified_color`` (LinearColor):  [Read-Write] The current specified color; only meaningful when ColorToUse == UseColor_Specified.

<a id="unreal.SlateColor.__init__"></a>

#### __init__

```python
def __init__(
    specified_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    color_use_rule: SlateColorStylingMode = SlateColorStylingMode.
    USE_COLOR_SPECIFIED
) -> None
```

<a id="unreal.SlateColor.specified_color"></a>

#### specified_color

```python
@property
def specified_color() -> LinearColor
```

(LinearColor):  [Read-Write] The current specified color; only meaningful when ColorToUse == UseColor_Specified.

<a id="unreal.SlateColor.specified_color"></a>

#### specified_color

```python
@specified_color.setter
def specified_color(value: LinearColor) -> None
```

<a id="unreal.SlateColor.color_use_rule"></a>

#### color_use_rule

```python
@property
def color_use_rule() -> SlateColorStylingMode
```

(SlateColorStylingMode):  [Read-Write] The rule for which color to pick.

<a id="unreal.SlateColor.color_use_rule"></a>

#### color_use_rule

```python
@color_use_rule.setter
def color_use_rule(value: SlateColorStylingMode) -> None
```

<a id="unreal.Margin"></a>