## ComputeGraphComponent Objects

```python
class ComputeGraphComponent(ActorComponent)
```

Component which holds a context for a UComputeGraph.
This object binds the graph to its data providers, and queues the execution.

**C++ Source:**

- **Plugin**: ComputeFramework
- **Module**: ComputeFramework
- **File**: ComputeGraphComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``compute_graph`` (ComputeGraph):  [Read-Write] The Compute Graph asset.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ComputeGraphComponent.compute_graph"></a>

#### compute_graph

```python
@property
def compute_graph() -> ComputeGraph
```

(ComputeGraph):  [Read-Write] The Compute Graph asset.

<a id="unreal.ComputeGraphComponent.compute_graph"></a>

#### compute_graph

```python
@compute_graph.setter
def compute_graph(value: ComputeGraph) -> None
```

<a id="unreal.ComputeGraphComponent.queue_execute"></a>

#### queue_execute

```python
def queue_execute() -> None
```

x.queue_execute() -> None
Queue the graph for execution at the next render update.

<a id="unreal.ComputeGraphComponent.destroy_data_providers"></a>

#### destroy_data_providers

```python
def destroy_data_providers() -> None
```

x.destroy_data_providers() -> None
Destroy all associated DataProvider objects.

<a id="unreal.ComputeGraphComponent.create_data_providers"></a>

#### create_data_providers

```python
def create_data_providers(binding_index: int, binding_object: Object) -> None
```

x.create_data_providers(binding_index, binding_object) -> None
Create all the Data Provider objects for a given binding object of the ComputeGraph.

Args:
    binding_index (int32): 
    binding_object (Object):

<a id="unreal.ComputeKernel"></a>