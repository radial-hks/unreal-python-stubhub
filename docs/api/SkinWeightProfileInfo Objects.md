## SkinWeightProfileInfo Objects

```python
class SkinWeightProfileInfo(StructBase)
```

Structure storing user facing properties, and is used to identify profiles at the SkeletalMesh level

**C++ Source:**

- **Module**: Engine
- **File**: SkinWeightProfile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_profile`` (PerPlatformBool):  [Read-Write] Whether or not this Profile should be considered the Default loaded for specific LODs rather than the original Skin Weights of the Skeletal Mesh
- ``default_profile_from_lod_index`` (PerPlatformInt):  [Read-Write] When DefaultProfile is set any LOD below this LOD Index will override the Skin Weights of the Skeletal Mesh with the Skin Weights from this Profile
- ``name`` (Name):  [Read-Write] Name of the Skin Weight Profile
- ``per_lod_source_files`` (Map[int32, str]):  [Read-Only]

<a id="unreal.SkinWeightProfileInfo.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SkeletalMeshLODGroupSettings"></a>