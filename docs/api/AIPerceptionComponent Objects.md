## AIPerceptionComponent Objects

```python
class AIPerceptionComponent(ActorComponent)
```

AIPerceptionComponent is used to register as stimuli listener in AIPerceptionSystem
and gathers registered stimuli. UpdatePerception is called when component gets new stimuli (batched)

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``dominant_sense`` (type(Class)):  [Read-Write] Indicated sense that takes precedence over other senses when determining sensed actor's location.
      Should be set to one of the senses configured in SensesConfig, or None.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_perception_updated`` (PerceptionUpdatedDelegate):  [Read-Write] Might want to move these to special "BP_AIPerceptionComponent"
- ``on_target_perception_forgotten`` (ActorPerceptionForgetUpdatedDelegate):  [Read-Write] Notifies all bound delegates that the perception info has been forgotten for a given target.
  The notification get broadcast when all stimuli of a given target expire. Note that this
  functionality requires the the actor forgetting must be enabled via AIPerceptionSystem.bForgetStaleActors.
- ``on_target_perception_info_updated`` (ActorPerceptionInfoUpdatedDelegate):  [Read-Write] Notifies all bound objects that perception info has been updated for a given target.
  The notification is broadcast for any received stimulus or on change of state
  according to the stimulus configuration.

  Note - This delegate will be called even if source actor is no longer valid
  by the time a stimulus gets processed so it is better to use source id for bookkeeping.
- ``on_target_perception_updated`` (ActorPerceptionUpdatedDelegate):  [Read-Write] Notifies all bound objects that perception info has been updated for a given target.
  The notification is broadcast for any received stimulus or on change of state
  according to the stimulus configuration.

  Note - This delegate will not be called if source actor is no longer valid
  by the time a stimulus gets processed.
  Use OnTargetPerceptionInfoUpdated providing a source id to handle those cases.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``senses_config`` (Array[AISenseConfig]):  [Read-Write]

<a id="unreal.AIPerceptionComponent.on_perception_updated"></a>

#### on_perception_updated

```python
@property
def on_perception_updated() -> PerceptionUpdatedDelegate
```

(PerceptionUpdatedDelegate):  [Read-Write] Might want to move these to special "BP_AIPerceptionComponent"

<a id="unreal.AIPerceptionComponent.on_perception_updated"></a>

#### on_perception_updated

```python
@on_perception_updated.setter
def on_perception_updated(value: PerceptionUpdatedDelegate) -> None
```

<a id="unreal.AIPerceptionComponent.on_target_perception_forgotten"></a>

#### on_target_perception_forgotten

```python
@property
def on_target_perception_forgotten() -> ActorPerceptionForgetUpdatedDelegate
```

(ActorPerceptionForgetUpdatedDelegate):  [Read-Write] Notifies all bound delegates that the perception info has been forgotten for a given target.
The notification get broadcast when all stimuli of a given target expire. Note that this
functionality requires the the actor forgetting must be enabled via AIPerceptionSystem.bForgetStaleActors.

<a id="unreal.AIPerceptionComponent.on_target_perception_forgotten"></a>

#### on_target_perception_forgotten

```python
@on_target_perception_forgotten.setter
def on_target_perception_forgotten(
        value: ActorPerceptionForgetUpdatedDelegate) -> None
```

<a id="unreal.AIPerceptionComponent.on_target_perception_updated"></a>

#### on_target_perception_updated

```python
@property
def on_target_perception_updated() -> ActorPerceptionUpdatedDelegate
```

(ActorPerceptionUpdatedDelegate):  [Read-Write] Notifies all bound objects that perception info has been updated for a given target.
The notification is broadcast for any received stimulus or on change of state
according to the stimulus configuration.

Note - This delegate will not be called if source actor is no longer valid
by the time a stimulus gets processed.
Use OnTargetPerceptionInfoUpdated providing a source id to handle those cases.

<a id="unreal.AIPerceptionComponent.on_target_perception_updated"></a>

#### on_target_perception_updated

```python
@on_target_perception_updated.setter
def on_target_perception_updated(
        value: ActorPerceptionUpdatedDelegate) -> None
```

<a id="unreal.AIPerceptionComponent.on_target_perception_info_updated"></a>

#### on_target_perception_info_updated

```python
@property
def on_target_perception_info_updated() -> ActorPerceptionInfoUpdatedDelegate
```

(ActorPerceptionInfoUpdatedDelegate):  [Read-Write] Notifies all bound objects that perception info has been updated for a given target.
The notification is broadcast for any received stimulus or on change of state
according to the stimulus configuration.

Note - This delegate will be called even if source actor is no longer valid
by the time a stimulus gets processed so it is better to use source id for bookkeeping.

<a id="unreal.AIPerceptionComponent.on_target_perception_info_updated"></a>

#### on_target_perception_info_updated

```python
@on_target_perception_info_updated.setter
def on_target_perception_info_updated(
        value: ActorPerceptionInfoUpdatedDelegate) -> None
```

<a id="unreal.AIPerceptionComponent.set_sense_enabled"></a>

#### set_sense_enabled

```python
def set_sense_enabled(sense_class: Class, enable: bool) -> None
```

x.set_sense_enabled(sense_class, enable) -> None
Note that this works only if given sense has been already configured for
    this component instance

Args:
    sense_class (type(Class)): 
    enable (bool):

<a id="unreal.AIPerceptionComponent.request_stimuli_listener_update"></a>

#### request_stimuli_listener_update

```python
def request_stimuli_listener_update() -> None
```

x.request_stimuli_listener_update() -> None
Notifies AIPerceptionSystem to update properties for this "stimuli listener"

<a id="unreal.AIPerceptionComponent.is_sense_enabled"></a>

#### is_sense_enabled

```python
def is_sense_enabled(sense_class: Class) -> bool
```

x.is_sense_enabled(sense_class) -> bool
Returns if a sense is active. Note that this works only if given sense has been
     already configured for this component instance

Args:
    sense_class (type(Class)): 

Returns:
    bool:

<a id="unreal.AIPerceptionComponent.get_perceived_hostile_actors_by_sense"></a>

#### get_perceived_hostile_actors_by_sense

```python
def get_perceived_hostile_actors_by_sense(sense_to_use: Class) -> Array[Actor]
```

x.get_perceived_hostile_actors_by_sense(sense_to_use) -> Array[Actor]
Get Perceived Hostile Actors by Sense

Args:
    sense_to_use (type(Class)): 

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.AIPerceptionComponent.get_perceived_hostile_actors"></a>

#### get_perceived_hostile_actors

```python
def get_perceived_hostile_actors() -> Array[Actor]
```

x.get_perceived_hostile_actors() -> Array[Actor]
blueprint interface

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.AIPerceptionComponent.get_known_perceived_actors"></a>

#### get_known_perceived_actors

```python
def get_known_perceived_actors(sense_to_use: Class) -> Array[Actor]
```

x.get_known_perceived_actors(sense_to_use) -> Array[Actor]
If SenseToUse is none all actors ever perceived in any way (and not forgotten yet) will get fetched

Args:
    sense_to_use (type(Class)): 

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.AIPerceptionComponent.get_currently_perceived_actors"></a>

#### get_currently_perceived_actors

```python
def get_currently_perceived_actors(sense_to_use: Class) -> Array[Actor]
```

x.get_currently_perceived_actors(sense_to_use) -> Array[Actor]
If SenseToUse is none all actors currently perceived in any way will get fetched

Args:
    sense_to_use (type(Class)): 

Returns:
    Array[Actor]: 

    out_actors (Array[Actor]):

<a id="unreal.AIPerceptionComponent.get_actors_perception"></a>

#### get_actors_perception

```python
def get_actors_perception(
        actor: Actor) -> Optional[ActorPerceptionBlueprintInfo]
```

x.get_actors_perception(actor) -> ActorPerceptionBlueprintInfo or None
Retrieves whatever has been sensed about given actor

Args:
    actor (Actor): 

Returns:
    ActorPerceptionBlueprintInfo or None: 

    info (ActorPerceptionBlueprintInfo):

<a id="unreal.AIPerceptionComponent.forget_all"></a>

#### forget_all

```python
def forget_all() -> None
```

x.forget_all() -> None
basically cleans up PerceptualData, resulting in loss of all previous perception

<a id="unreal.AIPerceptionStimuliSourceComponent"></a>