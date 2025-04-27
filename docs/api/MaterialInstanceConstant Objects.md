## MaterialInstanceConstant Objects

```python
class MaterialInstanceConstant(MaterialInstance)
```

Material Instances may be used to change the appearance of a material without incurring an expensive recompilation of the material.
General modification of the material cannot be supported without recompilation, so the instances are limited to changing the values of
predefined material parameters. The parameters are statically defined in the compiled material by a unique name, type and default value.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstanceConstant.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Write] Importing data and options used for this material
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``base_property_overrides`` (MaterialInstanceBasePropertyOverrides):  [Read-Write]
- ``blendable_location_override`` (BlendableLocation):  [Read-Write]
- ``blendable_priority_override`` (int32):  [Read-Write]
- ``double_vector_parameter_values`` (Array[DoubleVectorParameterValue]):  [Read-Write] DoubleVector parameters.
- ``editor_only_data`` (MaterialInterfaceEditorOnlyData):  [Read-Only]
- ``font_parameter_values`` (Array[FontParameterValue]):  [Read-Write] Font parameters.
- ``lightmass_settings`` (LightmassMaterialInterfaceSettings):  [Read-Write] The Lightmass settings for this object.
- ``nanite_override_material`` (MaterialOverrideNanite):  [Read-Write] An override material which will be used instead of this one when rendering with Nanite.
- ``neural_profile`` (NeuralProfile):  [Read-Write] Neural network profile. For internal usage, not editable/visible
- ``override_blendable_location`` (bool):  [Read-Write] For post process materials, use BlendableLocationOverride.
- ``override_blendable_priority`` (bool):  [Read-Write] For post process materials, use BlendablePriorityOverride.
- ``override_subsurface_profile`` (bool):  [Read-Write] Defines if SubsurfaceProfile from this instance is used or it uses the parent one.
- ``parent`` (MaterialInterface):  [Read-Write] Parent material.
- ``phys_material`` (PhysicalMaterial):  [Read-Write] Physical material to use for this graphics material. Used for sounds, effects etc.
- ``phys_material_mask`` (PhysicalMaterialMask):  [Read-Write] Physical material mask to use for this graphics material. Used for sounds, effects etc.
- ``physical_material_map`` (PhysicalMaterial):  [Read-Write] Physical material map used with physical material mask, when it exists.
- ``preview_mesh`` (SoftObjectPath):  [Read-Write] The mesh used by the material editor to preview the material.
- ``runtime_virtual_texture_parameter_values`` (Array[RuntimeVirtualTextureParameterValue]):  [Read-Write] RuntimeVirtualTexture parameters.
- ``scalar_parameter_values`` (Array[ScalarParameterValue]):  [Read-Write] Scalar parameters.
- ``sparse_volume_texture_parameter_values`` (Array[SparseVolumeTextureParameterValue]):  [Read-Write] Sparse Volume Texture parameters.
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Screen Space Subsurface Scattering..
- ``texture_collection_parameter_values`` (Array[TextureCollectionParameterValue]):  [Read-Write] Texture Collection parameters.
- ``texture_parameter_values`` (Array[TextureParameterValue]):  [Read-Write] Texture parameters.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``user_scene_texture_overrides`` (Array[UserSceneTextureOverride]):  [Read-Write] User scene texture overrides.  Applies to post process domain materials only.
- ``vector_parameter_values`` (Array[VectorParameterValue]):  [Read-Write] Vector parameters.

<a id="unreal.MaterialInstanceConstant.set_nanite_override_material"></a>

#### set_nanite_override_material

```python
def set_nanite_override_material(enable_override: bool,
                                 override_material: MaterialInterface) -> None
```

x.set_nanite_override_material(enable_override, override_material) -> None
Set an override material which will be used when rendering with nanite.

Args:
    enable_override (bool): 
    override_material (MaterialInterface):

<a id="unreal.MaterialInstanceConstant.get_vector_parameter_value"></a>

#### get_vector_parameter_value

```python
def get_vector_parameter_value(parameter_name: Name) -> LinearColor
```

x.get_vector_parameter_value(parameter_name) -> LinearColor
Get the MIC vector parameter value

Args:
    parameter_name (Name): 

Returns:
    LinearColor:

<a id="unreal.MaterialInstanceConstant.get_texture_parameter_value"></a>

#### get_texture_parameter_value

```python
def get_texture_parameter_value(parameter_name: Name) -> Texture
```

x.get_texture_parameter_value(parameter_name) -> Texture
Get the MIC texture parameter value

Args:
    parameter_name (Name): 

Returns:
    Texture:

<a id="unreal.MaterialInstanceConstant.get_scalar_parameter_value"></a>

#### get_scalar_parameter_value

```python
def get_scalar_parameter_value(parameter_name: Name) -> float
```

x.get_scalar_parameter_value(parameter_name) -> float
Get the scalar (float) parameter value from an MIC

Args:
    parameter_name (Name): 

Returns:
    float:

<a id="unreal.LandscapeMaterialInstanceConstant"></a>