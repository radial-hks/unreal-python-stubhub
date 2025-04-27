## RigUnit_DrawContainerSetTransform Objects

```python
class RigUnit_DrawContainerSetTransform(RigUnitMutable)
```

Set Imported Draw Container curve transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_DrawContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``instruction_name`` (Name):  [Read-Only]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_DrawContainerSetTransform.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    instruction_name: Name = "None",
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_DrawContainerSetTransform.instruction_name"></a>

#### instruction_name

```python
@property
def instruction_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigUnit_DrawContainerSetTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_DrawContainerSetTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_BeginExecution"></a>