## RigUnit_SetControlOffset Objects

```python
class RigUnit_SetControlOffset(RigUnitMutable)
```

SetControlOffset is used to perform a change in the hierarchy by setting a single control's transform.
This is typically only used during the Construction Event.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlOffset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``offset`` (Transform):  [Read-Write] The offset transform to set for the control
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.

<a id="unreal.RigUnit_SetControlOffset.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        control: Name = "None",
        offset: Transform = [[0.000000, 0.000000, 0.000000],
                             [-0.000000, 0.000000, 0.000000],
                             [1.000000, 1.000000, 1.000000]],
        space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
```

<a id="unreal.RigUnit_SetControlOffset.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetControlOffset.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlOffset.offset"></a>

#### offset

```python
@property
def offset() -> Transform
```

(Transform):  [Read-Write] The offset transform to set for the control

<a id="unreal.RigUnit_SetControlOffset.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Transform) -> None
```

<a id="unreal.RigUnit_SetControlOffset.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetControlOffset.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetShapeTransform"></a>