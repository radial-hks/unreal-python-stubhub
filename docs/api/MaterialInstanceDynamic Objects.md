## MaterialInstanceDynamic Objects

```python
class MaterialInstanceDynamic(MaterialInstance)
```

Material Instance Dynamic

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstanceDynamic.h

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

<a id="unreal.MaterialInstanceDynamic.set_vector_parameter_value_by_info"></a>

#### set_vector_parameter_value_by_info

```python
def set_vector_parameter_value_by_info(parameter_info: MaterialParameterInfo,
                                       value: LinearColor) -> None
```

x.set_vector_parameter_value_by_info(parameter_info, value) -> None
Set an MID vector parameter value, using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 
    value (LinearColor):

<a id="unreal.MaterialInstanceDynamic.set_vector_parameter_value"></a>

#### set_vector_parameter_value

```python
def set_vector_parameter_value(parameter_name: Name,
                               value: LinearColor) -> None
```

x.set_vector_parameter_value(parameter_name, value) -> None
Set an MID vector parameter value

Args:
    parameter_name (Name): 
    value (LinearColor):

<a id="unreal.MaterialInstanceDynamic.set_texture_parameter_value_by_info"></a>

#### set_texture_parameter_value_by_info

```python
def set_texture_parameter_value_by_info(parameter_info: MaterialParameterInfo,
                                        value: Texture) -> None
```

x.set_texture_parameter_value_by_info(parameter_info, value) -> None
Set an MID texture parameter value using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 
    value (Texture):

<a id="unreal.MaterialInstanceDynamic.set_texture_parameter_value"></a>

#### set_texture_parameter_value

```python
def set_texture_parameter_value(parameter_name: Name, value: Texture) -> None
```

x.set_texture_parameter_value(parameter_name, value) -> None
Set an MID texture parameter value

Args:
    parameter_name (Name): 
    value (Texture):

<a id="unreal.MaterialInstanceDynamic.set_sparse_volume_texture_parameter_value"></a>

#### set_sparse_volume_texture_parameter_value

```python
def set_sparse_volume_texture_parameter_value(
        parameter_name: Name, value: SparseVolumeTexture) -> None
```

x.set_sparse_volume_texture_parameter_value(parameter_name, value) -> None
Set an MID texture parameter value

Args:
    parameter_name (Name): 
    value (SparseVolumeTexture):

<a id="unreal.MaterialInstanceDynamic.set_scalar_parameter_value_by_info"></a>

#### set_scalar_parameter_value_by_info

```python
def set_scalar_parameter_value_by_info(parameter_info: MaterialParameterInfo,
                                       value: float) -> None
```

x.set_scalar_parameter_value_by_info(parameter_info, value) -> None
Set a MID scalar (float) parameter value using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 
    value (float):

<a id="unreal.MaterialInstanceDynamic.set_scalar_parameter_value"></a>

#### set_scalar_parameter_value

```python
def set_scalar_parameter_value(parameter_name: Name, value: float) -> None
```

x.set_scalar_parameter_value(parameter_name, value) -> None
Set a MID scalar (float) parameter value

Args:
    parameter_name (Name): 
    value (float):

<a id="unreal.MaterialInstanceDynamic.set_scalar_parameter_by_index"></a>

#### set_scalar_parameter_by_index

```python
def set_scalar_parameter_by_index(parameter_index: int, value: float) -> bool
```

x.set_scalar_parameter_by_index(parameter_index, value) -> bool
Use the cached value of OutParameterIndex from InitializeScalarParameterAndGetIndex to set the scalar parameter
ONLY on the exact same MID.  Do NOT presume the index can be used from one instance on another.  Only use this
pair of functions when optimization is critical; otherwise use either SetScalarParameterValueByInfo or
SetScalarParameterValue.

Args:
    parameter_index (int32): 
    value (float): 

Returns:
    bool:

<a id="unreal.MaterialInstanceDynamic.set_runtime_virtual_texture_parameter_value_by_info"></a>

#### set_runtime_virtual_texture_parameter_value_by_info

```python
def set_runtime_virtual_texture_parameter_value_by_info(
        parameter_info: MaterialParameterInfo,
        value: RuntimeVirtualTexture) -> None
```

x.set_runtime_virtual_texture_parameter_value_by_info(parameter_info, value) -> None
Set an MID texture parameter value using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 
    value (RuntimeVirtualTexture):

<a id="unreal.MaterialInstanceDynamic.set_runtime_virtual_texture_parameter_value"></a>

#### set_runtime_virtual_texture_parameter_value

```python
def set_runtime_virtual_texture_parameter_value(
        parameter_name: Name, value: RuntimeVirtualTexture) -> None
```

x.set_runtime_virtual_texture_parameter_value(parameter_name, value) -> None
Set an MID texture parameter value

Args:
    parameter_name (Name): 
    value (RuntimeVirtualTexture):

<a id="unreal.MaterialInstanceDynamic.set_double_vector_parameter_value"></a>

#### set_double_vector_parameter_value

```python
def set_double_vector_parameter_value(parameter_name: Name,
                                      value: Vector4) -> None
```

x.set_double_vector_parameter_value(parameter_name, value) -> None
Set an MID vector parameter value

Args:
    parameter_name (Name): 
    value (Vector4):

<a id="unreal.MaterialInstanceDynamic.interpolate_material_instance_parameters"></a>

#### interpolate_material_instance_parameters

```python
def interpolate_material_instance_parameters(source_a: MaterialInstance,
                                             source_b: MaterialInstance,
                                             alpha: float) -> None
```

x.interpolate_material_instance_parameters(source_a, source_b, alpha) -> None
Interpolates the scalar and vector parameters of this material instance based on two other material instances, and an alpha blending factor
The output is the object itself (this).
Supports the case SourceA==this || SourceB==this
Both material have to be from the same base material

Args:
    source_a (MaterialInstance): value that is used for Alpha=0, silently ignores the case if 0
    source_b (MaterialInstance): value that is used for Alpha=1, silently ignores the case if 0
    alpha (float): usually in the range 0..1, values outside the range extrapolate

<a id="unreal.MaterialInstanceDynamic.get_vector_parameter_value_by_info"></a>

#### get_vector_parameter_value_by_info

```python
def get_vector_parameter_value_by_info(
        parameter_info: MaterialParameterInfo) -> LinearColor
```

x.get_vector_parameter_value_by_info(parameter_info) -> LinearColor
Get the current MID vector parameter value, using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 

Returns:
    LinearColor:

<a id="unreal.MaterialInstanceDynamic.get_vector_parameter_value"></a>

#### get_vector_parameter_value

```python
def get_vector_parameter_value(parameter_name: Name) -> LinearColor
```

x.get_vector_parameter_value(parameter_name) -> LinearColor
Get the current MID vector parameter value

Args:
    parameter_name (Name): 

Returns:
    LinearColor:

<a id="unreal.MaterialInstanceDynamic.get_texture_parameter_value_by_info"></a>

#### get_texture_parameter_value_by_info

```python
def get_texture_parameter_value_by_info(
        parameter_info: MaterialParameterInfo) -> Texture
```

x.get_texture_parameter_value_by_info(parameter_info) -> Texture
Get the current MID texture parameter value, using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 

Returns:
    Texture:

<a id="unreal.MaterialInstanceDynamic.get_texture_parameter_value"></a>

#### get_texture_parameter_value

```python
def get_texture_parameter_value(parameter_name: Name) -> Texture
```

x.get_texture_parameter_value(parameter_name) -> Texture
Get the current MID texture parameter value

Args:
    parameter_name (Name): 

Returns:
    Texture:

<a id="unreal.MaterialInstanceDynamic.get_scalar_parameter_value_by_info"></a>

#### get_scalar_parameter_value_by_info

```python
def get_scalar_parameter_value_by_info(
        parameter_info: MaterialParameterInfo) -> float
```

x.get_scalar_parameter_value_by_info(parameter_info) -> float
Get the current scalar (float) parameter value from an MID, using MPI (to allow access to layer parameters)

Args:
    parameter_info (MaterialParameterInfo): 

Returns:
    float:

<a id="unreal.MaterialInstanceDynamic.get_scalar_parameter_value"></a>

#### get_scalar_parameter_value

```python
def get_scalar_parameter_value(parameter_name: Name) -> float
```

x.get_scalar_parameter_value(parameter_name) -> float
Get the current scalar (float) parameter value from an MID

Args:
    parameter_name (Name): 

Returns:
    float:

<a id="unreal.MaterialInstanceDynamic.copy_material_instance_parameters"></a>

#### copy_material_instance_parameters

```python
def copy_material_instance_parameters(
        source: MaterialInterface,
        quick_parameters_only: bool = False) -> None
```

x.copy_material_instance_parameters(source, quick_parameters_only=False) -> None
Copies over parameters given a material interface (copy each instance following the hierarchy)
Very slow implementation, avoid using at runtime. Hopefully we can replace it later with something like CopyInterpParameters()
The output is the object itself (this). Copying 'quick parameters only' will result in a much
faster copy process but will only copy dynamic scalar, vector and texture parameters on clients.

Args:
    source (MaterialInterface): 
    quick_parameters_only (bool): Copy scalar, vector and texture parameters only. Much faster but may not include required data

<a id="unreal.MaterialInstanceDynamic.initialize_scalar_parameter_and_get_index"></a>

#### initialize_scalar_parameter_and_get_index

```python
def initialize_scalar_parameter_and_get_index(parameter_name: Name,
                                              value: float) -> Optional[int]
```

x.initialize_scalar_parameter_and_get_index(parameter_name, value) -> int32 or None
Use this function to set an initial value and fetch the index for use in SetScalarParameterByIndex.  This
function should only be called once for a particular name, and then use SetScalarParameterByIndex for subsequent
calls.  However, beware using this except in cases where optimization is critical, which is generally only if
you're using an unusually high number of parameters in a material and setting a large number of parameters in the
same frame.  Also, if the material is changed in any way that can change the parameter list, the index can be
invalidated.

Args:
    parameter_name (Name): 
    value (float): 

Returns:
    int32 or None: 

    out_parameter_index (int32):

<a id="unreal.MaterialInstanceDynamic.copy_parameter_overrides"></a>

#### copy_parameter_overrides

```python
def copy_parameter_overrides(material_instance: MaterialInstance) -> None
```

x.copy_parameter_overrides(material_instance) -> None
Copy parameter values from another material instance. This will copy only
parameters explicitly overridden in that material instance!!

Args:
    material_instance (MaterialInstance):

<a id="unreal.MaterialParameterCollection"></a>