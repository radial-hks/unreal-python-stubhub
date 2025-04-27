## GeometryScript_VertexColors Objects

```python
class GeometryScript_VertexColors(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Vertex Color Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshVertexColorFunctions.h

<a id="unreal.GeometryScript_VertexColors.set_mesh_selection_vertex_color"></a>

#### set_mesh_selection_vertex_color

```python
@classmethod
def set_mesh_selection_vertex_color(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        color: LinearColor,
        flags: GeometryScriptColorFlags,
        create_color_seam: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_selection_vertex_color(target_mesh, selection, color, flags, create_color_seam=False, debug=None) -> DynamicMesh
Set the colors in the TargetMesh VertexColor Overlay identified by the Selection to a constant value.
For a Vertex Selection, each existing VertexColor Overlay Element for the vertex is updated.
For a Triangle or PolyGroup Selection, all Overlay Elements in the identified Triangles are updated.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): 
    color (LinearColor): the constant color to set
    flags (GeometryScriptColorFlags): specify which RGBA channels to set (default all channels)
    create_color_seam (bool): if true, a "hard edge" in the vertex colors is created, by creating new Elements for all the triangles in the selection. If enabled, Vertex selections are converted to Triangle selections, and Flags is ignored.
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_VertexColors.set_mesh_per_vertex_colors"></a>

#### set_mesh_per_vertex_colors

```python
@classmethod
def set_mesh_per_vertex_colors(
        cls,
        target_mesh: DynamicMesh,
        vertex_color_list: GeometryScriptColorList,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_per_vertex_colors(target_mesh, vertex_color_list, debug=None) -> DynamicMesh
Set all vertex colors in the TargetMesh VertexColor Overlay to the specified per-vertex colors

Args:
    target_mesh (DynamicMesh): 
    vertex_color_list (GeometryScriptColorList): per-vertex colors. Size must be less than or equal to the MaxVertexID of TargetMesh  (ie gaps are supported)
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_VertexColors.set_mesh_constant_vertex_color"></a>

#### set_mesh_constant_vertex_color

```python
@classmethod
def set_mesh_constant_vertex_color(
        cls,
        target_mesh: DynamicMesh,
        color: LinearColor,
        flags: GeometryScriptColorFlags,
        clear_existing: bool = False,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.set_mesh_constant_vertex_color(target_mesh, color, flags, clear_existing=False, debug=None) -> DynamicMesh
Set all vertex colors (optionally specific channels) in the TargetMesh VertexColor Overlay to a constant value

Args:
    target_mesh (DynamicMesh): 
    color (LinearColor): the constant color to set
    flags (GeometryScriptColorFlags): specify which RGBA channels to set (default all channels)
    clear_existing (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_VertexColors.get_mesh_per_vertex_colors"></a>

#### get_mesh_per_vertex_colors

```python
@classmethod
def get_mesh_per_vertex_colors(
    cls,
    target_mesh: DynamicMesh,
    blend_split_vertex_values: bool = True
) -> Tuple[DynamicMesh, GeometryScriptColorList, bool, bool]
```

X.get_mesh_per_vertex_colors(target_mesh, blend_split_vertex_values=True) -> (DynamicMesh, color_list=GeometryScriptColorList, is_valid_color_set=bool, has_vertex_id_gaps=bool)
Get a list of single vertex colors for each mesh vertex in the TargetMesh, derived from the VertexColor Overlay.
The VertexColor Overlay may store multiple colors for a single vertex (ie different colors for that vertex on different triangles)
In such cases the colors can either be averaged, or the last color seen will be used, depending on the bBlendSplitVertexValues parameter.

Args:
    target_mesh (DynamicMesh): 
    blend_split_vertex_values (bool): control how multiple colors at the same vertex should be interpreted

Returns:
    tuple: 

    color_list (GeometryScriptColorList): output color list will be stored here. Size will be equal to the MaxVertexID of TargetMesh  (not the VertexCount!)

    is_valid_color_set (bool): will be set to true if the VertexColor Overlay was valid

    has_vertex_id_gaps (bool): will be set to true if some vertex indices in TargetMesh were invalid, ie MaxVertexID > VertexCount

<a id="unreal.GeometryScript_VertexColors.convert_mesh_vertex_colors_srgb_to_linear"></a>

#### convert_mesh_vertex_colors_srgb_to_linear

```python
@classmethod
def convert_mesh_vertex_colors_srgb_to_linear(
        cls,
        target_mesh: DynamicMesh,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.convert_mesh_vertex_colors_srgb_to_linear(target_mesh, debug=None) -> DynamicMesh
Apply a SRGB to Linear color transformation on all vertex colors
on the mesh.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_VertexColors.convert_mesh_vertex_colors_linear_to_srgb"></a>

#### convert_mesh_vertex_colors_linear_to_srgb

```python
@classmethod
def convert_mesh_vertex_colors_linear_to_srgb(
        cls,
        target_mesh: DynamicMesh,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.convert_mesh_vertex_colors_linear_to_srgb(target_mesh, debug=None) -> DynamicMesh
Apply a Linear to SRGB color transformation on all vertex colors
on the mesh.

Args:
    target_mesh (DynamicMesh): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_VertexColors.blur_mesh_vertex_colors"></a>

#### blur_mesh_vertex_colors

```python
@classmethod
def blur_mesh_vertex_colors(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        num_iterations: int = 1,
        strength: float = 0.500000,
        blur_mode: GeometryScriptBlurColorMode = GeometryScriptBlurColorMode.
    UNIFORM,
        options: GeometryScriptBlurMeshVertexColorsOptions = [
            True, True, True, True
        ],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.blur_mesh_vertex_colors(target_mesh, selection, num_iterations=1, strength=0.500000, blur_mode=GeometryScriptBlurColorMode.UNIFORM, options=[True, True, True, True], debug=None) -> DynamicMesh
Blur the color attribute of the mesh. If the mesh has no color attribute, the function returns the mesh unchanged.

Args:
    target_mesh (DynamicMesh): The mesh containing the color attribute.
    selection (GeometryScriptMeshSelection): Only vertices in the selection will have their color attribute blurred.
    num_iterations (int32): The number of blur iterations.
    strength (double): Each iteration, we will blur between the vertex of the color at the previous iteration and its neighbors' average by Strength amount (expected to be in the zero to one range).
    blur_mode (GeometryScriptBlurColorMode): Determines how neighbors are weighted when computing their average.
    options (GeometryScriptBlurMeshVertexColorsOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshVoxelProcessing"></a>