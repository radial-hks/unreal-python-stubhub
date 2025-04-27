## EditorStaticMeshLibrary Objects

```python
class EditorStaticMeshLibrary(BlueprintFunctionLibrary)
```

Utility class to altering and analyzing a StaticMesh and use the common functionalities of the Mesh Editor.
The editor should not be in play in editor mode.

**C++ Source:**

- **Plugin**: EditorScriptingUtilities
- **Module**: EditorScriptingUtilities
- **File**: EditorStaticMeshLibrary.h

<a id="unreal.EditorStaticMeshLibrary.set_lods_with_notification"></a>

#### set_lods_with_notification

```python
@classmethod
def set_lods_with_notification(cls, static_mesh: StaticMesh,
                               reduction_options: StaticMeshReductionOptions,
                               apply_changes: bool) -> int
```

X.set_lods_with_notification(static_mesh, reduction_options, apply_changes) -> int32
Set Lods with Notification
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    reduction_options (StaticMeshReductionOptions): 
    apply_changes (bool): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.set_lods"></a>

#### set_lods

```python
@classmethod
def set_lods(cls, static_mesh: StaticMesh,
             reduction_options: StaticMeshReductionOptions) -> int
```

X.set_lods(static_mesh, reduction_options) -> int32
Set Lods
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    reduction_options (StaticMeshReductionOptions): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.set_lod_reduction_settings"></a>

#### set_lod_reduction_settings

```python
@classmethod
def set_lod_reduction_settings(
        cls, static_mesh: StaticMesh, lod_index: int,
        reduction_options: MeshReductionSettings) -> None
```

X.set_lod_reduction_settings(static_mesh, lod_index, reduction_options) -> None
Set Lod Reduction Settings
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    reduction_options (MeshReductionSettings):

<a id="unreal.EditorStaticMeshLibrary.set_lod_from_static_mesh"></a>

#### set_lod_from_static_mesh

```python
@classmethod
def set_lod_from_static_mesh(cls, destination_static_mesh: StaticMesh,
                             destination_lod_index: int,
                             source_static_mesh: StaticMesh,
                             source_lod_index: int,
                             reuse_existing_material_slots: bool) -> int
```

X.set_lod_from_static_mesh(destination_static_mesh, destination_lod_index, source_static_mesh, source_lod_index, reuse_existing_material_slots) -> int32
Set Lod from Static Mesh
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    destination_static_mesh (StaticMesh): 
    destination_lod_index (int32): 
    source_static_mesh (StaticMesh): 
    source_lod_index (int32): 
    reuse_existing_material_slots (bool): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.set_lod_build_settings"></a>

#### set_lod_build_settings

```python
@classmethod
def set_lod_build_settings(cls, static_mesh: StaticMesh, lod_index: int,
                           build_options: MeshBuildSettings) -> None
```

X.set_lod_build_settings(static_mesh, lod_index, build_options) -> None
Set Lod Build Settings
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    build_options (MeshBuildSettings):

<a id="unreal.EditorStaticMeshLibrary.set_generate_lightmap_uv"></a>

#### set_generate_lightmap_uv

```python
@classmethod
def set_generate_lightmap_uv(cls, static_mesh: StaticMesh,
                             generate_lightmap_u_vs: bool) -> bool
```

X.set_generate_lightmap_uv(static_mesh, generate_lightmap_u_vs) -> bool
Set Generate Lightmap UVs
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    generate_lightmap_u_vs (bool): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.set_convex_decomposition_collisions_with_notification"></a>

#### set_convex_decomposition_collisions_with_notification

```python
@classmethod
def set_convex_decomposition_collisions_with_notification(
        cls, static_mesh: StaticMesh, hull_count: int, max_hull_verts: int,
        hull_precision: int, apply_changes: bool) -> bool
```

X.set_convex_decomposition_collisions_with_notification(static_mesh, hull_count, max_hull_verts, hull_precision, apply_changes) -> bool
Set Convex Decomposition Collisions with Notification
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    hull_count (int32): 
    max_hull_verts (int32): 
    hull_precision (int32): 
    apply_changes (bool): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.set_convex_decomposition_collisions"></a>

#### set_convex_decomposition_collisions

```python
@classmethod
def set_convex_decomposition_collisions(cls, static_mesh: StaticMesh,
                                        hull_count: int, max_hull_verts: int,
                                        hull_precision: int) -> bool
```

X.set_convex_decomposition_collisions(static_mesh, hull_count, max_hull_verts, hull_precision) -> bool
Set Convex Decomposition Collisions
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    hull_count (int32): 
    max_hull_verts (int32): 
    hull_precision (int32): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.set_allow_cpu_access"></a>

#### set_allow_cpu_access

```python
@classmethod
def set_allow_cpu_access(cls, static_mesh: StaticMesh,
                         allow_cpu_access: bool) -> None
```

X.set_allow_cpu_access(static_mesh, allow_cpu_access) -> None
Set Allow CPUAccess
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    allow_cpu_access (bool):

<a id="unreal.EditorStaticMeshLibrary.remove_uv_channel"></a>

#### remove_uv_channel

```python
@classmethod
def remove_uv_channel(cls, static_mesh: StaticMesh, lod_index: int,
                      uv_channel_index: int) -> bool
```

X.remove_uv_channel(static_mesh, lod_index, uv_channel_index) -> bool
Remove UVChannel
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    uv_channel_index (int32): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.remove_lods"></a>

#### remove_lods

```python
@classmethod
def remove_lods(cls, static_mesh: StaticMesh) -> bool
```

X.remove_lods(static_mesh) -> bool
Remove Lods
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.remove_collisions_with_notification"></a>

#### remove_collisions_with_notification

```python
@classmethod
def remove_collisions_with_notification(cls, static_mesh: StaticMesh,
                                        apply_changes: bool) -> bool
```

X.remove_collisions_with_notification(static_mesh, apply_changes) -> bool
Remove Collisions with Notification
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    apply_changes (bool): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.remove_collisions"></a>

#### remove_collisions

```python
@classmethod
def remove_collisions(cls, static_mesh: StaticMesh) -> bool
```

X.remove_collisions(static_mesh) -> bool
Remove Collisions
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.reimport_all_custom_lo_ds"></a>

#### reimport_all_custom_lo_ds

```python
@classmethod
def reimport_all_custom_lo_ds(cls, static_mesh: StaticMesh) -> bool
```

X.reimport_all_custom_lo_ds(static_mesh) -> bool
Reimport All Custom LODs
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.is_section_collision_enabled"></a>

#### is_section_collision_enabled

```python
@classmethod
def is_section_collision_enabled(cls, static_mesh: StaticMesh, lod_index: int,
                                 section_index: int) -> bool
```

X.is_section_collision_enabled(static_mesh, lod_index, section_index) -> bool
Is Section Collision Enabled
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    section_index (int32): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.insert_uv_channel"></a>

#### insert_uv_channel

```python
@classmethod
def insert_uv_channel(cls, static_mesh: StaticMesh, lod_index: int,
                      uv_channel_index: int) -> bool
```

X.insert_uv_channel(static_mesh, lod_index, uv_channel_index) -> bool
Insert UVChannel
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    uv_channel_index (int32): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.import_lod"></a>

#### import_lod

```python
@classmethod
def import_lod(cls, base_static_mesh: StaticMesh, lod_index: int,
               source_filename: str) -> int
```

X.import_lod(base_static_mesh, lod_index, source_filename) -> int32
Import LOD
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    base_static_mesh (StaticMesh): 
    lod_index (int32): 
    source_filename (str): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.has_vertex_colors"></a>

#### has_vertex_colors

```python
@classmethod
def has_vertex_colors(cls, static_mesh: StaticMesh) -> bool
```

X.has_vertex_colors(static_mesh) -> bool
Has Vertex Colors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.has_instance_vertex_colors"></a>

#### has_instance_vertex_colors

```python
@classmethod
def has_instance_vertex_colors(
        cls, static_mesh_component: StaticMeshComponent) -> bool
```

X.has_instance_vertex_colors(static_mesh_component) -> bool
Has Instance Vertex Colors
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh_component (StaticMeshComponent): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.get_simple_collision_count"></a>

#### get_simple_collision_count

```python
@classmethod
def get_simple_collision_count(cls, static_mesh: StaticMesh) -> int
```

X.get_simple_collision_count(static_mesh) -> int32
Get Simple Collision Count
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.get_num_uv_channels"></a>

#### get_num_uv_channels

```python
@classmethod
def get_num_uv_channels(cls, static_mesh: StaticMesh, lod_index: int) -> int
```

X.get_num_uv_channels(static_mesh, lod_index) -> int32
Get Num UVChannels
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.get_number_verts"></a>

#### get_number_verts

```python
@classmethod
def get_number_verts(cls, static_mesh: StaticMesh, lod_index: int) -> int
```

X.get_number_verts(static_mesh, lod_index) -> int32
Get Number Verts
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.get_number_materials"></a>

#### get_number_materials

```python
@classmethod
def get_number_materials(cls, static_mesh: StaticMesh) -> int
```

X.get_number_materials(static_mesh) -> int32
Get Number Materials
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.get_lod_screen_sizes"></a>

#### get_lod_screen_sizes

```python
@classmethod
def get_lod_screen_sizes(cls, static_mesh: StaticMesh) -> Array[float]
```

X.get_lod_screen_sizes(static_mesh) -> Array[float]
Get Lod Screen Sizes
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    Array[float]:

<a id="unreal.EditorStaticMeshLibrary.get_lod_reduction_settings"></a>

#### get_lod_reduction_settings

```python
@classmethod
def get_lod_reduction_settings(cls, static_mesh: StaticMesh,
                               lod_index: int) -> MeshReductionSettings
```

X.get_lod_reduction_settings(static_mesh, lod_index) -> MeshReductionSettings
Get Lod Reduction Settings
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 

Returns:
    MeshReductionSettings: 

    out_reduction_options (MeshReductionSettings):

<a id="unreal.EditorStaticMeshLibrary.get_lod_count"></a>

#### get_lod_count

```python
@classmethod
def get_lod_count(cls, static_mesh: StaticMesh) -> int
```

X.get_lod_count(static_mesh) -> int32
Get Lod Count
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.get_lod_build_settings"></a>

#### get_lod_build_settings

```python
@classmethod
def get_lod_build_settings(cls, static_mesh: StaticMesh,
                           lod_index: int) -> MeshBuildSettings
```

X.get_lod_build_settings(static_mesh, lod_index) -> MeshBuildSettings
Get Lod Build Settings
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 

Returns:
    MeshBuildSettings: 

    out_build_options (MeshBuildSettings):

<a id="unreal.EditorStaticMeshLibrary.get_convex_collision_count"></a>

#### get_convex_collision_count

```python
@classmethod
def get_convex_collision_count(cls, static_mesh: StaticMesh) -> int
```

X.get_convex_collision_count(static_mesh) -> int32
Get Convex Collision Count
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.get_collision_complexity"></a>

#### get_collision_complexity

```python
@classmethod
def get_collision_complexity(cls,
                             static_mesh: StaticMesh) -> CollisionTraceFlag
```

X.get_collision_complexity(static_mesh) -> CollisionTraceFlag
Get Collision Complexity
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 

Returns:
    CollisionTraceFlag:

<a id="unreal.EditorStaticMeshLibrary.generate_planar_uv_channel"></a>

#### generate_planar_uv_channel

```python
@classmethod
def generate_planar_uv_channel(cls, static_mesh: StaticMesh, lod_index: int,
                               uv_channel_index: int, position: Vector,
                               orientation: Rotator, tiling: Vector2D) -> bool
```

X.generate_planar_uv_channel(static_mesh, lod_index, uv_channel_index, position, orientation, tiling) -> bool
Generate Planar UVChannel
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    uv_channel_index (int32): 
    position (Vector): 
    orientation (Rotator): 
    tiling (Vector2D): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.generate_cylindrical_uv_channel"></a>

#### generate_cylindrical_uv_channel

```python
@classmethod
def generate_cylindrical_uv_channel(cls, static_mesh: StaticMesh,
                                    lod_index: int, uv_channel_index: int,
                                    position: Vector, orientation: Rotator,
                                    tiling: Vector2D) -> bool
```

X.generate_cylindrical_uv_channel(static_mesh, lod_index, uv_channel_index, position, orientation, tiling) -> bool
Generate Cylindrical UVChannel
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    uv_channel_index (int32): 
    position (Vector): 
    orientation (Rotator): 
    tiling (Vector2D): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.generate_box_uv_channel"></a>

#### generate_box_uv_channel

```python
@classmethod
def generate_box_uv_channel(cls, static_mesh: StaticMesh, lod_index: int,
                            uv_channel_index: int, position: Vector,
                            orientation: Rotator, size: Vector) -> bool
```

X.generate_box_uv_channel(static_mesh, lod_index, uv_channel_index, position, orientation, size) -> bool
Generate Box UVChannel
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    uv_channel_index (int32): 
    position (Vector): 
    orientation (Rotator): 
    size (Vector): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.enable_section_collision"></a>

#### enable_section_collision

```python
@classmethod
def enable_section_collision(cls, static_mesh: StaticMesh,
                             collision_enabled: bool, lod_index: int,
                             section_index: int) -> None
```

X.enable_section_collision(static_mesh, collision_enabled, lod_index, section_index) -> None
Enable Section Collision
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    collision_enabled (bool): 
    lod_index (int32): 
    section_index (int32):

<a id="unreal.EditorStaticMeshLibrary.enable_section_cast_shadow"></a>

#### enable_section_cast_shadow

```python
@classmethod
def enable_section_cast_shadow(cls, static_mesh: StaticMesh, cast_shadow: bool,
                               lod_index: int, section_index: int) -> None
```

X.enable_section_cast_shadow(static_mesh, cast_shadow, lod_index, section_index) -> None
Enable Section Cast Shadow
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    cast_shadow (bool): 
    lod_index (int32): 
    section_index (int32):

<a id="unreal.EditorStaticMeshLibrary.bulk_set_convex_decomposition_collisions_with_notification"></a>

#### bulk_set_convex_decomposition_collisions_with_notification

```python
@classmethod
def bulk_set_convex_decomposition_collisions_with_notification(
        cls, static_meshes: Array[StaticMesh], hull_count: int,
        max_hull_verts: int, hull_precision: int, apply_changes: bool) -> bool
```

X.bulk_set_convex_decomposition_collisions_with_notification(static_meshes, hull_count, max_hull_verts, hull_precision, apply_changes) -> bool
Bulk Set Convex Decomposition Collisions with Notification
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_meshes (Array[StaticMesh]): 
    hull_count (int32): 
    max_hull_verts (int32): 
    hull_precision (int32): 
    apply_changes (bool): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.bulk_set_convex_decomposition_collisions"></a>

#### bulk_set_convex_decomposition_collisions

```python
@classmethod
def bulk_set_convex_decomposition_collisions(cls,
                                             static_meshes: Array[StaticMesh],
                                             hull_count: int,
                                             max_hull_verts: int,
                                             hull_precision: int) -> bool
```

X.bulk_set_convex_decomposition_collisions(static_meshes, hull_count, max_hull_verts, hull_precision) -> bool
Bulk Set Convex Decomposition Collisions
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_meshes (Array[StaticMesh]): 
    hull_count (int32): 
    max_hull_verts (int32): 
    hull_precision (int32): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.add_uv_channel"></a>

#### add_uv_channel

```python
@classmethod
def add_uv_channel(cls, static_mesh: StaticMesh, lod_index: int) -> bool
```

X.add_uv_channel(static_mesh, lod_index) -> bool
Add UVChannel
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 

Returns:
    bool:

<a id="unreal.EditorStaticMeshLibrary.add_simple_collisions_with_notification"></a>

#### add_simple_collisions_with_notification

```python
@classmethod
def add_simple_collisions_with_notification(
        cls, static_mesh: StaticMesh, shape_type: ScriptCollisionShapeType,
        apply_changes: bool) -> int
```

X.add_simple_collisions_with_notification(static_mesh, shape_type, apply_changes) -> int32
Add Simple Collisions with Notification
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    shape_type (ScriptCollisionShapeType): 
    apply_changes (bool): 

Returns:
    int32:

<a id="unreal.EditorStaticMeshLibrary.add_simple_collisions"></a>

#### add_simple_collisions

```python
@classmethod
def add_simple_collisions(cls, static_mesh: StaticMesh,
                          shape_type: ScriptCollisionShapeType) -> int
```

X.add_simple_collisions(static_mesh, shape_type) -> int32
Add Simple Collisions
deprecated: The Editor Scripting Utilities Plugin is deprecated - Use the function in Static Mesh Editor Subsystem

Args:
    static_mesh (StaticMesh): 
    shape_type (ScriptCollisionShapeType): 

Returns:
    int32:

<a id="unreal.StaticMeshUtilitiesLibrary"></a>