## Vector4 Objects

```python
class Vector4(StructBase)
```

A 4-D homogeneous vector.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Vector4.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``w`` (double):  [Read-Write]
- ``x`` (double):  [Read-Write]
- ``y`` (double):  [Read-Write]
- ``z`` (double):  [Read-Write]

<a id="unreal.Vector4.__init__"></a>

#### __init__

```python
def __init__(x: float = 0.000000,
             y: float = 0.000000,
             z: float = 0.000000,
             w: float = 0.000000) -> None
```

<a id="unreal.Vector4.x"></a>

#### x

```python
@property
def x() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector4.x"></a>

#### x

```python
@x.setter
def x(value: float) -> None
```

<a id="unreal.Vector4.y"></a>

#### y

```python
@property
def y() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector4.y"></a>

#### y

```python
@y.setter
def y(value: float) -> None
```

<a id="unreal.Vector4.z"></a>

#### z

```python
@property
def z() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector4.z"></a>

#### z

```python
@z.setter
def z(value: float) -> None
```

<a id="unreal.Vector4.w"></a>

#### w

```python
@property
def w() -> float
```

(double):  [Read-Write]

<a id="unreal.Vector4.w"></a>

#### w

```python
@w.setter
def w(value: float) -> None
```

<a id="unreal.Vector4.length_squared3"></a>

#### length_squared3

```python
def length_squared3() -> float
```

x.length_squared3() -> double
Returns the squared length of the vector. The W element is ignored.

Returns:
    double:

<a id="unreal.Vector4.length_squared"></a>

#### length_squared

```python
def length_squared() -> float
```

x.length_squared() -> double
Returns the squared length of the vector.

Returns:
    double:

<a id="unreal.Vector4.length3"></a>

#### length3

```python
def length3() -> float
```

x.length3() -> double
Returns the length of the vector. The W element is ignored.

Returns:
    double:

<a id="unreal.Vector4.length"></a>

#### length

```python
def length() -> float
```

x.length() -> double
Returns the length of the vector.

Returns:
    double:

<a id="unreal.Vector4.set"></a>

#### set

```python
def set(x: float, y: float, z: float, w: float) -> None
```

x.set(x, y, z, w) -> None
Set the values of the vector directly.

Args:
    x (double): 
    y (double): 
    z (double): 
    w (double):

<a id="unreal.Vector4.normal_unsafe3"></a>

#### normal_unsafe3

```python
def normal_unsafe3() -> Vector4
```

x.normal_unsafe3() -> Vector4
Calculates normalized unit version of vector without checking for zero length. The W element is ignored and the returned vector has W=0.

Returns:
    Vector4: Normalized version of vector.

<a id="unreal.Vector4.normalize3"></a>

#### normalize3

```python
def normalize3(tolerance: float = 0.000000) -> None
```

x.normalize3(tolerance=0.000000) -> None
Normalize this vector in-place if it is large enough or set it to (0,0,0,0) otherwise. The W element is ignored and the returned vector has W=0.

Args:
    tolerance (float): Minimum squared length of vector for normalization.

<a id="unreal.Vector4.normal3"></a>

#### normal3

```python
def normal3(tolerance: float = 0.000100) -> Vector4
```

x.normal3(tolerance=0.000100) -> Vector4
Gets a normalized unit copy of the vector, ensuring it is safe to do so based on the length. The W element is ignored and the returned vector has W=0.
Returns zero vector if vector length is too small to safely normalize.

Args:
    tolerance (float): Minimum squared vector length.

Returns:
    Vector4: A normalized copy if safe, (0,0,0) otherwise.

<a id="unreal.Vector4.negated"></a>

#### negated

```python
def negated() -> Vector4
```

x.negated() -> Vector4
Gets a negated copy of the vector. Equivalent to -Vector for scripts.

Returns:
    Vector4:

<a id="unreal.Vector4.mirror_by_vector3"></a>

#### mirror_by_vector3

```python
def mirror_by_vector3(surface_normal: Vector4) -> Vector4
```

x.mirror_by_vector3(surface_normal) -> Vector4
Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
Produces a result like shining a laser at a mirror!
The W element is ignored.

Args:
    surface_normal (Vector4): A normal of the surface the ray should be reflected on.

Returns:
    Vector4: Reflected vector.

<a id="unreal.Vector4.is_zero"></a>

#### is_zero

```python
def is_zero() -> bool
```

x.is_zero() -> bool
Checks whether all components of the vector are exactly zero.

Returns:
    bool: true if vector is exactly zero, otherwise false.

<a id="unreal.Vector4.is_unit3"></a>

#### is_unit3

```python
def is_unit3(squared_lenth_tolerance: float = 0.000100) -> bool
```

x.is_unit3(squared_lenth_tolerance=0.000100) -> bool
Determines if vector is normalized / unit (length 1) within specified squared tolerance. The W element is ignored.

Args:
    squared_lenth_tolerance (float): 

Returns:
    bool: true if unit, false otherwise.

<a id="unreal.Vector4.is_normal3"></a>

#### is_normal3

```python
def is_normal3() -> bool
```

x.is_normal3() -> bool
Determines if vector is normalized / unit (length 1). The W element is ignored.

Returns:
    bool: true if normalized, false otherwise.

<a id="unreal.Vector4.is_nearly_zero3"></a>

#### is_nearly_zero3

```python
def is_nearly_zero3(tolerance: float = 0.000100) -> bool
```

x.is_nearly_zero3(tolerance=0.000100) -> bool
Checks whether vector is near to zero within a specified tolerance. The W element is ignored.

Args:
    tolerance (float): Error tolerance.

Returns:
    bool: true if vector is in tolerance to zero, otherwise false.

<a id="unreal.Vector4.is_nan"></a>

#### is_nan

```python
def is_nan() -> bool
```

x.is_nan() -> bool
Determines if any component is not a number (NAN)

Returns:
    bool: true if one or more components is NAN, otherwise false.

<a id="unreal.Vector4.dot3"></a>

#### dot3

```python
def dot3(b: Vector4) -> float
```

x.dot3(b) -> double
Returns the dot product of two vectors - see http://mathworld.wolfram.com/DotProduct.html The W element is ignored.

Args:
    b (Vector4): 

Returns:
    double:

<a id="unreal.Vector4.dot"></a>

#### dot

```python
def dot(b: Vector4) -> float
```

x.dot(b) -> double
Returns the dot product of two vectors - see http://mathworld.wolfram.com/DotProduct.html

Args:
    b (Vector4): 

Returns:
    double:

<a id="unreal.Vector4.cross3"></a>

#### cross3

```python
def cross3(b: Vector4) -> Vector4
```

x.cross3(b) -> Vector4
Returns the cross product of two vectors - see  http://mathworld.wolfram.com/CrossProduct.html

Args:
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.Vector4.assign"></a>

#### assign

```python
def assign(vector: Vector4) -> None
```

x.assign(vector) -> None
Assign the values of the supplied vector.

Args:
    vector (Vector4): Vector to copy values from.

<a id="unreal.Vector4.subtract"></a>

#### subtract

```python
def subtract(b: Vector4) -> Vector4
```

x.subtract(b) -> Vector4
Returns subtraction of Vector B from Vector A (A - B)

Args:
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.Vector4.not_equal"></a>

#### not_equal

```python
def not_equal(b: Vector4) -> bool
```

x.not_equal(b) -> bool
Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Args:
    b (Vector4): 

Returns:
    bool:

<a id="unreal.Vector4.is_not_near_equal"></a>

#### is_not_near_equal

```python
def is_not_near_equal(b: Vector4, error_tolerance: float = 0.000100) -> bool
```

x.is_not_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

Args:
    b (Vector4): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Vector4.multiply"></a>

#### multiply

```python
def multiply(b: Vector4) -> Vector4
```

x.multiply(b) -> Vector4
Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z, A.w*B.w})

Args:
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.Vector4.equals"></a>

#### equals

```python
def equals(b: Vector4) -> bool
```

x.equals(b) -> bool
Returns true if vector A is equal to vector B (A == B)

Args:
    b (Vector4): 

Returns:
    bool:

<a id="unreal.Vector4.is_near_equal"></a>

#### is_near_equal

```python
def is_near_equal(b: Vector4, error_tolerance: float = 0.000100) -> bool
```

x.is_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

Args:
    b (Vector4): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Vector4.divide"></a>

#### divide

```python
def divide(b: Vector4) -> Vector4
```

x.divide(b) -> Vector4
Element-wise Vector divide (Result = {A.x/B.x, A.y/B.y, A.z/B.z, A.w/B.w})

Args:
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.Vector4.vector"></a>

#### vector

```python
def vector() -> Vector
```

x.vector() -> Vector
Converts a Vector4 to a Vector (dropping the W element)

Returns:
    Vector:

<a id="unreal.Vector4.rotator"></a>

#### rotator

```python
def rotator() -> Rotator
```

x.rotator() -> Rotator
Return the FRotator orientation corresponding to the direction in which the vector points.
Sets Yaw and Pitch to the proper numbers, and sets Roll to zero because the roll can't be determined from a vector.

Returns:
    Rotator: FRotator from the Vector's direction, without any roll.

<a id="unreal.Vector4.quaternion"></a>

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

<a id="unreal.Vector4.add"></a>

#### add

```python
def add(b: Vector4) -> Vector4
```

x.add(b) -> Vector4
Returns addition of Vector A and Vector B (A + B)

Args:
    b (Vector4): 

Returns:
    Vector4:

<a id="unreal.Vector4.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Vector4`` Returns true if vector A is equal to vector B (A == B)

<a id="unreal.Vector4.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``Vector4`` Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

<a id="unreal.Vector4.__add__"></a>

#### __add__

```python
def __add__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Returns addition of Vector A and Vector B (A + B)

<a id="unreal.Vector4.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Returns addition of Vector A and Vector B (A + B)

<a id="unreal.Vector4.__sub__"></a>

#### __sub__

```python
def __sub__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Returns subtraction of Vector B from Vector A (A - B)

<a id="unreal.Vector4.__isub__"></a>

#### __isub__

```python
def __isub__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Returns subtraction of Vector B from Vector A (A - B)

<a id="unreal.Vector4.__mul__"></a>

#### __mul__

```python
def __mul__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z, A.w*B.w})

<a id="unreal.Vector4.__imul__"></a>

#### __imul__

```python
def __imul__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Element-wise Vector multiplication (Result = {A.x*B.x, A.y*B.y, A.z*B.z, A.w*B.w})

<a id="unreal.Vector4.__truediv__"></a>

#### __truediv__

```python
def __truediv__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Element-wise Vector divide (Result = {A.x/B.x, A.y/B.y, A.z/B.z, A.w/B.w})

<a id="unreal.Vector4.__or__"></a>

#### __or__

```python
def __or__(other: Vector4) -> None
```

**Overloads:**

- ``Vector4`` Returns the dot product of two vectors - see http://mathworld.wolfram.com/DotProduct.html

<a id="unreal.Vector4.__neg__"></a>

#### __neg__

```python
def __neg__() -> None
```

Gets a negated copy of the vector. Equivalent to -Vector for scripts.

<a id="unreal.Vector4.ZERO"></a>

#### ZERO

(Vector4): 4D vector zero constant (0,0,0)

<a id="unreal.Vector4f"></a>