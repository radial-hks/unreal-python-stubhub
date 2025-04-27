## ActorSequenceComponent Objects

```python
class ActorSequenceComponent(ActorComponent)
```

Movie scene animation embedded within an actor.

**C++ Source:**

- **Plugin**: ActorSequence
- **Module**: ActorSequence
- **File**: ActorSequenceComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``playback_settings`` (MovieSceneSequencePlaybackSettings):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``sequence`` (ActorSequence):  [Read-Write] Embedded actor sequence data
- ``sequence_player`` (ActorSequencePlayer):  [Read-Write]

<a id="unreal.ActorSequenceComponent.sequence_player"></a>

#### sequence_player

```python
@property
def sequence_player() -> ActorSequencePlayer
```

(ActorSequencePlayer):  [Read-Only]

<a id="unreal.ActorSequenceComponent.stop_sequence"></a>

#### stop_sequence

```python
def stop_sequence() -> None
```

x.stop_sequence() -> None
Calls the Stop function on the SequencePlayer if its valid.

<a id="unreal.ActorSequenceComponent.play_sequence"></a>

#### play_sequence

```python
def play_sequence() -> None
```

x.play_sequence() -> None
Calls the Play function on the SequencePlayer if its valid.

<a id="unreal.ActorSequenceComponent.pause_sequence"></a>

#### pause_sequence

```python
def pause_sequence() -> None
```

x.pause_sequence() -> None
Calls the Pause function on the SequencePlayer if its valid.

<a id="unreal.ActorSequencePlayer"></a>