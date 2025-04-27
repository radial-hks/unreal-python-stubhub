## CameraLookatTrackingSettings Objects

```python
class CameraLookatTrackingSettings(StructBase)
```

Settings to control the camera's lookat feature

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_to_track`` (Actor):  [Read-Write] If set, camera will track this actor's location
- ``allow_roll`` (bool):  [Read-Write] True to allow user-defined roll, false otherwise.
- ``draw_debug_look_at_tracking_position`` (bool):  [Read-Write] True to draw a debug representation of the lookat location
- ``enable_look_at_tracking`` (bool):  [Read-Write] True to enable lookat tracking, false otherwise.
- ``look_at_tracking_interp_speed`` (float):  [Read-Write] Controls degree of smoothing. 0.f for no smoothing, higher numbers for faster/tighter tracking.
- ``relative_offset`` (Vector):  [Read-Write] Offset from actor position to look at. Relative to actor if tracking an actor, relative to world otherwise.

<a id="unreal.CameraLookatTrackingSettings.__init__"></a>

#### __init__

```python
def __init__(enable_look_at_tracking: bool = False,
             draw_debug_look_at_tracking_position: bool = False,
             look_at_tracking_interp_speed: float = 0.000000,
             actor_to_track: Actor = None,
             relative_offset: Vector = [0.000000, 0.000000, 0.000000],
             allow_roll: bool = False) -> None
```

<a id="unreal.CameraLookatTrackingSettings.enable_look_at_tracking"></a>

#### enable_look_at_tracking

```python
@property
def enable_look_at_tracking() -> bool
```

(bool):  [Read-Write] True to enable lookat tracking, false otherwise.

<a id="unreal.CameraLookatTrackingSettings.enable_look_at_tracking"></a>

#### enable_look_at_tracking

```python
@enable_look_at_tracking.setter
def enable_look_at_tracking(value: bool) -> None
```

<a id="unreal.CameraLookatTrackingSettings.draw_debug_look_at_tracking_position"></a>

#### draw_debug_look_at_tracking_position

```python
@property
def draw_debug_look_at_tracking_position() -> bool
```

(bool):  [Read-Write] True to draw a debug representation of the lookat location

<a id="unreal.CameraLookatTrackingSettings.draw_debug_look_at_tracking_position"></a>

#### draw_debug_look_at_tracking_position

```python
@draw_debug_look_at_tracking_position.setter
def draw_debug_look_at_tracking_position(value: bool) -> None
```

<a id="unreal.CameraLookatTrackingSettings.look_at_tracking_interp_speed"></a>

#### look_at_tracking_interp_speed

```python
@property
def look_at_tracking_interp_speed() -> float
```

(float):  [Read-Write] Controls degree of smoothing. 0.f for no smoothing, higher numbers for faster/tighter tracking.

<a id="unreal.CameraLookatTrackingSettings.look_at_tracking_interp_speed"></a>

#### look_at_tracking_interp_speed

```python
@look_at_tracking_interp_speed.setter
def look_at_tracking_interp_speed(value: float) -> None
```

<a id="unreal.CameraLookatTrackingSettings.actor_to_track"></a>

#### actor_to_track

```python
@property
def actor_to_track() -> Actor
```

(Actor):  [Read-Write] If set, camera will track this actor's location

<a id="unreal.CameraLookatTrackingSettings.actor_to_track"></a>

#### actor_to_track

```python
@actor_to_track.setter
def actor_to_track(value: Actor) -> None
```

<a id="unreal.CameraLookatTrackingSettings.relative_offset"></a>

#### relative_offset

```python
@property
def relative_offset() -> Vector
```

(Vector):  [Read-Write] Offset from actor position to look at. Relative to actor if tracking an actor, relative to world otherwise.

<a id="unreal.CameraLookatTrackingSettings.relative_offset"></a>

#### relative_offset

```python
@relative_offset.setter
def relative_offset(value: Vector) -> None
```

<a id="unreal.CameraLookatTrackingSettings.allow_roll"></a>

#### allow_roll

```python
@property
def allow_roll() -> bool
```

(bool):  [Read-Write] True to allow user-defined roll, false otherwise.

<a id="unreal.CameraLookatTrackingSettings.allow_roll"></a>

#### allow_roll

```python
@allow_roll.setter
def allow_roll(value: bool) -> None
```

<a id="unreal.CameraFilmbackSettings"></a>