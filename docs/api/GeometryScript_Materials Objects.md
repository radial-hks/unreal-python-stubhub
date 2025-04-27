## GeometryScript_Materials Objects

```python
class GeometryScript_Materials(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Material Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshMaterialFunctions.h

<a id="unreal.GeometryScript_Materials.set_triangle_material_id"></a>

#### set_triangle_material_id

```python
@classmethod
def set_triangle_material_id(
        cls,
        target_mesh: DynamicMesh,
        triangle_id: int,
        material_id: int,
        defer_change_notifications: bool = False) -> Tuple[DynamicMesh, bool]
```

X.set_triangle_material_id(target_mesh, triangle_id, material_id, defer_change_notifications=False) -> (DynamicMesh, is_valid_triangle=bool)
Assigns the specified triangle the given Material ID.
If the Target Mesh does not have Material IDs enabled, or if the Triangle ID is not an element of the Target Mesh then bIsValidTriangle will be set to false.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 
    material_id (int32): 
    defer_change_notifications (bool): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScript_Materials.set_polygroup_material_id"></a>

#### set_polygroup_material_id

```python
@classmethod
def set_polygroup_material_id(
        cls,
        target_mesh: DynamicMesh,
        group_layer: GeometryScriptGroupLayer,
        polygroup_id: int,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

X.set_polygroup_material_id(target_mesh, group_layer, polygroup_id, material_id, defer_change_notifications=False, debug=None) -> (DynamicMesh, is_valid_polygroup_id=bool)
Set a new MaterialID on all the triangles of TargetMesh with the given PolyGroup.

Args:
    target_mesh (DynamicMesh): 
    group_layer (GeometryScriptGroupLayer): PolyGroup Layer to use as basis for PolyGroups
    polygroup_id (int32): PolyGroup ID that specifies Triangles to set to new MaterialID
    material_id (int32): explicit new MaterialID to set
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    is_valid_polygroup_id (bool):

<a id="unreal.GeometryScript_Materials.set_material_id_on_triangles"></a>

#### set_material_id_on_triangles

```python
@classmethod
def set_material_id_on_triangles(
        cls,
        target_mesh: DynamicMesh,
        triangle_id_list: GeometryScriptIndexList,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_material_id_on_triangles(target_mesh, triangle_id_list, material_id, defer_change_notifications=False, debug=None) -> DynamicMesh
Assigns the Material ID to all the triangles specified by the Triangle ID List.

Args:
    target_mesh (DynamicMesh): 
    triangle_id_list (GeometryScriptIndexList): the triangles in the target mesh that will be updated with the new Material ID
    material_id (int32): the ID to be assigned to each triangle in the input list.
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Materials.set_material_id_for_mesh_selection"></a>

#### set_material_id_for_mesh_selection

```python
@classmethod
def set_material_id_for_mesh_selection(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_material_id_for_mesh_selection(target_mesh, selection, material_id, defer_change_notifications=False, debug=None) -> DynamicMesh
Set a new MaterialID on all the triangles of the given Selection.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    material_id (int32): new Material ID to set
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Materials.set_all_triangle_material_i_ds"></a>

#### set_all_triangle_material_i_ds

```python
@classmethod
def set_all_triangle_material_i_ds(
        cls,
        target_mesh: DynamicMesh,
        triangle_material_id_list: GeometryScriptIndexList,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_all_triangle_material_i_ds(target_mesh, triangle_material_id_list, defer_change_notifications=False, debug=None) -> DynamicMesh
Sets the Material ID of all triangles in a mesh to the values in an input Index List.

Args:
    target_mesh (DynamicMesh): 
    triangle_material_id_list (GeometryScriptIndexList): 
    defer_change_notifications (bool): if true, the UDynamicMesh does not emit a change event/signal for this modification.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Materials.remap_to_new_material_i_ds_by_material"></a>

#### remap_to_new_material_i_ds_by_material

```python
@classmethod
def remap_to_new_material_i_ds_by_material(
        cls,
        target_mesh: DynamicMesh,
        from_material_list: Array[MaterialInterface],
        to_material_list: Array[MaterialInterface],
        missing_material_id: int = -1,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.remap_to_new_material_i_ds_by_material(target_mesh, from_material_list, to_material_list, missing_material_id=-1, debug=None) -> DynamicMesh
Remap the Material IDs of the TargetMesh to a new set of Material IDs based on a 'From'/Current Material List, and a New Material List.
For each triangle, the current Material is determined as FromMaterialList[MaterialID], and then the first index of this Material is found
in the ToMaterialList, and this index is used as the new MaterialID

If a Material cannot be found in ToMaterialList, a warning will be printed and the MaterialID left unmodified,
unless MissingMaterialID is set to a value >= 0, in which case MissingMaterialID will be assigned

Args:
    target_mesh (DynamicMesh): 
    from_material_list (Array[MaterialInterface]): 
    to_material_list (Array[MaterialInterface]): 
    missing_material_id (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Materials.remap_material_i_ds"></a>

#### remap_material_i_ds

```python
@classmethod
def remap_material_i_ds(cls,
                        target_mesh: DynamicMesh,
                        from_material_id: int,
                        to_material_id: int,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.remap_material_i_ds(target_mesh, from_material_id, to_material_id, debug=None) -> DynamicMesh
For all triangles with a Material ID matching the given value (From Material ID), update the Material ID to the new value (To Material ID).

Args:
    target_mesh (DynamicMesh): 
    from_material_id (int32): 
    to_material_id (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Materials.remap_and_combine_materials"></a>

#### remap_and_combine_materials

```python
@classmethod
def remap_and_combine_materials(
    cls,
    target_mesh: DynamicMesh,
    target_mesh_materials: Array[MaterialInterface],
    required_materials: Array[MaterialInterface],
    remap_invalid_material_id: int = -1,
    compact_duplicate_materials: bool = True,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

X.remap_and_combine_materials(target_mesh, target_mesh_materials, required_materials, remap_invalid_material_id=-1, compact_duplicate_materials=True, debug=None) -> (DynamicMesh, combined_materials=Array[MaterialInterface])
Remap material IDs to be consistent with a Required Materials list.
The Target Mesh material IDs will be remapped to reference the Combined Materials list,
which will always start with the Required Materials.

If a Material cannot be found in CurrentMeshMaterials, a warning will be printed and the MaterialID left unmodified,
unless RemapInvalidMaterialID is set to a value >= 0, in which case RemapInvalidMaterialID will be assigned

Args:
    target_mesh (DynamicMesh): Mesh to update
    target_mesh_materials (Array[MaterialInterface]): Initial materials used by the TargetMesh
    required_materials (Array[MaterialInterface]): Materials that must be used, unchanged, in the output
    remap_invalid_material_id (int32): If >= 0, automatically remap invalid input material IDs to this value
    compact_duplicate_materials (bool): If true, materials from TargetMeshMaterials will only be added if they are not already in RequiredMaterials. If false, all TargetMeshMaterials are appended.
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    combined_materials (Array[MaterialInterface]): Final materials used by the TargetMesh after remapping. Always starts with the RequiredMaterials.

<a id="unreal.GeometryScript_Materials.get_triangles_by_material_id"></a>

#### get_triangles_by_material_id

```python
@classmethod
def get_triangles_by_material_id(
    cls,
    target_mesh: DynamicMesh,
    material_id: int,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.get_triangles_by_material_id(target_mesh, material_id, debug=None) -> (DynamicMesh, triangle_id_list=GeometryScriptIndexList)
Populates Triangle ID List with the Triangle IDs of triangles that share the specified Material ID in the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    material_id (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    triangle_id_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_Materials.get_triangle_material_id"></a>

#### get_triangle_material_id

```python
@classmethod
def get_triangle_material_id(cls, target_mesh: DynamicMesh,
                             triangle_id: int) -> Tuple[int, bool]
```

X.get_triangle_material_id(target_mesh, triangle_id) -> (int32, is_valid_triangle=bool)
Returns the current Material ID for a Triangle.
If the mesh does not have Material IDs enabled or if the Triangle ID is not an element of the mesh, the value 0 will be returned and bIsValidTriangle will be false.

Args:
    target_mesh (DynamicMesh): 
    triangle_id (int32): 

Returns:
    bool: 

    is_valid_triangle (bool):

<a id="unreal.GeometryScript_Materials.get_max_material_id"></a>

#### get_max_material_id

```python
@classmethod
def get_max_material_id(cls, target_mesh: DynamicMesh) -> Tuple[int, bool]
```

X.get_max_material_id(target_mesh) -> (int32, has_material_i_ds=bool)
Get Max Material ID

Args:
    target_mesh (DynamicMesh): 

Returns:
    bool: 

    has_material_i_ds (bool):

<a id="unreal.GeometryScript_Materials.get_material_i_ds_of_triangles"></a>

#### get_material_i_ds_of_triangles

```python
@classmethod
def get_material_i_ds_of_triangles(
    cls,
    target_mesh: DynamicMesh,
    triangle_id_list: GeometryScriptIndexList,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptIndexList]
```

X.get_material_i_ds_of_triangles(target_mesh, triangle_id_list, debug=None) -> (DynamicMesh, material_id_list=GeometryScriptIndexList)
This populates the MaterialIDList with Material IDs for each triangle in the TriangleIDList.
If a triangle is not present in the Target Mesh the number -1 will be used for the corresponding Material ID.
If Material IDs are not enabled on the TargetMesh no Material IDs will be added to the result list.

Args:
    target_mesh (DynamicMesh): 
    triangle_id_list (GeometryScriptIndexList): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptIndexList: 

    material_id_list (GeometryScriptIndexList):

<a id="unreal.GeometryScript_Materials.get_all_triangle_material_i_ds"></a>

#### get_all_triangle_material_i_ds

```python
@classmethod
def get_all_triangle_material_i_ds(
    cls, target_mesh: DynamicMesh
) -> Tuple[DynamicMesh, GeometryScriptIndexList, bool]
```

X.get_all_triangle_material_i_ds(target_mesh) -> (DynamicMesh, material_id_list=GeometryScriptIndexList, has_material_i_ds=bool)
Returns an Index List of all triangle Material IDs, constructed with one entry for each consecutive Triangle ID.
If Material IDs are not enabled on the mesh, bHasMaterialsIDs will be set to false on return and nothing will be added to the Material ID List.
warning: if the mesh is not Triangle-Compact (eg GetHasTriangleIDGaps == false) then the returned list will also have the same gaps where the number -1 will be recorded for any missing Triangle IDs.

Args:
    target_mesh (DynamicMesh): 

Returns:
    tuple: 

    material_id_list (GeometryScriptIndexList): 

    has_material_i_ds (bool):

<a id="unreal.GeometryScript_Materials.enable_material_i_ds"></a>

#### enable_material_i_ds

```python
@classmethod
def enable_material_i_ds(cls,
                         target_mesh: DynamicMesh,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.enable_material_i_ds(target_mesh, debug=None) -> DynamicMesh
Enables per-triangle Material IDs on a mesh and initializes the values to 0.
If Target Mesh already has Material IDs, this function will do nothing.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Materials.delete_triangles_by_material_id"></a>

#### delete_triangles_by_material_id

```python
@classmethod
def delete_triangles_by_material_id(
        cls,
        target_mesh: DynamicMesh,
        material_id: int,
        defer_change_notifications: bool = False,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, int]
```

X.delete_triangles_by_material_id(target_mesh, material_id, defer_change_notifications=False, debug=None) -> (DynamicMesh, num_deleted=int32)
Delete all triangles in TargetMesh with the given MaterialID

Args:
    target_mesh (DynamicMesh): 
    material_id (int32): 
    defer_change_notifications (bool): 
    debug (GeometryScriptDebug): 

Returns:
    int32: 

    num_deleted (int32): number of deleted triangles is returned here

<a id="unreal.GeometryScript_Materials.compact_material_i_ds"></a>

#### compact_material_i_ds

```python
@classmethod
def compact_material_i_ds(
    cls,
    target_mesh: DynamicMesh,
    source_material_list: Array[MaterialInterface],
    remove_duplicate_materials: bool = False,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[MaterialInterface]]
```

X.compact_material_i_ds(target_mesh, source_material_list, remove_duplicate_materials=False, debug=None) -> (DynamicMesh, compacted_material_list=Array[MaterialInterface])
Compact the MaterialIDs of the TargetMesh, ie remove any un-used MaterialIDs and remap the remaining
N in-use MaterialIDs to the range [0,N-1]. Optionally compute a Compacted list of Materials.

Args:
    target_mesh (DynamicMesh): 
    source_material_list (Array[MaterialInterface]): Input Material list, assumption is that SourceMaterialList.Num() == number of MaterialIDs on mesh at input
    remove_duplicate_materials (bool): Whether to also remove duplicate materials from the compacted list
    debug (GeometryScriptDebug): 

Returns:
    Array[MaterialInterface]: 

    compacted_material_list (Array[MaterialInterface]): new Compacted Material list, one-to-one with new compacted MaterialIDs

<a id="unreal.GeometryScript_Materials.clear_material_i_ds"></a>

#### clear_material_i_ds

```python
@classmethod
def clear_material_i_ds(cls,
                        target_mesh: DynamicMesh,
                        clear_value: int = 0,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.clear_material_i_ds(target_mesh, clear_value=0, debug=None) -> DynamicMesh
Resets all Material IDs on a mesh to the given ClearValue, or 0 if no ClearValue is provided.
If Material IDs are not already enabled on the Target Mesh, this function will first enable them and then set the value.

Args:
    target_mesh (DynamicMesh): 
    clear_value (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshModeling"></a>