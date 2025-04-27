## RigUnit_ToRigSpace_Transform Objects

```python
class RigUnit_ToRigSpace_Transform(RigUnit)
```

Converts a transform from world space to rig (global) space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_WorldSpace.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Transform):  [Read-Write] The result transform in global / rig space
- ``value`` (Transform):  [Read-Write] The input transform in world

<a id="unreal.RigUnit_ToRigSpace_Transform.__init__"></a>

#### __init__

```python
def __init__(
    value: Transform = [[0.000000, 0.000000, 0.000000],
                        [-0.000000, 0.000000, 0.000000],
                        [1.000000, 1.000000, 1.000000]],
    global_: Transform = [[0.000000, 0.000000, 0.000000],
                          [-0.000000, 0.000000, 0.000000],
                          [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Transform.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write] The input transform in world

<a id="unreal.RigUnit_ToRigSpace_Transform.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Transform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

deprecated: 'transform' was renamed to 'value'.

<a id="unreal.RigUnit_ToRigSpace_Transform.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ToRigSpace_Transform.global_"></a>

#### global_

```python
@property
def global_() -> Transform
```

(Transform):  [Read-Only] The result transform in global / rig space

<a id="unreal.RigUnit_ToWorldSpace_Location"></a>