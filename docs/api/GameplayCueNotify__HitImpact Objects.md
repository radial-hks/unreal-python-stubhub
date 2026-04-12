## GameplayCueNotify\_HitImpact Objects

```python
class GameplayCueNotify_HitImpact(GameplayCueNotify_Static)
```

Non instanced GameplayCueNotify for spawning particle and sound FX.
Still WIP - needs to be fleshed out more.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotify_HitImpact.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_cue_tag`` (GameplayTag):  [Read-Write] Tag this notify is activated by
- ``is_override`` (bool):  [Read-Write] Does this Cue override other cues, or is it called in addition to them? E.g., If this is Damage.Physical.Slash, we wont call Damage.Physical afer we run this cue.
- ``particle_system`` (ParticleSystem):  [Read-Write] Effects to play for weapon attacks against specific surfaces
- ``sound`` (SoundBase):  [Read-Write]

<a id="unreal.GameplayCueNotify_HitImpact.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Write]

<a id="unreal.GameplayCueNotify_HitImpact.sound"></a>

#### sound

```python
@sound.setter
def sound(value: SoundBase) -> None
```

<a id="unreal.GameplayCueNotify_HitImpact.particle_system"></a>

#### particle\_system

```python
@property
def particle_system() -> ParticleSystem
```

(ParticleSystem):  [Read-Write] Effects to play for weapon attacks against specific surfaces

<a id="unreal.GameplayCueNotify_HitImpact.particle_system"></a>

#### particle\_system

```python
@particle_system.setter
def particle_system(value: ParticleSystem) -> None
```

<a id="unreal.GameplayCueNotify_Looping"></a>