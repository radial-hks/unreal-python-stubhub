## CameraShakePatternUpdateParams Objects

```python
class CameraShakePatternUpdateParams(StructBase)
```

Parameters for updating a camera shake pattern.

**C++ Source:**

- **Module**: Engine
- **File**: CameraShakeBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta_time`` (float):  [Read-Write] The time elapsed since last update
- ``dynamic_scale`` (float):  [Read-Write] The dynamic scale being passed down from the camera manger for the next update
- ``pov`` (MinimalViewInfo):  [Read-Write] The current view that this camera shake should modify
- ``shake_scale`` (float):  [Read-Write] The base scale for this shake

<a id="unreal.CameraShakePatternUpdateParams.__init__"></a>

#### __init__

```python
def __init__(
    delta_time: float = 0.000000,
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

<a id="unreal.CameraShakePatternUpdateParams.delta_time"></a>

#### delta_time

```python
@property
def delta_time() -> float
```

(float):  [Read-Write] The time elapsed since last update

<a id="unreal.CameraShakePatternUpdateParams.delta_time"></a>

#### delta_time

```python
@delta_time.setter
def delta_time(value: float) -> None
```

<a id="unreal.CameraShakePatternUpdateParams.shake_scale"></a>

#### shake_scale

```python
@property
def shake_scale() -> float
```

(float):  [Read-Write] The base scale for this shake

<a id="unreal.CameraShakePatternUpdateParams.shake_scale"></a>

#### shake_scale

```python
@shake_scale.setter
def shake_scale(value: float) -> None
```

<a id="unreal.CameraShakePatternUpdateParams.dynamic_scale"></a>

#### dynamic_scale

```python
@property
def dynamic_scale() -> float
```

(float):  [Read-Write] The dynamic scale being passed down from the camera manger for the next update

<a id="unreal.CameraShakePatternUpdateParams.dynamic_scale"></a>

#### dynamic_scale

```python
@dynamic_scale.setter
def dynamic_scale(value: float) -> None
```

<a id="unreal.CameraShakePatternUpdateParams.pov"></a>

#### pov

```python
@property
def pov() -> MinimalViewInfo
```

(MinimalViewInfo):  [Read-Write] The current view that this camera shake should modify

<a id="unreal.CameraShakePatternUpdateParams.pov"></a>

#### pov

```python
@pov.setter
def pov(value: MinimalViewInfo) -> None
```

<a id="unreal.CameraShakeUpdateParams"></a>