## MassAgentComponent Objects

```python
class MassAgentComponent(ActorComponent)
```

There are two primary use cases for this component:
1. If placed on an AActor blueprint it lets the user specify additional fragments that will be created for
   entities spawned based on this given blueprint.
2. If present on an actor in the world it makes it communicate with the MassSimulation which will create an
   entity representing given actor. Use case 1) will also be applicable in this case. The component is unregistered by
   default and requires manual enabling via a 'Enable' call.
todo: use case 2) is currently sitting in a shelved CL of mine. Will be worked on next.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassActors
- **File**: MassAgentComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_register_in_editor_mode`` (bool):  [Read-Write]
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``entity_config`` (MassEntityConfig):  [Read-Write]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.MassAgentComponent.kill_entity"></a>

#### kill\_entity

```python
def kill_entity(destroy_actor: bool) -> None
```

x.kill_entity(destroy_actor) -> None
Kill Entity

Args:
    destroy_actor (bool):

<a id="unreal.MassAgentComponent.enable"></a>

#### enable

```python
def enable() -> None
```

x.enable() -> None
Registers the component with the owner effectively turning it on. Calling it multiple times won't break anything

<a id="unreal.MassAgentComponent.disable"></a>

#### disable

```python
def disable() -> None
```

x.disable() -> None
Registers the component with the owner effectively turning it off

<a id="unreal.MassAgentSyncTrait"></a>