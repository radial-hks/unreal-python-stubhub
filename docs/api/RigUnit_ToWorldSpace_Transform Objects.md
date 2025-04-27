## RigUnit_ToWorldSpace_Transform Objects

```python
class RigUnit_ToWorldSpace_Transform(RigUnit)
```

Converts a transform from rig (global) space to world space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (Transform):  [Read-Write] The input transform in global / rig space
- ``world`` (Transform):  [Read-Write] The result transform in world space

<a id="unreal.RigUnit_ToWorldSpace_Transform.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    world: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Transform.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write] The input transform in global / rig space

<a id="unreal.RigUnit_ToWorldSpace_Transform.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Transform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

deprecated: 'transform' was renamed to 'value'.

<a id="unreal.RigUnit_ToWorldSpace_Transform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ToWorldSpace_Transform.world"></a>

#### world

```python
@property
def world() -> Transform
```

(Transform):  [Read-Only] The result transform in world space

<a id="unreal.RigUnit_ToRigSpace_Transform"></a>