## ParticleCollisionSignature Objects

```python
class ParticleCollisionSignature(MulticastDelegateBase)
```

Fires when a particle dies

Args:
    event_name (Name): Custom event name for the Collision Event.
    emitter_time (float): The emitter time when the event occured.
    particle_time (int32): How long the particle had been alive at the time of the event.
    location (Vector): Location of the collision.
    velocity (Vector): Velocity of the particle at the point of collision.
    direction (Vector): Direction of the particle at the point of collision.
    normal (Vector): Normal to the surface with which collision occurred.
    bone_name (Name): 
    phys_mat (PhysicalMaterial): Physical Material for this collision.

**C++ Source:**

- **Module**: Engine
- **File**: Emitter.h

<a id="unreal.ParticleCollisionSignature.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.ParticleDeathSignature"></a>