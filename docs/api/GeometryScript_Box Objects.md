## GeometryScript_Box Objects

```python
class GeometryScript_Box(BlueprintFunctionLibrary)
```

Geometry Script Library Box Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ShapeFunctions.h

<a id="unreal.GeometryScript_Box.test_point_inside_box"></a>

#### test_point_inside_box

```python
@classmethod
def test_point_inside_box(cls,
                          box: Box,
                          point: Vector,
                          consider_on_box_as_inside: bool = True) -> bool
```

X.test_point_inside_box(box, point, consider_on_box_as_inside=True) -> bool
Test if a Point is inside the Box, returning true if so, otherwise false

Args:
    box (Box): 
    point (Vector): 
    consider_on_box_as_inside (bool): if true, a point lying on the box face is considered "inside", otherwise it is considered "outside"

Returns:
    bool:

<a id="unreal.GeometryScript_Box.test_box_sphere_intersection"></a>

#### test_box_sphere_intersection

```python
@classmethod
def test_box_sphere_intersection(cls, box: Box, sphere_center: Vector,
                                 sphere_radius: float) -> bool
```

X.test_box_sphere_intersection(box, sphere_center, sphere_radius) -> bool
Check if the Box intersects a Sphere defined by the SphereCenter and SphereRadius

Args:
    box (Box): 
    sphere_center (Vector): 
    sphere_radius (double): 

Returns:
    bool:

<a id="unreal.GeometryScript_Box.test_box_box_intersection"></a>

#### test_box_box_intersection

```python
@classmethod
def test_box_box_intersection(cls, box1: Box, box2: Box) -> bool
```

X.test_box_box_intersection(box1, box2) -> bool
Test if Box1 and Box2 intersect

Args:
    box1 (Box): 
    box2 (Box): 

Returns:
    bool:

<a id="unreal.GeometryScript_Box.make_box_from_center_size"></a>

#### make_box_from_center_size

```python
@classmethod
def make_box_from_center_size(cls, center: Vector, dimensions: Vector) -> Box
```

X.make_box_from_center_size(center, dimensions) -> Box
Create a Box from a Center point and X/Y/Z Dimensions (*not* Extents, which are half-dimensions)

Args:
    center (Vector): 
    dimensions (Vector): 

Returns:
    Box:

<a id="unreal.GeometryScript_Box.make_box_from_center_extents"></a>

#### make_box_from_center_extents

```python
@classmethod
def make_box_from_center_extents(cls, center: Vector, extents: Vector) -> Box
```

X.make_box_from_center_extents(center, extents) -> Box
Create a Box from a Center point and X/Y/Z Extents (Extents are half-dimensions)

Args:
    center (Vector): 
    extents (Vector): 

Returns:
    Box:

<a id="unreal.GeometryScript_Box.get_transformed_box"></a>

#### get_transformed_box

```python
@classmethod
def get_transformed_box(cls, box: Box, transform: Transform) -> Box
```

X.get_transformed_box(box, transform) -> Box
Apply the input Transform to the corners of the input Box, and return the new Box containing those points

Args:
    box (Box): 
    transform (Transform): 

Returns:
    Box:

<a id="unreal.GeometryScript_Box.get_expanded_box"></a>

#### get_expanded_box

```python
@classmethod
def get_expanded_box(cls, box: Box, expand_by: Vector) -> Box
```

X.get_expanded_box(box, expand_by) -> Box
Get the input Box expanded by adding the ExpandBy parameter to both the Min and Max.
Dimensions will be clamped to the center point if any of ExpandBy are larger than half the box size

Args:
    box (Box): 
    expand_by (Vector): 

Returns:
    Box:

<a id="unreal.GeometryScript_Box.get_box_volume_area"></a>

#### get_box_volume_area

```python
@classmethod
def get_box_volume_area(cls, box: Box) -> Tuple[float, float]
```

X.get_box_volume_area(box) -> (volume=double, surface_area=double)
Get the Volume and Surface Area of a Box

Args:
    box (Box): 

Returns:
    tuple: 

    volume (double): 

    surface_area (double):

<a id="unreal.GeometryScript_Box.get_box_point_distance"></a>

#### get_box_point_distance

```python
@classmethod
def get_box_point_distance(cls, box: Box, point: Vector) -> float
```

X.get_box_point_distance(box, point) -> double
Calculate the minimum distance between the Box and the Point

Args:
    box (Box): 
    point (Vector): 

Returns:
    double:

<a id="unreal.GeometryScript_Box.get_box_face_center"></a>

#### get_box_face_center

```python
@classmethod
def get_box_face_center(cls, box: Box,
                        face_index: int) -> Tuple[Vector, Vector]
```

X.get_box_face_center(box, face_index) -> (Vector, face_normal=Vector)
Get the position of the center of a face of the Box. Faces are indexed from 0 to 5,
using an ordering where 0/1 are the MinZ/MaxZ faces, 2/3 are MinY/MaxY, and 4/5 are MinX/MaxX

Args:
    box (Box): 
    face_index (int32): 

Returns:
    Vector: 

    face_normal (Vector): returned Normal vector of the identified face

<a id="unreal.GeometryScript_Box.get_box_corner"></a>

#### get_box_corner

```python
@classmethod
def get_box_corner(cls, box: Box, corner_index: int) -> Vector
```

X.get_box_corner(box, corner_index) -> Vector
Get the position of a corner of the Box. Corners are indexed from 0 to 7, using
an ordering where 0 is the Min corner, 1/2/3 are +Z/+Y/+X from the Min corner,
7 is the Max corner, and 4/5/6 are -Z/-Y/-X from the Max corner.

Args:
    box (Box): 
    corner_index (int32): 

Returns:
    Vector:

<a id="unreal.GeometryScript_Box.get_box_center_size"></a>

#### get_box_center_size

```python
@classmethod
def get_box_center_size(cls, box: Box) -> Tuple[Vector, Vector]
```

X.get_box_center_size(box) -> (center=Vector, dimensions=Vector)
Get the Center point and X/Y/Z Dimensions of a Box (full dimensions, not Extents)

Args:
    box (Box): 

Returns:
    tuple: 

    center (Vector): 

    dimensions (Vector):

<a id="unreal.GeometryScript_Box.get_box_box_distance"></a>

#### get_box_box_distance

```python
@classmethod
def get_box_box_distance(cls, box1: Box, box2: Box) -> float
```

X.get_box_box_distance(box1, box2) -> double
Calculate the minimum distance between Box1 and Box2

Args:
    box1 (Box): 
    box2 (Box): 

Returns:
    double:

<a id="unreal.GeometryScript_Box.find_closest_point_on_box"></a>

#### find_closest_point_on_box

```python
@classmethod
def find_closest_point_on_box(cls, box: Box,
                              point: Vector) -> Tuple[Vector, bool]
```

X.find_closest_point_on_box(box, point) -> (Vector, is_inside=bool)
Find the point on the faces of the Box that is closest to the input Point.
If the Point is inside the Box, it is returned, ie points Inside do not project to the Box Faces

Args:
    box (Box): 
    point (Vector): 

Returns:
    bool: 

    is_inside (bool): if the Point is inside the Box, this will return as true, otherwise false

<a id="unreal.GeometryScript_Box.find_box_box_intersection"></a>

#### find_box_box_intersection

```python
@classmethod
def find_box_box_intersection(cls, box1: Box, box2: Box) -> Tuple[Box, bool]
```

X.find_box_box_intersection(box1, box2) -> (Box, is_intersecting=bool)
Find the Box formed by the intersection of Box1 and Box2

Args:
    box1 (Box): 
    box2 (Box): 

Returns:
    bool: 

    is_intersecting (bool): if the boxes do not intersect, this will be returned as false, otherwise true

<a id="unreal.GeometryScript_TextureUtils"></a>