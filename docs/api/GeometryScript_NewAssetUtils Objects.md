## GeometryScript_NewAssetUtils Objects

```python
class GeometryScript_NewAssetUtils(BlueprintFunctionLibrary)
```

Geometry Script Library Create New Asset Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: CreateNewAssetUtilityFunctions.h

<a id="unreal.GeometryScript_NewAssetUtils.create_unique_new_asset_path_name"></a>

#### create_unique_new_asset_path_name

```python
@classmethod
def create_unique_new_asset_path_name(
    cls,
    asset_folder_path: str,
    base_asset_name: str,
    options: GeometryScriptUniqueAssetNameOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[str, str, GeometryScriptOutcomePins]
```

X.create_unique_new_asset_path_name(asset_folder_path, base_asset_name, options, debug=None) -> (unique_asset_path_and_name=str, unique_asset_name=str, outcome=GeometryScriptOutcomePins)
Create Unique New Asset Path Name

Args:
    asset_folder_path (str): 
    base_asset_name (str): 
    options (GeometryScriptUniqueAssetNameOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    unique_asset_path_and_name (str): 

    unique_asset_name (str): 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_NewAssetUtils.create_new_volume_from_mesh"></a>

#### create_new_volume_from_mesh

```python
@classmethod
def create_new_volume_from_mesh(
    cls,
    from_dynamic_mesh: DynamicMesh,
    create_in_world: World,
    actor_transform: Transform,
    base_actor_name: str,
    options: GeometryScriptCreateNewVolumeFromMeshOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[Volume, World, GeometryScriptOutcomePins]
```

X.create_new_volume_from_mesh(from_dynamic_mesh, create_in_world, actor_transform, base_actor_name, options, debug=None) -> (Volume, create_in_world=World, outcome=GeometryScriptOutcomePins)
Create New Volume from Mesh

Args:
    from_dynamic_mesh (DynamicMesh): 
    create_in_world (World): 
    actor_transform (Transform): 
    base_actor_name (str): 
    options (GeometryScriptCreateNewVolumeFromMeshOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    create_in_world (World): 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_NewAssetUtils.create_new_texture2d_asset"></a>

#### create_new_texture2d_asset

```python
@classmethod
def create_new_texture2d_asset(
    cls,
    from_texture: Texture2D,
    asset_path_and_name: str,
    options: GeometryScriptCreateNewTexture2DAssetOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[Texture2D, GeometryScriptOutcomePins]
```

X.create_new_texture2d_asset(from_texture, asset_path_and_name, options, debug=None) -> (Texture2D, outcome=GeometryScriptOutcomePins)
Create New Texture 2DAsset

Args:
    from_texture (Texture2D): 
    asset_path_and_name (str): 
    options (GeometryScriptCreateNewTexture2DAssetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_NewAssetUtils.create_new_static_mesh_asset_from_mesh_lo_ds"></a>

#### create_new_static_mesh_asset_from_mesh_lo_ds

```python
@classmethod
def create_new_static_mesh_asset_from_mesh_lo_ds(
    cls,
    from_dynamic_mesh: Array[DynamicMesh],
    asset_path_and_name: str,
    options: GeometryScriptCreateNewStaticMeshAssetOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[StaticMesh, GeometryScriptOutcomePins]
```

X.create_new_static_mesh_asset_from_mesh_lo_ds(from_dynamic_mesh, asset_path_and_name, options, debug=None) -> (StaticMesh, outcome=GeometryScriptOutcomePins)
Create a new StaticMesh asset from a collection of LODs represented by an array of DynamicMeshes.
Save the asset at the AssetPathAndName location.

Args:
    from_dynamic_mesh (Array[DynamicMesh]): 
    asset_path_and_name (str): 
    options (GeometryScriptCreateNewStaticMeshAssetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_NewAssetUtils.create_new_static_mesh_asset_from_mesh"></a>

#### create_new_static_mesh_asset_from_mesh

```python
@classmethod
def create_new_static_mesh_asset_from_mesh(
    cls,
    from_dynamic_mesh: DynamicMesh,
    asset_path_and_name: str,
    options: GeometryScriptCreateNewStaticMeshAssetOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[StaticMesh, GeometryScriptOutcomePins]
```

X.create_new_static_mesh_asset_from_mesh(from_dynamic_mesh, asset_path_and_name, options, debug=None) -> (StaticMesh, outcome=GeometryScriptOutcomePins)
Create a new StaticMesh asset from a DynamicMesh. Save the asset at the AssetPathAndName location.

Args:
    from_dynamic_mesh (DynamicMesh): 
    asset_path_and_name (str): 
    options (GeometryScriptCreateNewStaticMeshAssetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_NewAssetUtils.create_new_skeletal_mesh_asset_from_mesh_lo_ds"></a>

#### create_new_skeletal_mesh_asset_from_mesh_lo_ds

```python
@classmethod
def create_new_skeletal_mesh_asset_from_mesh_lo_ds(
    cls,
    from_dynamic_mesh_lo_ds: Array[DynamicMesh],
    skeleton: Skeleton,
    asset_path_and_name: str,
    options: GeometryScriptCreateNewSkeletalMeshAssetOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[SkeletalMesh, GeometryScriptOutcomePins]
```

X.create_new_skeletal_mesh_asset_from_mesh_lo_ds(from_dynamic_mesh_lo_ds, skeleton, asset_path_and_name, options, debug=None) -> (SkeletalMesh, outcome=GeometryScriptOutcomePins)
Create a new SkeletalMesh asset from a collection of LODs represented by an array of DynamicMeshes and a Skeleton.
Save the asset at the AssetPathAndName location.

Args:
    from_dynamic_mesh_lo_ds (Array[DynamicMesh]): 
    skeleton (Skeleton): 
    asset_path_and_name (str): 
    options (GeometryScriptCreateNewSkeletalMeshAssetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeometryScript_NewAssetUtils.create_new_skeletal_mesh_asset_from_mesh"></a>

#### create_new_skeletal_mesh_asset_from_mesh

```python
@classmethod
def create_new_skeletal_mesh_asset_from_mesh(
    cls,
    from_dynamic_mesh: DynamicMesh,
    skeleton: Skeleton,
    asset_path_and_name: str,
    options: GeometryScriptCreateNewSkeletalMeshAssetOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[SkeletalMesh, GeometryScriptOutcomePins]
```

X.create_new_skeletal_mesh_asset_from_mesh(from_dynamic_mesh, skeleton, asset_path_and_name, options, debug=None) -> (SkeletalMesh, outcome=GeometryScriptOutcomePins)
Create a new SkeletalMesh asset from a DynamicMesh and a Skeleton.
Save the asset at the AssetPathAndName location.

Args:
    from_dynamic_mesh (DynamicMesh): 
    skeleton (Skeleton): 
    asset_path_and_name (str): 
    options (GeometryScriptCreateNewSkeletalMeshAssetOptions): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptOutcomePins: 

    outcome (GeometryScriptOutcomePins):

<a id="unreal.GeneratedDynamicMeshActor"></a>