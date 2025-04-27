## GeometryScript_MeshSelection Objects

```python
class GeometryScript_MeshSelection(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Selection Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSelectionFunctions.h

<a id="unreal.GeometryScript_MeshSelection.select_selection_boundary_edges"></a>

#### select_selection_boundary_edges

```python
@classmethod
def select_selection_boundary_edges(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    exclude_mesh_boundary_edges: bool = False
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_selection_boundary_edges(target_mesh, selection, exclude_mesh_boundary_edges=False) -> (DynamicMesh, boundary_selection=GeometryScriptMeshSelection)
Create a new BoundarySelection, for the TargetMesh, of the edges on the boundary of another Selection

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    exclude_mesh_boundary_edges (bool): If true, do not include Selection boundary edges if they are also mesh boundary edges

Returns:
    GeometryScriptMeshSelection: 

    boundary_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_sharp_edges"></a>

#### select_mesh_sharp_edges

```python
@classmethod
def select_mesh_sharp_edges(
    cls,
    target_mesh: DynamicMesh,
    min_angle_deg: float = 20.000000
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_sharp_edges(target_mesh, min_angle_deg=20.000000) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Selection, for the TargetMesh, of all 'sharp' edges where the edge's adjacent triangle normals differ by at least MinAngleDeg

Args:
    target_mesh (DynamicMesh): 
    min_angle_deg (double): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_with_plane"></a>

#### select_mesh_elements_with_plane

```python
@classmethod
def select_mesh_elements_with_plane(
    cls,
    target_mesh: DynamicMesh,
    plane_origin: Vector = [0.000000, 0.000000, 0.000000],
    plane_normal: Vector = [0.000000, 0.000000, 1.000000],
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_with_plane(target_mesh, plane_origin=[0.000000, 0.000000, 0.000000], plane_normal=[0.000000, 0.000000, 1.000000], selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements on the "positive" side of a Plane

Args:
    target_mesh (DynamicMesh): 
    plane_origin (Vector): center point of the Plane
    plane_normal (Vector): normal vector for the Plane
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements on the other (negative) side of the Plane
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_in_sphere"></a>

#### select_mesh_elements_in_sphere

```python
@classmethod
def select_mesh_elements_in_sphere(
    cls,
    target_mesh: DynamicMesh,
    sphere_origin: Vector = [0.000000, 0.000000, 0.000000],
    sphere_radius: float = 100.000000,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_in_sphere(target_mesh, sphere_origin=[0.000000, 0.000000, 0.000000], sphere_radius=100.000000, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements contained in the Sphere.

Args:
    target_mesh (DynamicMesh): 
    sphere_origin (Vector): center point of the Sphere
    sphere_radius (double): radius of the Sphere
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not in the Sphere
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_inside_mesh"></a>

#### select_mesh_elements_inside_mesh

```python
@classmethod
def select_mesh_elements_inside_mesh(
    cls,
    target_mesh: DynamicMesh,
    selection_mesh: DynamicMesh,
    selection_mesh_transform: Transform,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    shell_distance: float = 0.000000,
    winding_threshold: float = 0.500000,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_inside_mesh(target_mesh, selection_mesh, selection_mesh_transform, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, shell_distance=0.000000, winding_threshold=0.500000, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements inside a second SelectionMesh
For Triangle and PolyGroup selections the triangle facet normal is used, for Vertex selections the per-vertex averaged normal is used.

Args:
    target_mesh (DynamicMesh): 
    selection_mesh (DynamicMesh): 
    selection_mesh_transform (Transform): Transform applied to SelectionMesh for inside/outside testing
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not within the given deviation
    shell_distance (double): If > 0, points within this distance from SelectionMesh will also be considered "inside"
    winding_threshold (double): Threshold used for Fast Mesh Winding Number inside/outside test (range is [0,1], with 1 being "inside")
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_in_box"></a>

#### select_mesh_elements_in_box

```python
@classmethod
def select_mesh_elements_in_box(
    cls,
    target_mesh: DynamicMesh,
    box: Box,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_in_box(target_mesh, box, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements contained in the Box.

Args:
    target_mesh (DynamicMesh): 
    box (Box): 
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not in the Box
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_by_polygroup"></a>

#### select_mesh_elements_by_polygroup

```python
@classmethod
def select_mesh_elements_by_polygroup(
    cls,
    target_mesh: DynamicMesh,
    group_layer: GeometryScriptGroupLayer,
    polygroup_id: int,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_by_polygroup(target_mesh, group_layer, polygroup_id, selection_type=GeometryScriptMeshSelectionType.TRIANGLES) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Selection of the SelectionType that contains all mesh elements referencing triangles with the given PolyGroup ID in the given GroupLayer

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): 
    polygroup_id (int32): 
    selection_type (GeometryScriptMeshSelectionType): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_by_normal_angle"></a>

#### select_mesh_elements_by_normal_angle

```python
@classmethod
def select_mesh_elements_by_normal_angle(
    cls,
    target_mesh: DynamicMesh,
    normal: Vector = [0.000000, 0.000000, 1.000000],
    max_angle_deg: float = 1.000000,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.
    TRIANGLES,
    invert: bool = False,
    min_num_triangle_points: int = 3
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_by_normal_angle(target_mesh, normal=[0.000000, 0.000000, 1.000000], max_angle_deg=1.000000, selection_type=GeometryScriptMeshSelectionType.TRIANGLES, invert=False, min_num_triangle_points=3) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Mesh Selection of the SelectionType for the TargetMesh by finding all elements that have a normal
vector that is within an angular deviation threshold from the given Normal.
For Triangle and PolyGroup selections the triangle facet normal is used, for Vertex selections the per-vertex averaged normal is used.

Args:
    target_mesh (DynamicMesh): 
    normal (Vector): normal/direction vector to measure against
    max_angle_deg (double): maximum angular deviation from Normal, in degrees
    selection_type (GeometryScriptMeshSelectionType): 
    invert (bool): return a selection of all elements not within the given deviation
    min_num_triangle_points (int32): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_elements_by_material_id"></a>

#### select_mesh_elements_by_material_id

```python
@classmethod
def select_mesh_elements_by_material_id(
    cls,
    target_mesh: DynamicMesh,
    material_id: int,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_elements_by_material_id(target_mesh, material_id, selection_type=GeometryScriptMeshSelectionType.TRIANGLES) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Selection of the SelectionType that contains all mesh elements referencing triangles with the given Material ID

Args:
    target_mesh (DynamicMesh): 
    material_id (int32): 
    selection_type (GeometryScriptMeshSelectionType): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.select_mesh_boundary_edges"></a>

#### select_mesh_boundary_edges

```python
@classmethod
def select_mesh_boundary_edges(
    cls, target_mesh: DynamicMesh
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.select_mesh_boundary_edges(target_mesh) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a new Selection, for the TargetMesh, of all mesh boundary edges

Args:
    target_mesh (DynamicMesh): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.invert_mesh_selection"></a>

#### invert_mesh_selection

```python
@classmethod
def invert_mesh_selection(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    only_to_connected: bool = False
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.invert_mesh_selection(target_mesh, selection, only_to_connected=False) -> (DynamicMesh, new_selection=GeometryScriptMeshSelection)
Invert the Selection on the TargetMesh, ie select what is not currently selected

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    only_to_connected (bool): if true, the inverse is limited to mesh areas geometrically connected to the Selection, instead of the entire mesh

Returns:
    GeometryScriptMeshSelection: 

    new_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.get_mesh_unique_selection_info"></a>

#### get_mesh_unique_selection_info

```python
@classmethod
def get_mesh_unique_selection_info(
    cls, target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection
) -> Tuple[GeometryScriptMeshSelectionType, int]
```

X.get_mesh_unique_selection_info(target_mesh, selection) -> (selection_type=GeometryScriptMeshSelectionType, num_selected=int32)
Query information about a Mesh Selection, and get a count of unique selected elements

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 

Returns:
    tuple: 

    selection_type (GeometryScriptMeshSelectionType): 

    num_selected (int32):

<a id="unreal.GeometryScript_MeshSelection.get_mesh_selection_info"></a>

#### get_mesh_selection_info

```python
@classmethod
def get_mesh_selection_info(
    cls, selection: GeometryScriptMeshSelection
) -> Tuple[GeometryScriptMeshSelectionType, int]
```

X.get_mesh_selection_info(selection) -> (selection_type=GeometryScriptMeshSelectionType, num_selected=int32)
Query information about a Mesh Selection
Note that NumSelected may double count some polygroups and (non-border) edges due to their internal representation
Use GetMeshUniqueSelectionInfo for an accurate count of unique mesh elements

Args:
    selection (GeometryScriptMeshSelection): 

Returns:
    tuple: 

    selection_type (GeometryScriptMeshSelectionType): 

    num_selected (int32):

<a id="unreal.GeometryScript_MeshSelection.expand_mesh_selection_to_connected"></a>

#### expand_mesh_selection_to_connected

```python
@classmethod
def expand_mesh_selection_to_connected(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    connection_type:
    GeometryScriptTopologyConnectionType = GeometryScriptTopologyConnectionType
    .GEOMETRIC
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.expand_mesh_selection_to_connected(target_mesh, selection, connection_type=GeometryScriptTopologyConnectionType.GEOMETRIC) -> (DynamicMesh, new_selection=GeometryScriptMeshSelection)
Expand the Selection on the TargetMesh to connected regions and return the NewSelection

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    connection_type (GeometryScriptTopologyConnectionType): defines what "connected" means, ie purely geometric connection, or some additional constraint like same MaterialIDs/etc

Returns:
    GeometryScriptMeshSelection: 

    new_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.expand_contract_mesh_selection"></a>

#### expand_contract_mesh_selection

```python
@classmethod
def expand_contract_mesh_selection(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    iterations: int = 1,
    contract: bool = False,
    only_expand_to_face_neighbours: bool = False
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.expand_contract_mesh_selection(target_mesh, selection, iterations=1, contract=False, only_expand_to_face_neighbours=False) -> (DynamicMesh, new_selection=GeometryScriptMeshSelection)
Grow or Shrink the Selection on the TargetMesh to connected neighbours.
For Vertex selections, Expand includes vertices in one-ring of selected vertices, and Contract removes any vertices with a one-ring neighbour that is not selected
For Triangle selections, Add/Remove Triangles connected to selected Triangles
For PolyGroup selections, Add/Remove PolyGroups connected to selected PolyGroups

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    iterations (int32): number of times to Expand/Contract the Selection. Valid range is [0,100] where 0 is a no-op.
    contract (bool): if true selection contracts instead of growing
    only_expand_to_face_neighbours (bool): if true, only adjacent Triangles/PolyGroups directly connected by an edge are added, vs connected to any selected vertex

Returns:
    GeometryScriptMeshSelection: 

    new_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.debug_print_mesh_selection"></a>

#### debug_print_mesh_selection

```python
@classmethod
def debug_print_mesh_selection(cls,
                               selection: GeometryScriptMeshSelection,
                               disable: bool = False) -> None
```

X.debug_print_mesh_selection(selection, disable=False) -> None
Print information about the Mesh Selection to the Output Log

Args:
    selection (GeometryScriptMeshSelection): 
    disable (bool): if true, printing will be disabled (useful for debugging)

<a id="unreal.GeometryScript_MeshSelection.create_select_all_mesh_selection"></a>

#### create_select_all_mesh_selection

```python
@classmethod
def create_select_all_mesh_selection(
    cls,
    target_mesh: DynamicMesh,
    selection_type:
    GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType.TRIANGLES
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.create_select_all_mesh_selection(target_mesh, selection_type=GeometryScriptMeshSelectionType.TRIANGLES) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Selection of the given SelectionType that contains all the mesh elements of TargetMesh

Args:
    target_mesh (DynamicMesh): 
    selection_type (GeometryScriptMeshSelectionType): 

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.convert_mesh_selection_to_index_list"></a>

#### convert_mesh_selection_to_index_list

```python
@classmethod
def convert_mesh_selection_to_index_list(
    cls,
    target_mesh: DynamicMesh,
    selection: GeometryScriptMeshSelection,
    convert_to_type: GeometryScriptIndexType = GeometryScriptIndexType.ANY
) -> Tuple[DynamicMesh, GeometryScriptIndexList, GeometryScriptIndexType]
```

X.convert_mesh_selection_to_index_list(target_mesh, selection, convert_to_type=GeometryScriptIndexType.ANY) -> (DynamicMesh, index_list=GeometryScriptIndexList, result_list_type=GeometryScriptIndexType)
Convert a Mesh Selection to an Index List

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    convert_to_type (GeometryScriptIndexType): optional parameter specifying the type of Index List to convert to. If Set to Any, no conversion will be performed.

Returns:
    tuple: 

    index_list (GeometryScriptIndexList): 

    result_list_type (GeometryScriptIndexType):

<a id="unreal.GeometryScript_MeshSelection.convert_mesh_selection_to_index_array"></a>

#### convert_mesh_selection_to_index_array

```python
@classmethod
def convert_mesh_selection_to_index_array(
    cls, target_mesh: DynamicMesh, selection: GeometryScriptMeshSelection
) -> Tuple[DynamicMesh, Array[int], GeometryScriptMeshSelectionType]
```

X.convert_mesh_selection_to_index_array(target_mesh, selection) -> (DynamicMesh, index_array=Array[int32], selection_type=GeometryScriptMeshSelectionType)
Convert a Mesh Selection to an Index Array

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 

Returns:
    tuple: 

    index_array (Array[int32]): 

    selection_type (GeometryScriptMeshSelectionType):

<a id="unreal.GeometryScript_MeshSelection.convert_mesh_selection"></a>

#### convert_mesh_selection

```python
@classmethod
def convert_mesh_selection(
    cls,
    target_mesh: DynamicMesh,
    from_selection: GeometryScriptMeshSelection,
    new_type: GeometryScriptMeshSelectionType = GeometryScriptMeshSelectionType
    .TRIANGLES,
    allow_partial_inclusion: bool = True
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.convert_mesh_selection(target_mesh, from_selection, new_type=GeometryScriptMeshSelectionType.TRIANGLES, allow_partial_inclusion=True) -> (DynamicMesh, to_selection=GeometryScriptMeshSelection)
Convert a Mesh Selection to a different Type (eg Vertices to Triangles, etc)
By default, Vertices map to Triangle one-rings, and Triangles to all contained vertices.
If bAllowPartialInclusion is disabled, then more restrictive conversions are performed, as follows:
  For To-Vertices, only include vertices where all one-ring triangles or edges are included in FromSelection.
  For To-Edges, only include edges where all adjacent triangles or vertices are included in FromSelection
  For To-Triangles, only include triangles where all tri vertices or edges are included in FromSelection.
  For To-PolyGroups, only include groups where all group triangles are touched by FromSelection
(Note: The To-PolyGroups rule allows vertex and edge selections that miss some vertices or edges, as long as they touch all the polygroup triangles.)

Args:
    target_mesh (DynamicMesh): 
    from_selection (GeometryScriptMeshSelection): 
    new_type (GeometryScriptMeshSelectionType): 
    allow_partial_inclusion (bool): if false, perform more limited selection conversion as described above

Returns:
    GeometryScriptMeshSelection: 

    to_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.convert_index_set_to_mesh_selection"></a>

#### convert_index_set_to_mesh_selection

```python
@classmethod
def convert_index_set_to_mesh_selection(
    cls, target_mesh: DynamicMesh, index_set: Set[int],
    selection_type: GeometryScriptMeshSelectionType
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.convert_index_set_to_mesh_selection(target_mesh, index_set, selection_type) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Mesh Selection from the IndexSet.

Args:
    target_mesh (DynamicMesh): 
    index_set (Set[int32]): 
    selection_type (GeometryScriptMeshSelectionType): type of indices specified in the selection

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.convert_index_list_to_mesh_selection"></a>

#### convert_index_list_to_mesh_selection

```python
@classmethod
def convert_index_list_to_mesh_selection(
    cls, target_mesh: DynamicMesh, index_list: GeometryScriptIndexList,
    selection_type: GeometryScriptMeshSelectionType
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.convert_index_list_to_mesh_selection(target_mesh, index_list, selection_type) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Mesh Selection from the Index List. For cases where the IndexList Type does not match
the SelectionType, ConvertMeshSelection with bAllowPartialInclusion=true is used to convert.

Args:
    target_mesh (DynamicMesh): 
    index_list (GeometryScriptIndexList): 
    selection_type (GeometryScriptMeshSelectionType): type of indices desired in the Output selection

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.convert_index_array_to_mesh_selection"></a>

#### convert_index_array_to_mesh_selection

```python
@classmethod
def convert_index_array_to_mesh_selection(
    cls, target_mesh: DynamicMesh, index_array: Array[int],
    selection_type: GeometryScriptMeshSelectionType
) -> Tuple[DynamicMesh, GeometryScriptMeshSelection]
```

X.convert_index_array_to_mesh_selection(target_mesh, index_array, selection_type) -> (DynamicMesh, selection=GeometryScriptMeshSelection)
Create a Mesh Selection from the IndexArray.

Args:
    target_mesh (DynamicMesh): 
    index_array (Array[int32]): 
    selection_type (GeometryScriptMeshSelectionType): type of indices specified in the selection

Returns:
    GeometryScriptMeshSelection: 

    selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelection.combine_mesh_selections"></a>

#### combine_mesh_selections

```python
@classmethod
def combine_mesh_selections(
    cls,
    selection_a: GeometryScriptMeshSelection,
    selection_b: GeometryScriptMeshSelection,
    combine_mode:
    GeometryScriptCombineSelectionMode = GeometryScriptCombineSelectionMode.ADD
) -> GeometryScriptMeshSelection
```

X.combine_mesh_selections(selection_a, selection_b, combine_mode=GeometryScriptCombineSelectionMode.ADD) -> GeometryScriptMeshSelection
Combine two Mesh Selections into a new Mesh Selection.
The two inputs SelectionA and SelectionB must have the same Type.

Args:
    selection_a (GeometryScriptMeshSelection): 
    selection_b (GeometryScriptMeshSelection): 
    combine_mode (GeometryScriptCombineSelectionMode): specifies how the selection elements in SelectionA and SelectionB are interpreted/combined.

Returns:
    GeometryScriptMeshSelection: 

    result_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScript_MeshSelectionQueries"></a>