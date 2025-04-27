## UsdCombinedPrimMetadata Objects

```python
class UsdCombinedPrimMetadata(StructBase)
```

Tracks metadata collected from multiple prim paths.
This is useful because often multiple prims will be read to generate an asset, like when collapsing or
collecting skinned Mesh prims for a SkeletalMesh.
This may also be used if multiple prims within the same stage end up generating the same asset,
which is shared via the asset cache: Both prims will store their metadata here.

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDMetadata.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``prim_path_to_metadata`` (Map[str, UsdPrimMetadata]):  [Read-Write]

<a id="unreal.UsdCombinedPrimMetadata.__init__"></a>

#### __init__

```python
def __init__(prim_path_to_metadata: Map[str, UsdPrimMetadata] = {}) -> None
```

<a id="unreal.UsdCombinedPrimMetadata.prim_path_to_metadata"></a>

#### prim_path_to_metadata

```python
@property
def prim_path_to_metadata() -> Map[str, UsdPrimMetadata]
```

(Map[str, UsdPrimMetadata]):  [Read-Write]

<a id="unreal.UsdCombinedPrimMetadata.prim_path_to_metadata"></a>

#### prim_path_to_metadata

```python
@prim_path_to_metadata.setter
def prim_path_to_metadata(value: Map[str, UsdPrimMetadata]) -> None
```

<a id="unreal.UsdMetadataImportOptions"></a>