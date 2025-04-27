## RigUnit_GetControlTransform Objects

```python
class RigUnit_GetControlTransform(RigUnit)
```

GetControlTransform is used to retrieve a single transform from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the transform for.
- ``maximum`` (Transform):  [Read-Write] The maximum value of the control.
- ``minimum`` (Transform):  [Read-Write] The minimum value of the control.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the Control's transform should be retrieved
  in local or global space.
- ``transform`` (Transform):  [Read-Write] The current value of the control.

<a id="unreal.RigUnit_GetControlTransform.__init__"></a>

#### __init__

```python
def __init__(
    control: Name = "None",
    space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    minimum: Transform = [[0.000000, 0.000000, 0.000000],
                          [-0.000000, 0.000000, 0.000000],
                          [1.000000, 1.000000, 1.000000]],
    maximum: Transform = [[0.000000, 0.000000, 0.000000],
                          [-0.000000, 0.000000, 0.000000],
                          [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetControlTransform.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the transform for.

<a id="unreal.RigUnit_GetControlTransform.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlTransform.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the Control's transform should be retrieved
in local or global space.

<a id="unreal.RigUnit_GetControlTransform.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetControlTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The current value of the control.

<a id="unreal.RigUnit_GetControlTransform.minimum"></a>

#### minimum

```python
@property
def minimum() -> Transform
```

(Transform):  [Read-Only] The minimum value of the control.

<a id="unreal.RigUnit_GetControlTransform.maximum"></a>

#### maximum

```python
@property
def maximum() -> Transform
```

(Transform):  [Read-Only] The maximum value of the control.

<a id="unreal.RigUnit_GetCurveValue"></a>