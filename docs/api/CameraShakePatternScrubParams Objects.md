## CameraShakePatternScrubParams Objects

```python
class CameraShakePatternScrubParams(StructBase)
```

Parameters for scrubbing a camera shake.

**C++ Source:**

- **Module**: Engine
- **File**: CameraShakeBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_time`` (float):  [Read-Write] The time to scrub to
- ``dynamic_scale`` (float):  [Read-Write] The dynamic scale being passed down from the camera manger for the next update
- ``pov`` (MinimalViewInfo):  [Read-Write] The current view that this camera shake should modify
- ``shake_scale`` (float):  [Read-Write] The base scale for this shake

<a id="unreal.CameraShakePatternScrubParams.__init__"></a>

#### __init__

```python
def __init__(
    absolute_time: float = 0.000000,
    shake_scale: float = 0.000000,
    dynamic_scale: float = 0.000000,
    pov: MinimalViewInfo = [[0.000000, 0.000000, 0.000000],
                            [0.000000, 0.000000, 0.000000], 90.000000,
                            90.000000, 1.000000, 512.000000, True, 0.000000,
                            False, False, 0.000000, 2097152.000000, -1.000000,
                            1.333333, False, False, True,
                            CameraProjectionMode.PERSPECTIVE, 0.000000, [],
                            [0.000000, 0.000000], 1.000000, 1.000000]
) -> None
```

<a id="unreal.CameraShakePatternScrubParams.absolute_time"></a>

#### absolute_time

```python
@property
def absolute_time() -> float
```

(float):  [Read-Write] The time to scrub to

<a id="unreal.CameraShakePatternScrubParams.absolute_time"></a>

#### absolute_time

```python
@absolute_time.setter
def absolute_time(value: float) -> None
```

<a id="unreal.CameraShakePatternScrubParams.shake_scale"></a>

#### shake_scale

```python
@property
def shake_scale() -> float
```

(float):  [Read-Write] The base scale for this shake

<a id="unreal.CameraShakePatternScrubParams.shake_scale"></a>

#### shake_scale

```python
@shake_scale.setter
def shake_scale(value: float) -> None
```

<a id="unreal.CameraShakePatternScrubParams.dynamic_scale"></a>

#### dynamic_scale

```python
@property
def dynamic_scale() -> float
```

(float):  [Read-Write] The dynamic scale being passed down from the camera manger for the next update

<a id="unreal.CameraShakePatternScrubParams.dynamic_scale"></a>

#### dynamic_scale

```python
@dynamic_scale.setter
def dynamic_scale(value: float) -> None
```

<a id="unreal.CameraShakePatternScrubParams.pov"></a>

#### pov

```python
@property
def pov() -> MinimalViewInfo
```

(MinimalViewInfo):  [Read-Write] The current view that this camera shake should modify

<a id="unreal.CameraShakePatternScrubParams.pov"></a>

#### pov

```python
@pov.setter
def pov(value: MinimalViewInfo) -> None
```

<a id="unreal.CameraShakeScrubParams"></a>