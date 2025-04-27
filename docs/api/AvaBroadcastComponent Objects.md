## AvaBroadcastComponent Objects

```python
class AvaBroadcastComponent(ActorComponent)
```

Add this actor component to blueprint actor to expose the API to control the broadcasting
of channels in game.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaBroadcastComponent.h

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
- ``stop_broadcast_on_tear_down`` (bool):  [Read-Write] Automatically stop broadcast when the world this component is part of is torn down.

<a id="unreal.AvaBroadcastComponent.stop_broadcasting"></a>

#### stop_broadcasting

```python
def stop_broadcasting() -> bool
```

x.stop_broadcasting() -> bool
Stop broadcasting all channels.

Returns:
    bool:

<a id="unreal.AvaBroadcastComponent.start_broadcasting"></a>

#### start_broadcasting

```python
def start_broadcasting() -> Optional[str]
```

x.start_broadcasting() -> str or None
Start broadcasting all channels.
Returns true on partial success, i.e. will be true even if some channels didn't start.
Outputs error messages related to outputs that caused problems.

Returns:
    str or None: 

    out_error_message (str):

<a id="unreal.AvalancheBroadcastComponent"></a>