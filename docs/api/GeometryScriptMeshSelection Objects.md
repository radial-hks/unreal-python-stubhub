## GeometryScriptMeshSelection Objects

```python
class GeometryScriptMeshSelection(StructBase)
```

FGeometryScriptMeshSelection is a container for a Mesh Selection used in Geometry Script.
The actual selection representation is not exposed to BP,
use functions in MeshSelectionFunctions/etc to manipulate the selection.

Internally the selection is stored as a SharedPtr to a FGeometrySelection, which
stores a TSet (so unique add and remove are efficient, but the selection cannot
be directly indexed without converting to an Array).

Note that the Selection storage is not a UProperty, and is not
serialized. FGeometryScriptMeshSelection instances *cannot* be serialized,
they are only transient data structures, that can be created and used Blueprint instances.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptSelectionTypes.h

<a id="unreal.GeometryScriptMeshSelection.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptMeshSelection.get_mesh_selection_info"></a>

#### get_mesh_selection_info

```python
def get_mesh_selection_info() -> Tuple[GeometryScriptMeshSelectionType, int]
```

x.get_mesh_selection_info() -> (selection_type=GeometryScriptMeshSelectionType, num_selected=int32)
Query information about a Mesh Selection
Note that NumSelected may double count some polygroups and (non-border) edges due to their internal representation
Use GetMeshUniqueSelectionInfo for an accurate count of unique mesh elements

Returns:
    tuple: 

    selection_type (GeometryScriptMeshSelectionType): 

    num_selected (int32):

<a id="unreal.GeometryScriptMeshSelection.debug_print_mesh_selection"></a>

#### debug_print_mesh_selection

```python
def debug_print_mesh_selection(disable: bool = False) -> None
```

x.debug_print_mesh_selection(disable=False) -> None
Print information about the Mesh Selection to the Output Log

Args:
    disable (bool): if true, printing will be disabled (useful for debugging)

<a id="unreal.GeometryScriptMeshSelection.combine_mesh_selections"></a>

#### combine_mesh_selections

```python
def combine_mesh_selections(
    selection_b: GeometryScriptMeshSelection,
    combine_mode:
    GeometryScriptCombineSelectionMode = GeometryScriptCombineSelectionMode.ADD
) -> GeometryScriptMeshSelection
```

x.combine_mesh_selections(selection_b, combine_mode=GeometryScriptCombineSelectionMode.ADD) -> GeometryScriptMeshSelection
Combine two Mesh Selections into a new Mesh Selection.
The two inputs SelectionA and SelectionB must have the same Type.

Args:
    selection_b (GeometryScriptMeshSelection): 
    combine_mode (GeometryScriptCombineSelectionMode): specifies how the selection elements in SelectionA and SelectionB are interpreted/combined.

Returns:
    GeometryScriptMeshSelection: 

    result_selection (GeometryScriptMeshSelection):

<a id="unreal.GeometryScriptCopyMeshFromAssetOptions"></a>