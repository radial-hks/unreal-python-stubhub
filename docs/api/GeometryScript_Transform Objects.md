## GeometryScript_Transform Objects

```python
class GeometryScript_Transform(BlueprintFunctionLibrary)
```

Geometry Script Library Transform Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: ShapeFunctions.h

<a id="unreal.GeometryScript_Transform.make_transform_from_z_axis"></a>

#### make_transform_from_z_axis

```python
@classmethod
def make_transform_from_z_axis(cls, location: Vector,
                               z_axis: Vector) -> Transform
```

X.make_transform_from_z_axis(location, z_axis) -> Transform
Create a Transform at the given Location, with the ZAxis vector as the Z axis of the Transform.

Args:
    location (Vector): 
    z_axis (Vector): 

Returns:
    Transform:

<a id="unreal.GeometryScript_Transform.make_transform_from_axes"></a>

#### make_transform_from_axes

```python
@classmethod
def make_transform_from_axes(cls,
                             location: Vector,
                             z_axis: Vector,
                             tangent_axis: Vector,
                             tangent_is_x: bool = True) -> Transform
```

X.make_transform_from_axes(location, z_axis, tangent_axis, tangent_is_x=True) -> Transform
Create a Transform at the given Location, with the ZAxis vector as the Z axis
of the Transform, and the X or Y axis oriented to the Tangent vector, based on
the bTangentIsX parameter.

Args:
    location (Vector): 
    z_axis (Vector): 
    tangent_axis (Vector): 
    tangent_is_x (bool): 

Returns:
    Transform:

<a id="unreal.GeometryScript_Transform.get_transform_axis_vector"></a>

#### get_transform_axis_vector

```python
@classmethod
def get_transform_axis_vector(
        cls,
        transform: Transform,
        axis: GeometryScriptAxis = GeometryScriptAxis.X) -> Vector
```

X.get_transform_axis_vector(transform, axis=GeometryScriptAxis.X) -> Vector
Get the Vector for the direction of the X/Y/Z axis of the Transform, ie the
Vector resulting from transforming the unit direction vectors (1,0,0) / etc

Args:
    transform (Transform): 
    axis (GeometryScriptAxis): 

Returns:
    Vector:

<a id="unreal.GeometryScript_Transform.get_transform_axis_ray"></a>

#### get_transform_axis_ray

```python
@classmethod
def get_transform_axis_ray(
        cls,
        transform: Transform,
        axis: GeometryScriptAxis = GeometryScriptAxis.X) -> Ray
```

X.get_transform_axis_ray(transform, axis=GeometryScriptAxis.X) -> Ray
Get the Ray at the Transform Location aligned with the direction of the X/Y/Z axis of the Transform,
ie the Direction Vector resulting from transforming the unit direction vectors (1,0,0) / etc

Args:
    transform (Transform): 
    axis (GeometryScriptAxis): 

Returns:
    Ray:

<a id="unreal.GeometryScript_Transform.get_transform_axis_plane"></a>

#### get_transform_axis_plane

```python
@classmethod
def get_transform_axis_plane(
        cls,
        transform: Transform,
        axis: GeometryScriptAxis = GeometryScriptAxis.X) -> Plane
```

X.get_transform_axis_plane(transform, axis=GeometryScriptAxis.X) -> Plane
Get the Plane at the Transform Location with the Plane Normal aligned with the direction of the X/Y/Z axis of the Transform,
ie the Direction Vector resulting from transforming the unit direction vectors (1,0,0) / etc

Args:
    transform (Transform): 
    axis (GeometryScriptAxis): 

Returns:
    Plane:

<a id="unreal.GeometryScript_Ray"></a>