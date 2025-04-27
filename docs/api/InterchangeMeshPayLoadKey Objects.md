## InterchangeMeshPayLoadKey Objects

```python
class InterchangeMeshPayLoadKey(StructBase)
```

Interchange Mesh Pay Load Key

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeMeshNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``type`` (InterchangeMeshPayLoadType):  [Read-Write]
- ``unique_id`` (str):  [Read-Write]

<a id="unreal.InterchangeMeshPayLoadKey.__init__"></a>

#### __init__

```python
def __init__(
    unique_id: str = "",
    type: InterchangeMeshPayLoadType = InterchangeMeshPayLoadType.NONE
) -> None
```

<a id="unreal.InterchangeMeshPayLoadKey.unique_id"></a>

#### unique_id

```python
@property
def unique_id() -> str
```

(str):  [Read-Write]

<a id="unreal.InterchangeMeshPayLoadKey.unique_id"></a>

#### unique_id

```python
@unique_id.setter
def unique_id(value: str) -> None
```

<a id="unreal.InterchangeMeshPayLoadKey.type"></a>

#### type

```python
@property
def type() -> InterchangeMeshPayLoadType
```

(InterchangeMeshPayLoadType):  [Read-Write]

<a id="unreal.InterchangeMeshPayLoadKey.type"></a>

#### type

```python
@type.setter
def type(value: InterchangeMeshPayLoadType) -> None
```

<a id="unreal.UsdPrimPathList"></a>