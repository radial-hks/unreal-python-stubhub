## Ray Objects

```python
class Ray(StructBase)
```

3D Ray represented by Origin and (normalized) Direction.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Ray.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (Vector):  [Read-Write]
- ``origin`` (Vector):  [Read-Write]

<a id="unreal.Ray.__init__"></a>

#### __init__

```python
def __init__(origin: Vector = [0.000000, 0.000000, 0.000000],
             direction: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.Ray.origin"></a>

#### origin

```python
@property
def origin() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Ray.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector) -> None
```

<a id="unreal.Ray.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Ray.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.Ray.get_transformed_ray"></a>

#### get_transformed_ray

```python
def get_transformed_ray(transform: Transform, invert: bool = False) -> Ray
```

x.get_transformed_ray(transform, invert=False) -> Ray
Apply the given Transform to the given Ray, or optionally the Transform Inverse, and return the new transformed Ray

Args:
    transform (Transform): 
    invert (bool): 

Returns:
    Ray:

<a id="unreal.Ray.get_ray_start_end"></a>

#### get_ray_start_end

```python
def get_ray_start_end(start_distance: float = 0.000000,
                      end_distance: float = 0.000000) -> Tuple[Vector, Vector]
```

x.get_ray_start_end(start_distance=0.000000, end_distance=0.000000) -> (start_point=Vector, end_point=Vector)
Get two points along the ray.

Args:
    start_distance (double): 
    end_distance (double): 

Returns:
    tuple: 

    start_point (Vector): returned as Origin + StartDistance*Direction

    end_point (Vector): returned as Origin + EndDistance*Direction, Unless EndDistance = 0, then MaxFloat is used as the Distance

<a id="unreal.Ray.get_ray_sphere_intersection"></a>

#### get_ray_sphere_intersection

```python
def get_ray_sphere_intersection(
        sphere_center: Vector,
        sphere_radius: float) -> Optional[Tuple[float, float]]
```

x.get_ray_sphere_intersection(sphere_center, sphere_radius) -> (distance1=double, distance2=double) or None
Check if the Ray intersects a Sphere defined by the SphereCenter and SphereRadius.
This function returns two intersection distances (ray parameters). If the ray grazes the sphere, both
distances will be the same, and if it misses, they will be MAX_FLOAT.
Use the function GetRayPoint to convert the distances to points on the ray/sphere.

Args:
    sphere_center (Vector): 
    sphere_radius (double): 

Returns:
    tuple or None: true if ray intersects sphere

    distance1 (double): Distance along ray (Ray Parameter) to first/closer intersection point with sphere

    distance2 (double): Distance along ray (Ray Parameter) to second/further intersection point with sphere

<a id="unreal.Ray.get_ray_segment_closest_point"></a>

#### get_ray_segment_closest_point

```python
def get_ray_segment_closest_point(
        seg_start_point: Vector,
        seg_end_point: Vector) -> Tuple[float, float, Vector, Vector]
```

x.get_ray_segment_closest_point(seg_start_point, seg_end_point) -> (double, ray_parameter=double, ray_point=Vector, seg_point=Vector)
Compute the pair of closest points on a 3D Ray and Line Segment
The Line Segment is defined by its two Endpoints.

Args:
    seg_start_point (Vector): 
    seg_end_point (Vector): 

Returns:
    tuple: the minimum distance between the Ray and Segment, ie between RayPoint and SegPoint

    ray_parameter (double): the Ray Parameter of the closest point on the Ray (range 0, inf)

    ray_point (Vector): the point on the Ray corresponding to RayParameter

    seg_point (Vector): the point on the Segment

<a id="unreal.Ray.get_ray_point_distance"></a>

#### get_ray_point_distance

```python
def get_ray_point_distance(point: Vector) -> float
```

x.get_ray_point_distance(point) -> double
Get the distance from Point to the closest point on the Ray

Args:
    point (Vector): 

Returns:
    double:

<a id="unreal.Ray.get_ray_point"></a>

#### get_ray_point

```python
def get_ray_point(distance: float) -> Vector
```

x.get_ray_point(distance) -> Vector
Get a Point at the given Distance along the Ray (Origin + Distance*Direction)

Args:
    distance (double): 

Returns:
    Vector:

<a id="unreal.Ray.get_ray_plane_intersection"></a>

#### get_ray_plane_intersection

```python
def get_ray_plane_intersection(plane: Plane) -> Optional[float]
```

x.get_ray_plane_intersection(plane) -> double or None
Find the intersection of a Ray and a Plane

Args:
    plane (Plane): 

Returns:
    double or None: true if the ray hits the plane (only false if ray is parallel with plane)

    hit_distance (double): the returned Distance along the ray (Ray Parameter) to intersection point with the Plane

<a id="unreal.Ray.get_ray_parameter"></a>

#### get_ray_parameter

```python
def get_ray_parameter(point: Vector) -> float
```

x.get_ray_parameter(point) -> double
Project the given Point onto the closest point along the Ray, and return the Ray Parameter/Distance at that Point

Args:
    point (Vector): 

Returns:
    double:

<a id="unreal.Ray.get_ray_line_closest_point"></a>

#### get_ray_line_closest_point

```python
def get_ray_line_closest_point(
        line_origin: Vector,
        line_direction: Vector) -> Tuple[float, float, Vector, float, Vector]
```

x.get_ray_line_closest_point(line_origin, line_direction) -> (double, ray_parameter=double, ray_point=Vector, line_parameter=double, line_point=Vector)
Compute the pair of closest points on a 3D Ray and Line.
The Line is defined by an Origin and Direction (ie same as a Ray) but extends infinitely in both directions.

Args:
    line_origin (Vector): 
    line_direction (Vector): 

Returns:
    tuple: the minimum distance between the Ray and Line, ie between RayPoint and LinePoint

    ray_parameter (double): the Ray Parameter of the closest point on the Ray (range 0, inf)

    ray_point (Vector): the point on the Ray corresponding to RayParameter

    line_parameter (double): the Line parameter of the closest point on the Line (range -inf, inf)

    line_point (Vector): the point on the Line corresponding to LineParameter

<a id="unreal.Ray.get_ray_closest_point"></a>

#### get_ray_closest_point

```python
def get_ray_closest_point(point: Vector) -> Vector
```

x.get_ray_closest_point(point) -> Vector
Get the closest point on the Ray to the given Point

Args:
    point (Vector): 

Returns:
    Vector:

<a id="unreal.Ray.get_ray_box_intersection"></a>

#### get_ray_box_intersection

```python
def get_ray_box_intersection(box: Box) -> Optional[float]
```

x.get_ray_box_intersection(box) -> double or None
Find the intersection of a Ray and a Box

Args:
    box (Box): 

Returns:
    double or None: true if the ray hits the box, and false otherwise

    hit_distance (double): Distance along the ray (Ray Parameter) to first intersection point with the Box

<a id="unreal.Rotator"></a>