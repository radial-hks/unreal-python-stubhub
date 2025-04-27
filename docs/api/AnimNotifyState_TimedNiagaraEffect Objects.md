## AnimNotifyState_TimedNiagaraEffect Objects

```python
class AnimNotifyState_TimedNiagaraEffect(AnimNotifyState)
```

Timed Niagara Effect Notify
Allows a looping Niagara effect to be played in an animation that will activate
at the beginning of the notify and deactivate at the end.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraAnimNotifies
- **File**: AnimNotifyState_TimedNiagaraEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_rate_scale_as_time_dilation`` (bool):  [Read-Write] Should we set the animation rate scale as time dilation on the spawn effect?
- ``destroy_at_end`` (bool):  [Read-Write] Whether the Niagara system should be immediately destroyed at the end of the notify state or be allowed to finish
- ``location_offset`` (Vector):  [Read-Write] Offset from the socket or bone to place the Niagara system
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``rotation_offset`` (Rotator):  [Read-Write] Rotation offset from the socket or bone for the Niagara system
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors
- ``socket_name`` (Name):  [Read-Write] The socket or bone to attach the system to
- ``template`` (NiagaraSystem):  [Read-Write] The niagara system to spawn for the notify state

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.template"></a>

#### template

```python
@property
def template() -> NiagaraSystem
```

(NiagaraSystem):  [Read-Only] The niagara system to spawn for the notify state

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.socket_name"></a>

#### socket_name

```python
@property
def socket_name() -> Name
```

(Name):  [Read-Only] The socket or bone to attach the system to

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.location_offset"></a>

#### location_offset

```python
@property
def location_offset() -> Vector
```

(Vector):  [Read-Only] Offset from the socket or bone to place the Niagara system

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.rotation_offset"></a>

#### rotation_offset

```python
@property
def rotation_offset() -> Rotator
```

(Rotator):  [Read-Only] Rotation offset from the socket or bone for the Niagara system

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.apply_rate_scale_as_time_dilation"></a>

#### apply_rate_scale_as_time_dilation

```python
@property
def apply_rate_scale_as_time_dilation() -> bool
```

(bool):  [Read-Only] Should we set the animation rate scale as time dilation on the spawn effect?

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.destroy_at_end"></a>

#### destroy_at_end

```python
@property
def destroy_at_end() -> bool
```

(bool):  [Read-Only] Whether the Niagara system should be immediately destroyed at the end of the notify state or be allowed to finish

<a id="unreal.AnimNotifyState_TimedNiagaraEffect.get_spawned_effect"></a>

#### get_spawned_effect

```python
def get_spawned_effect(mesh_comp: MeshComponent) -> FXSystemComponent
```

x.get_spawned_effect(mesh_comp) -> FXSystemComponent
Return FXSystemComponent created from SpawnEffect

Args:
    mesh_comp (MeshComponent): 

Returns:
    FXSystemComponent:

<a id="unreal.AnimNotifyState_TimedNiagaraEffectAdvanced"></a>