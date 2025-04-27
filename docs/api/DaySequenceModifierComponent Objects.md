## DaySequenceModifierComponent Objects

```python
class DaySequenceModifierComponent(SceneComponent)
```

Day Sequence Modifier Component

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceModifierComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``bias`` (int32):  [Read-Write] User-defined bias.
- ``blend_amount`` (float):  [Read-Write] Defines the region in which the effective blend weight is in the range (0.0, 1.0) (not inclusive) when Mode == EDaySequenceModifierMode::Volume.
- ``blend_policy`` (DaySequenceModifierUserBlendPolicy):  [Read-Write] Determines how the modifier uses UserBlendWeight to compute effective blend weight.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``day_night_cycle`` (DayNightCycleMode):  [Read-Write] Changes the way the modifier controls the day/night cycle time when enabled.
- ``day_night_cycle_time`` (float):  [Read-Write] The time to use for the day/night cycle.
- ``day_sequence_collection`` (DaySequenceCollectionAsset):  [Read-Write] The user provided collection. This is an alternative to UserDaySequence.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``ignore_bias`` (bool):  [Read-Write] When enabled, these overrides will always override all settings regardless of their bias.
- ``is_component_enabled`` (bool):  [Read-Write] Flag used track whether or not this component is enabled or disabled.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``is_enabled`` (bool):  [Read-Write] Non-serialized variable for tracking whether our overrides are enabled or not.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``mode`` (DaySequenceModifierMode):  [Read-Write] Determines how the modifier computes InternalBlendWeight.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_post_enable_modifier`` (OnPostEnableModifier):  [Read-Write] Blueprint exposed delegate invoked after the modifier component is enabled.
- ``on_post_reinitialize_sub_sequences`` (OnPostReinitializeSubSequences):  [Read-Write] Blueprint exposed delegate invoked after the component's subsequences are reinitialized.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``preview`` (bool):  [Read-Write] When enabled, preview this day sequence modifier in the editor.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``smooth_blending`` (bool):  [Read-Write] If true, day sequence evaluation while within the blending region will be smooth. Note: Can be very expensive.
- ``target_actor`` (DaySequenceActor):  [Read-Write] Non-serialized target actor we are currently bound to
- ``transient_sequence`` (DaySequence):  [Read-Write] The user provided Transient Day Sequence.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_collection`` (bool):  [Read-Write] If true, hide UserDaySequence and expose DaySequenceCollection.
- ``user_blend_weight`` (float):  [Read-Write] User specified blend weight. The final blend weight is determined by BlendPolicy.
- ``user_day_sequence`` (DaySequence):  [Read-Write] The user provided Day Sequence.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``volume_shape_components`` (Array[ComponentReference]):  [Read-Write] When set, the shape components will be used for the modifier volume, otherwise the default Box component will be used.

<a id="unreal.DaySequenceModifierComponent.target_actor"></a>

#### target_actor

```python
@property
def target_actor() -> DaySequenceActor
```

(DaySequenceActor):  [Read-Write] Non-serialized target actor we are currently bound to

<a id="unreal.DaySequenceModifierComponent.target_actor"></a>

#### target_actor

```python
@target_actor.setter
def target_actor(value: DaySequenceActor) -> None
```

<a id="unreal.DaySequenceModifierComponent.volume_shape_components"></a>

#### volume_shape_components

```python
@property
def volume_shape_components() -> Array[ComponentReference]
```

(Array[ComponentReference]):  [Read-Write] When set, the shape components will be used for the modifier volume, otherwise the default Box component will be used.

<a id="unreal.DaySequenceModifierComponent.volume_shape_components"></a>

#### volume_shape_components

```python
@volume_shape_components.setter
def volume_shape_components(value: Array[ComponentReference]) -> None
```

<a id="unreal.DaySequenceModifierComponent.user_day_sequence"></a>

#### user_day_sequence

```python
@property
def user_day_sequence() -> DaySequence
```

(DaySequence):  [Read-Write] The user provided Day Sequence.

<a id="unreal.DaySequenceModifierComponent.user_day_sequence"></a>

#### user_day_sequence

```python
@user_day_sequence.setter
def user_day_sequence(value: DaySequence) -> None
```

<a id="unreal.DaySequenceModifierComponent.transient_sequence"></a>

#### transient_sequence

```python
@property
def transient_sequence() -> DaySequence
```

(DaySequence):  [Read-Write] The user provided Transient Day Sequence.

<a id="unreal.DaySequenceModifierComponent.transient_sequence"></a>

#### transient_sequence

```python
@transient_sequence.setter
def transient_sequence(value: DaySequence) -> None
```

<a id="unreal.DaySequenceModifierComponent.bias"></a>

#### bias

```python
@property
def bias() -> int
```

(int32):  [Read-Write] User-defined bias.

<a id="unreal.DaySequenceModifierComponent.bias"></a>

#### bias

```python
@bias.setter
def bias(value: int) -> None
```

<a id="unreal.DaySequenceModifierComponent.day_night_cycle_time"></a>

#### day_night_cycle_time

```python
@property
def day_night_cycle_time() -> float
```

(float):  [Read-Write] The time to use for the day/night cycle.

<a id="unreal.DaySequenceModifierComponent.day_night_cycle_time"></a>

#### day_night_cycle_time

```python
@day_night_cycle_time.setter
def day_night_cycle_time(value: float) -> None
```

<a id="unreal.DaySequenceModifierComponent.blend_amount"></a>

#### blend_amount

```python
@property
def blend_amount() -> float
```

(float):  [Read-Write] Defines the region in which the effective blend weight is in the range (0.0, 1.0) (not inclusive) when Mode == EDaySequenceModifierMode::Volume.

<a id="unreal.DaySequenceModifierComponent.blend_amount"></a>

#### blend_amount

```python
@blend_amount.setter
def blend_amount(value: float) -> None
```

<a id="unreal.DaySequenceModifierComponent.user_blend_weight"></a>

#### user_blend_weight

```python
@property
def user_blend_weight() -> float
```

(float):  [Read-Write] User specified blend weight. The final blend weight is determined by BlendPolicy.

<a id="unreal.DaySequenceModifierComponent.user_blend_weight"></a>

#### user_blend_weight

```python
@user_blend_weight.setter
def user_blend_weight(value: float) -> None
```

<a id="unreal.DaySequenceModifierComponent.day_night_cycle"></a>

#### day_night_cycle

```python
@property
def day_night_cycle() -> DayNightCycleMode
```

(DayNightCycleMode):  [Read-Write] Changes the way the modifier controls the day/night cycle time when enabled.

<a id="unreal.DaySequenceModifierComponent.day_night_cycle"></a>

#### day_night_cycle

```python
@day_night_cycle.setter
def day_night_cycle(value: DayNightCycleMode) -> None
```

<a id="unreal.DaySequenceModifierComponent.mode"></a>

#### mode

```python
@property
def mode() -> DaySequenceModifierMode
```

(DaySequenceModifierMode):  [Read-Write] Determines how the modifier computes InternalBlendWeight.

<a id="unreal.DaySequenceModifierComponent.mode"></a>

#### mode

```python
@mode.setter
def mode(value: DaySequenceModifierMode) -> None
```

<a id="unreal.DaySequenceModifierComponent.blend_policy"></a>

#### blend_policy

```python
@property
def blend_policy() -> DaySequenceModifierUserBlendPolicy
```

(DaySequenceModifierUserBlendPolicy):  [Read-Write] Determines how the modifier uses UserBlendWeight to compute effective blend weight.

<a id="unreal.DaySequenceModifierComponent.blend_policy"></a>

#### blend_policy

```python
@blend_policy.setter
def blend_policy(value: DaySequenceModifierUserBlendPolicy) -> None
```

<a id="unreal.DaySequenceModifierComponent.on_post_reinitialize_sub_sequences"></a>

#### on_post_reinitialize_sub_sequences

```python
@property
def on_post_reinitialize_sub_sequences() -> OnPostReinitializeSubSequences
```

(OnPostReinitializeSubSequences):  [Read-Write] Blueprint exposed delegate invoked after the component's subsequences are reinitialized.

<a id="unreal.DaySequenceModifierComponent.on_post_reinitialize_sub_sequences"></a>

#### on_post_reinitialize_sub_sequences

```python
@on_post_reinitialize_sub_sequences.setter
def on_post_reinitialize_sub_sequences(
        value: OnPostReinitializeSubSequences) -> None
```

<a id="unreal.DaySequenceModifierComponent.on_post_enable_modifier"></a>

#### on_post_enable_modifier

```python
@property
def on_post_enable_modifier() -> OnPostEnableModifier
```

(OnPostEnableModifier):  [Read-Write] Blueprint exposed delegate invoked after the modifier component is enabled.

<a id="unreal.DaySequenceModifierComponent.on_post_enable_modifier"></a>

#### on_post_enable_modifier

```python
@on_post_enable_modifier.setter
def on_post_enable_modifier(value: OnPostEnableModifier) -> None
```

<a id="unreal.DaySequenceModifierComponent.ignore_bias"></a>

#### ignore_bias

```python
@property
def ignore_bias() -> bool
```

(bool):  [Read-Write] When enabled, these overrides will always override all settings regardless of their bias.

<a id="unreal.DaySequenceModifierComponent.ignore_bias"></a>

#### ignore_bias

```python
@ignore_bias.setter
def ignore_bias(value: bool) -> None
```

<a id="unreal.DaySequenceModifierComponent.is_component_enabled"></a>

#### is_component_enabled

```python
@property
def is_component_enabled() -> bool
```

(bool):  [Read-Only] Flag used track whether or not this component is enabled or disabled.

<a id="unreal.DaySequenceModifierComponent.is_enabled"></a>

#### is_enabled

```python
@property
def is_enabled() -> bool
```

(bool):  [Read-Only] Non-serialized variable for tracking whether our overrides are enabled or not.

<a id="unreal.DaySequenceModifierComponent.preview"></a>

#### preview

```python
@property
def preview() -> bool
```

(bool):  [Read-Write] When enabled, preview this day sequence modifier in the editor.

<a id="unreal.DaySequenceModifierComponent.preview"></a>

#### preview

```python
@preview.setter
def preview(value: bool) -> None
```

<a id="unreal.DaySequenceModifierComponent.smooth_blending"></a>

#### smooth_blending

```python
@property
def smooth_blending() -> bool
```

(bool):  [Read-Write] If true, day sequence evaluation while within the blending region will be smooth. Note: Can be very expensive.

<a id="unreal.DaySequenceModifierComponent.smooth_blending"></a>

#### smooth_blending

```python
@smooth_blending.setter
def smooth_blending(value: bool) -> None
```

<a id="unreal.DaySequenceModifierComponent.unbind_from_day_sequence_actor"></a>

#### unbind_from_day_sequence_actor

```python
def unbind_from_day_sequence_actor() -> None
```

x.unbind_from_day_sequence_actor() -> None
Unbind this component from its day sequence actor if valid.
Will removes the sub-sequence from the root sequence if it's set up.

<a id="unreal.DaySequenceModifierComponent.set_blend_target"></a>

#### set_blend_target

```python
def set_blend_target(actor: PlayerController) -> None
```

x.set_blend_target(actor) -> None
Sets the blend target to use when in Volume mode.

Args:
    actor (PlayerController):

<a id="unreal.DaySequenceModifierComponent.get_blend_weight"></a>

#### get_blend_weight

```python
def get_blend_weight() -> float
```

x.get_blend_weight() -> float
Get the current blend weight.

Returns:
    float:

<a id="unreal.DaySequenceModifierComponent.enable_component"></a>

#### enable_component

```python
def enable_component() -> None
```

x.enable_component() -> None
Enable this component.

<a id="unreal.DaySequenceModifierComponent.disable_component"></a>

#### disable_component

```python
def disable_component() -> None
```

x.disable_component() -> None
Disable this component.
Will remove the sub-sequence from the root sequence if it's set up.

<a id="unreal.DaySequenceModifierComponent.bind_to_day_sequence_actor"></a>

#### bind_to_day_sequence_actor

```python
def bind_to_day_sequence_actor(day_sequence_actor: DaySequenceActor) -> None
```

x.bind_to_day_sequence_actor(day_sequence_actor) -> None
Bind this component to the specified day sequence actor.
Will not add our overrides to the sub-sequence until EnableModifier is called.

Args:
    day_sequence_actor (DaySequenceActor):

<a id="unreal.DaySequenceModifierVolume"></a>