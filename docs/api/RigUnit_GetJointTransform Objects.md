## RigUnit_GetJointTransform Objects

```python
class RigUnit_GetJointTransform(RigUnitMutable)
```

Rig Unit Get Joint Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetJointTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_joint`` (Name):  [Read-Write] Transform op option. Use if ETransformSpace is BaseJoint
- ``base_transform`` (Transform):  [Read-Write] Transform op option. Use if ETransformSpace is BaseTransform
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``joint`` (Name):  [Read-Write]
- ``output`` (Transform):  [Read-Write] possibly space, relative transform so on can be input
- ``transform_space`` (TransformSpaceMode):  [Read-Write]
- ``type`` (TransformGetterType):  [Read-Write]

<a id="unreal.RigUnit_GetJointTransform.__init__"></a>

#### __init__

```python
def __init__(
    execute_context: ControlRigExecuteContext = [],
    joint: Name = "None",
    type: TransformGetterType = TransformGetterType.INITIAL,
    transform_space: TransformSpaceMode = TransformSpaceMode.LOCAL_SPACE,
    base_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
    base_joint: Name = "None",
    output: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetJointTransform.joint"></a>

#### joint

```python
@property
def joint() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_GetJointTransform.joint"></a>

#### joint

```python
@joint.setter
def joint(value: Name) -> None
```

<a id="unreal.RigUnit_GetJointTransform.type"></a>

#### type

```python
@property
def type() -> TransformGetterType
```

(TransformGetterType):  [Read-Write]

<a id="unreal.RigUnit_GetJointTransform.type"></a>

#### type

```python
@type.setter
def type(value: TransformGetterType) -> None
```

<a id="unreal.RigUnit_GetJointTransform.transform_space"></a>

#### transform_space

```python
@property
def transform_space() -> TransformSpaceMode
```

(TransformSpaceMode):  [Read-Write]

<a id="unreal.RigUnit_GetJointTransform.transform_space"></a>

#### transform_space

```python
@transform_space.setter
def transform_space(value: TransformSpaceMode) -> None
```

<a id="unreal.RigUnit_GetJointTransform.base_transform"></a>

#### base_transform

```python
@property
def base_transform() -> Transform
```

(Transform):  [Read-Write] Transform op option. Use if ETransformSpace is BaseTransform

<a id="unreal.RigUnit_GetJointTransform.base_transform"></a>

#### base_transform

```python
@base_transform.setter
def base_transform(value: Transform) -> None
```

<a id="unreal.RigUnit_GetJointTransform.base_joint"></a>

#### base_joint

```python
@property
def base_joint() -> Name
```

(Name):  [Read-Write] Transform op option. Use if ETransformSpace is BaseJoint

<a id="unreal.RigUnit_GetJointTransform.base_joint"></a>

#### base_joint

```python
@base_joint.setter
def base_joint(value: Name) -> None
```

<a id="unreal.RigUnit_GetJointTransform.output"></a>

#### output

```python
@property
def output() -> Transform
```

(Transform):  [Read-Only] possibly space, relative transform so on can be input

<a id="unreal.RigUnit_TwoBoneIKFK"></a>