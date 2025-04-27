## StaticMeshEditorSubsystem Objects

```python
class StaticMeshEditorSubsystem(EditorSubsystem)
```

UStaticMeshEditorSubsystem
Subsystem for exposing static mesh functionality to scripts

**C++ Source:**

- **Module**: StaticMeshEditor
- **File**: StaticMeshEditorSubsystem.h

<a id="unreal.StaticMeshEditorSubsystem.set_nanite_settings"></a>

#### set_nanite_settings

```python
def set_nanite_settings(static_mesh: StaticMesh,
                        nanite_settings: MeshNaniteSettings,
                        apply_changes: bool = True) -> None
```

x.set_nanite_settings(static_mesh, nanite_settings, apply_changes=True) -> None
Get the Nanite Settings for the mesh

Args:
    static_mesh (StaticMesh): Mesh to update nanite settings for
    nanite_settings (MeshNaniteSettings): Settings with which to update the mesh
    apply_changes (bool): Indicates if changes must be applied or not.

<a id="unreal.StaticMeshEditorSubsystem.set_lods_with_notification"></a>

#### set_lods_with_notification

```python
def set_lods_with_notification(static_mesh: StaticMesh,
                               reduction_options: StaticMeshReductionOptions,
                               apply_changes: bool) -> int
```

x.set_lods_with_notification(static_mesh, reduction_options, apply_changes) -> int32
Remove then add LODs on a static mesh.
The static mesh must have at least LOD 0.
The LOD 0 of the static mesh is kept after removal.
The build settings of LOD 0 will be applied to all subsequent LODs.

Args:
    static_mesh (StaticMesh): Mesh to process.
    reduction_options (StaticMeshReductionOptions): Options on how to generate LODs on the mesh.
    apply_changes (bool): Indicates if change must be notified.

Returns:
    int32: the number of LODs generated on the input mesh. An negative value indicates that the reduction could not be performed. See log for explanation. No action will be performed if ReductionOptions.ReductionSettings is empty

<a id="unreal.StaticMeshEditorSubsystem.set_lod_screen_sizes"></a>

#### set_lod_screen_sizes

```python
def set_lod_screen_sizes(static_mesh: StaticMesh,
                         screen_sizes: Array[float]) -> bool
```

x.set_lod_screen_sizes(static_mesh, screen_sizes) -> bool
Set LOD screen sizes.

Args:
    static_mesh (StaticMesh): Mesh to process.
    screen_sizes (Array[float]): Array of LOD screen sizes to set.

Returns:
    bool: A boolean indicating if setting the screen sizes was successful.

<a id="unreal.StaticMeshEditorSubsystem.set_lods"></a>

#### set_lods

```python
def set_lods(static_mesh: StaticMesh,
             reduction_options: StaticMeshReductionOptions) -> int
```

x.set_lods(static_mesh, reduction_options) -> int32
Same as SetLodsWithNotification but changes are applied.

Args:
    static_mesh (StaticMesh): 
    reduction_options (StaticMeshReductionOptions): 

Returns:
    int32:

<a id="unreal.StaticMeshEditorSubsystem.set_lod_reduction_settings"></a>

#### set_lod_reduction_settings

```python
def set_lod_reduction_settings(
        static_mesh: StaticMesh, lod_index: int,
        reduction_options: MeshReductionSettings) -> None
```

x.set_lod_reduction_settings(static_mesh, lod_index, reduction_options) -> None
Set the LOD reduction for the specified LOD index.

Args:
    static_mesh (StaticMesh): Mesh to process.
    lod_index (int32): The LOD we will apply the reduction settings.
    reduction_options (MeshReductionSettings): The reduction settings we want to apply to the LOD.

<a id="unreal.StaticMeshEditorSubsystem.set_lod_material_slot"></a>

#### set_lod_material_slot

```python
def set_lod_material_slot(static_mesh: StaticMesh, material_slot_index: int,
                          lod_index: int, section_index: int) -> None
```

x.set_lod_material_slot(static_mesh, material_slot_index, lod_index, section_index) -> None
Sets the material slot for a specific LOD.

Args:
    static_mesh (StaticMesh): Static mesh to Enables/disables shadow casting from.
    material_slot_index (int32): Index of the material slot to use.
    lod_index (int32): Index of the StaticMesh LOD.
    section_index (int32): Index of the StaticMesh Section.

<a id="unreal.StaticMeshEditorSubsystem.set_lod_group"></a>

#### set_lod_group

```python
def set_lod_group(static_mesh: StaticMesh,
                  lod_group: Name,
                  rebuild_immediately: bool = True) -> bool
```

x.set_lod_group(static_mesh, lod_group, rebuild_immediately=True) -> bool
Set the LODGroup for the specified static mesh

Args:
    static_mesh (StaticMesh): Mesh to process.
    lod_group (Name): Name of the LODGroup to apply
    rebuild_immediately (bool): If true, rebuild the static mesh immediately

Returns:
    bool: Success

<a id="unreal.StaticMeshEditorSubsystem.set_lod_from_static_mesh"></a>

#### set_lod_from_static_mesh

```python
def set_lod_from_static_mesh(destination_static_mesh: StaticMesh,
                             destination_lod_index: int,
                             source_static_mesh: StaticMesh,
                             source_lod_index: int,
                             reuse_existing_material_slots: bool) -> int
```

x.set_lod_from_static_mesh(destination_static_mesh, destination_lod_index, source_static_mesh, source_lod_index, reuse_existing_material_slots) -> int32
Adds or create a LOD at DestinationLodIndex using the geometry from SourceStaticMesh SourceLodIndex

Args:
    destination_static_mesh (StaticMesh): The static mesh to set the LOD in.
    destination_lod_index (int32): The index of the LOD to set.
    source_static_mesh (StaticMesh): The static mesh to get the LOD from.
    source_lod_index (int32): The index of the LOD to get.
    reuse_existing_material_slots (bool): If true, sections from SourceStaticMesh will be remapped to match the material slots of DestinationStaticMesh when they have the same material assigned. If false, all material slots of SourceStaticMesh will be appended in DestinationStaticMesh.

Returns:
    int32: The index of the LOD that was set. It can be different than DestinationLodIndex if it wasn't a valid index. A negative value indicates that the LOD was not set. See log for explanation.

<a id="unreal.StaticMeshEditorSubsystem.set_lod_build_settings"></a>

#### set_lod_build_settings

```python
def set_lod_build_settings(static_mesh: StaticMesh, lod_index: int,
                           build_options: MeshBuildSettings) -> None
```

x.set_lod_build_settings(static_mesh, lod_index, build_options) -> None
Set the LOD build options for the specified LOD index.

Args:
    static_mesh (StaticMesh): Mesh to process.
    lod_index (int32): The LOD we will apply the build settings.
    build_options (MeshBuildSettings): The build settings we want to apply to the LOD.

<a id="unreal.StaticMeshEditorSubsystem.set_generate_lightmap_uv"></a>

#### set_generate_lightmap_uv

```python
def set_generate_lightmap_uv(static_mesh: StaticMesh,
                             generate_lightmap_u_vs: bool) -> bool
```

x.set_generate_lightmap_uv(static_mesh, generate_lightmap_u_vs) -> bool
Set Generate Lightmap UVs for StaticMesh

Args:
    static_mesh (StaticMesh): 
    generate_lightmap_u_vs (bool): 

Returns:
    bool:

<a id="unreal.StaticMeshEditorSubsystem.set_convex_decomposition_collisions_with_notification"></a>

#### set_convex_decomposition_collisions_with_notification

```python
def set_convex_decomposition_collisions_with_notification(
        static_mesh: StaticMesh, hull_count: int, max_hull_verts: int,
        hull_precision: int, apply_changes: bool) -> bool
```

x.set_convex_decomposition_collisions_with_notification(static_mesh, hull_count, max_hull_verts, hull_precision, apply_changes) -> bool
Add a convex collision to a static mesh.
Any existing collisions will be removed from the static mesh.
This method replicates what is done when invoking menu entry "Collision > Auto Convex Collision" in the Mesh Editor.

Args:
    static_mesh (StaticMesh): Static mesh to add convex collision on.
    hull_count (int32): Maximum number of convex pieces that will be created. Must be positive.
    max_hull_verts (int32): Maximum number of vertices allowed for any generated convex hull.
    hull_precision (int32): Number of voxels to use when generating collision. Must be positive.
    apply_changes (bool): Indicates if changes must be apply or not.

Returns:
    bool: A boolean indicating if the addition was successful or not.

<a id="unreal.StaticMeshEditorSubsystem.set_convex_decomposition_collisions"></a>

#### set_convex_decomposition_collisions

```python
def set_convex_decomposition_collisions(static_mesh: StaticMesh,
                                        hull_count: int, max_hull_verts: int,
                                        hull_precision: int) -> bool
```

x.set_convex_decomposition_collisions(static_mesh, hull_count, max_hull_verts, hull_precision) -> bool
Same as SetConvexDecompositionCollisionsWithNotification but changes are automatically applied.

Args:
    static_mesh (StaticMesh): 
    hull_count (int32): 
    max_hull_verts (int32): 
    hull_precision (int32): 

Returns:
    bool:

<a id="unreal.StaticMeshEditorSubsystem.set_allow_cpu_access"></a>

#### set_allow_cpu_access

```python
def set_allow_cpu_access(static_mesh: StaticMesh,
                         allow_cpu_access: bool) -> None
```

x.set_allow_cpu_access(static_mesh, allow_cpu_access) -> None
Sets StaticMeshFlag bAllowCPUAccess

Args:
    static_mesh (StaticMesh): 
    allow_cpu_access (bool):

<a id="unreal.StaticMeshEditorSubsystem.replace_mesh_components_meshes_on_actors"></a>

#### replace_mesh_components_meshes_on_actors

```python
def replace_mesh_components_meshes_on_actors(actors: Array[Actor],
                                             mesh_to_be_replaced: StaticMesh,
                                             new_mesh: StaticMesh) -> None
```

x.replace_mesh_components_meshes_on_actors(actors, mesh_to_be_replaced, new_mesh) -> None
Find the references of the mesh MeshToBeReplaced on all the MeshComponents of all the Actors provided and replace it by NewMesh.

Args:
    actors (Array[Actor]): List of Actors to search from.
    mesh_to_be_replaced (StaticMesh): Mesh we want to replace.
    new_mesh (StaticMesh): Mesh to replace MeshToBeReplaced by.

<a id="unreal.StaticMeshEditorSubsystem.replace_mesh_components_meshes"></a>

#### replace_mesh_components_meshes

```python
def replace_mesh_components_meshes(mesh_components: Array[StaticMeshComponent],
                                   mesh_to_be_replaced: StaticMesh,
                                   new_mesh: StaticMesh) -> None
```

x.replace_mesh_components_meshes(mesh_components, mesh_to_be_replaced, new_mesh) -> None
Find the references of the mesh MeshToBeReplaced on all the MeshComponents provided and replace it by NewMesh.
The editor should not be in play in editor mode.

Args:
    mesh_components (Array[StaticMeshComponent]): List of MeshComponent to search from.
    mesh_to_be_replaced (StaticMesh): Mesh we want to replace.
    new_mesh (StaticMesh): Mesh to replace MeshToBeReplaced by.

<a id="unreal.StaticMeshEditorSubsystem.replace_mesh_components_materials_on_actors"></a>

#### replace_mesh_components_materials_on_actors

```python
def replace_mesh_components_materials_on_actors(
        actors: Array[Actor], material_to_be_replaced: MaterialInterface,
        new_material: MaterialInterface) -> None
```

x.replace_mesh_components_materials_on_actors(actors, material_to_be_replaced, new_material) -> None
Find the references of the material MaterialToReplaced on all the MeshComponents of all the Actors provided and replace it by NewMaterial.

Args:
    actors (Array[Actor]): List of Actors to search from.
    material_to_be_replaced (MaterialInterface): Material we want to replace.
    new_material (MaterialInterface): Material to replace MaterialToBeReplaced by.

<a id="unreal.StaticMeshEditorSubsystem.replace_mesh_components_materials"></a>

#### replace_mesh_components_materials

```python
def replace_mesh_components_materials(
        mesh_components: Array[MeshComponent],
        material_to_be_replaced: MaterialInterface,
        new_material: MaterialInterface) -> None
```

x.replace_mesh_components_materials(mesh_components, material_to_be_replaced, new_material) -> None
Find the references of the material MaterialToReplaced on all the MeshComponents provided and replace it by NewMaterial.

Args:
    mesh_components (Array[MeshComponent]): List of MeshComponent to search from.
    material_to_be_replaced (MaterialInterface): Material we want to replace.
    new_material (MaterialInterface): Material to replace MaterialToBeReplaced by.

<a id="unreal.StaticMeshEditorSubsystem.remove_uv_channel"></a>

#### remove_uv_channel

```python
def remove_uv_channel(static_mesh: StaticMesh, lod_index: int,
                      uv_channel_index: int) -> bool
```

x.remove_uv_channel(static_mesh, lod_index, uv_channel_index) -> bool
Removes the UV channel at the specified channel index on the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh on which to remove the UV channel.
    lod_index (int32): Index of the StaticMesh LOD.
    uv_channel_index (int32): Index where to remove the UV channel.

Returns:
    bool: true if the UV channel was removed.

<a id="unreal.StaticMeshEditorSubsystem.remove_lods"></a>

#### remove_lods

```python
def remove_lods(static_mesh: StaticMesh) -> bool
```

x.remove_lods(static_mesh) -> bool
Remove LODs on a static mesh except LOD 0.

Args:
    static_mesh (StaticMesh): Mesh to remove LOD from.

Returns:
    bool: A boolean indicating if the removal was successful, true, or not.

<a id="unreal.StaticMeshEditorSubsystem.remove_collisions_with_notification"></a>

#### remove_collisions_with_notification

```python
def remove_collisions_with_notification(static_mesh: StaticMesh,
                                        apply_changes: bool) -> bool
```

x.remove_collisions_with_notification(static_mesh, apply_changes) -> bool
Remove collisions from a static mesh.
This method replicates what is done when invoking menu entries "Collision > Remove Collision" in the Mesh Editor.

Args:
    static_mesh (StaticMesh): Static mesh to remove collisions from.
    apply_changes (bool): Indicates if changes must be apply or not.

Returns:
    bool: A boolean indicating if the removal was successful or not.

<a id="unreal.StaticMeshEditorSubsystem.remove_collisions"></a>

#### remove_collisions

```python
def remove_collisions(static_mesh: StaticMesh) -> bool
```

x.remove_collisions(static_mesh) -> bool
Same as RemoveCollisionsWithNotification but changes are applied.

Args:
    static_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.StaticMeshEditorSubsystem.reimport_all_custom_lo_ds"></a>

#### reimport_all_custom_lo_ds

```python
def reimport_all_custom_lo_ds(static_mesh: StaticMesh) -> bool
```

x.reimport_all_custom_lo_ds(static_mesh) -> bool
Re-import all the custom LODs present in the specified static mesh.

Args:
    static_mesh (StaticMesh): 

Returns:
    bool: true if re-import all LODs works, false otherwise see log for explanation.

<a id="unreal.StaticMeshEditorSubsystem.merge_static_mesh_actors"></a>

#### merge_static_mesh_actors

```python
def merge_static_mesh_actors(
        actors_to_merge: Array[StaticMeshActor],
        merge_options: MergeStaticMeshActorsOptions
) -> Optional[StaticMeshActor]
```

x.merge_static_mesh_actors(actors_to_merge, merge_options) -> StaticMeshActor or None
Merge the meshes into a unique mesh with the provided StaticMeshActors. There are multiple options on how to merge the meshes and their materials.
The ActorsToMerge need to be in the same Level.
This may have a high impact on performance depending of the MeshMergingSettings options.

Args:
    actors_to_merge (Array[StaticMeshActor]): List of Actors to merge.
    merge_options (MergeStaticMeshActorsOptions): Options on how to merge the actors.

Returns:
    StaticMeshActor or None: if the operation is successful.

    out_merged_actor (StaticMeshActor): The new created actor, if requested.

<a id="unreal.StaticMeshEditorSubsystem.join_static_mesh_actors"></a>

#### join_static_mesh_actors

```python
def join_static_mesh_actors(
        actors_to_join: Array[StaticMeshActor],
        join_options: JoinStaticMeshActorsOptions) -> Actor
```

x.join_static_mesh_actors(actors_to_join, join_options) -> Actor
Create a new Actor in the level that contains a duplicate of all the Actors Static Meshes Component.
The ActorsToJoin need to be in the same Level.
This will have a low impact on performance but may help the edition by grouping the meshes under a single Actor.

Args:
    actors_to_join (Array[StaticMeshActor]): List of Actors to join.
    join_options (JoinStaticMeshActorsOptions): Options on how to join the actors.

Returns:
    Actor: The new created actor.

<a id="unreal.StaticMeshEditorSubsystem.is_section_collision_enabled"></a>

#### is_section_collision_enabled

```python
def is_section_collision_enabled(static_mesh: StaticMesh, lod_index: int,
                                 section_index: int) -> bool
```

x.is_section_collision_enabled(static_mesh, lod_index, section_index) -> bool
Checks if a specific LOD mesh section has collision.

Args:
    static_mesh (StaticMesh): Static mesh to remove collisions from.
    lod_index (int32): Index of the StaticMesh LOD.
    section_index (int32): Index of the StaticMesh Section.

Returns:
    bool: True if the collision is enabled for the specified LOD of the StaticMesh section.

<a id="unreal.StaticMeshEditorSubsystem.insert_uv_channel"></a>

#### insert_uv_channel

```python
def insert_uv_channel(static_mesh: StaticMesh, lod_index: int,
                      uv_channel_index: int) -> bool
```

x.insert_uv_channel(static_mesh, lod_index, uv_channel_index) -> bool
Inserts an empty UV channel at the specified channel index on the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh on which to insert a UV channel.
    lod_index (int32): Index of the StaticMesh LOD.
    uv_channel_index (int32): Index where to insert the UV channel.

Returns:
    bool: true if a UV channel was added.

<a id="unreal.StaticMeshEditorSubsystem.import_lod"></a>

#### import_lod

```python
def import_lod(base_static_mesh: StaticMesh, lod_index: int,
               source_filename: str) -> int
```

x.import_lod(base_static_mesh, lod_index, source_filename) -> int32
Import or re-import a LOD into the specified base mesh. If the LOD do not exist it will import it and add it to the base static mesh. If the LOD already exist it will re-import the specified LOD.

Args:
    base_static_mesh (StaticMesh): 
    lod_index (int32): 
    source_filename (str): 

Returns:
    int32: the index of the LOD that was imported or re-imported. Will return INDEX_NONE if anything goes bad.

<a id="unreal.StaticMeshEditorSubsystem.has_vertex_colors"></a>

#### has_vertex_colors

```python
def has_vertex_colors(static_mesh: StaticMesh) -> bool
```

x.has_vertex_colors(static_mesh) -> bool
Check whether a static mesh has vertex colors

Args:
    static_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.StaticMeshEditorSubsystem.has_instance_vertex_colors"></a>

#### has_instance_vertex_colors

```python
def has_instance_vertex_colors(
        static_mesh_component: StaticMeshComponent) -> bool
```

x.has_instance_vertex_colors(static_mesh_component) -> bool
Check whether a static mesh component has vertex colors

Args:
    static_mesh_component (StaticMeshComponent): 

Returns:
    bool:

<a id="unreal.StaticMeshEditorSubsystem.get_simple_collision_count"></a>

#### get_simple_collision_count

```python
def get_simple_collision_count(static_mesh: StaticMesh) -> int
```

x.get_simple_collision_count(static_mesh) -> int32
Get number of simple collisions present on a static mesh.

Args:
    static_mesh (StaticMesh): Mesh to query on.

Returns:
    int32: An integer representing the number of simple collisions on the input static mesh. An negative value indicates that the command could not be executed. See log for explanation.

<a id="unreal.StaticMeshEditorSubsystem.get_num_uv_channels"></a>

#### get_num_uv_channels

```python
def get_num_uv_channels(static_mesh: StaticMesh, lod_index: int) -> int
```

x.get_num_uv_channels(static_mesh, lod_index) -> int32
Returns the number of UV channels for the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh to query.
    lod_index (int32): Index of the StaticMesh LOD.

Returns:
    int32: the number of UV channels.

<a id="unreal.StaticMeshEditorSubsystem.get_number_verts"></a>

#### get_number_verts

```python
def get_number_verts(static_mesh: StaticMesh, lod_index: int) -> int
```

x.get_number_verts(static_mesh, lod_index) -> int32
Get number of StaticMesh verts for an LOD

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 

Returns:
    int32:

<a id="unreal.StaticMeshEditorSubsystem.get_number_materials"></a>

#### get_number_materials

```python
def get_number_materials(static_mesh: StaticMesh) -> int
```

x.get_number_materials(static_mesh) -> int32
Get number of Materials for a StaticMesh

Args:
    static_mesh (StaticMesh): 

Returns:
    int32:

<a id="unreal.StaticMeshEditorSubsystem.get_nanite_settings"></a>

#### get_nanite_settings

```python
def get_nanite_settings(static_mesh: StaticMesh) -> MeshNaniteSettings
```

x.get_nanite_settings(static_mesh) -> MeshNaniteSettings
Get the Nanite Settings for the mesh

Args:
    static_mesh (StaticMesh): Mesh to access

Returns:
    MeshNaniteSettings: FMeshNaniteSettings struct for the given static mesh

<a id="unreal.StaticMeshEditorSubsystem.get_lod_screen_sizes"></a>

#### get_lod_screen_sizes

```python
def get_lod_screen_sizes(static_mesh: StaticMesh) -> Array[float]
```

x.get_lod_screen_sizes(static_mesh) -> Array[float]
Get an array of LOD screen sizes for evaluation.

Args:
    static_mesh (StaticMesh): Mesh to process.

Returns:
    Array[float]: array of LOD screen sizes.

<a id="unreal.StaticMeshEditorSubsystem.get_lod_reduction_settings"></a>

#### get_lod_reduction_settings

```python
def get_lod_reduction_settings(static_mesh: StaticMesh,
                               lod_index: int) -> MeshReductionSettings
```

x.get_lod_reduction_settings(static_mesh, lod_index) -> MeshReductionSettings
Copy the reduction options with the specified LOD reduction settings.

Args:
    static_mesh (StaticMesh): Mesh to process.
    lod_index (int32): The LOD we get the reduction settings.

Returns:
    MeshReductionSettings: 

    out_reduction_options (MeshReductionSettings): The reduction settings where we copy the reduction options.

<a id="unreal.StaticMeshEditorSubsystem.get_lod_material_slot"></a>

#### get_lod_material_slot

```python
def get_lod_material_slot(static_mesh: StaticMesh, lod_index: int,
                          section_index: int) -> int
```

x.get_lod_material_slot(static_mesh, lod_index, section_index) -> int32
Gets the material slot used for a specific LOD section.

Args:
    static_mesh (StaticMesh): Static mesh to get the material index from.
    lod_index (int32): Index of the StaticMesh LOD.
    section_index (int32): Index of the StaticMesh Section.

Returns:
    int32: MaterialSlotIndex   Index of the material slot used by the section or INDEX_NONE in case of error.

<a id="unreal.StaticMeshEditorSubsystem.get_lod_group"></a>

#### get_lod_group

```python
def get_lod_group(static_mesh: StaticMesh) -> Name
```

x.get_lod_group(static_mesh) -> Name
Get the LODGroup for the specified static mesh

Args:
    static_mesh (StaticMesh): 

Returns:
    Name: LODGroup

<a id="unreal.StaticMeshEditorSubsystem.get_lod_count"></a>

#### get_lod_count

```python
def get_lod_count(static_mesh: StaticMesh) -> int
```

x.get_lod_count(static_mesh) -> int32
Get number of LODs present on a static mesh.

Args:
    static_mesh (StaticMesh): Mesh to process.

Returns:
    int32: the number of LODs present on the input mesh. An negative value indicates that the command could not be executed. See log for explanation.

<a id="unreal.StaticMeshEditorSubsystem.get_lod_build_settings"></a>

#### get_lod_build_settings

```python
def get_lod_build_settings(static_mesh: StaticMesh,
                           lod_index: int) -> MeshBuildSettings
```

x.get_lod_build_settings(static_mesh, lod_index) -> MeshBuildSettings
Copy the build options with the specified LOD build settings.

Args:
    static_mesh (StaticMesh): Mesh to process.
    lod_index (int32): The LOD we get the reduction settings.

Returns:
    MeshBuildSettings: 

    out_build_options (MeshBuildSettings): The build settings where we copy the build options.

<a id="unreal.StaticMeshEditorSubsystem.get_convex_collision_count"></a>

#### get_convex_collision_count

```python
def get_convex_collision_count(static_mesh: StaticMesh) -> int
```

x.get_convex_collision_count(static_mesh) -> int32
Get number of convex collisions present on a static mesh.

Args:
    static_mesh (StaticMesh): Mesh to query on.

Returns:
    int32: An integer representing the number of convex collisions on the input static mesh. An negative value indicates that the command could not be executed. See log for explanation.

<a id="unreal.StaticMeshEditorSubsystem.get_collision_complexity"></a>

#### get_collision_complexity

```python
def get_collision_complexity(static_mesh: StaticMesh) -> CollisionTraceFlag
```

x.get_collision_complexity(static_mesh) -> CollisionTraceFlag
Get the Collision Trace behavior of a static mesh

Args:
    static_mesh (StaticMesh): Mesh to query on.

Returns:
    CollisionTraceFlag: the Collision Trace behavior.

<a id="unreal.StaticMeshEditorSubsystem.generate_planar_uv_channel"></a>

#### generate_planar_uv_channel

```python
def generate_planar_uv_channel(static_mesh: StaticMesh, lod_index: int,
                               uv_channel_index: int, position: Vector,
                               orientation: Rotator, tiling: Vector2D) -> bool
```

x.generate_planar_uv_channel(static_mesh, lod_index, uv_channel_index, position, orientation, tiling) -> bool
Generates planar UV mapping in the specified UV channel on the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh on which to generate the UV mapping.
    lod_index (int32): Index of the StaticMesh LOD.
    uv_channel_index (int32): Channel where to save the UV mapping.
    position (Vector): Position of the center of the projection gizmo.
    orientation (Rotator): Rotation to apply to the projection gizmo.
    tiling (Vector2D): The UV tiling to use to generate the UV mapping.

Returns:
    bool: true if the UV mapping was generated.

<a id="unreal.StaticMeshEditorSubsystem.generate_cylindrical_uv_channel"></a>

#### generate_cylindrical_uv_channel

```python
def generate_cylindrical_uv_channel(static_mesh: StaticMesh, lod_index: int,
                                    uv_channel_index: int, position: Vector,
                                    orientation: Rotator,
                                    tiling: Vector2D) -> bool
```

x.generate_cylindrical_uv_channel(static_mesh, lod_index, uv_channel_index, position, orientation, tiling) -> bool
Generates cylindrical UV mapping in the specified UV channel on the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh on which to generate the UV mapping.
    lod_index (int32): Index of the StaticMesh LOD.
    uv_channel_index (int32): Channel where to save the UV mapping.
    position (Vector): Position of the center of the projection gizmo.
    orientation (Rotator): Rotation to apply to the projection gizmo.
    tiling (Vector2D): The UV tiling to use to generate the UV mapping.

Returns:
    bool: true if the UV mapping was generated.

<a id="unreal.StaticMeshEditorSubsystem.generate_box_uv_channel"></a>

#### generate_box_uv_channel

```python
def generate_box_uv_channel(static_mesh: StaticMesh, lod_index: int,
                            uv_channel_index: int, position: Vector,
                            orientation: Rotator, size: Vector) -> bool
```

x.generate_box_uv_channel(static_mesh, lod_index, uv_channel_index, position, orientation, size) -> bool
Generates box UV mapping in the specified UV channel on the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh on which to generate the UV mapping.
    lod_index (int32): Index of the StaticMesh LOD.
    uv_channel_index (int32): Channel where to save the UV mapping.
    position (Vector): Position of the center of the projection gizmo.
    orientation (Rotator): Rotation to apply to the projection gizmo.
    size (Vector): The size of the box projection gizmo.

Returns:
    bool: true if the UV mapping was generated.

<a id="unreal.StaticMeshEditorSubsystem.enable_section_collision"></a>

#### enable_section_collision

```python
def enable_section_collision(static_mesh: StaticMesh, collision_enabled: bool,
                             lod_index: int, section_index: int) -> None
```

x.enable_section_collision(static_mesh, collision_enabled, lod_index, section_index) -> None
Enables/disables mesh section collision for a specific LOD.

Args:
    static_mesh (StaticMesh): Static mesh to Enables/disables collisions from.
    collision_enabled (bool): If the collision is enabled or not.
    lod_index (int32): Index of the StaticMesh LOD.
    section_index (int32): Index of the StaticMesh Section.

<a id="unreal.StaticMeshEditorSubsystem.enable_section_cast_shadow"></a>

#### enable_section_cast_shadow

```python
def enable_section_cast_shadow(static_mesh: StaticMesh, cast_shadow: bool,
                               lod_index: int, section_index: int) -> None
```

x.enable_section_cast_shadow(static_mesh, cast_shadow, lod_index, section_index) -> None
Enables/disables mesh section shadow casting for a specific LOD.

Args:
    static_mesh (StaticMesh): Static mesh to Enables/disables shadow casting from.
    cast_shadow (bool): If the section should cast shadow.
    lod_index (int32): Index of the StaticMesh LOD.
    section_index (int32): Index of the StaticMesh Section.

<a id="unreal.StaticMeshEditorSubsystem.create_proxy_mesh_actor"></a>

#### create_proxy_mesh_actor

```python
def create_proxy_mesh_actor(
        actors_to_merge: Array[StaticMeshActor],
        merge_options: CreateProxyMeshActorOptions
) -> Optional[StaticMeshActor]
```

x.create_proxy_mesh_actor(actors_to_merge, merge_options) -> StaticMeshActor or None
Build a proxy mesh actor that can replace a set of mesh actors.

Args:
    actors_to_merge (Array[StaticMeshActor]): List of actors to build a proxy for.
    merge_options (CreateProxyMeshActorOptions): 

Returns:
    StaticMeshActor or None: Success of the proxy creation

    out_merged_actor (StaticMeshActor): generated actor if requested

<a id="unreal.StaticMeshEditorSubsystem.bulk_set_convex_decomposition_collisions_with_notification"></a>

#### bulk_set_convex_decomposition_collisions_with_notification

```python
def bulk_set_convex_decomposition_collisions_with_notification(
        static_meshes: Array[StaticMesh], hull_count: int, max_hull_verts: int,
        hull_precision: int, apply_changes: bool) -> bool
```

x.bulk_set_convex_decomposition_collisions_with_notification(static_meshes, hull_count, max_hull_verts, hull_precision, apply_changes) -> bool
Compute convex collisions for a set of static meshes.
Any existing collisions will be removed from the static meshes.
This method replicates what is done when invoking menu entry "Collision > Auto Convex Collision" in the Mesh Editor.

Args:
    static_meshes (Array[StaticMesh]): Set of Static mesh to add convex collision on.
    hull_count (int32): Maximum number of convex pieces that will be created. Must be positive.
    max_hull_verts (int32): Maximum number of vertices allowed for any generated convex hull.
    hull_precision (int32): Number of voxels to use when generating collision. Must be positive.
    apply_changes (bool): Indicates if changes must be apply or not.

Returns:
    bool: A boolean indicating if the addition was successful or not.

<a id="unreal.StaticMeshEditorSubsystem.bulk_set_convex_decomposition_collisions"></a>

#### bulk_set_convex_decomposition_collisions

```python
def bulk_set_convex_decomposition_collisions(static_meshes: Array[StaticMesh],
                                             hull_count: int,
                                             max_hull_verts: int,
                                             hull_precision: int) -> bool
```

x.bulk_set_convex_decomposition_collisions(static_meshes, hull_count, max_hull_verts, hull_precision) -> bool
Same as SetConvexDecompositionCollisionsWithNotification but changes are automatically applied.

Args:
    static_meshes (Array[StaticMesh]): 
    hull_count (int32): 
    max_hull_verts (int32): 
    hull_precision (int32): 

Returns:
    bool:

<a id="unreal.StaticMeshEditorSubsystem.add_uv_channel"></a>

#### add_uv_channel

```python
def add_uv_channel(static_mesh: StaticMesh, lod_index: int) -> bool
```

x.add_uv_channel(static_mesh, lod_index) -> bool
Adds an empty UV channel at the end of the existing channels on the given LOD of a StaticMesh.

Args:
    static_mesh (StaticMesh): Static mesh on which to add a UV channel.
    lod_index (int32): Index of the StaticMesh LOD.

Returns:
    bool: true if a UV channel was added.

<a id="unreal.StaticMeshEditorSubsystem.add_simple_collisions_with_notification"></a>

#### add_simple_collisions_with_notification

```python
def add_simple_collisions_with_notification(
        static_mesh: StaticMesh, shape_type: ScriptCollisionShapeType,
        apply_changes: bool) -> int
```

x.add_simple_collisions_with_notification(static_mesh, shape_type, apply_changes) -> int32
Add simple collisions to a static mesh.
This method replicates what is done when invoking menu entries "Collision > Add [...] Simplified Collision" in the Mesh Editor.

Args:
    static_mesh (StaticMesh): Mesh to generate simple collision for.
    shape_type (ScriptCollisionShapeType): Options on which simple collision to add to the mesh.
    apply_changes (bool): Indicates if changes must be apply or not.

Returns:
    int32: An integer indicating the index of the collision newly created. A negative value indicates the addition failed.

<a id="unreal.StaticMeshEditorSubsystem.add_simple_collisions"></a>

#### add_simple_collisions

```python
def add_simple_collisions(static_mesh: StaticMesh,
                          shape_type: ScriptCollisionShapeType) -> int
```

x.add_simple_collisions(static_mesh, shape_type) -> int32
Same as AddSimpleCollisionsWithNotification but changes are automatically applied.

Args:
    static_mesh (StaticMesh): 
    shape_type (ScriptCollisionShapeType): 

Returns:
    int32:

<a id="unreal.EditorAssetLibrary"></a>