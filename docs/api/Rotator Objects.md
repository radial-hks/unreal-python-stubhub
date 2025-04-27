## Rotator Objects

```python
class Rotator(StructBase)
```

An orthogonal rotation in 3d space.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Rotator.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pitch`` (double):  [Read-Write] Pitch (degrees) around Y axis
- ``roll`` (double):  [Read-Write] Roll (degrees) around X axis
- ``yaw`` (double):  [Read-Write] Yaw (degrees) around Z axis

<a id="unreal.Rotator.__init__"></a>

#### __init__

```python
def __init__(roll: float = 0.000000,
             pitch: float = 0.000000,
             yaw: float = 0.000000) -> None
```

<a id="unreal.Rotator.pitch"></a>

#### pitch

```python
@property
def pitch() -> float
```

(double):  [Read-Write] Pitch (degrees) around Y axis

<a id="unreal.Rotator.pitch"></a>

#### pitch

```python
@pitch.setter
def pitch(value: float) -> None
```

<a id="unreal.Rotator.yaw"></a>

#### yaw

```python
@property
def yaw() -> float
```

(double):  [Read-Write] Yaw (degrees) around Z axis

<a id="unreal.Rotator.yaw"></a>

#### yaw

```python
@yaw.setter
def yaw(value: float) -> None
```

<a id="unreal.Rotator.roll"></a>

#### roll

```python
@property
def roll() -> float
```

(double):  [Read-Write] Roll (degrees) around X axis

<a id="unreal.Rotator.roll"></a>

#### roll

```python
@roll.setter
def roll(value: float) -> None
```

<a id="unreal.Rotator.lerp"></a>

#### lerp

```python
def lerp(b: Rotator, alpha: float, shortest_path: bool) -> Rotator
```

x.lerp(b, alpha, shortest_path) -> Rotator
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

Args:
    b (Rotator): 
    alpha (float): 
    shortest_path (bool): 

Returns:
    Rotator:

<a id="unreal.Rotator.is_not_near_equal"></a>

#### is_not_near_equal

```python
def is_not_near_equal(b: Rotator, error_tolerance: float = 0.000100) -> bool
```

x.is_not_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if rotator A is not equal to rotator B (A != B) within a specified error tolerance

Args:
    b (Rotator): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Rotator.delta"></a>

#### delta

```python
def delta(b: Rotator) -> Rotator
```

x.delta(b) -> Rotator
Normalized A-B

Args:
    b (Rotator): 

Returns:
    Rotator:

<a id="unreal.Rotator.inversed"></a>

#### inversed

```python
def inversed() -> Rotator
```

x.inversed() -> Rotator
Negate a rotator

Returns:
    Rotator:

<a id="unreal.Rotator.scale_integer"></a>

#### scale_integer

```python
def scale_integer(b: int) -> Rotator
```

x.scale_integer(b) -> Rotator
Returns rotator representing rotator A scaled by B

Args:
    b (int32): 

Returns:
    Rotator:

<a id="unreal.Rotator.scale"></a>

#### scale

```python
def scale(b: float) -> Rotator
```

x.scale(b) -> Rotator
Returns rotator representing rotator A scaled by B

Args:
    b (float): 

Returns:
    Rotator:

<a id="unreal.Rotator.get_up_vector"></a>

#### get_up_vector

```python
def get_up_vector() -> Vector
```

x.get_up_vector() -> Vector
Rotate the world up vector by the given rotation

Returns:
    Vector:

<a id="unreal.Rotator.get_right_vector"></a>

#### get_right_vector

```python
def get_right_vector() -> Vector
```

x.get_right_vector() -> Vector
Rotate the world right vector by the given rotation

Returns:
    Vector:

<a id="unreal.Rotator.get_forward_vector"></a>

#### get_forward_vector

```python
def get_forward_vector() -> Vector
```

x.get_forward_vector() -> Vector
Rotate the world forward vector by the given rotation

Returns:
    Vector:

<a id="unreal.Rotator.get_axes"></a>

#### get_axes

```python
def get_axes() -> Tuple[Vector, Vector, Vector]
```

x.get_axes() -> (x=Vector, y=Vector, z=Vector)
Get the reference frame direction vectors (axes) described by this rotation

Returns:
    tuple: 

    x (Vector): 

    y (Vector): 

    z (Vector):

<a id="unreal.Rotator.is_near_equal"></a>

#### is_near_equal

```python
def is_near_equal(b: Rotator, error_tolerance: float = 0.000100) -> bool
```

x.is_near_equal(b, error_tolerance=0.000100) -> bool
Returns true if rotator A is equal to rotator B (A == B) within a specified error tolerance

Args:
    b (Rotator): 
    error_tolerance (float): 

Returns:
    bool:

<a id="unreal.Rotator.to_vector"></a>

#### to_vector

```python
def to_vector() -> Vector
```

x.to_vector() -> Vector
Get the X direction vector after this rotation

Returns:
    Vector:

<a id="unreal.Rotator.transform"></a>

#### transform

```python
def transform() -> Transform
```

x.transform() -> Transform
Converts Rotator to Transform

Returns:
    Transform:

<a id="unreal.Rotator.quaternion"></a>

#### quaternion

```python
def quaternion() -> Quat
```

x.quaternion() -> Quat
Converts to Quaternion representation of this Rotator.

Returns:
    Quat:

<a id="unreal.Rotator.combine"></a>

#### combine

```python
def combine(b: Rotator) -> Rotator
```

x.combine(b) -> Rotator
Combine 2 rotations to give you the resulting rotation of first applying A, then B.

Args:
    b (Rotator): 

Returns:
    Rotator:

<a id="unreal.Rotator.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Rotator`` Returns true if rotator A is equal to rotator B (A == B) within a specified error tolerance

<a id="unreal.Rotator.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``Rotator`` Returns true if rotator A is not equal to rotator B (A != B) within a specified error tolerance

<a id="unreal.Rotator.__neg__"></a>

#### __neg__

```python
def __neg__() -> None
```

Negate a rotator

<a id="unreal.Rotator3f"></a>