## GeometryScript_PolyGroups Objects

```python
class GeometryScript_PolyGroups(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Polygroup Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPolygroupFunctions.h

<a id="unreal.GeometryScript_PolyGroups.set_polygroup_for_mesh_selection"></a>

#### set_polygroup_for_mesh_selection

```python
@classmethod
def set_polygroup_for_mesh_selection(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        selection: GeometryScriptMeshSelection,
        set_polygroup_id: int = 0,
        generate_new_polygroup: bool = False,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, int]
```

X.set_polygroup_for_mesh_selection(target_mesh, group_layer, selection, set_polygroup_id=0, generate_new_polygroup=False, defer_change_notifications=False) -> (DynamicMesh, set_polygroup_id_out=int32)
Set a new PolyGroup on all the triangles of the given Selection, for the given GroupLayer.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    selection (GeometryScriptMeshSelection): 
    set_polygroup_id (int32): explicit new PolyGroupID to set
    generate_new_polygroup (bool): if true, SetPolyGroupID is ignored and a new unique PolyGroupID is generated
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification

Returns:
    int32: 

    set_polygroup_id_out (int32): the PolyGroupID that was set on the triangles is returned here (whether explicit or auto-generated)

<a id="unreal.GeometryScript_PolyGroups.set_num_extended_polygroup_layers"></a>

#### set_num_extended_polygroup_layers

```python
@classmethod
def set_num_extended_polygroup_layers(
        cls,
        target_mesh: DynamicMesh,
        num_layers: int,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_num_extended_polygroup_layers(target_mesh, num_layers, debug=None) -> DynamicMesh
Sets the number of extended PolyGroup Layers on a Mesh.

Args:
    target_mesh (DynamicMesh): 
    num_layers (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.get_triangles_in_polygroup"></a>

#### get_triangles_in_polygroup

```python
@classmethod
def get_triangles_in_polygroup(
    cls, target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer,
    polygroup_id: int, triangle_i_ds_out: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.get_triangles_in_polygroup(target_mesh, group_layer, polygroup_id, triangle_i_ds_out) -> (DynamicMesh, triangle_i_ds_out=GeometryScriptIndexList)
Create list of all triangles with the given PolyGroup ID in the given GroupLayer (not necessarily a single connected-component)

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    polygroup_id (int32): 
    triangle_i_ds_out (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    triangle_i_ds_out (GeometryScriptIndexList):

<a id="unreal.GeometryScript_PolyGroups.get_triangle_polygroup_id"></a>

#### get_triangle_polygroup_id

```python
@classmethod
def get_triangle_polygroup_id(cls, target_mesh: DynamicMesh,
                              group_layer: GeometryScriptGroupLayer,
                              triangle_id: int) -> Tuple[int, bool]
```

X.get_triangle_polygroup_id(target_mesh, group_layer, triangle_id) -> (int32, is_valid_triangle=bool)
Gets the PolyGroup ID associated with the specified Triangle ID and stored in the Group Layer.
If the Group Layer or the Triangle does not exist, the value 0 will be returned and bIsValidTriangle set to false.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): indicates the layer on the Target Mesh to query.
    triangle_id (int32): identifies a triangle in the Target Mesh.

Returns:
    bool: 

    is_valid_triangle (bool): will be populated on return with false if either the Group Layer or the Triangle does not exist.

<a id="unreal.GeometryScript_PolyGroups.get_polygroup_i_ds_in_mesh"></a>

#### get_polygroup_i_ds_in_mesh

```python
@classmethod
def get_polygroup_i_ds_in_mesh(
    cls, target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer,
    polygroup_i_ds_out: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.get_polygroup_i_ds_in_mesh(target_mesh, group_layer, polygroup_i_ds_out) -> (DynamicMesh, polygroup_i_ds_out=GeometryScriptIndexList)
Create list of all unique PolyGroup IDs that exist in the PolyGroup Layer in the Mesh

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    polygroup_i_ds_out (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    polygroup_i_ds_out (GeometryScriptIndexList):

<a id="unreal.GeometryScript_PolyGroups.get_all_triangle_polygroup_i_ds"></a>

#### get_all_triangle_polygroup_i_ds

```python
@classmethod
def get_all_triangle_polygroup_i_ds(
    cls, target_mesh: DynamicMesh, group_layer: GeometryScriptGroupLayer,
    polygroup_i_ds_out: GeometryScriptIndexList
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.get_all_triangle_polygroup_i_ds(target_mesh, group_layer, polygroup_i_ds_out) -> (DynamicMesh, polygroup_i_ds_out=GeometryScriptIndexList)
Create list of per-triangle PolyGroup IDs for the PolyGroup in the Mesh
warning: if the mesh is not Triangle-Compact (eg GetHasTriangleIDGaps == false) then the returned list will also have the same gaps

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    polygroup_i_ds_out (GeometryScriptIndexList): 

Returns:
    GeometryScriptIndexList: 

    polygroup_i_ds_out (GeometryScriptIndexList):

<a id="unreal.GeometryScript_PolyGroups.enable_polygroups"></a>

#### enable_polygroups

```python
@classmethod
def enable_polygroups(cls,
                      target_mesh: DynamicMesh,
                      debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.enable_polygroups(target_mesh, debug=None) -> DynamicMesh
Enables the standard PolyGroup Layer on the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.delete_triangles_in_polygroup"></a>

#### delete_triangles_in_polygroup

```python
@classmethod
def delete_triangles_in_polygroup(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        polygroup_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
```

X.delete_triangles_in_polygroup(target_mesh, group_layer, polygroup_id, defer_change_notifications=False, debug=None) -> (DynamicMesh, num_deleted=int32)
Deletes all triangles from the Target Mesh that have a particular PolyGroup ID, in the specific Group Layer.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): specifies the PolyGroup Layer to query.
    polygroup_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    int32: 

    num_deleted (int32): on return will contain the number of triangles deleted from the Target Mesh.

<a id="unreal.GeometryScript_PolyGroups.copy_polygroups_layer"></a>

#### copy_polygroups_layer

```python
@classmethod
def copy_polygroups_layer(cls,
                          target_mesh: DynamicMesh,
                          from_group_layer: GeometryScriptGroupLayer,
                          to_group_layer: GeometryScriptGroupLayer,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.copy_polygroups_layer(target_mesh, from_group_layer, to_group_layer, debug=None) -> DynamicMesh
Copies the triangle PolyGroup assignments from one layer on the Target Mesh to another.
Note, this will have no effect if PolyGroups have not been enabled on the mesh, or if one of the requested Group Layers does not exist.

Args:
    target_mesh (DynamicMesh): 
    from_group_layer (GeometryScriptGroupLayer): 
    to_group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.convert_uv_islands_to_polygroups"></a>

#### convert_uv_islands_to_polygroups

```python
@classmethod
def convert_uv_islands_to_polygroups(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        uv_layer: int = 0,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.convert_uv_islands_to_polygroups(target_mesh, group_layer, uv_layer=0, debug=None) -> DynamicMesh
Creates and assigns a new PolyGroup for each disconnected UV island of a Mesh.
Note, this will have no effect if either the requested UV Layer or Group Layer does not exist.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): indicates PolyGroup Layer that will be populated with unique values for each UV island.
    uv_layer (int32): specifies the UV Layer used to construct the PolyGroups.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.convert_components_to_polygroups"></a>

#### convert_components_to_polygroups

```python
@classmethod
def convert_components_to_polygroups(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.convert_components_to_polygroups(target_mesh, group_layer, debug=None) -> DynamicMesh
Creates and assigns a new PolyGroup for each disconnected component of a Mesh. Regions of a mesh are disconnected they do not have a triangle in common.
Note, this will have no effect if the Group Layer does not exist.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.compute_polygroups_from_polygon_detection"></a>

#### compute_polygroups_from_polygon_detection

```python
@classmethod
def compute_polygroups_from_polygon_detection(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        respect_uv_seams: bool = True,
        respect_hard_normals: bool = False,
        quad_adjacency_weight: float = 1.000000,
        quad_metric_clamp: float = 1.000000,
        max_search_rounds: int = 1,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.compute_polygroups_from_polygon_detection(target_mesh, group_layer, respect_uv_seams=True, respect_hard_normals=False, quad_adjacency_weight=1.000000, quad_metric_clamp=1.000000, max_search_rounds=1, debug=None) -> DynamicMesh
Sets PolyGroups by identifying adjacent triangles that form reasonable quads. Note any triangles that do not neatly pair to form quads will receive their own PolyGroup.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    respect_uv_seams (bool): 
    respect_hard_normals (bool): 
    quad_adjacency_weight (double): 
    quad_metric_clamp (double): 
    max_search_rounds (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.compute_polygroups_from_angle_threshold"></a>

#### compute_polygroups_from_angle_threshold

```python
@classmethod
def compute_polygroups_from_angle_threshold(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        crease_angle: float = 15.000000,
        min_group_size: int = 2,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.compute_polygroups_from_angle_threshold(target_mesh, group_layer, crease_angle=15.000000, min_group_size=2, debug=None) -> DynamicMesh
Sets PolyGroups by partitioning the mesh based on an edge crease/opening-angle.
Note, this will have no effect if the Group Layer does not exist.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): indicates the PolyGroup Layer that will be populated.
    crease_angle (float): measured in degrees and used when comparing adjacent faces.
    min_group_size (int32): the minimum number of triangles in each PolyGroup.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_PolyGroups.clear_polygroups"></a>

#### clear_polygroups

```python
@classmethod
def clear_polygroups(cls,
                     target_mesh: DynamicMesh,
                     group_layer: GeometryScriptGroupLayer,
                     clear_value: int = 0,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.clear_polygroups(target_mesh, group_layer, clear_value=0, debug=None) -> DynamicMesh
Resets the triangle PolyGroup assignments within a PolyGroup Layer to the given Clear Value (or 0 if no Clear Value is specified).
Note, this will have no effect if PolyGroups have not been enabled on the mesh, or if the requested Group Layer does not exist.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    clear_value (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshPoolUtility"></a>