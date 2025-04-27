## Vector2D Objects

```python
class Vector2D(StructBase)
```

A vector in 2-D space composed of components (X, Y) with floating point precision.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Vector2D.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``x`` (double):  [Read-Write]
- ``y`` (double):  [Read-Write]

<a id="unreal.Vector2D.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000, y: float = 0.000000) -> None
```

<a id="unreal.Vector2D.x"></a>

#### x

```python
@property
def x() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector2D.x"></a>

#### x

```python
@x.setter
def x(value: float) -> None
```

<a id="unreal.Vector2D.y"></a>

#### y

```python
@property
def y() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector2D.y"></a>

#### y

```python
@y.setter
def y(value: float) -> None
```

<a id="unreal.Vector2D.length_squared"></a>

#### length_squared

```python
def length_squared() -> float
```

x.length_squared() -> double
Returns the squared length of a 2D Vector.

Returns:
    double:

<a id="unreal.Vector2D.length"></a>

#### length

```python
def length() -> float
```

x.length() -> double
Returns the length of a 2D Vector.

Returns:
    double:

<a id="unreal.Vector2D.interp_to_constant"></a>

#### interp_to_constant

```python
def interp_to_constant(target: Vector2D, delta_time: float,
                       interp_speed: float) -> Vector2D
```

x.interp_to_constant(target, delta_time, interp_speed) -> Vector2D
Tries to reach Target at a constant rate.

Args:
    target (Vector2D): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed

Returns:
    Vector2D: New interpolated position

<a id="unreal.Vector2D.interp_to"></a>

#### interp_to

```python
def interp_to(target: Vector2D, delta_time: float,
              interp_speed: float) -> Vector2D
```

x.interp_to(target, delta_time, interp_speed) -> Vector2D
Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    target (Vector2D): Target position
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Vector2D: New interpolated position

<a id="unreal.Vector2D.to_sign"></a>

#### to_sign

```python
def to_sign() -> Vector2D
```

x.to_sign() -> Vector2D
Get a copy of the vector as sign only.
Each component is set to +1 or -1, with the sign of zero treated as +1.

Returns:
    Vector2D: A copy of the vector with each component set to +1 or -1

<a id="unreal.Vector2D.to_rounded"></a>

#### to_rounded

```python
def to_rounded() -> Vector2D
```

x.to_rounded() -> Vector2D
Get this vector as a vector where each component has been rounded to the nearest int.

Returns:
    Vector2D: New FVector2D from this vector that is rounded.

<a id="unreal.Vector2D.to_direction_and_length"></a>

#### to_direction_and_length

```python
def to_direction_and_length() -> Tuple[Vector2D, float]
```

x.to_direction_and_length() -> (out_dir=Vector2D, out_length=double)
Util to convert this vector into a unit direction vector and its original length.

Returns:
    tuple: 

    out_dir (Vector2D): Reference passed in to store unit direction vector.

    out_length (double): Reference passed in to store length of the vector.

<a id="unreal.Vector2D.subtract"></a>

#### subtract

```python
def subtract(b: Vector2D) -> Vector2D
```

x.subtract(b) -> Vector2D
Returns subtraction of Vector B from Vector A (A - B)

Args:
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.subtract_float"></a>

#### subtract_float

```python
def subtract_float(b: float) -> Vector2D
```

x.subtract_float(b) -> Vector2D
Returns Vector A subtracted by B

Args:
    b (double): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.spherical_to_unit_cartesian"></a>

#### spherical_to_unit_cartesian

```python
def spherical_to_unit_cartesian() -> Vector
```

x.spherical_to_unit_cartesian() -> Vector
Converts spherical coordinates on the unit sphere into a Cartesian unit length vector.

Returns:
    Vector:

<a id="unreal.Vector2D.set"></a>

#### set

```python
def set(x: float, y: float) -> None
```

x.set(x, y) -> None
Set the values of the vector directly.

Args:
    x (double): 
    y (double):

<a id="unreal.Vector2D.not_equal"></a>

#### not_equal

```python
def not_equal(b: Vector2D) -> bool
```

x.not_equal(b) -> bool
Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

Args:
    b (Vector2D): 

Returns:
    bool:

<a id="unreal.Vector2D.is_not_near_equal"></a>

#### is_not_near_equal

```python
def is_not_near_equal(b: Vector2D, error_tolerance: float = 0.000100) -> bool
```

x.is_not_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

Args:
    b (Vector2D): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Vector2D.normal"></a>

#### normal

```python
def normal(tolerance: float = 0.000000) -> Vector2D
```

x.normal(tolerance=0.000000) -> Vector2D
Gets a normalized copy of the vector, checking it is safe to do so based on the length.
Returns zero vector if vector length is too small to safely normalize.

Args:
    tolerance (float): Minimum squared length of vector for normalization.

Returns:
    Vector2D: A normalized copy of the vector if safe, (0,0) otherwise.

<a id="unreal.Vector2D.normalize"></a>

#### normalize

```python
def normalize(tolerance: float = 0.000000) -> None
```

x.normalize(tolerance=0.000000) -> None
Normalize this vector in-place if it is large enough, set it to (0,0) otherwise.
see: NormalSafe2D()

Args:
    tolerance (float): Minimum squared length of vector for normalization.

<a id="unreal.Vector2D.normal_unsafe"></a>

#### normal_unsafe

```python
def normal_unsafe() -> Vector2D
```

x.normal_unsafe() -> Vector2D
Returns a unit normal version of the 2D vector

Returns:
    Vector2D:

<a id="unreal.Vector2D.negated"></a>

#### negated

```python
def negated() -> Vector2D
```

x.negated() -> Vector2D
Gets a negated copy of the vector.

Returns:
    Vector2D:

<a id="unreal.Vector2D.multiply"></a>

#### multiply

```python
def multiply(b: Vector2D) -> Vector2D
```

x.multiply(b) -> Vector2D
Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y})

Args:
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.multiply_float"></a>

#### multiply_float

```python
def multiply_float(b: float) -> Vector2D
```

x.multiply_float(b) -> Vector2D
Returns Vector A scaled by B

Args:
    b (double): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.is_zero"></a>

#### is_zero

```python
def is_zero() -> bool
```

x.is_zero() -> bool
Checks whether all components of the vector are exactly zero.

Returns:
    bool: true if vector is exactly zero, otherwise false.

<a id="unreal.Vector2D.is_nearly_zero"></a>

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

<a id="unreal.Vector2D.get_rotated"></a>

#### get_rotated

```python
def get_rotated(angle_deg: float) -> Vector2D
```

x.get_rotated(angle_deg) -> Vector2D
Rotates around axis (0,0,1)

Args:
    angle_deg (float): Angle to rotate (in degrees)

Returns:
    Vector2D: Rotated Vector

<a id="unreal.Vector2D.get_min"></a>

#### get_min

```python
def get_min() -> float
```

x.get_min() -> double
Get the minimum value of the vector's components.

Returns:
    double: The minimum value of the vector's components.

<a id="unreal.Vector2D.get_max"></a>

#### get_max

```python
def get_max() -> float
```

x.get_max() -> double
Get the maximum value of the vector's components.

Returns:
    double: The maximum value of the vector's components.

<a id="unreal.Vector2D.get_abs_max"></a>

#### get_abs_max

```python
def get_abs_max() -> float
```

x.get_abs_max() -> double
Get the maximum absolute value of the vector's components.

Returns:
    double: The maximum absolute value of the vector's components.

<a id="unreal.Vector2D.get_abs"></a>

#### get_abs

```python
def get_abs() -> Vector2D
```

x.get_abs() -> Vector2D
Get a copy of this vector with absolute value of each component.

Returns:
    Vector2D: A copy of this vector with absolute value of each component.

<a id="unreal.Vector2D.equals"></a>

#### equals

```python
def equals(b: Vector2D) -> bool
```

x.equals(b) -> bool
Returns true if vector A is equal to vector B (A == B)

Args:
    b (Vector2D): 

Returns:
    bool:

<a id="unreal.Vector2D.is_near_equal"></a>

#### is_near_equal

```python
def is_near_equal(b: Vector2D, error_tolerance: float = 0.000100) -> bool
```

x.is_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if vector2D A is equal to vector2D B (A == B) within a specified error tolerance

Args:
    b (Vector2D): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Vector2D.dot"></a>

#### dot

```python
def dot(b: Vector2D) -> float
```

x.dot(b) -> double
Returns the dot product of two 2d vectors - see http://mathworld.wolfram.com/DotProduct.html

Args:
    b (Vector2D): 

Returns:
    double:

<a id="unreal.Vector2D.divide"></a>

#### divide

```python
def divide(b: Vector2D) -> Vector2D
```

x.divide(b) -> Vector2D
Element-wise Vector divide (Result = {A.x/B.x, A.y/B.y})

Args:
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.divide_float"></a>

#### divide_float

```python
def divide_float(b: float = 1.000000) -> Vector2D
```

x.divide_float(b=1.000000) -> Vector2D
Returns Vector A divided by B

Args:
    b (double): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.distance_squared"></a>

#### distance_squared

```python
def distance_squared(v2: Vector2D) -> float
```

x.distance_squared(v2) -> double
Squared distance between two 2D points.

Args:
    v2 (Vector2D): The second point.

Returns:
    double: The squared distance between two 2D points.

<a id="unreal.Vector2D.distance"></a>

#### distance

```python
def distance(v2: Vector2D) -> float
```

x.distance(v2) -> double
Distance between two 2D points.

Args:
    v2 (Vector2D): The second point.

Returns:
    double: The distance between two 2D points.

<a id="unreal.Vector2D.cross"></a>

#### cross

```python
def cross(b: Vector2D) -> float
```

x.cross(b) -> double
Returns the cross product of two 2d vectors - see  http://mathworld.wolfram.com/CrossProduct.html

Args:
    b (Vector2D): 

Returns:
    double:

<a id="unreal.Vector2D.vector"></a>

#### vector

```python
def vector(z: float = 0.000000) -> Vector
```

x.vector(z=0.000000) -> Vector
Converts a Vector2D to a Vector

Args:
    z (float): 

Returns:
    Vector:

<a id="unreal.Vector2D.int_point"></a>

#### int_point

```python
def int_point() -> IntPoint
```

x.int_point() -> IntPoint
Converts a Vector2D to an IntPoint

Returns:
    IntPoint:

<a id="unreal.Vector2D.clamped_axes"></a>

#### clamped_axes

```python
def clamped_axes(min_axis_val: float, max_axis_val: float) -> Vector2D
```

x.clamped_axes(min_axis_val, max_axis_val) -> Vector2D
Creates a copy of this vector with both axes clamped to the given range.

Args:
    min_axis_val (double): 
    max_axis_val (double): 

Returns:
    Vector2D: New vector with clamped axes.

<a id="unreal.Vector2D.add"></a>

#### add

```python
def add(b: Vector2D) -> Vector2D
```

x.add(b) -> Vector2D
Returns addition of Vector A and Vector B (A + B)

Args:
    b (Vector2D): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.add_float"></a>

#### add_float

```python
def add_float(b: float) -> Vector2D
```

x.add_float(b) -> Vector2D
Returns Vector A added by B

Args:
    b (double): 

Returns:
    Vector2D:

<a id="unreal.Vector2D.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Vector2D`` Returns true if vector A is equal to vector B (A == B)

<a id="unreal.Vector2D.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``Vector2D`` Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

<a id="unreal.Vector2D.__add__"></a>

#### __add__

```python
def __add__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Returns addition of Vector A and Vector B (A + B)
- ``double`` Returns Vector A added by B

<a id="unreal.Vector2D.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Returns addition of Vector A and Vector B (A + B)
- ``double`` Returns Vector A added by B

<a id="unreal.Vector2D.__sub__"></a>

#### __sub__

```python
def __sub__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Returns subtraction of Vector B from Vector A (A - B)
- ``double`` Returns Vector A subtracted by B

<a id="unreal.Vector2D.__isub__"></a>

#### __isub__

```python
def __isub__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Returns subtraction of Vector B from Vector A (A - B)
- ``double`` Returns Vector A subtracted by B

<a id="unreal.Vector2D.__mul__"></a>

#### __mul__

```python
def __mul__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y})
- ``double`` Returns Vector A scaled by B

<a id="unreal.Vector2D.__imul__"></a>

#### __imul__

```python
def __imul__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y})
- ``double`` Returns Vector A scaled by B

<a id="unreal.Vector2D.__truediv__"></a>

#### __truediv__

```python
def __truediv__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Element-wise Vector divide (Result = {A.x/B.x, A.y/B.y})
- ``double`` Returns Vector A divided by B

<a id="unreal.Vector2D.__or__"></a>

#### __or__

```python
def __or__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Returns the dot product of two 2d vectors - see http://mathworld.wolfram.com/DotProduct.html

<a id="unreal.Vector2D.__xor__"></a>

#### __xor__

```python
def __xor__(other: Vector2D) -> None
```

**Overloads:**

- ``Vector2D`` Returns the cross product of two 2d vectors - see  http://mathworld.wolfram.com/CrossProduct.html

<a id="unreal.Vector2D.__neg__"></a>

#### __neg__

```python
def __neg__() -> None
```

Gets a negated copy of the vector.

<a id="unreal.Vector2D.ZERO"></a>

#### ZERO

(Vector2D): 2D zero vector constant (0,0)

<a id="unreal.Vector2D.UNIT45_DEG"></a>

#### UNIT45_DEG

(Vector2D): 2D unit vector constant along the 45 degree angle or symmetrical positive axes (sqrt(.5),sqrt(.5)) or (.707,.707). https://en.wikipedia.org/wiki/Unit_vector

<a id="unreal.Vector2D.ONE"></a>

#### ONE

(Vector2D): 2D one vector constant (1,1)

<a id="unreal.Box2f"></a>