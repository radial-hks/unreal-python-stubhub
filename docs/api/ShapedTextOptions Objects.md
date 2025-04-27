## ShapedTextOptions Objects

```python
class ShapedTextOptions(StructBase)
```

Common data for all widgets that use shaped text.
Contains the common options that should be exposed for the underlying Slate widget.

**C++ Source:**

- **Module**: UMG
- **File**: TextWidgetTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override_text_flow_direction`` (bool):  [Read-Write]
- ``override_text_shaping_method`` (bool):  [Read-Write]
- ``text_flow_direction`` (TextFlowDirection):  [Read-Write] Which text flow direction should the text within this widget use? (unset to use the default returned by GetDefaultTextFlowDirection)
- ``text_shaping_method`` (TextShapingMethod):  [Read-Write] Which text shaping method should the text within this widget use? (unset to use the default returned by GetDefaultTextShapingMethod)

<a id="unreal.ShapedTextOptions.__init__"></a>

#### __init__

```python
def __init__(
        text_shaping_method: TextShapingMethod = TextShapingMethod.AUTO,
        text_flow_direction: TextFlowDirection = TextFlowDirection.AUTO
) -> None
```

<a id="unreal.ShapedTextOptions.text_shaping_method"></a>

#### text_shaping_method

```python
@property
def text_shaping_method() -> TextShapingMethod
```

(TextShapingMethod):  [Read-Only] Which text shaping method should the text within this widget use? (unset to use the default returned by GetDefaultTextShapingMethod)

<a id="unreal.ShapedTextOptions.text_flow_direction"></a>

#### text_flow_direction

```python
@property
def text_flow_direction() -> TextFlowDirection
```

(TextFlowDirection):  [Read-Only] Which text flow direction should the text within this widget use? (unset to use the default returned by GetDefaultTextFlowDirection)

<a id="unreal.EditableTextStyle"></a>