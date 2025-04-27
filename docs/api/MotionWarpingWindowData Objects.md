## MotionWarpingWindowData Objects

```python
class MotionWarpingWindowData(StructBase)
```

Motion Warping Window Data

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: MotionWarpingComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_notify`` (AnimNotifyState_MotionWarping):  [Read-Write]
- ``end_time`` (float):  [Read-Write]
- ``start_time`` (float):  [Read-Write]

<a id="unreal.MotionWarpingWindowData.__init__"></a>

#### __init__

```python
def __init__(anim_notify: AnimNotifyState_MotionWarping = None,
             start_time: float = 0.000000,
             end_time: float = 0.000000) -> None
```

<a id="unreal.MotionWarpingWindowData.anim_notify"></a>

#### anim_notify

```python
@property
def anim_notify() -> AnimNotifyState_MotionWarping
```

(AnimNotifyState_MotionWarping):  [Read-Write]

<a id="unreal.MotionWarpingWindowData.anim_notify"></a>

#### anim_notify

```python
@anim_notify.setter
def anim_notify(value: AnimNotifyState_MotionWarping) -> None
```

<a id="unreal.MotionWarpingWindowData.start_time"></a>

#### start_time

```python
@property
def start_time() -> float
```

(float):  [Read-Write]

<a id="unreal.MotionWarpingWindowData.start_time"></a>

#### start_time

```python
@start_time.setter
def start_time(value: float) -> None
```

<a id="unreal.MotionWarpingWindowData.end_time"></a>

#### end_time

```python
@property
def end_time() -> float
```

(float):  [Read-Write]

<a id="unreal.MotionWarpingWindowData.end_time"></a>

#### end_time

```python
@end_time.setter
def end_time(value: float) -> None
```

<a id="unreal.MotionWarpingTarget"></a>