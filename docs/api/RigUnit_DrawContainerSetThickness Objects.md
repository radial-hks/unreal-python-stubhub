## RigUnit_DrawContainerSetThickness Objects

```python
class RigUnit_DrawContainerSetThickness(RigUnitMutable)
```

Set Imported Draw Container curve thickness

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DrawContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``instruction_name`` (Name):  [Read-Only]
- ``thickness`` (float):  [Read-Write]

<a id="unreal.RigUnit_DrawContainerSetThickness.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             instruction_name: Name = "None",
             thickness: float = 0.000000) -> None
```

<a id="unreal.RigUnit_DrawContainerSetThickness.instruction_name"></a>

#### instruction_name

```python
@property
def instruction_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerSetThickness.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_DrawContainerSetThickness.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_DrawContainerSetTransform"></a>