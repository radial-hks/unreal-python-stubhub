## UsdMeshAssetUserData Objects

```python
class UsdMeshAssetUserData(UsdAssetUserData)
```

We assign these to UStaticMeshes or USkeletalMeshes generated from USD

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

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

<a id="unreal.UsdMeshAssetUserData.material_slot_to_prim_paths"></a>

#### material_slot_to_prim_paths

```python
@property
def material_slot_to_prim_paths() -> Map[int, UsdPrimPathList]
```

(Map[int32, UsdPrimPathList]):  [Read-Write] Maps from a material slot index of an UStaticMesh or USkeletalMesh to a list of source prims that contain this
assignment. It can contain multiple prims in case we combine material slots and/or collapse prims
(e.g. {0: ['/Root/mesh', '/Root/othermesh/geomsubset0', '/Root/othermesh/geomsubset1'] }).

<a id="unreal.UsdMeshAssetUserData.material_slot_to_prim_paths"></a>

#### material_slot_to_prim_paths

```python
@material_slot_to_prim_paths.setter
def material_slot_to_prim_paths(value: Map[int, UsdPrimPathList]) -> None
```

<a id="unreal.UsdMeshAssetUserData.primvar_to_uv_index"></a>

#### primvar_to_uv_index

```python
@property
def primvar_to_uv_index() -> Map[str, int]
```

(Map[str, int32]):  [Read-Write] Describes which primvars should be assigned to each UV index.

<a id="unreal.UsdMeshAssetUserData.primvar_to_uv_index"></a>

#### primvar_to_uv_index

```python
@primvar_to_uv_index.setter
def primvar_to_uv_index(value: Map[str, int]) -> None
```

<a id="unreal.UsdGeometryCacheAssetUserData"></a>