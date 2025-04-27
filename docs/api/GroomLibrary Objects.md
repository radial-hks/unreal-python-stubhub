## GroomLibrary Objects

```python
class GroomLibrary(BlueprintFunctionLibrary)
```

Groom Blueprint Library

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomBlueprintLibrary.h

<a id="unreal.GroomLibrary.is_hair_strands_supported_in_world"></a>

#### is_hair_strands_supported_in_world

```python
@classmethod
def is_hair_strands_supported_in_world(cls,
                                       world_context_object: Object) -> bool
```

X.is_hair_strands_supported_in_world(world_context_object) -> bool
Check for strands support in the world of a given Actor Component

Args:
    world_context_object (Object): 

Returns:
    bool: true if strands are going to be rendered for the world's scene and false otherwise

<a id="unreal.GroomLibrary.create_new_groom_binding_asset_with_path"></a>

#### create_new_groom_binding_asset_with_path

```python
@classmethod
def create_new_groom_binding_asset_with_path(
        cls,
        desired_package_path: str,
        groom_asset: GroomAsset,
        skeletal_mesh: SkeletalMesh,
        num_interpolation_points: int = 100,
        source_skeletal_mesh_for_transfer: SkeletalMesh = None,
        matching_section: int = 0) -> GroomBindingAsset
```

X.create_new_groom_binding_asset_with_path(desired_package_path, groom_asset, skeletal_mesh, num_interpolation_points=100, source_skeletal_mesh_for_transfer=None, matching_section=0) -> GroomBindingAsset
Create a new groom binding asset within the contents space of the project.

Args:
    desired_package_path (str): The package path to use for the groom binding
    groom_asset (GroomAsset): Groom asset for binding
    skeletal_mesh (SkeletalMesh): Skeletal mesh on which the groom should be bound to
    num_interpolation_points (int32): Number of point used for RBF constraint (if used)
    source_skeletal_mesh_for_transfer (SkeletalMesh): Skeletal mesh on which the groom was authored. This should be used only if the skeletal mesh on which the groom is attached to, does not match the rest pose of the groom
    matching_section (int32): 

Returns:
    GroomBindingAsset:

<a id="unreal.GroomLibrary.create_new_groom_binding_asset"></a>

#### create_new_groom_binding_asset

```python
@classmethod
def create_new_groom_binding_asset(
        cls,
        groom_asset: GroomAsset,
        skeletal_mesh: SkeletalMesh,
        num_interpolation_points: int = 100,
        source_skeletal_mesh_for_transfer: SkeletalMesh = None,
        matching_section: int = 0) -> GroomBindingAsset
```

X.create_new_groom_binding_asset(groom_asset, skeletal_mesh, num_interpolation_points=100, source_skeletal_mesh_for_transfer=None, matching_section=0) -> GroomBindingAsset
Create a new groom binding asset within the contents space of the project. The asset name will be auto generated based on the groom asset name and the skeletal asset name

Args:
    groom_asset (GroomAsset): Groom asset for binding
    skeletal_mesh (SkeletalMesh): Skeletal mesh on which the groom should be bound to
    num_interpolation_points (int32): (Optional) Number of point used for RBF constraint
    source_skeletal_mesh_for_transfer (SkeletalMesh): (Optional) Skeletal mesh on which the groom was authored. This should be used only if the skeletal mesh on which the groom is attached to, does not match the rest pose of the groom
    matching_section (int32): 

Returns:
    GroomBindingAsset:

<a id="unreal.GroomLibrary.create_new_geometry_cache_groom_binding_asset_with_path"></a>

#### create_new_geometry_cache_groom_binding_asset_with_path

```python
@classmethod
def create_new_geometry_cache_groom_binding_asset_with_path(
        cls,
        desired_package_path: str,
        groom_asset: GroomAsset,
        geometry_cache: GeometryCache,
        num_interpolation_points: int = 100,
        source_geometry_cache_for_transfer: GeometryCache = None,
        matching_section: int = 0) -> GroomBindingAsset
```

X.create_new_geometry_cache_groom_binding_asset_with_path(desired_package_path, groom_asset, geometry_cache, num_interpolation_points=100, source_geometry_cache_for_transfer=None, matching_section=0) -> GroomBindingAsset
Create a new groom binding asset within the contents space of the project.

Args:
    desired_package_path (str): The package path to use for the groom binding
    groom_asset (GroomAsset): Groom asset for binding
    geometry_cache (GeometryCache): 
    num_interpolation_points (int32): Number of point used for RBF constraint (if used)
    source_geometry_cache_for_transfer (GeometryCache): 
    matching_section (int32): 

Returns:
    GroomBindingAsset:

<a id="unreal.GroomLibrary.create_new_geometry_cache_groom_binding_asset"></a>

#### create_new_geometry_cache_groom_binding_asset

```python
@classmethod
def create_new_geometry_cache_groom_binding_asset(
        cls,
        groom_asset: GroomAsset,
        geometry_cache: GeometryCache,
        num_interpolation_points: int = 100,
        source_geometry_cache_for_transfer: GeometryCache = None,
        matching_section: int = 0) -> GroomBindingAsset
```

X.create_new_geometry_cache_groom_binding_asset(groom_asset, geometry_cache, num_interpolation_points=100, source_geometry_cache_for_transfer=None, matching_section=0) -> GroomBindingAsset
Create a new groom binding asset within the contents space of the project. The asset name will be auto generated based on the groom asset name and the skeletal asset name

Args:
    groom_asset (GroomAsset): Groom asset for binding
    geometry_cache (GeometryCache): 
    num_interpolation_points (int32): (Optional) Number of point used for RBF constraint
    source_geometry_cache_for_transfer (GeometryCache): 
    matching_section (int32): 

Returns:
    GroomBindingAsset:

<a id="unreal.GroomCache"></a>