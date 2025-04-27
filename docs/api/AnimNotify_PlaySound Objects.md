## AnimNotify_PlaySound Objects

```python
class AnimNotify_PlaySound(AnimNotify)
```

Anim Notify Play Sound

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotify_PlaySound.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attach_name`` (Name):  [Read-Write] Socket or bone name to attach sound to
- ``follow`` (bool):  [Read-Write] If this sound should follow its owner
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``pitch_multiplier`` (float):  [Read-Write] Pitch Multiplier
- ``preview_ignore_attenuation`` (bool):  [Read-Write]
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify instance should fire in animation editors
- ``sound`` (SoundBase):  [Read-Write] Sound to Play
- ``volume_multiplier`` (float):  [Read-Write] Volume Multiplier

<a id="unreal.AnimNotify_PlaySound.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Only] Sound to Play

<a id="unreal.AnimNotify_PlaySound.volume_multiplier"></a>

#### volume_multiplier

```python
@property
def volume_multiplier() -> float
```

(float):  [Read-Only] Volume Multiplier

<a id="unreal.AnimNotify_PlaySound.pitch_multiplier"></a>

#### pitch_multiplier

```python
@property
def pitch_multiplier() -> float
```

(float):  [Read-Only] Pitch Multiplier

<a id="unreal.AnimNotify_PlaySound.follow"></a>

#### follow

```python
@property
def follow() -> bool
```

(bool):  [Read-Only] If this sound should follow its owner

<a id="unreal.AnimNotify_PlaySound.attach_name"></a>

#### attach_name

```python
@property
def attach_name() -> Name
```

(Name):  [Read-Only] Socket or bone name to attach sound to

<a id="unreal.AnimNotify_PlaySound_C"></a>