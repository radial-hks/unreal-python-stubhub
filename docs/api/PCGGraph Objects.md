## PCGGraph Objects

```python
class PCGGraph(PCGGraphInterface)
```

PCGGraph

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Text):  [Read-Write]
- ``color`` (LinearColor):  [Read-Write] Override of the color for the subgraph node for this graph.
- ``debug_flag_applies_to_individual_components`` (bool):  [Read-Write] When true the Debug flag in the graph editor will display debug information contextually for the selected debug object. Otherwise
  debug information is displayed for all components using a graph (requires regenerate).
- ``description`` (Text):  [Read-Write]
- ``expose_to_library`` (bool):  [Read-Write]
- ``generation_radii`` (PCGRuntimeGenerationRadii):  [Read-Write]
- ``hi_gen_exponential`` (uint32):  [Read-Write] Shifts the grid sizes upwards based on the value, which allows to use larger grids. A value of 1 will effectively use the graph's Grid-400 values x 2 for the actual Grid-800 sizes and so on.
- ``hi_gen_grid_size`` (PCGHiGenGrid):  [Read-Write]
- ``ignore_landscape_tracking`` (bool):  [Read-Write] Marks the graph to be not refreshed automatically when the landscape changes, even if it is used.
- ``input_node`` (PCGNode):  [Read-Only] Add input/output nodes
- ``is_editor_only`` (bool):  [Read-Write] Sets whether this graph is marked as editor-only; note that the IsEditorOnly call depends on the local graph value and the value in all subgraphs, recursively.
- ``landscape_uses_metadata`` (bool):  [Read-Write]
- ``nodes`` (Array[PCGNode]):  [Read-Only]
- ``output_node`` (PCGNode):  [Read-Only]
- ``override_color`` (bool):  [Read-Write]
- ``override_title`` (bool):  [Read-Write]
- ``title`` (Text):  [Read-Write] Override of the title for the subgraph node for this graph.
- ``use2d_grid`` (bool):  [Read-Write]
- ``use_hierarchical_generation`` (bool):  [Read-Write]
- ``user_parameters`` (InstancedPropertyBag):  [Read-Write] Parameters

<a id="unreal.PCGGraph.category"></a>

#### category

```python
@property
def category() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PCGGraph.category"></a>

#### category

```python
@category.setter
def category(value: Text) -> None
```

<a id="unreal.PCGGraph.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PCGGraph.description"></a>

#### description

```python
@description.setter
def description(value: Text) -> None
```

<a id="unreal.PCGGraph.ignore_landscape_tracking"></a>

#### ignore_landscape_tracking

```python
@property
def ignore_landscape_tracking() -> bool
```

(bool):  [Read-Write] Marks the graph to be not refreshed automatically when the landscape changes, even if it is used.

<a id="unreal.PCGGraph.ignore_landscape_tracking"></a>

#### ignore_landscape_tracking

```python
@ignore_landscape_tracking.setter
def ignore_landscape_tracking(value: bool) -> None
```

<a id="unreal.PCGGraph.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[PCGNode]
```

(Array[PCGNode]):  [Read-Only]

<a id="unreal.PCGGraph.input_node"></a>

#### input_node

```python
@property
def input_node() -> PCGNode
```

(PCGNode):  [Read-Only] Add input/output nodes

<a id="unreal.PCGGraph.output_node"></a>

#### output_node

```python
@property
def output_node() -> PCGNode
```

(PCGNode):  [Read-Only]

<a id="unreal.PCGGraph.is_editor_only"></a>

#### is_editor_only

```python
@property
def is_editor_only() -> bool
```

(bool):  [Read-Write] Sets whether this graph is marked as editor-only; note that the IsEditorOnly call depends on the local graph value and the value in all subgraphs, recursively.

<a id="unreal.PCGGraph.is_editor_only"></a>

#### is_editor_only

```python
@is_editor_only.setter
def is_editor_only(value: bool) -> None
```

<a id="unreal.PCGGraph.generation_radii"></a>

#### generation_radii

```python
@property
def generation_radii() -> PCGRuntimeGenerationRadii
```

(PCGRuntimeGenerationRadii):  [Read-Write]

<a id="unreal.PCGGraph.generation_radii"></a>

#### generation_radii

```python
@generation_radii.setter
def generation_radii(value: PCGRuntimeGenerationRadii) -> None
```

<a id="unreal.PCGGraph.remove_nodes"></a>

#### remove_nodes

```python
def remove_nodes() -> Array[PCGNode]
```

x.remove_nodes() -> Array[PCGNode]
Bulk removal of nodes, to avoid notifying the world everytime.

Returns:
    Array[PCGNode]: 

    nodes (Array[PCGNode]):

<a id="unreal.PCGGraph.remove_node"></a>

#### remove_node

```python
def remove_node(node: PCGNode) -> None
```

x.remove_node(node) -> None
Removes a node from the graph.

Args:
    node (PCGNode):

<a id="unreal.PCGGraph.remove_edge"></a>

#### remove_edge

```python
def remove_edge(from_: PCGNode, from_label: Name, to: PCGNode,
                to_label: Name) -> bool
```

x.remove_edge(from_, from_label, to, to_label) -> bool
Removes an edge in the graph. Returns true if an edge was removed.

Args:
    from_ (PCGNode): 
    from_label (Name): 
    to (PCGNode): 
    to_label (Name): 

Returns:
    bool:

<a id="unreal.PCGGraph.get_output_node"></a>

#### get_output_node

```python
def get_output_node() -> PCGNode
```

x.get_output_node() -> PCGNode
Returns the graph output node

Returns:
    PCGNode:

<a id="unreal.PCGGraph.get_input_node"></a>

#### get_input_node

```python
def get_input_node() -> PCGNode
```

x.get_input_node() -> PCGNode
Returns the graph input node

Returns:
    PCGNode:

<a id="unreal.PCGGraph.force_notification_for_editor"></a>

#### force_notification_for_editor

```python
def force_notification_for_editor(
        change_type: PCGChangeType = PCGChangeType.STRUCTURAL) -> None
```

x.force_notification_for_editor(change_type=PCGChangeType.STRUCTURAL) -> None
Force Notification for Editor

Args:
    change_type (PCGChangeType):

<a id="unreal.PCGGraph.add_node_of_type"></a>

#### add_node_of_type

```python
def add_node_of_type(settings_class: Class) -> Tuple[PCGNode, PCGSettings]
```

x.add_node_of_type(settings_class) -> (PCGNode, default_node_settings=PCGSettings)
Creates a default node based on the settings class wanted. Returns the newly created node.

Args:
    settings_class (type(Class)): 

Returns:
    PCGSettings: 

    default_node_settings (PCGSettings):

<a id="unreal.PCGGraph.add_node_instance"></a>

#### add_node_instance

```python
def add_node_instance(settings: PCGSettings) -> PCGNode
```

x.add_node_instance(settings) -> PCGNode
Creates a node containing an instance to the given settings. Returns the created node.

Args:
    settings (PCGSettings): 

Returns:
    PCGNode:

<a id="unreal.PCGGraph.add_node_copy"></a>

#### add_node_copy

```python
def add_node_copy(settings: PCGSettings) -> Tuple[PCGNode, PCGSettings]
```

x.add_node_copy(settings) -> (PCGNode, default_node_settings=PCGSettings)
Creates a node and copies the input settings. Returns the created node.

Args:
    settings (PCGSettings): 

Returns:
    PCGSettings: 

    default_node_settings (PCGSettings):

<a id="unreal.PCGGraph.add_edge"></a>

#### add_edge

```python
def add_edge(from_: PCGNode, from_pin_label: Name, to: PCGNode,
             to_pin_label: Name) -> PCGNode
```

x.add_edge(from_, from_pin_label, to, to_pin_label) -> PCGNode
Adds a directed edge in the graph. Returns the "To" node for easy chaining

Args:
    from_ (PCGNode): 
    from_pin_label (Name): 
    to (PCGNode): 
    to_pin_label (Name): 

Returns:
    PCGNode:

<a id="unreal.PCGGraphInstance"></a>