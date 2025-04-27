## InterchangeAnimationPayLoadKey Objects

```python
class InterchangeAnimationPayLoadKey(StructBase)
```

Interchange Animation Pay Load Key

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type`` (InterchangeAnimationPayLoadType):  [Read-Write]
- ``unique_id`` (str):  [Read-Write]

<a id="unreal.InterchangeAnimationPayLoadKey.__init__"></a>

#### __init__

```python
def __init__(
    unique_id: str = "",
    type: InterchangeAnimationPayLoadType = InterchangeAnimationPayLoadType.
    NONE
) -> None
```

<a id="unreal.InterchangeAnimationPayLoadKey.unique_id"></a>

#### unique_id

```python
@property
def unique_id() -> str
```

(str):  [Read-Write]

<a id="unreal.InterchangeAnimationPayLoadKey.unique_id"></a>

#### unique_id

```python
@unique_id.setter
def unique_id(value: str) -> None
```

<a id="unreal.InterchangeAnimationPayLoadKey.type"></a>

#### type

```python
@property
def type() -> InterchangeAnimationPayLoadType
```

(InterchangeAnimationPayLoadType):  [Read-Write]

<a id="unreal.InterchangeAnimationPayLoadKey.type"></a>

#### type

```python
@type.setter
def type(value: InterchangeAnimationPayLoadType) -> None
```

<a id="unreal.InterchangeMeshPayLoadKey"></a>