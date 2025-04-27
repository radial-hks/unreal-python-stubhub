## ViewportActionKeyInput Objects

```python
class ViewportActionKeyInput(StructBase)
```

Represents a generic action

**C++ Source:**

- **Module**: ViewportInteraction
- **File**: ViewportInteractionTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_type`` (Name):  [Read-Write] The name of this action
- ``event`` (InputEventType):  [Read-Write] Input event

<a id="unreal.ViewportActionKeyInput.__init__"></a>

#### __init__

```python
def __init__(action_type: Name = "None",
             event: InputEventType = InputEventType.IE_PRESSED) -> None
```

<a id="unreal.ViewportActionKeyInput.action_type"></a>

#### action_type

```python
@property
def action_type() -> Name
```

(Name):  [Read-Only] The name of this action

<a id="unreal.ViewportActionKeyInput.event"></a>

#### event

```python
@property
def event() -> InputEventType
```

(InputEventType):  [Read-Only] Input event

<a id="unreal.CompositionGraphCapturePasses"></a>