## GroomAsset Objects

```python
class GroomAsset(Object)
```

Implements an asset that can be used to store hair strands

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] Asset data to be used when re-importing
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``auto_lod_bias`` (float):  [Read-Write] When LOD mode is set to Auto, decrease the screen size at which curves reduction will occur.
- ``disable_below_min_lod_stripping`` (PerPlatformBool):  [Read-Write]
- ``enable_global_interpolation`` (bool):  [Read-Write] Enable radial basis function interpolation to be used instead of the local skin rigid transform (WIP)
- ``enable_simulation_cache`` (bool):  [Read-Write] Enable guide-cache support. This allows to attach a simulation-cache dynamically at runtime
- ``hair_groups_cards`` (Array[HairGroupsCardsSourceDescription]):  [Read-Write]
- ``hair_groups_info`` (Array[HairGroupInfoWithVisibility]):  [Read-Write]
- ``hair_groups_interpolation`` (Array[HairGroupsInterpolation]):  [Read-Write]
- ``hair_groups_lod`` (Array[HairGroupsLOD]):  [Read-Write]
- ``hair_groups_materials`` (Array[HairGroupsMaterial]):  [Read-Write]
- ``hair_groups_meshes`` (Array[HairGroupsMeshesSourceDescription]):  [Read-Write]
- ``hair_groups_physics`` (Array[HairGroupsPhysics]):  [Read-Write]
- ``hair_groups_rendering`` (Array[HairGroupsRendering]):  [Read-Write]
- ``hair_interpolation_type`` (GroomInterpolationType):  [Read-Write] Type of interpolation used (WIP)
- ``lod_mode`` (GroomLODMode):  [Read-Write] Define how LOD adapts curves & points for strands geometry. Auto: adapts the curve count based on screen coverage. Manual: use the discrete LOD created for each groups
- ``min_lod`` (PerPlatformInt):  [Read-Write]
- ``rigged_skeletal_mesh`` (SkeletalMesh):  [Read-Only]

<a id="unreal.GroomAsset.hair_groups_rendering"></a>

#### hair_groups_rendering

```python
@property
def hair_groups_rendering() -> Array[HairGroupsRendering]
```

(Array[HairGroupsRendering]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_rendering"></a>

#### hair_groups_rendering

```python
@hair_groups_rendering.setter
def hair_groups_rendering(value: Array[HairGroupsRendering]) -> None
```

<a id="unreal.GroomAsset.hair_groups_physics"></a>

#### hair_groups_physics

```python
@property
def hair_groups_physics() -> Array[HairGroupsPhysics]
```

(Array[HairGroupsPhysics]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_physics"></a>

#### hair_groups_physics

```python
@hair_groups_physics.setter
def hair_groups_physics(value: Array[HairGroupsPhysics]) -> None
```

<a id="unreal.GroomAsset.hair_groups_interpolation"></a>

#### hair_groups_interpolation

```python
@property
def hair_groups_interpolation() -> Array[HairGroupsInterpolation]
```

(Array[HairGroupsInterpolation]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_interpolation"></a>

#### hair_groups_interpolation

```python
@hair_groups_interpolation.setter
def hair_groups_interpolation(value: Array[HairGroupsInterpolation]) -> None
```

<a id="unreal.GroomAsset.hair_groups_lod"></a>

#### hair_groups_lod

```python
@property
def hair_groups_lod() -> Array[HairGroupsLOD]
```

(Array[HairGroupsLOD]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_lod"></a>

#### hair_groups_lod

```python
@hair_groups_lod.setter
def hair_groups_lod(value: Array[HairGroupsLOD]) -> None
```

<a id="unreal.GroomAsset.hair_groups_cards"></a>

#### hair_groups_cards

```python
@property
def hair_groups_cards() -> Array[HairGroupsCardsSourceDescription]
```

(Array[HairGroupsCardsSourceDescription]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_cards"></a>

#### hair_groups_cards

```python
@hair_groups_cards.setter
def hair_groups_cards(value: Array[HairGroupsCardsSourceDescription]) -> None
```

<a id="unreal.GroomAsset.hair_groups_meshes"></a>

#### hair_groups_meshes

```python
@property
def hair_groups_meshes() -> Array[HairGroupsMeshesSourceDescription]
```

(Array[HairGroupsMeshesSourceDescription]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_meshes"></a>

#### hair_groups_meshes

```python
@hair_groups_meshes.setter
def hair_groups_meshes(
        value: Array[HairGroupsMeshesSourceDescription]) -> None
```

<a id="unreal.GroomAsset.hair_groups_materials"></a>

#### hair_groups_materials

```python
@property
def hair_groups_materials() -> Array[HairGroupsMaterial]
```

(Array[HairGroupsMaterial]):  [Read-Write]

<a id="unreal.GroomAsset.hair_groups_materials"></a>

#### hair_groups_materials

```python
@hair_groups_materials.setter
def hair_groups_materials(value: Array[HairGroupsMaterial]) -> None
```

<a id="unreal.GroomAsset.enable_global_interpolation"></a>

#### enable_global_interpolation

```python
@property
def enable_global_interpolation() -> bool
```

(bool):  [Read-Write] Enable radial basis function interpolation to be used instead of the local skin rigid transform (WIP)

<a id="unreal.GroomAsset.enable_global_interpolation"></a>

#### enable_global_interpolation

```python
@enable_global_interpolation.setter
def enable_global_interpolation(value: bool) -> None
```

<a id="unreal.GroomAsset.enable_simulation_cache"></a>

#### enable_simulation_cache

```python
@property
def enable_simulation_cache() -> bool
```

(bool):  [Read-Write] Enable guide-cache support. This allows to attach a simulation-cache dynamically at runtime

<a id="unreal.GroomAsset.enable_simulation_cache"></a>

#### enable_simulation_cache

```python
@enable_simulation_cache.setter
def enable_simulation_cache(value: bool) -> None
```

<a id="unreal.GroomAsset.hair_interpolation_type"></a>

#### hair_interpolation_type

```python
@property
def hair_interpolation_type() -> GroomInterpolationType
```

(GroomInterpolationType):  [Read-Write] Type of interpolation used (WIP)

<a id="unreal.GroomAsset.hair_interpolation_type"></a>

#### hair_interpolation_type

```python
@hair_interpolation_type.setter
def hair_interpolation_type(value: GroomInterpolationType) -> None
```

<a id="unreal.GroomAsset.rigged_skeletal_mesh"></a>

#### rigged_skeletal_mesh

```python
@property
def rigged_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Only]

<a id="unreal.GroomAsset.deformed_skeletal_mesh"></a>

#### deformed_skeletal_mesh

```python
@property
def deformed_skeletal_mesh() -> SkeletalMesh
```

deprecated: 'deformed_skeletal_mesh' was renamed to 'rigged_skeletal_mesh'.

<a id="unreal.GroomAsset.has_asset_user_data_of_class"></a>

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

<a id="unreal.GroomAsset.get_asset_user_data_of_class"></a>

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

<a id="unreal.GroomAsset.add_asset_user_data_of_class"></a>

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

<a id="unreal.HairStrandsAsset"></a>