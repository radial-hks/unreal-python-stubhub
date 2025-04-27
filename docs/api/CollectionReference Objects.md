## CollectionReference Objects

```python
class CollectionReference(StructBase)
```

Reference to an editor collection of assets. This allows an editor-only picker UI

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection_name`` (Name):  [Read-Write] Name of the collection

<a id="unreal.CollectionReference.__init__"></a>

#### __init__

```python
def __init__(collection_name: Name = "None") -> None
```

<a id="unreal.CollectionReference.collection_name"></a>

#### collection_name

```python
@property
def collection_name() -> Name
```

(Name):  [Read-Write] Name of the collection

<a id="unreal.CollectionReference.collection_name"></a>

#### collection_name

```python
@collection_name.setter
def collection_name(value: Name) -> None
```

<a id="unreal.DepthFieldGlowInfo"></a>