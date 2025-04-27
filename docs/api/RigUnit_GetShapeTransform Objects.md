## RigUnit_GetShapeTransform Objects

```python
class RigUnit_GetShapeTransform(RigUnit)
```

GetShapeTransform is used to retrieve single control's shape transform.
This is typically only used during the Construction Event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlOffset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``transform`` (Transform):  [Read-Write] The shape transform to set for the control

<a id="unreal.RigUnit_GetShapeTransform.__init__"></a>

#### __init__

```python
def __init__(
    control: Name = "None",
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetShapeTransform.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_GetShapeTransform.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetShapeTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The shape transform to set for the control

<a id="unreal.RigUnit_SetShapeTransform"></a>