## CameraShakePatternStartParams Objects

```python
class CameraShakePatternStartParams(StructBase)
```

Parameters for starting a camera shake pattern.

**C++ Source:**

- **Module**: Engine
- **File**: CameraShakeBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_override`` (float):  [Read-Write] An optional override for the camera shake's duration
- ``is_restarting`` (bool):  [Read-Write] Whether the camera shake is restarting while playing
- ``override_duration`` (bool):  [Read-Write] Whether the camera shake's duration is overriden (see DurationOverride)

<a id="unreal.CameraShakePatternStartParams.__init__"></a>

#### __init__

```python
def __init__(is_restarting: bool = False,
             override_duration: bool = False,
             duration_override: float = 0.000000) -> None
```

<a id="unreal.CameraShakePatternStartParams.is_restarting"></a>

#### is_restarting

```python
@property
def is_restarting() -> bool
```

(bool):  [Read-Write] Whether the camera shake is restarting while playing

<a id="unreal.CameraShakePatternStartParams.is_restarting"></a>

#### is_restarting

```python
@is_restarting.setter
def is_restarting(value: bool) -> None
```

<a id="unreal.CameraShakePatternStartParams.override_duration"></a>

#### override_duration

```python
@property
def override_duration() -> bool
```

(bool):  [Read-Write] Whether the camera shake's duration is overriden (see DurationOverride)

<a id="unreal.CameraShakePatternStartParams.override_duration"></a>

#### override_duration

```python
@override_duration.setter
def override_duration(value: bool) -> None
```

<a id="unreal.CameraShakePatternStartParams.duration_override"></a>

#### duration_override

```python
@property
def duration_override() -> float
```

(float):  [Read-Write] An optional override for the camera shake's duration

<a id="unreal.CameraShakePatternStartParams.duration_override"></a>

#### duration_override

```python
@duration_override.setter
def duration_override(value: float) -> None
```

<a id="unreal.CameraShakeStartParams"></a>