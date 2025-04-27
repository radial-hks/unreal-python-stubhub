## RigUnit_ApplyFK Objects

```python
class RigUnit_ApplyFK(RigUnitMutable)
```

Rig Unit Apply FK

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ApplyFK.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_transform_mode`` (ApplyTransformMode):  [Read-Write]
- ``apply_transform_space`` (TransformSpaceMode):  [Read-Write]
- ``base_joint`` (Name):  [Read-Write] Transform op option. Use if ETransformSpace is BaseJoint
- ``base_transform`` (Transform):  [Read-Write] Transform op option. Use if ETransformSpace is BaseTransform
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``filter`` (TransformFilter):  [Read-Write] The filter determines what axes can be manipulated by the in-viewport widgets
- ``joint`` (Name):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigUnit_ApplyFK.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        joint: Name = "None",
        transform: Transform = [[0.000000, 0.000000, 0.000000],
                                [-0.000000, 0.000000, 0.000000],
                                [1.000000, 1.000000, 1.000000]],
        filter: TransformFilter = [[True, True, True], [True, True, True],
                                   [True, True, True]],
        apply_transform_mode: ApplyTransformMode = ApplyTransformMode.OVERRIDE,
        apply_transform_space: TransformSpaceMode = TransformSpaceMode.
    LOCAL_SPACE,
        base_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
        base_joint: Name = "None") -> None
```

<a id="unreal.RigUnit_ApplyFK.joint"></a>

#### joint

```python
@property
def joint() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_ApplyFK.joint"></a>

#### joint

```python
@joint.setter
def joint(value: Name) -> None
```

<a id="unreal.RigUnit_ApplyFK.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_ApplyFK.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ApplyFK.filter"></a>

#### filter

```python
@property
def filter() -> TransformFilter
```

(TransformFilter):  [Read-Write] The filter determines what axes can be manipulated by the in-viewport widgets

<a id="unreal.RigUnit_ApplyFK.filter"></a>

#### filter

```python
@filter.setter
def filter(value: TransformFilter) -> None
```

<a id="unreal.RigUnit_ApplyFK.apply_transform_mode"></a>

#### apply_transform_mode

```python
@property
def apply_transform_mode() -> ApplyTransformMode
```

(ApplyTransformMode):  [Read-Write]

<a id="unreal.RigUnit_ApplyFK.apply_transform_mode"></a>

#### apply_transform_mode

```python
@apply_transform_mode.setter
def apply_transform_mode(value: ApplyTransformMode) -> None
```

<a id="unreal.RigUnit_ApplyFK.apply_transform_space"></a>

#### apply_transform_space

```python
@property
def apply_transform_space() -> TransformSpaceMode
```

(TransformSpaceMode):  [Read-Write]

<a id="unreal.RigUnit_ApplyFK.apply_transform_space"></a>

#### apply_transform_space

```python
@apply_transform_space.setter
def apply_transform_space(value: TransformSpaceMode) -> None
```

<a id="unreal.RigUnit_ApplyFK.base_transform"></a>

#### base_transform

```python
@property
def base_transform() -> Transform
```

(Transform):  [Read-Write] Transform op option. Use if ETransformSpace is BaseTransform

<a id="unreal.RigUnit_ApplyFK.base_transform"></a>

#### base_transform

```python
@base_transform.setter
def base_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ApplyFK.base_joint"></a>

#### base_joint

```python
@property
def base_joint() -> Name
```

(Name):  [Read-Write] Transform op option. Use if ETransformSpace is BaseJoint

<a id="unreal.RigUnit_ApplyFK.base_joint"></a>

#### base_joint

```python
@base_joint.setter
def base_joint(value: Name) -> None
```

<a id="unreal.BlendTarget"></a>