## UsdAnimSequenceAssetUserData Objects

```python
class UsdAnimSequenceAssetUserData(UsdAssetUserData)
```

Usd Anim Sequence Asset User Data

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

<a id="unreal.UsdMaterialAssetUserData"></a>