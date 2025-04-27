## Quat Objects

```python
class Quat(StructBase)
```

Quaternion.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Quat.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``w`` (double):  [Read-Write]
- ``x`` (double):  [Read-Write]
- ``y`` (double):  [Read-Write]
- ``z`` (double):  [Read-Write]

<a id="unreal.Quat.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             z: float = 0.000000,
             w: float = 0.000000) -> None
```

<a id="unreal.Quat.x"></a>

#### x

```python
@property
def x() -> float
```

(double):  [Read-Write]

<a id="unreal.Quat.x"></a>

#### x

```python
@x.setter
def x(value: float) -> None
```

<a id="unreal.Quat.y"></a>

#### y

```python
@property
def y() -> float
```

(double):  [Read-Write]

<a id="unreal.Quat.y"></a>

#### y

```python
@y.setter
def y(value: float) -> None
```

<a id="unreal.Quat.z"></a>

#### z

```python
@property
def z() -> float
```

(double):  [Read-Write]

<a id="unreal.Quat.z"></a>

#### z

```python
@z.setter
def z(value: float) -> None
```

<a id="unreal.Quat.w"></a>

#### w

```python
@property
def w() -> float
```

(double):  [Read-Write]

<a id="unreal.Quat.w"></a>

#### w

```python
@w.setter
def w(value: float) -> None
```

<a id="unreal.Quat.subtract"></a>

#### subtract

```python
def subtract(b: Quat) -> Quat
```

x.subtract(b) -> Quat
Returns subtraction of Vector B from Vector A (A - B)

Args:
    b (Quat): 

Returns:
    Quat:

<a id="unreal.Quat.interp_spring_to"></a>

#### interp_spring_to

```python
def interp_spring_to(
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

x.interp_spring_to(target, spring_state, stiffness, critical_damping_factor, delta_time, mass=1.000000, target_velocity_amount=1.000000, initialize_from_target=False) -> (Quat, spring_state=QuaternionSpringState)
Uses a simple spring model to interpolate a quaternion from Current to Target.

Args:
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

<a id="unreal.Quat.vector_up"></a>

#### vector_up

```python
def vector_up() -> Vector
```

x.vector_up() -> Vector
Get the up direction (Z axis) after it has been rotated by this Quaternion.

Returns:
    Vector:

<a id="unreal.Quat.vector_right"></a>

#### vector_right

```python
def vector_right() -> Vector
```

x.vector_right() -> Vector
Get the right direction (Y axis) after it has been rotated by this Quaternion.

Returns:
    Vector:

<a id="unreal.Quat.vector_forward"></a>

#### vector_forward

```python
def vector_forward() -> Vector
```

x.vector_forward() -> Vector
Get the forward direction (X axis) after it has been rotated by this Quaternion.

Returns:
    Vector:

<a id="unreal.Quat.unrotate_vector"></a>

#### unrotate_vector

```python
def unrotate_vector(v: Vector) -> Vector
```

x.unrotate_vector(v) -> Vector
Rotate a vector by the inverse of this quaternion.

Args:
    v (Vector): the vector to be rotated

Returns:
    Vector: vector after rotation by the inverse of this quaternion.

<a id="unreal.Quat.slerp_quat"></a>

#### slerp_quat

```python
def slerp_quat(b: Quat, alpha: float) -> Quat
```

x.slerp_quat(b, alpha) -> Quat
Spherical interpolation between Quaternions. Result is normalized.

Args:
    b (Quat): The target quat we interp to
    alpha (double): The interpolation amount, usually 0 to 1.

Returns:
    Quat: Quat after spherical interpolation

<a id="unreal.Quat.size_squared"></a>

#### size_squared

```python
def size_squared() -> float
```

x.size_squared() -> float
Get the squared length of the quaternion.

Returns:
    float: The squared length of the quaternion.

<a id="unreal.Quat.size"></a>

#### size

```python
def size() -> float
```

x.size() -> float
Get the length of the quaternion.

Returns:
    float: The length of the quaternion.

<a id="unreal.Quat.set_from_euler"></a>

#### set_from_euler

```python
def set_from_euler(euler: Vector) -> None
```

x.set_from_euler(euler) -> None
Convert a vector of floating-point Euler angles (in degrees) into a Quaternion.

Args:
    euler (Vector): the Euler angles

<a id="unreal.Quat.set_components"></a>

#### set_components

```python
def set_components(x: float, y: float, z: float, w: float) -> None
```

x.set_components(x, y, z, w) -> None
Set X, Y, Z, W components of Quaternion.

Args:
    x (float): 
    y (float): 
    z (float): 
    w (float):

<a id="unreal.Quat.rotator"></a>

#### rotator

```python
def rotator() -> Rotator
```

x.rotator() -> Rotator
Converts to Rotator representation of this Quaternion.

Returns:
    Rotator:

<a id="unreal.Quat.rotate_vector"></a>

#### rotate_vector

```python
def rotate_vector(v: Vector) -> Vector
```

x.rotate_vector(v) -> Vector
Rotate a vector by this quaternion.

Args:
    v (Vector): the vector to be rotated

Returns:
    Vector: vector after rotation

<a id="unreal.Quat.normalized"></a>

#### normalized

```python
def normalized(tolerance: float = 0.000100) -> Quat
```

x.normalized(tolerance=0.000100) -> Quat
Get a normalized copy of this quaternion.
If it is too small, returns an identity quaternion.

Args:
    tolerance (float): Minimum squared length of quaternion for normalization.

Returns:
    Quat:

<a id="unreal.Quat.normalize"></a>

#### normalize

```python
def normalize(tolerance: float = 0.000100) -> None
```

x.normalize(tolerance=0.000100) -> None
Normalize this quaternion if it is large enough as compared to the supplied tolerance.
If it is too small then set it to the identity quaternion.

Args:
    tolerance (float): Minimum squared length of quaternion for normalization.

<a id="unreal.Quat.log"></a>

#### log

```python
def log() -> Quat
```

x.log() -> Quat
Quaternion with W=0 and V=theta*v. Used in combination with Exp().

Returns:
    Quat:

<a id="unreal.Quat.is_normalized"></a>

#### is_normalized

```python
def is_normalized() -> bool
```

x.is_normalized() -> bool
Return true if this quaternion is normalized

Returns:
    bool:

<a id="unreal.Quat.is_non_finite"></a>

#### is_non_finite

```python
def is_non_finite() -> bool
```

x.is_non_finite() -> bool
Determine if there are any non-finite values (NaN or Inf) in this Quat.

Returns:
    bool:

<a id="unreal.Quat.is_identity"></a>

#### is_identity

```python
def is_identity(tolerance: float = 0.000100) -> bool
```

x.is_identity(tolerance=0.000100) -> bool
Checks whether this Quaternion is an Identity Quaternion.
Assumes Quaternion tested is normalized.

Args:
    tolerance (float): Error tolerance for comparison with Identity Quaternion.

Returns:
    bool: true if Quaternion is a normalized Identity Quaternion.

<a id="unreal.Quat.is_finite"></a>

#### is_finite

```python
def is_finite() -> bool
```

x.is_finite() -> bool
Determine if all the values  are finite (not NaN nor Inf) in this Quat.

Returns:
    bool:

<a id="unreal.Quat.inversed"></a>

#### inversed

```python
def inversed() -> Quat
```

x.inversed() -> Quat
Return an inversed copy of this quaternion.

Returns:
    Quat:

<a id="unreal.Quat.get_rotation_axis"></a>

#### get_rotation_axis

```python
def get_rotation_axis() -> Vector
```

x.get_rotation_axis() -> Vector
Get the axis of rotation of the Quaternion.
This is the axis around which rotation occurs to transform the canonical coordinate system to the target orientation.
For the identity Quaternion which has no such rotation, FVector(1,0,0) is returned.

Returns:
    Vector:

<a id="unreal.Quat.get_axis_z"></a>

#### get_axis_z

```python
def get_axis_z() -> Vector
```

x.get_axis_z() -> Vector
Get the up direction (Z axis) after it has been rotated by this Quaternion.

Returns:
    Vector:

<a id="unreal.Quat.get_axis_y"></a>

#### get_axis_y

```python
def get_axis_y() -> Vector
```

x.get_axis_y() -> Vector
Get the right direction (Y axis) after it has been rotated by this Quaternion.

Returns:
    Vector:

<a id="unreal.Quat.get_axis_x"></a>

#### get_axis_x

```python
def get_axis_x() -> Vector
```

x.get_axis_x() -> Vector
Get the forward direction (X axis) after it has been rotated by this Quaternion.

Returns:
    Vector:

<a id="unreal.Quat.get_angle"></a>

#### get_angle

```python
def get_angle() -> float
```

x.get_angle() -> float
Get the angle of this quaternion

Returns:
    float:

<a id="unreal.Quat.exp"></a>

#### exp

```python
def exp() -> Quat
```

x.exp() -> Quat
Used in combination with Log().
Assumes a quaternion with W=0 and V=theta*v (where |v| = 1).
Exp(q) = (sin(theta)*v, cos(theta))

Returns:
    Quat:

<a id="unreal.Quat.euler"></a>

#### euler

```python
def euler() -> Vector
```

x.euler() -> Vector
Convert a Quaternion into floating-point Euler angles (in degrees).

Returns:
    Vector:

<a id="unreal.Quat.ensure_shortest_arc_to"></a>

#### ensure_shortest_arc_to

```python
def ensure_shortest_arc_to(b: Quat) -> None
```

x.ensure_shortest_arc_to(b) -> None
Modify the quaternion to ensure that the delta between it and B represents the shortest possible rotation angle.

Args:
    b (Quat):

<a id="unreal.Quat.angular_distance"></a>

#### angular_distance

```python
def angular_distance(b: Quat) -> float
```

x.angular_distance(b) -> float
Find the angular distance/difference between two rotation quaternions.

Args:
    b (Quat): Quaternion to find angle distance to

Returns:
    float: angular distance in radians

<a id="unreal.Quat.not_equal"></a>

#### not_equal

```python
def not_equal(b: Quat, error_tolerance: float = 0.000100) -> bool
```

x.not_equal(b, error_tolerance=0.000100) -> bool
Returns true if Quat A is not equal to Quat B (A != B) within a specified error tolerance

Args:
    b (Quat): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Quat.multiply"></a>

#### multiply

```python
def multiply(b: Quat) -> Quat
```

x.multiply(b) -> Quat
Gets the result of multiplying two quaternions (A * B).

Order matters when composing quaternions: C = A * B will yield a quaternion C that logically
first applies B then A to any subsequent transformation (right first, then left).

Args:
    b (Quat): The Quaternion to multiply by.

Returns:
    Quat: The result of multiplication (A * B).

<a id="unreal.Quat.equals"></a>

#### equals

```python
def equals(b: Quat, tolerance: float = 0.000100) -> bool
```

x.equals(b, tolerance=0.000100) -> bool
Returns true if Quaternion A is equal to Quaternion B (A == B) within a specified error tolerance

Args:
    b (Quat): 
    tolerance (float): 

Returns:
    bool:

<a id="unreal.Quat.add"></a>

#### add

```python
def add(b: Quat) -> Quat
```

x.add(b) -> Quat
Returns addition of Vector A and Vector B (A + B)

Args:
    b (Quat): 

Returns:
    Quat:

<a id="unreal.Quat.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Quat`` Returns true if Quaternion A is equal to Quaternion B (A == B) within a specified error tolerance

<a id="unreal.Quat.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``Quat`` Returns true if Quat A is not equal to Quat B (A != B) within a specified error tolerance

<a id="unreal.Quat.__add__"></a>

#### __add__

```python
def __add__(other: Quat) -> None
```

**Overloads:**

- ``Quat`` Returns addition of Vector A and Vector B (A + B)

<a id="unreal.Quat.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: Quat) -> None
```

**Overloads:**

- ``Quat`` Returns addition of Vector A and Vector B (A + B)

<a id="unreal.Quat.__sub__"></a>

#### __sub__

```python
def __sub__(other: Quat) -> None
```

**Overloads:**

- ``Quat`` Returns subtraction of Vector B from Vector A (A - B)

<a id="unreal.Quat.__isub__"></a>

#### __isub__

```python
def __isub__(other: Quat) -> None
```

**Overloads:**

- ``Quat`` Returns subtraction of Vector B from Vector A (A - B)

<a id="unreal.Quat.__mul__"></a>

#### __mul__

```python
def __mul__(other: Quat) -> None
```

**Overloads:**

- ``Quat`` Gets the result of multiplying two quaternions (A * B).

  Order matters when composing quaternions: C = A * B will yield a quaternion C that logically
  first applies B then A to any subsequent transformation (right first, then left).

  @param B The Quaternion to multiply by.
  @return The result of multiplication (A * B).

<a id="unreal.Quat.__imul__"></a>

#### __imul__

```python
def __imul__(other: Quat) -> None
```

**Overloads:**

- ``Quat`` Gets the result of multiplying two quaternions (A * B).

  Order matters when composing quaternions: C = A * B will yield a quaternion C that logically
  first applies B then A to any subsequent transformation (right first, then left).

  @param B The Quaternion to multiply by.
  @return The result of multiplication (A * B).

<a id="unreal.Quat.IDENTITY"></a>

#### IDENTITY

(Quat): Identity quaternion constant

<a id="unreal.InterpCurvePointTwoVectors"></a>