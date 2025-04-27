## PCGComponent Objects

```python
class PCGComponent(ActorComponent)
```

PCGComponent

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``activated`` (bool):  [Read-Write]
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``current_editing_mode`` (PCGEditorDirtyMode):  [Read-Write] Current editing mode that depends on the serialized editing mode and loading. If the component is set to GenerateAtRuntime, this will behave as Preview.
- ``dirty_generated`` (bool):  [Read-Only]
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``generate_on_drop_when_trigger_on_demand`` (bool):  [Read-Write] When Generation Trigger is OnDemand, we can still force the component to generate on drop.
- ``generated`` (bool):  [Read-Only] Flag to indicate whether this component has run in the editor. Note that for partitionable actors, this will always be false.
- ``generated_graph_output`` (PCGDataCollection):  [Read-Only]
- ``generation_grid_size`` (uint32):  [Read-Only]
- ``generation_in_progress`` (bool):  [Read-Only]
- ``generation_radii`` (PCGRuntimeGenerationRadii):  [Read-Write]
- ``generation_trigger`` (PCGComponentGenerationTrigger):  [Read-Write]
- ``graph_instance`` (PCGGraphInstance):  [Read-Only]
- ``ignore_landscape_tracking`` (bool):  [Read-Write] Marks the component to be not refreshed automatically when the landscape changes, even if it is used.
- ``input_type`` (PCGComponentInput):  [Read-Write]
- ``is_component_local`` (bool):  [Read-Only]
- ``is_component_partitioned`` (bool):  [Read-Write] Will partition the component in a grid, dispatching the generation to multiple local components. Grid size is determined by the
  PCGWorldActor unless the graph has Hierarchical Generation enabled, in which case grid sizes are determined by the graph.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``last_generated_bounds`` (Box):  [Read-Only]
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_pcg_graph_cancelled_external`` (OnPCGGraphCancelledExternal):  [Read-Write] Event dispatched when a graph cancels generation on this component.
- ``on_pcg_graph_cleaned_external`` (OnPCGGraphCleanedExternal):  [Read-Write] Event dispatched when a graph cleans on this component.
- ``on_pcg_graph_generated_external`` (OnPCGGraphGeneratedExternal):  [Read-Write] Event dispatched when a graph completes its generation on this component.
- ``on_pcg_graph_start_generating_external`` (OnPCGGraphStartGeneratingExternal):  [Read-Write] Event dispatched when a graph begins generation on this component.
- ``only_track_itself`` (bool):  [Read-Write] Even if the graph has external dependencies, the component won't react to them.
- ``override_generation_radii`` (bool):  [Read-Write] Manual overrides for the graph generation radii and cleanup radius multiplier.
- ``parse_actor_components`` (bool):  [Read-Write]
- ``per_pin_generated_output`` (Map[str, PCGDataCollection]):  [Read-Only] If any graph edges cross execution grid sizes, data on the edge is stored / retrieved from this map.
- ``post_generate_function_names`` (Array[Name]):  [Read-Write] Can specify a list of functions from the owner of this component to be called when generation is done, in order.
   Need to take (and only take) a PCGDataCollection as parameter and with "CallInEditor" flag enabled.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``regenerate_in_editor`` (bool):  [Read-Write]
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``scheduling_policy`` (PCGSchedulingPolicyBase):  [Read-Only] This is the instanced UPCGSchedulingPolicy object which holds scheduling parameters and calculates priorities.
- ``scheduling_policy_class`` (type(Class)):  [Read-Write] A Scheduling Policy dictates the order in which instances of this component will be scheduled.
- ``seed`` (int32):  [Read-Write]
- ``serialized_editing_mode`` (PCGEditorDirtyMode):  [Read-Only]

<a id="unreal.PCGComponent.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGComponent.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.PCGComponent.activated"></a>

#### activated

```python
@property
def activated() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGComponent.activated"></a>

#### activated

```python
@activated.setter
def activated(value: bool) -> None
```

<a id="unreal.PCGComponent.is_component_partitioned"></a>

#### is_component_partitioned

```python
@property
def is_component_partitioned() -> bool
```

(bool):  [Read-Write] Will partition the component in a grid, dispatching the generation to multiple local components. Grid size is determined by the
PCGWorldActor unless the graph has Hierarchical Generation enabled, in which case grid sizes are determined by the graph.

<a id="unreal.PCGComponent.is_component_partitioned"></a>

#### is_component_partitioned

```python
@is_component_partitioned.setter
def is_component_partitioned(value: bool) -> None
```

<a id="unreal.PCGComponent.generation_trigger"></a>

#### generation_trigger

```python
@property
def generation_trigger() -> PCGComponentGenerationTrigger
```

(PCGComponentGenerationTrigger):  [Read-Only]

<a id="unreal.PCGComponent.generate_on_drop_when_trigger_on_demand"></a>

#### generate_on_drop_when_trigger_on_demand

```python
@property
def generate_on_drop_when_trigger_on_demand() -> bool
```

(bool):  [Read-Only] When Generation Trigger is OnDemand, we can still force the component to generate on drop.

<a id="unreal.PCGComponent.override_generation_radii"></a>

#### override_generation_radii

```python
@property
def override_generation_radii() -> bool
```

(bool):  [Read-Write] Manual overrides for the graph generation radii and cleanup radius multiplier.

<a id="unreal.PCGComponent.override_generation_radii"></a>

#### override_generation_radii

```python
@override_generation_radii.setter
def override_generation_radii(value: bool) -> None
```

<a id="unreal.PCGComponent.generation_radii"></a>

#### generation_radii

```python
@property
def generation_radii() -> PCGRuntimeGenerationRadii
```

(PCGRuntimeGenerationRadii):  [Read-Write]

<a id="unreal.PCGComponent.generation_radii"></a>

#### generation_radii

```python
@generation_radii.setter
def generation_radii(value: PCGRuntimeGenerationRadii) -> None
```

<a id="unreal.PCGComponent.scheduling_policy_class"></a>

#### scheduling_policy_class

```python
@property
def scheduling_policy_class() -> Class
```

(type(Class)):  [Read-Only] A Scheduling Policy dictates the order in which instances of this component will be scheduled.

<a id="unreal.PCGComponent.scheduling_policy"></a>

#### scheduling_policy

```python
@property
def scheduling_policy() -> PCGSchedulingPolicyBase
```

(PCGSchedulingPolicyBase):  [Read-Only] This is the instanced UPCGSchedulingPolicy object which holds scheduling parameters and calculates priorities.

<a id="unreal.PCGComponent.regenerate_in_editor"></a>

#### regenerate_in_editor

```python
@property
def regenerate_in_editor() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGComponent.regenerate_in_editor"></a>

#### regenerate_in_editor

```python
@regenerate_in_editor.setter
def regenerate_in_editor(value: bool) -> None
```

<a id="unreal.PCGComponent.only_track_itself"></a>

#### only_track_itself

```python
@property
def only_track_itself() -> bool
```

(bool):  [Read-Write] Even if the graph has external dependencies, the component won't react to them.

<a id="unreal.PCGComponent.only_track_itself"></a>

#### only_track_itself

```python
@only_track_itself.setter
def only_track_itself(value: bool) -> None
```

<a id="unreal.PCGComponent.ignore_landscape_tracking"></a>

#### ignore_landscape_tracking

```python
@property
def ignore_landscape_tracking() -> bool
```

(bool):  [Read-Write] Marks the component to be not refreshed automatically when the landscape changes, even if it is used.

<a id="unreal.PCGComponent.ignore_landscape_tracking"></a>

#### ignore_landscape_tracking

```python
@ignore_landscape_tracking.setter
def ignore_landscape_tracking(value: bool) -> None
```

<a id="unreal.PCGComponent.dirty_generated"></a>

#### dirty_generated

```python
@property
def dirty_generated() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PCGComponent.on_pcg_graph_start_generating_external"></a>

#### on_pcg_graph_start_generating_external

```python
@property
def on_pcg_graph_start_generating_external(
) -> OnPCGGraphStartGeneratingExternal
```

(OnPCGGraphStartGeneratingExternal):  [Read-Write] Event dispatched when a graph begins generation on this component.

<a id="unreal.PCGComponent.on_pcg_graph_start_generating_external"></a>

#### on_pcg_graph_start_generating_external

```python
@on_pcg_graph_start_generating_external.setter
def on_pcg_graph_start_generating_external(
        value: OnPCGGraphStartGeneratingExternal) -> None
```

<a id="unreal.PCGComponent.on_pcg_graph_cancelled_external"></a>

#### on_pcg_graph_cancelled_external

```python
@property
def on_pcg_graph_cancelled_external() -> OnPCGGraphCancelledExternal
```

(OnPCGGraphCancelledExternal):  [Read-Write] Event dispatched when a graph cancels generation on this component.

<a id="unreal.PCGComponent.on_pcg_graph_cancelled_external"></a>

#### on_pcg_graph_cancelled_external

```python
@on_pcg_graph_cancelled_external.setter
def on_pcg_graph_cancelled_external(
        value: OnPCGGraphCancelledExternal) -> None
```

<a id="unreal.PCGComponent.on_pcg_graph_generated_external"></a>

#### on_pcg_graph_generated_external

```python
@property
def on_pcg_graph_generated_external() -> OnPCGGraphGeneratedExternal
```

(OnPCGGraphGeneratedExternal):  [Read-Write] Event dispatched when a graph completes its generation on this component.

<a id="unreal.PCGComponent.on_pcg_graph_generated_external"></a>

#### on_pcg_graph_generated_external

```python
@on_pcg_graph_generated_external.setter
def on_pcg_graph_generated_external(
        value: OnPCGGraphGeneratedExternal) -> None
```

<a id="unreal.PCGComponent.on_pcg_graph_cleaned_external"></a>

#### on_pcg_graph_cleaned_external

```python
@property
def on_pcg_graph_cleaned_external() -> OnPCGGraphCleanedExternal
```

(OnPCGGraphCleanedExternal):  [Read-Write] Event dispatched when a graph cleans on this component.

<a id="unreal.PCGComponent.on_pcg_graph_cleaned_external"></a>

#### on_pcg_graph_cleaned_external

```python
@on_pcg_graph_cleaned_external.setter
def on_pcg_graph_cleaned_external(value: OnPCGGraphCleanedExternal) -> None
```

<a id="unreal.PCGComponent.generated"></a>

#### generated

```python
@property
def generated() -> bool
```

(bool):  [Read-Only] Flag to indicate whether this component has run in the editor. Note that for partitionable actors, this will always be false.

<a id="unreal.PCGComponent.post_generate_function_names"></a>

#### post_generate_function_names

```python
@property
def post_generate_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Can specify a list of functions from the owner of this component to be called when generation is done, in order.
 Need to take (and only take) a PCGDataCollection as parameter and with "CallInEditor" flag enabled.

<a id="unreal.PCGComponent.post_generate_function_names"></a>

#### post_generate_function_names

```python
@post_generate_function_names.setter
def post_generate_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGComponent.graph_instance"></a>

#### graph_instance

```python
@property
def graph_instance() -> PCGGraphInstance
```

(PCGGraphInstance):  [Read-Only]

<a id="unreal.PCGComponent.input_type"></a>

#### input_type

```python
@property
def input_type() -> PCGComponentInput
```

(PCGComponentInput):  [Read-Write]

<a id="unreal.PCGComponent.input_type"></a>

#### input_type

```python
@input_type.setter
def input_type(value: PCGComponentInput) -> None
```

<a id="unreal.PCGComponent.parse_actor_components"></a>

#### parse_actor_components

```python
@property
def parse_actor_components() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGComponent.parse_actor_components"></a>

#### parse_actor_components

```python
@parse_actor_components.setter
def parse_actor_components(value: bool) -> None
```

<a id="unreal.PCGComponent.set_graph"></a>

#### set_graph

```python
def set_graph(graph: PCGGraphInterface) -> None
```

x.set_graph(graph) -> None
Set Graph

Args:
    graph (PCGGraphInterface):

<a id="unreal.PCGComponent.set_editing_mode"></a>

#### set_editing_mode

```python
def set_editing_mode(editing_mode: PCGEditorDirtyMode,
                     serialized_editing_mode: PCGEditorDirtyMode) -> None
```

x.set_editing_mode(editing_mode, serialized_editing_mode) -> None
Set Editing Mode

Args:
    editing_mode (PCGEditorDirtyMode): 
    serialized_editing_mode (PCGEditorDirtyMode):

<a id="unreal.PCGComponent.notify_properties_changed_from_blueprint"></a>

#### notify_properties_changed_from_blueprint

```python
def notify_properties_changed_from_blueprint() -> None
```

x.notify_properties_changed_from_blueprint() -> None
Notify properties changed, used in runtime cases, will dirty & trigger a regeneration if needed

<a id="unreal.PCGComponent.get_serialized_editing_mode"></a>

#### get_serialized_editing_mode

```python
def get_serialized_editing_mode() -> PCGEditorDirtyMode
```

x.get_serialized_editing_mode() -> PCGEditorDirtyMode
Get Serialized Editing Mode

Returns:
    PCGEditorDirtyMode:

<a id="unreal.PCGComponent.get_generated_graph_output"></a>

#### get_generated_graph_output

```python
def get_generated_graph_output() -> PCGDataCollection
```

x.get_generated_graph_output() -> PCGDataCollection
Retrieves generated data

Returns:
    PCGDataCollection:

<a id="unreal.PCGComponent.get_editing_mode"></a>

#### get_editing_mode

```python
def get_editing_mode() -> PCGEditorDirtyMode
```

x.get_editing_mode() -> PCGEditorDirtyMode
Returns the current editing mode

Returns:
    PCGEditorDirtyMode:

<a id="unreal.PCGComponent.generate_local"></a>

#### generate_local

```python
def generate_local(force: bool) -> None
```

x.generate_local(force) -> None
Starts generation from a local (vs. remote) standpoint. Will not be replicated. Will be delayed.

Args:
    force (bool):

<a id="unreal.PCGComponent.generate"></a>

#### generate

```python
def generate(force: bool) -> None
```

x.generate(force) -> None
Networked generation call that also activates the component as needed

Args:
    force (bool):

<a id="unreal.PCGComponent.clear_pcg_link"></a>

#### clear_pcg_link

```python
def clear_pcg_link(template_actor: Class = None) -> Actor
```

x.clear_pcg_link(template_actor=None) -> Actor
Move all generated resources under a new actor, following a template (AActor if not provided), clearing all link to this PCG component. Returns the new actor.

Args:
    template_actor (type(Class)): 

Returns:
    Actor:

<a id="unreal.PCGComponent.cleanup_local"></a>

#### cleanup_local

```python
def cleanup_local(remove_components: bool, save: bool = False) -> None
```

x.cleanup_local(remove_components, save=False) -> None
Cleans up the generation from a local (vs. remote) standpoint. Will not be replicated. Will be delayed.

Args:
    remove_components (bool): 
    save (bool):

<a id="unreal.PCGComponent.cleanup"></a>

#### cleanup

```python
def cleanup(remove_components: bool, save: bool = False) -> None
```

x.cleanup(remove_components, save=False) -> None
Networked cleanup call

Args:
    remove_components (bool): 
    save (bool):

<a id="unreal.PCGComponent.add_to_managed_resources"></a>

#### add_to_managed_resources

```python
def add_to_managed_resources(resource: PCGManagedResource) -> None
```

x.add_to_managed_resources(resource) -> None
Registers some managed resource to the current component

Args:
    resource (PCGManagedResource):

<a id="unreal.PCGComponent.add_components_to_managed_resources"></a>

#### add_components_to_managed_resources

```python
def add_components_to_managed_resources(
        components: Array[ActorComponent]) -> None
```

x.add_components_to_managed_resources(components) -> None
Creates a managed component resource and adds it to the current component. Note: in native code, consider using the explicit creation especially if there are special resource objects involved.

Args:
    components (Array[ActorComponent]):

<a id="unreal.PCGComponent.add_actors_to_managed_resources"></a>

#### add_actors_to_managed_resources

```python
def add_actors_to_managed_resources(actors: Array[Actor]) -> None
```

x.add_actors_to_managed_resources(actors) -> None
Creates a managed actors resource and adds it to the current component. Note: in native code, consider using the explicit creation especially if there are special resource objects involved.

Args:
    actors (Array[Actor]):

<a id="unreal.PCGComponent.refresh_pcg_runtime_component"></a>

#### refresh_pcg_runtime_component

```python
def refresh_pcg_runtime_component(flush_cache: bool = False) -> None
```

x.refresh_pcg_runtime_component(flush_cache=False) -> None
Refresh a component set to Generate At Runtime, if some parameters changed. Can also flush the cache.

Args:
    flush_cache (bool):

<a id="unreal.PCGBlueprintHelpers"></a>