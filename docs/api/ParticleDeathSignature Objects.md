## ParticleDeathSignature Objects

```python
class ParticleDeathSignature(MulticastDelegateBase)
```

Fires when a particle dies

Args:
    event_name (Name): Custom event name for the Death Event.
    emitter_time (float): The emitter time when the event occured.
    particle_time (int32): How long the particle had been alive at the time of the event.
    location (Vector): Location the particle was at when it died.
    velocity (Vector): Velocity of the particle when it died.
    direction (Vector): Direction of the particle when it died.

**C++ Source:**

- **Module**: Engine
- **File**: Emitter.h

<a id="unreal.ParticleDeathSignature.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.ParticleSpawnSignature"></a>