## RigUnit_AddBoneTransform Objects

```python
class RigUnit_AddBoneTransform(RigUnitMutable)
```

Offset Transform is used to perform a change in the hierarchy by setting a single bone's transform.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AddBoneTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone`` (Name):  [Read-Write] The name of the Bone to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``post_multiply`` (bool):  [Read-Write] If set to true the transform will be post multiplied, otherwise pre multiplied.
  Post multiplying means that the transform is understood as a parent space change,
  while pre multiplying means that the transform is understood as a child space change.
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``transform`` (Transform):  [Read-Write] The transform value to set for the given Bone.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AddBoneTransform.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             bone: Name = "None",
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             weight: float = 0.000000,
             post_multiply: bool = False,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_AddBoneTransform.bone"></a>

#### bone

```python
@property
def bone() -> Name
```

(Name):  [Read-Write] The name of the Bone to set the transform for.

<a id="unreal.RigUnit_AddBoneTransform.bone"></a>

#### bone

```python
@bone.setter
def bone(value: Name) -> None
```

<a id="unreal.RigUnit_AddBoneTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_AddBoneTransform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_AddBoneTransform.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_AddBoneTransform.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_AddBoneTransform.post_multiply"></a>

#### post_multiply

```python
@property
def post_multiply() -> bool
```

(bool):  [Read-Write] If set to true the transform will be post multiplied, otherwise pre multiplied.
Post multiplying means that the transform is understood as a parent space change,
while pre multiplying means that the transform is understood as a child space change.

<a id="unreal.RigUnit_AddBoneTransform.post_multiply"></a>

#### post_multiply

```python
@post_multiply.setter
def post_multiply(value: bool) -> None
```

<a id="unreal.RigUnit_AddBoneTransform.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_Item"></a>