## Transform Objects

```python
class Transform(StructBase)
```

Transform composed of Quat/Translation/Scale.
note: This is implemented in either TransformVectorized.h or TransformNonVectorized.h depending on the platform.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rotation`` (Quat):  [Read-Write] Rotation of this transformation, as a quaternion.
- ``scale3d`` (Vector):  [Read-Write] 3D scale (always applied in local space) as a vector.
- ``translation`` (Vector):  [Read-Write] Translation of this transformation, as a vector.

<a id="unreal.Transform.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [1.000000, 1.000000, 1.000000]) -> None
```

<a id="unreal.Transform.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

(Quat):  [Read-Write] Rotation of this transformation, as a quaternion.

<a id="unreal.Transform.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.Transform.translation"></a>

#### translation

```python
@property
def translation() -> Vector
```

(Vector):  [Read-Write] Translation of this transformation, as a vector.

<a id="unreal.Transform.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector) -> None
```

<a id="unreal.Transform.scale3d"></a>

#### scale3d

```python
@property
def scale3d() -> Vector
```

(Vector):  [Read-Write] 3D scale (always applied in local space) as a vector.

<a id="unreal.Transform.scale3d"></a>

#### scale3d

```python
@scale3d.setter
def scale3d(value: Vector) -> None
```

<a id="unreal.Transform.transform_rotation"></a>

#### transform_rotation

```python
def transform_rotation(rotation: Rotator) -> Rotator
```

x.transform_rotation(rotation) -> Rotator
Transform a rotator by the supplied transform.
For example, if T was an object's transform, this would transform a rotation from local space to world space.

Args:
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.Transform.transform_location"></a>

#### transform_location

```python
def transform_location(location: Vector) -> Vector
```

x.transform_location(location) -> Vector
Transform a position by the supplied transform.
For example, if T was an object's transform, this would transform a position from local space to world space.

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.Transform.transform_direction"></a>

#### transform_direction

```python
def transform_direction(direction: Vector) -> Vector
```

x.transform_direction(direction) -> Vector
Transform a direction vector by the supplied transform - will not change its length.
For example, if T was an object's transform, this would transform a direction from local space to world space.

Args:
    direction (Vector): 

Returns:
    Vector:

<a id="unreal.Transform.determinant"></a>

#### determinant

```python
def determinant() -> float
```

x.determinant() -> float
Calculates the determinant of the transform (converts to FMatrix internally)

Returns:
    float:

<a id="unreal.Transform.lerp"></a>

#### lerp

```python
def lerp(
    b: Transform,
    alpha: float,
    interp_mode: LerpInterpolationMode = LerpInterpolationMode.QUAT_INTERP
) -> Transform
```

x.lerp(b, alpha, interp_mode=LerpInterpolationMode.QUAT_INTERP) -> Transform
Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1).

Args:
    b (Transform): 
    alpha (float): 
    interp_mode (LerpInterpolationMode): 

Returns:
    Transform:

<a id="unreal.Transform.interp_to"></a>

#### interp_to

```python
def interp_to(target: Transform, delta_time: float,
              interp_speed: float) -> Transform
```

x.interp_to(target, delta_time, interp_speed) -> Transform
Tries to reach Target transform based on distance from Current position, giving a nice smooth feeling when tracking a position.

Args:
    target (Transform): Target transform
    delta_time (float): Time since last tick
    interp_speed (float): Interpolation speed, if the speed given is 0, then jump to the target.

Returns:
    Transform: New interpolated transform

<a id="unreal.Transform.is_near_equal"></a>

#### is_near_equal

```python
def is_near_equal(b: Transform,
                  location_tolerance: float = 0.000100,
                  rotation_tolerance: float = 0.000100,
                  scale3d_tolerance: float = 0.000100) -> bool
```

x.is_near_equal(b, location_tolerance=0.000100, rotation_tolerance=0.000100, scale3d_tolerance=0.000100) -> bool
Returns true if transform A is nearly equal to B

Args:
    b (Transform): 
    location_tolerance (float): How close position of transforms need to be to be considered equal
    rotation_tolerance (float): How close rotations of transforms need to be to be considered equal
    scale3d_tolerance (float): How close scale of transforms need to be to be considered equal

Returns:
    bool:

<a id="unreal.Transform.make_relative"></a>

#### make_relative

```python
def make_relative(relative_to: Transform) -> Transform
```

x.make_relative(relative_to) -> Transform
Computes a relative transform of one transform compared to another.

Example: ChildOffset = MakeRelativeTransform(Child.GetActorTransform(), Parent.GetActorTransform())
This computes the relative transform of the Child from the Parent.

Args:
    relative_to (Transform): The transform the result is relative to (in the same space as A)

Returns:
    Transform: The new relative transform

<a id="unreal.Transform.inverse"></a>

#### inverse

```python
def inverse() -> Transform
```

x.inverse() -> Transform
Returns the inverse of the given transform T.

Example: Given a LocalToWorld transform, WorldToLocal will be returned.

Returns:
    Transform: The inverse of T.

<a id="unreal.Transform.inverse_transform_rotation"></a>

#### inverse_transform_rotation

```python
def inverse_transform_rotation(rotation: Rotator) -> Rotator
```

x.inverse_transform_rotation(rotation) -> Rotator
Transform a rotator by the inverse of the supplied transform.
For example, if T was an object's transform, this would transform a rotation from world space to local space.

Args:
    rotation (Rotator): 

Returns:
    Rotator:

<a id="unreal.Transform.inverse_transform_location"></a>

#### inverse_transform_location

```python
def inverse_transform_location(location: Vector) -> Vector
```

x.inverse_transform_location(location) -> Vector
Transform a position by the inverse of the supplied transform.
For example, if T was an object's transform, this would transform a position from world space to local space.

Args:
    location (Vector): 

Returns:
    Vector:

<a id="unreal.Transform.inverse_transform_direction"></a>

#### inverse_transform_direction

```python
def inverse_transform_direction(direction: Vector) -> Vector
```

x.inverse_transform_direction(direction) -> Vector
Transform a direction vector by the inverse of the supplied transform - will not change its length.
For example, if T was an object's transform, this would transform a direction from world space to local space.

Args:
    direction (Vector): 

Returns:
    Vector:

<a id="unreal.Transform.equals"></a>

#### equals

```python
def equals(b: Transform) -> bool
```

x.equals(b) -> bool
Returns true if transform A is equal to transform B

Args:
    b (Transform): 

Returns:
    bool:

<a id="unreal.Transform.to_matrix"></a>

#### to_matrix

```python
def to_matrix() -> Matrix
```

x.to_matrix() -> Matrix
Converts a Transform to a Matrix with scale

Returns:
    Matrix:

<a id="unreal.Transform.multiply"></a>

#### multiply

```python
def multiply(b: Transform) -> Transform
```

x.multiply(b) -> Transform
Compose two transforms in order: A * B.

Order matters when composing transforms:
A * B will yield a transform that logically first applies A then B to any subsequent transformation.

Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

Args:
    b (Transform): 

Returns:
    Transform: New transform: A * B

<a id="unreal.Transform.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``Transform`` Returns true if transform A is equal to transform B

<a id="unreal.Transform.__mul__"></a>

#### __mul__

```python
def __mul__(other: Transform) -> None
```

**Overloads:**

- ``Transform`` Compose two transforms in order: A * B.

  Order matters when composing transforms:
  A * B will yield a transform that logically first applies A then B to any subsequent transformation.

  Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
  Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

  @return New transform: A * B

<a id="unreal.Transform.__imul__"></a>

#### __imul__

```python
def __imul__(other: Transform) -> None
```

**Overloads:**

- ``Transform`` Compose two transforms in order: A * B.

  Order matters when composing transforms:
  A * B will yield a transform that logically first applies A then B to any subsequent transformation.

  Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
  Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

  @return New transform: A * B

<a id="unreal.Transform3f"></a>