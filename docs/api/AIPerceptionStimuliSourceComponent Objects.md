## AIPerceptionStimuliSourceComponent Objects

```python
class AIPerceptionStimuliSourceComponent(ActorComponent)
```

Gives owning actor a way to auto-register as perception system's sense stimuli source

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionStimuliSourceComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_register_as_source`` (bool):  [Read-Write]
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``register_as_source_for_senses`` (Array[type(Class)]):  [Read-Write]
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.AIPerceptionStimuliSourceComponent.auto_register_as_source"></a>

#### auto_register_as_source

```python
@property
def auto_register_as_source() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AIPerceptionStimuliSourceComponent.register_as_source_for_senses"></a>

#### register_as_source_for_senses

```python
@property
def register_as_source_for_senses() -> Array[Class]
```

(Array[type(Class)]):  [Read-Only]

<a id="unreal.AIPerceptionStimuliSourceComponent.unregister_from_sense"></a>

#### unregister_from_sense

```python
def unregister_from_sense(sense_class: Class) -> None
```

x.unregister_from_sense(sense_class) -> None
Unregisters owning actor from sources list of a specified sense class

Args:
    sense_class (type(Class)):

<a id="unreal.AIPerceptionStimuliSourceComponent.unregister_from_perception_system"></a>

#### unregister_from_perception_system

```python
def unregister_from_perception_system() -> None
```

x.unregister_from_perception_system() -> None
Unregister owning actor from being a source of sense stimuli

<a id="unreal.AIPerceptionStimuliSourceComponent.register_with_perception_system"></a>

#### register_with_perception_system

```python
def register_with_perception_system() -> None
```

x.register_with_perception_system() -> None
Registers owning actor as source of stimuli for senses specified in RegisterAsSourceForSenses.
    Note that you don't have to do it if bAutoRegisterAsSource == true

<a id="unreal.AIPerceptionStimuliSourceComponent.register_for_sense"></a>

#### register_for_sense

```python
def register_for_sense(sense_class: Class) -> None
```

x.register_for_sense(sense_class) -> None
Registers owning actor as source for specified sense class

Args:
    sense_class (type(Class)):

<a id="unreal.AIPerceptionSystem"></a>