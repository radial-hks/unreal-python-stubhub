## SkeletalMeshLODSettings Objects

```python
class SkeletalMeshLODSettings(DataAsset)
```

Skeletal Mesh LODSettings

**C++ Source:**

- **Module**: Engine
- **File**: SkeletalMeshLODSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disable_below_min_lod_stripping`` (PerPlatformBool):  [Read-Write] When true LODs below MinLod will not be stripped during cook.
- ``lod_groups`` (Array[SkeletalMeshLODGroupSettings]):  [Read-Write]
- ``max_num_optional_lo_ds`` (PerPlatformInt):  [Read-Write] Default maximum number of optional LODs for meshes in this group (currently, need to be either 0 or > num of LODs below MinLod)
- ``max_num_streamed_lo_ds`` (PerPlatformInt):  [Read-Write] Default maximum number of streamed LODs for meshes in this group
- ``min_lod`` (PerPlatformInt):  [Read-Write] Minimum LOD to render. Can be overridden per mesh as well as set here for all mesh instances
- ``min_quality_level_lod`` (PerQualityLevelInt):  [Read-Write] Minimum Quality Level LOD to render. Can be overridden per mesh as well as set here for all mesh instances
- ``override_lod_streaming_settings`` (bool):  [Read-Write] Whether meshes in this group override default LOD streaming settings.
- ``support_lod_streaming`` (PerPlatformBool):  [Read-Write] Whether meshes in this group stream LODs by default

<a id="unreal.USkeletalMeshReductionSettings"></a>