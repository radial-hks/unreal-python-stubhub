## AnimGraphLibrary Objects

```python
class AnimGraphLibrary(BlueprintFunctionLibrary)
```

A library of the most common animation blueprint functions.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: KismetAnimationLibrary.h

<a id="unreal.AnimGraphLibrary.two_bone_ik"></a>

#### two_bone_ik

```python
@classmethod
def two_bone_ik(cls,
                root_pos: Vector,
                joint_pos: Vector,
                end_pos: Vector,
                joint_target: Vector,
                effector: Vector,
                allow_stretching: bool = False,
                start_stretch_ratio: float = 1.000000,
                max_stretch_scale: float = 1.200000) -> Tuple[Vector, Vector]
```

X.two_bone_ik(root_pos, joint_pos, end_pos, joint_target, effector, allow_stretching=False, start_stretch_ratio=1.000000, max_stretch_scale=1.200000) -> (out_joint_pos=Vector, out_end_pos=Vector)
Computes the transform for two bones using inverse kinematics.

Args:
    root_pos (Vector): The input root position of the two bone chain
    joint_pos (Vector): The input center (elbow) position of the two bone chain
    end_pos (Vector): The input end (wrist) position of the two bone chain
    joint_target (Vector): The IK target for the write to reach
    effector (Vector): The position of the target effector for the IK Chain.
    allow_stretching (bool): If set to true the bones are allowed to stretch
    start_stretch_ratio (float): The ratio at which the bones should start to stretch. The higher the value, the later the stretching wil start.
    max_stretch_scale (float): The maximum multiplier for the stretch to reach.

Returns:
    tuple: 

    out_joint_pos (Vector): The resulting position for the center (elbow)

    out_end_pos (Vector): The resulting position for the end (wrist)

<a id="unreal.AnimGraphLibrary.k2_start_profiling_timer"></a>

#### k2_start_profiling_timer

```python
@classmethod
def k2_start_profiling_timer(cls) -> None
```

X.k2_start_profiling_timer() -> None
This function starts measuring the time for a profiling bracket

<a id="unreal.AnimGraphLibrary.make_vector_from_perlin_noise"></a>

#### make_vector_from_perlin_noise

```python
@classmethod
def make_vector_from_perlin_noise(cls,
                                  x: float,
                                  y: float,
                                  z: float,
                                  range_out_min_x: float = -1.000000,
                                  range_out_max_x: float = 1.000000,
                                  range_out_min_y: float = -1.000000,
                                  range_out_max_y: float = 1.000000,
                                  range_out_min_z: float = -1.000000,
                                  range_out_max_z: float = 1.000000) -> Vector
```

X.make_vector_from_perlin_noise(x, y, z, range_out_min_x=-1.000000, range_out_max_x=1.000000, range_out_min_y=-1.000000, range_out_max_y=1.000000, range_out_min_z=-1.000000, range_out_max_z=1.000000) -> Vector
This function creates perlin noise from input X, Y, Z, and then range map to RangeOut, and out put to OutX, OutY, OutZ

Args:
    x (float): The x component for the input position of the noise
    y (float): The y component for the input position of the noise
    z (float): The z component for the input position of the noise
    range_out_min_x (float): The minimum for the output range for the x component
    range_out_max_x (float): The maximum for the output range for the x component
    range_out_min_y (float): The minimum for the output range for the y component
    range_out_max_y (float): The maximum for the output range for the y component
    range_out_min_z (float): The minimum for the output range for the z component
    range_out_max_z (float): The maximum for the output range for the z component

Returns:
    Vector:

<a id="unreal.AnimGraphLibrary.make_float_from_perlin_noise"></a>

#### make_float_from_perlin_noise

```python
@classmethod
def make_float_from_perlin_noise(cls, value: float, range_out_min: float,
                                 range_out_max: float) -> float
```

X.make_float_from_perlin_noise(value, range_out_min, range_out_max) -> float
This function creates perlin noise for a single float and then range map to RangeOut

Args:
    value (float): The input value for the noise function
    range_out_min (float): The minimum for the output range
    range_out_max (float): The maximum for the output range

Returns:
    float:

<a id="unreal.AnimGraphLibrary.look_at"></a>

#### look_at

```python
@classmethod
def look_at(cls,
            current_transform: Transform,
            target_position: Vector,
            look_at_vector: Vector,
            use_up_vector: bool = False,
            up_vector: Vector = ...,
            clamp_cone_in_degree: float = ...) -> Transform
```

X.look_at(current_transform, target_position, look_at_vector, use_up_vector=False, up_vector, clamp_cone_in_degree) -> Transform
Computes the transform which is "looking" at target position with a local axis.

Args:
    current_transform (Transform): The input transform to modify
    target_position (Vector): The position this transform should look at
    look_at_vector (Vector): The local vector to align with the target
    use_up_vector (bool): If set to true the lookat will also perform a twist rotation
    up_vector (Vector): The position to use for the upvector target (only used is bUseUpVector is turned on)
    clamp_cone_in_degree (float): A limit for only allowing the lookat to rotate as much as defined by the float value

Returns:
    Transform:

<a id="unreal.AnimGraphLibrary.k2_end_profiling_timer"></a>

#### k2_end_profiling_timer

```python
@classmethod
def k2_end_profiling_timer(cls,
                           log: bool = True,
                           log_prefix: str = "") -> float
```

X.k2_end_profiling_timer(log=True, log_prefix="") -> float
This function ends measuring a profiling bracket and optionally logs the result
result: The time spent in milliseconds

Args:
    log (bool): If set to true the result is logged to the OutputLog
    log_prefix (str): A prefix to use for the log

Returns:
    float:

<a id="unreal.AnimGraphLibrary.distance_between_sockets"></a>

#### distance_between_sockets

```python
@classmethod
def distance_between_sockets(cls,
                             component: SkeletalMeshComponent,
                             socket_or_bone_name_a: Name,
                             socket_space_a: RelativeTransformSpace,
                             socket_or_bone_name_b: Name,
                             socket_space_b: RelativeTransformSpace,
                             remap_range: bool = False,
                             range_min: float = ...,
                             range_max: float = ...,
                             out_range_min: float = ...,
                             out_range_max: float = ...) -> float
```

X.distance_between_sockets(component, socket_or_bone_name_a, socket_space_a, socket_or_bone_name_b, socket_space_b, remap_range=False, range_min, range_max, out_range_min, out_range_max) -> float
Computes the distance between two bones / sockets and can remap the range.

Args:
    component (SkeletalMeshComponent): The skeletal component to look for the sockets / bones within
    socket_or_bone_name_a (Name): The name of the first socket / bone
    socket_space_a (RelativeTransformSpace): The space for the first socket / bone
    socket_or_bone_name_b (Name): The name of the second socket / bone
    socket_space_b (RelativeTransformSpace): The space for the second socket / bone
    remap_range (bool): If set to true, the distance will be remapped using the range parameters
    range_min (float): The minimum for the input range (commonly == 0.0)
    range_max (float): The maximum for the input range (the max expected distance)
    out_range_min (float): The minimum for the output range (commonly == 0.0)
    out_range_max (float): The maximum for the output range (commonly == 1.0)

Returns:
    float:

<a id="unreal.AnimGraphLibrary.direction_between_sockets"></a>

#### direction_between_sockets

```python
@classmethod
def direction_between_sockets(cls, component: SkeletalMeshComponent,
                              socket_or_bone_name_from: Name,
                              socket_or_bone_name_to: Name) -> Vector
```

X.direction_between_sockets(component, socket_or_bone_name_from, socket_or_bone_name_to) -> Vector
Computes the direction between two bones / sockets.

Args:
    component (SkeletalMeshComponent): The skeletal component to look for the sockets / bones within
    socket_or_bone_name_from (Name): The name of the first socket / bone
    socket_or_bone_name_to (Name): The name of the second socket / bone

Returns:
    Vector:

<a id="unreal.AnimGraphLibrary.calculate_velocity_from_sockets"></a>

#### calculate_velocity_from_sockets

```python
@classmethod
def calculate_velocity_from_sockets(
        cls,
        delta_seconds: float,
        component: SkeletalMeshComponent,
        socket_or_bone_name: Name,
        reference_socket_or_bone: Name,
        socket_space: RelativeTransformSpace,
        offset_in_bone_space: Vector,
        history: PositionHistory,
        number_of_samples: int = 16,
        velocity_min: float = 0.000000,
        velocity_max: float = 128.000000,
        easing_type: EasingFuncType = ...,
        custom_curve: RuntimeFloatCurve = ...
) -> Tuple[float, PositionHistory]
```

X.calculate_velocity_from_sockets(delta_seconds, component, socket_or_bone_name, reference_socket_or_bone, socket_space, offset_in_bone_space, history, number_of_samples=16, velocity_min=0.000000, velocity_max=128.000000, easing_type, custom_curve) -> (float, history=PositionHistory)
This function calculates the velocity of an offset position on a bone / socket over time.
The bone's / socket's motion can be expressed within a reference frame (another bone / socket).
You need to hook up a valid PositionHistory variable to this for storage.

Args:
    delta_seconds (float): The time passed in seconds
    component (SkeletalMeshComponent): The skeletal component to look for the bones / sockets
    socket_or_bone_name (Name): The name of the bone / socket to track.
    reference_socket_or_bone (Name): The name of the bone / socket to use as a frame of reference (or None if no frame of reference == world space).
    socket_space (RelativeTransformSpace): The space to use for the two sockets / bones
    offset_in_bone_space (Vector): The relative position in the space of the bone / socket to track over time.
    history (PositionHistory): The history to use for storage.
    number_of_samples (int32): The number of samples to use for the history. The higher the number of samples - the smoother the velocity changes.
    velocity_min (float): The minimum velocity to use for normalization (if both min and max are set to 0, normalization is turned off)
    velocity_max (float): The maximum velocity to use for normalization (if both min and max are set to 0, normalization is turned off)
    easing_type (EasingFuncType): The easing function to use
    custom_curve (RuntimeFloatCurve): The curve to use if the easing type is "Custom"

Returns:
    PositionHistory: 

    history (PositionHistory): The history to use for storage.

<a id="unreal.AnimGraphLibrary.calculate_velocity_from_position_history"></a>

#### calculate_velocity_from_position_history

```python
@classmethod
def calculate_velocity_from_position_history(
        cls,
        delta_seconds: float,
        position: Vector,
        history: PositionHistory,
        number_of_samples: int = 16,
        velocity_min: float = 0.000000,
        velocity_max: float = 128.000000) -> Tuple[float, PositionHistory]
```

X.calculate_velocity_from_position_history(delta_seconds, position, history, number_of_samples=16, velocity_min=0.000000, velocity_max=128.000000) -> (float, history=PositionHistory)
This function calculates the velocity of a position changing over time.
You need to hook up a valid PositionHistory variable to this for storage.

Args:
    delta_seconds (float): The time passed in seconds
    position (Vector): The position to track over time.
    history (PositionHistory): The history to use for storage.
    number_of_samples (int32): The number of samples to use for the history. The higher the number of samples - the smoother the velocity changes.
    velocity_min (float): The minimum velocity to use for normalization (if both min and max are set to 0, normalization is turned off)
    velocity_max (float): The maximum velocity to use for normalization (if both min and max are set to 0, normalization is turned off)

Returns:
    PositionHistory: 

    history (PositionHistory): The history to use for storage.

<a id="unreal.AnimGraphLibrary.calculate_direction"></a>

#### calculate_direction

```python
@classmethod
def calculate_direction(cls, velocity: Vector,
                        base_rotation: Rotator) -> float
```

X.calculate_direction(velocity, base_rotation) -> float
Returns degree of the angle between Velocity and Rotation forward vector
The range of return will be from [-180, 180]. Useful for feeding directional blendspaces.

Args:
    velocity (Vector): The velocity to use as direction relative to BaseRotation
    base_rotation (Rotator): The base rotation, e.g. of a pawn

Returns:
    float:

<a id="unreal.LayeredBoneBlendLibrary"></a>