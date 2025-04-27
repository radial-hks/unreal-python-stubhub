## GeometryScript_MeshDeformers Objects

```python
class GeometryScript_MeshDeformers(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Deform Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

<a id="unreal.GeometryScript_MeshDeformers.apply_twist_warp_to_mesh"></a>

#### apply_twist_warp_to_mesh

```python
@classmethod
def apply_twist_warp_to_mesh(cls,
                             target_mesh: DynamicMesh,
                             options: GeometryScriptTwistWarpOptions,
                             twist_orientation: Transform,
                             twist_angle: float = 45.000000,
                             twist_extent: float = 50.000000,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_twist_warp_to_mesh(target_mesh, options, twist_orientation, twist_angle=45.000000, twist_extent=50.000000, debug=None) -> DynamicMesh
Applies a twist warp around an axis defined by the Twist Orientation transform.
The extents of the affected region can be controlled by the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptTwistWarpOptions): 
    twist_orientation (Transform): 
    twist_angle (float): 
    twist_extent (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_perlin_noise_to_mesh"></a>

#### apply_perlin_noise_to_mesh

```python
@classmethod
def apply_perlin_noise_to_mesh(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptPerlinNoiseOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_perlin_noise_to_mesh(target_mesh, selection, options, debug=None) -> DynamicMesh
Applies 3D Perlin noise displacement to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be displaced, otherwise the Options' EmptyBehavior will be followed.
    options (GeometryScriptPerlinNoiseOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_math_warp_to_mesh"></a>

#### apply_math_warp_to_mesh

```python
@classmethod
def apply_math_warp_to_mesh(cls,
                            target_mesh: DynamicMesh,
                            warp_orientation: Transform,
                            warp_type: GeometryScriptMathWarpType,
                            options: GeometryScriptMathWarpOptions,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_math_warp_to_mesh(target_mesh, warp_orientation, warp_type, options, debug=None) -> DynamicMesh
Applies various simple math-function-based warps around an axis defined by the Warp Orientation transform,
currently a 1D or 2D sine-wave with arbitrary orientation may be selected by WarpType.

Args:
    target_mesh (DynamicMesh): 
    warp_orientation (Transform): 
    warp_type (GeometryScriptMathWarpType): 
    options (GeometryScriptMathWarpOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_iterative_smoothing_to_mesh"></a>

#### apply_iterative_smoothing_to_mesh

```python
@classmethod
def apply_iterative_smoothing_to_mesh(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptIterativeMeshSmoothingOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_iterative_smoothing_to_mesh(target_mesh, selection, options, debug=None) -> DynamicMesh
Applies a number of iterations of mesh smoothing to a Dynamic Mesh.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be subject to smoothing,  otherwise the Options' EmptyBehavior will be followed.
    options (GeometryScriptIterativeMeshSmoothingOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_flare_warp_to_mesh"></a>

#### apply_flare_warp_to_mesh

```python
@classmethod
def apply_flare_warp_to_mesh(cls,
                             target_mesh: DynamicMesh,
                             options: GeometryScriptFlareWarpOptions,
                             flare_orientation: Transform,
                             flare_percent_x: float = 0.000000,
                             flare_percent_y: float = 0.000000,
                             flare_extent: float = 50.000000,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_flare_warp_to_mesh(target_mesh, options, flare_orientation, flare_percent_x=0.000000, flare_percent_y=0.000000, flare_extent=50.000000, debug=None) -> DynamicMesh
Applies a Flare/Bulge warp around an axis defined by the Flare Orientation transform.
The amount of flare in the perpendicular directions can be controlled by FlarePercentX and FlarePercentY
and the extents of the affected region can be controlled by the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptFlareWarpOptions): 
    flare_orientation (Transform): 
    flare_percent_x (float): 
    flare_percent_y (float): 
    flare_extent (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_displace_from_texture_map"></a>

#### apply_displace_from_texture_map

```python
@classmethod
def apply_displace_from_texture_map(
        cls,
        target_mesh: DynamicMesh,
        texture: Texture2D,
        selection: GeometryScriptMeshSelection,
        options: GeometryScriptDisplaceFromTextureOptions,
        uv_layer: int = 0,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_displace_from_texture_map(target_mesh, texture, selection, options, uv_layer=0, debug=None) -> DynamicMesh
Applies a displacement to a Dynamic Mesh based on a Texture2D and a UV Channel.

Args:
    target_mesh (DynamicMesh): 
    texture (Texture2D): 
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be subject to displacement,  otherwise the Options' EmptyBehavior will be followed.
    options (GeometryScriptDisplaceFromTextureOptions): 
    uv_layer (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_displace_from_per_vertex_vectors"></a>

#### apply_displace_from_per_vertex_vectors

```python
@classmethod
def apply_displace_from_per_vertex_vectors(
        cls,
        target_mesh: DynamicMesh,
        selection: GeometryScriptMeshSelection,
        vector_list: GeometryScriptVectorList,
        magnitude: float = 5.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_displace_from_per_vertex_vectors(target_mesh, selection, vector_list, magnitude=5.000000, debug=None) -> DynamicMesh
Add the vectors in VectorList, scaled by Magnitude, to the vertex positions in Target Mesh.
VectorList Length must be >= the MaxVertexID of the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    selection (GeometryScriptMeshSelection): if non-empty, only the vertices identified by the selection will be displaced. The VectorList must still be the same size as the whole mesh, this is just a filter on which vertices are updated.
    vector_list (GeometryScriptVectorList): 
    magnitude (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshDeformers.apply_bend_warp_to_mesh"></a>

#### apply_bend_warp_to_mesh

```python
@classmethod
def apply_bend_warp_to_mesh(cls,
                            target_mesh: DynamicMesh,
                            options: GeometryScriptBendWarpOptions,
                            bend_orientation: Transform,
                            bend_angle: float = 45.000000,
                            bend_extent: float = 50.000000,
                            debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.apply_bend_warp_to_mesh(target_mesh, options, bend_orientation, bend_angle=45.000000, bend_extent=50.000000, debug=None) -> DynamicMesh
Applies a Bend Warp around an axis defined by the Bend Orientation transform.
The extents of the affected region can be controlled by the Options.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptBendWarpOptions): 
    bend_orientation (Transform): 
    bend_angle (float): 
    bend_extent (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshGeodesic"></a>