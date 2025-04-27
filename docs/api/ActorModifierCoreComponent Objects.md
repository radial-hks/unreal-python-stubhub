## ActorModifierCoreComponent Objects

```python
class ActorModifierCoreComponent(ActorComponent)
```

Component that contains a modifier stack and can be added on any actor

**C++ Source:**

- **Plugin**: ActorModifierCore
- **Module**: ActorModifierCore
- **File**: ActorModifierCoreComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``modifier_stack`` (ActorModifierCoreStack):  [Read-Only] This is the root stack that will contain all modifiers for this actor
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ActorModifierCoreComponent.get_modifier_stack"></a>

#### get_modifier_stack

```python
def get_modifier_stack() -> ActorModifierCoreStack
```

x.get_modifier_stack() -> ActorModifierCoreStack
Get Modifier Stack

Returns:
    ActorModifierCoreStack:

<a id="unreal.TagCollectionModifierComponent"></a>