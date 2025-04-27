## UsdMaterialAssetUserData Objects

```python
class UsdMaterialAssetUserData(UsdAssetUserData)
```

AssetImportData assigned to Unreal materials that are generated when parsing USD Material prims

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``original_hash`` (str):  [Read-Only] Hash of the prim data that was used to generate this asset
- ``parameter_to_primvar`` (Map[str, str]):  [Read-Write] In the context of our reference materials that just read a single texture for each material parameter, this
  describes the primvar that the USD material is sampling for each texture.
  e.g. {'BaseColor': 'st0', 'Metallic': 'st1'}
- ``prim_paths`` (Array[str]):  [Read-Write] Paths to prims that generated the asset that owns this AssetUserData
- ``primvar_to_uv_index`` (Map[str, int32]):  [Read-Write] In the context of our reference materials that just read a single texture for each material parameter, this
  describes the Unreal UV index that will be used for sampling by each USD primvar. The idea is to use this in
  combination with ParameterToPrimvar, in order to describe which UV index the material has currently assigned to
  each parameter. When assigning the material to meshes later, we'll compare this member with the
  UUsdMeshAssetImportData's own PrimvarToUVIndex to see if they are compatible or not, and if not spawn a new
  material instance that is.
  e.g. {'firstPrimvar': 0, 'st': 1, 'st1': 2}
- ``stage_identifier_to_metadata`` (Map[str, UsdCombinedPrimMetadata]):  [Read-Write] Holds metadata collected for this asset, from all relevant Source prims.
  The asset that owns this user data may be shared via the asset cache, and reused for
  even entirely different stages. This map lets us keep track of which stage owns which
  bits of metadata

<a id="unreal.UsdMaterialAssetUserData.parameter_to_primvar"></a>

#### parameter_to_primvar

```python
@property
def parameter_to_primvar() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] In the context of our reference materials that just read a single texture for each material parameter, this
describes the primvar that the USD material is sampling for each texture.
e.g. {'BaseColor': 'st0', 'Metallic': 'st1'}

<a id="unreal.UsdMaterialAssetUserData.parameter_to_primvar"></a>

#### parameter_to_primvar

```python
@parameter_to_primvar.setter
def parameter_to_primvar(value: Map[str, str]) -> None
```

<a id="unreal.UsdMaterialAssetUserData.primvar_to_uv_index"></a>

#### primvar_to_uv_index

```python
@property
def primvar_to_uv_index() -> Map[str, int]
```

(Map[str, int32]):  [Read-Write] In the context of our reference materials that just read a single texture for each material parameter, this
describes the Unreal UV index that will be used for sampling by each USD primvar. The idea is to use this in
combination with ParameterToPrimvar, in order to describe which UV index the material has currently assigned to
each parameter. When assigning the material to meshes later, we'll compare this member with the
UUsdMeshAssetImportData's own PrimvarToUVIndex to see if they are compatible or not, and if not spawn a new
material instance that is.
e.g. {'firstPrimvar': 0, 'st': 1, 'st1': 2}

<a id="unreal.UsdMaterialAssetUserData.primvar_to_uv_index"></a>

#### primvar_to_uv_index

```python
@primvar_to_uv_index.setter
def primvar_to_uv_index(value: Map[str, int]) -> None
```

<a id="unreal.UsdMeshAssetUserData"></a>