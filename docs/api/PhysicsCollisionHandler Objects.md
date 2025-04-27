## PhysicsCollisionHandler Objects

```python
class PhysicsCollisionHandler(Object)
```

Physics Collision Handler

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsCollisionHandler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_impact_sound`` (SoundBase):  [Read-Write] Sound to play
- ``impact_re_fire_delay`` (float):  [Read-Write] Min time between effect/sound being triggered
- ``impact_threshold`` (float):  [Read-Write] How hard an impact must be to trigger effect/sound

<a id="unreal.PhysicsCollisionHandler.impact_threshold"></a>

#### impact_threshold

```python
@property
def impact_threshold() -> float
```

(float):  [Read-Write] How hard an impact must be to trigger effect/sound

<a id="unreal.PhysicsCollisionHandler.impact_threshold"></a>

#### impact_threshold

```python
@impact_threshold.setter
def impact_threshold(value: float) -> None
```

<a id="unreal.PhysicsCollisionHandler.impact_re_fire_delay"></a>

#### impact_re_fire_delay

```python
@property
def impact_re_fire_delay() -> float
```

(float):  [Read-Write] Min time between effect/sound being triggered

<a id="unreal.PhysicsCollisionHandler.impact_re_fire_delay"></a>

#### impact_re_fire_delay

```python
@impact_re_fire_delay.setter
def impact_re_fire_delay(value: float) -> None
```

<a id="unreal.PhysicsCollisionHandler.default_impact_sound"></a>

#### default_impact_sound

```python
@property
def default_impact_sound() -> SoundBase
```

(SoundBase):  [Read-Write] Sound to play

<a id="unreal.PhysicsCollisionHandler.default_impact_sound"></a>

#### default_impact_sound

```python
@default_impact_sound.setter
def default_impact_sound(value: SoundBase) -> None
```

<a id="unreal.PhysicsConstraintActor"></a>