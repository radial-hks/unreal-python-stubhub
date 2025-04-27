## GeometryScript_Ray Objects

```python
class GeometryScript_Ray(BlueprintFunctionLibrary)
```

Geometry Script Library Ray Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ShapeFunctions.h

<a id="unreal.GeometryScript_Ray.make_ray_from_points"></a>

#### make_ray_from_points

```python
@classmethod
def make_ray_from_points(cls, a: Vector, b: Vector) -> Ray
```

X.make_ray_from_points(a, b) -> Ray
Create a Ray from two points, placing the Origin at A and the Direction as Normalize(B-A)

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Ray:

<a id="unreal.GeometryScript_Ray.make_ray_from_point_direction"></a>

#### make_ray_from_point_direction

```python
@classmethod
def make_ray_from_point_direction(cls,
                                  origin: Vector,
                                  direction: Vector,
                                  direction_is_normalized: bool = True) -> Ray
```

X.make_ray_from_point_direction(origin, direction, direction_is_normalized=True) -> Ray
Create a Ray from an Origin and Direction, with optionally non-normalized Direction

Args:
    origin (Vector): 
    direction (Vector): 
    direction_is_normalized (bool): 

Returns:
    Ray:

<a id="unreal.GeometryScript_Ray.get_transformed_ray"></a>

#### get_transformed_ray

```python
@classmethod
def get_transformed_ray(cls,
                        ray: Ray,
                        transform: Transform,
                        invert: bool = False) -> Ray
```

X.get_transformed_ray(ray, transform, invert=False) -> Ray
Apply the given Transform to the given Ray, or optionally the Transform Inverse, and return the new transformed Ray

Args:
    ray (Ray): 
    transform (Transform): 
    invert (bool): 

Returns:
    Ray:

<a id="unreal.GeometryScript_Ray.get_ray_start_end"></a>

#### get_ray_start_end

```python
@classmethod
def get_ray_start_end(cls,
                      ray: Ray,
                      start_distance: float = 0.000000,
                      end_distance: float = 0.000000) -> Tuple[Vector, Vector]
```

X.get_ray_start_end(ray, start_distance=0.000000, end_distance=0.000000) -> (start_point=Vector, end_point=Vector)
Get two points along the ray.

Args:
    ray (Ray): 
    start_distance (double): 
    end_distance (double): 

Returns:
    tuple: 

    start_point (Vector): returned as Origin + StartDistance*Direction

    end_point (Vector): returned as Origin + EndDistance*Direction, Unless EndDistance = 0, then MaxFloat is used as the Distance

<a id="unreal.GeometryScript_Ray.get_ray_sphere_intersection"></a>

#### get_ray_sphere_intersection

```python
@classmethod
def get_ray_sphere_intersection(
        cls, ray: Ray, sphere_center: Vector,
        sphere_radius: float) -> Optional[Tuple[float, float]]
```

X.get_ray_sphere_intersection(ray, sphere_center, sphere_radius) -> (distance1=double, distance2=double) or None
Check if the Ray intersects a Sphere defined by the SphereCenter and SphereRadius.
This function returns two intersection distances (ray parameters). If the ray grazes the sphere, both
distances will be the same, and if it misses, they will be MAX_FLOAT.
Use the function GetRayPoint to convert the distances to points on the ray/sphere.

Args:
    ray (Ray): 
    sphere_center (Vector): 
    sphere_radius (double): 

Returns:
    tuple or None: true if ray intersects sphere

    distance1 (double): Distance along ray (Ray Parameter) to first/closer intersection point with sphere

    distance2 (double): Distance along ray (Ray Parameter) to second/further intersection point with sphere

<a id="unreal.GeometryScript_Ray.get_ray_segment_closest_point"></a>

#### get_ray_segment_closest_point

```python
@classmethod
def get_ray_segment_closest_point(
        cls, ray: Ray, seg_start_point: Vector,
        seg_end_point: Vector) -> Tuple[float, float, Vector, Vector]
```

X.get_ray_segment_closest_point(ray, seg_start_point, seg_end_point) -> (double, ray_parameter=double, ray_point=Vector, seg_point=Vector)
Compute the pair of closest points on a 3D Ray and Line Segment
The Line Segment is defined by its two Endpoints.

Args:
    ray (Ray): 
    seg_start_point (Vector): 
    seg_end_point (Vector): 

Returns:
    tuple: the minimum distance between the Ray and Segment, ie between RayPoint and SegPoint

    ray_parameter (double): the Ray Parameter of the closest point on the Ray (range 0, inf)

    ray_point (Vector): the point on the Ray corresponding to RayParameter

    seg_point (Vector): the point on the Segment

<a id="unreal.GeometryScript_Ray.get_ray_point_distance"></a>

#### get_ray_point_distance

```python
@classmethod
def get_ray_point_distance(cls, ray: Ray, point: Vector) -> float
```

X.get_ray_point_distance(ray, point) -> double
Get the distance from Point to the closest point on the Ray

Args:
    ray (Ray): 
    point (Vector): 

Returns:
    double:

<a id="unreal.GeometryScript_Ray.get_ray_point"></a>

#### get_ray_point

```python
@classmethod
def get_ray_point(cls, ray: Ray, distance: float) -> Vector
```

X.get_ray_point(ray, distance) -> Vector
Get a Point at the given Distance along the Ray (Origin + Distance*Direction)

Args:
    ray (Ray): 
    distance (double): 

Returns:
    Vector:

<a id="unreal.GeometryScript_Ray.get_ray_plane_intersection"></a>

#### get_ray_plane_intersection

```python
@classmethod
def get_ray_plane_intersection(cls, ray: Ray, plane: Plane) -> Optional[float]
```

X.get_ray_plane_intersection(ray, plane) -> double or None
Find the intersection of a Ray and a Plane

Args:
    ray (Ray): 
    plane (Plane): 

Returns:
    double or None: true if the ray hits the plane (only false if ray is parallel with plane)

    hit_distance (double): the returned Distance along the ray (Ray Parameter) to intersection point with the Plane

<a id="unreal.GeometryScript_Ray.get_ray_parameter"></a>

#### get_ray_parameter

```python
@classmethod
def get_ray_parameter(cls, ray: Ray, point: Vector) -> float
```

X.get_ray_parameter(ray, point) -> double
Project the given Point onto the closest point along the Ray, and return the Ray Parameter/Distance at that Point

Args:
    ray (Ray): 
    point (Vector): 

Returns:
    double:

<a id="unreal.GeometryScript_Ray.get_ray_line_closest_point"></a>

#### get_ray_line_closest_point

```python
@classmethod
def get_ray_line_closest_point(
        cls, ray: Ray, line_origin: Vector,
        line_direction: Vector) -> Tuple[float, float, Vector, float, Vector]
```

X.get_ray_line_closest_point(ray, line_origin, line_direction) -> (double, ray_parameter=double, ray_point=Vector, line_parameter=double, line_point=Vector)
Compute the pair of closest points on a 3D Ray and Line.
The Line is defined by an Origin and Direction (ie same as a Ray) but extends infinitely in both directions.

Args:
    ray (Ray): 
    line_origin (Vector): 
    line_direction (Vector): 

Returns:
    tuple: the minimum distance between the Ray and Line, ie between RayPoint and LinePoint

    ray_parameter (double): the Ray Parameter of the closest point on the Ray (range 0, inf)

    ray_point (Vector): the point on the Ray corresponding to RayParameter

    line_parameter (double): the Line parameter of the closest point on the Line (range -inf, inf)

    line_point (Vector): the point on the Line corresponding to LineParameter

<a id="unreal.GeometryScript_Ray.get_ray_closest_point"></a>

#### get_ray_closest_point

```python
@classmethod
def get_ray_closest_point(cls, ray: Ray, point: Vector) -> Vector
```

X.get_ray_closest_point(ray, point) -> Vector
Get the closest point on the Ray to the given Point

Args:
    ray (Ray): 
    point (Vector): 

Returns:
    Vector:

<a id="unreal.GeometryScript_Ray.get_ray_box_intersection"></a>

#### get_ray_box_intersection

```python
@classmethod
def get_ray_box_intersection(cls, ray: Ray, box: Box) -> Optional[float]
```

X.get_ray_box_intersection(ray, box) -> double or None
Find the intersection of a Ray and a Box

Args:
    ray (Ray): 
    box (Box): 

Returns:
    double or None: true if the ray hits the box, and false otherwise

    hit_distance (double): Distance along the ray (Ray Parameter) to first intersection point with the Box

<a id="unreal.GeometryScript_Box"></a>