## RootMotionModifier Objects

```python
class RootMotionModifier(Object)
```

URootMotionModifier

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: RootMotionModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actual_start_time`` (float):  [Read-Write] Actual playback time when the modifier becomes active
- ``animation`` (AnimSequenceBase):  [Read-Write] Source of the root motion we are warping
- ``current_position`` (float):  [Read-Write] Current playback time of the animation
- ``end_time`` (float):  [Read-Write] End time of the warping window
- ``previous_position`` (float):  [Read-Write] Previous playback time of the animation
- ``start_time`` (float):  [Read-Write] Start time of the warping window
- ``start_transform`` (Transform):  [Read-Write] Character owner transform at the time this modifier becomes active
- ``total_root_motion_within_window`` (Transform):  [Read-Write] Total root motion within the warping window
- ``weight`` (float):  [Read-Write] Current blend weight of the animation

<a id="unreal.RootMotionModifier.animation"></a>

#### animation

```python
@property
def animation() -> AnimSequenceBase
```

(AnimSequenceBase):  [Read-Only] Source of the root motion we are warping

<a id="unreal.RootMotionModifier.start_time"></a>

#### start_time

```python
@property
def start_time() -> float
```

(float):  [Read-Only] Start time of the warping window

<a id="unreal.RootMotionModifier.end_time"></a>

#### end_time

```python
@property
def end_time() -> float
```

(float):  [Read-Only] End time of the warping window

<a id="unreal.RootMotionModifier.previous_position"></a>

#### previous_position

```python
@property
def previous_position() -> float
```

(float):  [Read-Only] Previous playback time of the animation

<a id="unreal.RootMotionModifier.current_position"></a>

#### current_position

```python
@property
def current_position() -> float
```

(float):  [Read-Only] Current playback time of the animation

<a id="unreal.RootMotionModifier.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Only] Current blend weight of the animation

<a id="unreal.RootMotionModifier.start_transform"></a>

#### start_transform

```python
@property
def start_transform() -> Transform
```

(Transform):  [Read-Only] Character owner transform at the time this modifier becomes active

<a id="unreal.RootMotionModifier.actual_start_time"></a>

#### actual_start_time

```python
@property
def actual_start_time() -> float
```

(float):  [Read-Only] Actual playback time when the modifier becomes active

<a id="unreal.RootMotionModifier.total_root_motion_within_window"></a>

#### total_root_motion_within_window

```python
@property
def total_root_motion_within_window() -> Transform
```

(Transform):  [Read-Only] Total root motion within the warping window

<a id="unreal.RootMotionModifier_Warp"></a>