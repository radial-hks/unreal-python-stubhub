## MovieSceneCameraShakeSourceTrigger Objects

```python
class MovieSceneCameraShakeSourceTrigger(StructBase)
```

Movie Scene Camera Shake Source Trigger

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneCameraShakeSourceTriggerChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``play_scale`` (float):  [Read-Write] Scalar that affects shake intensity
- ``play_space`` (CameraShakePlaySpace):  [Read-Write]
- ``shake_class`` (type(Class)):  [Read-Write] Class of the camera shake to play
- ``user_defined_play_space`` (Rotator):  [Read-Write]

<a id="unreal.MovieSceneCameraShakeSourceTrigger.__init__"></a>

#### __init__

```python
def __init__(
        shake_class: Class = None,
        play_scale: float = 0.000000,
        play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
        user_defined_play_space: Rotator = [0.000000, 0.000000,
                                            0.000000]) -> None
```

<a id="unreal.MovieSceneCameraShakeSourceTrigger.shake_class"></a>

#### shake_class

```python
@property
def shake_class() -> Class
```

(type(Class)):  [Read-Write] Class of the camera shake to play

<a id="unreal.MovieSceneCameraShakeSourceTrigger.shake_class"></a>

#### shake_class

```python
@shake_class.setter
def shake_class(value: Class) -> None
```

<a id="unreal.MovieSceneCameraShakeSourceTrigger.play_scale"></a>

#### play_scale

```python
@property
def play_scale() -> float
```

(float):  [Read-Write] Scalar that affects shake intensity

<a id="unreal.MovieSceneCameraShakeSourceTrigger.play_scale"></a>

#### play_scale

```python
@play_scale.setter
def play_scale(value: float) -> None
```

<a id="unreal.MovieSceneCameraShakeSourceTrigger.play_space"></a>

#### play_space

```python
@property
def play_space() -> CameraShakePlaySpace
```

(CameraShakePlaySpace):  [Read-Write]

<a id="unreal.MovieSceneCameraShakeSourceTrigger.play_space"></a>

#### play_space

```python
@play_space.setter
def play_space(value: CameraShakePlaySpace) -> None
```

<a id="unreal.MovieSceneCameraShakeSourceTrigger.user_defined_play_space"></a>

#### user_defined_play_space

```python
@property
def user_defined_play_space() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.MovieSceneCameraShakeSourceTrigger.user_defined_play_space"></a>

#### user_defined_play_space

```python
@user_defined_play_space.setter
def user_defined_play_space(value: Rotator) -> None
```

<a id="unreal.MovieSceneEventPayloadVariable"></a>