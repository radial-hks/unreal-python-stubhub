## PropertyAnimatorCoreComponent Objects

```python
class PropertyAnimatorCoreComponent(ActorComponent)
```

A container for controllers that holds properties in this actor

**C++ Source:**

- **Plugin**: PropertyAnimatorCore
- **Module**: PropertyAnimatorCore
- **File**: PropertyAnimatorCoreComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_animators_time_source`` (PropertyAnimatorCoreTimeSourceBase):  [Read-Only] Active time source with its options, determined by its name
- ``animators_enabled`` (bool):  [Read-Write] Global state for all animators controlled by this component
- ``animators_magnitude`` (float):  [Read-Write] Global magnitude for all animators controlled by this component
- ``animators_time_source_name`` (Name):  [Read-Write] The global time source to use, can be overriden in animator
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
- ``property_animators`` (Array[PropertyAnimatorCoreBase]):  [Read-Write] Animators linked to this actor, they contain only properties within this actor
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.PropertyAnimatorCoreComponent.property_animators"></a>

#### property_animators

```python
@property
def property_animators() -> Array[PropertyAnimatorCoreBase]
```

(Array[PropertyAnimatorCoreBase]):  [Read-Write] Animators linked to this actor, they contain only properties within this actor

<a id="unreal.PropertyAnimatorCoreComponent.property_animators"></a>

#### property_animators

```python
@property_animators.setter
def property_animators(value: Array[PropertyAnimatorCoreBase]) -> None
```

<a id="unreal.CustomPropertyControlComponent"></a>