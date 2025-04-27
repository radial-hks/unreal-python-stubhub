## RandomStream Objects

```python
class RandomStream(StructBase)
```

Thread-safe random number generator that can be manually seeded.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\RandomStream.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial_seed`` (int32):  [Read-Write] Holds the initial seed.

<a id="unreal.RandomStream.__init__"></a>

#### __init__

```python
def __init__(initial_seed: int = 0) -> None
```

<a id="unreal.RandomStream.initial_seed"></a>

#### initial_seed

```python
@property
def initial_seed() -> int
```

(int32):  [Read-Write] Holds the initial seed.

<a id="unreal.RandomStream.initial_seed"></a>

#### initial_seed

```python
@initial_seed.setter
def initial_seed(value: int) -> None
```

<a id="unreal.RandomStream.set_seed"></a>

#### set_seed

```python
def set_seed(new_seed: int) -> None
```

x.set_seed(new_seed) -> None
Set the seed of a random stream to a specific number

Args:
    new_seed (int32):

<a id="unreal.RandomStream.generate_new_seed"></a>

#### generate_new_seed

```python
def generate_new_seed() -> None
```

x.generate_new_seed() -> None
Create a new random seed for a random stream

<a id="unreal.RandomStream.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Reset a random stream

<a id="unreal.RandomStream.random_unit_vector_in_elliptical_cone_in_radians"></a>

#### random_unit_vector_in_elliptical_cone_in_radians

```python
def random_unit_vector_in_elliptical_cone_in_radians(
        cone_dir: Vector, max_yaw_in_radians: float,
        max_pitch_in_radians: float) -> Vector
```

x.random_unit_vector_in_elliptical_cone_in_radians(cone_dir, max_yaw_in_radians, max_pitch_in_radians) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
The shape of the cone can be modified according to the yaw and pitch angles.

Args:
    cone_dir (Vector): 
    max_yaw_in_radians (float): The yaw angle of the cone (from ConeDir to horizontal edge), in radians.
    max_pitch_in_radians (float): The pitch angle of the cone (from ConeDir to vertical edge), in radians.

Returns:
    Vector:

<a id="unreal.RandomStream.random_unit_vector_in_elliptical_cone_in_degrees"></a>

#### random_unit_vector_in_elliptical_cone_in_degrees

```python
def random_unit_vector_in_elliptical_cone_in_degrees(
        cone_dir: Vector, max_yaw_in_degrees: float,
        max_pitch_in_degrees: float) -> Vector
```

x.random_unit_vector_in_elliptical_cone_in_degrees(cone_dir, max_yaw_in_degrees, max_pitch_in_degrees) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
The shape of the cone can be modified according to the yaw and pitch angles.

Args:
    cone_dir (Vector): 
    max_yaw_in_degrees (float): The yaw angle of the cone (from ConeDir to horizontal edge), in degrees.
    max_pitch_in_degrees (float): The pitch angle of the cone (from ConeDir to vertical edge), in degrees.

Returns:
    Vector:

<a id="unreal.RandomStream.random_unit_vector_in_cone_in_radians"></a>

#### random_unit_vector_in_cone_in_radians

```python
def random_unit_vector_in_cone_in_radians(
        cone_dir: Vector, cone_half_angle_in_radians: float) -> Vector
```

x.random_unit_vector_in_cone_in_radians(cone_dir, cone_half_angle_in_radians) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Args:
    cone_dir (Vector): The base "center" direction of the cone.
    cone_half_angle_in_radians (float): The half-angle of the cone (from ConeDir to edge), in radians.

Returns:
    Vector:

<a id="unreal.RandomStream.random_unit_vector_in_cone_in_degrees"></a>

#### random_unit_vector_in_cone_in_degrees

```python
def random_unit_vector_in_cone_in_degrees(
        cone_dir: Vector, cone_half_angle_in_degrees: float) -> Vector
```

x.random_unit_vector_in_cone_in_degrees(cone_dir, cone_half_angle_in_degrees) -> Vector
Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

Args:
    cone_dir (Vector): The base "center" direction of the cone.
    cone_half_angle_in_degrees (float): The half-angle of the cone (from ConeDir to edge), in degrees.

Returns:
    Vector:

<a id="unreal.RandomStream.random_unit_vector"></a>

#### random_unit_vector

```python
def random_unit_vector() -> Vector
```

x.random_unit_vector() -> Vector
Returns a random vector with length of 1.0

Returns:
    Vector:

<a id="unreal.RandomStream.random_rotator"></a>

#### random_rotator

```python
def random_rotator(roll: bool) -> Rotator
```

x.random_rotator(roll) -> Rotator
Create a random rotation

Args:
    roll (bool): 

Returns:
    Rotator:

<a id="unreal.RandomStream.random_point_in_box"></a>

#### random_point_in_box

```python
def random_point_in_box(box: Box) -> Vector
```

x.random_point_in_box(box) -> Vector
Returns a random point within the specified bounding box.

Args:
    box (Box): 

Returns:
    Vector:

<a id="unreal.RandomStream.random_point_in_bounded_box"></a>

#### random_point_in_bounded_box

```python
def random_point_in_bounded_box(center: Vector, half_size: Vector) -> Vector
```

x.random_point_in_bounded_box(center, half_size) -> Vector
Returns a random point within the specified bounding box using the first vector as an origin and the second as the half size of the AABB.

Args:
    center (Vector): 
    half_size (Vector): 

Returns:
    Vector:

<a id="unreal.RandomStream.random_int_in_range"></a>

#### random_int_in_range

```python
def random_int_in_range(min: int, max: int) -> int
```

x.random_int_in_range(min, max) -> int32
Return a random integer between Min and Max (>= Min and <= Max)

Args:
    min (int32): 
    max (int32): 

Returns:
    int32:

<a id="unreal.RandomStream.random_int"></a>

#### random_int

```python
def random_int(max: int) -> int
```

x.random_int(max) -> int32
Returns a uniformly distributed random number between 0 and Max - 1

Args:
    max (int32): 

Returns:
    int32:

<a id="unreal.RandomStream.random_float_in_range"></a>

#### random_float_in_range

```python
def random_float_in_range(min: float, max: float) -> float
```

x.random_float_in_range(min, max) -> float
Generate a random number between Min and Max

Args:
    min (float): 
    max (float): 

Returns:
    float:

<a id="unreal.RandomStream.random_float"></a>

#### random_float

```python
def random_float() -> float
```

x.random_float() -> float
Returns a random float between 0 and 1

Returns:
    float:

<a id="unreal.RandomStream.random_bool_with_weight"></a>

#### random_bool_with_weight

```python
def random_bool_with_weight(weight: float = 0.500000) -> bool
```

x.random_bool_with_weight(weight=0.500000) -> bool
Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
              Weight = .6 return value = True 60% of the time

Args:
    weight (float): 

Returns:
    bool:

<a id="unreal.RandomStream.random_bool"></a>

#### random_bool

```python
def random_bool() -> bool
```

x.random_bool() -> bool
Returns a random bool

Returns:
    bool:

<a id="unreal.Ray"></a>