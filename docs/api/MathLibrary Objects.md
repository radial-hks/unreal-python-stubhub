## MathLibrary Objects

```python
class MathLibrary(BlueprintFunctionLibrary)
```

Kismet Math Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetMathLibrary.h

<a id="unreal.MathLibrary.xor_int_int"></a>

#### xor_int_int

```python
@classmethod
def xor_int_int(cls, a: int, b: int) -> int
```

X.xor_int_int(a, b) -> int32
Bitwise XOR (A ^ B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.xor_int64_int64"></a>

#### xor_int64_int64

```python
@classmethod
def xor_int64_int64(cls, a: int, b: int) -> int
```

X.xor_int64_int64(a, b) -> int64
Bitwise XOR (A ^ B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.wrap"></a>

#### wrap

```python
@classmethod
def wrap(cls, value: int, min: int = 0, max: int = 100) -> int
```

X.wrap(value, min=0, max=100) -> int32
Returns Value between A and B (inclusive) that wraps around

Args:
    value (int32): 
    min (int32): 
    max (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.weighted_moving_average_f_vector"></a>

#### weighted_moving_average_f_vector

```python
@classmethod
def weighted_moving_average_f_vector(cls, current_sample: Vector,
                                     previous_sample: Vector,
                                     weight: float) -> Vector
```

X.weighted_moving_average_f_vector(current_sample, previous_sample, weight) -> Vector
Calculates the new value in a weighted moving average series using the previous value and the weight

Args:
    current_sample (Vector): The value to blend with the previous sample to get a new weighted value
    previous_sample (Vector): The last value from the series
    weight (float): The weight to blend with

Returns:
    Vector: the next value in the series

<a id="unreal.MathLibrary.weighted_moving_average_f_rotator"></a>

#### weighted_moving_average_f_rotator

```python
@classmethod
def weighted_moving_average_f_rotator(cls, current_sample: Rotator,
                                      previous_sample: Rotator,
                                      weight: float) -> Rotator
```

X.weighted_moving_average_f_rotator(current_sample, previous_sample, weight) -> Rotator
Calculates the new value in a weighted moving average series using the previous value and the weight

Args:
    current_sample (Rotator): The value to blend with the previous sample to get a new weighted value
    previous_sample (Rotator): The last value from the series
    weight (float): The weight to blend with

Returns:
    Rotator: the next value in the series

<a id="unreal.MathLibrary.weighted_moving_average_float"></a>

#### weighted_moving_average_float

```python
@classmethod
def weighted_moving_average_float(cls, current_sample: float,
                                  previous_sample: float,
                                  weight: float) -> float
```

X.weighted_moving_average_float(current_sample, previous_sample, weight) -> float
Calculates the new value in a weighted moving average series using the previous value and the weight

Args:
    current_sample (float): The value to blend with the previous sample to get a new weighted value
    previous_sample (float): The last value from the series
    weight (float): The weight to blend with

Returns:
    float: the next value in the series

<a id="unreal.MathLibrary.v_size_xy_squared"></a>

#### v_size_xy_squared

```python
@classmethod
def v_size_xy_squared(cls, a: Vector) -> float
```

X.v_size_xy_squared(a) -> double
Returns the squared length of the vector's XY components.

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.v_size_xy"></a>

#### v_size_xy

```python
@classmethod
def v_size_xy(cls, a: Vector) -> float
```

X.v_size_xy(a) -> double
Returns the length of the vector's XY components.

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.v_size_squared"></a>

#### v_size_squared

```python
@classmethod
def v_size_squared(cls, a: Vector) -> float
```

X.v_size_squared(a) -> double
Returns the squared length of the vector

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.v_size2d_squared"></a>

#### v_size2d_squared

```python
@classmethod
def v_size2d_squared(cls, a: Vector2D) -> float
```

X.v_size2d_squared(a) -> double
Returns the squared length of a 2D Vector.

Args:
    a (Vector2D): 

Returns:
    double:

<a id="unreal.MathLibrary.v_size2d"></a>

#### v_size2d

```python
@classmethod
def v_size2d(cls, a: Vector2D) -> float
```

X.v_size2d(a) -> double
Returns the length of a 2D Vector.

Args:
    a (Vector2D): 

Returns:
    double:

<a id="unreal.MathLibrary.v_size"></a>

#### v_size

```python
@classmethod
def v_size(cls, a: Vector) -> float
```

X.v_size(a) -> double
Returns the length of the vector

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.v_lerp"></a>

#### v_lerp

```python
@classmethod
def v_lerp(cls, a: Vector, b: Vector, alpha: float) -> Vector
```

X.v_lerp(a, b, alpha) -> Vector
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    a (Vector): 
    b (Vector): 
    alpha (float): 

Returns:
    Vector:

<a id="unreal.MathLibrary.v_interp_to_constant"></a>

#### v_interp_to_constant

```python
@classmethod
def v_interp_to_constant(cls, current: Vector, target: Vector,
                         delta_time: float, interp_speed: float) -> Vector
```

X.v_interp_to_constant(current, target, delta_time, interp_speed) -> Vector
Tries to reach Target at a constant rate.

Args:
    current (Vector): Actual position
    target (Vector): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed

Returns:
    Vector: New interpolated position

<a id="unreal.MathLibrary.v_interp_to"></a>

#### v_interp_to

```python
@classmethod
def v_interp_to(cls, current: Vector, target: Vector, delta_time: float,
                interp_speed: float) -> Vector
```

X.v_interp_to(current, target, delta_time, interp_speed) -> Vector
Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    current (Vector): Actual position
    target (Vector): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Vector: New interpolated position

<a id="unreal.MathLibrary.vector_spring_interp"></a>

#### vector_spring_interp

```python
@classmethod
def vector_spring_interp(
        cls,
        current: Vector,
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

X.vector_spring_interp(current, target, spring_state, stiffness, critical_damping_factor, delta_time, mass=1.000000, target_velocity_amount=1.000000, clamp=False, min_value=[-1.000000, -1.000000, -1.000000], max_value=[1.000000, 1.000000, 1.000000], initialize_from_target=False) -> (Vector, spring_state=VectorSpringState)
Uses a simple spring model to interpolate a vector from Current to Target.

Args:
    current (Vector): Current value
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

<a id="unreal.MathLibrary.vector_unwind_euler"></a>

#### vector_unwind_euler

```python
@classmethod
def vector_unwind_euler(cls, a: Vector) -> Vector
```

X.vector_unwind_euler(a) -> Vector
When this vector contains Euler angles (degrees), ensure that angles are between +/-180

Args:
    a (Vector): 

Returns:
    Vector: 

    a (Vector):

<a id="unreal.MathLibrary.vector_unit_cartesian_to_spherical"></a>

#### vector_unit_cartesian_to_spherical

```python
@classmethod
def vector_unit_cartesian_to_spherical(cls, a: Vector) -> Vector2D
```

X.vector_unit_cartesian_to_spherical(a) -> Vector2D
Converts a Cartesian unit vector into spherical coordinates on the unit sphere.

Args:
    a (Vector): 

Returns:
    Vector2D: Output Theta will be in the range [0, PI], and output Phi will be in the range [-PI, PI].

<a id="unreal.MathLibrary.vector_to_radians"></a>

#### vector_to_radians

```python
@classmethod
def vector_to_radians(cls, a: Vector) -> Vector
```

X.vector_to_radians(a) -> Vector
Converts a vector containing degree values to a vector containing radian values.

Args:
    a (Vector): 

Returns:
    Vector: Vector containing radian values

<a id="unreal.MathLibrary.vector_to_degrees"></a>

#### vector_to_degrees

```python
@classmethod
def vector_to_degrees(cls, a: Vector) -> Vector
```

X.vector_to_degrees(a) -> Vector
Converts a vector containing radian values to a vector containing degree values.

Args:
    a (Vector): 

Returns:
    Vector: Vector  containing degree values

<a id="unreal.MathLibrary.vector_snapped_to_grid"></a>

#### vector_snapped_to_grid

```python
@classmethod
def vector_snapped_to_grid(cls, vect: Vector, grid_size: float) -> Vector
```

X.vector_snapped_to_grid(vect, grid_size) -> Vector
Gets a copy of this vector snapped to a grid.

Args:
    vect (Vector): 
    grid_size (float): Grid dimension / step.

Returns:
    Vector: A copy of this vector snapped to a grid.

<a id="unreal.MathLibrary.vector_slerp_vector_to_direction"></a>

#### vector_slerp_vector_to_direction

```python
@classmethod
def vector_slerp_vector_to_direction(cls, vector: Vector, direction: Vector,
                                     alpha: float) -> Vector
```

X.vector_slerp_vector_to_direction(vector, direction, alpha) -> Vector
Interpolate from a vector to the direction of another vector along a spherical path.

Args:
    vector (Vector): Vector we interpolate from
    direction (Vector): Target direction we interpolate to
    alpha (double): interpolation amount, usually between 0-1

Returns:
    Vector: Vector after interpolating between Vector and Direction along a spherical path. The magnitude will remain the length of the starting vector.

<a id="unreal.MathLibrary.vector_slerp_normals"></a>

#### vector_slerp_normals

```python
@classmethod
def vector_slerp_normals(cls, normal_a: Vector, normal_b: Vector,
                         alpha: float) -> Vector
```

X.vector_slerp_normals(normal_a, normal_b, alpha) -> Vector
Interpolate from normalized vector A to normalized vector B along a spherical path.

Args:
    normal_a (Vector): Start direction of interpolation, must be normalized.
    normal_b (Vector): End target direction of interpolation, must be normalized.
    alpha (double): interpolation amount, usually between 0-1

Returns:
    Vector: Vector after interpolating between A and B along a spherical path.

<a id="unreal.MathLibrary.vector_set"></a>

#### vector_set

```python
@classmethod
def vector_set(cls, a: Vector, x: float, y: float, z: float) -> Vector
```

X.vector_set(a, x, y, z) -> Vector
Set the values of the vector directly.

Args:
    a (Vector): 
    x (double): 
    y (double): 
    z (double): 

Returns:
    Vector: 

    a (Vector):

<a id="unreal.MathLibrary.vector_reciprocal"></a>

#### vector_reciprocal

```python
@classmethod
def vector_reciprocal(cls, a: Vector) -> Vector
```

X.vector_reciprocal(a) -> Vector
Gets the reciprocal of this vector, avoiding division by zero.
Zero components are set to BIG_NUMBER.

Args:
    a (Vector): 

Returns:
    Vector: Reciprocal of this vector.

<a id="unreal.MathLibrary.vector_project_on_to_normal"></a>

#### vector_project_on_to_normal

```python
@classmethod
def vector_project_on_to_normal(cls, v: Vector, normal: Vector) -> Vector
```

X.vector_project_on_to_normal(v, normal) -> Vector
Gets a copy of this vector projected onto the input vector, which is assumed to be unit length.

Args:
    v (Vector): 
    normal (Vector): Vector to project onto (assumed to be unit length).

Returns:
    Vector: Projected vector.

<a id="unreal.MathLibrary.vector_normal_unsafe"></a>

#### vector_normal_unsafe

```python
@classmethod
def vector_normal_unsafe(cls, a: Vector) -> Vector
```

X.vector_normal_unsafe(a) -> Vector
Calculates normalized unit version of vector without checking for zero length.

Args:
    a (Vector): 

Returns:
    Vector: Normalized version of vector.

<a id="unreal.MathLibrary.vector_normalize"></a>

#### vector_normalize

```python
@classmethod
def vector_normalize(cls, a: Vector, tolerance: float = 0.000000) -> Vector
```

X.vector_normalize(a, tolerance=0.000000) -> Vector
Normalize this vector in-place if it is large enough or set it to (0,0,0) otherwise.

Args:
    a (Vector): 
    tolerance (float): Minimum squared length of vector for normalization.

Returns:
    Vector: 

    a (Vector):

<a id="unreal.MathLibrary.vector_normal2d"></a>

#### vector_normal2d

```python
@classmethod
def vector_normal2d(cls, a: Vector, tolerance: float = 0.000100) -> Vector
```

X.vector_normal2d(a, tolerance=0.000100) -> Vector
Gets a normalized unit copy of the 2D components of the vector, ensuring it is safe to do so. Z is set to zero.
Returns zero vector if vector length is too small to normalize.

Args:
    a (Vector): 
    tolerance (float): Minimum squared vector length.

Returns:
    Vector: Normalized copy if safe, (0,0,0) otherwise.

<a id="unreal.MathLibrary.vector_mirror_by_plane"></a>

#### vector_mirror_by_plane

```python
@classmethod
def vector_mirror_by_plane(cls, a: Vector, plane: Plane) -> Vector
```

X.vector_mirror_by_plane(a, plane) -> Vector
Mirrors a vector about a plane.

Args:
    a (Vector): 
    plane (Plane): 

Returns:
    Vector: Mirrored vector.

<a id="unreal.MathLibrary.vector_is_zero"></a>

#### vector_is_zero

```python
@classmethod
def vector_is_zero(cls, a: Vector) -> bool
```

X.vector_is_zero(a) -> bool
Checks whether all components of the vector are exactly zero.

Args:
    a (Vector): 

Returns:
    bool: true if vector is exactly zero, otherwise false.

<a id="unreal.MathLibrary.vector_is_unit"></a>

#### vector_is_unit

```python
@classmethod
def vector_is_unit(cls,
                   a: Vector,
                   squared_lenth_tolerance: float = 0.000100) -> bool
```

X.vector_is_unit(a, squared_lenth_tolerance=0.000100) -> bool
Determines if vector is normalized / unit (length 1) within specified squared tolerance.

Args:
    a (Vector): 
    squared_lenth_tolerance (float): 

Returns:
    bool: true if unit, false otherwise.

<a id="unreal.MathLibrary.vector_is_uniform"></a>

#### vector_is_uniform

```python
@classmethod
def vector_is_uniform(cls, a: Vector, tolerance: float = 0.000100) -> bool
```

X.vector_is_uniform(a, tolerance=0.000100) -> bool
Checks whether all components of this vector are the same, within a tolerance.

Args:
    a (Vector): 
    tolerance (float): Error tolerance.

Returns:
    bool: true if the vectors are equal within tolerance limits, false otherwise.

<a id="unreal.MathLibrary.vector_is_normal"></a>

#### vector_is_normal

```python
@classmethod
def vector_is_normal(cls, a: Vector) -> bool
```

X.vector_is_normal(a) -> bool
Determines if vector is normalized / unit (length 1).

Args:
    a (Vector): 

Returns:
    bool: true if normalized, false otherwise.

<a id="unreal.MathLibrary.vector_is_nearly_zero"></a>

#### vector_is_nearly_zero

```python
@classmethod
def vector_is_nearly_zero(cls, a: Vector, tolerance: float = 0.000100) -> bool
```

X.vector_is_nearly_zero(a, tolerance=0.000100) -> bool
Checks whether vector is near to zero within a specified tolerance.

Args:
    a (Vector): 
    tolerance (float): Error tolerance.

Returns:
    bool: true if vector is in tolerance to zero, otherwise false.

<a id="unreal.MathLibrary.vector_is_nan"></a>

#### vector_is_nan

```python
@classmethod
def vector_is_nan(cls, a: Vector) -> bool
```

X.vector_is_nan(a) -> bool
Determines if any component is not a number (NAN)

Args:
    a (Vector): 

Returns:
    bool: true if one or more components is NAN, otherwise false.

<a id="unreal.MathLibrary.vector_heading_angle"></a>

#### vector_heading_angle

```python
@classmethod
def vector_heading_angle(cls, a: Vector) -> float
```

X.vector_heading_angle(a) -> double
Convert a direction vector into a 'heading' angle.

Args:
    a (Vector): 

Returns:
    double: 'Heading' angle between +/-PI radians. 0 is pointing down +X.

<a id="unreal.MathLibrary.vector_get_sign_vector"></a>

#### vector_get_sign_vector

```python
@classmethod
def vector_get_sign_vector(cls, a: Vector) -> Vector
```

X.vector_get_sign_vector(a) -> Vector
Get a copy of the vector as sign only.
Each component is set to +1 or -1, with the sign of zero treated as +1.

Args:
    a (Vector): copy of the vector with each component set to +1 or -1

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_get_projection"></a>

#### vector_get_projection

```python
@classmethod
def vector_get_projection(cls, a: Vector) -> Vector
```

X.vector_get_projection(a) -> Vector
Projects 2D components of vector based on Z.

Args:
    a (Vector): 

Returns:
    Vector: Projected version of vector based on Z.

<a id="unreal.MathLibrary.vector_get_abs_min"></a>

#### vector_get_abs_min

```python
@classmethod
def vector_get_abs_min(cls, a: Vector) -> float
```

X.vector_get_abs_min(a) -> double
Find the minimum absolute element (abs(X), abs(Y) or abs(Z)) of a vector

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.vector_get_abs_max"></a>

#### vector_get_abs_max

```python
@classmethod
def vector_get_abs_max(cls, a: Vector) -> float
```

X.vector_get_abs_max(a) -> double
Find the maximum absolute element (abs(X), abs(Y) or abs(Z)) of a vector

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.vector_get_abs"></a>

#### vector_get_abs

```python
@classmethod
def vector_get_abs(cls, a: Vector) -> Vector
```

X.vector_get_abs(a) -> Vector
Get a copy of this vector with absolute value of each component.

Args:
    a (Vector): 

Returns:
    Vector: A copy of this vector with absolute value of each component.

<a id="unreal.MathLibrary.vector_distance_squared"></a>

#### vector_distance_squared

```python
@classmethod
def vector_distance_squared(cls, v1: Vector, v2: Vector) -> float
```

X.vector_distance_squared(v1, v2) -> double
Squared distance between two points.

Args:
    v1 (Vector): The first point.
    v2 (Vector): The second point.

Returns:
    double: The squared distance between two points.

<a id="unreal.MathLibrary.vector_distance2d_squared"></a>

#### vector_distance2d_squared

```python
@classmethod
def vector_distance2d_squared(cls, v1: Vector, v2: Vector) -> float
```

X.vector_distance2d_squared(v1, v2) -> double
Squared euclidean distance between two points in the XY plane (ignoring Z).

Args:
    v1 (Vector): The first point.
    v2 (Vector): The second point.

Returns:
    double: The distance between two points in the XY plane.

<a id="unreal.MathLibrary.vector_distance2d"></a>

#### vector_distance2d

```python
@classmethod
def vector_distance2d(cls, v1: Vector, v2: Vector) -> float
```

X.vector_distance2d(v1, v2) -> double
Euclidean distance between two points in the XY plane (ignoring Z).

Args:
    v1 (Vector): The first point.
    v2 (Vector): The second point.

Returns:
    double: The distance between two points in the XY plane.

<a id="unreal.MathLibrary.vector_distance"></a>

#### vector_distance

```python
@classmethod
def vector_distance(cls, v1: Vector, v2: Vector) -> float
```

X.vector_distance(v1, v2) -> double
Distance between two points.

Args:
    v1 (Vector): The first point.
    v2 (Vector): The second point.

Returns:
    double: The distance between two points.

<a id="unreal.MathLibrary.vector_cosine_angle2d"></a>

#### vector_cosine_angle2d

```python
@classmethod
def vector_cosine_angle2d(cls, a: Vector, b: Vector) -> float
```

X.vector_cosine_angle2d(a, b) -> double
Returns the cosine of the angle between this vector and another projected onto the XY plane (no Z).

Args:
    a (Vector): 
    b (Vector): the other vector to find the 2D cosine of the angle with.

Returns:
    double: The cosine.

<a id="unreal.MathLibrary.vector_component_min"></a>

#### vector_component_min

```python
@classmethod
def vector_component_min(cls, a: Vector, b: Vector) -> Vector
```

X.vector_component_min(a, b) -> Vector
Find the minimum elements (X, Y and Z) between the two vector's components

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_component_max"></a>

#### vector_component_max

```python
@classmethod
def vector_component_max(cls, a: Vector, b: Vector) -> Vector
```

X.vector_component_max(a, b) -> Vector
Find the maximum elements (X, Y and Z) between the two vector's components

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_clamp_size_max2d"></a>

#### vector_clamp_size_max2d

```python
@classmethod
def vector_clamp_size_max2d(cls, a: Vector, max: float) -> Vector
```

X.vector_clamp_size_max2d(a, max) -> Vector
Create a copy of this vector, with the maximum 2D magnitude/size/length clamped to MaxSize. Z is unchanged.

Args:
    a (Vector): 
    max (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_clamp_size_max"></a>

#### vector_clamp_size_max

```python
@classmethod
def vector_clamp_size_max(cls, a: Vector, max: float) -> Vector
```

X.vector_clamp_size_max(a, max) -> Vector
Create a copy of this vector, with its maximum magnitude/size/length clamped to MaxSize.

Args:
    a (Vector): 
    max (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_clamp_size2d"></a>

#### vector_clamp_size2d

```python
@classmethod
def vector_clamp_size2d(cls, a: Vector, min: float, max: float) -> Vector
```

X.vector_clamp_size2d(a, min, max) -> Vector
Create a copy of this vector, with the 2D magnitude/size/length clamped between Min and Max. Z is unchanged.

Args:
    a (Vector): 
    min (double): 
    max (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_bounded_to_cube"></a>

#### vector_bounded_to_cube

```python
@classmethod
def vector_bounded_to_cube(cls, vect: Vector, radius: float) -> Vector
```

X.vector_bounded_to_cube(vect, radius) -> Vector
Get a copy of this vector, clamped inside of an axis aligned cube centered at the origin.

Args:
    vect (Vector): 
    radius (float): Half size of the cube (or radius of sphere circumscribed in the cube).

Returns:
    Vector: A copy of this vector, bound by cube.

<a id="unreal.MathLibrary.vector_bounded_to_box"></a>

#### vector_bounded_to_box

```python
@classmethod
def vector_bounded_to_box(cls, vect: Vector, box_min: Vector,
                          box_max: Vector) -> Vector
```

X.vector_bounded_to_box(vect, box_min, box_max) -> Vector
Get a copy of this vector, clamped inside of the specified axis aligned cube.

Args:
    vect (Vector): 
    box_min (Vector): 
    box_max (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.vector_assign"></a>

#### vector_assign

```python
@classmethod
def vector_assign(cls, a: Vector, vector: Vector) -> Vector
```

X.vector_assign(a, vector) -> Vector
Assign the values of the supplied vector.

Args:
    a (Vector): 
    vector (Vector): Vector to copy values from.

Returns:
    Vector: 

    a (Vector):

<a id="unreal.MathLibrary.vector_add_bounded"></a>

#### vector_add_bounded

```python
@classmethod
def vector_add_bounded(cls, a: Vector, add_vect: Vector,
                       radius: float) -> Vector
```

X.vector_add_bounded(a, add_vect, radius) -> Vector
Add a vector to this and clamp the result to an axis aligned cube centered at the origin.

Args:
    a (Vector): 
    add_vect (Vector): Vector to add.
    radius (float): Half size of the cube.

Returns:
    Vector: 

    a (Vector):

<a id="unreal.MathLibrary.vector4_size_squared3"></a>

#### vector4_size_squared3

```python
@classmethod
def vector4_size_squared3(cls, a: Vector4) -> float
```

X.vector4_size_squared3(a) -> double
Returns the squared length of the vector. The W element is ignored.

Args:
    a (Vector4): 

Returns:
    double:

<a id="unreal.MathLibrary.vector4_size_squared"></a>

#### vector4_size_squared

```python
@classmethod
def vector4_size_squared(cls, a: Vector4) -> float
```

X.vector4_size_squared(a) -> double
Returns the squared length of the vector.

Args:
    a (Vector4): 

Returns:
    double:

<a id="unreal.MathLibrary.vector4_size3"></a>

#### vector4_size3

```python
@classmethod
def vector4_size3(cls, a: Vector4) -> float
```

X.vector4_size3(a) -> double
Returns the length of the vector. The W element is ignored.

Args:
    a (Vector4): 

Returns:
    double:

<a id="unreal.MathLibrary.vector4_size"></a>

#### vector4_size

```python
@classmethod
def vector4_size(cls, a: Vector4) -> float
```

X.vector4_size(a) -> double
Returns the length of the vector.

Args:
    a (Vector4): 

Returns:
    double:

<a id="unreal.MathLibrary.vector4_set"></a>

#### vector4_set

```python
@classmethod
def vector4_set(cls, a: Vector4, x: float, y: float, z: float,
                w: float) -> Vector4
```

X.vector4_set(a, x, y, z, w) -> Vector4
Set the values of the vector directly.

Args:
    a (Vector4): 
    x (double): 
    y (double): 
    z (double): 
    w (double): 

Returns:
    Vector4: 

    a (Vector4):

<a id="unreal.MathLibrary.vector4_normal_unsafe3"></a>

#### vector4_normal_unsafe3

```python
@classmethod
def vector4_normal_unsafe3(cls, a: Vector4) -> Vector4
```

X.vector4_normal_unsafe3(a) -> Vector4
Calculates normalized unit version of vector without checking for zero length. The W element is ignored and the returned vector has W=0.

Args:
    a (Vector4): 

Returns:
    Vector4: Normalized version of vector.

<a id="unreal.MathLibrary.vector4_normalize3"></a>

#### vector4_normalize3

```python
@classmethod
def vector4_normalize3(cls,
                       a: Vector4,
                       tolerance: float = 0.000000) -> Vector4
```

X.vector4_normalize3(a, tolerance=0.000000) -> Vector4
Normalize this vector in-place if it is large enough or set it to (0,0,0,0) otherwise. The W element is ignored and the returned vector has W=0.

Args:
    a (Vector4): 
    tolerance (float): Minimum squared length of vector for normalization.

Returns:
    Vector4: 

    a (Vector4):

<a id="unreal.MathLibrary.vector4_normal3"></a>

#### vector4_normal3

```python
@classmethod
def vector4_normal3(cls, a: Vector4, tolerance: float = 0.000100) -> Vector4
```

X.vector4_normal3(a, tolerance=0.000100) -> Vector4
Gets a normalized unit copy of the vector, ensuring it is safe to do so based on the length. The W element is ignored and the returned vector has W=0.
Returns zero vector if vector length is too small to safely normalize.

Args:
    a (Vector4): 
    tolerance (float): Minimum squared vector length.

Returns:
    Vector4: A normalized copy if safe, (0,0,0) otherwise.

<a id="unreal.MathLibrary.vector4_negated"></a>

#### vector4_negated

```python
@classmethod
def vector4_negated(cls, a: Vector4) -> Vector4
```

X.vector4_negated(a) -> Vector4
Gets a negated copy of the vector. Equivalent to -Vector for scripts.

Args:
    a (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.vector4_mirror_by_vector3"></a>

#### vector4_mirror_by_vector3

```python
@classmethod
def vector4_mirror_by_vector3(cls, direction: Vector4,
                              surface_normal: Vector4) -> Vector4
```

X.vector4_mirror_by_vector3(direction, surface_normal) -> Vector4
Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
Produces a result like shining a laser at a mirror!
The W element is ignored.

Args:
    direction (Vector4): Direction vector the ray is coming from.
    surface_normal (Vector4): A normal of the surface the ray should be reflected on.

Returns:
    Vector4: Reflected vector.

<a id="unreal.MathLibrary.vector4_is_zero"></a>

#### vector4_is_zero

```python
@classmethod
def vector4_is_zero(cls, a: Vector4) -> bool
```

X.vector4_is_zero(a) -> bool
Checks whether all components of the vector are exactly zero.

Args:
    a (Vector4): 

Returns:
    bool: true if vector is exactly zero, otherwise false.

<a id="unreal.MathLibrary.vector4_is_unit3"></a>

#### vector4_is_unit3

```python
@classmethod
def vector4_is_unit3(cls,
                     a: Vector4,
                     squared_lenth_tolerance: float = 0.000100) -> bool
```

X.vector4_is_unit3(a, squared_lenth_tolerance=0.000100) -> bool
Determines if vector is normalized / unit (length 1) within specified squared tolerance. The W element is ignored.

Args:
    a (Vector4): 
    squared_lenth_tolerance (float): 

Returns:
    bool: true if unit, false otherwise.

<a id="unreal.MathLibrary.vector4_is_normal3"></a>

#### vector4_is_normal3

```python
@classmethod
def vector4_is_normal3(cls, a: Vector4) -> bool
```

X.vector4_is_normal3(a) -> bool
Determines if vector is normalized / unit (length 1). The W element is ignored.

Args:
    a (Vector4): 

Returns:
    bool: true if normalized, false otherwise.

<a id="unreal.MathLibrary.vector4_is_nearly_zero3"></a>

#### vector4_is_nearly_zero3

```python
@classmethod
def vector4_is_nearly_zero3(cls,
                            a: Vector4,
                            tolerance: float = 0.000100) -> bool
```

X.vector4_is_nearly_zero3(a, tolerance=0.000100) -> bool
Checks whether vector is near to zero within a specified tolerance. The W element is ignored.

Args:
    a (Vector4): 
    tolerance (float): Error tolerance.

Returns:
    bool: true if vector is in tolerance to zero, otherwise false.

<a id="unreal.MathLibrary.vector4_is_nan"></a>

#### vector4_is_nan

```python
@classmethod
def vector4_is_nan(cls, a: Vector4) -> bool
```

X.vector4_is_nan(a) -> bool
Determines if any component is not a number (NAN)

Args:
    a (Vector4): 

Returns:
    bool: true if one or more components is NAN, otherwise false.

<a id="unreal.MathLibrary.vector4_dot_product3"></a>

#### vector4_dot_product3

```python
@classmethod
def vector4_dot_product3(cls, a: Vector4, b: Vector4) -> float
```

X.vector4_dot_product3(a, b) -> double
Returns the dot product of two vectors - see http://mathworld.wolfram.com/DotProduct.html The W element is ignored.

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    double:

<a id="unreal.MathLibrary.vector4_dot_product"></a>

#### vector4_dot_product

```python
@classmethod
def vector4_dot_product(cls, a: Vector4, b: Vector4) -> float
```

X.vector4_dot_product(a, b) -> double
Returns the dot product of two vectors - see http://mathworld.wolfram.com/DotProduct.html

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    double:

<a id="unreal.MathLibrary.vector4_cross_product3"></a>

#### vector4_cross_product3

```python
@classmethod
def vector4_cross_product3(cls, a: Vector4, b: Vector4) -> Vector4
```

X.vector4_cross_product3(a, b) -> Vector4
Returns the cross product of two vectors - see  http://mathworld.wolfram.com/CrossProduct.html

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.vector4_assign"></a>

#### vector4_assign

```python
@classmethod
def vector4_assign(cls, a: Vector4, vector: Vector4) -> Vector4
```

X.vector4_assign(a, vector) -> Vector4
Assign the values of the supplied vector.

Args:
    a (Vector4): 
    vector (Vector4): Vector to copy values from.

Returns:
    Vector4: 

    a (Vector4):

<a id="unreal.MathLibrary.vector2d_interp_to_constant"></a>

#### vector2d_interp_to_constant

```python
@classmethod
def vector2d_interp_to_constant(cls, current: Vector2D, target: Vector2D,
                                delta_time: float,
                                interp_speed: float) -> Vector2D
```

X.vector2d_interp_to_constant(current, target, delta_time, interp_speed) -> Vector2D
Tries to reach Target at a constant rate.

Args:
    current (Vector2D): Actual position
    target (Vector2D): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed

Returns:
    Vector2D: New interpolated position

<a id="unreal.MathLibrary.vector2d_interp_to"></a>

#### vector2d_interp_to

```python
@classmethod
def vector2d_interp_to(cls, current: Vector2D, target: Vector2D,
                       delta_time: float, interp_speed: float) -> Vector2D
```

X.vector2d_interp_to(current, target, delta_time, interp_speed) -> Vector2D
Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    current (Vector2D): Actual position
    target (Vector2D): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Vector2D: New interpolated position

<a id="unreal.MathLibrary.utc_now"></a>

#### utc_now

```python
@classmethod
def utc_now(cls) -> DateTime
```

X.utc_now() -> DateTime
Returns the UTC date and time on this computer

Returns:
    DateTime:

<a id="unreal.MathLibrary.transform_vector4"></a>

#### transform_vector4

```python
@classmethod
def transform_vector4(cls, matrix: Matrix, vec4: Vector4) -> Vector4
```

X.transform_vector4(matrix, vec4) -> Vector4
Transform the input vector4 by a provided matrix4x4 and returns the resulting vector4.

Args:
    matrix (Matrix): 
    vec4 (Vector4): 

Returns:
    Vector4: Transformed vector4.

<a id="unreal.MathLibrary.transform_rotation"></a>

#### transform_rotation

```python
@classmethod
def transform_rotation(cls, t: Transform, rotation: Rotator) -> Rotator
```

X.transform_rotation(t, rotation) -> Rotator
Transform a rotator by the supplied transform.
For example, if T was an object's transform, this would transform a rotation from local space to world space.

Args:
    t (Transform): 
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.transform_location"></a>

#### transform_location

```python
@classmethod
def transform_location(cls, t: Transform, location: Vector) -> Vector
```

X.transform_location(t, location) -> Vector
Transform a position by the supplied transform.
For example, if T was an object's transform, this would transform a position from local space to world space.

Args:
    t (Transform): 
    location (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.transform_position"></a>

#### transform_position

```python
@classmethod
def transform_position(cls, t: Transform, location: Vector) -> Vector
```

deprecated: 'transform_position' was renamed to 'transform_location'.

<a id="unreal.MathLibrary.transform_direction"></a>

#### transform_direction

```python
@classmethod
def transform_direction(cls, t: Transform, direction: Vector) -> Vector
```

X.transform_direction(t, direction) -> Vector
Transform a direction vector by the supplied transform - will not change its length.
For example, if T was an object's transform, this would transform a direction from local space to world space.

Args:
    t (Transform): 
    direction (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.transform_determinant"></a>

#### transform_determinant

```python
@classmethod
def transform_determinant(cls, transform: Transform) -> float
```

X.transform_determinant(transform) -> float
Calculates the determinant of the transform (converts to FMatrix internally)

Args:
    transform (Transform): 

Returns:
    float:

<a id="unreal.MathLibrary.to_unix_timestamp_double"></a>

#### to_unix_timestamp_double

```python
@classmethod
def to_unix_timestamp_double(cls, time: DateTime) -> float
```

X.to_unix_timestamp_double(time) -> double
Returns this date as the number of seconds since the Unix Epoch (January 1st of 1970).
see: FromUnixTimestamp

Args:
    time (DateTime): 

Returns:
    double: Time of day.

<a id="unreal.MathLibrary.to_unix_timestamp"></a>

#### to_unix_timestamp

```python
@classmethod
def to_unix_timestamp(cls, time: DateTime) -> int
```

X.to_unix_timestamp(time) -> int64
Returns this date as the number of seconds since the Unix Epoch (January 1st of 1970).
see: FromUnixTimestamp

Args:
    time (DateTime): 

Returns:
    int64: Time of day.

<a id="unreal.MathLibrary.to_sign2d"></a>

#### to_sign2d

```python
@classmethod
def to_sign2d(cls, a: Vector2D) -> Vector2D
```

X.to_sign2d(a) -> Vector2D
Get a copy of the vector as sign only.
Each component is set to +1 or -1, with the sign of zero treated as +1.

Args:
    a (Vector2D): 

Returns:
    Vector2D: A copy of the vector with each component set to +1 or -1

<a id="unreal.MathLibrary.to_rounded2d"></a>

#### to_rounded2d

```python
@classmethod
def to_rounded2d(cls, a: Vector2D) -> Vector2D
```

X.to_rounded2d(a) -> Vector2D
Get this vector as a vector where each component has been rounded to the nearest int.

Args:
    a (Vector2D): 

Returns:
    Vector2D: New FVector2D from this vector that is rounded.

<a id="unreal.MathLibrary.to_hex_linear_color"></a>

#### to_hex_linear_color

```python
@classmethod
def to_hex_linear_color(cls, color: LinearColor) -> str
```

X.to_hex_linear_color(color) -> str
Converts this color value to a hexadecimal string. The format of the string is RRGGBBAA.

Args:
    color (LinearColor): 

Returns:
    str:

<a id="unreal.MathLibrary.to_direction_and_length2d"></a>

#### to_direction_and_length2d

```python
@classmethod
def to_direction_and_length2d(cls, a: Vector2D) -> Tuple[Vector2D, float]
```

X.to_direction_and_length2d(a) -> (out_dir=Vector2D, out_length=double)
Util to convert this vector into a unit direction vector and its original length.

Args:
    a (Vector2D): 

Returns:
    tuple: 

    out_dir (Vector2D): Reference passed in to store unit direction vector.

    out_length (double): Reference passed in to store length of the vector.

<a id="unreal.MathLibrary.today"></a>

#### today

```python
@classmethod
def today(cls) -> DateTime
```

X.today() -> DateTime
Returns the local date on this computer

Returns:
    DateTime:

<a id="unreal.MathLibrary.t_lerp"></a>

#### t_lerp

```python
@classmethod
def t_lerp(
    cls,
    a: Transform,
    b: Transform,
    alpha: float,
    interp_mode: LerpInterpolationMode = LerpInterpolationMode.QUAT_INTERP
) -> Transform
```

X.t_lerp(a, b, alpha, interp_mode=LerpInterpolationMode.QUAT_INTERP) -> Transform
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1).

Args:
    a (Transform): 
    b (Transform): 
    alpha (float): 
    interp_mode (LerpInterpolationMode): 

Returns:
    Transform:

<a id="unreal.MathLibrary.t_interp_to"></a>

#### t_interp_to

```python
@classmethod
def t_interp_to(cls, current: Transform, target: Transform, delta_time: float,
                interp_speed: float) -> Transform
```

X.t_interp_to(current, target, delta_time, interp_speed) -> Transform
Tries to reach Target transform based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    current (Transform): Actual transform
    target (Transform): Target transform
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Transform: New interpolated transform

<a id="unreal.MathLibrary.timespan_ratio"></a>

#### timespan_ratio

```python
@classmethod
def timespan_ratio(cls, a: Timespan, b: Timespan) -> float
```

X.timespan_ratio(a, b) -> float
Returns the ratio between two time spans (A / B), handles zero values

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    float:

<a id="unreal.MathLibrary.timespan_from_string"></a>

#### timespan_from_string

```python
@classmethod
def timespan_from_string(cls, timespan_string: str) -> Optional[Timespan]
```

X.timespan_from_string(timespan_string) -> Timespan or None
Converts a time span string to a Timespan object

Args:
    timespan_string (str): 

Returns:
    Timespan or None: 

    result (Timespan):

<a id="unreal.MathLibrary.tan"></a>

#### tan

```python
@classmethod
def tan(cls, a: float) -> float
```

X.tan(a) -> double
Returns the tan of A (expects Radians)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.subtract_vector_vector"></a>

#### subtract_vector_vector

```python
@classmethod
def subtract_vector_vector(cls, a: Vector, b: Vector) -> Vector
```

X.subtract_vector_vector(a, b) -> Vector
Vector subtraction

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.subtract_vector_int"></a>

#### subtract_vector_int

```python
@classmethod
def subtract_vector_int(cls, a: Vector, b: int) -> Vector
```

X.subtract_vector_int(a, b) -> Vector
Subtracts an integer from each component of a vector

Args:
    a (Vector): 
    b (int32): 

Returns:
    Vector:

<a id="unreal.MathLibrary.subtract_vector_float"></a>

#### subtract_vector_float

```python
@classmethod
def subtract_vector_float(cls, a: Vector, b: float) -> Vector
```

X.subtract_vector_float(a, b) -> Vector
Subtracts a float from each component of a vector

Args:
    a (Vector): 
    b (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.subtract_vector4_vector4"></a>

#### subtract_vector4_vector4

```python
@classmethod
def subtract_vector4_vector4(cls, a: Vector4, b: Vector4) -> Vector4
```

X.subtract_vector4_vector4(a, b) -> Vector4
Returns subtraction of Vector B from Vector A (A - B)

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.subtract_vector2d_vector2d"></a>

#### subtract_vector2d_vector2d

```python
@classmethod
def subtract_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> Vector2D
```

X.subtract_vector2d_vector2d(a, b) -> Vector2D
Returns subtraction of Vector B from Vector A (A - B)

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.subtract_vector2d_float"></a>

#### subtract_vector2d_float

```python
@classmethod
def subtract_vector2d_float(cls, a: Vector2D, b: float) -> Vector2D
```

X.subtract_vector2d_float(a, b) -> Vector2D
Returns Vector A subtracted by B

Args:
    a (Vector2D): 
    b (double): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.subtract_timespan_timespan"></a>

#### subtract_timespan_timespan

```python
@classmethod
def subtract_timespan_timespan(cls, a: Timespan, b: Timespan) -> Timespan
```

X.subtract_timespan_timespan(a, b) -> Timespan
Subtraction (A - B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.subtract_quat_quat"></a>

#### subtract_quat_quat

```python
@classmethod
def subtract_quat_quat(cls, a: Quat, b: Quat) -> Quat
```

X.subtract_quat_quat(a, b) -> Quat
Returns subtraction of Vector B from Vector A (A - B)

Args:
    a (Quat): 
    b (Quat): 

Returns:
    Quat:

<a id="unreal.MathLibrary.subtract_linear_color_linear_color"></a>

#### subtract_linear_color_linear_color

```python
@classmethod
def subtract_linear_color_linear_color(cls, a: LinearColor,
                                       b: LinearColor) -> LinearColor
```

X.subtract_linear_color_linear_color(a, b) -> LinearColor
Element-wise subtraction of two linear colors (R-R, G-G, B-B, A-A)

Args:
    a (LinearColor): 
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.subtract_int_point_int_point"></a>

#### subtract_int_point_int_point

```python
@classmethod
def subtract_int_point_int_point(cls, a: IntPoint, b: IntPoint) -> IntPoint
```

X.subtract_int_point_int_point(a, b) -> IntPoint
Returns IntPoint A subtracted by B

Args:
    a (IntPoint): 
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.subtract_int_point_int"></a>

#### subtract_int_point_int

```python
@classmethod
def subtract_int_point_int(cls, a: IntPoint, b: int) -> IntPoint
```

X.subtract_int_point_int(a, b) -> IntPoint
Subtraction (A - B)

Args:
    a (IntPoint): 
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.subtract_int_int"></a>

#### subtract_int_int

```python
@classmethod
def subtract_int_int(cls, a: int, b: int = 1) -> int
```

X.subtract_int_int(a, b=1) -> int32
Subtraction (A - B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.subtract_int64_int64"></a>

#### subtract_int64_int64

```python
@classmethod
def subtract_int64_int64(cls, a: int, b: int = 1) -> int
```

X.subtract_int64_int64(a, b=1) -> int64
Subtraction (A - B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.subtract_double_double"></a>

#### subtract_double_double

```python
@classmethod
def subtract_double_double(cls, a: float, b: float = 1.000000) -> float
```

X.subtract_double_double(a, b=1.000000) -> double
Subtraction (A - B)

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.subtract_float_float"></a>

#### subtract_float_float

```python
@classmethod
def subtract_float_float(cls, a: float, b: float = 1.000000) -> float
```

deprecated: 'subtract_float_float' was renamed to 'subtract_double_double'.

<a id="unreal.MathLibrary.subtract_date_time_timespan"></a>

#### subtract_date_time_timespan

```python
@classmethod
def subtract_date_time_timespan(cls, a: DateTime, b: Timespan) -> DateTime
```

X.subtract_date_time_timespan(a, b) -> DateTime
Subtraction (A - B)

Args:
    a (DateTime): 
    b (Timespan): 

Returns:
    DateTime:

<a id="unreal.MathLibrary.subtract_date_time_date_time"></a>

#### subtract_date_time_date_time

```python
@classmethod
def subtract_date_time_date_time(cls, a: DateTime, b: DateTime) -> Timespan
```

X.subtract_date_time_date_time(a, b) -> Timespan
Subtraction (A - B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.subtract_byte_byte"></a>

#### subtract_byte_byte

```python
@classmethod
def subtract_byte_byte(cls, a: int, b: int = 1) -> int
```

X.subtract_byte_byte(a, b=1) -> uint8
Subtraction (A - B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.square"></a>

#### square

```python
@classmethod
def square(cls, a: float) -> float
```

X.square(a) -> double
Returns square of A (A*A)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.sqrt"></a>

#### sqrt

```python
@classmethod
def sqrt(cls, a: float) -> float
```

X.sqrt(a) -> double
Returns square root of A

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.spherical2d_to_unit_cartesian"></a>

#### spherical2d_to_unit_cartesian

```python
@classmethod
def spherical2d_to_unit_cartesian(cls, a: Vector2D) -> Vector
```

X.spherical2d_to_unit_cartesian(a) -> Vector
Converts spherical coordinates on the unit sphere into a Cartesian unit length vector.

Args:
    a (Vector2D): 

Returns:
    Vector:

<a id="unreal.MathLibrary.sin"></a>

#### sin

```python
@classmethod
def sin(cls, a: float) -> float
```

X.sin(a) -> double
Returns the sine of A (expects Radians)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.sign_of_integer64"></a>

#### sign_of_integer64

```python
@classmethod
def sign_of_integer64(cls, a: int) -> int
```

X.sign_of_integer64(a) -> int64
Sign (integer64, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

Args:
    a (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.sign_of_integer"></a>

#### sign_of_integer

```python
@classmethod
def sign_of_integer(cls, a: int) -> int
```

X.sign_of_integer(a) -> int32
Sign (integer, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

Args:
    a (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.sign_of_float"></a>

#### sign_of_float

```python
@classmethod
def sign_of_float(cls, a: float) -> float
```

X.sign_of_float(a) -> double
Sign (float, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.set_vector_spring_state_velocity"></a>

#### set_vector_spring_state_velocity

```python
@classmethod
def set_vector_spring_state_velocity(cls, spring_state: VectorSpringState,
                                     velocity: Vector) -> VectorSpringState
```

X.set_vector_spring_state_velocity(spring_state, velocity) -> VectorSpringState
Sets the state velocity of a vector spring

Args:
    spring_state (VectorSpringState): 
    velocity (Vector): 

Returns:
    VectorSpringState: 

    spring_state (VectorSpringState):

<a id="unreal.MathLibrary.set_random_stream_seed"></a>

#### set_random_stream_seed

```python
@classmethod
def set_random_stream_seed(cls, stream: RandomStream,
                           new_seed: int) -> RandomStream
```

X.set_random_stream_seed(stream, new_seed) -> RandomStream
Set the seed of a random stream to a specific number

Args:
    stream (RandomStream): 
    new_seed (int32): 

Returns:
    RandomStream: 

    stream (RandomStream):

<a id="unreal.MathLibrary.set_quaternion_spring_state_angular_velocity"></a>

#### set_quaternion_spring_state_angular_velocity

```python
@classmethod
def set_quaternion_spring_state_angular_velocity(
        cls, spring_state: QuaternionSpringState,
        angular_velocity: Vector) -> QuaternionSpringState
```

X.set_quaternion_spring_state_angular_velocity(spring_state, angular_velocity) -> QuaternionSpringState
Sets the state angular velocity of a quaternion spring

Args:
    spring_state (QuaternionSpringState): 
    angular_velocity (Vector): 

Returns:
    QuaternionSpringState: 

    spring_state (QuaternionSpringState):

<a id="unreal.MathLibrary.set_float_spring_state_velocity"></a>

#### set_float_spring_state_velocity

```python
@classmethod
def set_float_spring_state_velocity(cls, spring_state: FloatSpringState,
                                    velocity: float) -> FloatSpringState
```

X.set_float_spring_state_velocity(spring_state, velocity) -> FloatSpringState
Sets the state velocity of a float spring

Args:
    spring_state (FloatSpringState): 
    velocity (float): 

Returns:
    FloatSpringState: 

    spring_state (FloatSpringState):

<a id="unreal.MathLibrary.set2d"></a>

#### set2d

```python
@classmethod
def set2d(cls, a: Vector2D, x: float, y: float) -> Vector2D
```

X.set2d(a, x, y) -> Vector2D
Set the values of the vector directly.

Args:
    a (Vector2D): 
    x (double): 
    y (double): 

Returns:
    Vector2D: 

    a (Vector2D):

<a id="unreal.MathLibrary.select_vector"></a>

#### select_vector

```python
@classmethod
def select_vector(cls, a: Vector, b: Vector, pick_a: bool) -> Vector
```

X.select_vector(a, b, pick_a) -> Vector
If bPickA is true, A is returned, otherwise B is

Args:
    a (Vector): 
    b (Vector): 
    pick_a (bool): 

Returns:
    Vector:

<a id="unreal.MathLibrary.select_transform"></a>

#### select_transform

```python
@classmethod
def select_transform(cls, a: Transform, b: Transform,
                     pick_a: bool) -> Transform
```

X.select_transform(a, b, pick_a) -> Transform
If bPickA is true, A is returned, otherwise B is

Args:
    a (Transform): 
    b (Transform): 
    pick_a (bool): 

Returns:
    Transform:

<a id="unreal.MathLibrary.select_text"></a>

#### select_text

```python
@classmethod
def select_text(cls, a: Text, b: Text, pick_a: bool) -> Text
```

X.select_text(a, b, pick_a) -> Text
If bPickA is true, A is returned, otherwise B is

Args:
    a (Text): 
    b (Text): 
    pick_a (bool): 

Returns:
    Text:

<a id="unreal.MathLibrary.select_string"></a>

#### select_string

```python
@classmethod
def select_string(cls, a: str, b: str, pick_a: bool) -> str
```

X.select_string(a, b, pick_a) -> str
If bPickA is true, A is returned, otherwise B is

Args:
    a (str): 
    b (str): 
    pick_a (bool): 

Returns:
    str:

<a id="unreal.MathLibrary.select_rotator"></a>

#### select_rotator

```python
@classmethod
def select_rotator(cls, a: Rotator, b: Rotator, pick_a: bool) -> Rotator
```

X.select_rotator(a, b, pick_a) -> Rotator
If bPickA is true, A is returned, otherwise B is

Args:
    a (Rotator): 
    b (Rotator): 
    pick_a (bool): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.select_object"></a>

#### select_object

```python
@classmethod
def select_object(cls, a: Object, b: Object, select_a: bool) -> Object
```

X.select_object(a, b, select_a) -> Object
If bPickA is true, A is returned, otherwise B is

Args:
    a (Object): 
    b (Object): 
    select_a (bool): 

Returns:
    Object:

<a id="unreal.MathLibrary.select_name"></a>

#### select_name

```python
@classmethod
def select_name(cls, a: Name, b: Name, pick_a: bool) -> Name
```

X.select_name(a, b, pick_a) -> Name
If bPickA is true, A is returned, otherwise B is

Args:
    a (Name): 
    b (Name): 
    pick_a (bool): 

Returns:
    Name:

<a id="unreal.MathLibrary.select_int"></a>

#### select_int

```python
@classmethod
def select_int(cls, a: int, b: int, pick_a: bool) -> int
```

X.select_int(a, b, pick_a) -> int32
If bPickA is true, A is returned, otherwise B is

Args:
    a (int32): 
    b (int32): 
    pick_a (bool): 

Returns:
    int32:

<a id="unreal.MathLibrary.select_float"></a>

#### select_float

```python
@classmethod
def select_float(cls, a: float, b: float, pick_a: bool) -> float
```

X.select_float(a, b, pick_a) -> double
If bPickA is true, A is returned, otherwise B is

Args:
    a (double): 
    b (double): 
    pick_a (bool): 

Returns:
    double:

<a id="unreal.MathLibrary.select_color"></a>

#### select_color

```python
@classmethod
def select_color(cls, a: LinearColor, b: LinearColor,
                 pick_a: bool) -> LinearColor
```

X.select_color(a, b, pick_a) -> LinearColor
If bPickA is true, A is returned, otherwise B is

Args:
    a (LinearColor): 
    b (LinearColor): 
    pick_a (bool): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.select_class"></a>

#### select_class

```python
@classmethod
def select_class(cls, a: Class, b: Class, select_a: bool) -> Class
```

X.select_class(a, b, select_a) -> type(Class)
If bPickA is true, A is returned, otherwise B is

Args:
    a (type(Class)): 
    b (type(Class)): 
    select_a (bool): 

Returns:
    type(Class):

<a id="unreal.MathLibrary.seed_random_stream"></a>

#### seed_random_stream

```python
@classmethod
def seed_random_stream(cls, stream: RandomStream) -> RandomStream
```

X.seed_random_stream(stream) -> RandomStream
Create a new random seed for a random stream

Args:
    stream (RandomStream): 

Returns:
    RandomStream: 

    stream (RandomStream):

<a id="unreal.MathLibrary.safe_divide"></a>

#### safe_divide

```python
@classmethod
def safe_divide(cls, a: float, b: float) -> float
```

X.safe_divide(a, b) -> double
This functions returns 0 if B (the denominator) is zero

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.round64"></a>

#### round64

```python
@classmethod
def round64(cls, a: float) -> int
```

X.round64(a) -> int64
Rounds A to the nearest integer (e.g., -1.6 becomes -2 and 1.6 becomes 2)

Args:
    a (double): 

Returns:
    int64:

<a id="unreal.MathLibrary.round"></a>

#### round

```python
@classmethod
def round(cls, a: float) -> int
```

X.round(a) -> int32
Rounds A to the nearest integer (e.g., -1.6 becomes -2 and 1.6 becomes 2)

Args:
    a (double): 

Returns:
    int32:

<a id="unreal.MathLibrary.rotator_from_axis_and_angle"></a>

#### rotator_from_axis_and_angle

```python
@classmethod
def rotator_from_axis_and_angle(cls, axis: Vector, angle: float) -> Rotator
```

X.rotator_from_axis_and_angle(axis, angle) -> Rotator
Create a rotation from an axis and supplied angle (in degrees)

Args:
    axis (Vector): 
    angle (float): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.rotate_angle_axis"></a>

#### rotate_angle_axis

```python
@classmethod
def rotate_angle_axis(cls, vect: Vector, angle_deg: float,
                      axis: Vector) -> Vector
```

X.rotate_angle_axis(vect, angle_deg, axis) -> Vector
Returns result of vector A rotated by AngleDeg around Axis

Args:
    vect (Vector): 
    angle_deg (float): 
    axis (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.r_lerp"></a>

#### r_lerp

```python
@classmethod
def r_lerp(cls, a: Rotator, b: Rotator, alpha: float,
           shortest_path: bool) -> Rotator
```

X.r_lerp(a, b, alpha, shortest_path) -> Rotator
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    a (Rotator): 
    b (Rotator): 
    alpha (float): 
    shortest_path (bool): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.r_interp_to_constant"></a>

#### r_interp_to_constant

```python
@classmethod
def r_interp_to_constant(cls, current: Rotator, target: Rotator,
                         delta_time: float, interp_speed: float) -> Rotator
```

X.r_interp_to_constant(current, target, delta_time, interp_speed) -> Rotator
Tries to reach Target rotation at a constant rate.

Args:
    current (Rotator): Actual rotation
    target (Rotator): Target rotation
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed

Returns:
    Rotator: New interpolated position

<a id="unreal.MathLibrary.r_interp_to"></a>

#### r_interp_to

```python
@classmethod
def r_interp_to(cls, current: Rotator, target: Rotator, delta_time: float,
                interp_speed: float) -> Rotator
```

X.r_interp_to(current, target, delta_time, interp_speed) -> Rotator
Tries to reach Target rotation based on Current rotation, giving a nice smooth feeling when rotating to Target rotation.

Args:
    current (Rotator): Actual rotation
    target (Rotator): Target rotation
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Rotator: New interpolated position

<a id="unreal.MathLibrary.rgb_to_hsv_vector"></a>

#### rgb_to_hsv_vector

```python
@classmethod
def rgb_to_hsv_vector(cls, rgb: LinearColor) -> LinearColor
```

X.rgb_to_hsv_vector(rgb) -> LinearColor
Converts a RGB linear color to HSV (where H is in R (0..360), S is in G (0..1), and V is in B (0..1))

Args:
    rgb (LinearColor): 

Returns:
    LinearColor: 

    hsv (LinearColor):

<a id="unreal.MathLibrary.rgb_to_hsv"></a>

#### rgb_to_hsv

```python
@classmethod
def rgb_to_hsv(cls, color: LinearColor) -> Tuple[float, float, float, float]
```

X.rgb_to_hsv(color) -> (h=float, s=float, v=float, a=float)
Breaks apart a color into individual HSV components (as well as alpha) (Hue is [0..360) while Saturation and Value are 0..1)

Args:
    color (LinearColor): 

Returns:
    tuple: 

    h (float): 

    s (float): 

    v (float): 

    a (float):

<a id="unreal.MathLibrary.rgb_linear_to_hsv"></a>

#### rgb_linear_to_hsv

```python
@classmethod
def rgb_linear_to_hsv(cls, rgb: LinearColor) -> LinearColor
```

X.rgb_linear_to_hsv(rgb) -> LinearColor
Converts a RGB linear color to HSV (where H is in R, S is in G, and V is in B)

Args:
    rgb (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.reset_vector_spring_state"></a>

#### reset_vector_spring_state

```python
@classmethod
def reset_vector_spring_state(
        cls, spring_state: VectorSpringState) -> VectorSpringState
```

X.reset_vector_spring_state(spring_state) -> VectorSpringState
Resets the state of a vector spring

Args:
    spring_state (VectorSpringState): 

Returns:
    VectorSpringState: 

    spring_state (VectorSpringState):

<a id="unreal.MathLibrary.reset_random_stream"></a>

#### reset_random_stream

```python
@classmethod
def reset_random_stream(cls, stream: RandomStream) -> None
```

X.reset_random_stream(stream) -> None
Reset a random stream

Args:
    stream (RandomStream):

<a id="unreal.MathLibrary.reset_quaternion_spring_state"></a>

#### reset_quaternion_spring_state

```python
@classmethod
def reset_quaternion_spring_state(
        cls, spring_state: QuaternionSpringState) -> QuaternionSpringState
```

X.reset_quaternion_spring_state(spring_state) -> QuaternionSpringState
Resets the state of a quaternion spring

Args:
    spring_state (QuaternionSpringState): 

Returns:
    QuaternionSpringState: 

    spring_state (QuaternionSpringState):

<a id="unreal.MathLibrary.reset_float_spring_state"></a>

#### reset_float_spring_state

```python
@classmethod
def reset_float_spring_state(
        cls, spring_state: FloatSpringState) -> FloatSpringState
```

X.reset_float_spring_state(spring_state) -> FloatSpringState
Resets the state of a float spring

Args:
    spring_state (FloatSpringState): 

Returns:
    FloatSpringState: 

    spring_state (FloatSpringState):

<a id="unreal.MathLibrary.random_unit_vector_in_elliptical_cone_in_radians_from_stream"></a>

#### random_unit_vector_in_elliptical_cone_in_radians_from_stream

```python
@classmethod
def random_unit_vector_in_elliptical_cone_in_radians_from_stream(
        cls, stream: RandomStream, cone_dir: Vector, max_yaw_in_radians: float,
        max_pitch_in_radians: float) -> Vector
```

X.random_unit_vector_in_elliptical_cone_in_radians_from_stream(stream, cone_dir, max_yaw_in_radians, max_pitch_in_radians) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
The shape of the cone can be modified according to the yaw and pitch angles.

Args:
    stream (RandomStream): The random stream from which to obtain the vector.
    cone_dir (Vector): 
    max_yaw_in_radians (float): The yaw angle of the cone (from ConeDir to horizontal edge), in radians.
    max_pitch_in_radians (float): The pitch angle of the cone (from ConeDir to vertical edge), in radians.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_elliptical_cone_in_radians"></a>

#### random_unit_vector_in_elliptical_cone_in_radians

```python
@classmethod
def random_unit_vector_in_elliptical_cone_in_radians(
        cls, cone_dir: Vector, max_yaw_in_radians: float,
        max_pitch_in_radians: float) -> Vector
```

X.random_unit_vector_in_elliptical_cone_in_radians(cone_dir, max_yaw_in_radians, max_pitch_in_radians) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
The shape of the cone can be modified according to the yaw and pitch angles.

Args:
    cone_dir (Vector): 
    max_yaw_in_radians (float): The yaw angle of the cone (from ConeDir to horizontal edge), in radians.
    max_pitch_in_radians (float): The pitch angle of the cone (from ConeDir to vertical edge), in radians.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_elliptical_cone_in_degrees_from_stream"></a>

#### random_unit_vector_in_elliptical_cone_in_degrees_from_stream

```python
@classmethod
def random_unit_vector_in_elliptical_cone_in_degrees_from_stream(
        cls, stream: RandomStream, cone_dir: Vector, max_yaw_in_degrees: float,
        max_pitch_in_degrees: float) -> Vector
```

X.random_unit_vector_in_elliptical_cone_in_degrees_from_stream(stream, cone_dir, max_yaw_in_degrees, max_pitch_in_degrees) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
The shape of the cone can be modified according to the yaw and pitch angles.

Args:
    stream (RandomStream): The random stream from which to obtain the vector.
    cone_dir (Vector): 
    max_yaw_in_degrees (float): The yaw angle of the cone (from ConeDir to horizontal edge), in degrees.
    max_pitch_in_degrees (float): The pitch angle of the cone (from ConeDir to vertical edge), in degrees.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_elliptical_cone_in_degrees"></a>

#### random_unit_vector_in_elliptical_cone_in_degrees

```python
@classmethod
def random_unit_vector_in_elliptical_cone_in_degrees(
        cls, cone_dir: Vector, max_yaw_in_degrees: float,
        max_pitch_in_degrees: float) -> Vector
```

X.random_unit_vector_in_elliptical_cone_in_degrees(cone_dir, max_yaw_in_degrees, max_pitch_in_degrees) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
The shape of the cone can be modified according to the yaw and pitch angles.

Args:
    cone_dir (Vector): 
    max_yaw_in_degrees (float): The yaw angle of the cone (from ConeDir to horizontal edge), in degrees.
    max_pitch_in_degrees (float): The pitch angle of the cone (from ConeDir to vertical edge), in degrees.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_cone_with_yaw_and_pitch"></a>

#### random_unit_vector_in_cone_with_yaw_and_pitch

```python
@classmethod
def random_unit_vector_in_cone_with_yaw_and_pitch(
        cls, cone_dir: Vector, max_yaw_in_degrees: float,
        max_pitch_in_degrees: float) -> Vector
```

deprecated: 'random_unit_vector_in_cone_with_yaw_and_pitch' was renamed to 'random_unit_vector_in_elliptical_cone_in_degrees'.

<a id="unreal.MathLibrary.random_unit_vector_in_cone_in_radians_from_stream"></a>

#### random_unit_vector_in_cone_in_radians_from_stream

```python
@classmethod
def random_unit_vector_in_cone_in_radians_from_stream(
        cls, stream: RandomStream, cone_dir: Vector,
        cone_half_angle_in_radians: float) -> Vector
```

X.random_unit_vector_in_cone_in_radians_from_stream(stream, cone_dir, cone_half_angle_in_radians) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Args:
    stream (RandomStream): The random stream from which to obtain the vector.
    cone_dir (Vector): The base "center" direction of the cone.
    cone_half_angle_in_radians (float): The half-angle of the cone (from ConeDir to edge), in radians.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_cone_in_radians"></a>

#### random_unit_vector_in_cone_in_radians

```python
@classmethod
def random_unit_vector_in_cone_in_radians(
        cls, cone_dir: Vector, cone_half_angle_in_radians: float) -> Vector
```

X.random_unit_vector_in_cone_in_radians(cone_dir, cone_half_angle_in_radians) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Args:
    cone_dir (Vector): The base "center" direction of the cone.
    cone_half_angle_in_radians (float): The half-angle of the cone (from ConeDir to edge), in radians.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_cone"></a>

#### random_unit_vector_in_cone

```python
@classmethod
def random_unit_vector_in_cone(cls, cone_dir: Vector,
                               cone_half_angle_in_radians: float) -> Vector
```

deprecated: 'random_unit_vector_in_cone' was renamed to 'random_unit_vector_in_cone_in_radians'.

<a id="unreal.MathLibrary.random_unit_vector_in_cone_in_degrees_from_stream"></a>

#### random_unit_vector_in_cone_in_degrees_from_stream

```python
@classmethod
def random_unit_vector_in_cone_in_degrees_from_stream(
        cls, stream: RandomStream, cone_dir: Vector,
        cone_half_angle_in_degrees: float) -> Vector
```

X.random_unit_vector_in_cone_in_degrees_from_stream(stream, cone_dir, cone_half_angle_in_degrees) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Args:
    stream (RandomStream): The random stream from which to obtain the vector.
    cone_dir (Vector): The base "center" direction of the cone.
    cone_half_angle_in_degrees (float): The half-angle of the cone (from ConeDir to edge), in degrees.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_in_cone_in_degrees"></a>

#### random_unit_vector_in_cone_in_degrees

```python
@classmethod
def random_unit_vector_in_cone_in_degrees(
        cls, cone_dir: Vector, cone_half_angle_in_degrees: float) -> Vector
```

X.random_unit_vector_in_cone_in_degrees(cone_dir, cone_half_angle_in_degrees) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Args:
    cone_dir (Vector): The base "center" direction of the cone.
    cone_half_angle_in_degrees (float): The half-angle of the cone (from ConeDir to edge), in degrees.

Returns:
    Vector:

<a id="unreal.MathLibrary.random_unit_vector_from_stream"></a>

#### random_unit_vector_from_stream

```python
@classmethod
def random_unit_vector_from_stream(cls, stream: RandomStream) -> Vector
```

X.random_unit_vector_from_stream(stream) -> Vector
Returns a random vector with length of 1.0

Args:
    stream (RandomStream): 

Returns:
    Vector:

<a id="unreal.MathLibrary.v_rand_from_stream"></a>

#### v_rand_from_stream

```python
@classmethod
def v_rand_from_stream(cls, stream: RandomStream) -> Vector
```

deprecated: 'v_rand_from_stream' was renamed to 'random_unit_vector_from_stream'.

<a id="unreal.MathLibrary.random_unit_vector"></a>

#### random_unit_vector

```python
@classmethod
def random_unit_vector(cls) -> Vector
```

X.random_unit_vector() -> Vector
Returns a random vector with length of 1

Returns:
    Vector:

<a id="unreal.MathLibrary.v_rand"></a>

#### v_rand

```python
@classmethod
def v_rand(cls) -> Vector
```

deprecated: 'v_rand' was renamed to 'random_unit_vector'.

<a id="unreal.MathLibrary.random_rotator_from_stream"></a>

#### random_rotator_from_stream

```python
@classmethod
def random_rotator_from_stream(cls, stream: RandomStream,
                               roll: bool) -> Rotator
```

X.random_rotator_from_stream(stream, roll) -> Rotator
Create a random rotation

Args:
    stream (RandomStream): 
    roll (bool): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.rot_rand_from_stream"></a>

#### rot_rand_from_stream

```python
@classmethod
def rot_rand_from_stream(cls, stream: RandomStream, roll: bool) -> Rotator
```

deprecated: 'rot_rand_from_stream' was renamed to 'random_rotator_from_stream'.

<a id="unreal.MathLibrary.random_rotator"></a>

#### random_rotator

```python
@classmethod
def random_rotator(cls, roll: bool = False) -> Rotator
```

X.random_rotator(roll=False) -> Rotator
Generates a random rotation, with optional random roll.

Args:
    roll (bool): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.rot_rand"></a>

#### rot_rand

```python
@classmethod
def rot_rand(cls, roll: bool = False) -> Rotator
```

deprecated: 'rot_rand' was renamed to 'random_rotator'.

<a id="unreal.MathLibrary.random_point_in_bounding_box_from_stream_box"></a>

#### random_point_in_bounding_box_from_stream_box

```python
@classmethod
def random_point_in_bounding_box_from_stream_box(cls, stream: RandomStream,
                                                 box: Box) -> Vector
```

X.random_point_in_bounding_box_from_stream_box(stream, box) -> Vector
Returns a random point within the specified bounding box.

Args:
    stream (RandomStream): 
    box (Box): 

Returns:
    Vector:

<a id="unreal.MathLibrary.random_point_in_bounding_box_from_stream"></a>

#### random_point_in_bounding_box_from_stream

```python
@classmethod
def random_point_in_bounding_box_from_stream(cls, stream: RandomStream,
                                             center: Vector,
                                             half_size: Vector) -> Vector
```

X.random_point_in_bounding_box_from_stream(stream, center, half_size) -> Vector
Returns a random point within the specified bounding box using the first vector as an origin and the second as the half size of the AABB.

Args:
    stream (RandomStream): 
    center (Vector): 
    half_size (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.random_point_in_bounding_box_box"></a>

#### random_point_in_bounding_box_box

```python
@classmethod
def random_point_in_bounding_box_box(cls, box: Box) -> Vector
```

X.random_point_in_bounding_box_box(box) -> Vector
Returns a random point within the specified bounding box.

Args:
    box (Box): 

Returns:
    Vector:

<a id="unreal.MathLibrary.random_point_in_bounding_box"></a>

#### random_point_in_bounding_box

```python
@classmethod
def random_point_in_bounding_box(cls, center: Vector,
                                 half_size: Vector) -> Vector
```

X.random_point_in_bounding_box(center, half_size) -> Vector
Returns a random point within the specified bounding box using the first vector as an origin and the second as the box extents.

Args:
    center (Vector): 
    half_size (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.random_integer_in_range_from_stream"></a>

#### random_integer_in_range_from_stream

```python
@classmethod
def random_integer_in_range_from_stream(cls, stream: RandomStream, min: int,
                                        max: int) -> int
```

X.random_integer_in_range_from_stream(stream, min, max) -> int32
Return a random integer between Min and Max (>= Min and <= Max)

Args:
    stream (RandomStream): 
    min (int32): 
    max (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.rand_range_from_stream"></a>

#### rand_range_from_stream

```python
@classmethod
def rand_range_from_stream(cls, stream: RandomStream, min: int,
                           max: int) -> int
```

deprecated: 'rand_range_from_stream' was renamed to 'random_integer_in_range_from_stream'.

<a id="unreal.MathLibrary.random_integer_in_range"></a>

#### random_integer_in_range

```python
@classmethod
def random_integer_in_range(cls, min: int, max: int) -> int
```

X.random_integer_in_range(min, max) -> int32
Return a random integer between Min and Max (>= Min and <= Max)

Args:
    min (int32): 
    max (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.rand_range"></a>

#### rand_range

```python
@classmethod
def rand_range(cls, min: int, max: int) -> int
```

deprecated: 'rand_range' was renamed to 'random_integer_in_range'.

<a id="unreal.MathLibrary.random_integer_from_stream"></a>

#### random_integer_from_stream

```python
@classmethod
def random_integer_from_stream(cls, stream: RandomStream, max: int) -> int
```

X.random_integer_from_stream(stream, max) -> int32
Returns a uniformly distributed random number between 0 and Max - 1

Args:
    stream (RandomStream): 
    max (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.rand_from_stream"></a>

#### rand_from_stream

```python
@classmethod
def rand_from_stream(cls, stream: RandomStream, max: int) -> int
```

deprecated: 'rand_from_stream' was renamed to 'random_integer_from_stream'.

<a id="unreal.MathLibrary.random_integer64_in_range"></a>

#### random_integer64_in_range

```python
@classmethod
def random_integer64_in_range(cls, min: int, max: int) -> int
```

X.random_integer64_in_range(min, max) -> int64
Return a random integer64 between Min and Max (>= Min and <= Max)

Args:
    min (int64): 
    max (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.random_integer64"></a>

#### random_integer64

```python
@classmethod
def random_integer64(cls, max: int) -> int
```

X.random_integer64(max) -> int64
Returns a uniformly distributed random number between 0 and Max - 1

Args:
    max (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.random_integer"></a>

#### random_integer

```python
@classmethod
def random_integer(cls, max: int) -> int
```

X.random_integer(max) -> int32
Returns a uniformly distributed random number between 0 and Max - 1

Args:
    max (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.rand"></a>

#### rand

```python
@classmethod
def rand(cls, max: int) -> int
```

deprecated: 'rand' was renamed to 'random_integer'.

<a id="unreal.MathLibrary.random_float_in_range_from_stream"></a>

#### random_float_in_range_from_stream

```python
@classmethod
def random_float_in_range_from_stream(cls, stream: RandomStream, min: float,
                                      max: float) -> float
```

X.random_float_in_range_from_stream(stream, min, max) -> float
Generate a random number between Min and Max

Args:
    stream (RandomStream): 
    min (float): 
    max (float): 

Returns:
    float:

<a id="unreal.MathLibrary.f_rand_range_from_stream"></a>

#### f_rand_range_from_stream

```python
@classmethod
def f_rand_range_from_stream(cls, stream: RandomStream, min: float,
                             max: float) -> float
```

deprecated: 'f_rand_range_from_stream' was renamed to 'random_float_in_range_from_stream'.

<a id="unreal.MathLibrary.random_float_in_range"></a>

#### random_float_in_range

```python
@classmethod
def random_float_in_range(cls, min: float, max: float) -> float
```

X.random_float_in_range(min, max) -> double
Generate a random number between Min and Max

Args:
    min (double): 
    max (double): 

Returns:
    double:

<a id="unreal.MathLibrary.f_rand_range"></a>

#### f_rand_range

```python
@classmethod
def f_rand_range(cls, min: float, max: float) -> float
```

deprecated: 'f_rand_range' was renamed to 'random_float_in_range'.

<a id="unreal.MathLibrary.random_float_from_stream"></a>

#### random_float_from_stream

```python
@classmethod
def random_float_from_stream(cls, stream: RandomStream) -> float
```

X.random_float_from_stream(stream) -> float
Returns a random float between 0 and 1

Args:
    stream (RandomStream): 

Returns:
    float:

<a id="unreal.MathLibrary.f_rand_from_stream"></a>

#### f_rand_from_stream

```python
@classmethod
def f_rand_from_stream(cls, stream: RandomStream) -> float
```

deprecated: 'f_rand_from_stream' was renamed to 'random_float_from_stream'.

<a id="unreal.MathLibrary.random_float"></a>

#### random_float

```python
@classmethod
def random_float(cls) -> float
```

X.random_float() -> double
Returns a random float between 0 and 1

Returns:
    double:

<a id="unreal.MathLibrary.f_rand"></a>

#### f_rand

```python
@classmethod
def f_rand(cls) -> float
```

deprecated: 'f_rand' was renamed to 'random_float'.

<a id="unreal.MathLibrary.random_bool_with_weight_from_stream"></a>

#### random_bool_with_weight_from_stream

```python
@classmethod
def random_bool_with_weight_from_stream(cls,
                                        random_stream: RandomStream,
                                        weight: float = 0.500000) -> bool
```

X.random_bool_with_weight_from_stream(random_stream, weight=0.500000) -> bool
Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
              Weight = .6 return value = True 60% of the time

Args:
    random_stream (RandomStream): 
    weight (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.random_bool_with_weight"></a>

#### random_bool_with_weight

```python
@classmethod
def random_bool_with_weight(cls, weight: float = 0.500000) -> bool
```

X.random_bool_with_weight(weight=0.500000) -> bool
Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
             Weight = .6 return value = True 60% of the time

Args:
    weight (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.random_bool_from_stream"></a>

#### random_bool_from_stream

```python
@classmethod
def random_bool_from_stream(cls, stream: RandomStream) -> bool
```

X.random_bool_from_stream(stream) -> bool
Returns a random bool

Args:
    stream (RandomStream): 

Returns:
    bool:

<a id="unreal.MathLibrary.rand_bool_from_stream"></a>

#### rand_bool_from_stream

```python
@classmethod
def rand_bool_from_stream(cls, stream: RandomStream) -> bool
```

deprecated: 'rand_bool_from_stream' was renamed to 'random_bool_from_stream'.

<a id="unreal.MathLibrary.random_bool"></a>

#### random_bool

```python
@classmethod
def random_bool(cls) -> bool
```

X.random_bool() -> bool
Returns a uniformly distributed random bool

Returns:
    bool:

<a id="unreal.MathLibrary.rand_bool"></a>

#### rand_bool

```python
@classmethod
def rand_bool(cls) -> bool
```

deprecated: 'rand_bool' was renamed to 'random_bool'.

<a id="unreal.MathLibrary.radians_to_degrees"></a>

#### radians_to_degrees

```python
@classmethod
def radians_to_degrees(cls, a: float) -> float
```

X.radians_to_degrees(a) -> double
Returns degrees value based on the input radians

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.quaternion_spring_interp"></a>

#### quaternion_spring_interp

```python
@classmethod
def quaternion_spring_interp(
    cls,
    current: Quat,
    target: Quat,
    spring_state: QuaternionSpringState,
    stiffness: float,
    critical_damping_factor: float,
    delta_time: float,
    mass: float = 1.000000,
    target_velocity_amount: float = 1.000000,
    initialize_from_target: bool = False
) -> Tuple[Quat, QuaternionSpringState]
```

X.quaternion_spring_interp(current, target, spring_state, stiffness, critical_damping_factor, delta_time, mass=1.000000, target_velocity_amount=1.000000, initialize_from_target=False) -> (Quat, spring_state=QuaternionSpringState)
Uses a simple spring model to interpolate a quaternion from Current to Target.

Args:
    current (Quat): Current value
    target (Quat): Target value
    spring_state (QuaternionSpringState): Data related to spring model (velocity, error, etc..) - Create a unique variable per spring
    stiffness (float): How stiff the spring model is (more stiffness means more oscillation around the target value)
    critical_damping_factor (float): How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
    delta_time (float): Time difference since the last update
    mass (float): Multiplier that acts like mass on a spring
    target_velocity_amount (float): If 1 then the target velocity will be calculated and used, which results following the target more closely/without lag. Values down to zero (recommended when using this to smooth data) will progressively disable this effect.
    initialize_from_target (bool): If set then the current value will be set from the target on the first update

Returns:
    QuaternionSpringState: 

    spring_state (QuaternionSpringState): Data related to spring model (velocity, error, etc..) - Create a unique variable per spring

<a id="unreal.MathLibrary.quat_vector_up"></a>

#### quat_vector_up

```python
@classmethod
def quat_vector_up(cls, q: Quat) -> Vector
```

X.quat_vector_up(q) -> Vector
Get the up direction (Z axis) after it has been rotated by this Quaternion.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_vector_right"></a>

#### quat_vector_right

```python
@classmethod
def quat_vector_right(cls, q: Quat) -> Vector
```

X.quat_vector_right(q) -> Vector
Get the right direction (Y axis) after it has been rotated by this Quaternion.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_vector_forward"></a>

#### quat_vector_forward

```python
@classmethod
def quat_vector_forward(cls, q: Quat) -> Vector
```

X.quat_vector_forward(q) -> Vector
Get the forward direction (X axis) after it has been rotated by this Quaternion.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_unrotate_vector"></a>

#### quat_unrotate_vector

```python
@classmethod
def quat_unrotate_vector(cls, q: Quat, v: Vector) -> Vector
```

X.quat_unrotate_vector(q, v) -> Vector
Rotate a vector by the inverse of this quaternion.

Args:
    q (Quat): 
    v (Vector): the vector to be rotated

Returns:
    Vector: vector after rotation by the inverse of this quaternion.

<a id="unreal.MathLibrary.quat_slerp"></a>

#### quat_slerp

```python
@classmethod
def quat_slerp(cls, a: Quat, b: Quat, alpha: float) -> Quat
```

X.quat_slerp(a, b, alpha) -> Quat
Spherical interpolation between Quaternions. Result is normalized.

Args:
    a (Quat): The starting quat we interp from
    b (Quat): The target quat we interp to
    alpha (double): The interpolation amount, usually 0 to 1.

Returns:
    Quat: Quat after spherical interpolation

<a id="unreal.MathLibrary.quat_size_squared"></a>

#### quat_size_squared

```python
@classmethod
def quat_size_squared(cls, q: Quat) -> float
```

X.quat_size_squared(q) -> float
Get the squared length of the quaternion.

Args:
    q (Quat): 

Returns:
    float: The squared length of the quaternion.

<a id="unreal.MathLibrary.quat_size"></a>

#### quat_size

```python
@classmethod
def quat_size(cls, q: Quat) -> float
```

X.quat_size(q) -> float
Get the length of the quaternion.

Args:
    q (Quat): 

Returns:
    float: The length of the quaternion.

<a id="unreal.MathLibrary.quat_set_from_euler"></a>

#### quat_set_from_euler

```python
@classmethod
def quat_set_from_euler(cls, q: Quat, euler: Vector) -> Quat
```

X.quat_set_from_euler(q, euler) -> Quat
Convert a vector of floating-point Euler angles (in degrees) into a Quaternion.

Args:
    q (Quat): Quaternion to update
    euler (Vector): the Euler angles

Returns:
    Quat: 

    q (Quat): Quaternion to update

<a id="unreal.MathLibrary.quat_set_components"></a>

#### quat_set_components

```python
@classmethod
def quat_set_components(cls, q: Quat, x: float, y: float, z: float,
                        w: float) -> Quat
```

X.quat_set_components(q, x, y, z, w) -> Quat
Set X, Y, Z, W components of Quaternion.

Args:
    q (Quat): 
    x (float): 
    y (float): 
    z (float): 
    w (float): 

Returns:
    Quat: 

    q (Quat):

<a id="unreal.MathLibrary.quat_rotator"></a>

#### quat_rotator

```python
@classmethod
def quat_rotator(cls, q: Quat) -> Rotator
```

X.quat_rotator(q) -> Rotator
Converts to Rotator representation of this Quaternion.

Args:
    q (Quat): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.quat_rotate_vector"></a>

#### quat_rotate_vector

```python
@classmethod
def quat_rotate_vector(cls, q: Quat, v: Vector) -> Vector
```

X.quat_rotate_vector(q, v) -> Vector
Rotate a vector by this quaternion.

Args:
    q (Quat): 
    v (Vector): the vector to be rotated

Returns:
    Vector: vector after rotation

<a id="unreal.MathLibrary.quat_normalized"></a>

#### quat_normalized

```python
@classmethod
def quat_normalized(cls, q: Quat, tolerance: float = 0.000100) -> Quat
```

X.quat_normalized(q, tolerance=0.000100) -> Quat
Get a normalized copy of this quaternion.
If it is too small, returns an identity quaternion.

Args:
    q (Quat): 
    tolerance (float): Minimum squared length of quaternion for normalization.

Returns:
    Quat:

<a id="unreal.MathLibrary.quat_normalize"></a>

#### quat_normalize

```python
@classmethod
def quat_normalize(cls, q: Quat, tolerance: float = 0.000100) -> Quat
```

X.quat_normalize(q, tolerance=0.000100) -> Quat
Normalize this quaternion if it is large enough as compared to the supplied tolerance.
If it is too small then set it to the identity quaternion.

Args:
    q (Quat): 
    tolerance (float): Minimum squared length of quaternion for normalization.

Returns:
    Quat: 

    q (Quat):

<a id="unreal.MathLibrary.quat_make_from_euler"></a>

#### quat_make_from_euler

```python
@classmethod
def quat_make_from_euler(cls, euler: Vector) -> Quat
```

X.quat_make_from_euler(euler) -> Quat
Convert a vector of floating-point Euler angles (in degrees) into a Quaternion.

Args:
    euler (Vector): the Euler angles

Returns:
    Quat: constructed Quat

<a id="unreal.MathLibrary.quat_log"></a>

#### quat_log

```python
@classmethod
def quat_log(cls, q: Quat) -> Quat
```

X.quat_log(q) -> Quat
Quaternion with W=0 and V=theta*v. Used in combination with Exp().

Args:
    q (Quat): 

Returns:
    Quat:

<a id="unreal.MathLibrary.quat_is_normalized"></a>

#### quat_is_normalized

```python
@classmethod
def quat_is_normalized(cls, q: Quat) -> bool
```

X.quat_is_normalized(q) -> bool
Return true if this quaternion is normalized

Args:
    q (Quat): 

Returns:
    bool:

<a id="unreal.MathLibrary.quat_is_non_finite"></a>

#### quat_is_non_finite

```python
@classmethod
def quat_is_non_finite(cls, q: Quat) -> bool
```

X.quat_is_non_finite(q) -> bool
Determine if there are any non-finite values (NaN or Inf) in this Quat.

Args:
    q (Quat): 

Returns:
    bool:

<a id="unreal.MathLibrary.quat_is_identity"></a>

#### quat_is_identity

```python
@classmethod
def quat_is_identity(cls, q: Quat, tolerance: float = 0.000100) -> bool
```

X.quat_is_identity(q, tolerance=0.000100) -> bool
Checks whether this Quaternion is an Identity Quaternion.
Assumes Quaternion tested is normalized.

Args:
    q (Quat): 
    tolerance (float): Error tolerance for comparison with Identity Quaternion.

Returns:
    bool: true if Quaternion is a normalized Identity Quaternion.

<a id="unreal.MathLibrary.quat_is_finite"></a>

#### quat_is_finite

```python
@classmethod
def quat_is_finite(cls, q: Quat) -> bool
```

X.quat_is_finite(q) -> bool
Determine if all the values  are finite (not NaN nor Inf) in this Quat.

Args:
    q (Quat): 

Returns:
    bool:

<a id="unreal.MathLibrary.quat_inversed"></a>

#### quat_inversed

```python
@classmethod
def quat_inversed(cls, q: Quat) -> Quat
```

X.quat_inversed(q) -> Quat
Return an inversed copy of this quaternion.

Args:
    q (Quat): 

Returns:
    Quat:

<a id="unreal.MathLibrary.quat_get_rotation_axis"></a>

#### quat_get_rotation_axis

```python
@classmethod
def quat_get_rotation_axis(cls, q: Quat) -> Vector
```

X.quat_get_rotation_axis(q) -> Vector
Get the axis of rotation of the Quaternion.
This is the axis around which rotation occurs to transform the canonical coordinate system to the target orientation.
For the identity Quaternion which has no such rotation, FVector(1,0,0) is returned.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_get_axis_z"></a>

#### quat_get_axis_z

```python
@classmethod
def quat_get_axis_z(cls, q: Quat) -> Vector
```

X.quat_get_axis_z(q) -> Vector
Get the up direction (Z axis) after it has been rotated by this Quaternion.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_get_axis_y"></a>

#### quat_get_axis_y

```python
@classmethod
def quat_get_axis_y(cls, q: Quat) -> Vector
```

X.quat_get_axis_y(q) -> Vector
Get the right direction (Y axis) after it has been rotated by this Quaternion.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_get_axis_x"></a>

#### quat_get_axis_x

```python
@classmethod
def quat_get_axis_x(cls, q: Quat) -> Vector
```

X.quat_get_axis_x(q) -> Vector
Get the forward direction (X axis) after it has been rotated by this Quaternion.

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_get_angle"></a>

#### quat_get_angle

```python
@classmethod
def quat_get_angle(cls, q: Quat) -> float
```

X.quat_get_angle(q) -> float
Get the angle of this quaternion

Args:
    q (Quat): 

Returns:
    float:

<a id="unreal.MathLibrary.quat_find_between_vectors"></a>

#### quat_find_between_vectors

```python
@classmethod
def quat_find_between_vectors(cls, start: Vector, end: Vector) -> Quat
```

X.quat_find_between_vectors(start, end) -> Quat
Generates the 'smallest' (geodesic) rotation around a sphere between two vectors of arbitrary length.

Args:
    start (Vector): Vector the rotation starts from
    end (Vector): Vector the rotation ends at

Returns:
    Quat: Quat that will rotate from Start to End

<a id="unreal.MathLibrary.quat_find_between_normals"></a>

#### quat_find_between_normals

```python
@classmethod
def quat_find_between_normals(cls, start_normal: Vector,
                              end_normal: Vector) -> Quat
```

X.quat_find_between_normals(start_normal, end_normal) -> Quat
Generates the 'smallest' (geodesic) rotation around a sphere between two normals (assumed to be unit length).

Args:
    start_normal (Vector): 
    end_normal (Vector): 

Returns:
    Quat: Quat that will rotate from Start to End

<a id="unreal.MathLibrary.quat_exp"></a>

#### quat_exp

```python
@classmethod
def quat_exp(cls, q: Quat) -> Quat
```

X.quat_exp(q) -> Quat
Used in combination with Log().
Assumes a quaternion with W=0 and V=theta*v (where |v| = 1).
Exp(q) = (sin(theta)*v, cos(theta))

Args:
    q (Quat): 

Returns:
    Quat:

<a id="unreal.MathLibrary.quat_euler"></a>

#### quat_euler

```python
@classmethod
def quat_euler(cls, q: Quat) -> Vector
```

X.quat_euler(q) -> Vector
Convert a Quaternion into floating-point Euler angles (in degrees).

Args:
    q (Quat): 

Returns:
    Vector:

<a id="unreal.MathLibrary.quat_enforce_shortest_arc_with"></a>

#### quat_enforce_shortest_arc_with

```python
@classmethod
def quat_enforce_shortest_arc_with(cls, a: Quat, b: Quat) -> Quat
```

X.quat_enforce_shortest_arc_with(a, b) -> Quat
Modify the quaternion to ensure that the delta between it and B represents the shortest possible rotation angle.

Args:
    a (Quat): 
    b (Quat): 

Returns:
    Quat: 

    a (Quat):

<a id="unreal.MathLibrary.quat_angular_distance"></a>

#### quat_angular_distance

```python
@classmethod
def quat_angular_distance(cls, a: Quat, b: Quat) -> float
```

X.quat_angular_distance(a, b) -> float
Find the angular distance/difference between two rotation quaternions.

Args:
    a (Quat): 
    b (Quat): Quaternion to find angle distance to

Returns:
    float: angular distance in radians

<a id="unreal.MathLibrary.project_vector_on_to_vector"></a>

#### project_vector_on_to_vector

```python
@classmethod
def project_vector_on_to_vector(cls, v: Vector, target: Vector) -> Vector
```

X.project_vector_on_to_vector(v, target) -> Vector
Projects one vector (V) onto another (Target) and returns the projected vector.
If Target is nearly zero in length, returns the zero vector.

Args:
    v (Vector): Vector to project.
    target (Vector): Vector on which we are projecting.

Returns:
    Vector: V projected on to Target.

<a id="unreal.MathLibrary.project_on_to"></a>

#### project_on_to

```python
@classmethod
def project_on_to(cls, v: Vector, target: Vector) -> Vector
```

deprecated: 'project_on_to' was renamed to 'project_vector_on_to_vector'.

<a id="unreal.MathLibrary.project_vector_on_to_plane"></a>

#### project_vector_on_to_plane

```python
@classmethod
def project_vector_on_to_plane(cls, v: Vector, plane_normal: Vector) -> Vector
```

X.project_vector_on_to_plane(v, plane_normal) -> Vector
Projects a vector onto a plane defined by a normalized vector (PlaneNormal).

Args:
    v (Vector): Vector to project onto the plane.
    plane_normal (Vector): Normal of the plane.

Returns:
    Vector: Vector projected onto the plane.

<a id="unreal.MathLibrary.project_point_on_to_plane"></a>

#### project_point_on_to_plane

```python
@classmethod
def project_point_on_to_plane(cls, point: Vector, plane_base: Vector,
                              plane_normal: Vector) -> Vector
```

X.project_point_on_to_plane(point, plane_base, plane_normal) -> Vector
Projects/snaps a point onto a plane defined by a point on the plane and a plane normal.

Args:
    point (Vector): Point to project onto the plane.
    plane_base (Vector): A point on the plane.
    plane_normal (Vector): Normal of the plane.

Returns:
    Vector: Point projected onto the plane.

<a id="unreal.MathLibrary.points_are_coplanar"></a>

#### points_are_coplanar

```python
@classmethod
def points_are_coplanar(cls,
                        points: Array[Vector],
                        tolerance: float = 0.100000) -> bool
```

X.points_are_coplanar(points, tolerance=0.100000) -> bool
Determines whether a given set of points are coplanar, with a tolerance. Any three points or less are always coplanar.

Args:
    points (Array[Vector]): The set of points to determine coplanarity for.
    tolerance (float): Larger numbers means more variance is allowed.

Returns:
    bool: Whether the points are relatively coplanar, based on the tolerance

<a id="unreal.MathLibrary.perlin_noise1d"></a>

#### perlin_noise1d

```python
@classmethod
def perlin_noise1d(cls, value: float) -> float
```

X.perlin_noise1d(value) -> float
Generates a 1D Perlin noise from the given value.  Returns a continuous random value between -1.0 and 1.0.

Args:
    value (float): The input value that Perlin noise will be generated from.  This is usually a steadily incrementing time value.

Returns:
    float: Perlin noise in the range of -1.0 to 1.0

<a id="unreal.MathLibrary.percent_int_int"></a>

#### percent_int_int

```python
@classmethod
def percent_int_int(cls, a: int, b: int = 1) -> int
```

X.percent_int_int(a, b=1) -> int32
Modulo (A % B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.percent_int64_int64"></a>

#### percent_int64_int64

```python
@classmethod
def percent_int64_int64(cls, a: int, b: int = 1) -> int
```

X.percent_int64_int64(a, b=1) -> int64
Modulo (A % B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.percent_byte_byte"></a>

#### percent_byte_byte

```python
@classmethod
def percent_byte_byte(cls, a: int, b: int = 1) -> int
```

X.percent_byte_byte(a, b=1) -> uint8
Modulo (A % B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.or_int_int"></a>

#### or_int_int

```python
@classmethod
def or_int_int(cls, a: int, b: int) -> int
```

X.or_int_int(a, b) -> int32
Bitwise OR (A | B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.or_int64_int64"></a>

#### or_int64_int64

```python
@classmethod
def or_int64_int64(cls, a: int, b: int) -> int
```

X.or_int64_int64(a, b) -> int64
Bitwise OR (A | B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.now"></a>

#### now

```python
@classmethod
def now(cls) -> DateTime
```

X.now() -> DateTime
Returns the local date and time on this computer

Returns:
    DateTime:

<a id="unreal.MathLibrary.not_equal_exactly_vector_vector"></a>

#### not_equal_exactly_vector_vector

```python
@classmethod
def not_equal_exactly_vector_vector(cls, a: Vector, b: Vector) -> bool
```

X.not_equal_exactly_vector_vector(a, b) -> bool
Returns true if vector A is not equal to vector B (A != B)

Args:
    a (Vector): 
    b (Vector): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_exactly_vector4_vector4"></a>

#### not_equal_exactly_vector4_vector4

```python
@classmethod
def not_equal_exactly_vector4_vector4(cls, a: Vector4, b: Vector4) -> bool
```

X.not_equal_exactly_vector4_vector4(a, b) -> bool
Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_exactly_vector2d_vector2d"></a>

#### not_equal_exactly_vector2d_vector2d

```python
@classmethod
def not_equal_exactly_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> bool
```

X.not_equal_exactly_vector2d_vector2d(a, b) -> bool
Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_vector_vector"></a>

#### not_equal_vector_vector

```python
@classmethod
def not_equal_vector_vector(cls,
                            a: Vector,
                            b: Vector,
                            error_tolerance: float = 0.000100) -> bool
```

X.not_equal_vector_vector(a, b, error_tolerance=0.000100) -> bool
Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Args:
    a (Vector): 
    b (Vector): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_vector4_vector4"></a>

#### not_equal_vector4_vector4

```python
@classmethod
def not_equal_vector4_vector4(cls,
                              a: Vector4,
                              b: Vector4,
                              error_tolerance: float = 0.000100) -> bool
```

X.not_equal_vector4_vector4(a, b, error_tolerance=0.000100) -> bool
Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Args:
    a (Vector4): 
    b (Vector4): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_vector2d_vector2d"></a>

#### not_equal_vector2d_vector2d

```python
@classmethod
def not_equal_vector2d_vector2d(cls,
                                a: Vector2D,
                                b: Vector2D,
                                error_tolerance: float = 0.000100) -> bool
```

X.not_equal_vector2d_vector2d(a, b, error_tolerance=0.000100) -> bool
Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

Args:
    a (Vector2D): 
    b (Vector2D): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_timespan_timespan"></a>

#### not_equal_timespan_timespan

```python
@classmethod
def not_equal_timespan_timespan(cls, a: Timespan, b: Timespan) -> bool
```

X.not_equal_timespan_timespan(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_rotator_rotator"></a>

#### not_equal_rotator_rotator

```python
@classmethod
def not_equal_rotator_rotator(cls,
                              a: Rotator,
                              b: Rotator,
                              error_tolerance: float = 0.000100) -> bool
```

X.not_equal_rotator_rotator(a, b, error_tolerance=0.000100) -> bool
Returns true if rotator A is not equal to rotator B (A != B) within a specified error tolerance

Args:
    a (Rotator): 
    b (Rotator): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_quat_quat"></a>

#### not_equal_quat_quat

```python
@classmethod
def not_equal_quat_quat(cls,
                        a: Quat,
                        b: Quat,
                        error_tolerance: float = 0.000100) -> bool
```

X.not_equal_quat_quat(a, b, error_tolerance=0.000100) -> bool
Returns true if Quat A is not equal to Quat B (A != B) within a specified error tolerance

Args:
    a (Quat): 
    b (Quat): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_object_object"></a>

#### not_equal_object_object

```python
@classmethod
def not_equal_object_object(cls, a: Object, b: Object) -> bool
```

X.not_equal_object_object(a, b) -> bool
Returns true if A and B are not equal (A != B)

Args:
    a (Object): 
    b (Object): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_name_name"></a>

#### not_equal_name_name

```python
@classmethod
def not_equal_name_name(cls, a: Name, b: Name) -> bool
```

X.not_equal_name_name(a, b) -> bool
Returns true if A and B are not equal (A != B)

Args:
    a (Name): 
    b (Name): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_matrix_matrix"></a>

#### not_equal_matrix_matrix

```python
@classmethod
def not_equal_matrix_matrix(cls,
                            a: Matrix,
                            b: Matrix,
                            tolerance: float = 0.000100) -> bool
```

X.not_equal_matrix_matrix(a, b, tolerance=0.000100) -> bool
Checks whether another Matrix is not equal to this, within specified tolerance.

Args:
    a (Matrix): 
    b (Matrix): 
    tolerance (float): 

Returns:
    bool: true if two Matrix are not equal, within specified tolerance, otherwise false.

<a id="unreal.MathLibrary.not_equal_linear_color_linear_color"></a>

#### not_equal_linear_color_linear_color

```python
@classmethod
def not_equal_linear_color_linear_color(cls, a: LinearColor,
                                        b: LinearColor) -> bool
```

X.not_equal_linear_color_linear_color(a, b) -> bool
Returns true if linear color A is not equal to linear color B (A != B) within a specified error tolerance

Args:
    a (LinearColor): 
    b (LinearColor): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_int_point_int_point"></a>

#### not_equal_int_point_int_point

```python
@classmethod
def not_equal_int_point_int_point(cls, a: IntPoint, b: IntPoint) -> bool
```

X.not_equal_int_point_int_point(a, b) -> bool
Returns true if IntPoint A is NOT equal to IntPoint B (A != B)

Args:
    a (IntPoint): 
    b (IntPoint): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_int_int"></a>

#### not_equal_int_int

```python
@classmethod
def not_equal_int_int(cls, a: int, b: int) -> bool
```

X.not_equal_int_int(a, b) -> bool
Returns true if A is not equal to B (A != B)

Args:
    a (int32): 
    b (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_int64_int64"></a>

#### not_equal_int64_int64

```python
@classmethod
def not_equal_int64_int64(cls, a: int, b: int) -> bool
```

X.not_equal_int64_int64(a, b) -> bool
Returns true if A is not equal to B (A != B)

Args:
    a (int64): 
    b (int64): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_double_double"></a>

#### not_equal_double_double

```python
@classmethod
def not_equal_double_double(cls, a: float, b: float) -> bool
```

X.not_equal_double_double(a, b) -> bool
Returns true if A does not equal B (A != B)

Args:
    a (double): 
    b (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_float_float"></a>

#### not_equal_float_float

```python
@classmethod
def not_equal_float_float(cls, a: float, b: float) -> bool
```

deprecated: 'not_equal_float_float' was renamed to 'not_equal_double_double'.

<a id="unreal.MathLibrary.not_equal_date_time_date_time"></a>

#### not_equal_date_time_date_time

```python
@classmethod
def not_equal_date_time_date_time(cls, a: DateTime, b: DateTime) -> bool
```

X.not_equal_date_time_date_time(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_class_class"></a>

#### not_equal_class_class

```python
@classmethod
def not_equal_class_class(cls, a: Class, b: Class) -> bool
```

X.not_equal_class_class(a, b) -> bool
Returns true if A and B are not equal (A != B)

Args:
    a (type(Class)): 
    b (type(Class)): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_byte_byte"></a>

#### not_equal_byte_byte

```python
@classmethod
def not_equal_byte_byte(cls, a: int, b: int) -> bool
```

X.not_equal_byte_byte(a, b) -> bool
Returns true if A is not equal to B (A != B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_equal_bool_bool"></a>

#### not_equal_bool_bool

```python
@classmethod
def not_equal_bool_bool(cls, a: bool, b: bool) -> bool
```

X.not_equal_bool_bool(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_pre_bool"></a>

#### not_pre_bool

```python
@classmethod
def not_pre_bool(cls, a: bool) -> bool
```

X.not_pre_bool(a) -> bool
Returns the logical complement of the Boolean value (NOT A)

Args:
    a (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.not_int64"></a>

#### not_int64

```python
@classmethod
def not_int64(cls, a: int) -> int
```

X.not_int64(a) -> int64
Bitwise NOT (~A)

Args:
    a (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.not_int"></a>

#### not_int

```python
@classmethod
def not_int(cls, a: int) -> int
```

X.not_int(a) -> int32
Bitwise NOT (~A)

Args:
    a (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.normal_safe2d"></a>

#### normal_safe2d

```python
@classmethod
def normal_safe2d(cls, a: Vector2D, tolerance: float = 0.000000) -> Vector2D
```

X.normal_safe2d(a, tolerance=0.000000) -> Vector2D
Gets a normalized copy of the vector, checking it is safe to do so based on the length.
Returns zero vector if vector length is too small to safely normalize.

Args:
    a (Vector2D): 
    tolerance (float): Minimum squared length of vector for normalization.

Returns:
    Vector2D: A normalized copy of the vector if safe, (0,0) otherwise.

<a id="unreal.MathLibrary.normalize_to_range"></a>

#### normalize_to_range

```python
@classmethod
def normalize_to_range(cls, value: float, range_min: float,
                       range_max: float) -> float
```

X.normalize_to_range(value, range_min, range_max) -> double
Returns Value normalized to the given range.  (e.g. 20 normalized to the range 10->50 would result in 0.25)

Args:
    value (double): 
    range_min (double): 
    range_max (double): 

Returns:
    double:

<a id="unreal.MathLibrary.inverse_lerp"></a>

#### inverse_lerp

```python
@classmethod
def inverse_lerp(cls, value: float, range_min: float,
                 range_max: float) -> float
```

deprecated: 'inverse_lerp' was renamed to 'normalize_to_range'.

<a id="unreal.MathLibrary.normalized_delta_rotator"></a>

#### normalized_delta_rotator

```python
@classmethod
def normalized_delta_rotator(cls, a: Rotator, b: Rotator) -> Rotator
```

X.normalized_delta_rotator(a, b) -> Rotator
Normalized A-B

Args:
    a (Rotator): 
    b (Rotator): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.normalize_axis"></a>

#### normalize_axis

```python
@classmethod
def normalize_axis(cls, angle: float) -> float
```

X.normalize_axis(angle) -> float
Clamps an angle to the range of [-180, 180].

Args:
    angle (float): The Angle to clamp.

Returns:
    float: The clamped angle.

<a id="unreal.MathLibrary.normalize2d"></a>

#### normalize2d

```python
@classmethod
def normalize2d(cls, a: Vector2D, tolerance: float = 0.000000) -> Vector2D
```

X.normalize2d(a, tolerance=0.000000) -> Vector2D
Normalize this vector in-place if it is large enough, set it to (0,0) otherwise.
see: NormalSafe2D()

Args:
    a (Vector2D): 
    tolerance (float): Minimum squared length of vector for normalization.

Returns:
    Vector2D: 

    a (Vector2D):

<a id="unreal.MathLibrary.normal2d"></a>

#### normal2d

```python
@classmethod
def normal2d(cls, a: Vector2D) -> Vector2D
```

X.normal2d(a) -> Vector2D
Returns a unit normal version of the 2D vector

Args:
    a (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.normal"></a>

#### normal

```python
@classmethod
def normal(cls, a: Vector, tolerance: float = 0.000100) -> Vector
```

X.normal(a, tolerance=0.000100) -> Vector
Gets a normalized unit copy of the vector, ensuring it is safe to do so based on the length.
Returns zero vector if vector length is too small to safely normalize.

Args:
    a (Vector): 
    tolerance (float): Minimum squared vector length.

Returns:
    Vector: A normalized copy if safe, (0,0,0) otherwise.

<a id="unreal.MathLibrary.negate_vector"></a>

#### negate_vector

```python
@classmethod
def negate_vector(cls, a: Vector) -> Vector
```

X.negate_vector(a) -> Vector
Negate a vector.

Args:
    a (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.negate_rotator"></a>

#### negate_rotator

```python
@classmethod
def negate_rotator(cls, a: Rotator) -> Rotator
```

X.negate_rotator(a) -> Rotator
Negate a rotator

Args:
    a (Rotator): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.negated2d"></a>

#### negated2d

```python
@classmethod
def negated2d(cls, a: Vector2D) -> Vector2D
```

X.negated2d(a) -> Vector2D
Gets a negated copy of the vector.

Args:
    a (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.nearly_equal_transform_transform"></a>

#### nearly_equal_transform_transform

```python
@classmethod
def nearly_equal_transform_transform(
        cls,
        a: Transform,
        b: Transform,
        location_tolerance: float = 0.000100,
        rotation_tolerance: float = 0.000100,
        scale3d_tolerance: float = 0.000100) -> bool
```

X.nearly_equal_transform_transform(a, b, location_tolerance=0.000100, rotation_tolerance=0.000100, scale3d_tolerance=0.000100) -> bool
Returns true if transform A is nearly equal to B

Args:
    a (Transform): 
    b (Transform): 
    location_tolerance (float): How close position of transforms need to be to be considered equal
    rotation_tolerance (float): How close rotations of transforms need to be to be considered equal
    scale3d_tolerance (float): How close scale of transforms need to be to be considered equal

Returns:
    bool:

<a id="unreal.MathLibrary.nearly_equal_float_float"></a>

#### nearly_equal_float_float

```python
@classmethod
def nearly_equal_float_float(cls,
                             a: float,
                             b: float,
                             error_tolerance: float = 0.000001) -> bool
```

X.nearly_equal_float_float(a, b, error_tolerance=0.000001) -> bool
Returns true if A is nearly equal to B (|A - B| < ErrorTolerance)

Args:
    a (double): 
    b (double): 
    error_tolerance (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.multiply_multiply_float_float"></a>

#### multiply_multiply_float_float

```python
@classmethod
def multiply_multiply_float_float(cls, base: float, exp: float) -> float
```

X.multiply_multiply_float_float(base, exp) -> double
Power (Base to the Exp-th power)

Args:
    base (double): 
    exp (double): 

Returns:
    double:

<a id="unreal.MathLibrary.multiply_by_pi"></a>

#### multiply_by_pi

```python
@classmethod
def multiply_by_pi(cls, value: float) -> float
```

X.multiply_by_pi(value) -> double
Multiplies the input value by pi.

Args:
    value (double): 

Returns:
    double:

<a id="unreal.MathLibrary.multiply_vector_vector"></a>

#### multiply_vector_vector

```python
@classmethod
def multiply_vector_vector(cls, a: Vector, b: Vector) -> Vector
```

X.multiply_vector_vector(a, b) -> Vector
Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z})

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.multiply_vector_int"></a>

#### multiply_vector_int

```python
@classmethod
def multiply_vector_int(cls, a: Vector, b: int) -> Vector
```

X.multiply_vector_int(a, b) -> Vector
Scales Vector A by B

Args:
    a (Vector): 
    b (int32): 

Returns:
    Vector:

<a id="unreal.MathLibrary.multiply_vector_float"></a>

#### multiply_vector_float

```python
@classmethod
def multiply_vector_float(cls, a: Vector, b: float) -> Vector
```

X.multiply_vector_float(a, b) -> Vector
Scales Vector A by B

Args:
    a (Vector): 
    b (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.multiply_vector4_vector4"></a>

#### multiply_vector4_vector4

```python
@classmethod
def multiply_vector4_vector4(cls, a: Vector4, b: Vector4) -> Vector4
```

X.multiply_vector4_vector4(a, b) -> Vector4
Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z, A.w*B.w})

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.multiply_vector2d_vector2d"></a>

#### multiply_vector2d_vector2d

```python
@classmethod
def multiply_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> Vector2D
```

X.multiply_vector2d_vector2d(a, b) -> Vector2D
Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y})

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.multiply_vector2d_float"></a>

#### multiply_vector2d_float

```python
@classmethod
def multiply_vector2d_float(cls, a: Vector2D, b: float) -> Vector2D
```

X.multiply_vector2d_float(a, b) -> Vector2D
Returns Vector A scaled by B

Args:
    a (Vector2D): 
    b (double): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.multiply_timespan_float"></a>

#### multiply_timespan_float

```python
@classmethod
def multiply_timespan_float(cls, a: Timespan, scalar: float) -> Timespan
```

X.multiply_timespan_float(a, scalar) -> Timespan
Scalar multiplication (A * s)

Args:
    a (Timespan): 
    scalar (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.multiply_rotator_int"></a>

#### multiply_rotator_int

```python
@classmethod
def multiply_rotator_int(cls, a: Rotator, b: int) -> Rotator
```

X.multiply_rotator_int(a, b) -> Rotator
Returns rotator representing rotator A scaled by B

Args:
    a (Rotator): 
    b (int32): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.multiply_rotator_float"></a>

#### multiply_rotator_float

```python
@classmethod
def multiply_rotator_float(cls, a: Rotator, b: float) -> Rotator
```

X.multiply_rotator_float(a, b) -> Rotator
Returns rotator representing rotator A scaled by B

Args:
    a (Rotator): 
    b (float): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.multiply_quat_quat"></a>

#### multiply_quat_quat

```python
@classmethod
def multiply_quat_quat(cls, a: Quat, b: Quat) -> Quat
```

X.multiply_quat_quat(a, b) -> Quat
Gets the result of multiplying two quaternions (A * B).

Order matters when composing quaternions: C = A * B will yield a quaternion C that logically
first applies B then A to any subsequent transformation (right first, then left).

Args:
    a (Quat): 
    b (Quat): The Quaternion to multiply by.

Returns:
    Quat: The result of multiplication (A * B).

<a id="unreal.MathLibrary.multiply_matrix_matrix"></a>

#### multiply_matrix_matrix

```python
@classmethod
def multiply_matrix_matrix(cls, a: Matrix, b: Matrix) -> Matrix
```

X.multiply_matrix_matrix(a, b) -> Matrix
Gets the result of multiplying a Matrix to this.

Args:
    a (Matrix): 
    b (Matrix): 

Returns:
    Matrix: The result of multiplication.

<a id="unreal.MathLibrary.multiply_matrix_float"></a>

#### multiply_matrix_float

```python
@classmethod
def multiply_matrix_float(cls, a: Matrix, b: float) -> Matrix
```

X.multiply_matrix_float(a, b) -> Matrix
Multiplies all values of the matrix by a float.
If your Matrix represents a Transform that you wish to scale you should use Apply Scale instead

Args:
    a (Matrix): 
    b (double): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.multiply_linear_color_linear_color"></a>

#### multiply_linear_color_linear_color

```python
@classmethod
def multiply_linear_color_linear_color(cls, a: LinearColor,
                                       b: LinearColor) -> LinearColor
```

X.multiply_linear_color_linear_color(a, b) -> LinearColor
Element-wise multiplication of two linear colors (R*R, G*G, B*B, A*A)

Args:
    a (LinearColor): 
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.multiply_linear_color_float"></a>

#### multiply_linear_color_float

```python
@classmethod
def multiply_linear_color_float(cls, a: LinearColor, b: float) -> LinearColor
```

X.multiply_linear_color_float(a, b) -> LinearColor
Element-wise multiplication of a linear color by a float (F*R, F*G, F*B, F*A)

Args:
    a (LinearColor): 
    b (float): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.multiply_int_point_int_point"></a>

#### multiply_int_point_int_point

```python
@classmethod
def multiply_int_point_int_point(cls, a: IntPoint, b: IntPoint) -> IntPoint
```

X.multiply_int_point_int_point(a, b) -> IntPoint
Returns IntPoint A multiplied by B

Args:
    a (IntPoint): 
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.multiply_int_point_int"></a>

#### multiply_int_point_int

```python
@classmethod
def multiply_int_point_int(cls, a: IntPoint, b: int) -> IntPoint
```

X.multiply_int_point_int(a, b) -> IntPoint
Multiplication (A * B)

Args:
    a (IntPoint): 
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.multiply_int_int"></a>

#### multiply_int_int

```python
@classmethod
def multiply_int_int(cls, a: int, b: int) -> int
```

X.multiply_int_int(a, b) -> int32
Multiplication (A * B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.multiply_int_float"></a>

#### multiply_int_float

```python
@classmethod
def multiply_int_float(cls, a: int, b: float) -> float
```

X.multiply_int_float(a, b) -> double
Multiplication (A * B)

Args:
    a (int32): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.multiply_int64_int64"></a>

#### multiply_int64_int64

```python
@classmethod
def multiply_int64_int64(cls, a: int, b: int) -> int
```

X.multiply_int64_int64(a, b) -> int64
Multiplication (A * B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.multiply_double_double"></a>

#### multiply_double_double

```python
@classmethod
def multiply_double_double(cls, a: float, b: float) -> float
```

X.multiply_double_double(a, b) -> double
Multiplication (A * B)

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.multiply_float_float"></a>

#### multiply_float_float

```python
@classmethod
def multiply_float_float(cls, a: float, b: float) -> float
```

deprecated: 'multiply_float_float' was renamed to 'multiply_double_double'.

<a id="unreal.MathLibrary.multiply_byte_byte"></a>

#### multiply_byte_byte

```python
@classmethod
def multiply_byte_byte(cls, a: int, b: int) -> int
```

X.multiply_byte_byte(a, b) -> uint8
Multiplication (A * B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.mirror_vector_by_normal"></a>

#### mirror_vector_by_normal

```python
@classmethod
def mirror_vector_by_normal(cls, vect: Vector, normal: Vector) -> Vector
```

X.mirror_vector_by_normal(vect, normal) -> Vector
Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
Produces a result like shining a laser at a mirror!

Args:
    vect (Vector): Direction vector the ray is coming from.
    normal (Vector): A normal of the surface the ray should be reflected on.

Returns:
    Vector: Reflected vector.

<a id="unreal.MathLibrary.min_of_int_array"></a>

#### min_of_int_array

```python
@classmethod
def min_of_int_array(cls, int_array: Array[int]) -> Tuple[int, int]
```

X.min_of_int_array(int_array) -> (index_of_min_value=int32, min_value=int32)
Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Args:
    int_array (Array[int32]): 

Returns:
    tuple: 

    index_of_min_value (int32): 

    min_value (int32):

<a id="unreal.MathLibrary.min_of_float_array"></a>

#### min_of_float_array

```python
@classmethod
def min_of_float_array(cls, float_array: Array[float]) -> Tuple[int, float]
```

X.min_of_float_array(float_array) -> (index_of_min_value=int32, min_value=float)
Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Args:
    float_array (Array[float]): 

Returns:
    tuple: 

    index_of_min_value (int32): 

    min_value (float):

<a id="unreal.MathLibrary.min_of_byte_array"></a>

#### min_of_byte_array

```python
@classmethod
def min_of_byte_array(cls, byte_array: Array[int]) -> Tuple[int, int]
```

X.min_of_byte_array(byte_array) -> (index_of_min_value=int32, min_value=uint8)
Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Args:
    byte_array (Array[uint8]): 

Returns:
    tuple: 

    index_of_min_value (int32): 

    min_value (uint8):

<a id="unreal.MathLibrary.min_int64"></a>

#### min_int64

```python
@classmethod
def min_int64(cls, a: int, b: int) -> int
```

X.min_int64(a, b) -> int64
Returns the minimum value of A and B

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.min_area_rectangle"></a>

#### min_area_rectangle

```python
@classmethod
def min_area_rectangle(
        cls,
        world_context_object: Object,
        points: Array[Vector],
        sample_surface_normal: Vector,
        debug_draw: bool = False) -> Tuple[Vector, Rotator, float, float]
```

X.min_area_rectangle(world_context_object, points, sample_surface_normal, debug_draw=False) -> (out_rect_center=Vector, out_rect_rotation=Rotator, out_rect_length_x=float, out_rect_length_y=float)
Finds the minimum area rectangle that encloses a set of coplanar points.
Uses the exhaustive search algorithm in http://www.geometrictools.com/Documentation/MinimumAreaRectangle.pdf

Args:
    world_context_object (Object): Pointer to world context; only used when debug draw is enabled
    points (Array[Vector]): Points to enclose in the rectangle; need to be within the same plane for correct results
    sample_surface_normal (Vector): Normal indicating the surface direction for the points
    debug_draw (bool): Draws the output rectangle for debugging purposes provided the world context is set as well

Returns:
    tuple: 

    out_rect_center (Vector): Translation for the output rectangle from the origin

    out_rect_rotation (Rotator): Rotation for the output rectangle from the XY plane

    out_rect_length_x (float): Length of the output rectangle along the X axis before rotation

    out_rect_length_y (float): Length of the output rectangle along the Y axis before rotation

<a id="unreal.MathLibrary.minimum_area_rectangle"></a>

#### minimum_area_rectangle

```python
@classmethod
def minimum_area_rectangle(
        cls,
        world_context_object: Object,
        points: Array[Vector],
        sample_surface_normal: Vector,
        debug_draw: bool = False) -> Tuple[Vector, Rotator, float, float]
```

deprecated: 'minimum_area_rectangle' was renamed to 'min_area_rectangle'.

<a id="unreal.MathLibrary.min"></a>

#### min

```python
@classmethod
def min(cls, a: int, b: int) -> int
```

X.min(a, b) -> int32
Returns the minimum value of A and B

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.median_of_int_array"></a>

#### median_of_int_array

```python
@classmethod
def median_of_int_array(cls, int_array: Array[int]) -> float
```

X.median_of_int_array(int_array) -> float
Returns median of all array entries. Returns value of 0 if the supplied array is empty.

Args:
    int_array (Array[int32]): 

Returns:
    float: 

    median_value (float):

<a id="unreal.MathLibrary.max_of_int_array"></a>

#### max_of_int_array

```python
@classmethod
def max_of_int_array(cls, int_array: Array[int]) -> Tuple[int, int]
```

X.max_of_int_array(int_array) -> (index_of_max_value=int32, max_value=int32)
Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Args:
    int_array (Array[int32]): 

Returns:
    tuple: 

    index_of_max_value (int32): 

    max_value (int32):

<a id="unreal.MathLibrary.max_of_float_array"></a>

#### max_of_float_array

```python
@classmethod
def max_of_float_array(cls, float_array: Array[float]) -> Tuple[int, float]
```

X.max_of_float_array(float_array) -> (index_of_max_value=int32, max_value=float)
Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Args:
    float_array (Array[float]): 

Returns:
    tuple: 

    index_of_max_value (int32): 

    max_value (float):

<a id="unreal.MathLibrary.max_of_byte_array"></a>

#### max_of_byte_array

```python
@classmethod
def max_of_byte_array(cls, byte_array: Array[int]) -> Tuple[int, int]
```

X.max_of_byte_array(byte_array) -> (index_of_max_value=int32, max_value=uint8)
Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

Args:
    byte_array (Array[uint8]): 

Returns:
    tuple: 

    index_of_max_value (int32): 

    max_value (uint8):

<a id="unreal.MathLibrary.max_int64"></a>

#### max_int64

```python
@classmethod
def max_int64(cls, a: int, b: int) -> int
```

X.max_int64(a, b) -> int64
Returns the maximum value of A and B

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.max"></a>

#### max

```python
@classmethod
def max(cls, a: int, b: int) -> int
```

X.max(a, b) -> int32
Returns the maximum value of A and B

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.matrix_transform_vector4"></a>

#### matrix_transform_vector4

```python
@classmethod
def matrix_transform_vector4(cls, m: Matrix, v: Vector4) -> Vector4
```

X.matrix_transform_vector4(m, v) -> Vector4
Transform a vector by the matrix.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    v (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.matrix_transform_vector"></a>

#### matrix_transform_vector

```python
@classmethod
def matrix_transform_vector(cls, m: Matrix, v: Vector) -> Vector4
```

X.matrix_transform_vector(m, v) -> Vector4
Transform a direction vector - will not take into account translation part of the FMatrix.
If you want to transform a surface normal (or plane) and correctly account for non-uniform scaling you should use TransformByUsingAdjointT.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    v (Vector): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.matrix_transform_position"></a>

#### matrix_transform_position

```python
@classmethod
def matrix_transform_position(cls, m: Matrix, v: Vector) -> Vector4
```

X.matrix_transform_position(m, v) -> Vector4
Transform a location - will take into account translation part of the FMatrix.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    v (Vector): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.matrix_to_quat"></a>

#### matrix_to_quat

```python
@classmethod
def matrix_to_quat(cls, m: Matrix) -> Quat
```

X.matrix_to_quat(m) -> Quat
Transform a rotation matrix into a quaternion.
(Assumes Matrix represents a transform)
warning: rotation part will need to be unit length for this to be right!

Args:
    m (Matrix): 

Returns:
    Quat:

<a id="unreal.MathLibrary.matrix_set_origin"></a>

#### matrix_set_origin

```python
@classmethod
def matrix_set_origin(cls, m: Matrix, new_origin: Vector) -> Matrix
```

X.matrix_set_origin(m, new_origin) -> Matrix
Set the origin of the coordinate system to the given vector
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    new_origin (Vector): 

Returns:
    Matrix: 

    m (Matrix):

<a id="unreal.MathLibrary.matrix_set_column"></a>

#### matrix_set_column

```python
@classmethod
def matrix_set_column(cls, m: Matrix, column: MatrixColumns,
                      value: Vector) -> Matrix
```

X.matrix_set_column(m, column, value) -> Matrix
Matrix Set Column

Args:
    m (Matrix): 
    column (MatrixColumns): 
    value (Vector): 

Returns:
    Matrix: 

    m (Matrix):

<a id="unreal.MathLibrary.matrix_set_axis"></a>

#### matrix_set_axis

```python
@classmethod
def matrix_set_axis(cls, m: Matrix, axis: AxisType,
                    axis_vector: Vector) -> Matrix
```

X.matrix_set_axis(m, axis, axis_vector) -> Matrix
set an axis of this matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    axis (AxisType): vector of the axis
    axis_vector (Vector): 

Returns:
    Matrix: 

    m (Matrix):

<a id="unreal.MathLibrary.matrix_scale_translation"></a>

#### matrix_scale_translation

```python
@classmethod
def matrix_scale_translation(cls, m: Matrix, scale3d: Vector) -> Matrix
```

X.matrix_scale_translation(m, scale3d) -> Matrix
Scale the translation part of the matrix by the supplied vector.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    scale3d (Vector): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_remove_translation"></a>

#### matrix_remove_translation

```python
@classmethod
def matrix_remove_translation(cls, m: Matrix) -> Matrix
```

X.matrix_remove_translation(m) -> Matrix
Remove any translation from this matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_remove_scaling"></a>

#### matrix_remove_scaling

```python
@classmethod
def matrix_remove_scaling(cls,
                          m: Matrix,
                          tolerance: float = 0.000000) -> Matrix
```

X.matrix_remove_scaling(m, tolerance=0.000000) -> Matrix
Remove any scaling from this matrix (ie magnitude of each row is 1) with error Tolerance
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    tolerance (float): 

Returns:
    Matrix: 

    m (Matrix):

<a id="unreal.MathLibrary.matrix_mirror"></a>

#### matrix_mirror

```python
@classmethod
def matrix_mirror(cls, m: Matrix, mirror_axis: AxisType,
                  flip_axis: AxisType) -> Matrix
```

X.matrix_mirror(m, mirror_axis, flip_axis) -> Matrix
Utility for mirroring this transform across a certain plane, and flipping one of the axis as well.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    mirror_axis (AxisType): 
    flip_axis (AxisType): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_inverse_transform_vector"></a>

#### matrix_inverse_transform_vector

```python
@classmethod
def matrix_inverse_transform_vector(cls, m: Matrix, v: Vector) -> Vector
```

X.matrix_inverse_transform_vector(m, v) -> Vector
Transform a direction vector by the inverse of this matrix - will not take into account translation part.
If you want to transform a surface normal (or plane) and correctly account for non-uniform scaling you should use TransformByUsingAdjointT with adjoint of matrix inverse.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    v (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.matrix_inverse_transform_position"></a>

#### matrix_inverse_transform_position

```python
@classmethod
def matrix_inverse_transform_position(cls, m: Matrix, v: Vector) -> Vector
```

X.matrix_inverse_transform_position(m, v) -> Vector
Inverts the matrix and then transforms V - correctly handles scaling in this matrix.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    v (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.matrix_get_unit_axis"></a>

#### matrix_get_unit_axis

```python
@classmethod
def matrix_get_unit_axis(cls, m: Matrix, axis: AxisType) -> Vector
```

X.matrix_get_unit_axis(m, axis) -> Vector
get unit length axis of this matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    axis (AxisType): 

Returns:
    Vector: vector of the axis

<a id="unreal.MathLibrary.matrix_get_unit_axes"></a>

#### matrix_get_unit_axes

```python
@classmethod
def matrix_get_unit_axes(cls, m: Matrix) -> Tuple[Vector, Vector, Vector]
```

X.matrix_get_unit_axes(m) -> (x=Vector, y=Vector, z=Vector)
get unit length axes of this matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 

Returns:
    tuple: 

    x (Vector): axes returned to this param

    y (Vector): axes returned to this param

    z (Vector): axes returned to this param

<a id="unreal.MathLibrary.matrix_get_transposed"></a>

#### matrix_get_transposed

```python
@classmethod
def matrix_get_transposed(cls, m: Matrix) -> Matrix
```

X.matrix_get_transposed(m) -> Matrix
Transpose.

Args:
    m (Matrix): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_get_transpose_adjoint"></a>

#### matrix_get_transpose_adjoint

```python
@classmethod
def matrix_get_transpose_adjoint(cls, m: Matrix) -> Matrix
```

X.matrix_get_transpose_adjoint(m) -> Matrix
Get the Transose Adjoint of the Matrix.

Args:
    m (Matrix): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_get_scale_vector"></a>

#### matrix_get_scale_vector

```python
@classmethod
def matrix_get_scale_vector(cls,
                            m: Matrix,
                            tolerance: float = 0.000000) -> Vector
```

X.matrix_get_scale_vector(m, tolerance=0.000000) -> Vector
return a 3D scale vector calculated from this matrix (where each component is the magnitude of a row vector) with error Tolerance.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    tolerance (float): 

Returns:
    Vector:

<a id="unreal.MathLibrary.matrix_get_scaled_axis"></a>

#### matrix_get_scaled_axis

```python
@classmethod
def matrix_get_scaled_axis(cls, m: Matrix, axis: AxisType) -> Vector
```

X.matrix_get_scaled_axis(m, axis) -> Vector
get axis of this matrix scaled by the scale of the matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    axis (AxisType): 

Returns:
    Vector: vector of the axis

<a id="unreal.MathLibrary.matrix_get_scaled_axes"></a>

#### matrix_get_scaled_axes

```python
@classmethod
def matrix_get_scaled_axes(cls, m: Matrix) -> Tuple[Vector, Vector, Vector]
```

X.matrix_get_scaled_axes(m) -> (x=Vector, y=Vector, z=Vector)
get axes of this matrix scaled by the scale of the matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 

Returns:
    tuple: 

    x (Vector): axes returned to this param

    y (Vector): axes returned to this param

    z (Vector): axes returned to this param

<a id="unreal.MathLibrary.matrix_get_rot_determinant"></a>

#### matrix_get_rot_determinant

```python
@classmethod
def matrix_get_rot_determinant(cls, m: Matrix) -> float
```

X.matrix_get_rot_determinant(m) -> float


Args:
    m (Matrix): 

Returns:
    float: the determinant of rotation 3x3 matrix (Assumes Top Left 3x3 Submatrix represents a Rotation)

<a id="unreal.MathLibrary.matrix_get_rotator"></a>

#### matrix_get_rotator

```python
@classmethod
def matrix_get_rotator(cls, m: Matrix) -> Rotator
```

X.matrix_get_rotator(m) -> Rotator
Get the rotator representation of this matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 

Returns:
    Rotator: rotator representation of this matrix

<a id="unreal.MathLibrary.matrix_get_origin"></a>

#### matrix_get_origin

```python
@classmethod
def matrix_get_origin(cls, matrix: Matrix) -> Vector
```

X.matrix_get_origin(matrix) -> Vector
Get the origin of the co-ordinate system
(Assumes Matrix represents a transform)

Args:
    matrix (Matrix): 

Returns:
    Vector: co-ordinate system origin

<a id="unreal.MathLibrary.matrix_get_maximum_axis_scale"></a>

#### matrix_get_maximum_axis_scale

```python
@classmethod
def matrix_get_maximum_axis_scale(cls, m: Matrix) -> float
```

X.matrix_get_maximum_axis_scale(m) -> float


Args:
    m (Matrix): 

Returns:
    float: the maximum magnitude of any row of the matrix. (Assumes Matrix represents a transform)

<a id="unreal.MathLibrary.matrix_get_matrix_without_scale"></a>

#### matrix_get_matrix_without_scale

```python
@classmethod
def matrix_get_matrix_without_scale(cls,
                                    m: Matrix,
                                    tolerance: float = 0.000000) -> Matrix
```

X.matrix_get_matrix_without_scale(m, tolerance=0.000000) -> Matrix
Returns matrix after RemoveScaling with error Tolerance
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    tolerance (float): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_get_inverse"></a>

#### matrix_get_inverse

```python
@classmethod
def matrix_get_inverse(cls, m: Matrix) -> Matrix
```

X.matrix_get_inverse(m) -> Matrix
Get the inverse of the Matrix. Handles nil matrices.

Args:
    m (Matrix): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_get_frustum_top_plane"></a>

#### matrix_get_frustum_top_plane

```python
@classmethod
def matrix_get_frustum_top_plane(cls, m: Matrix) -> Optional[Plane]
```

X.matrix_get_frustum_top_plane(m) -> Plane or None
Get the top plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Args:
    m (Matrix): 

Returns:
    Plane or None: 

    out_plane (Plane): the top plane of the Frustum of this matrix

<a id="unreal.MathLibrary.matrix_get_frustum_right_plane"></a>

#### matrix_get_frustum_right_plane

```python
@classmethod
def matrix_get_frustum_right_plane(cls, m: Matrix) -> Optional[Plane]
```

X.matrix_get_frustum_right_plane(m) -> Plane or None
Get the right plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Args:
    m (Matrix): 

Returns:
    Plane or None: 

    out_plane (Plane): the right plane of the Frustum of this matrix

<a id="unreal.MathLibrary.matrix_get_frustum_near_plane"></a>

#### matrix_get_frustum_near_plane

```python
@classmethod
def matrix_get_frustum_near_plane(cls, m: Matrix) -> Optional[Plane]
```

X.matrix_get_frustum_near_plane(m) -> Plane or None
Get the near plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Args:
    m (Matrix): 

Returns:
    Plane or None: 

    out_plane (Plane): the near plane of the Frustum of this matrix

<a id="unreal.MathLibrary.matrix_get_frustum_left_plane"></a>

#### matrix_get_frustum_left_plane

```python
@classmethod
def matrix_get_frustum_left_plane(cls, m: Matrix) -> Optional[Plane]
```

X.matrix_get_frustum_left_plane(m) -> Plane or None
Get the left plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Args:
    m (Matrix): 

Returns:
    Plane or None: 

    out_plane (Plane): the left plane of the Frustum of this matrix

<a id="unreal.MathLibrary.matrix_get_frustum_far_plane"></a>

#### matrix_get_frustum_far_plane

```python
@classmethod
def matrix_get_frustum_far_plane(cls, m: Matrix) -> Optional[Plane]
```

X.matrix_get_frustum_far_plane(m) -> Plane or None
Get the far plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Args:
    m (Matrix): 

Returns:
    Plane or None: 

    out_plane (Plane): the far plane of the Frustum of this matrix

<a id="unreal.MathLibrary.matrix_get_frustum_bottom_plane"></a>

#### matrix_get_frustum_bottom_plane

```python
@classmethod
def matrix_get_frustum_bottom_plane(cls, m: Matrix) -> Optional[Plane]
```

X.matrix_get_frustum_bottom_plane(m) -> Plane or None
Get the bottom plane of the Frustum of this matrix
(Assumes Matrix represents a View Projection Matrix)

Args:
    m (Matrix): 

Returns:
    Plane or None: 

    out_plane (Plane): the bottom plane of the Frustum of this matrix

<a id="unreal.MathLibrary.matrix_get_determinant"></a>

#### matrix_get_determinant

```python
@classmethod
def matrix_get_determinant(cls, m: Matrix) -> float
```

X.matrix_get_determinant(m) -> float


Args:
    m (Matrix): 

Returns:
    float: determinant of this matrix.

<a id="unreal.MathLibrary.matrix_get_column"></a>

#### matrix_get_column

```python
@classmethod
def matrix_get_column(cls, m: Matrix, column: MatrixColumns) -> Vector
```

X.matrix_get_column(m, column) -> Vector
get a column of this matrix

Args:
    m (Matrix): 
    column (MatrixColumns): 

Returns:
    Vector: vector of the column

<a id="unreal.MathLibrary.matrix_contains_na_n"></a>

#### matrix_contains_na_n

```python
@classmethod
def matrix_contains_na_n(cls, m: Matrix) -> bool
```

X.matrix_contains_na_n(m) -> bool
Returns true if any element of this matrix is NaN

Args:
    m (Matrix): 

Returns:
    bool:

<a id="unreal.MathLibrary.matrix_concatenate_translation"></a>

#### matrix_concatenate_translation

```python
@classmethod
def matrix_concatenate_translation(cls, m: Matrix,
                                   translation: Vector) -> Matrix
```

X.matrix_concatenate_translation(m, translation) -> Matrix
Returns a matrix with an additional translation concatenated.
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    translation (Vector): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.matrix_apply_scale"></a>

#### matrix_apply_scale

```python
@classmethod
def matrix_apply_scale(cls, m: Matrix, scale: float) -> Matrix
```

X.matrix_apply_scale(m, scale) -> Matrix
Apply Scale to this matrix
(Assumes Matrix represents a transform)

Args:
    m (Matrix): 
    scale (float): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.map_range_unclamped"></a>

#### map_range_unclamped

```python
@classmethod
def map_range_unclamped(cls, value: float, range_a: float, range_b: float,
                        out_range_a: float, out_range_b: float) -> float
```

X.map_range_unclamped(value, range_a, range_b, out_range_a, out_range_b) -> double
Returns Value mapped from one range into another.  (e.g. 20 normalized from the range 10->50 to 20->40 would result in 25)

Args:
    value (double): 
    range_a (double): 
    range_b (double): 
    out_range_a (double): 
    out_range_b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.map_range"></a>

#### map_range

```python
@classmethod
def map_range(cls, value: float, range_a: float, range_b: float,
              out_range_a: float, out_range_b: float) -> float
```

deprecated: 'map_range' was renamed to 'map_range_unclamped'.

<a id="unreal.MathLibrary.map_range_clamped"></a>

#### map_range_clamped

```python
@classmethod
def map_range_clamped(cls, value: float, range_a: float, range_b: float,
                      out_range_a: float, out_range_b: float) -> float
```

X.map_range_clamped(value, range_a, range_b, out_range_a, out_range_b) -> double
Returns Value mapped from one range into another where the Value is clamped to the Input Range.  (e.g. 0.5 normalized from the range 0->1 to 0->50 would result in 25)

Args:
    value (double): 
    range_a (double): 
    range_b (double): 
    out_range_a (double): 
    out_range_b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.make_rot_from_zy"></a>

#### make_rot_from_zy

```python
@classmethod
def make_rot_from_zy(cls, z: Vector, y: Vector) -> Rotator
```

X.make_rot_from_zy(z, y) -> Rotator
Builds a matrix with given Z and Y axes. Z will remain fixed, Y may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

Args:
    z (Vector): 
    y (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_zx"></a>

#### make_rot_from_zx

```python
@classmethod
def make_rot_from_zx(cls, z: Vector, x: Vector) -> Rotator
```

X.make_rot_from_zx(z, x) -> Rotator
Builds a matrix with given Z and X axes. Z will remain fixed, X may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

Args:
    z (Vector): 
    x (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_z"></a>

#### make_rot_from_z

```python
@classmethod
def make_rot_from_z(cls, z: Vector) -> Rotator
```

X.make_rot_from_z(z) -> Rotator
Builds a rotation matrix given only a ZAxis. X and Y are unspecified but will be orthonormal. ZAxis need not be normalized.

Args:
    z (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_yz"></a>

#### make_rot_from_yz

```python
@classmethod
def make_rot_from_yz(cls, y: Vector, z: Vector) -> Rotator
```

X.make_rot_from_yz(y, z) -> Rotator
Builds a matrix with given Y and Z axes. Y will remain fixed, Z may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

Args:
    y (Vector): 
    z (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_yx"></a>

#### make_rot_from_yx

```python
@classmethod
def make_rot_from_yx(cls, y: Vector, x: Vector) -> Rotator
```

X.make_rot_from_yx(y, x) -> Rotator
Builds a matrix with given Y and X axes. Y will remain fixed, X may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

Args:
    y (Vector): 
    x (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_y"></a>

#### make_rot_from_y

```python
@classmethod
def make_rot_from_y(cls, y: Vector) -> Rotator
```

X.make_rot_from_y(y) -> Rotator
Builds a rotation matrix given only a YAxis. X and Z are unspecified but will be orthonormal. YAxis need not be normalized.

Args:
    y (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_xz"></a>

#### make_rot_from_xz

```python
@classmethod
def make_rot_from_xz(cls, x: Vector, z: Vector) -> Rotator
```

X.make_rot_from_xz(x, z) -> Rotator
Builds a matrix with given X and Z axes. X will remain fixed, Z may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

Args:
    x (Vector): 
    z (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_xy"></a>

#### make_rot_from_xy

```python
@classmethod
def make_rot_from_xy(cls, x: Vector, y: Vector) -> Rotator
```

X.make_rot_from_xy(x, y) -> Rotator
Builds a matrix with given X and Y axes. X will remain fixed, Y may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

Args:
    x (Vector): 
    y (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rot_from_x"></a>

#### make_rot_from_x

```python
@classmethod
def make_rot_from_x(cls, x: Vector) -> Rotator
```

X.make_rot_from_x(x) -> Rotator
Builds a rotator given only a XAxis. Y and Z are unspecified but will be orthonormal. XAxis need not be normalized.

Args:
    x (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_rotation_from_axes"></a>

#### make_rotation_from_axes

```python
@classmethod
def make_rotation_from_axes(cls, forward: Vector, right: Vector,
                            up: Vector) -> Rotator
```

X.make_rotation_from_axes(forward, right, up) -> Rotator
Build a reference frame from three axes

Args:
    forward (Vector): 
    right (Vector): 
    up (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.make_relative_transform"></a>

#### make_relative_transform

```python
@classmethod
def make_relative_transform(cls, a: Transform,
                            relative_to: Transform) -> Transform
```

X.make_relative_transform(a, relative_to) -> Transform
Computes a relative transform of one transform compared to another.

Example: ChildOffset = MakeRelativeTransform(Child.GetActorTransform(), Parent.GetActorTransform())
This computes the relative transform of the Child from the Parent.

Args:
    a (Transform): The object's transform
    relative_to (Transform): The transform the result is relative to (in the same space as A)

Returns:
    Transform: The new relative transform

<a id="unreal.MathLibrary.convert_transform_to_relative"></a>

#### convert_transform_to_relative

```python
@classmethod
def convert_transform_to_relative(cls, a: Transform,
                                  relative_to: Transform) -> Transform
```

deprecated: 'convert_transform_to_relative' was renamed to 'make_relative_transform'.

<a id="unreal.MathLibrary.make_pulsating_value"></a>

#### make_pulsating_value

```python
@classmethod
def make_pulsating_value(cls,
                         current_time: float,
                         pulses_per_second: float = 1.000000,
                         phase: float = 0.000000) -> float
```

X.make_pulsating_value(current_time, pulses_per_second=1.000000, phase=0.000000) -> float
Simple function to create a pulsating scalar value

Args:
    current_time (float): Current absolute time
    pulses_per_second (float): How many full pulses per second?
    phase (float): Optional phase amount, between 0.0 and 1.0 (to synchronize pulses)

Returns:
    float: Pulsating value (0.0-1.0)

<a id="unreal.MathLibrary.make_plane_from_point_and_normal"></a>

#### make_plane_from_point_and_normal

```python
@classmethod
def make_plane_from_point_and_normal(cls, point: Vector,
                                     normal: Vector) -> Plane
```

X.make_plane_from_point_and_normal(point, normal) -> Plane
Creates a plane with a facing direction of Normal at the given Point

Args:
    point (Vector): A point on the plane
    normal (Vector): The Normal of the plane at Point

Returns:
    Plane: Plane instance

<a id="unreal.MathLibrary.make_box_with_origin"></a>

#### make_box_with_origin

```python
@classmethod
def make_box_with_origin(cls, origin: Vector, extent: Vector) -> Box
```

X.make_box_with_origin(origin, extent) -> Box
Utility function to build an box from an Origin and Extent

Args:
    origin (Vector): The location of the bounding box.
    extent (Vector): Half size of the bounding box.

Returns:
    Box: A new axis-aligned bounding box.

<a id="unreal.MathLibrary.loge"></a>

#### loge

```python
@classmethod
def loge(cls, a: float) -> float
```

X.loge(a) -> double
Returns natural log of A (if e^R == A, returns R)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.log"></a>

#### log

```python
@classmethod
def log(cls, a: float, base: float = 1.000000) -> float
```

X.log(a, base=1.000000) -> double
Returns log of A base B (if B^R == A, returns R)

Args:
    a (double): 
    base (double): 

Returns:
    double:

<a id="unreal.MathLibrary.line_plane_intersection_origin_normal"></a>

#### line_plane_intersection_origin_normal

```python
@classmethod
def line_plane_intersection_origin_normal(
        cls, line_start: Vector, line_end: Vector, plane_origin: Vector,
        plane_normal: Vector) -> Optional[Tuple[float, Vector]]
```

X.line_plane_intersection_origin_normal(line_start, line_end, plane_origin, plane_normal) -> (t=float, intersection=Vector) or None
Computes the intersection point between a line and a plane.

Args:
    line_start (Vector): 
    line_end (Vector): 
    plane_origin (Vector): 
    plane_normal (Vector): 

Returns:
    tuple or None: True if the intersection test was successful.

    t (float): The t of the intersection between the line and the plane

    intersection (Vector): The point of intersection between the line and the plane

<a id="unreal.MathLibrary.line_plane_intersection"></a>

#### line_plane_intersection

```python
@classmethod
def line_plane_intersection(cls, line_start: Vector, line_end: Vector,
                            a_plane: Plane) -> Optional[Tuple[float, Vector]]
```

X.line_plane_intersection(line_start, line_end, a_plane) -> (t=float, intersection=Vector) or None
Computes the intersection point between a line and a plane.

Args:
    line_start (Vector): 
    line_end (Vector): 
    a_plane (Plane): 

Returns:
    tuple or None: True if the intersection test was successful.

    t (float): The t of the intersection between the line and the plane

    intersection (Vector): The point of intersection between the line and the plane

<a id="unreal.MathLibrary.linear_color_lerp_using_hsv"></a>

#### linear_color_lerp_using_hsv

```python
@classmethod
def linear_color_lerp_using_hsv(cls, a: LinearColor, b: LinearColor,
                                alpha: float) -> LinearColor
```

X.linear_color_lerp_using_hsv(a, b, alpha) -> LinearColor
Linearly interpolates between two colors by the specified Alpha amount (100% of A when Alpha=0 and 100% of B when Alpha=1).  The interpolation is performed in HSV color space taking the shortest path to the new color's hue.  This can give better results than a normal lerp, but is much more expensive.  The incoming colors are in RGB space, and the output color will be RGB.  The alpha value will also be interpolated.

Args:
    a (LinearColor): The color and alpha to interpolate from as linear RGBA
    b (LinearColor): The color and alpha to interpolate to as linear RGBA
    alpha (float): Scalar interpolation amount (usually between 0.0 and 1.0 inclusive)

Returns:
    LinearColor: The interpolated color in linear RGB space along with the interpolated alpha value

<a id="unreal.MathLibrary.linear_color_lerp"></a>

#### linear_color_lerp

```python
@classmethod
def linear_color_lerp(cls, a: LinearColor, b: LinearColor,
                      alpha: float) -> LinearColor
```

X.linear_color_lerp(a, b, alpha) -> LinearColor
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    a (LinearColor): 
    b (LinearColor): 
    alpha (float): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.linear_color_to_rgbe"></a>

#### linear_color_to_rgbe

```python
@classmethod
def linear_color_to_rgbe(cls, linear_color: LinearColor) -> Color
```

X.linear_color_to_rgbe(linear_color) -> Color
Converts from linear to 8-bit RGBE as outlined in Gregory Ward's Real Pixels article, Graphics Gems II, page 80.

Args:
    linear_color (LinearColor): 

Returns:
    Color:

<a id="unreal.MathLibrary.linear_color_to_new_opacity"></a>

#### linear_color_to_new_opacity

```python
@classmethod
def linear_color_to_new_opacity(cls, color: LinearColor,
                                opacity: float) -> LinearColor
```

X.linear_color_to_new_opacity(color, opacity) -> LinearColor
Returns a copy of this color using the specified opacity/alpha.

Args:
    color (LinearColor): 
    opacity (float): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.linear_color_set_temperature"></a>

#### linear_color_set_temperature

```python
@classmethod
def linear_color_set_temperature(cls, out_color: LinearColor,
                                 temperature: float) -> LinearColor
```

X.linear_color_set_temperature(out_color, temperature) -> LinearColor
Converts temperature in Kelvins of a black body radiator to RGB chromaticity.

Args:
    out_color (LinearColor): 
    temperature (float): 

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_set_rgba"></a>

#### linear_color_set_rgba

```python
@classmethod
def linear_color_set_rgba(cls,
                          out_color: LinearColor,
                          r: float,
                          g: float,
                          b: float,
                          a: float = 1.000000) -> LinearColor
```

X.linear_color_set_rgba(out_color, r, g, b, a=1.000000) -> LinearColor
Assign individual linear RGBA components.

Args:
    out_color (LinearColor): 
    r (float): 
    g (float): 
    b (float): 
    a (float): 

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_set_random_hue"></a>

#### linear_color_set_random_hue

```python
@classmethod
def linear_color_set_random_hue(cls, out_color: LinearColor) -> LinearColor
```

X.linear_color_set_random_hue(out_color) -> LinearColor
Sets to a random color. Choses a quite nice color based on a random hue.

Args:
    out_color (LinearColor): 

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_set_from_srgb"></a>

#### linear_color_set_from_srgb

```python
@classmethod
def linear_color_set_from_srgb(cls, out_color: LinearColor,
                               srgb: Color) -> LinearColor
```

X.linear_color_set_from_srgb(out_color, srgb) -> LinearColor
Assigns an FColor coming from an observed sRGB output, into a linear color.

Args:
    out_color (LinearColor): 
    srgb (Color): The sRGB color that needs to be converted into linear space.

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_set_from_pow22"></a>

#### linear_color_set_from_pow22

```python
@classmethod
def linear_color_set_from_pow22(cls, out_color: LinearColor,
                                color: Color) -> LinearColor
```

X.linear_color_set_from_pow22(out_color, color) -> LinearColor
Assigns an FColor coming from an observed Pow(1/2.2) output, into a linear color.

Args:
    out_color (LinearColor): 
    color (Color): The Pow(1/2.2) color that needs to be converted into linear space.

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_set_from_hsv"></a>

#### linear_color_set_from_hsv

```python
@classmethod
def linear_color_set_from_hsv(cls,
                              out_color: LinearColor,
                              h: float,
                              s: float,
                              v: float,
                              a: float = 1.000000) -> LinearColor
```

X.linear_color_set_from_hsv(out_color, h, s, v, a=1.000000) -> LinearColor
Assigns an HSV color to a linear space RGB color

Args:
    out_color (LinearColor): 
    h (float): 
    s (float): 
    v (float): 
    a (float): 

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_set"></a>

#### linear_color_set

```python
@classmethod
def linear_color_set(cls, out_color: LinearColor,
                     color: LinearColor) -> LinearColor
```

X.linear_color_set(out_color, color) -> LinearColor
Assign contents of InColor

Args:
    out_color (LinearColor): 
    color (LinearColor): 

Returns:
    LinearColor: 

    out_color (LinearColor):

<a id="unreal.MathLibrary.linear_color_quantize_round"></a>

#### linear_color_quantize_round

```python
@classmethod
def linear_color_quantize_round(cls, color: LinearColor) -> Color
```

X.linear_color_quantize_round(color) -> Color
Quantizes the linear color with rounding and returns the result as an 8-bit color.  This bypasses the SRGB conversion.

Args:
    color (LinearColor): 

Returns:
    Color:

<a id="unreal.MathLibrary.linear_color_quantize"></a>

#### linear_color_quantize

```python
@classmethod
def linear_color_quantize(cls, color: LinearColor) -> Color
```

X.linear_color_quantize(color) -> Color
Quantizes the linear color and returns the result as an 8-bit color.  This bypasses the SRGB conversion.
deprecated: Use LinearColor_QuantizeRound instead for correct color conversion.

Args:
    color (LinearColor): 

Returns:
    Color:

<a id="unreal.MathLibrary.linear_color_is_near_equal"></a>

#### linear_color_is_near_equal

```python
@classmethod
def linear_color_is_near_equal(cls,
                               a: LinearColor,
                               b: LinearColor,
                               tolerance: float = 0.000100) -> bool
```

X.linear_color_is_near_equal(a, b, tolerance=0.000100) -> bool
Returns true if linear color A is equal to linear color B (A == B) within a specified error tolerance

Args:
    a (LinearColor): 
    b (LinearColor): 
    tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.linear_color_get_min"></a>

#### linear_color_get_min

```python
@classmethod
def linear_color_get_min(cls, color: LinearColor) -> float
```

X.linear_color_get_min(color) -> float
Returns the minimum color channel value in this color structure

Args:
    color (LinearColor): 

Returns:
    float: The minimum color channel value

<a id="unreal.MathLibrary.linear_color_get_max"></a>

#### linear_color_get_max

```python
@classmethod
def linear_color_get_max(cls, color: LinearColor) -> float
```

X.linear_color_get_max(color) -> float
Returns the maximum color channel value in this color structure

Args:
    color (LinearColor): 

Returns:
    float: The maximum color channel value

<a id="unreal.MathLibrary.linear_color_get_luminance"></a>

#### linear_color_get_luminance

```python
@classmethod
def linear_color_get_luminance(cls, color: LinearColor) -> float
```

X.linear_color_get_luminance(color) -> float
Returns the perceived brightness of a color on a display taking into account the impact on the human eye per color channel: green > red > blue.

Args:
    color (LinearColor): 

Returns:
    float:

<a id="unreal.MathLibrary.linear_color_distance"></a>

#### linear_color_distance

```python
@classmethod
def linear_color_distance(cls, c1: LinearColor, c2: LinearColor) -> float
```

X.linear_color_distance(c1, c2) -> float
Euclidean distance between two color points.

Args:
    c1 (LinearColor): 
    c2 (LinearColor): 

Returns:
    float:

<a id="unreal.MathLibrary.linear_color_desaturated"></a>

#### linear_color_desaturated

```python
@classmethod
def linear_color_desaturated(cls, color: LinearColor,
                             desaturation: float) -> LinearColor
```

X.linear_color_desaturated(color, desaturation) -> LinearColor
Returns a desaturated color, with 0 meaning no desaturation and 1 == full desaturation

Args:
    color (LinearColor): 
    desaturation (float): 

Returns:
    LinearColor: Desaturated color

<a id="unreal.MathLibrary.less_less_vector_rotator"></a>

#### less_less_vector_rotator

```python
@classmethod
def less_less_vector_rotator(cls, a: Vector, b: Rotator) -> Vector
```

X.less_less_vector_rotator(a, b) -> Vector
Returns result of vector A rotated by the inverse of Rotator B

Args:
    a (Vector): 
    b (Rotator): 

Returns:
    Vector:

<a id="unreal.MathLibrary.less_equal_timespan_timespan"></a>

#### less_equal_timespan_timespan

```python
@classmethod
def less_equal_timespan_timespan(cls, a: Timespan, b: Timespan) -> bool
```

X.less_equal_timespan_timespan(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_equal_int_int"></a>

#### less_equal_int_int

```python
@classmethod
def less_equal_int_int(cls, a: int, b: int) -> bool
```

X.less_equal_int_int(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)

Args:
    a (int32): 
    b (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_equal_int64_int64"></a>

#### less_equal_int64_int64

```python
@classmethod
def less_equal_int64_int64(cls, a: int, b: int) -> bool
```

X.less_equal_int64_int64(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)

Args:
    a (int64): 
    b (int64): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_equal_double_double"></a>

#### less_equal_double_double

```python
@classmethod
def less_equal_double_double(cls, a: float, b: float) -> bool
```

X.less_equal_double_double(a, b) -> bool
Returns true if A is Less than or equal to B (A <= B)

Args:
    a (double): 
    b (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_equal_float_float"></a>

#### less_equal_float_float

```python
@classmethod
def less_equal_float_float(cls, a: float, b: float) -> bool
```

deprecated: 'less_equal_float_float' was renamed to 'less_equal_double_double'.

<a id="unreal.MathLibrary.less_equal_date_time_date_time"></a>

#### less_equal_date_time_date_time

```python
@classmethod
def less_equal_date_time_date_time(cls, a: DateTime, b: DateTime) -> bool
```

X.less_equal_date_time_date_time(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_equal_byte_byte"></a>

#### less_equal_byte_byte

```python
@classmethod
def less_equal_byte_byte(cls, a: int, b: int) -> bool
```

X.less_equal_byte_byte(a, b) -> bool
Returns true if A is less than or equal to B (A <= B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_timespan_timespan"></a>

#### less_timespan_timespan

```python
@classmethod
def less_timespan_timespan(cls, a: Timespan, b: Timespan) -> bool
```

X.less_timespan_timespan(a, b) -> bool
Returns true if A is less than B (A < B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_int_int"></a>

#### less_int_int

```python
@classmethod
def less_int_int(cls, a: int, b: int) -> bool
```

X.less_int_int(a, b) -> bool
Returns true if A is less than B (A < B)

Args:
    a (int32): 
    b (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_int64_int64"></a>

#### less_int64_int64

```python
@classmethod
def less_int64_int64(cls, a: int, b: int) -> bool
```

X.less_int64_int64(a, b) -> bool
Returns true if A is less than B (A < B)

Args:
    a (int64): 
    b (int64): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_double_double"></a>

#### less_double_double

```python
@classmethod
def less_double_double(cls, a: float, b: float) -> bool
```

X.less_double_double(a, b) -> bool
Returns true if A is Less than B (A < B)

Args:
    a (double): 
    b (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_float_float"></a>

#### less_float_float

```python
@classmethod
def less_float_float(cls, a: float, b: float) -> bool
```

deprecated: 'less_float_float' was renamed to 'less_double_double'.

<a id="unreal.MathLibrary.less_date_time_date_time"></a>

#### less_date_time_date_time

```python
@classmethod
def less_date_time_date_time(cls, a: DateTime, b: DateTime) -> bool
```

X.less_date_time_date_time(a, b) -> bool
Returns true if A is less than B (A < B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.less_byte_byte"></a>

#### less_byte_byte

```python
@classmethod
def less_byte_byte(cls, a: int, b: int) -> bool
```

X.less_byte_byte(a, b) -> bool
Returns true if A is less than B (A < B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.MathLibrary.lerp"></a>

#### lerp

```python
@classmethod
def lerp(cls, a: float, b: float, alpha: float) -> float
```

X.lerp(a, b, alpha) -> double
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    a (double): 
    b (double): 
    alpha (double): 

Returns:
    double:

<a id="unreal.MathLibrary.is_zero2d"></a>

#### is_zero2d

```python
@classmethod
def is_zero2d(cls, a: Vector2D) -> bool
```

X.is_zero2d(a) -> bool
Checks whether all components of the vector are exactly zero.

Args:
    a (Vector2D): 

Returns:
    bool: true if vector is exactly zero, otherwise false.

<a id="unreal.MathLibrary.is_point_in_box_with_transform_box"></a>

#### is_point_in_box_with_transform_box

```python
@classmethod
def is_point_in_box_with_transform_box(cls, point: Vector,
                                       box_world_transform: Transform,
                                       box_extent: Box) -> bool
```

X.is_point_in_box_with_transform_box(point, box_world_transform, box_extent) -> bool
Determines whether a given point is in a box with a given transform. Includes points on the box.

Args:
    point (Vector): Point to test
    box_world_transform (Transform): Component-to-World transform of the box.
    box_extent (Box): 

Returns:
    bool: Whether the point is in the box.

<a id="unreal.MathLibrary.is_point_in_box_with_transform"></a>

#### is_point_in_box_with_transform

```python
@classmethod
def is_point_in_box_with_transform(cls, point: Vector,
                                   box_world_transform: Transform,
                                   box_extent: Vector) -> bool
```

X.is_point_in_box_with_transform(point, box_world_transform, box_extent) -> bool
Determines whether a given point is in a box with a given transform. Includes points on the box.

Args:
    point (Vector): Point to test
    box_world_transform (Transform): Component-to-World transform of the box.
    box_extent (Vector): Extents of the box (distance in each axis from origin), in component space.

Returns:
    bool: Whether the point is in the box.

<a id="unreal.MathLibrary.is_point_in_box_box"></a>

#### is_point_in_box_box

```python
@classmethod
def is_point_in_box_box(cls, point: Vector, box: Box) -> bool
```

X.is_point_in_box_box(point, box) -> bool
Determines whether the given point is in a box. Includes points on the box.

Args:
    point (Vector): Point to test
    box (Box): Box to test against

Returns:
    bool: Whether the point is in the box.

<a id="unreal.MathLibrary.is_point_in_box"></a>

#### is_point_in_box

```python
@classmethod
def is_point_in_box(cls, point: Vector, box_origin: Vector,
                    box_extent: Vector) -> bool
```

X.is_point_in_box(point, box_origin, box_extent) -> bool
Determines whether the given point is in a box. Includes points on the box.

Args:
    point (Vector): Point to test
    box_origin (Vector): Origin of the box
    box_extent (Vector): Extents of the box (distance in each axis from origin)

Returns:
    bool: Whether the point is in the box.

<a id="unreal.MathLibrary.is_nearly_zero2d"></a>

#### is_nearly_zero2d

```python
@classmethod
def is_nearly_zero2d(cls, a: Vector2D, tolerance: float = 0.000100) -> bool
```

X.is_nearly_zero2d(a, tolerance=0.000100) -> bool
Checks whether vector is near to zero within a specified tolerance.

Args:
    a (Vector2D): 
    tolerance (float): Error tolerance.

Returns:
    bool: true if vector is in tolerance to zero, otherwise false.

<a id="unreal.MathLibrary.is_morning"></a>

#### is_morning

```python
@classmethod
def is_morning(cls, a: DateTime) -> bool
```

X.is_morning(a) -> bool
Returns whether A's time is in the morning

Args:
    a (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.is_leap_year"></a>

#### is_leap_year

```python
@classmethod
def is_leap_year(cls, year: int) -> bool
```

X.is_leap_year(year) -> bool
Returns whether given year is a leap year

Args:
    year (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.is_afternoon"></a>

#### is_afternoon

```python
@classmethod
def is_afternoon(cls, a: DateTime) -> bool
```

X.is_afternoon(a) -> bool
Returns whether A's time is in the afternoon

Args:
    a (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.invert_transform"></a>

#### invert_transform

```python
@classmethod
def invert_transform(cls, t: Transform) -> Transform
```

X.invert_transform(t) -> Transform
Returns the inverse of the given transform T.

Example: Given a LocalToWorld transform, WorldToLocal will be returned.

Args:
    t (Transform): The transform you wish to invert

Returns:
    Transform: The inverse of T.

<a id="unreal.MathLibrary.inverse_transform_rotation"></a>

#### inverse_transform_rotation

```python
@classmethod
def inverse_transform_rotation(cls, t: Transform,
                               rotation: Rotator) -> Rotator
```

X.inverse_transform_rotation(t, rotation) -> Rotator
Transform a rotator by the inverse of the supplied transform.
For example, if T was an object's transform, this would transform a rotation from world space to local space.

Args:
    t (Transform): 
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.inverse_transform_location"></a>

#### inverse_transform_location

```python
@classmethod
def inverse_transform_location(cls, t: Transform, location: Vector) -> Vector
```

X.inverse_transform_location(t, location) -> Vector
Transform a position by the inverse of the supplied transform.
For example, if T was an object's transform, this would transform a position from world space to local space.

Args:
    t (Transform): 
    location (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.inverse_transform_position"></a>

#### inverse_transform_position

```python
@classmethod
def inverse_transform_position(cls, t: Transform, location: Vector) -> Vector
```

deprecated: 'inverse_transform_position' was renamed to 'inverse_transform_location'.

<a id="unreal.MathLibrary.inverse_transform_direction"></a>

#### inverse_transform_direction

```python
@classmethod
def inverse_transform_direction(cls, t: Transform,
                                direction: Vector) -> Vector
```

X.inverse_transform_direction(t, direction) -> Vector
Transform a direction vector by the inverse of the supplied transform - will not change its length.
For example, if T was an object's transform, this would transform a direction from world space to local space.

Args:
    t (Transform): 
    direction (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.in_range_int_int"></a>

#### in_range_int_int

```python
@classmethod
def in_range_int_int(cls,
                     value: int,
                     min: int = 0,
                     max: int = 10,
                     inclusive_min: bool = True,
                     inclusive_max: bool = True) -> bool
```

X.in_range_int_int(value, min=0, max=10, inclusive_min=True, inclusive_max=True) -> bool
Returns true if value is between Min and Max (V >= Min && V <= Max)
If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Args:
    value (int32): 
    min (int32): 
    max (int32): 
    inclusive_min (bool): 
    inclusive_max (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.in_range_int64_int64"></a>

#### in_range_int64_int64

```python
@classmethod
def in_range_int64_int64(cls,
                         value: int,
                         min: int = 0,
                         max: int = 10,
                         inclusive_min: bool = True,
                         inclusive_max: bool = True) -> bool
```

X.in_range_int64_int64(value, min=0, max=10, inclusive_min=True, inclusive_max=True) -> bool
Returns true if value is between Min and Max (V >= Min && V <= Max)
If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Args:
    value (int64): 
    min (int64): 
    max (int64): 
    inclusive_min (bool): 
    inclusive_max (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.in_range_float_float"></a>

#### in_range_float_float

```python
@classmethod
def in_range_float_float(cls,
                         value: float,
                         min: float = 0.000000,
                         max: float = 1.000000,
                         inclusive_min: bool = True,
                         inclusive_max: bool = True) -> bool
```

X.in_range_float_float(value, min=0.000000, max=1.000000, inclusive_min=True, inclusive_max=True) -> bool
Returns true if value is between Min and Max (V >= Min && V <= Max)
If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

Args:
    value (double): 
    min (double): 
    max (double): 
    inclusive_min (bool): 
    inclusive_max (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.hypotenuse"></a>

#### hypotenuse

```python
@classmethod
def hypotenuse(cls, width: float, height: float) -> float
```

X.hypotenuse(width, height) -> double
Returns the hypotenuse of a right-angled triangle given the width and height.

Args:
    width (double): 
    height (double): 

Returns:
    double:

<a id="unreal.MathLibrary.hsv_to_rgb_linear"></a>

#### hsv_to_rgb_linear

```python
@classmethod
def hsv_to_rgb_linear(cls, hsv: LinearColor) -> LinearColor
```

X.hsv_to_rgb_linear(hsv) -> LinearColor
Converts a HSV linear color (where H is in R, S is in G, and V is in B) to linear RGB

Args:
    hsv (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.hsv_to_rgb_vector"></a>

#### hsv_to_rgb_vector

```python
@classmethod
def hsv_to_rgb_vector(cls, hsv: LinearColor) -> LinearColor
```

X.hsv_to_rgb_vector(hsv) -> LinearColor
Converts a HSV linear color (where H is in R (0..360), S is in G (0..1), and V is in B (0..1)) to RGB

Args:
    hsv (LinearColor): 

Returns:
    LinearColor: 

    rgb (LinearColor):

<a id="unreal.MathLibrary.hsv_to_rgb"></a>

#### hsv_to_rgb

```python
@classmethod
def hsv_to_rgb(cls,
               h: float,
               s: float,
               v: float,
               a: float = 1.000000) -> LinearColor
```

X.hsv_to_rgb(h, s, v, a=1.000000) -> LinearColor
Make a color from individual color components (HSV space; Hue is [0..360) while Saturation and Value are 0..1)

Args:
    h (float): 
    s (float): 
    v (float): 
    a (float): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.grid_snap_float"></a>

#### grid_snap_float

```python
@classmethod
def grid_snap_float(cls, location: float, grid_size: float) -> float
```

X.grid_snap_float(location, grid_size) -> double
Snaps a value to the nearest grid multiple. E.g.,
            Location = 5.1, GridSize = 10.0 : return value = 10.0
If GridSize is 0 Location is returned
if GridSize is very small precision issues may occur.

Args:
    location (double): 
    grid_size (double): 

Returns:
    double:

<a id="unreal.MathLibrary.greater_greater_vector_rotator"></a>

#### greater_greater_vector_rotator

```python
@classmethod
def greater_greater_vector_rotator(cls, a: Vector, b: Rotator) -> Vector
```

X.greater_greater_vector_rotator(a, b) -> Vector
Returns result of vector A rotated by Rotator B

Args:
    a (Vector): 
    b (Rotator): 

Returns:
    Vector:

<a id="unreal.MathLibrary.greater_equal_timespan_timespan"></a>

#### greater_equal_timespan_timespan

```python
@classmethod
def greater_equal_timespan_timespan(cls, a: Timespan, b: Timespan) -> bool
```

X.greater_equal_timespan_timespan(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_equal_int_int"></a>

#### greater_equal_int_int

```python
@classmethod
def greater_equal_int_int(cls, a: int, b: int) -> bool
```

X.greater_equal_int_int(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (int32): 
    b (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_equal_int64_int64"></a>

#### greater_equal_int64_int64

```python
@classmethod
def greater_equal_int64_int64(cls, a: int, b: int) -> bool
```

X.greater_equal_int64_int64(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (int64): 
    b (int64): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_equal_double_double"></a>

#### greater_equal_double_double

```python
@classmethod
def greater_equal_double_double(cls, a: float, b: float) -> bool
```

X.greater_equal_double_double(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (double): 
    b (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_equal_float_float"></a>

#### greater_equal_float_float

```python
@classmethod
def greater_equal_float_float(cls, a: float, b: float) -> bool
```

deprecated: 'greater_equal_float_float' was renamed to 'greater_equal_double_double'.

<a id="unreal.MathLibrary.greater_equal_date_time_date_time"></a>

#### greater_equal_date_time_date_time

```python
@classmethod
def greater_equal_date_time_date_time(cls, a: DateTime, b: DateTime) -> bool
```

X.greater_equal_date_time_date_time(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_equal_byte_byte"></a>

#### greater_equal_byte_byte

```python
@classmethod
def greater_equal_byte_byte(cls, a: int, b: int) -> bool
```

X.greater_equal_byte_byte(a, b) -> bool
Returns true if A is greater than or equal to B (A >= B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_timespan_timespan"></a>

#### greater_timespan_timespan

```python
@classmethod
def greater_timespan_timespan(cls, a: Timespan, b: Timespan) -> bool
```

X.greater_timespan_timespan(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_int_int"></a>

#### greater_int_int

```python
@classmethod
def greater_int_int(cls, a: int, b: int) -> bool
```

X.greater_int_int(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (int32): 
    b (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_int64_int64"></a>

#### greater_int64_int64

```python
@classmethod
def greater_int64_int64(cls, a: int, b: int) -> bool
```

X.greater_int64_int64(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (int64): 
    b (int64): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_double_double"></a>

#### greater_double_double

```python
@classmethod
def greater_double_double(cls, a: float, b: float) -> bool
```

X.greater_double_double(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (double): 
    b (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_float_float"></a>

#### greater_float_float

```python
@classmethod
def greater_float_float(cls, a: float, b: float) -> bool
```

deprecated: 'greater_float_float' was renamed to 'greater_double_double'.

<a id="unreal.MathLibrary.greater_date_time_date_time"></a>

#### greater_date_time_date_time

```python
@classmethod
def greater_date_time_date_time(cls, a: DateTime, b: DateTime) -> bool
```

X.greater_date_time_date_time(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.greater_byte_byte"></a>

#### greater_byte_byte

```python
@classmethod
def greater_byte_byte(cls, a: int, b: int) -> bool
```

X.greater_byte_byte(a, b) -> bool
Returns true if A is greater than B (A > B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.MathLibrary.get_year"></a>

#### get_year

```python
@classmethod
def get_year(cls, a: DateTime) -> int
```

X.get_year(a) -> int32
Returns the year component of A

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_vector_array_average"></a>

#### get_vector_array_average

```python
@classmethod
def get_vector_array_average(cls, vectors: Array[Vector]) -> Vector
```

X.get_vector_array_average(vectors) -> Vector
Find the average of an array of vectors

Args:
    vectors (Array[Vector]): 

Returns:
    Vector:

<a id="unreal.MathLibrary.get_up_vector"></a>

#### get_up_vector

```python
@classmethod
def get_up_vector(cls, rot: Rotator) -> Vector
```

X.get_up_vector(rot) -> Vector
Rotate the world up vector by the given rotation

Args:
    rot (Rotator): 

Returns:
    Vector:

<a id="unreal.MathLibrary.get_total_seconds"></a>

#### get_total_seconds

```python
@classmethod
def get_total_seconds(cls, a: Timespan) -> float
```

X.get_total_seconds(a) -> float
Returns the total number of seconds in A

Args:
    a (Timespan): 

Returns:
    float:

<a id="unreal.MathLibrary.get_total_minutes"></a>

#### get_total_minutes

```python
@classmethod
def get_total_minutes(cls, a: Timespan) -> float
```

X.get_total_minutes(a) -> float
Returns the total number of minutes in A

Args:
    a (Timespan): 

Returns:
    float:

<a id="unreal.MathLibrary.get_total_milliseconds"></a>

#### get_total_milliseconds

```python
@classmethod
def get_total_milliseconds(cls, a: Timespan) -> float
```

X.get_total_milliseconds(a) -> float
Returns the total number of milliseconds in A

Args:
    a (Timespan): 

Returns:
    float:

<a id="unreal.MathLibrary.get_total_hours"></a>

#### get_total_hours

```python
@classmethod
def get_total_hours(cls, a: Timespan) -> float
```

X.get_total_hours(a) -> float
Returns the total number of hours in A

Args:
    a (Timespan): 

Returns:
    float:

<a id="unreal.MathLibrary.get_total_days"></a>

#### get_total_days

```python
@classmethod
def get_total_days(cls, a: Timespan) -> float
```

X.get_total_days(a) -> float
Returns the total number of days in A

Args:
    a (Timespan): 

Returns:
    float:

<a id="unreal.MathLibrary.get_time_of_day"></a>

#### get_time_of_day

```python
@classmethod
def get_time_of_day(cls, a: DateTime) -> Timespan
```

X.get_time_of_day(a) -> Timespan
Returns the time elapsed since midnight of A

Args:
    a (DateTime): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.get_tau"></a>

#### get_tau

```python
@classmethod
def get_tau(cls) -> float
```

X.get_tau() -> double
Returns the value of TAU (= 2 * PI)

Returns:
    double:

<a id="unreal.MathLibrary.get_slope_degree_angles"></a>

#### get_slope_degree_angles

```python
@classmethod
def get_slope_degree_angles(cls, my_right_y_axis: Vector, floor_normal: Vector,
                            up_vector: Vector) -> Tuple[float, float]
```

X.get_slope_degree_angles(my_right_y_axis, floor_normal, up_vector) -> (out_slope_pitch_degree_angle=float, out_slope_roll_degree_angle=float)
Returns Slope Pitch and Roll angles in degrees based on the following information:
outparam: OutSlopePitchDegreeAngle    Slope Pitch angle (degrees)
outparam: OutSlopeRollDegreeAngle             Slope Roll angle (degrees)

Args:
    my_right_y_axis (Vector): Right (Y) direction unit vector of Actor standing on Slope.
    floor_normal (Vector): Floor Normal (unit) vector.
    up_vector (Vector): UpVector of reference frame.

Returns:
    tuple: 

    out_slope_pitch_degree_angle (float): 

    out_slope_roll_degree_angle (float):

<a id="unreal.MathLibrary.get_seconds"></a>

#### get_seconds

```python
@classmethod
def get_seconds(cls, a: Timespan) -> int
```

X.get_seconds(a) -> int32
Returns the seconds component of A

Args:
    a (Timespan): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_second"></a>

#### get_second

```python
@classmethod
def get_second(cls, a: DateTime) -> int
```

X.get_second(a) -> int32
Returns the second component of A

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_runtime_float_curve_value"></a>

#### get_runtime_float_curve_value

```python
@classmethod
def get_runtime_float_curve_value(cls,
                                  curve: RuntimeFloatCurve,
                                  time: float,
                                  default_value: float = 0.000000) -> float
```

X.get_runtime_float_curve_value(curve, time, default_value=0.000000) -> float
Evaluate this runtime float curve at the specified time
see: FRichCurve::Eval

Args:
    curve (RuntimeFloatCurve): The runtime float curve to evaluate
    time (float): The time at which to evaluate the curve
    default_value (float): The default value which should be used if the curve cannot be evaluated at the given time.

Returns:
    float: The curve's value at the given time.

<a id="unreal.MathLibrary.get_rotated2d"></a>

#### get_rotated2d

```python
@classmethod
def get_rotated2d(cls, a: Vector2D, angle_deg: float) -> Vector2D
```

X.get_rotated2d(a, angle_deg) -> Vector2D
Rotates around axis (0,0,1)

Args:
    a (Vector2D): 
    angle_deg (float): Angle to rotate (in degrees)

Returns:
    Vector2D: Rotated Vector

<a id="unreal.MathLibrary.get_right_vector"></a>

#### get_right_vector

```python
@classmethod
def get_right_vector(cls, rot: Rotator) -> Vector
```

X.get_right_vector(rot) -> Vector
Rotate the world right vector by the given rotation

Args:
    rot (Rotator): 

Returns:
    Vector:

<a id="unreal.MathLibrary.get_reflection_vector"></a>

#### get_reflection_vector

```python
@classmethod
def get_reflection_vector(cls, direction: Vector,
                          surface_normal: Vector) -> Vector
```

X.get_reflection_vector(direction, surface_normal) -> Vector
Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
Produces a result like shining a laser at a mirror!

Args:
    direction (Vector): Direction vector the ray is coming from.
    surface_normal (Vector): A normal of the surface the ray should be reflected on.

Returns:
    Vector: Reflected vector.

<a id="unreal.MathLibrary.get_point_distance_to_segment"></a>

#### get_point_distance_to_segment

```python
@classmethod
def get_point_distance_to_segment(cls, point: Vector, segment_start: Vector,
                                  segment_end: Vector) -> float
```

X.get_point_distance_to_segment(point, segment_start, segment_end) -> float
Find the distance from a point to the closest point on a segment.

Args:
    point (Vector): Point for which we find the distance to the closest point on the segment.
    segment_start (Vector): Start of the segment.
    segment_end (Vector): End of the segment.

Returns:
    float: The distance from the given point to the closest point on the segment.

<a id="unreal.MathLibrary.get_point_distance_to_line"></a>

#### get_point_distance_to_line

```python
@classmethod
def get_point_distance_to_line(cls, point: Vector, line_origin: Vector,
                               line_direction: Vector) -> float
```

X.get_point_distance_to_line(point, line_origin, line_direction) -> float
Find the distance from a point to the closest point on an infinite line.

Args:
    point (Vector): Point for which we find the distance to the closest point on the line.
    line_origin (Vector): Point of reference on the line.
    line_direction (Vector): Direction of the line. Not required to be normalized.

Returns:
    float: The distance from the given point to the closest point on the line.

<a id="unreal.MathLibrary.get_pi"></a>

#### get_pi

```python
@classmethod
def get_pi(cls) -> float
```

X.get_pi() -> double
Returns the value of PI

Returns:
    double:

<a id="unreal.MathLibrary.get_month"></a>

#### get_month

```python
@classmethod
def get_month(cls, a: DateTime) -> int
```

X.get_month(a) -> int32
Returns the month component of A

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_minutes"></a>

#### get_minutes

```python
@classmethod
def get_minutes(cls, a: Timespan) -> int
```

X.get_minutes(a) -> int32
Returns the minutes component of A

Args:
    a (Timespan): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_minute"></a>

#### get_minute

```python
@classmethod
def get_minute(cls, a: DateTime) -> int
```

X.get_minute(a) -> int32
Returns the minute component of A

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_min_element"></a>

#### get_min_element

```python
@classmethod
def get_min_element(cls, a: Vector) -> float
```

X.get_min_element(a) -> double
Find the minimum element (X, Y or Z) of a vector

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.get_min2d"></a>

#### get_min2d

```python
@classmethod
def get_min2d(cls, a: Vector2D) -> float
```

X.get_min2d(a) -> double
Get the minimum value of the vector's components.

Args:
    a (Vector2D): 

Returns:
    double: The minimum value of the vector's components.

<a id="unreal.MathLibrary.get_milliseconds"></a>

#### get_milliseconds

```python
@classmethod
def get_milliseconds(cls, a: Timespan) -> int
```

X.get_milliseconds(a) -> int32
Returns the milliseconds component of A

Args:
    a (Timespan): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_millisecond"></a>

#### get_millisecond

```python
@classmethod
def get_millisecond(cls, a: DateTime) -> int
```

X.get_millisecond(a) -> int32
Returns the millisecond component of A

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_max_element"></a>

#### get_max_element

```python
@classmethod
def get_max_element(cls, a: Vector) -> float
```

X.get_max_element(a) -> double
Find the maximum element (X, Y or Z) of a vector

Args:
    a (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.get_max2d"></a>

#### get_max2d

```python
@classmethod
def get_max2d(cls, a: Vector2D) -> float
```

X.get_max2d(a) -> double
Get the maximum value of the vector's components.

Args:
    a (Vector2D): 

Returns:
    double: The maximum value of the vector's components.

<a id="unreal.MathLibrary.get_hours"></a>

#### get_hours

```python
@classmethod
def get_hours(cls, a: Timespan) -> int
```

X.get_hours(a) -> int32
Returns the hours component of A

Args:
    a (Timespan): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_hour12"></a>

#### get_hour12

```python
@classmethod
def get_hour12(cls, a: DateTime) -> int
```

X.get_hour12(a) -> int32
Returns the hour component of A (12h format)

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_hour"></a>

#### get_hour

```python
@classmethod
def get_hour(cls, a: DateTime) -> int
```

X.get_hour(a) -> int32
Returns the hour component of A (24h format)

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_forward_vector"></a>

#### get_forward_vector

```python
@classmethod
def get_forward_vector(cls, rot: Rotator) -> Vector
```

X.get_forward_vector(rot) -> Vector
Rotate the world forward vector by the given rotation

Args:
    rot (Rotator): 

Returns:
    Vector:

<a id="unreal.MathLibrary.get_duration"></a>

#### get_duration

```python
@classmethod
def get_duration(cls, a: Timespan) -> Timespan
```

X.get_duration(a) -> Timespan
Returns the absolute value of A

Args:
    a (Timespan): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.get_direction_unit_vector"></a>

#### get_direction_unit_vector

```python
@classmethod
def get_direction_unit_vector(cls, from_: Vector, to: Vector) -> Vector
```

X.get_direction_unit_vector(from_, to) -> Vector
Find the unit direction vector from one position to another or (0,0,0) if positions are the same.

Args:
    from_ (Vector): 
    to (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.get_direction_vector"></a>

#### get_direction_vector

```python
@classmethod
def get_direction_vector(cls, from_: Vector, to: Vector) -> Vector
```

deprecated: 'get_direction_vector' was renamed to 'get_direction_unit_vector'.

<a id="unreal.MathLibrary.get_days"></a>

#### get_days

```python
@classmethod
def get_days(cls, a: Timespan) -> int
```

X.get_days(a) -> int32
Returns the days component of A

Args:
    a (Timespan): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_day_of_year"></a>

#### get_day_of_year

```python
@classmethod
def get_day_of_year(cls, a: DateTime) -> int
```

X.get_day_of_year(a) -> int32
Returns the day of year of A

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_day"></a>

#### get_day

```python
@classmethod
def get_day(cls, a: DateTime) -> int
```

X.get_day(a) -> int32
Returns the day component of A (1 to 31)

Args:
    a (DateTime): 

Returns:
    int32:

<a id="unreal.MathLibrary.get_date"></a>

#### get_date

```python
@classmethod
def get_date(cls, a: DateTime) -> DateTime
```

X.get_date(a) -> DateTime
Returns the date component of A

Args:
    a (DateTime): 

Returns:
    DateTime:

<a id="unreal.MathLibrary.get_box_volume"></a>

#### get_box_volume

```python
@classmethod
def get_box_volume(cls, box: Box) -> float
```

X.get_box_volume(box) -> double
Gets the volume of this box.

Args:
    box (Box): 

Returns:
    double: The box volume.

<a id="unreal.MathLibrary.get_box_size"></a>

#### get_box_size

```python
@classmethod
def get_box_size(cls, box: Box) -> Vector
```

X.get_box_size(box) -> Vector
Gets the size of this box.

Args:
    box (Box): 

Returns:
    Vector: The box size.

<a id="unreal.MathLibrary.get_box_center"></a>

#### get_box_center

```python
@classmethod
def get_box_center(cls, box: Box) -> Vector
```

X.get_box_center(box) -> Vector
Gets the center point of this box.

Args:
    box (Box): 

Returns:
    Vector: The center point.

<a id="unreal.MathLibrary.get_axes"></a>

#### get_axes

```python
@classmethod
def get_axes(cls, a: Rotator) -> Tuple[Vector, Vector, Vector]
```

X.get_axes(a) -> (x=Vector, y=Vector, z=Vector)
Get the reference frame direction vectors (axes) described by this rotation

Args:
    a (Rotator): 

Returns:
    tuple: 

    x (Vector): 

    y (Vector): 

    z (Vector):

<a id="unreal.MathLibrary.get_abs_max2d"></a>

#### get_abs_max2d

```python
@classmethod
def get_abs_max2d(cls, a: Vector2D) -> float
```

X.get_abs_max2d(a) -> double
Get the maximum absolute value of the vector's components.

Args:
    a (Vector2D): 

Returns:
    double: The maximum absolute value of the vector's components.

<a id="unreal.MathLibrary.get_abs2d"></a>

#### get_abs2d

```python
@classmethod
def get_abs2d(cls, a: Vector2D) -> Vector2D
```

X.get_abs2d(a) -> Vector2D
Get a copy of this vector with absolute value of each component.

Args:
    a (Vector2D): 

Returns:
    Vector2D: A copy of this vector with absolute value of each component.

<a id="unreal.MathLibrary.f_wrap"></a>

#### f_wrap

```python
@classmethod
def f_wrap(cls,
           value: float,
           min: float = 0.000000,
           max: float = 1.000000) -> float
```

X.f_wrap(value, min=0.000000, max=1.000000) -> double
Returns Value wrapped from A and B (inclusive)

Args:
    value (double): 
    min (double): 
    max (double): 

Returns:
    double:

<a id="unreal.MathLibrary.f_trunc_vector"></a>

#### f_trunc_vector

```python
@classmethod
def f_trunc_vector(cls, vector: Vector) -> IntVector
```

X.f_trunc_vector(vector) -> IntVector
Rounds A to an integer with truncation towards zero for each element in a vector.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

Args:
    vector (Vector): 

Returns:
    IntVector:

<a id="unreal.MathLibrary.f_trunc64"></a>

#### f_trunc64

```python
@classmethod
def f_trunc64(cls, a: float) -> int
```

X.f_trunc64(a) -> int64
Rounds A towards zero, truncating the fractional part (e.g., -1.6 becomes -1 and 1.6 becomes 1)

Args:
    a (double): 

Returns:
    int64:

<a id="unreal.MathLibrary.f_trunc"></a>

#### f_trunc

```python
@classmethod
def f_trunc(cls, a: float) -> int
```

X.f_trunc(a) -> int32
Rounds A towards zero, truncating the fractional part (e.g., -1.6 becomes -1 and 1.6 becomes 1)

Args:
    a (double): 

Returns:
    int32:

<a id="unreal.MathLibrary.from_unix_timestamp"></a>

#### from_unix_timestamp

```python
@classmethod
def from_unix_timestamp(cls, unix_time: int) -> DateTime
```

X.from_unix_timestamp(unix_time) -> DateTime
Returns the date from Unix time (seconds from midnight 1970-01-01)
see: ToUnixTimestamp

Args:
    unix_time (int64): Unix time (seconds from midnight 1970-01-01)

Returns:
    DateTime: Gregorian date and time.

<a id="unreal.MathLibrary.from_seconds"></a>

#### from_seconds

```python
@classmethod
def from_seconds(cls, seconds: float) -> Timespan
```

X.from_seconds(seconds) -> Timespan
Returns a time span that represents the specified number of seconds

Args:
    seconds (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.from_minutes"></a>

#### from_minutes

```python
@classmethod
def from_minutes(cls, minutes: float) -> Timespan
```

X.from_minutes(minutes) -> Timespan
Returns a time span that represents the specified number of minutes

Args:
    minutes (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.from_milliseconds"></a>

#### from_milliseconds

```python
@classmethod
def from_milliseconds(cls, milliseconds: float) -> Timespan
```

X.from_milliseconds(milliseconds) -> Timespan
Returns a time span that represents the specified number of milliseconds

Args:
    milliseconds (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.from_hours"></a>

#### from_hours

```python
@classmethod
def from_hours(cls, hours: float) -> Timespan
```

X.from_hours(hours) -> Timespan
Returns a time span that represents the specified number of hours

Args:
    hours (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.from_days"></a>

#### from_days

```python
@classmethod
def from_days(cls, days: float) -> Timespan
```

X.from_days(days) -> Timespan
Returns a time span that represents the specified number of days

Args:
    days (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.fraction"></a>

#### fraction

```python
@classmethod
def fraction(cls, a: float) -> float
```

X.fraction(a) -> double
Returns the fractional part of a float.

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.f_mod64"></a>

#### f_mod64

```python
@classmethod
def f_mod64(cls, dividend: float, divisor: float) -> Tuple[int, float]
```

X.f_mod64(dividend, divisor) -> (int64, remainder=double)
Returns the number of times Divisor will go into Dividend (i.e., Dividend divided by Divisor), as well as the remainder

Args:
    dividend (double): 
    divisor (double): 

Returns:
    double: 

    remainder (double):

<a id="unreal.MathLibrary.f_mod"></a>

#### f_mod

```python
@classmethod
def f_mod(cls, dividend: float, divisor: float) -> Tuple[int, float]
```

X.f_mod(dividend, divisor) -> (int32, remainder=double)
Returns the number of times Divisor will go into Dividend (i.e., Dividend divided by Divisor), as well as the remainder

Args:
    dividend (double): 
    divisor (double): 

Returns:
    double: 

    remainder (double):

<a id="unreal.MathLibrary.f_min"></a>

#### f_min

```python
@classmethod
def f_min(cls, a: float, b: float) -> float
```

X.f_min(a, b) -> double
Returns the minimum value of A and B

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.f_max"></a>

#### f_max

```python
@classmethod
def f_max(cls, a: float, b: float) -> float
```

X.f_max(a, b) -> double
Returns the maximum value of A and B

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.float_spring_interp"></a>

#### float_spring_interp

```python
@classmethod
def float_spring_interp(
        cls,
        current: float,
        target: float,
        spring_state: FloatSpringState,
        stiffness: float,
        critical_damping_factor: float,
        delta_time: float,
        mass: float = 1.000000,
        target_velocity_amount: float = 1.000000,
        clamp: bool = False,
        min_value: float = -1.000000,
        max_value: float = 1.000000,
        initialize_from_target: bool = False
) -> Tuple[float, FloatSpringState]
```

X.float_spring_interp(current, target, spring_state, stiffness, critical_damping_factor, delta_time, mass=1.000000, target_velocity_amount=1.000000, clamp=False, min_value=-1.000000, max_value=1.000000, initialize_from_target=False) -> (float, spring_state=FloatSpringState)
Uses a simple spring model to interpolate a float from Current to Target.

Args:
    current (float): Current value
    target (float): Target value
    spring_state (FloatSpringState): Data related to spring model (velocity, error, etc..) - Create a unique variable per spring
    stiffness (float): How stiff the spring model is (more stiffness means more oscillation around the target value)
    critical_damping_factor (float): How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation)
    delta_time (float): Time difference since the last update
    mass (float): Multiplier that acts like mass on a spring
    target_velocity_amount (float): If 1 then the target velocity will be calculated and used, which results following the target more closely/without lag. Values down to zero (recommended when using this to smooth data) will progressively disable this effect.
    clamp (bool): Whether to use the Min/Max values to clamp the motion
    min_value (float): Clamps the minimum output value and cancels the velocity if it reaches this limit
    max_value (float): Clamps the maximum output value and cancels the velocity if it reaches this limit
    initialize_from_target (bool): If set then the current value will be set from the target on the first update

Returns:
    FloatSpringState: 

    spring_state (FloatSpringState): Data related to spring model (velocity, error, etc..) - Create a unique variable per spring

<a id="unreal.MathLibrary.fixed_turn"></a>

#### fixed_turn

```python
@classmethod
def fixed_turn(cls, current: float, desired: float,
               delta_rate: float) -> float
```

X.fixed_turn(current, desired, delta_rate) -> float
Returns a new rotation component value

Args:
    current (float): is the current rotation value
    desired (float): is the desired rotation value
    delta_rate (float): is the rotation amount to apply

Returns:
    float: a new rotation component value clamped in the range (-360,360)

<a id="unreal.MathLibrary.f_interp_to_constant"></a>

#### f_interp_to_constant

```python
@classmethod
def f_interp_to_constant(cls, current: float, target: float, delta_time: float,
                         interp_speed: float) -> float
```

X.f_interp_to_constant(current, target, delta_time, interp_speed) -> double
Tries to reach Target at a constant rate.

Args:
    current (double): Actual position
    target (double): Target position
    delta_time (double): Time since last tick
    interp_speed (double): Interpolation speed

Returns:
    double: New interpolated position

<a id="unreal.MathLibrary.f_interp_to"></a>

#### f_interp_to

```python
@classmethod
def f_interp_to(cls, current: float, target: float, delta_time: float,
                interp_speed: float) -> float
```

X.f_interp_to(current, target, delta_time, interp_speed) -> double
Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    current (double): Actual position
    target (double): Target position
    delta_time (double): Time since last tick
    interp_speed (double): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    double: New interpolated position

<a id="unreal.MathLibrary.f_interp_ease_in_out"></a>

#### f_interp_ease_in_out

```python
@classmethod
def f_interp_ease_in_out(cls, a: float, b: float, alpha: float,
                         exponent: float) -> float
```

X.f_interp_ease_in_out(a, b, alpha, exponent) -> double
Interpolate between A and B, applying an ease in/out function.  Exp controls the degree of the curve.

Args:
    a (double): 
    b (double): 
    alpha (double): 
    exponent (double): 

Returns:
    double:

<a id="unreal.MathLibrary.find_relative_look_at_rotation"></a>

#### find_relative_look_at_rotation

```python
@classmethod
def find_relative_look_at_rotation(cls, start_transform: Transform,
                                   target_location: Vector) -> Rotator
```

X.find_relative_look_at_rotation(start_transform, target_location) -> Rotator
Find a local rotation (range of [-180, 180]) for an object with StartTransform to point at TargetLocation.
Useful for getting LookAt Azimuth or Pawn Aim Offset.

Args:
    start_transform (Transform): 
    target_location (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.find_nearest_points_on_line_segments"></a>

#### find_nearest_points_on_line_segments

```python
@classmethod
def find_nearest_points_on_line_segments(
        cls, segment1_start: Vector, segment1_end: Vector,
        segment2_start: Vector, segment2_end: Vector) -> Tuple[Vector, Vector]
```

X.find_nearest_points_on_line_segments(segment1_start, segment1_end, segment2_start, segment2_end) -> (segment1_point=Vector, segment2_point=Vector)
Find closest points between 2 segments.

Args:
    segment1_start (Vector): Start of the 1st segment.
    segment1_end (Vector): End of the 1st segment.
    segment2_start (Vector): Start of the 2nd segment.
    segment2_end (Vector): End of the 2nd segment.

Returns:
    tuple: 

    segment1_point (Vector): Closest point on segment 1 to segment 2.

    segment2_point (Vector): Closest point on segment 2 to segment 1.

<a id="unreal.MathLibrary.find_look_at_rotation"></a>

#### find_look_at_rotation

```python
@classmethod
def find_look_at_rotation(cls, start: Vector, target: Vector) -> Rotator
```

X.find_look_at_rotation(start, target) -> Rotator
Find a rotation for an object at Start location to point at Target location.

Args:
    start (Vector): 
    target (Vector): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.find_closest_point_on_segment"></a>

#### find_closest_point_on_segment

```python
@classmethod
def find_closest_point_on_segment(cls, point: Vector, segment_start: Vector,
                                  segment_end: Vector) -> Vector
```

X.find_closest_point_on_segment(point, segment_start, segment_end) -> Vector
Find the closest point on a segment to a given point.

Args:
    point (Vector): Point for which we find the closest point on the segment.
    segment_start (Vector): Start of the segment.
    segment_end (Vector): End of the segment.

Returns:
    Vector: The closest point on the segment to the given point.

<a id="unreal.MathLibrary.find_closest_point_on_line"></a>

#### find_closest_point_on_line

```python
@classmethod
def find_closest_point_on_line(cls, point: Vector, line_origin: Vector,
                               line_direction: Vector) -> Vector
```

X.find_closest_point_on_line(point, line_origin, line_direction) -> Vector
Find the closest point on an infinite line to a given point.

Args:
    point (Vector): Point for which we find the closest point on the line.
    line_origin (Vector): Point of reference on the line.
    line_direction (Vector): Direction of the line. Not required to be normalized.

Returns:
    Vector: The closest point on the line to the given point.

<a id="unreal.MathLibrary.f_floor64"></a>

#### f_floor64

```python
@classmethod
def f_floor64(cls, a: float) -> int
```

X.f_floor64(a) -> int64
Rounds A down towards negative infinity / down to the previous integer (e.g., -1.6 becomes -2 and 1.6 becomes 1)

Args:
    a (double): 

Returns:
    int64:

<a id="unreal.MathLibrary.f_floor"></a>

#### f_floor

```python
@classmethod
def f_floor(cls, a: float) -> int
```

X.f_floor(a) -> int32
Rounds A down towards negative infinity / down to the previous integer (e.g., -1.6 becomes -2 and 1.6 becomes 1)

Args:
    a (double): 

Returns:
    int32:

<a id="unreal.MathLibrary.f_clamp"></a>

#### f_clamp

```python
@classmethod
def f_clamp(cls,
            value: float,
            min: float = 0.000000,
            max: float = 1.000000) -> float
```

X.f_clamp(value, min=0.000000, max=1.000000) -> double
Returns Value clamped between A and B (inclusive)

Args:
    value (double): 
    min (double): 
    max (double): 

Returns:
    double:

<a id="unreal.MathLibrary.f_ceil64"></a>

#### f_ceil64

```python
@classmethod
def f_ceil64(cls, a: float) -> int
```

X.f_ceil64(a) -> int64
Rounds A up towards positive infinity / up to the next integer (e.g., -1.6 becomes -1 and 1.6 becomes 2)

Args:
    a (double): 

Returns:
    int64:

<a id="unreal.MathLibrary.f_ceil"></a>

#### f_ceil

```python
@classmethod
def f_ceil(cls, a: float) -> int
```

X.f_ceil(a) -> int32
Rounds A up towards positive infinity / up to the next integer (e.g., -1.6 becomes -1 and 1.6 becomes 2)

Args:
    a (double): 

Returns:
    int32:

<a id="unreal.MathLibrary.exp"></a>

#### exp

```python
@classmethod
def exp(cls, a: float) -> float
```

X.exp(a) -> double
Returns exponential(e) to the power A (e^A)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.equal_exactly_vector_vector"></a>

#### equal_exactly_vector_vector

```python
@classmethod
def equal_exactly_vector_vector(cls, a: Vector, b: Vector) -> bool
```

X.equal_exactly_vector_vector(a, b) -> bool
Returns true if vector A is equal to vector B (A == B)

Args:
    a (Vector): 
    b (Vector): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_exactly_vector4_vector4"></a>

#### equal_exactly_vector4_vector4

```python
@classmethod
def equal_exactly_vector4_vector4(cls, a: Vector4, b: Vector4) -> bool
```

X.equal_exactly_vector4_vector4(a, b) -> bool
Returns true if vector A is equal to vector B (A == B)

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_exactly_vector2d_vector2d"></a>

#### equal_exactly_vector2d_vector2d

```python
@classmethod
def equal_exactly_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> bool
```

X.equal_exactly_vector2d_vector2d(a, b) -> bool
Returns true if vector A is equal to vector B (A == B)

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_vector_vector"></a>

#### equal_equal_vector_vector

```python
@classmethod
def equal_equal_vector_vector(cls,
                              a: Vector,
                              b: Vector,
                              error_tolerance: float = 0.000100) -> bool
```

X.equal_equal_vector_vector(a, b, error_tolerance=0.000100) -> bool
Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

Args:
    a (Vector): 
    b (Vector): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.nearly_equal_vector_vector"></a>

#### nearly_equal_vector_vector

```python
@classmethod
def nearly_equal_vector_vector(cls,
                               a: Vector,
                               b: Vector,
                               error_tolerance: float = 0.000100) -> bool
```

deprecated: 'nearly_equal_vector_vector' was renamed to 'equal_equal_vector_vector'.

<a id="unreal.MathLibrary.equal_equal_vector4_vector4"></a>

#### equal_equal_vector4_vector4

```python
@classmethod
def equal_equal_vector4_vector4(cls,
                                a: Vector4,
                                b: Vector4,
                                error_tolerance: float = 0.000100) -> bool
```

X.equal_equal_vector4_vector4(a, b, error_tolerance=0.000100) -> bool
Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

Args:
    a (Vector4): 
    b (Vector4): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_vector2d_vector2d"></a>

#### equal_equal_vector2d_vector2d

```python
@classmethod
def equal_equal_vector2d_vector2d(cls,
                                  a: Vector2D,
                                  b: Vector2D,
                                  error_tolerance: float = 0.000100) -> bool
```

X.equal_equal_vector2d_vector2d(a, b, error_tolerance=0.000100) -> bool
Returns true if vector2D A is equal to vector2D B (A == B) within a specified error tolerance

Args:
    a (Vector2D): 
    b (Vector2D): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_transform_transform"></a>

#### equal_equal_transform_transform

```python
@classmethod
def equal_equal_transform_transform(cls, a: Transform, b: Transform) -> bool
```

X.equal_equal_transform_transform(a, b) -> bool
Returns true if transform A is equal to transform B

Args:
    a (Transform): 
    b (Transform): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_timespan_timespan"></a>

#### equal_equal_timespan_timespan

```python
@classmethod
def equal_equal_timespan_timespan(cls, a: Timespan, b: Timespan) -> bool
```

X.equal_equal_timespan_timespan(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_rotator_rotator"></a>

#### equal_equal_rotator_rotator

```python
@classmethod
def equal_equal_rotator_rotator(cls,
                                a: Rotator,
                                b: Rotator,
                                error_tolerance: float = 0.000100) -> bool
```

X.equal_equal_rotator_rotator(a, b, error_tolerance=0.000100) -> bool
Returns true if rotator A is equal to rotator B (A == B) within a specified error tolerance

Args:
    a (Rotator): 
    b (Rotator): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.nearly_equal_rotator_rotator"></a>

#### nearly_equal_rotator_rotator

```python
@classmethod
def nearly_equal_rotator_rotator(cls,
                                 a: Rotator,
                                 b: Rotator,
                                 error_tolerance: float = 0.000100) -> bool
```

deprecated: 'nearly_equal_rotator_rotator' was renamed to 'equal_equal_rotator_rotator'.

<a id="unreal.MathLibrary.equal_equal_quat_quat"></a>

#### equal_equal_quat_quat

```python
@classmethod
def equal_equal_quat_quat(cls,
                          a: Quat,
                          b: Quat,
                          tolerance: float = 0.000100) -> bool
```

X.equal_equal_quat_quat(a, b, tolerance=0.000100) -> bool
Returns true if Quaternion A is equal to Quaternion B (A == B) within a specified error tolerance

Args:
    a (Quat): 
    b (Quat): 
    tolerance (float): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_object_object"></a>

#### equal_equal_object_object

```python
@classmethod
def equal_equal_object_object(cls, a: Object, b: Object) -> bool
```

X.equal_equal_object_object(a, b) -> bool
Returns true if A and B are equal (A == B)

Args:
    a (Object): 
    b (Object): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_name_name"></a>

#### equal_equal_name_name

```python
@classmethod
def equal_equal_name_name(cls, a: Name, b: Name) -> bool
```

X.equal_equal_name_name(a, b) -> bool
Returns true if A and B are equal (A == B)

Args:
    a (Name): 
    b (Name): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_matrix_matrix"></a>

#### equal_equal_matrix_matrix

```python
@classmethod
def equal_equal_matrix_matrix(cls,
                              a: Matrix,
                              b: Matrix,
                              tolerance: float = 0.000100) -> bool
```

X.equal_equal_matrix_matrix(a, b, tolerance=0.000100) -> bool
Checks whether another Matrix is equal to this, within specified tolerance.

Args:
    a (Matrix): 
    b (Matrix): 
    tolerance (float): Error Tolerance.

Returns:
    bool: true if two Matrix are equal, within specified tolerance, otherwise false.

<a id="unreal.MathLibrary.equal_equal_linear_color_linear_color"></a>

#### equal_equal_linear_color_linear_color

```python
@classmethod
def equal_equal_linear_color_linear_color(cls, a: LinearColor,
                                          b: LinearColor) -> bool
```

X.equal_equal_linear_color_linear_color(a, b) -> bool
Returns true if linear color A is equal to linear color B (A == B) within a specified error tolerance

Args:
    a (LinearColor): 
    b (LinearColor): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_int_int"></a>

#### equal_equal_int_int

```python
@classmethod
def equal_equal_int_int(cls, a: int, b: int) -> bool
```

X.equal_equal_int_int(a, b) -> bool
Returns true if A is equal to B (A == B)

Args:
    a (int32): 
    b (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_int64_int64"></a>

#### equal_equal_int64_int64

```python
@classmethod
def equal_equal_int64_int64(cls, a: int, b: int) -> bool
```

X.equal_equal_int64_int64(a, b) -> bool
Returns true if A is equal to B (A == B)

Args:
    a (int64): 
    b (int64): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_double_double"></a>

#### equal_equal_double_double

```python
@classmethod
def equal_equal_double_double(cls, a: float, b: float) -> bool
```

X.equal_equal_double_double(a, b) -> bool
Returns true if A is exactly equal to B (A == B)

Args:
    a (double): 
    b (double): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_float_float"></a>

#### equal_equal_float_float

```python
@classmethod
def equal_equal_float_float(cls, a: float, b: float) -> bool
```

deprecated: 'equal_equal_float_float' was renamed to 'equal_equal_double_double'.

<a id="unreal.MathLibrary.equal_equal_date_time_date_time"></a>

#### equal_equal_date_time_date_time

```python
@classmethod
def equal_equal_date_time_date_time(cls, a: DateTime, b: DateTime) -> bool
```

X.equal_equal_date_time_date_time(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_class_class"></a>

#### equal_equal_class_class

```python
@classmethod
def equal_equal_class_class(cls, a: Class, b: Class) -> bool
```

X.equal_equal_class_class(a, b) -> bool
Returns true if A and B are equal (A == B)

Args:
    a (type(Class)): 
    b (type(Class)): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_byte_byte"></a>

#### equal_equal_byte_byte

```python
@classmethod
def equal_equal_byte_byte(cls, a: int, b: int) -> bool
```

X.equal_equal_byte_byte(a, b) -> bool
Returns true if A is equal to B (A == B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_equal_bool_bool"></a>

#### equal_equal_bool_bool

```python
@classmethod
def equal_equal_bool_bool(cls, a: bool, b: bool) -> bool
```

X.equal_equal_bool_bool(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.equal_int_point_int_point"></a>

#### equal_int_point_int_point

```python
@classmethod
def equal_int_point_int_point(cls, a: IntPoint, b: IntPoint) -> bool
```

X.equal_int_point_int_point(a, b) -> bool
Returns true if IntPoint A is equal to IntPoint B (A == B)

Args:
    a (IntPoint): 
    b (IntPoint): 

Returns:
    bool:

<a id="unreal.MathLibrary.dynamic_weighted_moving_average_f_vector"></a>

#### dynamic_weighted_moving_average_f_vector

```python
@classmethod
def dynamic_weighted_moving_average_f_vector(cls, current_sample: Vector,
                                             previous_sample: Vector,
                                             max_distance: float,
                                             min_weight: float,
                                             max_weight: float) -> Vector
```

X.dynamic_weighted_moving_average_f_vector(current_sample, previous_sample, max_distance, min_weight, max_weight) -> Vector
Calculates the new value in a weighted moving average series using the previous value and a weight range.
The weight range is used to dynamically adjust based upon distance between the samples
This allows you to smooth a value more aggressively for small noise and let large movements be smoothed less (or vice versa)

Args:
    current_sample (Vector): The value to blend with the previous sample to get a new weighted value
    previous_sample (Vector): The last value from the series
    max_distance (float): Distance to use as the blend between min weight or max weight
    min_weight (float): The weight use when the distance is small
    max_weight (float): The weight use when the distance is large

Returns:
    Vector: the next value in the series

<a id="unreal.MathLibrary.dynamic_weighted_moving_average_f_rotator"></a>

#### dynamic_weighted_moving_average_f_rotator

```python
@classmethod
def dynamic_weighted_moving_average_f_rotator(cls, current_sample: Rotator,
                                              previous_sample: Rotator,
                                              max_distance: float,
                                              min_weight: float,
                                              max_weight: float) -> Rotator
```

X.dynamic_weighted_moving_average_f_rotator(current_sample, previous_sample, max_distance, min_weight, max_weight) -> Rotator
Calculates the new value in a weighted moving average series using the previous value and a weight range.
The weight range is used to dynamically adjust based upon distance between the samples
This allows you to smooth a value more aggressively for small noise and let large movements be smoothed less (or vice versa)

Args:
    current_sample (Rotator): The value to blend with the previous sample to get a new weighted value
    previous_sample (Rotator): The last value from the series
    max_distance (float): Distance to use as the blend between min weight or max weight
    min_weight (float): The weight use when the distance is small
    max_weight (float): The weight use when the distance is large

Returns:
    Rotator: the next value in the series

<a id="unreal.MathLibrary.dynamic_weighted_moving_average_float"></a>

#### dynamic_weighted_moving_average_float

```python
@classmethod
def dynamic_weighted_moving_average_float(cls, current_sample: float,
                                          previous_sample: float,
                                          max_distance: float,
                                          min_weight: float,
                                          max_weight: float) -> float
```

X.dynamic_weighted_moving_average_float(current_sample, previous_sample, max_distance, min_weight, max_weight) -> float
Calculates the new value in a weighted moving average series using the previous value and a weight range.
The weight range is used to dynamically adjust based upon distance between the samples
This allows you to smooth a value more aggressively for small noise and let large movements be smoothed less (or vice versa)

Args:
    current_sample (float): The value to blend with the previous sample to get a new weighted value
    previous_sample (float): The last value from the series
    max_distance (float): Distance to use as the blend between min weight or max weight
    min_weight (float): The weight use when the distance is small
    max_weight (float): The weight use when the distance is large

Returns:
    float: the next value in the series

<a id="unreal.MathLibrary.dot_product2d"></a>

#### dot_product2d

```python
@classmethod
def dot_product2d(cls, a: Vector2D, b: Vector2D) -> float
```

X.dot_product2d(a, b) -> double
Returns the dot product of two 2d vectors - see http://mathworld.wolfram.com/DotProduct.html

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    double:

<a id="unreal.MathLibrary.dot_vector_vector"></a>

#### dot_vector_vector

```python
@classmethod
def dot_vector_vector(cls, a: Vector, b: Vector) -> float
```

X.dot_vector_vector(a, b) -> double
Returns the dot product of two 3d vectors - see http://mathworld.wolfram.com/DotProduct.html

Args:
    a (Vector): 
    b (Vector): 

Returns:
    double:

<a id="unreal.MathLibrary.divide_vector_vector"></a>

#### divide_vector_vector

```python
@classmethod
def divide_vector_vector(cls,
                         a: Vector,
                         b: Vector = [1.000000, 1.000000, 1.000000]) -> Vector
```

X.divide_vector_vector(a, b=[1.000000, 1.000000, 1.000000]) -> Vector
Element-wise Vector division (Result = {A.x/B.x, A.y/B.y, A.z/B.z})

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.divide_vector_int"></a>

#### divide_vector_int

```python
@classmethod
def divide_vector_int(cls, a: Vector, b: int = 1) -> Vector
```

X.divide_vector_int(a, b=1) -> Vector
Vector divide by an integer

Args:
    a (Vector): 
    b (int32): 

Returns:
    Vector:

<a id="unreal.MathLibrary.divide_vector_float"></a>

#### divide_vector_float

```python
@classmethod
def divide_vector_float(cls, a: Vector, b: float = 1.000000) -> Vector
```

X.divide_vector_float(a, b=1.000000) -> Vector
Vector divide by a float

Args:
    a (Vector): 
    b (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.divide_vector4_vector4"></a>

#### divide_vector4_vector4

```python
@classmethod
def divide_vector4_vector4(cls, a: Vector4, b: Vector4) -> Vector4
```

X.divide_vector4_vector4(a, b) -> Vector4
Element-wise Vector divide (Result = {A.x/B.x, A.y/B.y, A.z/B.z, A.w/B.w})

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.divide_vector2d_vector2d"></a>

#### divide_vector2d_vector2d

```python
@classmethod
def divide_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> Vector2D
```

X.divide_vector2d_vector2d(a, b) -> Vector2D
Element-wise Vector divide (Result = {A.x/B.x, A.y/B.y})

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.divide_vector2d_float"></a>

#### divide_vector2d_float

```python
@classmethod
def divide_vector2d_float(cls, a: Vector2D, b: float = 1.000000) -> Vector2D
```

X.divide_vector2d_float(a, b=1.000000) -> Vector2D
Returns Vector A divided by B

Args:
    a (Vector2D): 
    b (double): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.divide_timespan_float"></a>

#### divide_timespan_float

```python
@classmethod
def divide_timespan_float(cls, a: Timespan, scalar: float) -> Timespan
```

X.divide_timespan_float(a, scalar) -> Timespan
Scalar division (A / s)

Args:
    a (Timespan): 
    scalar (float): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.divide_linear_color_linear_color"></a>

#### divide_linear_color_linear_color

```python
@classmethod
def divide_linear_color_linear_color(cls, a: LinearColor,
                                     b: LinearColor) -> LinearColor
```

X.divide_linear_color_linear_color(a, b) -> LinearColor
Element-wise multiplication of two linear colors (R/R, G/G, B/B, A/A)

Args:
    a (LinearColor): 
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.divide_int_point_int_point"></a>

#### divide_int_point_int_point

```python
@classmethod
def divide_int_point_int_point(cls, a: IntPoint, b: IntPoint) -> IntPoint
```

X.divide_int_point_int_point(a, b) -> IntPoint
Returns IntPoint A divided by B

Args:
    a (IntPoint): 
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.divide_int_point_int"></a>

#### divide_int_point_int

```python
@classmethod
def divide_int_point_int(cls, a: IntPoint, b: int) -> IntPoint
```

X.divide_int_point_int(a, b) -> IntPoint
Division (A * B)

Args:
    a (IntPoint): 
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.divide_int_int"></a>

#### divide_int_int

```python
@classmethod
def divide_int_int(cls, a: int, b: int = 1) -> int
```

X.divide_int_int(a, b=1) -> int32
Division (A / B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.divide_int64_int64"></a>

#### divide_int64_int64

```python
@classmethod
def divide_int64_int64(cls, a: int, b: int = 1) -> int
```

X.divide_int64_int64(a, b=1) -> int64
Division (A / B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.divide_double_double"></a>

#### divide_double_double

```python
@classmethod
def divide_double_double(cls, a: float, b: float = 1.000000) -> float
```

X.divide_double_double(a, b=1.000000) -> double
Division (A / B)

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.divide_float_float"></a>

#### divide_float_float

```python
@classmethod
def divide_float_float(cls, a: float, b: float = 1.000000) -> float
```

deprecated: 'divide_float_float' was renamed to 'divide_double_double'.

<a id="unreal.MathLibrary.divide_byte_byte"></a>

#### divide_byte_byte

```python
@classmethod
def divide_byte_byte(cls, a: int, b: int = 1) -> int
```

X.divide_byte_byte(a, b=1) -> uint8
Division (A / B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.distance_squared2d"></a>

#### distance_squared2d

```python
@classmethod
def distance_squared2d(cls, v1: Vector2D, v2: Vector2D) -> float
```

X.distance_squared2d(v1, v2) -> double
Squared distance between two 2D points.

Args:
    v1 (Vector2D): The first point.
    v2 (Vector2D): The second point.

Returns:
    double: The squared distance between two 2D points.

<a id="unreal.MathLibrary.distance2d"></a>

#### distance2d

```python
@classmethod
def distance2d(cls, v1: Vector2D, v2: Vector2D) -> float
```

X.distance2d(v1, v2) -> double
Distance between two 2D points.

Args:
    v1 (Vector2D): The first point.
    v2 (Vector2D): The second point.

Returns:
    double: The distance between two 2D points.

<a id="unreal.MathLibrary.deg_tan"></a>

#### deg_tan

```python
@classmethod
def deg_tan(cls, a: float) -> float
```

X.deg_tan(a) -> double
Returns the tan of A (expects Degrees)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.deg_sin"></a>

#### deg_sin

```python
@classmethod
def deg_sin(cls, a: float) -> float
```

X.deg_sin(a) -> double
Returns the sin of A (expects Degrees)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.degrees_to_radians"></a>

#### degrees_to_radians

```python
@classmethod
def degrees_to_radians(cls, a: float) -> float
```

X.degrees_to_radians(a) -> double
Returns radians value based on the input degrees

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.deg_cos"></a>

#### deg_cos

```python
@classmethod
def deg_cos(cls, a: float) -> float
```

X.deg_cos(a) -> double
Returns the cos of A (expects Degrees)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.deg_atan2"></a>

#### deg_atan2

```python
@classmethod
def deg_atan2(cls, y: float, x: float) -> float
```

X.deg_atan2(y, x) -> double
Returns the inverse tan (atan2) of A/B (result is in Degrees)

Args:
    y (double): 
    x (double): 

Returns:
    double:

<a id="unreal.MathLibrary.deg_atan"></a>

#### deg_atan

```python
@classmethod
def deg_atan(cls, a: float) -> float
```

X.deg_atan(a) -> double
Returns the inverse tan (atan) (result is in Degrees)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.deg_asin"></a>

#### deg_asin

```python
@classmethod
def deg_asin(cls, a: float) -> float
```

X.deg_asin(a) -> double
Returns the inverse sin (arcsin) of A (result is in Degrees)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.deg_acos"></a>

#### deg_acos

```python
@classmethod
def deg_acos(cls, a: float) -> float
```

X.deg_acos(a) -> double
Returns the inverse cos (arccos) of A (result is in Degrees)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.days_in_year"></a>

#### days_in_year

```python
@classmethod
def days_in_year(cls, year: int) -> int
```

X.days_in_year(year) -> int32
Returns the number of days in the given year

Args:
    year (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.days_in_month"></a>

#### days_in_month

```python
@classmethod
def days_in_month(cls, year: int, month: int) -> int
```

X.days_in_month(year, month) -> int32
Returns the number of days in the given year and month

Args:
    year (int32): 
    month (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.date_time_min_value"></a>

#### date_time_min_value

```python
@classmethod
def date_time_min_value(cls) -> DateTime
```

X.date_time_min_value() -> DateTime
Returns the minimum date and time value

Returns:
    DateTime:

<a id="unreal.MathLibrary.date_time_max_value"></a>

#### date_time_max_value

```python
@classmethod
def date_time_max_value(cls) -> DateTime
```

X.date_time_max_value() -> DateTime
Returns the maximum date and time value

Returns:
    DateTime:

<a id="unreal.MathLibrary.date_time_from_string"></a>

#### date_time_from_string

```python
@classmethod
def date_time_from_string(cls, date_time_string: str) -> Optional[DateTime]
```

X.date_time_from_string(date_time_string) -> DateTime or None
Converts a date string to a DateTime object

Args:
    date_time_string (str): 

Returns:
    DateTime or None: 

    result (DateTime):

<a id="unreal.MathLibrary.date_time_from_iso_string"></a>

#### date_time_from_iso_string

```python
@classmethod
def date_time_from_iso_string(cls, iso_string: str) -> Optional[DateTime]
```

X.date_time_from_iso_string(iso_string) -> DateTime or None
Converts a date string in ISO-8601 format to a DateTime object

Args:
    iso_string (str): 

Returns:
    DateTime or None: 

    result (DateTime):

<a id="unreal.MathLibrary.cross_product2d"></a>

#### cross_product2d

```python
@classmethod
def cross_product2d(cls, a: Vector2D, b: Vector2D) -> float
```

X.cross_product2d(a, b) -> double
Returns the cross product of two 2d vectors - see  http://mathworld.wolfram.com/CrossProduct.html

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    double:

<a id="unreal.MathLibrary.cross_vector_vector"></a>

#### cross_vector_vector

```python
@classmethod
def cross_vector_vector(cls, a: Vector, b: Vector) -> Vector
```

X.cross_vector_vector(a, b) -> Vector
Returns the cross product of two 3d vectors - see http://mathworld.wolfram.com/CrossProduct.html

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.create_vector_from_yaw_pitch"></a>

#### create_vector_from_yaw_pitch

```python
@classmethod
def create_vector_from_yaw_pitch(cls,
                                 yaw: float,
                                 pitch: float,
                                 length: float = 1.000000) -> Vector
```

X.create_vector_from_yaw_pitch(yaw, pitch, length=1.000000) -> Vector
Creates a directional vector from rotation values {Pitch, Yaw} supplied in degrees with specified Length

Args:
    yaw (float): 
    pitch (float): 
    length (float): 

Returns:
    Vector:

<a id="unreal.MathLibrary.cos"></a>

#### cos

```python
@classmethod
def cos(cls, a: float) -> float
```

X.cos(a) -> double
Returns the cosine of A (expects Radians)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.convert3d_to1d"></a>

#### convert3d_to1d

```python
@classmethod
def convert3d_to1d(cls, index3d: IntVector, x_size: int, y_size: int) -> int
```

X.convert3d_to1d(index3d, x_size, y_size) -> int32
Maps a 3D array index to a 1D array index.

Args:
    index3d (IntVector): The 3D array index
    x_size (int32): X dimension of the 3D array
    y_size (int32): Y dimension of the 3D array

Returns:
    int32: The equivalent 1D index of the array

<a id="unreal.MathLibrary.convert2d_to1d"></a>

#### convert2d_to1d

```python
@classmethod
def convert2d_to1d(cls, index2d: IntPoint, x_size: int) -> int
```

X.convert2d_to1d(index2d, x_size) -> int32
Maps a 2D array index to a 1D array index.

Args:
    index2d (IntPoint): The 2D array index
    x_size (int32): X dimension of the 2D array

Returns:
    int32: The equivalent 1D index of the array

<a id="unreal.MathLibrary.convert1d_to3d"></a>

#### convert1d_to3d

```python
@classmethod
def convert1d_to3d(cls, index1d: int, x_size: int, y_size: int) -> IntVector
```

X.convert1d_to3d(index1d, x_size, y_size) -> IntVector
Maps a 1D array index to a 3D array index.

Args:
    index1d (int32): The 1D array index
    x_size (int32): X dimension of the 3D array
    y_size (int32): Y dimension of the 3D array

Returns:
    IntVector: The equivalent 3D index of the array

<a id="unreal.MathLibrary.convert1d_to2d"></a>

#### convert1d_to2d

```python
@classmethod
def convert1d_to2d(cls, index1d: int, x_size: int) -> IntPoint
```

X.convert1d_to2d(index1d, x_size) -> IntPoint
Maps a 1D array index to a 2D array index.

Args:
    index1d (int32): The 1D array index
    x_size (int32): X dimension of the 2D array

Returns:
    IntPoint: The equivalent 2D index of the array

<a id="unreal.MathLibrary.conv_vector_to_vector2d"></a>

#### conv_vector_to_vector2d

```python
@classmethod
def conv_vector_to_vector2d(cls, vector: Vector) -> Vector2D
```

X.conv_vector_to_vector2d(vector) -> Vector2D
Converts a Vector to a Vector2D using the Vector's (X, Y) coordinates

Args:
    vector (Vector): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.conv_vector_to_transform"></a>

#### conv_vector_to_transform

```python
@classmethod
def conv_vector_to_transform(cls, location: Vector) -> Transform
```

X.conv_vector_to_transform(location) -> Transform
Converts a vector to a transform. Uses vector as location

Args:
    location (Vector): 

Returns:
    Transform:

<a id="unreal.MathLibrary.conv_vector_to_rotator"></a>

#### conv_vector_to_rotator

```python
@classmethod
def conv_vector_to_rotator(cls, vec: Vector) -> Rotator
```

X.conv_vector_to_rotator(vec) -> Rotator
Return the FRotator orientation corresponding to the direction in which the vector points.
Sets Yaw and Pitch to the proper numbers, and sets Roll to zero because the roll can't be determined from a vector.

Args:
    vec (Vector): 

Returns:
    Rotator: FRotator from the Vector's direction, without any roll.

<a id="unreal.MathLibrary.conv_vector_to_quaternion"></a>

#### conv_vector_to_quaternion

```python
@classmethod
def conv_vector_to_quaternion(cls, vec: Vector) -> Quat
```

X.conv_vector_to_quaternion(vec) -> Quat
Return the Quaternion orientation corresponding to the direction in which the vector points.
Similar to the FRotator version, returns a result without roll such that it preserves the up vector.
note: If you don't care about preserving the up vector and just want the most direct rotation, you can use the faster 'FindBetweenVectors(ForwardVector, YourVector)' or 'FindBetweenNormals(...)' if you know the vector is of unit length.

Args:
    vec (Vector): 

Returns:
    Quat: Quaternion from the Vector's direction, without any roll.

<a id="unreal.MathLibrary.conv_vector_to_quaterion"></a>

#### conv_vector_to_quaterion

```python
@classmethod
def conv_vector_to_quaterion(cls, vec: Vector) -> Quat
```

deprecated: 'conv_vector_to_quaterion' was renamed to 'conv_vector_to_quaternion'.

<a id="unreal.MathLibrary.conv_vector_to_linear_color"></a>

#### conv_vector_to_linear_color

```python
@classmethod
def conv_vector_to_linear_color(cls, vec: Vector) -> LinearColor
```

X.conv_vector_to_linear_color(vec) -> LinearColor
Converts a vector to LinearColor

Args:
    vec (Vector): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.conv_vector4_to_vector"></a>

#### conv_vector4_to_vector

```python
@classmethod
def conv_vector4_to_vector(cls, vector4: Vector4) -> Vector
```

X.conv_vector4_to_vector(vector4) -> Vector
Converts a Vector4 to a Vector (dropping the W element)

Args:
    vector4 (Vector4): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_vector4_to_rotator"></a>

#### conv_vector4_to_rotator

```python
@classmethod
def conv_vector4_to_rotator(cls, vec: Vector4) -> Rotator
```

X.conv_vector4_to_rotator(vec) -> Rotator
Return the FRotator orientation corresponding to the direction in which the vector points.
Sets Yaw and Pitch to the proper numbers, and sets Roll to zero because the roll can't be determined from a vector.

Args:
    vec (Vector4): 

Returns:
    Rotator: FRotator from the Vector's direction, without any roll.

<a id="unreal.MathLibrary.conv_vector4_to_quaternion"></a>

#### conv_vector4_to_quaternion

```python
@classmethod
def conv_vector4_to_quaternion(cls, vec: Vector4) -> Quat
```

X.conv_vector4_to_quaternion(vec) -> Quat
Return the Quaternion orientation corresponding to the direction in which the vector points.
Similar to the FRotator version, returns a result without roll such that it preserves the up vector.
note: If you don't care about preserving the up vector and just want the most direct rotation, you can use the faster 'FindBetweenVectors(ForwardVector, YourVector)' or 'FindBetweenNormals(...)' if you know the vector is of unit length.

Args:
    vec (Vector4): 

Returns:
    Quat: Quaternion from the Vector's direction, without any roll.

<a id="unreal.MathLibrary.conv_vector4_to_quaterion"></a>

#### conv_vector4_to_quaterion

```python
@classmethod
def conv_vector4_to_quaterion(cls, vec: Vector4) -> Quat
```

deprecated: 'conv_vector4_to_quaterion' was renamed to 'conv_vector4_to_quaternion'.

<a id="unreal.MathLibrary.conv_vector2d_to_vector"></a>

#### conv_vector2d_to_vector

```python
@classmethod
def conv_vector2d_to_vector(cls,
                            vector2d: Vector2D,
                            z: float = 0.000000) -> Vector
```

X.conv_vector2d_to_vector(vector2d, z=0.000000) -> Vector
Converts a Vector2D to a Vector

Args:
    vector2d (Vector2D): 
    z (float): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_vector2d_to_int_point"></a>

#### conv_vector2d_to_int_point

```python
@classmethod
def conv_vector2d_to_int_point(cls, vector2d: Vector2D) -> IntPoint
```

X.conv_vector2d_to_int_point(vector2d) -> IntPoint
Converts a Vector2D to an IntPoint

Args:
    vector2d (Vector2D): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.conv_transform_to_matrix"></a>

#### conv_transform_to_matrix

```python
@classmethod
def conv_transform_to_matrix(cls, transform: Transform) -> Matrix
```

X.conv_transform_to_matrix(transform) -> Matrix
Converts a Transform to a Matrix with scale

Args:
    transform (Transform): 

Returns:
    Matrix:

<a id="unreal.MathLibrary.conv_rotator_to_vector"></a>

#### conv_rotator_to_vector

```python
@classmethod
def conv_rotator_to_vector(cls, rot: Rotator) -> Vector
```

X.conv_rotator_to_vector(rot) -> Vector
Get the X direction vector after this rotation

Args:
    rot (Rotator): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_rotator_to_transform"></a>

#### conv_rotator_to_transform

```python
@classmethod
def conv_rotator_to_transform(cls, rotator: Rotator) -> Transform
```

X.conv_rotator_to_transform(rotator) -> Transform
Converts Rotator to Transform

Args:
    rotator (Rotator): 

Returns:
    Transform:

<a id="unreal.MathLibrary.conv_rotator_to_quaternion"></a>

#### conv_rotator_to_quaternion

```python
@classmethod
def conv_rotator_to_quaternion(cls, rot: Rotator) -> Quat
```

X.conv_rotator_to_quaternion(rot) -> Quat
Converts to Quaternion representation of this Rotator.

Args:
    rot (Rotator): 

Returns:
    Quat:

<a id="unreal.MathLibrary.conv_matrix_to_transform"></a>

#### conv_matrix_to_transform

```python
@classmethod
def conv_matrix_to_transform(cls, matrix: Matrix) -> Transform
```

X.conv_matrix_to_transform(matrix) -> Transform
Converts a Matrix to a Transform
(Assumes Matrix represents a transform)

Args:
    matrix (Matrix): 

Returns:
    Transform:

<a id="unreal.MathLibrary.conv_matrix_to_rotator"></a>

#### conv_matrix_to_rotator

```python
@classmethod
def conv_matrix_to_rotator(cls, matrix: Matrix) -> Rotator
```

X.conv_matrix_to_rotator(matrix) -> Rotator
Converts a Matrix to a Rotator
(Assumes Matrix represents a transform)

Args:
    matrix (Matrix): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.conv_linear_color_to_vector"></a>

#### conv_linear_color_to_vector

```python
@classmethod
def conv_linear_color_to_vector(cls, linear_color: LinearColor) -> Vector
```

X.conv_linear_color_to_vector(linear_color) -> Vector
Converts a LinearColor to a vector

Args:
    linear_color (LinearColor): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_linear_color_to_color"></a>

#### conv_linear_color_to_color

```python
@classmethod
def conv_linear_color_to_color(cls,
                               linear_color: LinearColor,
                               use_srgb: bool = True) -> Color
```

X.conv_linear_color_to_color(linear_color, use_srgb=True) -> Color
Quantizes the linear color and returns the result as a FColor with optional sRGB conversion and quality as goal.

Args:
    linear_color (LinearColor): 
    use_srgb (bool): 

Returns:
    Color:

<a id="unreal.MathLibrary.conv_int_vector_to_vector"></a>

#### conv_int_vector_to_vector

```python
@classmethod
def conv_int_vector_to_vector(cls, int_vector: IntVector) -> Vector
```

X.conv_int_vector_to_vector(int_vector) -> Vector
Converts an IntVector to a vector

Args:
    int_vector (IntVector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_int_to_vector"></a>

#### conv_int_to_vector

```python
@classmethod
def conv_int_to_vector(cls, int: int) -> Vector
```

X.conv_int_to_vector(int) -> Vector
Converts an integer to a FVector

Args:
    int (int32): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_int_to_int_vector"></a>

#### conv_int_to_int_vector

```python
@classmethod
def conv_int_to_int_vector(cls, int: int) -> IntVector
```

X.conv_int_to_int_vector(int) -> IntVector
Converts an integer to an IntVector

Args:
    int (int32): 

Returns:
    IntVector:

<a id="unreal.MathLibrary.conv_int_to_int64"></a>

#### conv_int_to_int64

```python
@classmethod
def conv_int_to_int64(cls, int: int) -> int
```

X.conv_int_to_int64(int) -> int64
Converts an integer to a 64 bit integer

Args:
    int (int32): 

Returns:
    int64:

<a id="unreal.MathLibrary.conv_int_to_double"></a>

#### conv_int_to_double

```python
@classmethod
def conv_int_to_double(cls, int: int) -> float
```

X.conv_int_to_double(int) -> double
Converts an integer to a float

Args:
    int (int32): 

Returns:
    double:

<a id="unreal.MathLibrary.conv_int_to_float"></a>

#### conv_int_to_float

```python
@classmethod
def conv_int_to_float(cls, int: int) -> float
```

deprecated: 'conv_int_to_float' was renamed to 'conv_int_to_double'.

<a id="unreal.MathLibrary.conv_int_to_byte"></a>

#### conv_int_to_byte

```python
@classmethod
def conv_int_to_byte(cls, int: int) -> int
```

X.conv_int_to_byte(int) -> uint8
Converts an integer to a byte (if the integer is too large, returns the low 8 bits)

Args:
    int (int32): 

Returns:
    uint8:

<a id="unreal.MathLibrary.conv_int_to_bool"></a>

#### conv_int_to_bool

```python
@classmethod
def conv_int_to_bool(cls, int: int) -> bool
```

X.conv_int_to_bool(int) -> bool
Converts a int to a bool

Args:
    int (int32): 

Returns:
    bool:

<a id="unreal.MathLibrary.conv_int_point_to_vector2d"></a>

#### conv_int_point_to_vector2d

```python
@classmethod
def conv_int_point_to_vector2d(cls, int_point: IntPoint) -> Vector2D
```

X.conv_int_point_to_vector2d(int_point) -> Vector2D
Converts an IntPoint to a Vector2D

Args:
    int_point (IntPoint): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.conv_int64_to_int"></a>

#### conv_int64_to_int

```python
@classmethod
def conv_int64_to_int(cls, int: int) -> int
```

X.conv_int64_to_int(int) -> int32
Converts a 64 bit integer to a 32 bit integer (if the integer is too large, returns the low 32 bits)

Args:
    int (int64): 

Returns:
    int32:

<a id="unreal.MathLibrary.conv_int64_to_double"></a>

#### conv_int64_to_double

```python
@classmethod
def conv_int64_to_double(cls, int: int) -> float
```

X.conv_int64_to_double(int) -> double
Converts a 64 bit integer to a float

Args:
    int (int64): 

Returns:
    double:

<a id="unreal.MathLibrary.conv_int64_to_byte"></a>

#### conv_int64_to_byte

```python
@classmethod
def conv_int64_to_byte(cls, int: int) -> int
```

X.conv_int64_to_byte(int) -> uint8
Converts a 64 bit integer to a byte (if the integer is too large, returns the low 8 bits)

Args:
    int (int64): 

Returns:
    uint8:

<a id="unreal.MathLibrary.conv_double_to_vector2d"></a>

#### conv_double_to_vector2d

```python
@classmethod
def conv_double_to_vector2d(cls, double: float) -> Vector2D
```

X.conv_double_to_vector2d(double) -> Vector2D
Convert a float into a vector, where each element is that float

Args:
    double (double): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.conv_double_to_vector"></a>

#### conv_double_to_vector

```python
@classmethod
def conv_double_to_vector(cls, double: float) -> Vector
```

X.conv_double_to_vector(double) -> Vector
Converts a double into a vector, where each element is that float

Args:
    double (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.conv_float_to_vector"></a>

#### conv_float_to_vector

```python
@classmethod
def conv_float_to_vector(cls, double: float) -> Vector
```

deprecated: 'conv_float_to_vector' was renamed to 'conv_double_to_vector'.

<a id="unreal.MathLibrary.conv_double_to_linear_color"></a>

#### conv_double_to_linear_color

```python
@classmethod
def conv_double_to_linear_color(cls, double: float) -> LinearColor
```

X.conv_double_to_linear_color(double) -> LinearColor
Converts a float into a LinearColor, where each RGB element is that float

Args:
    double (double): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.conv_float_to_linear_color"></a>

#### conv_float_to_linear_color

```python
@classmethod
def conv_float_to_linear_color(cls, double: float) -> LinearColor
```

deprecated: 'conv_float_to_linear_color' was renamed to 'conv_double_to_linear_color'.

<a id="unreal.MathLibrary.conv_double_to_int64"></a>

#### conv_double_to_int64

```python
@classmethod
def conv_double_to_int64(cls, double: float) -> int
```

X.conv_double_to_int64(double) -> int64
Converts a float to a 64 bit integer

Args:
    double (double): 

Returns:
    int64:

<a id="unreal.MathLibrary.conv_color_to_linear_color"></a>

#### conv_color_to_linear_color

```python
@classmethod
def conv_color_to_linear_color(cls, color: Color) -> LinearColor
```

X.conv_color_to_linear_color(color) -> LinearColor
Converts a color to LinearColor

Args:
    color (Color): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.conv_byte_to_int64"></a>

#### conv_byte_to_int64

```python
@classmethod
def conv_byte_to_int64(cls, byte: int) -> int
```

X.conv_byte_to_int64(byte) -> int64
Converts a byte to an integer

Args:
    byte (uint8): 

Returns:
    int64:

<a id="unreal.MathLibrary.conv_byte_to_int"></a>

#### conv_byte_to_int

```python
@classmethod
def conv_byte_to_int(cls, byte: int) -> int
```

X.conv_byte_to_int(byte) -> int32
Converts a byte to an integer

Args:
    byte (uint8): 

Returns:
    int32:

<a id="unreal.MathLibrary.conv_byte_to_double"></a>

#### conv_byte_to_double

```python
@classmethod
def conv_byte_to_double(cls, byte: int) -> float
```

X.conv_byte_to_double(byte) -> double
Converts a byte to a float

Args:
    byte (uint8): 

Returns:
    double:

<a id="unreal.MathLibrary.conv_byte_to_float"></a>

#### conv_byte_to_float

```python
@classmethod
def conv_byte_to_float(cls, byte: int) -> float
```

deprecated: 'conv_byte_to_float' was renamed to 'conv_byte_to_double'.

<a id="unreal.MathLibrary.conv_bool_to_int"></a>

#### conv_bool_to_int

```python
@classmethod
def conv_bool_to_int(cls, bool: bool) -> int
```

X.conv_bool_to_int(bool) -> int32
Converts a bool to an int

Args:
    bool (bool): 

Returns:
    int32:

<a id="unreal.MathLibrary.conv_bool_to_double"></a>

#### conv_bool_to_double

```python
@classmethod
def conv_bool_to_double(cls, bool: bool) -> float
```

X.conv_bool_to_double(bool) -> double
Converts a bool to a float (0.0 or 1.0)

Args:
    bool (bool): 

Returns:
    double:

<a id="unreal.MathLibrary.conv_bool_to_float"></a>

#### conv_bool_to_float

```python
@classmethod
def conv_bool_to_float(cls, bool: bool) -> float
```

deprecated: 'conv_bool_to_float' was renamed to 'conv_bool_to_double'.

<a id="unreal.MathLibrary.conv_bool_to_byte"></a>

#### conv_bool_to_byte

```python
@classmethod
def conv_bool_to_byte(cls, bool: bool) -> int
```

X.conv_bool_to_byte(bool) -> uint8
Converts a bool to a byte

Args:
    bool (bool): 

Returns:
    uint8:

<a id="unreal.MathLibrary.compose_transforms"></a>

#### compose_transforms

```python
@classmethod
def compose_transforms(cls, a: Transform, b: Transform) -> Transform
```

X.compose_transforms(a, b) -> Transform
Compose two transforms in order: A * B.

Order matters when composing transforms:
A * B will yield a transform that logically first applies A then B to any subsequent transformation.

Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

Args:
    a (Transform): 
    b (Transform): 

Returns:
    Transform: New transform: A * B

<a id="unreal.MathLibrary.compose_rotators"></a>

#### compose_rotators

```python
@classmethod
def compose_rotators(cls, a: Rotator, b: Rotator) -> Rotator
```

X.compose_rotators(a, b) -> Rotator
Combine 2 rotations to give you the resulting rotation of first applying A, then B.

Args:
    a (Rotator): 
    b (Rotator): 

Returns:
    Rotator:

<a id="unreal.MathLibrary.class_is_child_of"></a>

#### class_is_child_of

```python
@classmethod
def class_is_child_of(cls, test_class: Class, parent_class: Class) -> bool
```

X.class_is_child_of(test_class, parent_class) -> bool
Determine if a class is a child of another class.

Args:
    test_class (type(Class)): 
    parent_class (type(Class)): 

Returns:
    bool: true if TestClass == ParentClass, or if TestClass is a child of ParentClass; false otherwise, or if either the value for either parameter is 'None'.

<a id="unreal.MathLibrary.clamp_vector_size"></a>

#### clamp_vector_size

```python
@classmethod
def clamp_vector_size(cls, a: Vector, min: float, max: float) -> Vector
```

X.clamp_vector_size(a, min, max) -> Vector
Create a copy of this vector, with its magnitude/size/length clamped between Min and Max.

Args:
    a (Vector): 
    min (double): 
    max (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.clamp_int64"></a>

#### clamp_int64

```python
@classmethod
def clamp_int64(cls, value: int, min: int, max: int) -> int
```

X.clamp_int64(value, min, max) -> int64
Returns Value clamped to be between A and B (inclusive)

Args:
    value (int64): 
    min (int64): 
    max (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.clamp_axis"></a>

#### clamp_axis

```python
@classmethod
def clamp_axis(cls, angle: float) -> float
```

X.clamp_axis(angle) -> float
Clamps an angle to the range of [0, 360].

Args:
    angle (float): The angle to clamp.

Returns:
    float: The clamped angle.

<a id="unreal.MathLibrary.clamp_axes2d"></a>

#### clamp_axes2d

```python
@classmethod
def clamp_axes2d(cls, a: Vector2D, min_axis_val: float,
                 max_axis_val: float) -> Vector2D
```

X.clamp_axes2d(a, min_axis_val, max_axis_val) -> Vector2D
Creates a copy of this vector with both axes clamped to the given range.

Args:
    a (Vector2D): 
    min_axis_val (double): 
    max_axis_val (double): 

Returns:
    Vector2D: New vector with clamped axes.

<a id="unreal.MathLibrary.clamp_angle"></a>

#### clamp_angle

```python
@classmethod
def clamp_angle(cls, angle_degrees: float, min_angle_degrees: float,
                max_angle_degrees: float) -> float
```

X.clamp_angle(angle_degrees, min_angle_degrees, max_angle_degrees) -> double
Clamps an arbitrary angle to be between the given angles.  Will clamp to nearest boundary.

Args:
    angle_degrees (double): 
    min_angle_degrees (double): "from" angle that defines the beginning of the range of valid angles (sweeping clockwise)
    max_angle_degrees (double): "to" angle that defines the end of the range of valid angles

Returns:
    double: Returns clamped angle in the range -180..180.

<a id="unreal.MathLibrary.clamp"></a>

#### clamp

```python
@classmethod
def clamp(cls, value: int, min: int, max: int) -> int
```

X.clamp(value, min, max) -> int32
Returns Value clamped to be between A and B (inclusive)

Args:
    value (int32): 
    min (int32): 
    max (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.c_interp_to"></a>

#### c_interp_to

```python
@classmethod
def c_interp_to(cls, current: LinearColor, target: LinearColor,
                delta_time: float, interp_speed: float) -> LinearColor
```

X.c_interp_to(current, target, delta_time, interp_speed) -> LinearColor
Interpolate Linear Color from Current to Target. Scaled by distance to Target, so it has a strong start speed and ease out.

Args:
    current (LinearColor): Current Color
    target (LinearColor): Target Color
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    LinearColor: New interpolated Color

<a id="unreal.MathLibrary.break_rot_into_axes"></a>

#### break_rot_into_axes

```python
@classmethod
def break_rot_into_axes(cls, rot: Rotator) -> Tuple[Vector, Vector, Vector]
```

X.break_rot_into_axes(rot) -> (x=Vector, y=Vector, z=Vector)
Breaks apart a rotator into its component axes

Args:
    rot (Rotator): 

Returns:
    tuple: 

    x (Vector): 

    y (Vector): 

    z (Vector):

<a id="unreal.MathLibrary.break_color"></a>

#### break_color

```python
@classmethod
def break_color(cls, color: LinearColor) -> Tuple[float, float, float, float]
```

X.break_color(color) -> (r=float, g=float, b=float, a=float)
Breaks apart a color into individual RGB components (as well as alpha)

Args:
    color (LinearColor): 

Returns:
    tuple: 

    r (float): 

    g (float): 

    b (float): 

    a (float):

<a id="unreal.MathLibrary.box_overlap"></a>

#### box_overlap

```python
@classmethod
def box_overlap(cls, a: Box, b: Box) -> Box
```

X.box_overlap(a, b) -> Box
Returns the overlap TBox<T> of two boxes

Args:
    a (Box): The bounding box to test
    b (Box): The bounding box to test overlap against

Returns:
    Box: the overlap box. It can be 0 if they don't overlap

<a id="unreal.MathLibrary.box_is_point_inside"></a>

#### box_is_point_inside

```python
@classmethod
def box_is_point_inside(cls, box: Box, point: Vector) -> bool
```

X.box_is_point_inside(box, point) -> bool
Checks whether the given location is inside this box.
note: This function assumes boxes have open bounds, i.e. points lying on the border of the box are not inside. Use IsPointInBox_Box to include borders in the test.

Args:
    box (Box): The box to test
    point (Vector): The location to test for inside the bounding volume.

Returns:
    bool: true if location is inside this volume.

<a id="unreal.MathLibrary.box_is_inside_or_on"></a>

#### box_is_inside_or_on

```python
@classmethod
def box_is_inside_or_on(cls, inner_test: Box, outer_test: Box) -> bool
```

X.box_is_inside_or_on(inner_test, outer_test) -> bool
Returns true if the InnerTest Box is is completely inside or on OuterTest Box

Args:
    inner_test (Box): The box to check if it is on the inside
    outer_test (Box): The box to check if InnerTest is within or on.

Returns:
    bool: True if InnerTest Box is is completely inside of or on OuterTest Box

<a id="unreal.MathLibrary.box_is_inside"></a>

#### box_is_inside

```python
@classmethod
def box_is_inside(cls, inner_test: Box, outer_test: Box) -> bool
```

X.box_is_inside(inner_test, outer_test) -> bool
Returns true if the InnerTest Box is is completely inside of the OuterTest Box

Args:
    inner_test (Box): The box to check if it is on the inside
    outer_test (Box): The box to check if InnerTest is within.

Returns:
    bool: True if InnerTest Box is is completely inside of OuterTest Box

<a id="unreal.MathLibrary.box_intersects"></a>

#### box_intersects

```python
@classmethod
def box_intersects(cls, a: Box, b: Box) -> bool
```

X.box_intersects(a, b) -> bool
Checks whether the given bounding box A intersects this bounding box B.
note: This function assumes boxes have closed bounds, i.e. boxes with coincident borders on any edge will overlap.

Args:
    a (Box): The bounding box to check intersection against
    b (Box): The bounding box to intersect with.

Returns:
    bool: true if the boxes intersect, false otherwise.

<a id="unreal.MathLibrary.box_get_closest_point_to"></a>

#### box_get_closest_point_to

```python
@classmethod
def box_get_closest_point_to(cls, box: Box, point: Vector) -> Vector
```

X.box_get_closest_point_to(box, point) -> Vector
Calculates the closest point on or inside the box to a given point in space.

Args:
    box (Box): The box to check if the point is inside of
    point (Vector): The point in space

Returns:
    Vector: The closest point on or inside the box.

<a id="unreal.MathLibrary.box_expand_by"></a>

#### box_expand_by

```python
@classmethod
def box_expand_by(cls, box: Box, negative: Vector, positive: Vector) -> Box
```

X.box_expand_by(box, negative, positive) -> Box
Returns a box of increased size.

Args:
    box (Box): 
    negative (Vector): The size to increase the volume by in the negative direction (positive values move the bounds outwards)
    positive (Vector): The size to increase the volume by in the positive direction (positive values move the bounds outwards)

Returns:
    Box: A new bounding box.

<a id="unreal.MathLibrary.boolean_xor"></a>

#### boolean_xor

```python
@classmethod
def boolean_xor(cls, a: bool, b: bool) -> bool
```

X.boolean_xor(a, b) -> bool
Returns the logical eXclusive OR of two values (A XOR B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.boolean_or"></a>

#### boolean_or

```python
@classmethod
def boolean_or(cls, a: bool, b: bool) -> bool
```

X.boolean_or(a, b) -> bool
Returns the logical OR of two values (A OR B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.boolean_nor"></a>

#### boolean_nor

```python
@classmethod
def boolean_nor(cls, a: bool, b: bool) -> bool
```

X.boolean_nor(a, b) -> bool
Returns the logical Not OR of two values (A NOR B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.boolean_nand"></a>

#### boolean_nand

```python
@classmethod
def boolean_nand(cls, a: bool, b: bool) -> bool
```

X.boolean_nand(a, b) -> bool
Returns the logical NAND of two values (A AND B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.boolean_and"></a>

#### boolean_and

```python
@classmethod
def boolean_and(cls, a: bool, b: bool) -> bool
```

X.boolean_and(a, b) -> bool
Returns the logical AND of two values (A AND B)

Args:
    a (bool): 
    b (bool): 

Returns:
    bool:

<a id="unreal.MathLibrary.b_min"></a>

#### b_min

```python
@classmethod
def b_min(cls, a: int, b: int) -> int
```

X.b_min(a, b) -> uint8
Returns the minimum value of A and B

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.b_max"></a>

#### b_max

```python
@classmethod
def b_max(cls, a: int, b: int) -> int
```

X.b_max(a, b) -> uint8
Returns the maximum value of A and B

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.average_of_int_array"></a>

#### average_of_int_array

```python
@classmethod
def average_of_int_array(cls, int_array: Array[int]) -> float
```

X.average_of_int_array(int_array) -> float
Returns average of all array entries. Returns value of 0 if the supplied array is empty.

Args:
    int_array (Array[int32]): 

Returns:
    float: 

    average_value (float):

<a id="unreal.MathLibrary.atan2"></a>

#### atan2

```python
@classmethod
def atan2(cls, y: float, x: float) -> float
```

X.atan2(y, x) -> double
Returns the inverse tan (atan2) of A/B (result is in Radians)

Args:
    y (double): 
    x (double): 

Returns:
    double:

<a id="unreal.MathLibrary.atan"></a>

#### atan

```python
@classmethod
def atan(cls, a: float) -> float
```

X.atan(a) -> double
Returns the inverse tan (atan) (result is in Radians)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.asin"></a>

#### asin

```python
@classmethod
def asin(cls, a: float) -> float
```

X.asin(a) -> double
Returns the inverse sine (arcsin) of A (result is in Radians)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.and_int_int"></a>

#### and_int_int

```python
@classmethod
def and_int_int(cls, a: int, b: int) -> int
```

X.and_int_int(a, b) -> int32
Bitwise AND (A & B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.and_int64_int64"></a>

#### and_int64_int64

```python
@classmethod
def and_int64_int64(cls, a: int, b: int) -> int
```

X.and_int64_int64(a, b) -> int64
Bitwise AND (A & B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.add_vector_vector"></a>

#### add_vector_vector

```python
@classmethod
def add_vector_vector(cls, a: Vector, b: Vector) -> Vector
```

X.add_vector_vector(a, b) -> Vector
Vector addition

Args:
    a (Vector): 
    b (Vector): 

Returns:
    Vector:

<a id="unreal.MathLibrary.add_vector_int"></a>

#### add_vector_int

```python
@classmethod
def add_vector_int(cls, a: Vector, b: int) -> Vector
```

X.add_vector_int(a, b) -> Vector
Adds an integer to each component of a vector

Args:
    a (Vector): 
    b (int32): 

Returns:
    Vector:

<a id="unreal.MathLibrary.add_vector_float"></a>

#### add_vector_float

```python
@classmethod
def add_vector_float(cls, a: Vector, b: float) -> Vector
```

X.add_vector_float(a, b) -> Vector
Adds a float to each component of a vector

Args:
    a (Vector): 
    b (double): 

Returns:
    Vector:

<a id="unreal.MathLibrary.add_vector4_vector4"></a>

#### add_vector4_vector4

```python
@classmethod
def add_vector4_vector4(cls, a: Vector4, b: Vector4) -> Vector4
```

X.add_vector4_vector4(a, b) -> Vector4
Returns addition of Vector A and Vector B (A + B)

Args:
    a (Vector4): 
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.MathLibrary.add_vector2d_vector2d"></a>

#### add_vector2d_vector2d

```python
@classmethod
def add_vector2d_vector2d(cls, a: Vector2D, b: Vector2D) -> Vector2D
```

X.add_vector2d_vector2d(a, b) -> Vector2D
Returns addition of Vector A and Vector B (A + B)

Args:
    a (Vector2D): 
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.add_vector2d_float"></a>

#### add_vector2d_float

```python
@classmethod
def add_vector2d_float(cls, a: Vector2D, b: float) -> Vector2D
```

X.add_vector2d_float(a, b) -> Vector2D
Returns Vector A added by B

Args:
    a (Vector2D): 
    b (double): 

Returns:
    Vector2D:

<a id="unreal.MathLibrary.add_timespan_timespan"></a>

#### add_timespan_timespan

```python
@classmethod
def add_timespan_timespan(cls, a: Timespan, b: Timespan) -> Timespan
```

X.add_timespan_timespan(a, b) -> Timespan
Addition (A + B)

Args:
    a (Timespan): 
    b (Timespan): 

Returns:
    Timespan:

<a id="unreal.MathLibrary.add_quat_quat"></a>

#### add_quat_quat

```python
@classmethod
def add_quat_quat(cls, a: Quat, b: Quat) -> Quat
```

X.add_quat_quat(a, b) -> Quat
Returns addition of Vector A and Vector B (A + B)

Args:
    a (Quat): 
    b (Quat): 

Returns:
    Quat:

<a id="unreal.MathLibrary.add_matrix_matrix"></a>

#### add_matrix_matrix

```python
@classmethod
def add_matrix_matrix(cls, a: Matrix, b: Matrix) -> Matrix
```

X.add_matrix_matrix(a, b) -> Matrix
Gets the result of adding a matrix to this.

Args:
    a (Matrix): 
    b (Matrix): 

Returns:
    Matrix: The result of addition.

<a id="unreal.MathLibrary.add_linear_color_linear_color"></a>

#### add_linear_color_linear_color

```python
@classmethod
def add_linear_color_linear_color(cls, a: LinearColor,
                                  b: LinearColor) -> LinearColor
```

X.add_linear_color_linear_color(a, b) -> LinearColor
Element-wise addition of two linear colors (R+R, G+G, B+B, A+A)

Args:
    a (LinearColor): 
    b (LinearColor): 

Returns:
    LinearColor:

<a id="unreal.MathLibrary.add_int_point_int_point"></a>

#### add_int_point_int_point

```python
@classmethod
def add_int_point_int_point(cls, a: IntPoint, b: IntPoint) -> IntPoint
```

X.add_int_point_int_point(a, b) -> IntPoint
Returns IntPoint A added by B

Args:
    a (IntPoint): 
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.add_int_point_int"></a>

#### add_int_point_int

```python
@classmethod
def add_int_point_int(cls, a: IntPoint, b: int) -> IntPoint
```

X.add_int_point_int(a, b) -> IntPoint
Addition (A - B)

Args:
    a (IntPoint): 
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.MathLibrary.add_int_int"></a>

#### add_int_int

```python
@classmethod
def add_int_int(cls, a: int, b: int = 1) -> int
```

X.add_int_int(a, b=1) -> int32
Addition (A + B)

Args:
    a (int32): 
    b (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.add_int64_int64"></a>

#### add_int64_int64

```python
@classmethod
def add_int64_int64(cls, a: int, b: int = 1) -> int
```

X.add_int64_int64(a, b=1) -> int64
Addition (A + B)

Args:
    a (int64): 
    b (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.add_double_double"></a>

#### add_double_double

```python
@classmethod
def add_double_double(cls, a: float, b: float = 1.000000) -> float
```

X.add_double_double(a, b=1.000000) -> double
Addition (A + B)

Args:
    a (double): 
    b (double): 

Returns:
    double:

<a id="unreal.MathLibrary.add_float_float"></a>

#### add_float_float

```python
@classmethod
def add_float_float(cls, a: float, b: float = 1.000000) -> float
```

deprecated: 'add_float_float' was renamed to 'add_double_double'.

<a id="unreal.MathLibrary.add_date_time_timespan"></a>

#### add_date_time_timespan

```python
@classmethod
def add_date_time_timespan(cls, a: DateTime, b: Timespan) -> DateTime
```

X.add_date_time_timespan(a, b) -> DateTime
Addition (A + B)

Args:
    a (DateTime): 
    b (Timespan): 

Returns:
    DateTime:

<a id="unreal.MathLibrary.add_date_time_date_time"></a>

#### add_date_time_date_time

```python
@classmethod
def add_date_time_date_time(cls, a: DateTime, b: DateTime) -> DateTime
```

X.add_date_time_date_time(a, b) -> DateTime
Addition (A + B)

Args:
    a (DateTime): 
    b (DateTime): 

Returns:
    DateTime:

<a id="unreal.MathLibrary.add_byte_byte"></a>

#### add_byte_byte

```python
@classmethod
def add_byte_byte(cls, a: int, b: int = 1) -> int
```

X.add_byte_byte(a, b=1) -> uint8
Addition (A + B)

Args:
    a (uint8): 
    b (uint8): 

Returns:
    uint8:

<a id="unreal.MathLibrary.acos"></a>

#### acos

```python
@classmethod
def acos(cls, a: float) -> float
```

X.acos(a) -> double
Returns the inverse cosine (arccos) of A (result is in Radians)

Args:
    a (double): 

Returns:
    double:

<a id="unreal.MathLibrary.abs_int64"></a>

#### abs_int64

```python
@classmethod
def abs_int64(cls, a: int) -> int
```

X.abs_int64(a) -> int64
Returns the absolute (positive) value of A

Args:
    a (int64): 

Returns:
    int64:

<a id="unreal.MathLibrary.abs_int"></a>

#### abs_int

```python
@classmethod
def abs_int(cls, a: int) -> int
```

X.abs_int(a) -> int32
Returns the absolute (positive) value of A

Args:
    a (int32): 

Returns:
    int32:

<a id="unreal.MathLibrary.abs"></a>

#### abs

```python
@classmethod
def abs(cls, a: float) -> float
```

X.abs(a) -> double
Returns the absolute (positive) value of A

Args:
    a (double): 

Returns:
    double:

<a id="unreal.RenderingLibrary"></a>