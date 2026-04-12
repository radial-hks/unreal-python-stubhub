## PythonMeshLib Objects

```python
class PythonMeshLib(BlueprintFunctionLibrary)
```

class FSphere;  UE5.0 pr1

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonMeshLib.h

<a id="unreal.PythonMeshLib.trace_dynamic_mesh_triangles_visibility"></a>

#### trace\_dynamic\_mesh\_triangles\_visibility

```python
@classmethod
def trace_dynamic_mesh_triangles_visibility(
        cls, target_mesh_component: DynamicMeshComponent,
        triangle_ids: Array[int], view_info: MinimalViewInfo, debug_draw: bool,
        profile_name: Name) -> Optional[TAPythonPrimitiveHitResult]
```

X.trace_dynamic_mesh_triangles_visibility(target_mesh_component, triangle_ids, view_info, debug_draw, profile_name) -> TAPythonPrimitiveHitResult or None
Trace the visibility of DynamicMesh's triangles in current view.
note: added in v1.2.0
note: need UE5.2+

Args:
    target_mesh_component (DynamicMeshComponent): The target DynamicMeshComponent.
    triangle_ids (Array[int32]): The triangle ids of DynamicMesh.
    view_info (MinimalViewInfo): The current view info.
    debug_draw (bool): Debug draw or not.
    profile_name (Name): The trace profile name.

Returns:
    TAPythonPrimitiveHitResult or None: TAPythonPrimitiveHitResult or None:

    result (TAPythonPrimitiveHitResult):

<a id="unreal.PythonMeshLib.set_uvs_from_camera_projection"></a>

#### set\_uvs\_from\_camera\_projection

```python
@classmethod
def set_uvs_from_camera_projection(cls, target_mesh: DynamicMesh,
                                   uv_set_index: int,
                                   selection: GeometryScriptMeshSelection,
                                   m: Matrix,
                                   view_info: MinimalViewInfo) -> DynamicMesh
```

X.set_uvs_from_camera_projection(target_mesh, uv_set_index, selection, m, view_info) -> DynamicMesh
Project the DynamicMesh to specified UVSet in current view.
note: need UE 5.1+

Args:
    target_mesh (DynamicMesh): The target DynamicMesh.
    uv_set_index (int32): The UVSet index of mesh.
    selection (GeometryScriptMeshSelection): The selection of mesh.
    m (Matrix): The transform matrix of DynamicMesh.
    view_info (MinimalViewInfo): The current view info.

Returns:
    DynamicMesh: The projected DynamicMesh.

<a id="unreal.PythonMeshLib.set_static_mesh_sockets"></a>

#### set\_static\_mesh\_sockets

```python
@classmethod
def set_static_mesh_sockets(cls, obj: Object,
                            sockets: Array[StaticMeshSocket]) -> bool
```

X.set_static_mesh_sockets(obj, sockets) -> bool
Set the static mesh sockets of the mesh object
result: Succeed or not.

Args:
    obj (Object): The target mesh.
    sockets (Array[StaticMeshSocket]): The sockets for mesh.

Returns:
    bool:

<a id="unreal.PythonMeshLib.set_static_mesh_socket_name"></a>

#### set\_static\_mesh\_socket\_name

```python
@classmethod
def set_static_mesh_socket_name(cls, socket: StaticMeshSocket,
                                socket_name: Name) -> StaticMeshSocket
```

X.set_static_mesh_socket_name(socket, socket_name) -> StaticMeshSocket
Set the name of static mesh socket.
deprecated: SetStaticMeshSocketName is deprecated, use set_editor_property('socket_name', new_socket_name) instead
result: The mesh socket.

Args:
    socket (StaticMeshSocket): The target Socket.
    socket_name (Name): The new name of socket.

Returns:
    StaticMeshSocket:

<a id="unreal.PythonMeshLib.set_static_mesh_materials"></a>

#### set\_static\_mesh\_materials

```python
@classmethod
def set_static_mesh_materials(cls, mesh: StaticMesh,
                              materials: Array[StaticMaterial],
                              slot_names: Array[Name]) -> None
```

X.set_static_mesh_materials(mesh, materials, slot_names) -> None
Get all Static Materials of static mesh.

Args:
    mesh (StaticMesh): The target static mesh.
    materials (Array[StaticMaterial]): The material list you want to set to the mesh.
    slot_names (Array[Name]): The new material slot names of the mesh.

<a id="unreal.PythonMeshLib.set_lod_section_material_slot_index"></a>

#### set\_lod\_section\_material\_slot\_index

```python
@classmethod
def set_lod_section_material_slot_index(cls, static_mesh: StaticMesh,
                                        lod_index: int, section_index: int,
                                        new_material_slot_index: int,
                                        new_material_slot_name: Name) -> None
```

X.set_lod_section_material_slot_index(static_mesh, lod_index, section_index, new_material_slot_index, new_material_slot_name) -> None
Set Material Slot Index of Specified mesh LOD.

Args:
    static_mesh (StaticMesh): 
    lod_index (int32): 
    section_index (int32): The section index of LOD.
    new_material_slot_index (int32): The new material slot index for the section.
    new_material_slot_name (Name): The name for material slot.

<a id="unreal.PythonMeshLib.rasterize_and_trace_triangles_uv"></a>

#### rasterize\_and\_trace\_triangles\_uv

```python
@classmethod
def rasterize_and_trace_triangles_uv(
    cls, world: World, target_mesh: DynamicMesh, triangle_ids: Array[int],
    uv_channel: int, texture_width: int, texture_height: int,
    transform: Transform, start_point: Vector, profile_name: Name,
    debug_draw: bool
) -> Tuple[Array[IntPoint], Array[IntPoint], Array[int], Array[int]]
```

X.rasterize_and_trace_triangles_uv(world, target_mesh, triangle_ids, uv_channel, texture_width, texture_height, transform, start_point, profile_name, debug_draw) -> (blocked_points=Array[IntPoint], not_blocked_points=Array[IntPoint], each_triangles_pixel_counts=Array[int32], each_triangles_blocked_pixel_counts=Array[int32])
Trace the visibility of DynamicMesh in current view.(Experimental)
note: added in v1.2.0 (Experimental)
note: need UE5.2+

Args:
    world (World): The world of DynamicMesh.
    target_mesh (DynamicMesh): The target DynamicMesh.
    triangle_ids (Array[int32]): The triangle ids of DynamicMesh for trace.
    uv_channel (int32): The uv channel of DynamicMesh.
    texture_width (int32): The width of texture.
    texture_height (int32): The height of texture.
    transform (Transform): The transform of DynamicMesh.
    start_point (Vector): The start point of trace.
    profile_name (Name): The trace profile name.
    debug_draw (bool): Debug draw or not.

Returns:
    tuple: 

    blocked_points (Array[IntPoint]): 

    not_blocked_points (Array[IntPoint]): 

    each_triangles_pixel_counts (Array[int32]): 

    each_triangles_blocked_pixel_counts (Array[int32]):

<a id="unreal.PythonMeshLib.is_this_lod_generated_by_mesh_reduction"></a>

#### is\_this\_lod\_generated\_by\_mesh\_reduction

```python
@classmethod
def is_this_lod_generated_by_mesh_reduction(cls, mesh: StaticMesh,
                                            lod_level: int) -> bool
```

X.is_this_lod_generated_by_mesh_reduction(mesh, lod_level) -> bool
Is Specified LOD is generated in editor.
result: Whether this LOD's mesh is generated in editor or not.

Args:
    mesh (StaticMesh): The target static mesh.
    lod_level (int32): Specified LOD level.

Returns:
    bool:

<a id="unreal.PythonMeshLib.get_visible_triangles"></a>

#### get\_visible\_triangles

```python
@classmethod
def get_visible_triangles(
        cls, target_mesh: DynamicMesh, mesh_transform: Transform,
        view_info: MinimalViewInfo,
        invert: bool) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.get_visible_triangles(target_mesh, mesh_transform, view_info, invert) -> (DynamicMesh, selection_out=GeometryScriptMeshSelection)
Get the visible triangles of DynamicMesh in current view.
note: need UE 5.1+

Args:
    target_mesh (DynamicMesh): The target DynamicMesh.
    mesh_transform (Transform): The transform of DynamicMesh.
    view_info (MinimalViewInfo): The current view info.
    invert (bool): Invert the selection or not.

Returns:
    GeometryScriptMeshSelection: The visible triangles of DynamicMesh(FGeometryScriptMeshSelection).

    selection_out (GeometryScriptMeshSelection):

<a id="unreal.PythonMeshLib.get_triangles_face_normal_in_view"></a>

#### get\_triangles\_face\_normal\_in\_view

```python
@classmethod
def get_triangles_face_normal_in_view(
        cls, target_mesh_component: DynamicMeshComponent,
        triangle_ids: Array[int], view_info: MinimalViewInfo) -> Array[Vector]
```

X.get_triangles_face_normal_in_view(target_mesh_component, triangle_ids, view_info) -> Array[Vector]
Get the face normal of DynamicMesh in current view.  (Experimental)
note: added in v1.2.0 (Experimental)
note: need UE5.2+

Args:
    target_mesh_component (DynamicMeshComponent): The target DynamicMeshComponent.
    triangle_ids (Array[int32]): The triangle ids of DynamicMesh.
    view_info (MinimalViewInfo): The current view info.

Returns:
    Array[Vector]: The face normals of each triangle of DynamicMesh.

<a id="unreal.PythonMeshLib.get_static_mesh_sockets"></a>

#### get\_static\_mesh\_sockets

```python
@classmethod
def get_static_mesh_sockets(cls, obj: Object) -> Array[StaticMeshSocket]
```

X.get_static_mesh_sockets(obj) -> Array[StaticMeshSocket]
Get the static mesh sockets of the mesh object
result: The static mesh sockets of the mesh.

Args:
    obj (Object): The target mesh.

Returns:
    Array[StaticMeshSocket]:

<a id="unreal.PythonMeshLib.get_static_mesh_materials"></a>

#### get\_static\_mesh\_materials

```python
@classmethod
def get_static_mesh_materials(cls, mesh: StaticMesh) -> Array[StaticMaterial]
```

X.get_static_mesh_materials(mesh) -> Array[StaticMaterial]
Get all Static Materials of static mesh.

Args:
    mesh (StaticMesh): The Static Mesh owned the Materials.

Returns:
    Array[StaticMaterial]: 

    out_materials (Array[StaticMaterial]): The Static Materials of the mesh in list.

<a id="unreal.PythonMeshLib.get_section_cast_shadow"></a>

#### get\_section\_cast\_shadow

```python
@classmethod
def get_section_cast_shadow(cls, static_mesh: StaticMesh, lod_level: int,
                            section_id: int) -> bool
```

X.get_section_cast_shadow(static_mesh, lod_level, section_id) -> bool
Is specified section of LOD cast shadow.
result: Whether this section of mesh cast shadow.

Args:
    static_mesh (StaticMesh): 
    lod_level (int32): Specified LOD level.
    section_id (int32): Specified section id of LOD.

Returns:
    bool:

<a id="unreal.PythonMeshLib.get_overlapping_sphere_count"></a>

#### get\_overlapping\_sphere\_count

```python
@classmethod
def get_overlapping_sphere_count(
        cls, hism: HierarchicalInstancedStaticMeshComponent,
        sphere_center: Vector, sphere_radius: float) -> int
```

X.get_overlapping_sphere_count(hism, sphere_center, sphere_radius) -> int32
Get the number of instances that overlap a given sphere
result: The overlapped number of instances.

Args:
    hism (HierarchicalInstancedStaticMeshComponent): The target HierarchicalInstancedStaticMeshComponent.
    sphere_center (Vector): The center position of Sphere for overlapping test.
    sphere_radius (float): The radius of Sphere.

Returns:
    int32:

<a id="unreal.PythonMeshLib.get_overlapping_box_count"></a>

#### get\_overlapping\_box\_count

```python
@classmethod
def get_overlapping_box_count(cls,
                              hism: HierarchicalInstancedStaticMeshComponent,
                              box: Box) -> int
```

X.get_overlapping_box_count(hism, box) -> int32
Get the number of instances that overlap a given box
result: The overlapped number of instances.

Args:
    hism (HierarchicalInstancedStaticMeshComponent): The target HierarchicalInstancedStaticMeshComponent.
    box (Box): Box for overlapping test.

Returns:
    int32:

<a id="unreal.PythonMeshLib.get_original_lod_mat_names"></a>

#### get\_original\_lod\_mat\_names

```python
@classmethod
def get_original_lod_mat_names(cls, mesh: StaticMesh,
                               lod_level: int) -> Optional[Array[str]]
```

X.get_original_lod_mat_names(mesh, lod_level) -> Array[str] or None
Get the Section Original Material Names from specified LOD of mesh.

Args:
    mesh (StaticMesh): The target static mesh.
    lod_level (int32): Specified LOD level.

Returns:
    Array[str] or None: 

    out_material_names (Array[str]): The Material's names.

<a id="unreal.PythonMeshLib.get_original_lod_data_count"></a>

#### get\_original\_lod\_data\_count

```python
@classmethod
def get_original_lod_data_count(cls, mesh: StaticMesh) -> int
```

X.get_original_lod_data_count(mesh) -> int32
Get number of LODs from ImportMeshData. It's may not equal to the number of actual mesh asset, which can generate lods in editor.

Args:
    mesh (StaticMesh): The target static mesh.

Returns:
    int32: The number of LOD.

<a id="unreal.PythonMeshLib.get_imported_original_mat_names"></a>

#### get\_imported\_original\_mat\_names

```python
@classmethod
def get_imported_original_mat_names(cls,
                                    mesh: StaticMesh) -> Optional[Array[str]]
```

X.get_imported_original_mat_names(mesh) -> Array[str] or None
Get the names from Mesh's ImportMaterialOriginalNameData of StaticMesh's ImportData

Args:
    mesh (StaticMesh): The target static mesh.

Returns:
    Array[str] or None: 

    out_material_names (Array[str]): The names in material original name data.

<a id="unreal.PythonMeshLib.export_normal_and_derivatives"></a>

#### export\_normal\_and\_derivatives

```python
@classmethod
def export_normal_and_derivatives(cls, mesh_component: DynamicMeshComponent,
                                  triangle_ids: Array[int], uv_channel: int,
                                  view_info: MinimalViewInfo,
                                  view_size: Vector2D,
                                  export_tex_size: int) -> Array[int]
```

X.export_normal_and_derivatives(mesh_component, triangle_ids, uv_channel, view_info, view_size, export_tex_size) -> Array[uint8]
Export the current normal and mip of DynamicMesh in current view as raw data. (Experimental)
note: added in v1.2.0 (Experimental)
note: need UE5.2+

Args:
    mesh_component (DynamicMeshComponent): The target DynamicMeshComponent.
    triangle_ids (Array[int32]): The triangle ids of DynamicMesh.
    uv_channel (int32): The uv channel of DynamicMesh.
    view_info (MinimalViewInfo): The current view info.
    view_size (Vector2D): The size of current view
    export_tex_size (int32): The width and height of exported square texture.

Returns:
    Array[uint8]: The raw data of exported texture.

<a id="unreal.PythonMeshLib.convert_procedural_mesh_to_static_mesh"></a>

#### convert\_procedural\_mesh\_to\_static\_mesh

```python
@classmethod
def convert_procedural_mesh_to_static_mesh(
        cls,
        proc_mesh_comp: ProceduralMeshComponent,
        package_path: str,
        recompute_normals: bool = False,
        recompute_tangents: bool = False,
        remove_degenerates: bool = False,
        use_high_precision_tangent_basis: bool = False,
        use_full_precision_u_vs: bool = False,
        generate_lightmap_u_vs: bool = True) -> StaticMesh
```

X.convert_procedural_mesh_to_static_mesh(proc_mesh_comp, package_path, recompute_normals=False, recompute_tangents=False, remove_degenerates=False, use_high_precision_tangent_basis=False, use_full_precision_u_vs=False, generate_lightmap_u_vs=True) -> StaticMesh
UStaticMesh* StaticMeshvert the procedural mesh to static mesh asset

Args:
    proc_mesh_comp (ProceduralMeshComponent): The ProcMeshComp mesh Component
    package_path (str): The StaticMesh Asset package path
    recompute_normals (bool): Recompute mesh normal or not, default = false
    recompute_tangents (bool): Recompute mesh tangents or not, default = false
    remove_degenerates (bool): Remove Degenerates triangles or not, default = false
    use_high_precision_tangent_basis (bool): Use high precision tangent basis or not, default = false
    use_full_precision_u_vs (bool): Stored UVs with full floating point precision or not, default = false
    generate_lightmap_u_vs (bool): Generate Lightmap UVs or not, default = true

Returns:
    StaticMesh: return the converted static mesh

<a id="unreal.PythonMeshLib.cal_triangles_derivatives"></a>

#### cal\_triangles\_derivatives

```python
@classmethod
def cal_triangles_derivatives(cls, mesh_component: DynamicMeshComponent,
                              triangle_ids: Array[int], uv_channel: int,
                              view_info: MinimalViewInfo,
                              view_size: Vector2D) -> Array[Vector2D]
```

X.cal_triangles_derivatives(mesh_component, triangle_ids, uv_channel, view_info, view_size) -> Array[Vector2D]
Calculate the merged ddxy of DynamicMesh's triangles in current view. (Experimental)
note: added in v1.2.0 (Experimental)
note: need UE5.2+

Args:
    mesh_component (DynamicMeshComponent): The target DynamicMeshComponent.
    triangle_ids (Array[int32]): The triangle ids of DynamicMesh.
    uv_channel (int32): The uv channel of DynamicMesh.
    view_info (MinimalViewInfo): The current view info.
    view_size (Vector2D): The size of current view

Returns:
    Array[Vector2D]: The merged ddxy of DynamicMesh's triangles, which not the same as ddx，ddy in shader.

<a id="unreal.PythonMeshLib.apply_nanite"></a>

#### apply\_nanite

```python
@classmethod
def apply_nanite(cls, static_mesh: StaticMesh, enable_nanite: bool) -> None
```

X.apply_nanite(static_mesh, enable_nanite) -> None
Set and Apply the Enable Nanite of static mesh asset. UE5 Only.
note: This function will trigger Nanite mesh rebuild, which will cost several seconds or more.

Args:
    static_mesh (StaticMesh): The target static mesh asset.
    enable_nanite (bool): Enable Nanite or not.

<a id="unreal.PythonPhysicsAssetLib"></a>