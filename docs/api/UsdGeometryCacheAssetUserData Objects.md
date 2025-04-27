## UsdGeometryCacheAssetUserData Objects

```python
class UsdGeometryCacheAssetUserData(UsdMeshAssetUserData)
```

We assign these to UGeometryCaches generated from USD

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``layer_start_offset_seconds`` (float):  [Read-Write] Check analogous comment on UUsdAnimSequenceAssetUserData
- ``material_slot_to_prim_paths`` (Map[int32, UsdPrimPathList]):  [Read-Write] Maps from a material slot index of an UStaticMesh or USkeletalMesh to a list of source prims that contain this
  assignment. It can contain multiple prims in case we combine material slots and/or collapse prims
  (e.g. {0: ['/Root/mesh', '/Root/othermesh/geomsubset0', '/Root/othermesh/geomsubset1'] }).
- ``original_hash`` (str):  [Read-Only] Hash of the prim data that was used to generate this asset
- ``prim_paths`` (Array[str]):  [Read-Write] Paths to prims that generated the asset that owns this AssetUserData
- ``primvar_to_uv_index`` (Map[str, int32]):  [Read-Write] Describes which primvars should be assigned to each UV index.
- ``stage_identifier_to_metadata`` (Map[str, UsdCombinedPrimMetadata]):  [Read-Write] Holds metadata collected for this asset, from all relevant Source prims.
  The asset that owns this user data may be shared via the asset cache, and reused for
  even entirely different stages. This map lets us keep track of which stage owns which
  bits of metadata

<a id="unreal.UsdGeometryCacheAssetUserData.layer_start_offset_seconds"></a>

#### layer_start_offset_seconds

```python
@property
def layer_start_offset_seconds() -> float
```

(float):  [Read-Write] Check analogous comment on UUsdAnimSequenceAssetUserData

<a id="unreal.UsdGeometryCacheAssetUserData.layer_start_offset_seconds"></a>

#### layer_start_offset_seconds

```python
@layer_start_offset_seconds.setter
def layer_start_offset_seconds(value: float) -> None
```

<a id="unreal.UsdLevelSequenceAssetUserData"></a>