## ElementID Objects

```python
class ElementID(StructBase)
```

todo: mesheditor: Need comments
todo: mesheditor script: BP doesn't have name spaces, so we might need a more specific display name, or just rename our various types

**C++ Source:**

- **Module**: MeshDescription
- **File**: MeshTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id_value`` (int32):  [Read-Write] The actual mesh element index this ID represents.  Read-only.

<a id="unreal.ElementID.__init__"></a>

#### __init__

```python
def __init__(id_value: int = 0) -> None
```

<a id="unreal.ElementID.id_value"></a>

#### id_value

```python
@property
def id_value() -> int
```

(int32):  [Read-Only] The actual mesh element index this ID represents.  Read-only.

<a id="unreal.VertexID"></a>