## WorldPartitionStreamingSourceComponent Objects

```python
class WorldPartitionStreamingSourceComponent(ActorComponent)
```

World Partition Streaming Source Component

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartitionStreamingSourceComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``debug_color`` (Color):  [Read-Write] Color used for debugging.
- ``default_visualizer_loading_range`` (float):  [Read-Write] Value used by debug visualizer when grid loading range is chosen.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``priority`` (StreamingSourcePriority):  [Read-Write]
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``shapes`` (Array[StreamingSourceShape]):  [Read-Write] Optional aggregated shape list used to build a custom shape for the streaming source. When empty, fallbacks sphere shape with a radius equal to grid's loading range.
- ``streaming_source_enabled`` (bool):  [Read-Write] Whether this component is enabled or not
- ``target_behavior`` (StreamingSourceTargetBehavior):  [Read-Write] When TargetGrids or TargetHLODLayers are specified, this indicates the behavior.
- ``target_grid`` (Name):  [Read-Write]
  deprecated: Use TargetGrids instead.
- ``target_grids`` (Array[Name]):  [Read-Write] Optional target grids affected by streaming source.
- ``target_hlod_layer`` (HLODLayer):  [Read-Write]
  deprecated: Use TargetHLODLayers instead.
- ``target_hlod_layers`` (Array[HLODLayer]):  [Read-Write] Optional target HLODLayers affected by the streaming source.
  deprecated: Use TargetGrids instead.
- ``target_state`` (StreamingSourceTargetState):  [Read-Write]

<a id="unreal.WorldPartitionStreamingSourceComponent.target_behavior"></a>

#### target_behavior

```python
@property
def target_behavior() -> StreamingSourceTargetBehavior
```

(StreamingSourceTargetBehavior):  [Read-Write] When TargetGrids or TargetHLODLayers are specified, this indicates the behavior.

<a id="unreal.WorldPartitionStreamingSourceComponent.target_behavior"></a>

#### target_behavior

```python
@target_behavior.setter
def target_behavior(value: StreamingSourceTargetBehavior) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.target_grids"></a>

#### target_grids

```python
@property
def target_grids() -> Array[Name]
```

(Array[Name]):  [Read-Write] Optional target grids affected by streaming source.

<a id="unreal.WorldPartitionStreamingSourceComponent.target_grids"></a>

#### target_grids

```python
@target_grids.setter
def target_grids(value: Array[Name]) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.target_grid"></a>

#### target_grid

```python
@property
def target_grid() -> Name
```

(Name):  [Read-Write]
deprecated: Use TargetGrids instead.

<a id="unreal.WorldPartitionStreamingSourceComponent.target_grid"></a>

#### target_grid

```python
@target_grid.setter
def target_grid(value: Name) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.target_hlod_layers"></a>

#### target_hlod_layers

```python
@property
def target_hlod_layers() -> Array[HLODLayer]
```

(Array[HLODLayer]):  [Read-Write] Optional target HLODLayers affected by the streaming source.
deprecated: Use TargetGrids instead.

<a id="unreal.WorldPartitionStreamingSourceComponent.target_hlod_layers"></a>

#### target_hlod_layers

```python
@target_hlod_layers.setter
def target_hlod_layers(value: Array[HLODLayer]) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.target_hlod_layer"></a>

#### target_hlod_layer

```python
@property
def target_hlod_layer() -> HLODLayer
```

(HLODLayer):  [Read-Write]
deprecated: Use TargetHLODLayers instead.

<a id="unreal.WorldPartitionStreamingSourceComponent.target_hlod_layer"></a>

#### target_hlod_layer

```python
@target_hlod_layer.setter
def target_hlod_layer(value: HLODLayer) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.shapes"></a>

#### shapes

```python
@property
def shapes() -> Array[StreamingSourceShape]
```

(Array[StreamingSourceShape]):  [Read-Write] Optional aggregated shape list used to build a custom shape for the streaming source. When empty, fallbacks sphere shape with a radius equal to grid's loading range.

<a id="unreal.WorldPartitionStreamingSourceComponent.shapes"></a>

#### shapes

```python
@shapes.setter
def shapes(value: Array[StreamingSourceShape]) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.priority"></a>

#### priority

```python
@property
def priority() -> StreamingSourcePriority
```

(StreamingSourcePriority):  [Read-Write]

<a id="unreal.WorldPartitionStreamingSourceComponent.priority"></a>

#### priority

```python
@priority.setter
def priority(value: StreamingSourcePriority) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.streaming_source_enabled"></a>

#### streaming_source_enabled

```python
@property
def streaming_source_enabled() -> bool
```

(bool):  [Read-Write] Whether this component is enabled or not

<a id="unreal.WorldPartitionStreamingSourceComponent.streaming_source_enabled"></a>

#### streaming_source_enabled

```python
@streaming_source_enabled.setter
def streaming_source_enabled(value: bool) -> None
```

<a id="unreal.WorldPartitionStreamingSourceComponent.is_streaming_source_enabled"></a>

#### is_streaming_source_enabled

```python
def is_streaming_source_enabled() -> bool
```

x.is_streaming_source_enabled() -> bool
Returns true if the component is active.

Returns:
    bool:

<a id="unreal.WorldPartitionStreamingSourceComponent.is_streaming_completed"></a>

#### is_streaming_completed

```python
def is_streaming_completed() -> bool
```

x.is_streaming_completed() -> bool
Returns true if streaming is completed for this streaming source component.

Returns:
    bool:

<a id="unreal.WorldPartitionStreamingSourceComponent.enable_streaming_source"></a>

#### enable_streaming_source

```python
def enable_streaming_source() -> None
```

x.enable_streaming_source() -> None
Enable the component

<a id="unreal.WorldPartitionStreamingSourceComponent.disable_streaming_source"></a>

#### disable_streaming_source

```python
def disable_streaming_source() -> None
```

x.disable_streaming_source() -> None
Disable the component

<a id="unreal.CurveTable"></a>