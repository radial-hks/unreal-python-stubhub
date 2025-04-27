## VOIPTalker Objects

```python
class VOIPTalker(ActorComponent)
```

VOIPTalker

**C++ Source:**

- **Module**: Engine
- **File**: VoiceConfig.h

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
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``settings`` (VoiceSettings):  [Read-Write] Configurable settings for this player's voice. When set, this will update the next time the player speaks.

<a id="unreal.VOIPTalker.settings"></a>

#### settings

```python
@property
def settings() -> VoiceSettings
```

(VoiceSettings):  [Read-Write] Configurable settings for this player's voice. When set, this will update the next time the player speaks.

<a id="unreal.VOIPTalker.settings"></a>

#### settings

```python
@settings.setter
def settings(value: VoiceSettings) -> None
```

<a id="unreal.VOIPTalker.register_with_player_state"></a>

#### register_with_player_state

```python
def register_with_player_state(owning_state: PlayerState) -> None
```

x.register_with_player_state(owning_state) -> None
This function sets up this talker with a specific player.
It is necessary to use this to properly control a specific player's voice
and receive events.

Args:
    owning_state (PlayerState):

<a id="unreal.VOIPTalker.get_voice_level"></a>

#### get_voice_level

```python
def get_voice_level() -> float
```

x.get_voice_level() -> float
Get the current level of how loud this player is speaking. Will return 0.0
if player is not talking.

Returns:
    float:

<a id="unreal.VOIPTalker.create_talker_for_player"></a>

#### create_talker_for_player

```python
@classmethod
def create_talker_for_player(cls, owning_state: PlayerState) -> VOIPTalker
```

X.create_talker_for_player(owning_state) -> VOIPTalker
function for creating and registering a UVOIPTalker.

Args:
    owning_state (PlayerState): 

Returns:
    VOIPTalker:

<a id="unreal.VOIPTalker.bp_on_talking_end"></a>

#### bp_on_talking_end

```python
def bp_on_talking_end() -> None
```

x.bp_on_talking_end() -> None
Blueprint native event for when this player stops speaking.

<a id="unreal.VOIPTalker.bp_on_talking_begin"></a>

#### bp_on_talking_begin

```python
def bp_on_talking_begin(audio_component: AudioComponent) -> None
```

x.bp_on_talking_begin(audio_component) -> None
Blueprint native event for when this player starts speaking.

Args:
    audio_component (AudioComponent):

<a id="unreal.VOIPStatics"></a>