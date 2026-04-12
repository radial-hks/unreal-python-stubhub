## MaterialInstance Objects

```python
class MaterialInstance(MaterialInterface)
```

Material Instance

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstance.h

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

<a id="unreal.MaterialInstance.phys_material"></a>

#### phys\_material

```python
@property
def phys_material() -> PhysicalMaterial
```

(PhysicalMaterial):  [Read-Write] Physical material to use for this graphics material. Used for sounds, effects etc.

<a id="unreal.MaterialInstance.phys_material"></a>

#### phys\_material

```python
@phys_material.setter
def phys_material(value: PhysicalMaterial) -> None
```

<a id="unreal.MaterialInstance.parent"></a>

#### parent

```python
@property
def parent() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] Parent material.

<a id="unreal.MaterialInstance.override_subsurface_profile"></a>

#### override\_subsurface\_profile

```python
@property
def override_subsurface_profile() -> bool
```

(bool):  [Read-Only] Defines if SubsurfaceProfile from this instance is used or it uses the parent one.

<a id="unreal.MaterialInstance.override_blendable_location"></a>

#### override\_blendable\_location

```python
@property
def override_blendable_location() -> bool
```

(bool):  [Read-Write] For post process materials, use BlendableLocationOverride.

<a id="unreal.MaterialInstance.override_blendable_location"></a>

#### override\_blendable\_location

```python
@override_blendable_location.setter
def override_blendable_location(value: bool) -> None
```

<a id="unreal.MaterialInstance.override_blendable_priority"></a>

#### override\_blendable\_priority

```python
@property
def override_blendable_priority() -> bool
```

(bool):  [Read-Write] For post process materials, use BlendablePriorityOverride.

<a id="unreal.MaterialInstance.override_blendable_priority"></a>

#### override\_blendable\_priority

```python
@override_blendable_priority.setter
def override_blendable_priority(value: bool) -> None
```

<a id="unreal.MaterialInstance.blendable_location_override"></a>

#### blendable\_location\_override

```python
@property
def blendable_location_override() -> BlendableLocation
```

(BlendableLocation):  [Read-Write]

<a id="unreal.MaterialInstance.blendable_location_override"></a>

#### blendable\_location\_override

```python
@blendable_location_override.setter
def blendable_location_override(value: BlendableLocation) -> None
```

<a id="unreal.MaterialInstance.blendable_priority_override"></a>

#### blendable\_priority\_override

```python
@property
def blendable_priority_override() -> int
```

(int32):  [Read-Write]

<a id="unreal.MaterialInstance.blendable_priority_override"></a>

#### blendable\_priority\_override

```python
@blendable_priority_override.setter
def blendable_priority_override(value: int) -> None
```

<a id="unreal.MaterialInstance.scalar_parameter_values"></a>

#### scalar\_parameter\_values

```python
@property
def scalar_parameter_values() -> Array[ScalarParameterValue]
```

(Array[ScalarParameterValue]):  [Read-Only] Scalar parameters.

<a id="unreal.MaterialInstance.vector_parameter_values"></a>

#### vector\_parameter\_values

```python
@property
def vector_parameter_values() -> Array[VectorParameterValue]
```

(Array[VectorParameterValue]):  [Read-Only] Vector parameters.

<a id="unreal.MaterialInstance.double_vector_parameter_values"></a>

#### double\_vector\_parameter\_values

```python
@property
def double_vector_parameter_values() -> Array[DoubleVectorParameterValue]
```

(Array[DoubleVectorParameterValue]):  [Read-Only] DoubleVector parameters.

<a id="unreal.MaterialInstance.texture_parameter_values"></a>

#### texture\_parameter\_values

```python
@property
def texture_parameter_values() -> Array[TextureParameterValue]
```

(Array[TextureParameterValue]):  [Read-Only] Texture parameters.

<a id="unreal.MaterialInstance.texture_collection_parameter_values"></a>

#### texture\_collection\_parameter\_values

```python
@property
def texture_collection_parameter_values(
) -> Array[TextureCollectionParameterValue]
```

(Array[TextureCollectionParameterValue]):  [Read-Only] Texture Collection parameters.

<a id="unreal.MaterialInstance.runtime_virtual_texture_parameter_values"></a>

#### runtime\_virtual\_texture\_parameter\_values

```python
@property
def runtime_virtual_texture_parameter_values(
) -> Array[RuntimeVirtualTextureParameterValue]
```

(Array[RuntimeVirtualTextureParameterValue]):  [Read-Only] RuntimeVirtualTexture parameters.

<a id="unreal.MaterialInstance.sparse_volume_texture_parameter_values"></a>

#### sparse\_volume\_texture\_parameter\_values

```python
@property
def sparse_volume_texture_parameter_values(
) -> Array[SparseVolumeTextureParameterValue]
```

(Array[SparseVolumeTextureParameterValue]):  [Read-Only] Sparse Volume Texture parameters.

<a id="unreal.MaterialInstance.font_parameter_values"></a>

#### font\_parameter\_values

```python
@property
def font_parameter_values() -> Array[FontParameterValue]
```

(Array[FontParameterValue]):  [Read-Only] Font parameters.

<a id="unreal.MaterialInstanceConstant"></a>