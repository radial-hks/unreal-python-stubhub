## AnimNotify_PlayParticleEffect Objects

```python
class AnimNotify_PlayParticleEffect(AnimNotify)
```

Anim Notify Play Particle Effect

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotify_PlayParticleEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attached`` (bool):  [Read-Write] Should attach to the bone/socket
- ``location_offset`` (Vector):  [Read-Write] Location offset from the socket
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``ps_template`` (ParticleSystem):  [Read-Write] Particle System to Spawn
- ``rotation_offset`` (Rotator):  [Read-Write] Rotation offset from socket
- ``scale`` (Vector):  [Read-Write] Scale to spawn the particle system at
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify instance should fire in animation editors
- ``socket_name`` (Name):  [Read-Write] SocketName to attach to

<a id="unreal.AnimNotify_PlayParticleEffect.ps_template"></a>

#### ps_template

```python
@property
def ps_template() -> ParticleSystem
```

(ParticleSystem):  [Read-Only] Particle System to Spawn

<a id="unreal.AnimNotify_PlayParticleEffect.location_offset"></a>

#### location_offset

```python
@property
def location_offset() -> Vector
```

(Vector):  [Read-Only] Location offset from the socket

<a id="unreal.AnimNotify_PlayParticleEffect.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Rotator
```

(Rotator):  [Read-Only] Rotation offset from socket

<a id="unreal.AnimNotify_PlayParticleEffect.attached"></a>

#### attached

```python
@property
def attached() -> bool
```

(bool):  [Read-Only] Should attach to the bone/socket

<a id="unreal.AnimNotify_PlayParticleEffect.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] SocketName to attach to

<a id="unreal.AnimNotify_PlayParticleEffect_C"></a>