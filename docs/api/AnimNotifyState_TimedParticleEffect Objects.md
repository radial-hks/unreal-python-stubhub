## AnimNotifyState_TimedParticleEffect Objects

```python
class AnimNotifyState_TimedParticleEffect(AnimNotifyState)
```

Timed Particle Effect Notify
Allows a looping particle effect to be played in an animation that will activate
at the beginning of the notify and deactivate at the end.

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyState_TimedParticleEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``destroy_at_end`` (bool):  [Read-Write] Whether the particle system should be immediately destroyed at the end of the notify state or be allowed to finish
- ``location_offset`` (Vector):  [Read-Write] Offset from the socket or bone to place the particle system
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``ps_template`` (ParticleSystem):  [Read-Write] The particle system to spawn for the notify state
- ``rotation_offset`` (Rotator):  [Read-Write] Rotation offset from the socket or bone for the particle system
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors
- ``socket_name`` (Name):  [Read-Write] The socket or bone to attach the system to

<a id="unreal.AnimNotifyState_Trail"></a>