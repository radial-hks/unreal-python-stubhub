## ClusterUnionReplicatedProxyComponent Objects

```python
class ClusterUnionReplicatedProxyComponent(ActorComponent)
```

This component lets us store replicated information about how any particular UPrimitiveComponent
should be attached to its parent cluster union. The benefits of using a separate components are:

    1) It lets us avoid adding any additional overhead into the UPrimitiveComponent.
 2) It lets the replicated information have the same net relevancy as the actor being added to the cluster union
    rather than having the same net relevancy as the cluster union (i.e. in the case of replicating this data in
    an array in the ClusterUnionComponent).
 3) It lets us pinpoint what exactly is being added/removed (vs if all this data was stored in an array) which lets
    us be a bit more efficient in terms of modifying the cluster union.

**C++ Source:**

- **Module**: Engine
- **File**: ClusterUnionReplicatedProxyComponent.h

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

<a id="unreal.ConstraintInstanceBlueprintLibrary"></a>