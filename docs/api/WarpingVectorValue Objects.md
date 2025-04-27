## WarpingVectorValue Objects

```python
class WarpingVectorValue(StructBase)
```

Vector values which may be specified in a configured space

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: BoneControllerTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mode`` (WarpingVectorMode):  [Read-Write] Space of the corresponding Vector value
- ``value`` (Vector):  [Read-Write] Specifies a vector relative to the space defined by Mode

<a id="unreal.WarpingVectorValue.__init__"></a>

#### __init__

```python
def __init__(
        mode: WarpingVectorMode = WarpingVectorMode.COMPONENT_SPACE_VECTOR,
        value: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.WarpingVectorValue.mode"></a>

#### mode

```python
@property
def mode() -> WarpingVectorMode
```

(WarpingVectorMode):  [Read-Write] Space of the corresponding Vector value

<a id="unreal.WarpingVectorValue.mode"></a>

#### mode

```python
@mode.setter
def mode(value: WarpingVectorMode) -> None
```

<a id="unreal.WarpingVectorValue.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write] Specifies a vector relative to the space defined by Mode

<a id="unreal.WarpingVectorValue.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.LayeredBoneBlendReference"></a>