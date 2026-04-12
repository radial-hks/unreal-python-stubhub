## TKMathFunctionLibrary Objects

```python
class TKMathFunctionLibrary(BlueprintFunctionLibrary)
```

TKMath Function Library

**C++ Source:**

- **Plugin**: VictoryBPLibrary
- **Module**: VictoryBPLibrary
- **File**: TKMathFunctionLibrary.h

<a id="unreal.TKMathFunctionLibrary.vector_radians_to_degrees"></a>

#### vector\_radians\_to\_degrees

```python
@classmethod
def vector_radians_to_degrees(cls, rad_vector: Vector) -> Vector
```

X.vector_radians_to_degrees(rad_vector) -> Vector
Converts radians to degrees.

Args:
    rad_vector (Vector): 

Returns:
    Vector:

<a id="unreal.TKMathFunctionLibrary.vector_degrees_to_radians"></a>

#### vector\_degrees\_to\_radians

```python
@classmethod
def vector_degrees_to_radians(cls, deg_vector: Vector) -> Vector
```

X.vector_degrees_to_radians(deg_vector) -> Vector
Converts degrees to radians.

Args:
    deg_vector (Vector): 

Returns:
    Vector:

<a id="unreal.TKMathFunctionLibrary.sphere_box_intersection"></a>

#### sphere\_box\_intersection

```python
@classmethod
def sphere_box_intersection(cls, sphere_origin: Vector, sphere_radius: float,
                            box_origin: Vector, box_extent: Vector) -> bool
```

X.sphere_box_intersection(sphere_origin, sphere_radius, box_origin, box_extent) -> bool
Performs a sphere vs box intersection test.

Args:
    sphere_origin (Vector): the center of the sphere being tested against the box.
    sphere_radius (float): the size of the sphere being tested.
    box_origin (Vector): the box origin being tested against.
    box_extent (Vector): the box extend (width, depth, height).

Returns:
    bool: Whether the sphere/box intersect or not.

<a id="unreal.TKMathFunctionLibrary.signed_distance_plane_point"></a>

#### signed\_distance\_plane\_point

```python
@classmethod
def signed_distance_plane_point(cls, plane_normal: Vector, plane_point: Vector,
                                point: Vector) -> float
```

X.signed_distance_plane_point(plane_normal, plane_point, point) -> float
Get the shortest distance between a point and a plane.
The output is signed so it holds information as to which side of the plane normal the point is.

Args:
    plane_normal (Vector): 
    plane_point (Vector): 
    point (Vector): 

Returns:
    float:

<a id="unreal.TKMathFunctionLibrary.set_vector_length"></a>

#### set\_vector\_length

```python
@classmethod
def set_vector_length(cls, a: Vector, size: float) -> Vector
```

X.set_vector_length(a, size) -> Vector
Changes the size (length) of a Vector to the given size (normalized vector * size).

Args:
    a (Vector): 
    size (float): 

Returns:
    Vector:

<a id="unreal.TKMathFunctionLibrary.set_center_of_mass_offset"></a>

#### set\_center\_of\_mass\_offset

```python
@classmethod
def set_center_of_mass_offset(cls,
                              target: PrimitiveComponent,
                              offset: Vector,
                              bone_name: Name = "None") -> None
```

X.set_center_of_mass_offset(target, offset, bone_name="None") -> None
* Set the physx center of mass offset.
* Note: this offsets the physx-calculated center of mass (it is not an offset from the pivot point).

Args:
    target (PrimitiveComponent): 
    offset (Vector): 
    bone_name (Name):

<a id="unreal.TKMathFunctionLibrary.round_to_upper_multiple"></a>

#### round\_to\_upper\_multiple

```python
@classmethod
def round_to_upper_multiple(cls,
                            a: int,
                            multiple: int = 32,
                            skip_self: bool = False) -> int
```

X.round_to_upper_multiple(a, multiple=32, skip_self=False) -> int32
Rounds an integer to the upper multiple of the given number.
If Skip Self is set to True it will skip to the next multiple if the integer rounds to itself.

Args:
    a (int32): 
    multiple (int32): The multiple number to round to.
    skip_self (bool): Skip to the next multiple if the integer rounds to itself.

Returns:
    int32:

<a id="unreal.TKMathFunctionLibrary.round_to_nearest_multiple"></a>

#### round\_to\_nearest\_multiple

```python
@classmethod
def round_to_nearest_multiple(cls, a: int, multiple: int = 32) -> int
```

X.round_to_nearest_multiple(a, multiple=32) -> int32
Rounds an integer to the nearest multiple of the given number.

Args:
    a (int32): 
    multiple (int32): 

Returns:
    int32:

<a id="unreal.TKMathFunctionLibrary.round_to_lower_multiple"></a>

#### round\_to\_lower\_multiple

```python
@classmethod
def round_to_lower_multiple(cls,
                            a: int,
                            multiple: int = 32,
                            skip_self: bool = False) -> int
```

X.round_to_lower_multiple(a, multiple=32, skip_self=False) -> int32
Rounds an integer to the lower multiple of the given number.
If Skip Self is set to True it will skip to the previous multiple if the integer rounds to itself.

Args:
    a (int32): 
    multiple (int32): The multiple number to round to.
    skip_self (bool): Skip to the previous multiple if the integer rounds to itself.

Returns:
    int32:

<a id="unreal.TKMathFunctionLibrary.project_point_on_line"></a>

#### project\_point\_on\_line

```python
@classmethod
def project_point_on_line(cls, line_origin: Vector, line_direction: Vector,
                          point: Vector) -> Vector
```

X.project_point_on_line(line_origin, line_direction, point) -> Vector
Returns a vector point which is a projection from a point to a line (defined by the vector couple LineOrigin, LineDirection).
The line is infinite (in both directions).

Args:
    line_origin (Vector): 
    line_direction (Vector): 
    point (Vector): 

Returns:
    Vector:

<a id="unreal.TKMathFunctionLibrary.point_on_which_side_of_line_segment"></a>

#### point\_on\_which\_side\_of\_line\_segment

```python
@classmethod
def point_on_which_side_of_line_segment(cls, line_point1: Vector,
                                        line_point2: Vector,
                                        point: Vector) -> int
```

X.point_on_which_side_of_line_segment(line_point1, line_point2, point) -> int32
* Returns 0 if point is on the line segment.
* Returns 1 if point is not on the line segment and it is on the side of linePoint1.
* Returns 2 if point is not on the line segment and it is on the side of linePoint2.

Args:
    line_point1 (Vector): 
    line_point2 (Vector): 
    point (Vector): 

Returns:
    int32:

<a id="unreal.TKMathFunctionLibrary.negate_vector2d"></a>

#### negate\_vector2d

```python
@classmethod
def negate_vector2d(cls, a: Vector2D) -> Vector2D
```

X.negate_vector2d(a) -> Vector2D
Reverses the sign (- or +) of a Vector2D.

Args:
    a (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.TKMathFunctionLibrary.negate_int"></a>

#### negate\_int

```python
@classmethod
def negate_int(cls, a: int) -> int
```

X.negate_int(a) -> int32
Reverses the sign (- or +) of an integer.

Args:
    a (int32): 

Returns:
    int32:

<a id="unreal.TKMathFunctionLibrary.negate_float"></a>

#### negate\_float

```python
@classmethod
def negate_float(cls, a: float) -> float
```

X.negate_float(a) -> float
Reverses the sign (- or +) of a float.

Args:
    a (float): 

Returns:
    float:

<a id="unreal.TKMathFunctionLibrary.line_to_line_intersection"></a>

#### line\_to\_line\_intersection

```python
@classmethod
def line_to_line_intersection(cls, line_point1: Vector, line_dir1: Vector,
                              line_point2: Vector,
                              line_dir2: Vector) -> Optional[Vector]
```

X.line_to_line_intersection(line_point1, line_dir1, line_point2, line_dir2) -> Vector or None
Calculate the intersection point of two infinitely long lines. Returns true if lines intersect, otherwise false.
Note that in 3d, two lines do not intersect most of the time.
So if the two lines are not in the same plane, use Closest Points On Two Lines instead.

Args:
    line_point1 (Vector): Line point of the first line.
    line_dir1 (Vector): Line direction (normal) of the first line. Should be a normalized vector.
    line_point2 (Vector): Line point of the second line.
    line_dir2 (Vector): Line direction (normal) of the second line. Should be a normalized vector.

Returns:
    Vector or None: true if lines intersect, otherwise false.

    intersection_point (Vector): The intersection point of the lines. Returns zero if the lines do not intersect or the operation fails.

<a id="unreal.TKMathFunctionLibrary.line_extent_box_intersection"></a>

#### line\_extent\_box\_intersection

```python
@classmethod
def line_extent_box_intersection(
        cls, in_box: Box, start: Vector, end: Vector,
        extent: Vector) -> Optional[Tuple[Vector, Vector, float]]
```

X.line_extent_box_intersection(in_box, start, end, extent) -> (hit_location=Vector, hit_normal=Vector, hit_time=float) or None
Swept-Box vs Box test.
Sweps a box defined by Extend from Start to End points and returns whether it hit a box or not plus the hit location and hit normal if successful.

Args:
    in_box (Box): 
    start (Vector): 
    end (Vector): 
    extent (Vector): 

Returns:
    tuple or None: 

    hit_location (Vector): 

    hit_normal (Vector): 

    hit_time (float):

<a id="unreal.TKMathFunctionLibrary.is_power_of_two"></a>

#### is\_power\_of\_two

```python
@classmethod
def is_power_of_two(cls, x: int) -> bool
```

X.is_power_of_two(x) -> bool
Returns true if the integer is a power of two number.

Args:
    x (int32): 

Returns:
    bool:

<a id="unreal.TKMathFunctionLibrary.is_point_inside_box"></a>

#### is\_point\_inside\_box

```python
@classmethod
def is_point_inside_box(cls, point: Vector, box_origin: Vector,
                        box_extent: Vector) -> bool
```

X.is_point_inside_box(point, box_origin, box_extent) -> bool
Returns true if the given Point vector is within a box (defined by BoxOrigin and BoxExtent).

Args:
    point (Vector): 
    box_origin (Vector): 
    box_extent (Vector): 

Returns:
    bool:

<a id="unreal.TKMathFunctionLibrary.is_multiple_of"></a>

#### is\_multiple\_of

```python
@classmethod
def is_multiple_of(cls, a: int, multiple: int) -> bool
```

X.is_multiple_of(a, multiple) -> bool
Returns true if the integer is a multiple of the given number.

Args:
    a (int32): 
    multiple (int32): 

Returns:
    bool:

<a id="unreal.TKMathFunctionLibrary.is_line_inside_sphere"></a>

#### is\_line\_inside\_sphere

```python
@classmethod
def is_line_inside_sphere(cls, line_start: Vector, line_dir: Vector,
                          line_length: float, sphere_origin: Vector,
                          sphere_radius: float) -> bool
```

X.is_line_inside_sphere(line_start, line_dir, line_length, sphere_origin, sphere_radius) -> bool
Determines whether a line intersects a sphere.

Args:
    line_start (Vector): 
    line_dir (Vector): 
    line_length (float): 
    sphere_origin (Vector): 
    sphere_radius (float): 

Returns:
    bool:

<a id="unreal.TKMathFunctionLibrary.is_even_number"></a>

#### is\_even\_number

```python
@classmethod
def is_even_number(cls, a: float) -> bool
```

X.is_even_number(a) -> bool
Returns true if the number is even (false if it's odd).

Args:
    a (float): 

Returns:
    bool:

<a id="unreal.TKMathFunctionLibrary.grid_snap"></a>

#### grid\_snap

```python
@classmethod
def grid_snap(cls, a: Vector, grid: float) -> Vector
```

X.grid_snap(a, grid) -> Vector
Snaps vector to nearest grid multiple.

Args:
    a (Vector): 
    grid (float): 

Returns:
    Vector:

<a id="unreal.TKMathFunctionLibrary.get_velocity_at_point"></a>

#### get\_velocity\_at\_point

```python
@classmethod
def get_velocity_at_point(cls,
                          target: PrimitiveComponent,
                          point: Vector,
                          bone_name: Name = "None",
                          draw_debug_info: bool = False) -> Vector
```

X.get_velocity_at_point(target, point, bone_name="None", draw_debug_info=False) -> Vector
Get the current world velocity of a point on a physics-enabled component.

Args:
    target (PrimitiveComponent): 
    point (Vector): Point in world space.
    bone_name (Name): If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body.
    draw_debug_info (bool): Draw debug point & string.

Returns:
    Vector: The velocity of the point in world space.

<a id="unreal.TKMathFunctionLibrary.get_console_variable_int"></a>

#### get\_console\_variable\_int

```python
@classmethod
def get_console_variable_int(cls, variable_name: str) -> int
```

X.get_console_variable_int(variable_name) -> int32
Get Console Variable Int

Args:
    variable_name (str): 

Returns:
    int32:

<a id="unreal.TKMathFunctionLibrary.get_console_variable_float"></a>

#### get\_console\_variable\_float

```python
@classmethod
def get_console_variable_float(cls, variable_name: str) -> float
```

X.get_console_variable_float(variable_name) -> float
Get Console Variable Float

Args:
    variable_name (str): 

Returns:
    float:

<a id="unreal.TKMathFunctionLibrary.convert_physics_linear_velocity"></a>

#### convert\_physics\_linear\_velocity

```python
@classmethod
def convert_physics_linear_velocity(cls, velocity: Vector,
                                    speed_unit: SpeedUnit) -> float
```

X.convert_physics_linear_velocity(velocity, speed_unit) -> float
Converts Physics Linear Velocity to a more useful speed unit.

Args:
    velocity (Vector): 
    speed_unit (SpeedUnit): 

Returns:
    float:

<a id="unreal.TKMathFunctionLibrary.convert_anchor_to_anchor"></a>

#### convert\_anchor\_to\_anchor

```python
@classmethod
def convert_anchor_to_anchor(cls, world_context_object: Object,
                             current_anchor: Anchors, offsets: Margin,
                             target_anchor: Anchors) -> Margin
```

X.convert_anchor_to_anchor(world_context_object, current_anchor, offsets, target_anchor) -> Margin
Converts UMG layout offsets to another anchor.

Args:
    world_context_object (Object): 
    current_anchor (Anchors): 
    offsets (Margin): 
    target_anchor (Anchors): 

Returns:
    Margin: 

    converted_offsets (Margin):

<a id="unreal.TKMathFunctionLibrary.closest_points_on_two_lines"></a>

#### closest\_points\_on\_two\_lines

```python
@classmethod
def closest_points_on_two_lines(
        cls, line_point1: Vector, line_vec1: Vector, line_point2: Vector,
        line_vec2: Vector) -> Optional[Tuple[Vector, Vector]]
```

X.closest_points_on_two_lines(line_point1, line_vec1, line_point2, line_vec2) -> (closest_point_line1=Vector, closest_point_line2=Vector) or None
* Calculate the closest points between two infinitely long lines.
* If lines are intersecting (not parallel) it will return false! Use Line To Line Intersection instead.
*

Args:
    line_point1 (Vector): Line point of the first line. *
    line_vec1 (Vector): Line direction (normal) of the first line. Should be a normalized vector. *
    line_point2 (Vector): Line point of the second line. *
    line_vec2 (Vector): Line direction (normal) of the second line. Should be a normalized vector. *

Returns:
    tuple or None: true if lines are parallel, false otherwise.

    closest_point_line1 (Vector): The closest point of line1 to line2. Returns zero if the lines intersect. *

    closest_point_line2 (Vector): The closest point of line2 to line1. Returns zero if the lines intersect. *

<a id="unreal.TKMathFunctionLibrary.closest_points_of_line_segments"></a>

#### closest\_points\_of\_line\_segments

```python
@classmethod
def closest_points_of_line_segments(
        cls, line1_start: Vector, line1_end: Vector, line2_start: Vector,
        line2_end: Vector) -> Tuple[Vector, Vector]
```

X.closest_points_of_line_segments(line1_start, line1_end, line2_start, line2_end) -> (line_point1=Vector, line_point2=Vector)
Find closest points between 2 line segments.

Args:
    line1_start (Vector): 
    line1_end (Vector): 
    line2_start (Vector): 
    line2_end (Vector): 

Returns:
    tuple: 

    line_point1 (Vector): Closest point on segment 1 to segment 2.

    line_point2 (Vector): Closest point on segment 2 to segment 1.

<a id="unreal.TKMathFunctionLibrary.closest_point_on_sphere_to_line"></a>

#### closest\_point\_on\_sphere\_to\_line

```python
@classmethod
def closest_point_on_sphere_to_line(cls, sphere_origin: Vector,
                                    sphere_radius: float, line_origin: Vector,
                                    line_dir: Vector) -> Vector
```

X.closest_point_on_sphere_to_line(sphere_origin, sphere_radius, line_origin, line_dir) -> Vector
Find closest point on a Sphere to a Line.
When line intersects Sphere, then closest point to LineOrigin is returned.

Args:
    sphere_origin (Vector): Origin of Sphere
    sphere_radius (float): Radius of Sphere
    line_origin (Vector): Origin of line
    line_dir (Vector): Direction of line.

Returns:
    Vector: Closest point on sphere to given line.

<a id="unreal.TKMathFunctionLibrary.closest_point_on_line_seqment"></a>

#### closest\_point\_on\_line\_seqment

```python
@classmethod
def closest_point_on_line_seqment(cls, point: Vector, line_start: Vector,
                                  line_end: Vector) -> Vector
```

X.closest_point_on_line_seqment(point, line_start, line_end) -> Vector
Find the point on line segment from LineStart to LineEnd which is closest to Point.

Args:
    point (Vector): 
    line_start (Vector): 
    line_end (Vector): 

Returns:
    Vector:

<a id="unreal.TKMathFunctionLibrary.are_line_segments_crossing"></a>

#### are\_line\_segments\_crossing

```python
@classmethod
def are_line_segments_crossing(cls, point_a1: Vector, point_a2: Vector,
                               point_b1: Vector, point_b2: Vector) -> bool
```

X.are_line_segments_crossing(point_a1, point_a2, point_b1, point_b2) -> bool
* Returns true if the two line segments are intersecting and not parallel.
* If you need the intersection point, use Closest Points On Two Lines.

Args:
    point_a1 (Vector): 
    point_a2 (Vector): 
    point_b1 (Vector): 
    point_b2 (Vector): 

Returns:
    bool:

<a id="unreal.RamaVictoryPluginCreateProcessPipe"></a>