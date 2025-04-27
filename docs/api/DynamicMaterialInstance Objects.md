## DynamicMaterialInstance Objects

```python
class DynamicMaterialInstance(MaterialInstanceDynamic)
```

A Material Designer Material with its own integrated Material Designer Model that generates the base Material.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DynamicMaterialInstance.h

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
- ``material_model_base`` (DynamicMaterialModelBase):  [Read-Only]
- ``nanite_override_material`` (MaterialOverrideNanite):  [Read-Write] An override material which will be used instead of this one when rendering with Nanite.
- ``neural_profile`` (NeuralProfile):  [Read-Write] Neural network profile. For internal usage, not editable/visible
- ``override_blendable_location`` (bool):  [Read-Write] For post process materials, use BlendableLocationOverride.
- ``override_blendable_priority`` (bool):  [Read-Write] For post process materials, use BlendablePriorityOverride.
- ``override_subsurface_profile`` (bool):  [Read-Write] Defines if SubsurfaceProfile from this instance is used or it uses the parent one.
- ``parent`` (MaterialInterface):  [Read-Write] Parent material.
- ``phys_material`` (PhysicalMaterial):  [Read-Write] Physical material to use for this graphics material. Used for sounds, effects etc.
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

<a id="unreal.DynamicMaterialInstance.material_model_base"></a>

#### material_model_base

```python
@property
def material_model_base() -> DynamicMaterialModelBase
```

(DynamicMaterialModelBase):  [Read-Only]

<a id="unreal.DynamicMaterialInstance.material_model"></a>

#### material_model

```python
@property
def material_model() -> DynamicMaterialModelBase
```

deprecated: 'material_model' was renamed to 'material_model_base'.

<a id="unreal.DynamicMaterialInstance.get_material_model_base"></a>

#### get_material_model_base

```python
def get_material_model_base() -> DynamicMaterialModelBase
```

x.get_material_model_base() -> DynamicMaterialModelBase
Returns the Material Model associated with this Material Designer Material.

Returns:
    DynamicMaterialModelBase:

<a id="unreal.DynamicMaterialInstance.get_material_model"></a>

#### get_material_model

```python
def get_material_model() -> DynamicMaterialModel
```

x.get_material_model() -> DynamicMaterialModel
Resolves the base Material Model used with this Instance and returns it.

Returns:
    DynamicMaterialModel:

<a id="unreal.DynamicMaterialModelBase"></a>