## UsdAssetUserData Objects

```python
class UsdAssetUserData(AssetUserData)
```

Usd Asset User Data

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``original_hash`` (str):  [Read-Only] Hash of the prim data that was used to generate this asset
- ``prim_paths`` (Array[str]):  [Read-Write] Paths to prims that generated the asset that owns this AssetUserData
- ``stage_identifier_to_metadata`` (Map[str, UsdCombinedPrimMetadata]):  [Read-Write] Holds metadata collected for this asset, from all relevant Source prims.
  The asset that owns this user data may be shared via the asset cache, and reused for
  even entirely different stages. This map lets us keep track of which stage owns which
  bits of metadata

<a id="unreal.UsdAssetUserData.prim_paths"></a>

#### prim_paths

```python
@property
def prim_paths() -> Array[str]
```

(Array[str]):  [Read-Write] Paths to prims that generated the asset that owns this AssetUserData

<a id="unreal.UsdAssetUserData.prim_paths"></a>

#### prim_paths

```python
@prim_paths.setter
def prim_paths(value: Array[str]) -> None
```

<a id="unreal.UsdAssetUserData.stage_identifier_to_metadata"></a>

#### stage_identifier_to_metadata

```python
@property
def stage_identifier_to_metadata() -> Map[str, UsdCombinedPrimMetadata]
```

(Map[str, UsdCombinedPrimMetadata]):  [Read-Write] Holds metadata collected for this asset, from all relevant Source prims.
The asset that owns this user data may be shared via the asset cache, and reused for
even entirely different stages. This map lets us keep track of which stage owns which
bits of metadata

<a id="unreal.UsdAssetUserData.stage_identifier_to_metadata"></a>

#### stage_identifier_to_metadata

```python
@stage_identifier_to_metadata.setter
def stage_identifier_to_metadata(
        value: Map[str, UsdCombinedPrimMetadata]) -> None
```

<a id="unreal.UsdAssetUserData.original_hash"></a>

#### original_hash

```python
@property
def original_hash() -> str
```

(str):  [Read-Only] Hash of the prim data that was used to generate this asset

<a id="unreal.UsdAnimSequenceAssetUserData"></a>