## RigUnit_TransformConstraint Objects

```python
class RigUnit_TransformConstraint(RigUnit_HighlevelBaseMutable)
```

Rig Unit Transform Constraint

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_bone`` (Name):  [Read-Write] Transform op option. Use if ETransformSpace is BaseJoint
- ``base_transform`` (Transform):  [Read-Write] Transform op option. Use if ETransformSpace is BaseTransform
- ``base_transform_space`` (TransformSpaceMode):  [Read-Write]
- ``bone`` (Name):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``targets`` (Array[ConstraintTarget]):  [Read-Write]
- ``use_initial_transforms`` (bool):  [Read-Only] If checked the initial transform will be used for the constraint data

<a id="unreal.RigUnit_TransformConstraint.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             bone: Name = "None",
             base_transform_space: TransformSpaceMode = TransformSpaceMode.
             LOCAL_SPACE,
             base_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                          [-0.000000, 0.000000, 0.000000],
                                          [1.000000, 1.000000, 1.000000]],
             base_bone: Name = "None",
             targets: Array[ConstraintTarget] = [],
             use_initial_transforms: bool = False) -> None
```

<a id="unreal.RigUnit_TransformConstraint.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_TransformConstraint.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_TransformConstraint.base_transform_space"></a>

#### base_transform_space

```python
@property
def base_transform_space() -> TransformSpaceMode
```

(TransformSpaceMode):  [Read-Write]

<a id="unreal.RigUnit_TransformConstraint.base_transform_space"></a>

#### base_transform_space

```python
@base_transform_space.setter
def base_transform_space(value: TransformSpaceMode) -> None
```

<a id="unreal.RigUnit_TransformConstraint.base_transform"></a>

#### base_transform

```python
@property
def base_transform() -> Transform
```

(Transform):  [Read-Write] Transform op option. Use if ETransformSpace is BaseTransform

<a id="unreal.RigUnit_TransformConstraint.base_transform"></a>

#### base_transform

```python
@base_transform.setter
def base_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_TransformConstraint.base_bone"></a>

#### base_bone

```python
@property
def base_bone() -> Name
```

(Name):  [Read-Write] Transform op option. Use if ETransformSpace is BaseJoint

<a id="unreal.RigUnit_TransformConstraint.base_bone"></a>

#### base_bone

```python
@base_bone.setter
def base_bone(value: Name) -> None
```

<a id="unreal.RigUnit_TransformConstraint.targets"></a>

#### targets

```python
@property
def targets() -> Array[ConstraintTarget]
```

(Array[ConstraintTarget]):  [Read-Write]

<a id="unreal.RigUnit_TransformConstraint.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[ConstraintTarget]) -> None
```

<a id="unreal.RigUnit_TransformConstraint.use_initial_transforms"></a>

#### use_initial_transforms

```python
@property
def use_initial_transforms() -> bool
```

(bool):  [Read-Only] If checked the initial transform will be used for the constraint data

<a id="unreal.RigUnit_TransformConstraintPerItem"></a>