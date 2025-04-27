## RigUnit_BlendTransform Objects

```python
class RigUnit_BlendTransform(RigUnit)
```

Rig Unit Blend Transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BlendTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Transform):  [Read-Write]
- ``source`` (Transform):  [Read-Write]
- ``targets`` (Array[BlendTarget]):  [Read-Write]

<a id="unreal.RigUnit_BlendTransform.__init__"></a>

#### __init__

```python
def __init__(
    source: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]],
    targets: Array[BlendTarget] = [],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_BlendTransform.source"></a>

#### source

```python
@property
def source() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigUnit_BlendTransform.source"></a>

#### source

```python
@source.setter
def source(value: Transform) -> None
```

<a id="unreal.RigUnit_BlendTransform.targets"></a>

#### targets

```python
@property
def targets() -> Array[BlendTarget]
```

(Array[BlendTarget]):  [Read-Write]

<a id="unreal.RigUnit_BlendTransform.targets"></a>

#### targets

```python
@targets.setter
def targets(value: Array[BlendTarget]) -> None
```

<a id="unreal.RigUnit_BlendTransform.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_GetJointTransform"></a>