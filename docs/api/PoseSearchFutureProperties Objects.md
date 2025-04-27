## PoseSearchFutureProperties Objects

```python
class PoseSearchFutureProperties(StructBase)
```

Pose Search Future Properties

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation`` (Object):  [Read-Write] Animation to play (it'll start at AnimationTime seconds)
- ``animation_time`` (float):  [Read-Write] Start time for Animation
- ``interval_time`` (float):  [Read-Write] Interval time before playing Animation

<a id="unreal.PoseSearchFutureProperties.__init__"></a>

#### __init__

```python
def __init__(animation: Object = None,
             animation_time: float = 0.000000,
             interval_time: float = 0.000000) -> None
```

<a id="unreal.PoseSearchFutureProperties.animation"></a>

#### animation

```python
@property
def animation() -> Object
```

(Object):  [Read-Write] Animation to play (it'll start at AnimationTime seconds)

<a id="unreal.PoseSearchFutureProperties.animation"></a>

#### animation

```python
@animation.setter
def animation(value: Object) -> None
```

<a id="unreal.PoseSearchFutureProperties.animation_time"></a>

#### animation_time

```python
@property
def animation_time() -> float
```

(float):  [Read-Write] Start time for Animation

<a id="unreal.PoseSearchFutureProperties.animation_time"></a>

#### animation_time

```python
@animation_time.setter
def animation_time(value: float) -> None
```

<a id="unreal.PoseSearchFutureProperties.interval_time"></a>

#### interval_time

```python
@property
def interval_time() -> float
```

(float):  [Read-Write] Interval time before playing Animation

<a id="unreal.PoseSearchFutureProperties.interval_time"></a>

#### interval_time

```python
@interval_time.setter
def interval_time(value: float) -> None
```

<a id="unreal.PoseSearchContinuingProperties"></a>