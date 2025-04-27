## GeometryScript_Primitives Objects

```python
class GeometryScript_Primitives(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Primitive Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

<a id="unreal.GeometryScript_Primitives.create_constrained_edges_loop"></a>

#### create_constrained_edges_loop

```python
@classmethod
def create_constrained_edges_loop(cls,
                                  num_vertices: int,
                                  start: int = 0) -> Array[IntPoint]
```

X.create_constrained_edges_loop(num_vertices, start=0) -> Array[IntPoint]
Intended for use with AppendDelaunayTriangulation2D:
Create a loop of edges through sequential vertices
e.g., a Loop(3,0) will construct edges (2,0), (0,1) and (1,2)

Args:
    num_vertices (int32): 
    start (int32): 

Returns:
    Array[IntPoint]:

<a id="unreal.GeometryScript_Primitives.create_constrained_edges_chain"></a>

#### create_constrained_edges_chain

```python
@classmethod
def create_constrained_edges_chain(cls,
                                   num_vertices: int,
                                   start: int = 0) -> Array[IntPoint]
```

X.create_constrained_edges_chain(num_vertices, start=0) -> Array[IntPoint]
Intended for use with AppendDelaunayTriangulation2D:
Create a chain of edges through sequential vertices
e.g., a Chain(3,0) will construct edges (0,1) and (1,2)

Args:
    num_vertices (int32): 
    start (int32): 

Returns:
    Array[IntPoint]:

<a id="unreal.GeometryScript_Primitives.append_voronoi_diagram2d"></a>

#### append_voronoi_diagram2d

```python
@classmethod
def append_voronoi_diagram2d(cls,
                             target_mesh: DynamicMesh,
                             primitive_options: GeometryScriptPrimitiveOptions,
                             transform: Transform,
                             voronoi_sites: Array[Vector2D],
                             voronoi_options: GeometryScriptVoronoiOptions,
                             debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_voronoi_diagram2d(target_mesh, primitive_options, transform, voronoi_sites, voronoi_options, debug=None) -> DynamicMesh
Generates triangulated Voronoi Cells from the provided Voronoi Sites, identifying each with PolyGroups, and appends to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    voronoi_sites (Array[Vector2D]): 
    voronoi_options (GeometryScriptVoronoiOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_triangulated_polygon3d"></a>

#### append_triangulated_polygon3d

```python
@classmethod
def append_triangulated_polygon3d(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices3d: Array[Vector],
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_triangulated_polygon3d(target_mesh, primitive_options, transform, polygon_vertices3d, debug=None) -> DynamicMesh
Appends a Triangulated Polygon (with vertices specified in 3D) to the Target Mesh.
Uses Ear Clipping-based triangulation. Output vertices will always be 1:1 with input vertices.
Polygon endpoint is not repeated.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices3d (Array[Vector]): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_triangulated_polygon"></a>

#### append_triangulated_polygon

```python
@classmethod
def append_triangulated_polygon(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        allow_self_intersections: bool = True,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_triangulated_polygon(target_mesh, primitive_options, transform, polygon_vertices, allow_self_intersections=True, debug=None) -> DynamicMesh
Appends a Triangulated Polygon to the Target Mesh.
Polygon should be oriented counter-clockwise to produce a correctly-oriented shape, otherwise it will be inside-out
Polygon endpoint is not repeated.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    allow_self_intersections (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_torus"></a>

#### append_torus

```python
@classmethod
def append_torus(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        revolve_options: GeometryScriptRevolveOptions,
        major_radius: float = 50.000000,
        minor_radius: float = 25.000000,
        major_steps: int = 16,
        minor_steps: int = 8,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_torus(target_mesh, primitive_options, transform, revolve_options, major_radius=50.000000, minor_radius=25.000000, major_steps=16, minor_steps=8, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D torus (donut) or partial torus to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    revolve_options (GeometryScriptRevolveOptions): 
    major_radius (float): 
    minor_radius (float): 
    major_steps (int32): 
    minor_steps (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_sweep_polyline"></a>

#### append_sweep_polyline

```python
@classmethod
def append_sweep_polyline(cls,
                          target_mesh: DynamicMesh,
                          primitive_options: GeometryScriptPrimitiveOptions,
                          transform: Transform,
                          polyline_vertices: Array[Vector2D],
                          sweep_path: Array[Transform],
                          polyline_tex_param_u: Array[float],
                          sweep_path_tex_param_v: Array[float],
                          loop: bool = False,
                          start_scale: float = 1.000000,
                          end_scale: float = 1.000000,
                          rotation_angle_deg: float = 0.000000,
                          miter_limit: float = 1.000000,
                          debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_sweep_polyline(target_mesh, primitive_options, transform, polyline_vertices, sweep_path, polyline_tex_param_u, sweep_path_tex_param_v, loop=False, start_scale=1.000000, end_scale=1.000000, rotation_angle_deg=0.000000, miter_limit=1.000000, debug=None) -> DynamicMesh
Sweep the given 2D PolylineVertices along the SweepPath specified as a set of FTransforms
If the 2D vertices are (U,V), then in the coordinate space of the FTransform, X points "along" the path,
Y points "right" (U) and Z points "up" (V).

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polyline_vertices (Array[Vector2D]): vertices of the open 2D path that will be swept along the SweepPath
    sweep_path (Array[Transform]): defines the 3D sweep path curve as a 3D poly-path, with rotation and scaling at each polypath vertex taken from the Transform
    polyline_tex_param_u (Array[float]): defines U coordinate value for each element in PolylineVertices. Must be same length as PolylineVertices (ignored if length=0).
    sweep_path_tex_param_v (Array[float]): defines V coordinate value for each element in SweepPath. Must be same length as SweepPath if bLoop=false, length+1 if bLoop=true, and ignored if length=0.
    loop (bool): if true, SweepPath is considered to be a Loop and a section connecting the end and start of the path is added (bCapped is ignored)
    start_scale (float): uniform scaling applied to the 2D polygon at the start of the path. Interpolated via arc length to EndScale at the end of the path.
    end_scale (float): uniform scaling applied to the 2D polygon at the end of the path
    rotation_angle_deg (float): Rotation applied to the 2D Polygon. Positive rotation rotates clockwise, ie Up/+Z/+V towards Right/+Y/+U. This Rotation is applied before any rotation in the SweepPath Transforms.
    miter_limit (float): If > 1, maximum scaling to apply at sharp turns in the curve path to keep the apparent swept profile from shrinking, and sweep path frames will be aligned to the path direction
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_sweep_polygon"></a>

#### append_sweep_polygon

```python
@classmethod
def append_sweep_polygon(cls,
                         target_mesh: DynamicMesh,
                         primitive_options: GeometryScriptPrimitiveOptions,
                         transform: Transform,
                         polygon_vertices: Array[Vector2D],
                         sweep_path: Array[Transform],
                         loop: bool = False,
                         capped: bool = True,
                         start_scale: float = 1.000000,
                         end_scale: float = 1.000000,
                         rotation_angle_deg: float = 0.000000,
                         miter_limit: float = 1.000000,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_sweep_polygon(target_mesh, primitive_options, transform, polygon_vertices, sweep_path, loop=False, capped=True, start_scale=1.000000, end_scale=1.000000, rotation_angle_deg=0.000000, miter_limit=1.000000, debug=None) -> DynamicMesh
Sweep the given 2D PolygonVertices along the SweepPath specified as a set of FTransforms
If the 2D vertices are (U,V), then in the coordinate space of the FTransform, X points "along" the path,
Y points "right" (U) and Z points "up" (V).

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): vertices of the closed 2D polyon that will be swept along the SweepPath
    sweep_path (Array[Transform]): defines the 3D sweep path curve as a 3D poly-path, with rotation and scaling at each polypath vertex taken from the Transform
    loop (bool): if true, SweepPath is considered to be a Loop and a section connecting the end and start of the path is added (bCapped is ignored)
    capped (bool): if true the open ends of the swept generalized cylinder are triangulated
    start_scale (float): uniform scaling applied to the 2D polygon at the start of the path. Interpolated via arc length to EndScale at the end of the path.
    end_scale (float): uniform scaling applied to the 2D polygon at the end of the path
    rotation_angle_deg (float): Rotation applied to the 2D Polygon. Positive rotation rotates clockwise, ie Up/+Z/+V towards Right/+Y/+U. This Rotation is applied before any rotation in the SweepPath Transforms.
    miter_limit (float): If > 1, maximum scaling to apply at sharp turns in the curve path to keep the apparent swept profile from shrinking, and sweep path frames will be aligned to the path direction
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_spiral_revolve_polygon"></a>

#### append_spiral_revolve_polygon

```python
@classmethod
def append_spiral_revolve_polygon(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        revolve_options: GeometryScriptRevolveOptions,
        radius: float = 100.000000,
        steps: int = 18,
        rise_per_revolution: float = 50.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_spiral_revolve_polygon(target_mesh, primitive_options, transform, polygon_vertices, revolve_options, radius=100.000000, steps=18, rise_per_revolution=50.000000, debug=None) -> DynamicMesh
Revolves a 2D polygon on a helical path, like one used to create a vertical spiral, appending the result to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    revolve_options (GeometryScriptRevolveOptions): 
    radius (float): 
    steps (int32): 
    rise_per_revolution (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_sphere_lat_long_with_collision"></a>

#### append_sphere_lat_long_with_collision

```python
@classmethod
def append_sphere_lat_long_with_collision(
    cls,
    target_mesh: DynamicMesh,
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    radius: float = 50.000000,
    steps_phi: int = 10,
    steps_theta: int = 16,
    origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode
    .CENTER,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

X.append_sphere_lat_long_with_collision(target_mesh, primitive_options, transform, radius=50.000000, steps_phi=10, steps_theta=16, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D Sphere triangulated using latitude/longitude topology to the Target Mesh.
Also creates matching simple collision. Note: If transform has non-uniform scale, collision shape will be a uniform-scale approximation
matching the behavior of the physics system -- specifically, it will scale the sphere radius by the smallest axis scale.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_phi (int32): 
    steps_theta (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Primitives.append_sphere_lat_long"></a>

#### append_sphere_lat_long

```python
@classmethod
def append_sphere_lat_long(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 50.000000,
        steps_phi: int = 10,
        steps_theta: int = 16,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.
    CENTER,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_sphere_lat_long(target_mesh, primitive_options, transform, radius=50.000000, steps_phi=10, steps_theta=16, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> DynamicMesh
Appends a 3D Sphere triangulated using latitude/longitude topology to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_phi (int32): 
    steps_theta (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_sphere_covering"></a>

#### append_sphere_covering

```python
@classmethod
def append_sphere_covering(cls,
                           target_mesh: DynamicMesh,
                           primitive_options: GeometryScriptPrimitiveOptions,
                           transform: Transform,
                           sphere_covering: GeometryScriptSphereCovering,
                           steps_x: int = 6,
                           steps_y: int = 6,
                           steps_z: int = 6,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_sphere_covering(target_mesh, primitive_options, transform, sphere_covering, steps_x=6, steps_y=6, steps_z=6, debug=None) -> DynamicMesh
Appends the spheres in the Sphere Covering to the Target Mesh

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    sphere_covering (GeometryScriptSphereCovering): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_sphere_box_with_collision"></a>

#### append_sphere_box_with_collision

```python
@classmethod
def append_sphere_box_with_collision(
    cls,
    target_mesh: DynamicMesh,
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    radius: float = 50.000000,
    steps_x: int = 6,
    steps_y: int = 6,
    steps_z: int = 6,
    origin: GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode
    .CENTER,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

X.append_sphere_box_with_collision(target_mesh, primitive_options, transform, radius=50.000000, steps_x=6, steps_y=6, steps_z=6, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D sphere triangulated using box topology to the Target Mesh.
Also creates matching simple collision. Note: If transform has non-uniform scale, collision shape will be a uniform-scale approximation
matching the behavior of the physics system -- specifically, it will scale the sphere radius by the smallest axis scale.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Primitives.append_sphere_box"></a>

#### append_sphere_box

```python
@classmethod
def append_sphere_box(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 50.000000,
        steps_x: int = 6,
        steps_y: int = 6,
        steps_z: int = 6,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.
    CENTER,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_sphere_box(target_mesh, primitive_options, transform, radius=50.000000, steps_x=6, steps_y=6, steps_z=6, origin=GeometryScriptPrimitiveOriginMode.CENTER, debug=None) -> DynamicMesh
Appends a 3D sphere triangulated using box topology to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_simple_swept_polygon"></a>

#### append_simple_swept_polygon

```python
@classmethod
def append_simple_swept_polygon(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        sweep_path: Array[Vector],
        loop: bool = False,
        capped: bool = True,
        start_scale: float = 1.000000,
        end_scale: float = 1.000000,
        rotation_angle_deg: float = 0.000000,
        miter_limit: float = 1.000000,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_simple_swept_polygon(target_mesh, primitive_options, transform, polygon_vertices, sweep_path, loop=False, capped=True, start_scale=1.000000, end_scale=1.000000, rotation_angle_deg=0.000000, miter_limit=1.000000, debug=None) -> DynamicMesh
Sweeps a 2D polygon along an arbitrary 3D path, appending the result to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): vertices of the closed 2D polyon that will be swept along the SweepPath
    sweep_path (Array[Vector]): defines the 3D sweep path curve
    loop (bool): if true, SweepPath is considered to be a Loop and a section connecting the end and start of the path is added (bCapped is ignored)
    capped (bool): if true the open ends of the swept generalized cylinder are triangulated
    start_scale (float): uniform scaling applied to the 2D polygon at the start of the path. Interpolated via arc length to EndScale at the end of the path.
    end_scale (float): uniform scaling applied to the 2D polygon at the end of the path
    rotation_angle_deg (float): Rotation applied to the 2D Polygon. Positive rotation rotates clockwise, ie Up/+Z/+V towards Right/+Y/+U
    miter_limit (float): If > 1, maximum scaling to apply at sharp turns in the curve path to keep the apparent swept profile from shrinking
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_simple_extrude_polygon"></a>

#### append_simple_extrude_polygon

```python
@classmethod
def append_simple_extrude_polygon(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_vertices: Array[Vector2D],
        height: float = 100.000000,
        height_steps: int = 0,
        capped: bool = True,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_simple_extrude_polygon(target_mesh, primitive_options, transform, polygon_vertices, height=100.000000, height_steps=0, capped=True, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Polygon should be oriented counter-clockwise to produce a correctly-oriented shape, otherwise it will be inside-out
Polygon endpoint is not repeated.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    height (float): 
    height_steps (int32): 
    capped (bool): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_simple_collision_shapes"></a>

#### append_simple_collision_shapes

```python
@classmethod
def append_simple_collision_shapes(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        simple_collision: GeometryScriptSimpleCollision,
        triangulation_options:
    GeometryScriptSimpleCollisionTriangulationOptions,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_simple_collision_shapes(target_mesh, primitive_options, transform, simple_collision, triangulation_options, debug=None) -> DynamicMesh
Appends Simple Collision shapes to the Target Mesh, triangulated as specified by Triangulation Options

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): Transform to be applied to simple collision shapes, following the method by which simple collision shapes are transformed -- so, e.g., spheres will not be non-uniformly scaled
    simple_collision (GeometryScriptSimpleCollision): 
    triangulation_options (GeometryScriptSimpleCollisionTriangulationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_round_rectangle_xy"></a>

#### append_round_rectangle_xy

```python
@classmethod
def append_round_rectangle_xy(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        corner_radius: float = 5.000000,
        steps_width: int = 0,
        steps_height: int = 0,
        steps_round: int = 4,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_round_rectangle_xy(target_mesh, primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, corner_radius=5.000000, steps_width=0, steps_height=0, steps_round=4, debug=None) -> DynamicMesh
Appends a planar Rectangle with Rounded Corners (RoundRect) to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    corner_radius (float): 
    steps_width (int32): 
    steps_height (int32): 
    steps_round (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_round_rectangle_compatibility_5_0"></a>

#### append_round_rectangle_compatibility_5_0

```python
@classmethod
def append_round_rectangle_compatibility_5_0(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        corner_radius: float = 5.000000,
        steps_width: int = 0,
        steps_height: int = 0,
        steps_round: int = 4,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_round_rectangle_compatibility_5_0(target_mesh, primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, corner_radius=5.000000, steps_width=0, steps_height=0, steps_round=4, debug=None) -> DynamicMesh
5.0 Preview 1 Compatibility version of AppendRoundRectangleXY.
Incorrectly divides the input DimensionX and DimensionY by 2.
warning: It is strongly recommended that callers of this function update to the current AppendRoundRectangleXY function!

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    corner_radius (float): 
    steps_width (int32): 
    steps_height (int32): 
    steps_round (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_round_rectangle"></a>

#### append_round_rectangle

```python
@classmethod
def append_round_rectangle(cls,
                           target_mesh: DynamicMesh,
                           primitive_options: GeometryScriptPrimitiveOptions,
                           transform: Transform,
                           dimension_x: float = 100.000000,
                           dimension_y: float = 100.000000,
                           corner_radius: float = 5.000000,
                           steps_width: int = 0,
                           steps_height: int = 0,
                           steps_round: int = 4,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

deprecated: 'append_round_rectangle' was renamed to 'append_round_rectangle_compatibility_5_0'.

<a id="unreal.GeometryScript_Primitives.append_revolve_polygon"></a>

#### append_revolve_polygon

```python
@classmethod
def append_revolve_polygon(cls,
                           target_mesh: DynamicMesh,
                           primitive_options: GeometryScriptPrimitiveOptions,
                           transform: Transform,
                           polygon_vertices: Array[Vector2D],
                           revolve_options: GeometryScriptRevolveOptions,
                           radius: float = 100.000000,
                           steps: int = 8,
                           debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_revolve_polygon(target_mesh, primitive_options, transform, polygon_vertices, revolve_options, radius=100.000000, steps=8, debug=None) -> DynamicMesh
In the coordinate system of the revolve polygon, +X is towards the "outside" of the revolve donut, and +Y is "up" (ie +Z in local space)
Polygon should be oriented counter-clockwise to produce a correctly-oriented shape, otherwise it will be inside-out
Polygon endpoint is not repeated.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_vertices (Array[Vector2D]): 
    revolve_options (GeometryScriptRevolveOptions): 
    radius (float): 
    steps (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_revolve_path"></a>

#### append_revolve_path

```python
@classmethod
def append_revolve_path(cls,
                        target_mesh: DynamicMesh,
                        primitive_options: GeometryScriptPrimitiveOptions,
                        transform: Transform,
                        path_vertices: Array[Vector2D],
                        revolve_options: GeometryScriptRevolveOptions,
                        steps: int = 8,
                        capped: bool = True,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_revolve_path(target_mesh, primitive_options, transform, path_vertices, revolve_options, steps=8, capped=True, debug=None) -> DynamicMesh
Revolves an open 2D path, with optional top and bottom end caps, appending the result to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    path_vertices (Array[Vector2D]): 
    revolve_options (GeometryScriptRevolveOptions): 
    steps (int32): 
    capped (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_rectangle_xy"></a>

#### append_rectangle_xy

```python
@classmethod
def append_rectangle_xy(cls,
                        target_mesh: DynamicMesh,
                        primitive_options: GeometryScriptPrimitiveOptions,
                        transform: Transform,
                        dimension_x: float = 100.000000,
                        dimension_y: float = 100.000000,
                        steps_width: int = 0,
                        steps_height: int = 0,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_rectangle_xy(target_mesh, primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, steps_width=0, steps_height=0, debug=None) -> DynamicMesh
Appends a planar Rectangle to a Dynamic Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    steps_width (int32): 
    steps_height (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_rectangle_compatibility_5_0"></a>

#### append_rectangle_compatibility_5_0

```python
@classmethod
def append_rectangle_compatibility_5_0(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        steps_width: int = 0,
        steps_height: int = 0,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_rectangle_compatibility_5_0(target_mesh, primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, steps_width=0, steps_height=0, debug=None) -> DynamicMesh
5.0 Preview 1 Compatibility version of AppendRectangleXY. Incorrectly interprets the input dimensions.
Incorrectly divides the input DimensionX and DimensionY by 2.
warning: It is strongly recommended that callers of this function update to the current AppendRectangleXY function!

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    steps_width (int32): 
    steps_height (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_rectangle"></a>

#### append_rectangle

```python
@classmethod
def append_rectangle(cls,
                     target_mesh: DynamicMesh,
                     primitive_options: GeometryScriptPrimitiveOptions,
                     transform: Transform,
                     dimension_x: float = 100.000000,
                     dimension_y: float = 100.000000,
                     steps_width: int = 0,
                     steps_height: int = 0,
                     debug: GeometryScriptDebug = None) -> DynamicMesh
```

deprecated: 'append_rectangle' was renamed to 'append_rectangle_compatibility_5_0'.

<a id="unreal.GeometryScript_Primitives.append_polygon_list_triangulation"></a>

#### append_polygon_list_triangulation

```python
@classmethod
def append_polygon_list_triangulation(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        polygon_list: GeometryScriptGeneralPolygonList,
        triangulation_options: GeometryScriptPolygonsTriangulationOptions,
        debug: GeometryScriptDebug = None) -> Tuple[DynamicMesh, bool]
```

X.append_polygon_list_triangulation(target_mesh, primitive_options, transform, polygon_list, triangulation_options, debug=None) -> (DynamicMesh, triangulation_error=bool)
Generates a Delaunay Triangulation of the provided Polygon List, and appends it to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    polygon_list (GeometryScriptGeneralPolygonList): 
    triangulation_options (GeometryScriptPolygonsTriangulationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    triangulation_error (bool): Reports whether the triangulation contains errors, typically due to intersecting edges in the input. Consider pre-processing the PolygonsList with PolygonsUnion to resolve intersections and prevent this error.

<a id="unreal.GeometryScript_Primitives.append_linear_stairs"></a>

#### append_linear_stairs

```python
@classmethod
def append_linear_stairs(cls,
                         target_mesh: DynamicMesh,
                         primitive_options: GeometryScriptPrimitiveOptions,
                         transform: Transform,
                         step_width: float = 100.000000,
                         step_height: float = 20.000000,
                         step_depth: float = 30.000000,
                         num_steps: int = 8,
                         floating: bool = False,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_linear_stairs(target_mesh, primitive_options, transform, step_width=100.000000, step_height=20.000000, step_depth=30.000000, num_steps=8, floating=False, debug=None) -> DynamicMesh
Appends a linear staircase to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    step_width (float): 
    step_height (float): 
    step_depth (float): 
    num_steps (int32): 
    floating (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_disc"></a>

#### append_disc

```python
@classmethod
def append_disc(cls,
                target_mesh: DynamicMesh,
                primitive_options: GeometryScriptPrimitiveOptions,
                transform: Transform,
                radius: float = 50.000000,
                angle_steps: int = 16,
                spoke_steps: int = 0,
                start_angle: float = 0.000000,
                end_angle: float = 360.000000,
                hole_radius: float = 0.000000,
                debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_disc(target_mesh, primitive_options, transform, radius=50.000000, angle_steps=16, spoke_steps=0, start_angle=0.000000, end_angle=360.000000, hole_radius=0.000000, debug=None) -> DynamicMesh
Appends a planar disc to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    angle_steps (int32): 
    spoke_steps (int32): 
    start_angle (float): 
    end_angle (float): 
    hole_radius (float): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_delaunay_triangulation2d"></a>

#### append_delaunay_triangulation2d

```python
@classmethod
def append_delaunay_triangulation2d(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        vertex_positions: Array[Vector2D],
        constrained_edges: Array[IntPoint],
        triangulation_options:
    GeometryScriptConstrainedDelaunayTriangulationOptions,
        debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[int], bool]
```

X.append_delaunay_triangulation2d(target_mesh, primitive_options, transform, vertex_positions, constrained_edges, triangulation_options, debug=None) -> (DynamicMesh, positions_to_vertex_i_ds=Array[int32], has_duplicate_vertices=bool)
Generates a Delaunay Triangulation of the provided vertices, and appends it to the Target Mesh.
If optional Constrained Edges are provided, will generate a Constrained Delaunay Triangulation which connects the specified vertices with edges.
On success, all vertices are always appended to the output mesh, though duplicate vertices will not be used in any triangles and may optionally be removed.
Use PositionsToVertexIDs to map indices in the input VertexPositions array to vertex IDs in the Dynamic Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    vertex_positions (Array[Vector2D]): 
    constrained_edges (Array[IntPoint]): 
    triangulation_options (GeometryScriptConstrainedDelaunayTriangulationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    positions_to_vertex_i_ds (Array[int32]): 

    has_duplicate_vertices (bool):

<a id="unreal.GeometryScript_Primitives.append_cylinder"></a>

#### append_cylinder

```python
@classmethod
def append_cylinder(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 50.000000,
        height: float = 100.000000,
        radial_steps: int = 12,
        height_steps: int = 0,
        capped: bool = True,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_cylinder(target_mesh, primitive_options, transform, radius=50.000000, height=100.000000, radial_steps=12, height_steps=0, capped=True, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D Cylinder (with optional end caps) to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    height (float): 
    radial_steps (int32): 
    height_steps (int32): 
    capped (bool): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_curved_stairs"></a>

#### append_curved_stairs

```python
@classmethod
def append_curved_stairs(cls,
                         target_mesh: DynamicMesh,
                         primitive_options: GeometryScriptPrimitiveOptions,
                         transform: Transform,
                         step_width: float = 100.000000,
                         step_height: float = 20.000000,
                         inner_radius: float = 150.000000,
                         curve_angle: float = 90.000000,
                         num_steps: int = 8,
                         floating: bool = False,
                         debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_curved_stairs(target_mesh, primitive_options, transform, step_width=100.000000, step_height=20.000000, inner_radius=150.000000, curve_angle=90.000000, num_steps=8, floating=False, debug=None) -> DynamicMesh
Appends a rising circular staircase to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    step_width (float): 
    step_height (float): 
    inner_radius (float): 
    curve_angle (float): 
    num_steps (int32): 
    floating (bool): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_cone"></a>

#### append_cone

```python
@classmethod
def append_cone(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        base_radius: float = 50.000000,
        top_radius: float = 5.000000,
        height: float = 100.000000,
        radial_steps: int = 12,
        height_steps: int = 4,
        capped: bool = True,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_cone(target_mesh, primitive_options, transform, base_radius=50.000000, top_radius=5.000000, height=100.000000, radial_steps=12, height_steps=4, capped=True, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D cone to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    base_radius (float): 
    top_radius (float): 
    height (float): 
    radial_steps (int32): 
    height_steps (int32): 
    capped (bool): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_capsule_with_collision"></a>

#### append_capsule_with_collision

```python
@classmethod
def append_capsule_with_collision(
    cls,
    target_mesh: DynamicMesh,
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    radius: float = 30.000000,
    line_length: float = 75.000000,
    hemisphere_steps: int = 5,
    circle_steps: int = 8,
    segment_steps: int = 0,
    origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

X.append_capsule_with_collision(target_mesh, primitive_options, transform, radius=30.000000, line_length=75.000000, hemisphere_steps=5, circle_steps=8, segment_steps=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D Capsule to the Target Mesh.
Also creates matching simple collision. Note: If transform has non-uniform scale, collision shape will be a uniform-scale approximation
matching the behavior of the physics system -- specifically, it will scale the radius by the larger of the X, Y axis scales, and the length by the Z axis scale

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    line_length (float): 
    hemisphere_steps (int32): 
    circle_steps (int32): 
    segment_steps (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Primitives.append_capsule"></a>

#### append_capsule

```python
@classmethod
def append_capsule(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        radius: float = 30.000000,
        line_length: float = 75.000000,
        hemisphere_steps: int = 5,
        circle_steps: int = 8,
        segment_steps: int = 0,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_capsule(target_mesh, primitive_options, transform, radius=30.000000, line_length=75.000000, hemisphere_steps=5, circle_steps=8, segment_steps=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D Capsule to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    radius (float): 
    line_length (float): 
    hemisphere_steps (int32): 
    circle_steps (int32): 
    segment_steps (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_box_with_collision"></a>

#### append_box_with_collision

```python
@classmethod
def append_box_with_collision(
    cls,
    target_mesh: DynamicMesh,
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    dimension_x: float = 100.000000,
    dimension_y: float = 100.000000,
    dimension_z: float = 100.000000,
    steps_x: int = 0,
    steps_y: int = 0,
    steps_z: int = 0,
    origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

X.append_box_with_collision(target_mesh, primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, dimension_z=100.000000, steps_x=0, steps_y=0, steps_z=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D box to the Target Mesh
Also creates matching simple collision

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    dimension_z (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Primitives.append_box"></a>

#### append_box

```python
@classmethod
def append_box(
        cls,
        target_mesh: DynamicMesh,
        primitive_options: GeometryScriptPrimitiveOptions,
        transform: Transform,
        dimension_x: float = 100.000000,
        dimension_y: float = 100.000000,
        dimension_z: float = 100.000000,
        steps_x: int = 0,
        steps_y: int = 0,
        steps_z: int = 0,
        origin:
    GeometryScriptPrimitiveOriginMode = GeometryScriptPrimitiveOriginMode.BASE,
        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_box(target_mesh, primitive_options, transform, dimension_x=100.000000, dimension_y=100.000000, dimension_z=100.000000, steps_x=0, steps_y=0, steps_z=0, origin=GeometryScriptPrimitiveOriginMode.BASE, debug=None) -> DynamicMesh
Appends a 3D box to the Target Mesh.

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    dimension_x (float): 
    dimension_y (float): 
    dimension_z (float): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    origin (GeometryScriptPrimitiveOriginMode): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_Primitives.append_bounding_box_with_collision"></a>

#### append_bounding_box_with_collision

```python
@classmethod
def append_bounding_box_with_collision(
    cls,
    target_mesh: DynamicMesh,
    primitive_options: GeometryScriptPrimitiveOptions,
    transform: Transform,
    box: Box,
    steps_x: int = 0,
    steps_y: int = 0,
    steps_z: int = 0,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, GeometryScriptSimpleCollision]
```

X.append_bounding_box_with_collision(target_mesh, primitive_options, transform, box, steps_x=0, steps_y=0, steps_z=0, debug=None) -> (DynamicMesh, simple_collision=GeometryScriptSimpleCollision)
Appends a 3D box to the Target Mesh with dimensions and origin taken from the input Box
Also creates matching simple collision

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    box (Box): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    debug (GeometryScriptDebug): 

Returns:
    GeometryScriptSimpleCollision: 

    simple_collision (GeometryScriptSimpleCollision):

<a id="unreal.GeometryScript_Primitives.append_bounding_box"></a>

#### append_bounding_box

```python
@classmethod
def append_bounding_box(cls,
                        target_mesh: DynamicMesh,
                        primitive_options: GeometryScriptPrimitiveOptions,
                        transform: Transform,
                        box: Box,
                        steps_x: int = 0,
                        steps_y: int = 0,
                        steps_z: int = 0,
                        debug: GeometryScriptDebug = None) -> DynamicMesh
```

X.append_bounding_box(target_mesh, primitive_options, transform, box, steps_x=0, steps_y=0, steps_z=0, debug=None) -> DynamicMesh
Appends a 3D box to the Target Mesh with dimensions and origin taken from the input Box

Args:
    target_mesh (DynamicMesh): 
    primitive_options (GeometryScriptPrimitiveOptions): 
    transform (Transform): 
    box (Box): 
    steps_x (int32): 
    steps_y (int32): 
    steps_z (int32): 
    debug (GeometryScriptDebug): 

Returns:
    DynamicMesh:

<a id="unreal.GeometryScript_MeshQueries"></a>