## RigUnit_SetShapeTransform Objects

```python
class RigUnit_SetShapeTransform(RigUnitMutable)
```

SetShapeTransform is used to perform a change in the hierarchy by setting a single control's shape transform.
This is typically only used during the Construction Event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlOffset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``transform`` (Transform):  [Read-Write] The shape transform to set for the control

<a id="unreal.RigUnit_SetShapeTransform.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    control: Name = "None",
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_SetShapeTransform.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetShapeTransform.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetShapeTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The shape transform to set for the control

<a id="unreal.RigUnit_SetShapeTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_SetControlBool"></a>