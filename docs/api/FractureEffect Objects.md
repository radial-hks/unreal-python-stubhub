## FractureEffect Objects

```python
class FractureEffect(StructBase)
```

Struct used to hold effects for destructible damage events

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``particle_system`` (ParticleSystem):  [Read-Write] Particle system effect to play at fracture location.
- ``sound`` (SoundBase):  [Read-Write] Sound cue to play at fracture location.

<a id="unreal.FractureEffect.__init__"></a>

#### __init__

```python
def __init__(particle_system: ParticleSystem = None,
             sound: SoundBase = None) -> None
```

<a id="unreal.FractureEffect.particle_system"></a>

#### particle_system

```python
@property
def particle_system() -> ParticleSystem
```

(ParticleSystem):  [Read-Write] Particle system effect to play at fracture location.

<a id="unreal.FractureEffect.particle_system"></a>

#### particle_system

```python
@particle_system.setter
def particle_system(value: ParticleSystem) -> None
```

<a id="unreal.FractureEffect.sound"></a>

#### sound

```python
@property
def sound() -> SoundBase
```

(SoundBase):  [Read-Write] Sound cue to play at fracture location.

<a id="unreal.FractureEffect.sound"></a>

#### sound

```python
@sound.setter
def sound(value: SoundBase) -> None
```

<a id="unreal.BasedPosition"></a>