## ParticleSpawnSignature Objects

```python
class ParticleSpawnSignature(MulticastDelegateBase)
```

Fires when a particle is spawned

Args:
    event_name (Name): Custom event name for the Spawn Event.
    emitter_time (float): The emitter time when the event occured.
    location (Vector): Location at which the particle was spawned.
    velocity (Vector): Initial velocity of the spawned particle.

**C++ Source:**

- **Module**: Engine
- **File**: Emitter.h

<a id="unreal.ParticleSpawnSignature.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.PlasticDeformationEventSignature"></a>