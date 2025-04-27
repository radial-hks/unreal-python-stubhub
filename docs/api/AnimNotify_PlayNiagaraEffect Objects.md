## AnimNotify_PlayNiagaraEffect Objects

```python
class AnimNotify_PlayNiagaraEffect(AnimNotify)
```

Anim Notify Play Niagara Effect

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraAnimNotifies
- **File**: AnimNotify_PlayNiagaraEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_scale`` (bool):  [Read-Write] Whether or not we are in absolute scale mode
- ``attached`` (bool):  [Read-Write] Should attach to the bone/socket
- ``location_offset`` (Vector):  [Read-Write] Location offset from the socket
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``rotation_offset`` (Rotator):  [Read-Write] Rotation offset from socket
- ``scale`` (Vector):  [Read-Write] Scale to spawn the Niagara system at
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify instance should fire in animation editors
- ``socket_name`` (Name):  [Read-Write] SocketName to attach to
- ``template`` (NiagaraSystem):  [Read-Write] Niagara System to Spawn

<a id="unreal.AnimNotify_PlayNiagaraEffect.template"></a>

#### template

```python
@property
def template() -> NiagaraSystem
```

(NiagaraSystem):  [Read-Only] Niagara System to Spawn

<a id="unreal.AnimNotify_PlayNiagaraEffect.location_offset"></a>

#### location_offset

```python
@property
def location_offset() -> Vector
```

(Vector):  [Read-Only] Location offset from the socket

<a id="unreal.AnimNotify_PlayNiagaraEffect.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Rotator
```

(Rotator):  [Read-Only] Rotation offset from socket

<a id="unreal.AnimNotify_PlayNiagaraEffect.attached"></a>

#### attached

```python
@property
def attached() -> bool
```

(bool):  [Read-Only] Should attach to the bone/socket

<a id="unreal.AnimNotify_PlayNiagaraEffect.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] SocketName to attach to

<a id="unreal.AnimNotify_PlayNiagaraEffect.get_spawned_effect"></a>

#### get_spawned_effect

```python
def get_spawned_effect() -> FXSystemComponent
```

x.get_spawned_effect() -> FXSystemComponent
Return FXSystemComponent created from SpawnEffect

Returns:
    FXSystemComponent:

<a id="unreal.MovieSceneNiagaraCacheSection"></a>