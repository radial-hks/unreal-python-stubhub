## UsdPrimMetadata Objects

```python
class UsdPrimMetadata(StructBase)
```

Describes all the metadata values collected from a particular USD prim

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDMetadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``metadata`` (Map[str, UsdMetadataValue]):  [Read-Write]

<a id="unreal.UsdPrimMetadata.__init__"></a>

#### __init__

```python
def __init__(metadata: Map[str, UsdMetadataValue] = {}) -> None
```

<a id="unreal.UsdPrimMetadata.metadata"></a>

#### metadata

```python
@property
def metadata() -> Map[str, UsdMetadataValue]
```

(Map[str, UsdMetadataValue]):  [Read-Write]

<a id="unreal.UsdPrimMetadata.metadata"></a>

#### metadata

```python
@metadata.setter
def metadata(value: Map[str, UsdMetadataValue]) -> None
```

<a id="unreal.UsdCombinedPrimMetadata"></a>