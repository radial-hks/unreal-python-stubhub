## MaterialInterface Objects

```python
class MaterialInterface(Object)
```

Material Interface

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Write] Importing data and options used for this material
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``editor_only_data`` (MaterialInterfaceEditorOnlyData):  [Read-Only]
- ``lightmass_settings`` (LightmassMaterialInterfaceSettings):  [Read-Write] The Lightmass settings for this object.
- ``neural_profile`` (NeuralProfile):  [Read-Write] Neural network profile. For internal usage, not editable/visible
- ``preview_mesh`` (SoftObjectPath):  [Read-Write] The mesh used by the material editor to preview the material.
- ``subsurface_profile`` (SubsurfaceProfile):  [Read-Write] SubsurfaceProfile, for Screen Space Subsurface Scattering..
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.MaterialInterface.subsurface_profile"></a>

#### subsurface_profile

```python
@property
def subsurface_profile() -> SubsurfaceProfile
```

(SubsurfaceProfile):  [Read-Only] SubsurfaceProfile, for Screen Space Subsurface Scattering..

<a id="unreal.MaterialInterface.neural_profile"></a>

#### neural_profile

```python
@property
def neural_profile() -> NeuralProfile
```

(NeuralProfile):  [Read-Only] Neural network profile. For internal usage, not editable/visible

<a id="unreal.MaterialInterface.set_force_mip_levels_to_be_resident"></a>

#### set_force_mip_levels_to_be_resident

```python
def set_force_mip_levels_to_be_resident(
        override_force_miplevels_to_be_resident: bool,
        force_miplevels_to_be_resident_value: bool,
        force_duration: float,
        cinematic_texture_groups: int = 0,
        fast_response: bool = False) -> None
```

x.set_force_mip_levels_to_be_resident(override_force_miplevels_to_be_resident, force_miplevels_to_be_resident_value, force_duration, cinematic_texture_groups=0, fast_response=False) -> None
Force the streaming system to disregard the normal logic for the specified duration and
instead always load all mip-levels for all textures used by this material.

Args:
    override_force_miplevels_to_be_resident (bool): Whether to use (true) or ignore (false) the bForceMiplevelsToBeResidentValue parameter.
    force_miplevels_to_be_resident_value (bool): true forces all mips to stream in. false lets other factors decide what to do with the mips.
    force_duration (float): Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. Negative value turns it off.
    cinematic_texture_groups (int32): Bitfield indicating texture groups that should use extra high-resolution mips
    fast_response (bool): USE WITH EXTREME CAUTION! Fast response textures incur sizable GT overhead and disturb streaming metric calculation. Avoid whenever possible.

<a id="unreal.MaterialInterface.get_physical_material_mask"></a>

#### get_physical_material_mask

```python
def get_physical_material_mask() -> PhysicalMaterialMask
```

x.get_physical_material_mask() -> PhysicalMaterialMask
Return a pointer to the physical material mask used by this material instance.

Returns:
    PhysicalMaterialMask: The physical material.

<a id="unreal.MaterialInterface.get_physical_material_from_map"></a>

#### get_physical_material_from_map

```python
def get_physical_material_from_map(index: int) -> PhysicalMaterial
```

x.get_physical_material_from_map(index) -> PhysicalMaterial
Return a pointer to the physical material from mask map at given index.

Args:
    index (int32): 

Returns:
    PhysicalMaterial: The physical material.

<a id="unreal.MaterialInterface.get_physical_material"></a>

#### get_physical_material

```python
def get_physical_material() -> PhysicalMaterial
```

x.get_physical_material() -> PhysicalMaterial
Return a pointer to the physical material used by this material instance.

Returns:
    PhysicalMaterial: The physical material.

<a id="unreal.MaterialInterface.get_parameter_info"></a>

#### get_parameter_info

```python
def get_parameter_info(
        association: MaterialParameterAssociation, parameter_name: Name,
        layer_function: MaterialFunctionInterface) -> MaterialParameterInfo
```

x.get_parameter_info(association, parameter_name, layer_function) -> MaterialParameterInfo
Get Parameter Info

Args:
    association (MaterialParameterAssociation): 
    parameter_name (Name): 
    layer_function (MaterialFunctionInterface): 

Returns:
    MaterialParameterInfo:

<a id="unreal.MaterialInterface.get_nanite_overide_material"></a>

#### get_nanite_overide_material

```python
def get_nanite_overide_material() -> MaterialInterface
```

x.get_nanite_overide_material() -> MaterialInterface
Get the associated nanite override material.

Returns:
    MaterialInterface:

<a id="unreal.MaterialInterface.get_blend_mode"></a>

#### get_blend_mode

```python
def get_blend_mode() -> BlendMode
```

x.get_blend_mode() -> BlendMode
Get Blend Mode

Returns:
    BlendMode:

<a id="unreal.MaterialInterface.get_base_material"></a>

#### get_base_material

```python
def get_base_material() -> Material
```

x.get_base_material() -> Material
Walks up parent chain and finds the base Material that this is an instance of. Just calls the virtual GetMaterial()

Returns:
    Material:

<a id="unreal.MaterialInterface.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.MaterialInterface.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.MaterialInterface.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.Material"></a>