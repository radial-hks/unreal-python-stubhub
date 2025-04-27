## UsdSparseVolumeTextureAssetUserData Objects

```python
class UsdSparseVolumeTextureAssetUserData(UsdAssetUserData)
```

We use this mainly to help in mapping between stage timeCode and the FrameIndex for animated SVTs

**C++ Source:**

- **Plugin**: USDCore
- **Module**: USDClasses
- **File**: USDAssetUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``original_hash`` (str):  [Read-Only] Hash of the prim data that was used to generate this asset
- ``prim_paths`` (Array[str]):  [Read-Write] Paths to prims that generated the asset that owns this AssetUserData
- ``source_open_vdb_asset_prim_paths`` (Array[str]):  [Read-Write] Paths to all the OpenVDBAsset prims that led to the generation of this SVT asset
- ``stage_identifier_to_metadata`` (Map[str, UsdCombinedPrimMetadata]):  [Read-Write] Holds metadata collected for this asset, from all relevant Source prims.
  The asset that owns this user data may be shared via the asset cache, and reused for
  even entirely different stages. This map lets us keep track of which stage owns which
  bits of metadata
- ``time_sample_path_indices`` (Array[int32]):  [Read-Write] Corresponding indices of the frame of the SVT that should be played at a particular timeCode.
  Example: TimeSamplePathTimeCodes is [10, 20] and TimeSamplePathIndices is [2, 7] --> At timeCode 10 the frame index 2
  of the SVT should be played, i.e. the .vdb file that is the third entry within TimeSamplePaths
- ``time_sample_path_time_codes`` (Array[double]):  [Read-Write] TimeCodes of all the filePath attribute time samples as seen on the OpenVDBAsset prim in its own layer, in order
- ``time_sample_paths`` (Array[str]):  [Read-Write] File paths that originated each of the SVT frames, in order.
  The SVT should have as many frames as there are entries in this array.

<a id="unreal.UsdSparseVolumeTextureAssetUserData.source_open_vdb_asset_prim_paths"></a>

#### source_open_vdb_asset_prim_paths

```python
@property
def source_open_vdb_asset_prim_paths() -> Array[str]
```

(Array[str]):  [Read-Write] Paths to all the OpenVDBAsset prims that led to the generation of this SVT asset

<a id="unreal.UsdSparseVolumeTextureAssetUserData.source_open_vdb_asset_prim_paths"></a>

#### source_open_vdb_asset_prim_paths

```python
@source_open_vdb_asset_prim_paths.setter
def source_open_vdb_asset_prim_paths(value: Array[str]) -> None
```

<a id="unreal.UsdSparseVolumeTextureAssetUserData.time_sample_path_time_codes"></a>

#### time_sample_path_time_codes

```python
@property
def time_sample_path_time_codes() -> Array[float]
```

(Array[double]):  [Read-Write] TimeCodes of all the filePath attribute time samples as seen on the OpenVDBAsset prim in its own layer, in order

<a id="unreal.UsdSparseVolumeTextureAssetUserData.time_sample_path_time_codes"></a>

#### time_sample_path_time_codes

```python
@time_sample_path_time_codes.setter
def time_sample_path_time_codes(value: Array[float]) -> None
```

<a id="unreal.UsdSparseVolumeTextureAssetUserData.time_sample_path_indices"></a>

#### time_sample_path_indices

```python
@property
def time_sample_path_indices() -> Array[int]
```

(Array[int32]):  [Read-Write] Corresponding indices of the frame of the SVT that should be played at a particular timeCode.
Example: TimeSamplePathTimeCodes is [10, 20] and TimeSamplePathIndices is [2, 7] --> At timeCode 10 the frame index 2
of the SVT should be played, i.e. the .vdb file that is the third entry within TimeSamplePaths

<a id="unreal.UsdSparseVolumeTextureAssetUserData.time_sample_path_indices"></a>

#### time_sample_path_indices

```python
@time_sample_path_indices.setter
def time_sample_path_indices(value: Array[int]) -> None
```

<a id="unreal.UsdSparseVolumeTextureAssetUserData.time_sample_paths"></a>

#### time_sample_paths

```python
@property
def time_sample_paths() -> Array[str]
```

(Array[str]):  [Read-Write] File paths that originated each of the SVT frames, in order.
The SVT should have as many frames as there are entries in this array.

<a id="unreal.UsdSparseVolumeTextureAssetUserData.time_sample_paths"></a>

#### time_sample_paths

```python
@time_sample_paths.setter
def time_sample_paths(value: Array[str]) -> None
```

<a id="unreal.UsdDrawModeComponent"></a>