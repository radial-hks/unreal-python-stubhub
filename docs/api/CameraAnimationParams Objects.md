## CameraAnimationParams Objects

```python
class CameraAnimationParams(StructBase)
```

Parameter struct for adding new camera animations to UCameraAnimationCameraModifier

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: CameraAnimationCameraModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_override`` (float):  [Read-Write] Override the duration of the animation with a new duration (including blends)
- ``ease_in_duration`` (float):  [Read-Write] Ease-in duration in seconds
- ``ease_in_type`` (CameraAnimationEasingType):  [Read-Write] Ease-in function type
- ``ease_out_duration`` (float):  [Read-Write] Ease-out duration in seconds
- ``ease_out_type`` (CameraAnimationEasingType):  [Read-Write] Ease-out function type
- ``loop`` (bool):  [Read-Write] Whether the camera animation should loop
- ``play_rate`` (float):  [Read-Write] Time scale for playing the new camera animation
- ``play_space`` (CameraAnimationPlaySpace):  [Read-Write] The transform space to use for the new camera shake
- ``random_start_time`` (bool):  [Read-Write] Whether the camera animation should have a random start time
- ``scale`` (float):  [Read-Write] Global scale to use for the new camera animation
- ``start_offset`` (int32):  [Read-Write] Offset, in frames, into the animation to start at
- ``user_play_space_rot`` (Rotator):  [Read-Write] User space to use when PlaySpace is UserDefined

<a id="unreal.CameraAnimationParams.__init__"></a>

#### __init__

```python
def __init__(
        play_rate: float = 0.000000,
        scale: float = 0.000000,
        ease_in_type: CameraAnimationEasingType = CameraAnimationEasingType.
    LINEAR,
        ease_in_duration: float = 0.000000,
        ease_out_type: CameraAnimationEasingType = CameraAnimationEasingType.
    LINEAR,
        ease_out_duration: float = 0.000000,
        loop: bool = False,
        start_offset: int = 0,
        random_start_time: bool = False,
        duration_override: float = 0.000000,
        play_space: CameraAnimationPlaySpace = CameraAnimationPlaySpace.
    CAMERA_LOCAL,
        user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.CameraAnimationParams.play_rate"></a>

#### play_rate

```python
@property
def play_rate() -> float
```

(float):  [Read-Write] Time scale for playing the new camera animation

<a id="unreal.CameraAnimationParams.play_rate"></a>

#### play_rate

```python
@play_rate.setter
def play_rate(value: float) -> None
```

<a id="unreal.CameraAnimationParams.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] Global scale to use for the new camera animation

<a id="unreal.CameraAnimationParams.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.CameraAnimationParams.ease_in_type"></a>

#### ease_in_type

```python
@property
def ease_in_type() -> CameraAnimationEasingType
```

(CameraAnimationEasingType):  [Read-Write] Ease-in function type

<a id="unreal.CameraAnimationParams.ease_in_type"></a>

#### ease_in_type

```python
@ease_in_type.setter
def ease_in_type(value: CameraAnimationEasingType) -> None
```

<a id="unreal.CameraAnimationParams.ease_in_duration"></a>

#### ease_in_duration

```python
@property
def ease_in_duration() -> float
```

(float):  [Read-Write] Ease-in duration in seconds

<a id="unreal.CameraAnimationParams.ease_in_duration"></a>

#### ease_in_duration

```python
@ease_in_duration.setter
def ease_in_duration(value: float) -> None
```

<a id="unreal.CameraAnimationParams.ease_out_type"></a>

#### ease_out_type

```python
@property
def ease_out_type() -> CameraAnimationEasingType
```

(CameraAnimationEasingType):  [Read-Write] Ease-out function type

<a id="unreal.CameraAnimationParams.ease_out_type"></a>

#### ease_out_type

```python
@ease_out_type.setter
def ease_out_type(value: CameraAnimationEasingType) -> None
```

<a id="unreal.CameraAnimationParams.ease_out_duration"></a>

#### ease_out_duration

```python
@property
def ease_out_duration() -> float
```

(float):  [Read-Write] Ease-out duration in seconds

<a id="unreal.CameraAnimationParams.ease_out_duration"></a>

#### ease_out_duration

```python
@ease_out_duration.setter
def ease_out_duration(value: float) -> None
```

<a id="unreal.CameraAnimationParams.loop"></a>

#### loop

```python
@property
def loop() -> bool
```

(bool):  [Read-Write] Whether the camera animation should loop

<a id="unreal.CameraAnimationParams.loop"></a>

#### loop

```python
@loop.setter
def loop(value: bool) -> None
```

<a id="unreal.CameraAnimationParams.start_offset"></a>

#### start_offset

```python
@property
def start_offset() -> int
```

(int32):  [Read-Write] Offset, in frames, into the animation to start at

<a id="unreal.CameraAnimationParams.start_offset"></a>

#### start_offset

```python
@start_offset.setter
def start_offset(value: int) -> None
```

<a id="unreal.CameraAnimationParams.random_start_time"></a>

#### random_start_time

```python
@property
def random_start_time() -> bool
```

(bool):  [Read-Write] Whether the camera animation should have a random start time

<a id="unreal.CameraAnimationParams.random_start_time"></a>

#### random_start_time

```python
@random_start_time.setter
def random_start_time(value: bool) -> None
```

<a id="unreal.CameraAnimationParams.duration_override"></a>

#### duration_override

```python
@property
def duration_override() -> float
```

(float):  [Read-Write] Override the duration of the animation with a new duration (including blends)

<a id="unreal.CameraAnimationParams.duration_override"></a>

#### duration_override

```python
@duration_override.setter
def duration_override(value: float) -> None
```

<a id="unreal.CameraAnimationParams.play_space"></a>

#### play_space

```python
@property
def play_space() -> CameraAnimationPlaySpace
```

(CameraAnimationPlaySpace):  [Read-Write] The transform space to use for the new camera shake

<a id="unreal.CameraAnimationParams.play_space"></a>

#### play_space

```python
@play_space.setter
def play_space(value: CameraAnimationPlaySpace) -> None
```

<a id="unreal.CameraAnimationParams.user_play_space_rot"></a>

#### user_play_space_rot

```python
@property
def user_play_space_rot() -> Rotator
```

(Rotator):  [Read-Write] User space to use when PlaySpace is UserDefined

<a id="unreal.CameraAnimationParams.user_play_space_rot"></a>

#### user_play_space_rot

```python
@user_play_space_rot.setter
def user_play_space_rot(value: Rotator) -> None
```

<a id="unreal.CameraAnimationHandle"></a>