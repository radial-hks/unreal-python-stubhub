## RigUnit_DrawContainerSetColor Objects

```python
class RigUnit_DrawContainerSetColor(RigUnitMutable)
```

Set Imported Draw Container curve color

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DrawContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``instruction_name`` (Name):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerSetColor.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        instruction_name: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_DrawContainerSetColor.instruction_name"></a>

#### instruction_name

```python
@property
def instruction_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerSetColor.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigUnit_DrawContainerSetColor.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigUnit_DrawContainerSetThickness"></a>