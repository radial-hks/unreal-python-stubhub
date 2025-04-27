## GeometryScript_PolyPath Objects

```python
class GeometryScript_PolyPath(BlueprintFunctionLibrary)
```

Geometry Script Library Poly Path Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolyPathFunctions.h

<a id="unreal.GeometryScript_PolyPath.sample_spline_to_transforms"></a>

#### sample_spline_to_transforms

```python
@classmethod
def sample_spline_to_transforms(
    cls,
    spline: SplineComponent,
    sampling_options: GeometryScriptSplineSamplingOptions,
    relative_transform: Transform,
    include_scale: bool = True
) -> Optional[Tuple[Array[Transform], Array[float]]]
```

X.sample_spline_to_transforms(spline, sampling_options, relative_transform, include_scale=True) -> (frames=Array[Transform], frame_times=Array[double]) or None
Sample a USplineComponent into a list of FTransforms, based on the given SamplingOptions.

Args:
    spline (SplineComponent): 
    sampling_options (GeometryScriptSplineSamplingOptions): 
    relative_transform (Transform): a constant Transform applied to each sample Transform in its local frame of reference. So, eg, an X Rotation will rotate each frame around the local spline Tangent vector
    include_scale (bool): if true, the Scale of each FTransform is taken from the Spline, otherwise the Transforms have unit scale

Returns:
    tuple or None: whether the FrameTimes are w.r.t. a 'constant speed' traversal of the spline

    frames (Array[Transform]): Transforms are returned here, with X axis oriented along spline Tangent and Z as the 'Up' vector.

    frame_times (Array[double]): the spline Time value used for each Frame. Note the Times Use Constant Velocity output indicates whether these times are w.r.t. to a constant-speed parameterization of the spline.

<a id="unreal.GeometryScript_PolyPath.get_poly_path_vertex"></a>

#### get_poly_path_vertex

```python
@classmethod
def get_poly_path_vertex(cls, poly_path: GeometryScriptPolyPath,
                         index: int) -> Tuple[Vector, bool]
```

X.get_poly_path_vertex(poly_path, index) -> (Vector, is_valid_index=bool)
Returns the 3D position of the requested vertex in the PolyPath.
If the Index does not correspond to a vertex in the PolyPath, a Zero Vector (0,0,0) will be returned.

Args:
    poly_path (GeometryScriptPolyPath): 
    index (int32): specifies a vertex in the PolyPath.

Returns:
    bool: 

    is_valid_index (bool): will be false on return if the Index is not included in the PolyPath.

<a id="unreal.GeometryScript_PolyPath.get_poly_path_tangent"></a>

#### get_poly_path_tangent

```python
@classmethod
def get_poly_path_tangent(cls, poly_path: GeometryScriptPolyPath,
                          index: int) -> Tuple[Vector, bool]
```

X.get_poly_path_tangent(poly_path, index) -> (Vector, is_valid_index=bool)
Returns the local tangent vector of the PolyPath at the specified vertex index.
If the Index does not correspond to a vertex in the PolyPath, a Zero Vector (0,0,0) will be returned.

Args:
    poly_path (GeometryScriptPolyPath): 
    index (int32): specifies a vertex in the PolyPath

Returns:
    bool: 

    is_valid_index (bool): will be false on return if the Index is not included in the PolyPath

<a id="unreal.GeometryScript_PolyPath.get_poly_path_num_vertices"></a>

#### get_poly_path_num_vertices

```python
@classmethod
def get_poly_path_num_vertices(cls, poly_path: GeometryScriptPolyPath) -> int
```

X.get_poly_path_num_vertices(poly_path) -> int32
Returns the number of vertices in the the PolyPath.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    int32:

<a id="unreal.GeometryScript_PolyPath.get_poly_path_last_index"></a>

#### get_poly_path_last_index

```python
@classmethod
def get_poly_path_last_index(cls, poly_path: GeometryScriptPolyPath) -> int
```

X.get_poly_path_last_index(poly_path) -> int32
Returns the index of the last vertex in the PolyPath.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    int32:

<a id="unreal.GeometryScript_PolyPath.get_poly_path_arc_length"></a>

#### get_poly_path_arc_length

```python
@classmethod
def get_poly_path_arc_length(cls, poly_path: GeometryScriptPolyPath) -> float
```

X.get_poly_path_arc_length(poly_path) -> double
Returns the length of the PolyPath.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    double:

<a id="unreal.GeometryScript_PolyPath.get_nearest_vertex_index"></a>

#### get_nearest_vertex_index

```python
@classmethod
def get_nearest_vertex_index(cls, poly_path: GeometryScriptPolyPath,
                             point: Vector) -> int
```

X.get_nearest_vertex_index(poly_path, point) -> int32
Find the index of the vertex closest to a given point.  Returns -1 if the PolyPath has no vertices.

Args:
    poly_path (GeometryScriptPolyPath): 
    point (Vector): 

Returns:
    int32:

<a id="unreal.GeometryScript_PolyPath.flatten_to2d_on_axis"></a>

#### flatten_to2d_on_axis

```python
@classmethod
def flatten_to2d_on_axis(
    cls,
    poly_path: GeometryScriptPolyPath,
    drop_axis: GeometryScriptAxis = GeometryScriptAxis.Z
) -> GeometryScriptPolyPath
```

X.flatten_to2d_on_axis(poly_path, drop_axis=GeometryScriptAxis.Z) -> GeometryScriptPolyPath
Create a 2D, flattened copy of the path by dropping the given axis, and using the other two coordinates as the new X, Y coordinates.

Args:
    poly_path (GeometryScriptPolyPath): 
    drop_axis (GeometryScriptAxis): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_PolyPath.create_circle_path3d"></a>

#### create_circle_path3d

```python
@classmethod
def create_circle_path3d(cls,
                         transform: Transform,
                         radius: float = 10.000000,
                         num_points: int = 10) -> GeometryScriptPolyPath
```

X.create_circle_path3d(transform, radius=10.000000, num_points=10) -> GeometryScriptPolyPath
Create a closed circle around the origin on the XY plane, then transformed by Transform.
By our convention for closed paths, the end vertex is *not* a duplicate of the start vertex.

Args:
    transform (Transform): 
    radius (float): 
    num_points (int32): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_PolyPath.create_circle_path2d"></a>

#### create_circle_path2d

```python
@classmethod
def create_circle_path2d(cls,
                         center: Vector2D = [0.000000, 0.000000],
                         radius: float = 10.000000,
                         num_points: int = 10) -> GeometryScriptPolyPath
```

X.create_circle_path2d(center=[0.000000, 0.000000], radius=10.000000, num_points=10) -> GeometryScriptPolyPath
Create a closed circle on the XY plane around the given Center.
By our convention for closed paths, the end vertex is *not* a duplicate of the start vertex.

Args:
    center (Vector2D): 
    radius (float): 
    num_points (int32): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_PolyPath.create_arc_path3d"></a>

#### create_arc_path3d

```python
@classmethod
def create_arc_path3d(cls,
                      transform: Transform,
                      radius: float = 10.000000,
                      num_points: int = 10,
                      start_angle: float = 0.000000,
                      end_angle: float = 90.000000) -> GeometryScriptPolyPath
```

X.create_arc_path3d(transform, radius=10.000000, num_points=10, start_angle=0.000000, end_angle=90.000000) -> GeometryScriptPolyPath
Create an open arc around the origin on the XY plane, then transformed by Transform.
As it is an open path, the end vertex exactly hits the target EndAngle (so will be positioned on the start vertex if the end aligns to the start)

Args:
    transform (Transform): 
    radius (float): 
    num_points (int32): 
    start_angle (float): 
    end_angle (float): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_PolyPath.create_arc_path2d"></a>

#### create_arc_path2d

```python
@classmethod
def create_arc_path2d(cls,
                      center: Vector2D = [0.000000, 0.000000],
                      radius: float = 10.000000,
                      num_points: int = 10,
                      start_angle: float = 0.000000,
                      end_angle: float = 90.000000) -> GeometryScriptPolyPath
```

X.create_arc_path2d(center=[0.000000, 0.000000], radius=10.000000, num_points=10, start_angle=0.000000, end_angle=90.000000) -> GeometryScriptPolyPath
Create an open arc on the XY plane around the given Center.
As it is an open path, the end vertex exactly hits the target EndAngle (so will be positioned on the start vertex if the end aligns to the start)

Args:
    center (Vector2D): 
    radius (float): 
    num_points (int32): 
    start_angle (float): 
    end_angle (float): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_PolyPath.convert_spline_to_poly_path"></a>

#### convert_spline_to_poly_path

```python
@classmethod
def convert_spline_to_poly_path(
    cls, spline: SplineComponent,
    sampling_options: GeometryScriptSplineSamplingOptions
) -> GeometryScriptPolyPath
```

X.convert_spline_to_poly_path(spline, sampling_options) -> GeometryScriptPolyPath
Sample positions from a USplineComponent into a PolyPath, based on the given SamplingOptions

Args:
    spline (SplineComponent): 
    sampling_options (GeometryScriptSplineSamplingOptions): 

Returns:
    GeometryScriptPolyPath: 

    poly_path (GeometryScriptPolyPath):

<a id="unreal.GeometryScript_PolyPath.convert_poly_path_to_array_of_vector2d"></a>

#### convert_poly_path_to_array_of_vector2d

```python
@classmethod
def convert_poly_path_to_array_of_vector2d(
        cls, poly_path: GeometryScriptPolyPath) -> Array[Vector2D]
```

X.convert_poly_path_to_array_of_vector2d(poly_path) -> Array[Vector2D]
Creates an array of 2D Vectors with the PolyPath vertex locations projected onto the XY plane.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    Array[Vector2D]: 

    vertex_array (Array[Vector2D]):

<a id="unreal.GeometryScript_PolyPath.convert_poly_path_to_array"></a>

#### convert_poly_path_to_array

```python
@classmethod
def convert_poly_path_to_array(
        cls, poly_path: GeometryScriptPolyPath) -> Array[Vector]
```

X.convert_poly_path_to_array(poly_path) -> Array[Vector]
Populates an array of 3D vectors with the PolyPath vertex locations.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    Array[Vector]: 

    vertex_array (Array[Vector]):

<a id="unreal.GeometryScript_PolyPath.convert_array_to_poly_path"></a>

#### convert_array_to_poly_path

```python
@classmethod
def convert_array_to_poly_path(
        cls, vertex_array: Array[Vector]) -> GeometryScriptPolyPath
```

X.convert_array_to_poly_path(vertex_array) -> GeometryScriptPolyPath
Creates a PolyPath from an array of 3D position vectors.

Args:
    vertex_array (Array[Vector]): 

Returns:
    GeometryScriptPolyPath: 

    poly_path (GeometryScriptPolyPath):

<a id="unreal.GeometryScript_PolyPath.convert_array_of_vector2d_to_poly_path"></a>

#### convert_array_of_vector2d_to_poly_path

```python
@classmethod
def convert_array_of_vector2d_to_poly_path(
        cls, vertex_array: Array[Vector2D]) -> GeometryScriptPolyPath
```

X.convert_array_of_vector2d_to_poly_path(vertex_array) -> GeometryScriptPolyPath
Creates a PolyPath from an array of 2D position vectors. The Z-coordinate of the corresponding PolyPath vertices will be zero.

Args:
    vertex_array (Array[Vector2D]): 

Returns:
    GeometryScriptPolyPath: 

    poly_path (GeometryScriptPolyPath):

<a id="unreal.GeometryScript_PolyPath.conv_geometry_script_poly_path_to_array_of_vector2d"></a>

#### conv_geometry_script_poly_path_to_array_of_vector2d

```python
@classmethod
def conv_geometry_script_poly_path_to_array_of_vector2d(
        cls, poly_path: GeometryScriptPolyPath) -> Array[Vector2D]
```

X.conv_geometry_script_poly_path_to_array_of_vector2d(poly_path) -> Array[Vector2D]
Returns an array of 2D Vectors with the PolyPath vertex locations projected onto the XY plane.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    Array[Vector2D]:

<a id="unreal.GeometryScript_PolyPath.conv_geometry_script_poly_path_to_array"></a>

#### conv_geometry_script_poly_path_to_array

```python
@classmethod
def conv_geometry_script_poly_path_to_array(
        cls, poly_path: GeometryScriptPolyPath) -> Array[Vector]
```

X.conv_geometry_script_poly_path_to_array(poly_path) -> Array[Vector]
Returns an array of 3D vectors with the PolyPath vertex locations.

Args:
    poly_path (GeometryScriptPolyPath): 

Returns:
    Array[Vector]:

<a id="unreal.GeometryScript_PolyPath.conv_array_to_geometry_script_poly_path"></a>

#### conv_array_to_geometry_script_poly_path

```python
@classmethod
def conv_array_to_geometry_script_poly_path(
        cls, path_vertices: Array[Vector]) -> GeometryScriptPolyPath
```

X.conv_array_to_geometry_script_poly_path(path_vertices) -> GeometryScriptPolyPath
Returns a PolyPath created from an array of 3D position vectors.

Args:
    path_vertices (Array[Vector]): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_PolyPath.conv_array_of_vector2d_to_geometry_script_poly_path"></a>

#### conv_array_of_vector2d_to_geometry_script_poly_path

```python
@classmethod
def conv_array_of_vector2d_to_geometry_script_poly_path(
        cls, path_vertices: Array[Vector2D]) -> GeometryScriptPolyPath
```

X.conv_array_of_vector2d_to_geometry_script_poly_path(path_vertices) -> GeometryScriptPolyPath
Returns a PolyPath created from an array of 2D position vectors. The Z-coordinate of the corresponding PolyPath vertices will be zero.

Args:
    path_vertices (Array[Vector2D]): 

Returns:
    GeometryScriptPolyPath:

<a id="unreal.GeometryScript_SceneUtils"></a>