## Box Objects

```python
class Box(StructBase)
```

A bounding box.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Box.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_valid`` (bool):  [Read-Write]
- ``max`` (Vector):  [Read-Write]
- ``min`` (Vector):  [Read-Write]

<a id="unreal.Box.__init__"></a>

#### __init__

```python
def __init__(min: Vector = [0.000000, 0.000000, 0.000000],
             max: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.Box.min"></a>

#### min

```python
@property
def min() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Box.min"></a>

#### min

```python
@min.setter
def min(value: Vector) -> None
```

<a id="unreal.Box.max"></a>

#### max

```python
@property
def max() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Box.max"></a>

#### max

```python
@max.setter
def max(value: Vector) -> None
```

<a id="unreal.Box.is_valid"></a>

#### is_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Box.is_valid"></a>

#### is_valid

```python
@is_valid.setter
def is_valid(value: bool) -> None
```

<a id="unreal.Box.random_point_in_box_extents"></a>

#### random_point_in_box_extents

```python
def random_point_in_box_extents() -> Vector
```

x.random_point_in_box_extents() -> Vector
Returns a random point within the specified bounding box.

Returns:
    Vector:

<a id="unreal.Box.test_point_inside_box"></a>

#### test_point_inside_box

```python
def test_point_inside_box(point: Vector,
                          consider_on_box_as_inside: bool = True) -> bool
```

x.test_point_inside_box(point, consider_on_box_as_inside=True) -> bool
Test if a Point is inside the Box, returning true if so, otherwise false

Args:
    point (Vector): 
    consider_on_box_as_inside (bool): if true, a point lying on the box face is considered "inside", otherwise it is considered "outside"

Returns:
    bool:

<a id="unreal.Box.test_box_sphere_intersection"></a>

#### test_box_sphere_intersection

```python
def test_box_sphere_intersection(sphere_center: Vector,
                                 sphere_radius: float) -> bool
```

x.test_box_sphere_intersection(sphere_center, sphere_radius) -> bool
Check if the Box intersects a Sphere defined by the SphereCenter and SphereRadius

Args:
    sphere_center (Vector): 
    sphere_radius (double): 

Returns:
    bool:

<a id="unreal.Box.test_box_box_intersection"></a>

#### test_box_box_intersection

```python
def test_box_box_intersection(box2: Box) -> bool
```

x.test_box_box_intersection(box2) -> bool
Test if Box1 and Box2 intersect

Args:
    box2 (Box): 

Returns:
    bool:

<a id="unreal.Box.get_transformed_box"></a>

#### get_transformed_box

```python
def get_transformed_box(transform: Transform) -> Box
```

x.get_transformed_box(transform) -> Box
Apply the input Transform to the corners of the input Box, and return the new Box containing those points

Args:
    transform (Transform): 

Returns:
    Box:

<a id="unreal.Box.get_expanded_box"></a>

#### get_expanded_box

```python
def get_expanded_box(expand_by: Vector) -> Box
```

x.get_expanded_box(expand_by) -> Box
Get the input Box expanded by adding the ExpandBy parameter to both the Min and Max.
Dimensions will be clamped to the center point if any of ExpandBy are larger than half the box size

Args:
    expand_by (Vector): 

Returns:
    Box:

<a id="unreal.Box.get_box_volume_area"></a>

#### get_box_volume_area

```python
def get_box_volume_area() -> Tuple[float, float]
```

x.get_box_volume_area() -> (volume=double, surface_area=double)
Get the Volume and Surface Area of a Box

Returns:
    tuple: 

    volume (double): 

    surface_area (double):

<a id="unreal.Box.get_box_point_distance"></a>

#### get_box_point_distance

```python
def get_box_point_distance(point: Vector) -> float
```

x.get_box_point_distance(point) -> double
Calculate the minimum distance between the Box and the Point

Args:
    point (Vector): 

Returns:
    double:

<a id="unreal.Box.get_box_face_center"></a>

#### get_box_face_center

```python
def get_box_face_center(face_index: int) -> Tuple[Vector, Vector]
```

x.get_box_face_center(face_index) -> (Vector, face_normal=Vector)
Get the position of the center of a face of the Box. Faces are indexed from 0 to 5,
using an ordering where 0/1 are the MinZ/MaxZ faces, 2/3 are MinY/MaxY, and 4/5 are MinX/MaxX

Args:
    face_index (int32): 

Returns:
    Vector: 

    face_normal (Vector): returned Normal vector of the identified face

<a id="unreal.Box.get_box_corner"></a>

#### get_box_corner

```python
def get_box_corner(corner_index: int) -> Vector
```

x.get_box_corner(corner_index) -> Vector
Get the position of a corner of the Box. Corners are indexed from 0 to 7, using
an ordering where 0 is the Min corner, 1/2/3 are +Z/+Y/+X from the Min corner,
7 is the Max corner, and 4/5/6 are -Z/-Y/-X from the Max corner.

Args:
    corner_index (int32): 

Returns:
    Vector:

<a id="unreal.Box.get_box_center_size"></a>

#### get_box_center_size

```python
def get_box_center_size() -> Tuple[Vector, Vector]
```

x.get_box_center_size() -> (center=Vector, dimensions=Vector)
Get the Center point and X/Y/Z Dimensions of a Box (full dimensions, not Extents)

Returns:
    tuple: 

    center (Vector): 

    dimensions (Vector):

<a id="unreal.Box.get_box_box_distance"></a>

#### get_box_box_distance

```python
def get_box_box_distance(box2: Box) -> float
```

x.get_box_box_distance(box2) -> double
Calculate the minimum distance between Box1 and Box2

Args:
    box2 (Box): 

Returns:
    double:

<a id="unreal.Box.find_closest_point_on_box"></a>

#### find_closest_point_on_box

```python
def find_closest_point_on_box(point: Vector) -> Tuple[Vector, bool]
```

x.find_closest_point_on_box(point) -> (Vector, is_inside=bool)
Find the point on the faces of the Box that is closest to the input Point.
If the Point is inside the Box, it is returned, ie points Inside do not project to the Box Faces

Args:
    point (Vector): 

Returns:
    bool: 

    is_inside (bool): if the Point is inside the Box, this will return as true, otherwise false

<a id="unreal.Box.find_box_box_intersection"></a>

#### find_box_box_intersection

```python
def find_box_box_intersection(box2: Box) -> Tuple[Box, bool]
```

x.find_box_box_intersection(box2) -> (Box, is_intersecting=bool)
Find the Box formed by the intersection of Box1 and Box2

Args:
    box2 (Box): 

Returns:
    bool: 

    is_intersecting (bool): if the boxes do not intersect, this will be returned as false, otherwise true

<a id="unreal.Vector"></a>