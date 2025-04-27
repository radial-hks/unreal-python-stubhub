## CameraTrackingFocusSettings Objects

```python
class CameraTrackingFocusSettings(StructBase)
```

Settings to control tracking-focus mode.

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_to_track`` (Actor):  [Read-Write] Focus distance will be tied to this actor's location.
- ``draw_debug_tracking_focus_point`` (bool):  [Read-Write] True to draw a debug representation of the tracked position.
- ``relative_offset`` (Vector):  [Read-Write] Offset from actor position to track. Relative to actor if tracking an actor, relative to world otherwise.

<a id="unreal.CameraTrackingFocusSettings.__init__"></a>

#### __init__

```python
def __init__(actor_to_track: Actor = None,
             relative_offset: Vector = [0.000000, 0.000000, 0.000000],
             draw_debug_tracking_focus_point: bool = False) -> None
```

<a id="unreal.CameraTrackingFocusSettings.actor_to_track"></a>

#### actor_to_track

```python
@property
def actor_to_track() -> Actor
```

(Actor):  [Read-Write] Focus distance will be tied to this actor's location.

<a id="unreal.CameraTrackingFocusSettings.actor_to_track"></a>

#### actor_to_track

```python
@actor_to_track.setter
def actor_to_track(value: Actor) -> None
```

<a id="unreal.CameraTrackingFocusSettings.relative_offset"></a>

#### relative_offset

```python
@property
def relative_offset() -> Vector
```

(Vector):  [Read-Write] Offset from actor position to track. Relative to actor if tracking an actor, relative to world otherwise.

<a id="unreal.CameraTrackingFocusSettings.relative_offset"></a>

#### relative_offset

```python
@relative_offset.setter
def relative_offset(value: Vector) -> None
```

<a id="unreal.CameraTrackingFocusSettings.draw_debug_tracking_focus_point"></a>

#### draw_debug_tracking_focus_point

```python
@property
def draw_debug_tracking_focus_point() -> bool
```

(bool):  [Read-Write] True to draw a debug representation of the tracked position.

<a id="unreal.CameraTrackingFocusSettings.draw_debug_tracking_focus_point"></a>

#### draw_debug_tracking_focus_point

```python
@draw_debug_tracking_focus_point.setter
def draw_debug_tracking_focus_point(value: bool) -> None
```

<a id="unreal.CameraFocusSettings"></a>