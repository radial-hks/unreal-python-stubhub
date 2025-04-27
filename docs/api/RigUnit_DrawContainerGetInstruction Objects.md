## RigUnit_DrawContainerGetInstruction Objects

```python
class RigUnit_DrawContainerGetInstruction(RigUnit)
```

Get Imported Draw Container curve transform and color

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DrawContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``instruction_name`` (Name):  [Read-Only]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DrawContainerGetInstruction.__init__"></a>

#### __init__

```python
def __init__(
    instruction_name: Name = "None",
    color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_DrawContainerGetInstruction.instruction_name"></a>

#### instruction_name

```python
@property
def instruction_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerGetInstruction.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerGetInstruction.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerSetColor"></a>