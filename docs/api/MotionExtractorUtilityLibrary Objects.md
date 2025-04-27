## MotionExtractorUtilityLibrary Objects

```python
class MotionExtractorUtilityLibrary(BlueprintFunctionLibrary)
```

Motion Extractor Utility Library

**C++ Source:**

- **Plugin**: AnimationModifierLibrary
- **Module**: AnimationModifierLibrary
- **File**: MotionExtractorUtilities.h

<a id="unreal.MotionExtractorUtilityLibrary.get_stopped_ranges_from_root_motion"></a>

#### get_stopped_ranges_from_root_motion

```python
@classmethod
def get_stopped_ranges_from_root_motion(
        cls,
        anim_sequence: AnimSequence,
        stop_speed_threshold: float = 10.000000,
        sample_rate: float = 120.000000) -> Array[Vector2D]
```

X.get_stopped_ranges_from_root_motion(anim_sequence, stop_speed_threshold=10.000000, sample_rate=120.000000) -> Array[Vector2D]
Returns the ranges (X/Start to Y/End) in the specified animation sequence where the animation is considered stopped.

Args:
    anim_sequence (AnimSequence): Anim sequence to check
    stop_speed_threshold (float): Root motion speed under which the animation is considered stopped.
    sample_rate (float): Sample rate of the animation. It's recommended to use high values if the animation has very sudden direction changes.

Returns:
    Array[Vector2D]:

<a id="unreal.MotionExtractorUtilityLibrary.get_moving_ranges_from_root_motion"></a>

#### get_moving_ranges_from_root_motion

```python
@classmethod
def get_moving_ranges_from_root_motion(
        cls,
        anim_sequence: AnimSequence,
        stop_speed_threshold: float = 10.000000,
        sample_rate: float = 120.000000) -> Array[Vector2D]
```

X.get_moving_ranges_from_root_motion(anim_sequence, stop_speed_threshold=10.000000, sample_rate=120.000000) -> Array[Vector2D]
Returns the ranges (X/Start to Y/End) in the specified animation sequence where the animation is considered moving.

Args:
    anim_sequence (AnimSequence): Anim sequence to check
    stop_speed_threshold (float): Root motion speed over which the animation is considered moving.
    sample_rate (float): Sample rate of the animation. It's recommended to use high values if the animation has very sudden direction changes.

Returns:
    Array[Vector2D]:

<a id="unreal.MotionExtractorUtilityLibrary.get_desired_value"></a>

#### get_desired_value

```python
@classmethod
def get_desired_value(cls, bone_transform: Transform,
                      last_bone_transform: Transform, delta_time: float,
                      motion_type: MotionExtractor_MotionType,
                      axis: MotionExtractor_Axis) -> float
```

X.get_desired_value(bone_transform, last_bone_transform, delta_time, motion_type, axis) -> float
Returns the desired value from the extracted poses based on input settings.

Args:
    bone_transform (Transform): Current frame's bone transform
    last_bone_transform (Transform): Last frame's bone transform. Unused when not calculating speeds.
    delta_time (float): Time step used between current and last bone transforms. Unused when not calculating speeds.
    motion_type (MotionExtractor_MotionType): What type of motion to extract (translation, rotation, speed, etc.)
    axis (MotionExtractor_Axis): Which axis/axes to extract motion from

Returns:
    float:

<a id="unreal.MotionExtractorUtilityLibrary.generate_curve_name"></a>

#### generate_curve_name

```python
@classmethod
def generate_curve_name(cls, bone_name: Name,
                        motion_type: MotionExtractor_MotionType,
                        axis: MotionExtractor_Axis) -> Name
```

X.generate_curve_name(bone_name, motion_type, axis) -> Name
Generates a curve name based on input settings.

Args:
    bone_name (Name): The name of the bone
    motion_type (MotionExtractor_MotionType): What type of motion this curve represents (translation, rotation, speed, etc.)
    axis (MotionExtractor_Axis): Which axis/axes the motion for this curve was extracted from

Returns:
    Name:

<a id="unreal.ReOrientRootBoneModifier"></a>