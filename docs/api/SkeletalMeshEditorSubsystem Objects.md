## SkeletalMeshEditorSubsystem Objects

```python
class SkeletalMeshEditorSubsystem(EditorSubsystem)
```

USkeletalMeshEditorSubsystem
Subsystem for exposing skeletal mesh functionality to scripts

**C++ Source:**

- **Module**: SkeletalMeshEditor
- **File**: SkeletalMeshEditorSubsystem.h

<a id="unreal.SkeletalMeshEditorSubsystem.set_section_visible_in_ray_tracing"></a>

#### set_section_visible_in_ray_tracing

```python
def set_section_visible_in_ray_tracing(skeletal_mesh: SkeletalMesh,
                                       lod_index: int, section_index: int,
                                       visible_in_ray_tracing: bool) -> bool
```

x.set_section_visible_in_ray_tracing(skeletal_mesh, lod_index, section_index, visible_in_ray_tracing) -> bool
Set bVisibleInRayTracing for a section of a LOD of a Skeletal Mesh.

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.
    visible_in_ray_tracing (bool): The function will set the bVisibleInRayTracing used by the section

Returns:
    bool: false if invalid mesh or LOD index or section index.

<a id="unreal.SkeletalMeshEditorSubsystem.set_section_recompute_tangents_vertex_mask_channel"></a>

#### set_section_recompute_tangents_vertex_mask_channel

```python
def set_section_recompute_tangents_vertex_mask_channel(
        skeletal_mesh: SkeletalMesh, lod_index: int, section_index: int,
        recompute_tangents_vertex_mask_channel: int) -> bool
```

x.set_section_recompute_tangents_vertex_mask_channel(skeletal_mesh, lod_index, section_index, recompute_tangents_vertex_mask_channel) -> bool
Set RecomputeTangentsVertexMaskChannel for a section of a LOD of a Skeletal Mesh.

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.
    recompute_tangents_vertex_mask_channel (uint8): The function will set the RecomputeTangentsVertexMaskChannel used by the section

Returns:
    bool: false if invalid mesh or LOD index or section index.

<a id="unreal.SkeletalMeshEditorSubsystem.set_section_recompute_tangent"></a>

#### set_section_recompute_tangent

```python
def set_section_recompute_tangent(skeletal_mesh: SkeletalMesh, lod_index: int,
                                  section_index: int,
                                  recompute_tangent: bool) -> bool
```

x.set_section_recompute_tangent(skeletal_mesh, lod_index, section_index, recompute_tangent) -> bool
Set bRecomputeTangent for a section of a LOD of a Skeletal Mesh.

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.
    recompute_tangent (bool): The function will set the bRecomputeTangent used by the section

Returns:
    bool: false if invalid mesh or LOD index or section index.

<a id="unreal.SkeletalMeshEditorSubsystem.set_section_cast_shadow"></a>

#### set_section_cast_shadow

```python
def set_section_cast_shadow(skeletal_mesh: SkeletalMesh, lod_index: int,
                            section_index: int, cast_shadow: bool) -> bool
```

x.set_section_cast_shadow(skeletal_mesh, lod_index, section_index, cast_shadow) -> bool
Set bCastShadow for a section of a LOD of a Skeletal Mesh.

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.
    cast_shadow (bool): The function will set the bCastShadow used by the section

Returns:
    bool: false if invalid mesh or LOD index or section index.

<a id="unreal.SkeletalMeshEditorSubsystem.set_lod_build_settings"></a>

#### set_lod_build_settings

```python
@classmethod
def set_lod_build_settings(cls, skeletal_mesh: SkeletalMesh, lod_index: int,
                           build_options: SkeletalMeshBuildSettings) -> None
```

X.set_lod_build_settings(skeletal_mesh, lod_index, build_options) -> None
Set the LOD build options for the specified LOD index.

Args:
    skeletal_mesh (SkeletalMesh): Mesh to process.
    lod_index (int32): The LOD we will apply the build settings.
    build_options (SkeletalMeshBuildSettings): The build settings we want to apply to the LOD.

<a id="unreal.SkeletalMeshEditorSubsystem.rename_socket"></a>

#### rename_socket

```python
@classmethod
def rename_socket(cls, skeletal_mesh: SkeletalMesh, old_name: Name,
                  new_name: Name) -> bool
```

X.rename_socket(skeletal_mesh, old_name, new_name) -> bool
Rename a socket within a skeleton

Args:
    skeletal_mesh (SkeletalMesh): The mesh inside which we are renaming a socket
    old_name (Name): The old name of the socket
    new_name (Name): The new name of the socket

Returns:
    bool: true if the renaming succeeded.

<a id="unreal.SkeletalMeshEditorSubsystem.reimport_all_custom_lo_ds"></a>

#### reimport_all_custom_lo_ds

```python
@classmethod
def reimport_all_custom_lo_ds(cls, skeletal_mesh: SkeletalMesh) -> bool
```

X.reimport_all_custom_lo_ds(skeletal_mesh) -> bool
Re-import the specified skeletal mesh and all the custom LODs.

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    bool: true if re-import works, false otherwise see log for explanation.

<a id="unreal.SkeletalMeshEditorSubsystem.regenerate_lod"></a>

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
Regenerate LODs of the mesh

Args:
    skeletal_mesh (SkeletalMesh): The mesh that will regenerate LOD
    new_lod_count (int32): Set valid value (>0) if you want to change LOD count. Otherwise, it will use the current LOD and regenerate
    regenerate_even_if_imported (bool): If this is true, it only regenerate even if this LOD was imported before If false, it will regenerate for only previously auto generated ones
    generate_base_lod (bool): If this is true and there is some reduction data, the base LOD will be reduce according to the settings

Returns:
    bool: true if succeed. If mesh reduction is not available this will return false.

<a id="unreal.SkeletalMeshEditorSubsystem.is_physics_asset_compatible"></a>

#### is_physics_asset_compatible

```python
@classmethod
def is_physics_asset_compatible(cls, target_mesh: SkeletalMesh,
                                physics_asset: PhysicsAsset) -> bool
```

X.is_physics_asset_compatible(target_mesh, physics_asset) -> bool
Checks whether a physics asset is compatible with the given SkeletalMesh

Args:
    target_mesh (SkeletalMesh): The mesh to test for compatibility
    physics_asset (PhysicsAsset): The PhysicsAsset to test for compatibility

Returns:
    bool: Whether the physics asset is compatible with the target SkeletalMesh

<a id="unreal.SkeletalMeshEditorSubsystem.import_lod"></a>

#### import_lod

```python
@classmethod
def import_lod(cls, base_mesh: SkeletalMesh, lod_index: int,
               source_filename: str) -> int
```

X.import_lod(base_mesh, lod_index, source_filename) -> int32
Import or re-import a LOD into the specified base mesh. If the LOD do not exist it will import it and add it to the base static mesh. If the LOD already exist it will re-import the specified LOD.

Args:
    base_mesh (SkeletalMesh): 
    lod_index (int32): 
    source_filename (str): 

Returns:
    int32: The index of the LOD that was imported or re-imported. Will return INDEX_NONE if anything goes bad.

<a id="unreal.SkeletalMeshEditorSubsystem.get_section_visible_in_ray_tracing"></a>

#### get_section_visible_in_ray_tracing

```python
def get_section_visible_in_ray_tracing(skeletal_mesh: SkeletalMesh,
                                       lod_index: int,
                                       section_index: int) -> Optional[bool]
```

x.get_section_visible_in_ray_tracing(skeletal_mesh, lod_index, section_index) -> bool or None
Get bVisibleInRayTracing from a section of a LOD of a Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.

Returns:
    bool or None: false if invalid mesh or LOD index or section index.

    out_visible_in_ray_tracing (bool): The function will set the bVisibleInRayTracing used by the section

<a id="unreal.SkeletalMeshEditorSubsystem.get_section_recompute_tangents_vertex_mask_channel"></a>

#### get_section_recompute_tangents_vertex_mask_channel

```python
def get_section_recompute_tangents_vertex_mask_channel(
        skeletal_mesh: SkeletalMesh, lod_index: int,
        section_index: int) -> Optional[int]
```

x.get_section_recompute_tangents_vertex_mask_channel(skeletal_mesh, lod_index, section_index) -> uint8 or None
Get RecomputeTangentsVertexMaskChannel from a section of a LOD of a Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.

Returns:
    uint8 or None: false if invalid mesh or LOD index or section index.

    out_recompute_tangents_vertex_mask_channel (uint8): The function will set the RecomputeTangentsVertexMaskChannel used by the section

<a id="unreal.SkeletalMeshEditorSubsystem.get_section_recompute_tangent"></a>

#### get_section_recompute_tangent

```python
def get_section_recompute_tangent(skeletal_mesh: SkeletalMesh, lod_index: int,
                                  section_index: int) -> Optional[bool]
```

x.get_section_recompute_tangent(skeletal_mesh, lod_index, section_index) -> bool or None
Get bRecomputeTangent from a section of a LOD of a Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.

Returns:
    bool or None: false if invalid mesh or LOD index or section index.

    out_recompute_tangent (bool): The function will set the bRecomputeTangent used by the section

<a id="unreal.SkeletalMeshEditorSubsystem.get_section_cast_shadow"></a>

#### get_section_cast_shadow

```python
def get_section_cast_shadow(skeletal_mesh: SkeletalMesh, lod_index: int,
                            section_index: int) -> Optional[bool]
```

x.get_section_cast_shadow(skeletal_mesh, lod_index, section_index) -> bool or None
Get bCastShadow from a section of a LOD of a Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.
    section_index (int32): Index of the LOD section.

Returns:
    bool or None: false if invalid mesh or LOD index or section index.

    out_cast_shadow (bool): The function will set the bCastShadow used by the section

<a id="unreal.SkeletalMeshEditorSubsystem.get_num_verts"></a>

#### get_num_verts

```python
def get_num_verts(skeletal_mesh: SkeletalMesh, lod_index: int) -> int
```

x.get_num_verts(skeletal_mesh, lod_index) -> int32
Get number of mesh vertices for an LOD of a Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.

Returns:
    int32: Number of vertices. Returns 0 if invalid mesh or LOD index.

<a id="unreal.SkeletalMeshEditorSubsystem.get_num_sections"></a>

#### get_num_sections

```python
def get_num_sections(skeletal_mesh: SkeletalMesh, lod_index: int) -> int
```

x.get_num_sections(skeletal_mesh, lod_index) -> int32
Get number of sections for a LOD of a Skeletal Mesh

Args:
    skeletal_mesh (SkeletalMesh): Mesh to get number of vertices from.
    lod_index (int32): Index of the mesh LOD.

Returns:
    int32: Number of sections. Returns INDEX_NONE if invalid mesh or LOD index.

<a id="unreal.SkeletalMeshEditorSubsystem.get_lod_material_slot"></a>

#### get_lod_material_slot

```python
def get_lod_material_slot(skeletal_mesh: SkeletalMesh, lod_index: int,
                          section_index: int) -> int
```

x.get_lod_material_slot(skeletal_mesh, lod_index, section_index) -> int32
Gets the material slot used for a specific LOD section.

Args:
    skeletal_mesh (SkeletalMesh): SkeletalMesh to get the material index from.
    lod_index (int32): Index of the StaticMesh LOD.
    section_index (int32): Index of the StaticMesh Section.

Returns:
    int32: MaterialSlotIndex   Index of the material slot used by the section or INDEX_NONE in case of error.

<a id="unreal.SkeletalMeshEditorSubsystem.get_lod_count"></a>

#### get_lod_count

```python
@classmethod
def get_lod_count(cls, skeletal_mesh: SkeletalMesh) -> int
```

X.get_lod_count(skeletal_mesh) -> int32
Retrieve the number of LOD contain in the specified skeletal mesh.

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    int32: The LOD number.

<a id="unreal.SkeletalMeshEditorSubsystem.get_lod_build_settings"></a>

#### get_lod_build_settings

```python
@classmethod
def get_lod_build_settings(cls, skeletal_mesh: SkeletalMesh,
                           lod_index: int) -> SkeletalMeshBuildSettings
```

X.get_lod_build_settings(skeletal_mesh, lod_index) -> SkeletalMeshBuildSettings
Copy the build options with the specified LOD build settings.

Args:
    skeletal_mesh (SkeletalMesh): Mesh to process.
    lod_index (int32): The LOD we get the reduction settings.

Returns:
    SkeletalMeshBuildSettings: 

    out_build_options (SkeletalMeshBuildSettings): The build settings where we copy the build options.

<a id="unreal.SkeletalMeshEditorSubsystem.create_physics_asset"></a>

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

<a id="unreal.SkeletalMeshEditorSubsystem.assign_physics_asset"></a>

#### assign_physics_asset

```python
@classmethod
def assign_physics_asset(cls, target_mesh: SkeletalMesh,
                         physics_asset: PhysicsAsset) -> bool
```

X.assign_physics_asset(target_mesh, physics_asset) -> bool
Assigns a PhysicsAsset to the given SkeletalMesh if it is compatible. Passing
nullptr / None as the physics asset will always succeed and will clear the
physics asset assignment for the target SkeletalMesh

Args:
    target_mesh (SkeletalMesh): The mesh to attempt to assign the PhysicsAsset to
    physics_asset (PhysicsAsset): The physics asset to assign to the provided mesh (or nullptr/None)

Returns:
    bool: Whether the physics asset was successfully assigned to the mesh

<a id="unreal.StaticMeshEditorSubsystem"></a>