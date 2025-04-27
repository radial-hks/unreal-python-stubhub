## AnimationSettings Objects

```python
class AnimationSettings(DeveloperSettings)
```

Default animation settings.

**C++ Source:**

- **Module**: Engine
- **File**: AnimationSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_blend_modes`` (Map[Name, CustomAttributeBlendType]):  [Read-Write] Animation Attribute specific blend types (by name)
- ``bone_custom_attributes_names`` (Array[CustomAttributeSetting]):  [Read-Write] List of animation attribute names to import directly on their corresponding bone names. The meaning field allows to contextualize the attribute name and customize tooling for it.
- ``bone_names_with_custom_attributes`` (Array[str]):  [Read-Write] List of bone names for which all animation attributes are directly imported on the bone.
- ``bone_timecode_custom_attribute_name_settings`` (TimecodeCustomAttributeNameSettings):  [Read-Write] Names that identify bone animation attributes representing the individual components of a timecode and a subframe along with a take name.
            These will be included in the list of bone custom attribute names to import.
- ``compress_commandlet_version`` (int32):  [Read-Only] Compression version for recompress commandlet, bump this to trigger full recompressed, otherwise only new imported animations will be recompressed
- ``default_attribute_blend_mode`` (CustomAttributeBlendType):  [Read-Write] Default Animation Attribute blend type
- ``default_frame_rate`` (FrameRate):  [Read-Write] Project specific default frame-rate used when (re)initializing any animation based data
- ``enable_performance_log`` (bool):  [Read-Write] If true, recompression will log performance information
- ``enforce_supported_frame_rates`` (bool):  [Read-Write] Whether to enforce the project to only use entries from SupportedFrameRates for the animation assets, if disable will warn instead
- ``first_recompress_using_current_or_default`` (bool):  [Read-Write] If true, then the animation will be first recompressed with its current compressor if non-NULL, or with the global default compressor (specified in the engine ini)
  Also known as "Run Current Default Compressor"
- ``force_below_threshold`` (bool):  [Read-Write] If true and the existing compression error is greater than Alternative Compression Threshold, then any compression technique (even one that increases the size) with a lower error will be used until it falls below the threshold
- ``force_recompression`` (bool):  [Read-Write] If true, this will forcibly recompress every animation, this should not be checked in enabled
- ``key_end_effectors_match_name_array`` (Array[str]):  [Read-Write] List of bone names to treat with higher precision, in addition to any bones with sockets
- ``mirror_find_replace_expressions`` (Array[MirrorFindReplaceExpression]):  [Read-Write] Find and Replace Expressions used for mirroring
- ``raise_max_error_to_existing`` (bool):  [Read-Write] , EditAnywhere, Category = Compression
  deprecated: No longer used.
- ``strip_animation_data_on_dedicated_server`` (bool):  [Read-Write] If true, animation track data will be stripped from dedicated server cooked data
- ``tick_animation_on_skeletal_mesh_init`` (bool):  [Read-Write] If true, pre-4.19 behavior of zero-ticking animations during skeletal mesh init
- ``transform_attribute_names`` (Array[str]):  [Read-Write] Names to match against when importing FBX node transform curves as attributes (can use ? and * wildcards)
- ``user_defined_struct_attributes`` (Array[UserDefinedStruct]):  [Read-Write] Register user defined structs as animation attributes

<a id="unreal.AnimationSettings.raise_max_error_to_existing"></a>

#### raise_max_error_to_existing

```python
@property
def raise_max_error_to_existing() -> bool
```

(bool):  [Read-Write] , EditAnywhere, Category = Compression
deprecated: No longer used.

<a id="unreal.AnimationSettings.raise_max_error_to_existing"></a>

#### raise_max_error_to_existing

```python
@raise_max_error_to_existing.setter
def raise_max_error_to_existing(value: bool) -> None
```

<a id="unreal.AnimationSettings.get_bone_custom_attribute_names_to_import"></a>

#### get_bone_custom_attribute_names_to_import

```python
def get_bone_custom_attribute_names_to_import() -> Array[str]
```

x.get_bone_custom_attribute_names_to_import() -> Array[str]
Gets the complete list of bone animation attribute names to consider for import.
          This includes the designated timecode animation attributes as well as other bone animation attributes identified in the settings.

Returns:
    Array[str]:

<a id="unreal.AnimCompositeBase"></a>