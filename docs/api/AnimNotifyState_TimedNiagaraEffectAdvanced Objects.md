## AnimNotifyState_TimedNiagaraEffectAdvanced Objects

```python
class AnimNotifyState_TimedNiagaraEffectAdvanced(
        AnimNotifyState_TimedNiagaraEffect)
```

Same as Timed Niagara Effect but also provides some more advanced abilities at an additional cost.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraAnimNotifies
- **File**: AnimNotifyState_TimedNiagaraEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anim_curves`` (Array[CurveParameterPair]):  [Read-Write] Array of fnames to map Anim Curve names to Niagara Parameters.
- ``apply_rate_scale_as_time_dilation`` (bool):  [Read-Write] Should we set the animation rate scale as time dilation on the spawn effect?
- ``apply_rate_scale_to_progress`` (bool):  [Read-Write] Should we apply the animation rate scale when calculating the elasped time.
- ``destroy_at_end`` (bool):  [Read-Write] Whether the Niagara system should be immediately destroyed at the end of the notify state or be allowed to finish
- ``enable_normalized_notify_progress`` (bool):  [Read-Write] This send a 0-1 value of the normalized progress to the FX Component to the float User Parameter.
- ``location_offset`` (Vector):  [Read-Write] Offset from the socket or bone to place the Niagara system
- ``notify_color`` (Color):  [Read-Write] Color of Notify in editor
- ``notify_progress_user_parameter`` (Name):  [Read-Write] The name of your niagara user variable you would like to send the normalized notify progress to.
- ``rotation_offset`` (Rotator):  [Read-Write] Rotation offset from the socket or bone for the Niagara system
- ``should_fire_in_editor`` (bool):  [Read-Write] Whether this notify state instance should fire in animation editors
- ``socket_name`` (Name):  [Read-Write] The socket or bone to attach the system to
- ``template`` (NiagaraSystem):  [Read-Write] The niagara system to spawn for the notify state

<a id="unreal.AnimNotifyState_TimedNiagaraEffectAdvanced.apply_rate_scale_to_progress"></a>

#### apply_rate_scale_to_progress

```python
@property
def apply_rate_scale_to_progress() -> bool
```

(bool):  [Read-Only] Should we apply the animation rate scale when calculating the elasped time.

<a id="unreal.AnimNotifyState_TimedNiagaraEffectAdvanced.get_notify_progress"></a>

#### get_notify_progress

```python
def get_notify_progress(mesh_comp: MeshComponent) -> float
```

x.get_notify_progress(mesh_comp) -> float
Returns a 0 to 1 value for the progress of this component along the notify.

Args:
    mesh_comp (MeshComponent): 

Returns:
    float:

<a id="unreal.AnimNotify_PlayNiagaraEffect"></a>