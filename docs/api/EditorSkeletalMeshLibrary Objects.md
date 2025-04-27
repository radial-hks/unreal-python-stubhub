## EditorSkeletalMeshLibrary Objects

```python
class EditorSkeletalMeshLibrary(BlueprintFunctionLibrary)
```

Utility class to altering and analyzing a SkeletalMesh and use the common functionalities of the SkeletalMesh Editor.
The editor should not be in play in editor mode.

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorSkeletalMeshLibrary.h

<a id="unreal.EditorSkeletalMeshLibrary.strip_lod_geometry"></a>

#### strip_lod_geometry

```python
@classmethod
def strip_lod_geometry(cls, skeletal_mesh: SkeletalMesh, lod_index: int,
                       texture_mask: Texture2D, threshold: float) -> bool
```

X.strip_lod_geometry(skeletal_mesh, lod_index, texture_mask, threshold) -> bool
This function will strip all triangle in the specified LOD that don't have any UV area pointing on a black pixel in the TextureMask.
We use the UVChannel 0 to find the pixels in the texture.

Args:
    skeletal_mesh (SkeletalMesh): 
    lod_index (int32): 
    texture_mask (Texture2D): 
    threshold (float): 

Returns:
    bool:

<a id="unreal.EditorSkeletalMeshLibrary.set_lod_build_settings"></a>

#### set_lod_build_settings

```python
@classmethod
def set_lod_build_settings(cls, skeletal_mesh: SkeletalMesh, lod_index: int,
                           build_options: SkeletalMeshBuildSettings) -> None
```

X.set_lod_build_settings(skeletal_mesh, lod_index, build_options) -> None
Set Lod Build Settings
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 
    lod_index (int32): 
    build_options (SkeletalMeshBuildSettings):

<a id="unreal.EditorSkeletalMeshLibrary.rename_socket"></a>

#### rename_socket

```python
@classmethod
def rename_socket(cls, skeletal_mesh: SkeletalMesh, old_name: Name,
                  new_name: Name) -> bool
```

X.rename_socket(skeletal_mesh, old_name, new_name) -> bool
Rename Socket
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 
    old_name (Name): 
    new_name (Name): 

Returns:
    bool:

<a id="unreal.EditorSkeletalMeshLibrary.remove_lo_ds"></a>

#### remove_lo_ds

```python
@classmethod
def remove_lo_ds(cls, skeletal_mesh: SkeletalMesh,
                 to_remove_lo_ds: Array[int]) -> bool
```

X.remove_lo_ds(skeletal_mesh, to_remove_lo_ds) -> bool
Remove all the specified LODs. This function will remove all the valid LODs in the list.
Valid LOD is any LOD greater then 0 that exist in the skeletalmesh. We cannot remove the base LOD 0.

Args:
    skeletal_mesh (SkeletalMesh): The mesh inside which we are renaming a socket
    to_remove_lo_ds (Array[int32]): The LODs we need to remove

Returns:
    bool: true if the successfully remove all the LODs. False otherwise, but evedn if it return false it will have removed all valid LODs.

<a id="unreal.EditorSkeletalMeshLibrary.reimport_all_custom_lo_ds"></a>

#### reimport_all_custom_lo_ds

```python
@classmethod
def reimport_all_custom_lo_ds(cls, skeletal_mesh: SkeletalMesh) -> bool
```

X.reimport_all_custom_lo_ds(skeletal_mesh) -> bool
Reimport All Custom LODs
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    bool:

<a id="unreal.EditorSkeletalMeshLibrary.regenerate_lod"></a>

#### regenerate_lod

```python
@classmethod
def regenerate_lod(cls,
                   skeletal_mesh: SkeletalMesh,
                   new_lod_count: int = 0,
                   regenerate_even_if_imported: bool = False,
                   generate_base_lod: bool = False) -> bool
```

X.regenerate_lod(skeletal_mesh, new_lod_count=0, regenerate_even_if_imported=False, generate_base_lod=False) -> bool
Regenerate LOD
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 
    new_lod_count (int32): 
    regenerate_even_if_imported (bool): 
    generate_base_lod (bool): 

Returns:
    bool:

<a id="unreal.EditorSkeletalMeshLibrary.import_lod"></a>

#### import_lod

```python
@classmethod
def import_lod(cls, base_mesh: SkeletalMesh, lod_index: int,
               source_filename: str) -> int
```

X.import_lod(base_mesh, lod_index, source_filename) -> int32
Import LOD
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    base_mesh (SkeletalMesh): 
    lod_index (int32): 
    source_filename (str): 

Returns:
    int32:

<a id="unreal.EditorSkeletalMeshLibrary.get_num_verts"></a>

#### get_num_verts

```python
@classmethod
def get_num_verts(cls, skeletal_mesh: SkeletalMesh, lod_index: int) -> int
```

X.get_num_verts(skeletal_mesh, lod_index) -> int32
Get Num Verts
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 
    lod_index (int32): 

Returns:
    int32:

<a id="unreal.EditorSkeletalMeshLibrary.get_lod_count"></a>

#### get_lod_count

```python
@classmethod
def get_lod_count(cls, skeletal_mesh: SkeletalMesh) -> int
```

X.get_lod_count(skeletal_mesh) -> int32
Get LODCount
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    int32:

<a id="unreal.EditorSkeletalMeshLibrary.get_lod_build_settings"></a>

#### get_lod_build_settings

```python
@classmethod
def get_lod_build_settings(cls, skeletal_mesh: SkeletalMesh,
                           lod_index: int) -> SkeletalMeshBuildSettings
```

X.get_lod_build_settings(skeletal_mesh, lod_index) -> SkeletalMeshBuildSettings
Get Lod Build Settings
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Skeletal Mesh Editor Subsystem

Args:
    skeletal_mesh (SkeletalMesh): 
    lod_index (int32): 

Returns:
    SkeletalMeshBuildSettings: 

    out_build_options (SkeletalMeshBuildSettings):

<a id="unreal.EditorSkeletalMeshLibrary.create_physics_asset"></a>

#### create_physics_asset

```python
@classmethod
def create_physics_asset(cls, skeletal_mesh: SkeletalMesh) -> PhysicsAsset
```

X.create_physics_asset(skeletal_mesh) -> PhysicsAsset
This function creates a PhysicsAsset for the given SkeletalMesh with the same settings as if it were created through FBX import

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    PhysicsAsset:

<a id="unreal.SkeletalMeshUtilitiesLibrary"></a>