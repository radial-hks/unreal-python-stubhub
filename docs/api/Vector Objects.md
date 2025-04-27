## Vector Objects

```python
class Vector(StructBase)
```

A point or direction FVector in 3d space.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Vector.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``x`` (double):  [Read-Write]
- ``y`` (double):  [Read-Write]
- ``z`` (double):  [Read-Write]

<a id="unreal.Vector.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             z: float = 0.000000) -> None
```

<a id="unreal.Vector.x"></a>

#### x

```python
@property
def x() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector.x"></a>

#### x

```python
@x.setter
def x(value: float) -> None
```

<a id="unreal.Vector.y"></a>

#### y

```python
@property
def y() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector.y"></a>

#### y

```python
@y.setter
def y(value: float) -> None
```

<a id="unreal.Vector.z"></a>

#### z

```python
@property
def z() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector.z"></a>

#### z

```python
@z.setter
def z(value: float) -> None
```

<a id="unreal.Vector.length2d_squared"></a>

#### length2d_squared

```python
def length2d_squared() -> float
```

x.length2d_squared() -> double
Returns the squared length of the vector's XY components.

Returns:
    double:

<a id="unreal.Vector.length2d"></a>

#### length2d

```python
def length2d() -> float
```

x.length2d() -> double
Returns the length of the vector's XY components.

Returns:
    double:

<a id="unreal.Vector.length_squared"></a>

#### length_squared

```python
def length_squared() -> float
```

x.length_squared() -> double
Returns the squared length of the vector

Returns:
    double:

<a id="unreal.Vector.length"></a>

#### length

```python
def length() -> float
```

x.length() -> double
Returns the length of the vector

Returns:
    double:

<a id="unreal.Vector.lerp_to"></a>

#### lerp_to

```python
def lerp_to(b: Vector, alpha: float) -> Vector
```

x.lerp_to(b, alpha) -> Vector
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    b (Vector): 
    alpha (float): 

Returns:
    Vector:

<a id="unreal.Vector.interp_to_constant"></a>

#### interp_to_constant

```python
def interp_to_constant(target: Vector, delta_time: float,
                       interp_speed: float) -> Vector
```

x.interp_to_constant(target, delta_time, interp_speed) -> Vector
Tries to reach Target at a constant rate.

Args:
    target (Vector): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed

Returns:
    Vector: New interpolated position

<a id="unreal.Vector.interp_to"></a>

#### interp_to

```python
def interp_to(target: Vector, delta_time: float,
              interp_speed: float) -> Vector
```

x.interp_to(target, delta_time, interp_speed) -> Vector
Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    target (Vector): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Vector: New interpolated position

<a id="unreal.Vector.interp_spring_to"></a>

#### interp_spring_to

```python
def interp_spring_to(
        target: Vector,
        spring_state: VectorSpringState,
        stiffness: float,
        critical_damping_factor: float,
        delta_time: float,
        mass: float = 1.000000,
        target_velocity_amount: float = 1.000000,
        clamp: bool = False,
        min_value: Vector = [-1.000000, -1.000000, -1.000000],
        max_value: Vector = [1.000000, 1.000000, 1.000000],
        initialize_from_target: bool = False
) -> Tuple[Vector, VectorSpringState]
```

x.interp_spring_to(target, spring_state, stiffness, critical_damping_factor, delta_time, mass=1.000000, target_velocity_amount=1.000000, clamp=False, min_value=[-1.000000, -1.000000, -1.000000], max_value=[1.000000, 1.000000, 1.000000], initialize_from_target=False) -> (Vector, spring_state=VectorSpringState)
Uses a simple spring model to interpolate a vector from Current to Target.

Args:
    target (Vector): Target value
    spring_state (VectorSpringState): Data related to spring model (velocity, error, etc..) - Create a unique variable per spring
    stiffness (float): How stiff the spring model is (more stiffness means more oscillation around the target value)
    critical_damping_factor (float): How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
    delta_time (float): Time difference since the last update
    mass (float): Multiplier that acts like mass on a spring
    target_velocity_amount (float): If 1 then the target velocity will be calculated and used, which results following the target more closely/without lag. Values down to zero (recommended when using this to smooth data) will progressively disable this effect.
    clamp (bool): Whether to use the Min/Max values to clamp the motion
    min_value (Vector): Clamps the minimum output value and cancels the velocity if it reaches this limit
    max_value (Vector): Clamps the maximum output value and cancels the velocity if it reaches this limit
    initialize_from_target (bool): If set then the current value will be set from the target on the first update

Returns:
    VectorSpringState: 

    spring_state (VectorSpringState): Data related to spring model (velocity, error, etc..) - Create a unique variable per spring

<a id="unreal.Vector.unwind_euler"></a>

#### unwind_euler

```python
def unwind_euler() -> None
```

x.unwind_euler() -> None
When this vector contains Euler angles (degrees), ensure that angles are between +/-180

<a id="unreal.Vector.unit_cartesian_to_spherical"></a>

#### unit_cartesian_to_spherical

```python
def unit_cartesian_to_spherical() -> Vector2D
```

x.unit_cartesian_to_spherical() -> Vector2D
Converts a Cartesian unit vector into spherical coordinates on the unit sphere.

Returns:
    Vector2D: Output Theta will be in the range [0, PI], and output Phi will be in the range [-PI, PI].

<a id="unreal.Vector.to_radians"></a>

#### to_radians

```python
def to_radians() -> Vector
```

x.to_radians() -> Vector
Converts a vector containing degree values to a vector containing radian values.

Returns:
    Vector: Vector containing radian values

<a id="unreal.Vector.to_degrees"></a>

#### to_degrees

```python
def to_degrees() -> Vector
```

x.to_degrees() -> Vector
Converts a vector containing radian values to a vector containing degree values.

Returns:
    Vector: Vector  containing degree values

<a id="unreal.Vector.snapped_to_grid"></a>

#### snapped_to_grid

```python
def snapped_to_grid(grid_size: float) -> Vector
```

x.snapped_to_grid(grid_size) -> Vector
Gets a copy of this vector snapped to a grid.

Args:
    grid_size (float): Grid dimension / step.

Returns:
    Vector: A copy of this vector snapped to a grid.

<a id="unreal.Vector.slerp_vectors"></a>

#### slerp_vectors

```python
def slerp_vectors(direction: Vector, alpha: float) -> Vector
```

x.slerp_vectors(direction, alpha) -> Vector
Interpolate from a vector to the direction of another vector along a spherical path.

Args:
    direction (Vector): Target direction we interpolate to
    alpha (double): interpolation amount, usually between 0-1

Returns:
    Vector: Vector after interpolating between Vector and Direction along a spherical path. The magnitude will remain the length of the starting vector.

<a id="unreal.Vector.slerp_normals"></a>

#### slerp_normals

```python
def slerp_normals(normal_b: Vector, alpha: float) -> Vector
```

x.slerp_normals(normal_b, alpha) -> Vector
Interpolate from normalized vector A to normalized vector B along a spherical path.

Args:
    normal_b (Vector): End target direction of interpolation, must be normalized.
    alpha (double): interpolation amount, usually between 0-1

Returns:
    Vector: Vector after interpolating between A and B along a spherical path.

<a id="unreal.Vector.set"></a>

#### set

```python
def set(x: float, y: float, z: float) -> None
```

x.set(x, y, z) -> None
Set the values of the vector directly.

Args:
    x (double): 
    y (double): 
    z (double):

<a id="unreal.Vector.reciprocal"></a>

#### reciprocal

```python
def reciprocal() -> Vector
```

x.reciprocal() -> Vector
Gets the reciprocal of this vector, avoiding division by zero.
Zero components are set to BIG_NUMBER.

Returns:
    Vector: Reciprocal of this vector.

<a id="unreal.Vector.project_on_to_normal"></a>

#### project_on_to_normal

```python
def project_on_to_normal(normal: Vector) -> Vector
```

x.project_on_to_normal(normal) -> Vector
Gets a copy of this vector projected onto the input vector, which is assumed to be unit length.

Args:
    normal (Vector): Vector to project onto (assumed to be unit length).

Returns:
    Vector: Projected vector.

<a id="unreal.Vector.normal_unsafe"></a>

#### normal_unsafe

```python
def normal_unsafe() -> Vector
```

x.normal_unsafe() -> Vector
Calculates normalized unit version of vector without checking for zero length.

Returns:
    Vector: Normalized version of vector.

<a id="unreal.Vector.normalize"></a>

#### normalize

```python
def normalize(tolerance: float = 0.000000) -> None
```

x.normalize(tolerance=0.000000) -> None
Normalize this vector in-place if it is large enough or set it to (0,0,0) otherwise.

Args:
    tolerance (float): Minimum squared length of vector for normalization.

<a id="unreal.Vector.normal2d"></a>

#### normal2d

```python
def normal2d(tolerance: float = 0.000100) -> Vector
```

x.normal2d(tolerance=0.000100) -> Vector
Gets a normalized unit copy of the 2D components of the vector, ensuring it is safe to do so. Z is set to zero.
Returns zero vector if vector length is too small to normalize.

Args:
    tolerance (float): Minimum squared vector length.

Returns:
    Vector: Normalized copy if safe, (0,0,0) otherwise.

<a id="unreal.Vector.mirror_by_plane"></a>

#### mirror_by_plane

```python
def mirror_by_plane(plane: Plane) -> Vector
```

x.mirror_by_plane(plane) -> Vector
Mirrors a vector about a plane.

Args:
    plane (Plane): 

Returns:
    Vector: Mirrored vector.

<a id="unreal.Vector.is_zero"></a>

#### is_zero

```python
def is_zero() -> bool
```

x.is_zero() -> bool
Checks whether all components of the vector are exactly zero.

Returns:
    bool: true if vector is exactly zero, otherwise false.

<a id="unreal.Vector.is_unit"></a>

#### is_unit

```python
def is_unit(squared_lenth_tolerance: float = 0.000100) -> bool
```

x.is_unit(squared_lenth_tolerance=0.000100) -> bool
Determines if vector is normalized / unit (length 1) within specified squared tolerance.

Args:
    squared_lenth_tolerance (float): 

Returns:
    bool: true if unit, false otherwise.

<a id="unreal.Vector.is_uniform"></a>

#### is_uniform

```python
def is_uniform(tolerance: float = 0.000100) -> bool
```

x.is_uniform(tolerance=0.000100) -> bool
Checks whether all components of this vector are the same, within a tolerance.

Args:
    tolerance (float): Error tolerance.

Returns:
    bool: true if the vectors are equal within tolerance limits, false otherwise.

<a id="unreal.Vector.is_normal"></a>

#### is_normal

```python
def is_normal() -> bool
```

x.is_normal() -> bool
Determines if vector is normalized / unit (length 1).

Returns:
    bool: true if normalized, false otherwise.

<a id="unreal.Vector.is_nearly_zero"></a>

#### is_nearly_zero

```python
def is_nearly_zero(tolerance: float = 0.000100) -> bool
```

x.is_nearly_zero(tolerance=0.000100) -> bool
Checks whether vector is near to zero within a specified tolerance.

Args:
    tolerance (float): Error tolerance.

Returns:
    bool: true if vector is in tolerance to zero, otherwise false.

<a id="unreal.Vector.is_nan"></a>

#### is_nan

```python
def is_nan() -> bool
```

x.is_nan() -> bool
Determines if any component is not a number (NAN)

Returns:
    bool: true if one or more components is NAN, otherwise false.

<a id="unreal.Vector.heading_angle"></a>

#### heading_angle

```python
def heading_angle() -> float
```

x.heading_angle() -> double
Convert a direction vector into a 'heading' angle.

Returns:
    double: 'Heading' angle between +/-PI radians. 0 is pointing down +X.

<a id="unreal.Vector.get_sign_vector"></a>

#### get_sign_vector

```python
def get_sign_vector() -> Vector
```

x.get_sign_vector() -> Vector
Get a copy of the vector as sign only.
Each component is set to +1 or -1, with the sign of zero treated as +1.

Returns:
    Vector:

<a id="unreal.Vector.get_projection"></a>

#### get_projection

```python
def get_projection() -> Vector
```

x.get_projection() -> Vector
Projects 2D components of vector based on Z.

Returns:
    Vector: Projected version of vector based on Z.

<a id="unreal.Vector.get_abs_min"></a>

#### get_abs_min

```python
def get_abs_min() -> float
```

x.get_abs_min() -> double
Find the minimum absolute element (abs(X), abs(Y) or abs(Z)) of a vector

Returns:
    double:

<a id="unreal.Vector.get_abs_max"></a>

#### get_abs_max

```python
def get_abs_max() -> float
```

x.get_abs_max() -> double
Find the maximum absolute element (abs(X), abs(Y) or abs(Z)) of a vector

Returns:
    double:

<a id="unreal.Vector.get_abs"></a>

#### get_abs

```python
def get_abs() -> Vector
```

x.get_abs() -> Vector
Get a copy of this vector with absolute value of each component.

Returns:
    Vector: A copy of this vector with absolute value of each component.

<a id="unreal.Vector.distance_squared"></a>

#### distance_squared

```python
def distance_squared(v2: Vector) -> float
```

x.distance_squared(v2) -> double
Squared distance between two points.

Args:
    v2 (Vector): The second point.

Returns:
    double: The squared distance between two points.

<a id="unreal.Vector.distance2d_squared"></a>

#### distance2d_squared

```python
def distance2d_squared(v2: Vector) -> float
```

x.distance2d_squared(v2) -> double
Squared euclidean distance between two points in the XY plane (ignoring Z).

Args:
    v2 (Vector): The second point.

Returns:
    double: The distance between two points in the XY plane.

<a id="unreal.Vector.distance2d"></a>

#### distance2d

```python
def distance2d(v2: Vector) -> float
```

x.distance2d(v2) -> double
Euclidean distance between two points in the XY plane (ignoring Z).

Args:
    v2 (Vector): The second point.

Returns:
    double: The distance between two points in the XY plane.

<a id="unreal.Vector.distance"></a>

#### distance

```python
def distance(v2: Vector) -> float
```

x.distance(v2) -> double
Distance between two points.

Args:
    v2 (Vector): The second point.

Returns:
    double: The distance between two points.

<a id="unreal.Vector.cosine_angle2d"></a>

#### cosine_angle2d

```python
def cosine_angle2d(b: Vector) -> float
```

x.cosine_angle2d(b) -> double
Returns the cosine of the angle between this vector and another projected onto the XY plane (no Z).

Args:
    b (Vector): the other vector to find the 2D cosine of the angle with.

Returns:
    double: The cosine.

<a id="unreal.Vector.get_min"></a>

#### get_min

```python
def get_min(b: Vector) -> Vector
```

x.get_min(b) -> Vector
Find the minimum elements (X, Y and Z) between the two vector's components

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.get_max"></a>

#### get_max

```python
def get_max(b: Vector) -> Vector
```

x.get_max(b) -> Vector
Find the maximum elements (X, Y and Z) between the two vector's components

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.clamped_size_max2d"></a>

#### clamped_size_max2d

```python
def clamped_size_max2d(max: float) -> Vector
```

x.clamped_size_max2d(max) -> Vector
Create a copy of this vector, with the maximum 2D magnitude/size/length clamped to MaxSize. Z is unchanged.

Args:
    max (double): 

Returns:
    Vector:

<a id="unreal.Vector.clamped_size_max"></a>

#### clamped_size_max

```python
def clamped_size_max(max: float) -> Vector
```

x.clamped_size_max(max) -> Vector
Create a copy of this vector, with its maximum magnitude/size/length clamped to MaxSize.

Args:
    max (double): 

Returns:
    Vector:

<a id="unreal.Vector.clamped_size2d"></a>

#### clamped_size2d

```python
def clamped_size2d(min: float, max: float) -> Vector
```

x.clamped_size2d(min, max) -> Vector
Create a copy of this vector, with the 2D magnitude/size/length clamped between Min and Max. Z is unchanged.

Args:
    min (double): 
    max (double): 

Returns:
    Vector:

<a id="unreal.Vector.bounded_to_cube"></a>

#### bounded_to_cube

```python
def bounded_to_cube(radius: float) -> Vector
```

x.bounded_to_cube(radius) -> Vector
Get a copy of this vector, clamped inside of an axis aligned cube centered at the origin.

Args:
    radius (float): Half size of the cube (or radius of sphere circumscribed in the cube).

Returns:
    Vector: A copy of this vector, bound by cube.

<a id="unreal.Vector.bounded_to_box"></a>

#### bounded_to_box

```python
def bounded_to_box(box_min: Vector, box_max: Vector) -> Vector
```

x.bounded_to_box(box_min, box_max) -> Vector
Get a copy of this vector, clamped inside of the specified axis aligned cube.

Args:
    box_min (Vector): 
    box_max (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.assign"></a>

#### assign

```python
def assign(vector: Vector) -> None
```

x.assign(vector) -> None
Assign the values of the supplied vector.

Args:
    vector (Vector): Vector to copy values from.

<a id="unreal.Vector.add_bounded"></a>

#### add_bounded

```python
def add_bounded(add_vect: Vector, radius: float) -> None
```

x.add_bounded(add_vect, radius) -> None
Add a vector to this and clamp the result to an axis aligned cube centered at the origin.

Args:
    add_vect (Vector): Vector to add.
    radius (float): Half size of the cube.

<a id="unreal.Vector.subtract"></a>

#### subtract

```python
def subtract(b: Vector) -> Vector
```

x.subtract(b) -> Vector
Vector subtraction

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.subtract_int"></a>

#### subtract_int

```python
def subtract_int(b: int) -> Vector
```

x.subtract_int(b) -> Vector
Subtracts an integer from each component of a vector

Args:
    b (int32): 

Returns:
    Vector:

<a id="unreal.Vector.subtract_float"></a>

#### subtract_float

```python
def subtract_float(b: float) -> Vector
```

x.subtract_float(b) -> Vector
Subtracts a float from each component of a vector

Args:
    b (double): 

Returns:
    Vector:

<a id="unreal.Vector.rotator_from_axis_and_angle"></a>

#### rotator_from_axis_and_angle

```python
def rotator_from_axis_and_angle(angle: float) -> Rotator
```

x.rotator_from_axis_and_angle(angle) -> Rotator
Create a rotation from an axis and supplied angle (in degrees)

Args:
    angle (float): 

Returns:
    Rotator:

<a id="unreal.Vector.rotate_angle_axis"></a>

#### rotate_angle_axis

```python
def rotate_angle_axis(angle_deg: float, axis: Vector) -> Vector
```

x.rotate_angle_axis(angle_deg, axis) -> Vector
Returns result of vector A rotated by AngleDeg around Axis

Args:
    angle_deg (float): 
    axis (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.random_point_in_box_extents"></a>

#### random_point_in_box_extents

```python
def random_point_in_box_extents(half_size: Vector) -> Vector
```

x.random_point_in_box_extents(half_size) -> Vector
Returns a random point within the specified bounding box using the first vector as an origin and the second as the box extents.

Args:
    half_size (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.find_quat_between_vectors"></a>

#### find_quat_between_vectors

```python
def find_quat_between_vectors(end: Vector) -> Quat
```

x.find_quat_between_vectors(end) -> Quat
Generates the 'smallest' (geodesic) rotation around a sphere between two vectors of arbitrary length.

Args:
    end (Vector): Vector the rotation ends at

Returns:
    Quat: Quat that will rotate from Start to End

<a id="unreal.Vector.find_quat_between_normals"></a>

#### find_quat_between_normals

```python
def find_quat_between_normals(end_normal: Vector) -> Quat
```

x.find_quat_between_normals(end_normal) -> Quat
Generates the 'smallest' (geodesic) rotation around a sphere between two normals (assumed to be unit length).

Args:
    end_normal (Vector): 

Returns:
    Quat: Quat that will rotate from Start to End

<a id="unreal.Vector.project_on_to"></a>

#### project_on_to

```python
def project_on_to(target: Vector) -> Vector
```

x.project_on_to(target) -> Vector
Projects one vector (V) onto another (Target) and returns the projected vector.
If Target is nearly zero in length, returns the zero vector.

Args:
    target (Vector): Vector on which we are projecting.

Returns:
    Vector: V projected on to Target.

<a id="unreal.Vector.project_on_to_plane"></a>

#### project_on_to_plane

```python
def project_on_to_plane(plane_normal: Vector) -> Vector
```

x.project_on_to_plane(plane_normal) -> Vector
Projects a vector onto a plane defined by a normalized vector (PlaneNormal).

Args:
    plane_normal (Vector): Normal of the plane.

Returns:
    Vector: Vector projected onto the plane.

<a id="unreal.Vector.project_point_on_to_plane"></a>

#### project_point_on_to_plane

```python
def project_point_on_to_plane(plane_base: Vector,
                              plane_normal: Vector) -> Vector
```

x.project_point_on_to_plane(plane_base, plane_normal) -> Vector
Projects/snaps a point onto a plane defined by a point on the plane and a plane normal.

Args:
    plane_base (Vector): A point on the plane.
    plane_normal (Vector): Normal of the plane.

Returns:
    Vector: Point projected onto the plane.

<a id="unreal.Vector.not_equal"></a>

#### not_equal

```python
def not_equal(b: Vector) -> bool
```

x.not_equal(b) -> bool
Returns true if vector A is not equal to vector B (A != B)

Args:
    b (Vector): 

Returns:
    bool:

<a id="unreal.Vector.is_not_near_equal"></a>

#### is_not_near_equal

```python
def is_not_near_equal(b: Vector, error_tolerance: float = 0.000100) -> bool
```

x.is_not_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Args:
    b (Vector): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Vector.normal"></a>

#### normal

```python
def normal(tolerance: float = 0.000100) -> Vector
```

x.normal(tolerance=0.000100) -> Vector
Gets a normalized unit copy of the vector, ensuring it is safe to do so based on the length.
Returns zero vector if vector length is too small to safely normalize.

Args:
    tolerance (float): Minimum squared vector length.

Returns:
    Vector: A normalized copy if safe, (0,0,0) otherwise.

<a id="unreal.Vector.negated"></a>

#### negated

```python
def negated() -> Vector
```

x.negated() -> Vector
Negate a vector.

Returns:
    Vector:

<a id="unreal.Vector.multiply"></a>

#### multiply

```python
def multiply(b: Vector) -> Vector
```

x.multiply(b) -> Vector
Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z})

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.multiply_int"></a>

#### multiply_int

```python
def multiply_int(b: int) -> Vector
```

x.multiply_int(b) -> Vector
Scales Vector A by B

Args:
    b (int32): 

Returns:
    Vector:

<a id="unreal.Vector.multiply_float"></a>

#### multiply_float

```python
def multiply_float(b: float) -> Vector
```

x.multiply_float(b) -> Vector
Scales Vector A by B

Args:
    b (double): 

Returns:
    Vector:

<a id="unreal.Vector.unrotate"></a>

#### unrotate

```python
def unrotate(b: Rotator) -> Vector
```

x.unrotate(b) -> Vector
Returns result of vector A rotated by the inverse of Rotator B

Args:
    b (Rotator): 

Returns:
    Vector:

<a id="unreal.Vector.rotate"></a>

#### rotate

```python
def rotate(b: Rotator) -> Vector
```

x.rotate(b) -> Vector
Returns result of vector A rotated by Rotator B

Args:
    b (Rotator): 

Returns:
    Vector:

<a id="unreal.Vector.mirror_by_vector"></a>

#### mirror_by_vector

```python
def mirror_by_vector(surface_normal: Vector) -> Vector
```

x.mirror_by_vector(surface_normal) -> Vector
Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
Produces a result like shining a laser at a mirror!

Args:
    surface_normal (Vector): A normal of the surface the ray should be reflected on.

Returns:
    Vector: Reflected vector.

<a id="unreal.Vector.get_min_element"></a>

#### get_min_element

```python
def get_min_element() -> float
```

x.get_min_element() -> double
Find the minimum element (X, Y or Z) of a vector

Returns:
    double:

<a id="unreal.Vector.get_max_element"></a>

#### get_max_element

```python
def get_max_element() -> float
```

x.get_max_element() -> double
Find the maximum element (X, Y or Z) of a vector

Returns:
    double:

<a id="unreal.Vector.direction_unit_to"></a>

#### direction_unit_to

```python
def direction_unit_to(to: Vector) -> Vector
```

x.direction_unit_to(to) -> Vector
Find the unit direction vector from one position to another or (0,0,0) if positions are the same.

Args:
    to (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.truncated"></a>

#### truncated

```python
def truncated() -> IntVector
```

x.truncated() -> IntVector
Rounds A to an integer with truncation towards zero for each element in a vector.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

Returns:
    IntVector:

<a id="unreal.Vector.equals"></a>

#### equals

```python
def equals(b: Vector) -> bool
```

x.equals(b) -> bool
Returns true if vector A is equal to vector B (A == B)

Args:
    b (Vector): 

Returns:
    bool:

<a id="unreal.Vector.is_near_equal"></a>

#### is_near_equal

```python
def is_near_equal(b: Vector, error_tolerance: float = 0.000100) -> bool
```

x.is_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

Args:
    b (Vector): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Vector.dot"></a>

#### dot

```python
def dot(b: Vector) -> float
```

x.dot(b) -> double
Returns the dot product of two 3d vectors - see http://mathworld.wolfram.com/DotProduct.html

Args:
    b (Vector): 

Returns:
    double:

<a id="unreal.Vector.divide"></a>

#### divide

```python
def divide(b: Vector = [1.000000, 1.000000, 1.000000]) -> Vector
```

x.divide(b=[1.000000, 1.000000, 1.000000]) -> Vector
Element-wise Vector division (Result = {A.x/B.x, A.y/B.y, A.z/B.z})

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.divide_int"></a>

#### divide_int

```python
def divide_int(b: int = 1) -> Vector
```

x.divide_int(b=1) -> Vector
Vector divide by an integer

Args:
    b (int32): 

Returns:
    Vector:

<a id="unreal.Vector.divide_float"></a>

#### divide_float

```python
def divide_float(b: float = 1.000000) -> Vector
```

x.divide_float(b=1.000000) -> Vector
Vector divide by a float

Args:
    b (double): 

Returns:
    Vector:

<a id="unreal.Vector.cross"></a>

#### cross

```python
def cross(b: Vector) -> Vector
```

x.cross(b) -> Vector
Returns the cross product of two 3d vectors - see http://mathworld.wolfram.com/CrossProduct.html

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.vector2d"></a>

#### vector2d

```python
def vector2d() -> Vector2D
```

x.vector2d() -> Vector2D
Converts a Vector to a Vector2D using the Vector's (X, Y) coordinates

Returns:
    Vector2D:

<a id="unreal.Vector.transform"></a>

#### transform

```python
def transform() -> Transform
```

x.transform() -> Transform
Converts a vector to a transform. Uses vector as location

Returns:
    Transform:

<a id="unreal.Vector.rotator"></a>

#### rotator

```python
def rotator() -> Rotator
```

x.rotator() -> Rotator
Return the FRotator orientation corresponding to the direction in which the vector points.
Sets Yaw and Pitch to the proper numbers, and sets Roll to zero because the roll can't be determined from a vector.

Returns:
    Rotator: FRotator from the Vector's direction, without any roll.

<a id="unreal.Vector.quaternion"></a>

#### quaternion

```python
def quaternion() -> Quat
```

x.quaternion() -> Quat
Return the Quaternion orientation corresponding to the direction in which the vector points.
Similar to the FRotator version, returns a result without roll such that it preserves the up vector.
note: If you don't care about preserving the up vector and just want the most direct rotation, you can use the faster 'FindBetweenVectors(ForwardVector, YourVector)' or 'FindBetweenNormals(...)' if you know the vector is of unit length.

Returns:
    Quat: Quaternion from the Vector's direction, without any roll.

<a id="unreal.Vector.linear_color"></a>

#### linear_color

```python
def linear_color() -> LinearColor
```

x.linear_color() -> LinearColor
Converts a vector to LinearColor

Returns:
    LinearColor:

<a id="unreal.Vector.clamped_size"></a>

#### clamped_size

```python
def clamped_size(min: float, max: float) -> Vector
```

x.clamped_size(min, max) -> Vector
Create a copy of this vector, with its magnitude/size/length clamped between Min and Max.

Args:
    min (double): 
    max (double): 

Returns:
    Vector:

<a id="unreal.Vector.add"></a>

#### add

```python
def add(b: Vector) -> Vector
```

x.add(b) -> Vector
Vector addition

Args:
    b (Vector): 

Returns:
    Vector:

<a id="unreal.Vector.add_int"></a>

#### add_int

```python
def add_int(b: int) -> Vector
```

x.add_int(b) -> Vector
Adds an integer to each component of a vector

Args:
    b (int32): 

Returns:
    Vector:

<a id="unreal.Vector.add_float"></a>

#### add_float

```python
def add_float(b: float) -> Vector
```

x.add_float(b) -> Vector
Adds a float to each component of a vector

Args:
    b (double): 

Returns:
    Vector:

<a id="unreal.Vector.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Vector`` Returns true if vector A is equal to vector B (A == B)

<a id="unreal.Vector.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``Vector`` Returns true if vector A is not equal to vector B (A != B)

<a id="unreal.Vector.__add__"></a>

#### __add__

```python
def __add__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Vector addition

<a id="unreal.Vector.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Vector addition

<a id="unreal.Vector.__sub__"></a>

#### __sub__

```python
def __sub__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Vector subtraction

<a id="unreal.Vector.__isub__"></a>

#### __isub__

```python
def __isub__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Vector subtraction

<a id="unreal.Vector.__mul__"></a>

#### __mul__

```python
def __mul__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z})
- ``double`` Scales Vector A by B

<a id="unreal.Vector.__imul__"></a>

#### __imul__

```python
def __imul__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z})
- ``double`` Scales Vector A by B

<a id="unreal.Vector.__truediv__"></a>

#### __truediv__

```python
def __truediv__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Element-wise Vector division (Result = {A.x/B.x, A.y/B.y, A.z/B.z})
- ``double`` Vector divide by a float

<a id="unreal.Vector.__or__"></a>

#### __or__

```python
def __or__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Returns the dot product of two 3d vectors - see http://mathworld.wolfram.com/DotProduct.html

<a id="unreal.Vector.__xor__"></a>

#### __xor__

```python
def __xor__(other: Vector) -> None
```

**Overloads:**

- ``Vector`` Returns the cross product of two 3d vectors - see http://mathworld.wolfram.com/CrossProduct.html

<a id="unreal.Vector.__neg__"></a>

#### __neg__

```python
def __neg__() -> None
```

Negate a vector.

<a id="unreal.Vector.ZERO"></a>

#### ZERO

(Vector): 3D vector zero constant (0,0,0)

<a id="unreal.Vector.UP"></a>

#### UP

(Vector): 3D vector Unreal up direction constant (0,0,1)

<a id="unreal.Vector.RIGHT"></a>

#### RIGHT

(Vector): 3D vector Unreal right direction constant (0,1,0)

<a id="unreal.Vector.ONE"></a>

#### ONE

(Vector): 3D vector one constant (1,1,1)

<a id="unreal.Vector.LEFT"></a>

#### LEFT

(Vector): 3D vector Unreal left direction constant (0,-1,0)

<a id="unreal.Vector.FORWARD"></a>

#### FORWARD

(Vector): 3D vector Unreal forward direction constant (1,0,0)

<a id="unreal.Vector.DOWN"></a>

#### DOWN

(Vector): 3D vector Unreal down direction constant (0,0,-1)

<a id="unreal.Vector.BACKWARD"></a>

#### BACKWARD

(Vector): 3D vector Unreal backward direction constant (-1,0,0)

<a id="unreal.Box2D"></a>