## MovieGraphConfig Objects

```python
class MovieGraphConfig(Object)
```

This is the runtime representation of the UMoviePipelineEdGraph which contains the actual strongly
typed graph network that is read by the MoviePipeline. There is an editor-only representation of
this graph (UMoviePipelineEdGraph).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphConfig.h

<a id="unreal.MovieGraphConfig.update_global_variable_values"></a>

#### update_global_variable_values

```python
def update_global_variable_values(pipeline: MovieGraphPipeline) -> None
```

x.update_global_variable_values(pipeline) -> None
Updates the values of all global variables.

Args:
    pipeline (MovieGraphPipeline):

<a id="unreal.MovieGraphConfig.remove_outbound_edges"></a>

#### remove_outbound_edges

```python
def remove_outbound_edges(node: MovieGraphNode, pin_name: Name) -> bool
```

x.remove_outbound_edges(node, pin_name) -> bool
Convinence function which removes all Outobund (pins on the right side of a node) edges connected to the given outbound pin by name, for the given node.

Args:
    node (MovieGraphNode): 
    pin_name (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.remove_nodes"></a>

#### remove_nodes

```python
def remove_nodes(nodes: Array[MovieGraphNode]) -> bool
```

x.remove_nodes(nodes) -> bool
Like RemoveNode but takes an entire array at once for convinence.

Args:
    nodes (Array[MovieGraphNode]): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.remove_node"></a>

#### remove_node

```python
def remove_node(node: MovieGraphNode) -> bool
```

x.remove_node(node) -> bool
Removes the specified node from the graph, disconnecting connected edges as it goes.

Args:
    node (MovieGraphNode): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.remove_labeled_edge"></a>

#### remove_labeled_edge

```python
def remove_labeled_edge(from_node: MovieGraphNode, from_pin_name: Name,
                        to_node: MovieGraphNode, to_pin_name: Name) -> bool
```

x.remove_labeled_edge(from_node, from_pin_name, to_node, to_pin_name) -> bool
Like AddLabeledEdge, removes the given connection between Node A and Node B (for the specified pins by name).

Args:
    from_node (MovieGraphNode): 
    from_pin_name (Name): 
    to_node (MovieGraphNode): 
    to_pin_name (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.remove_inbound_edges"></a>

#### remove_inbound_edges

```python
def remove_inbound_edges(node: MovieGraphNode, pin_name: Name) -> bool
```

x.remove_inbound_edges(node, pin_name) -> bool
Convinence function which removes all Inbound (pins on the left side of a node) edges connected to the given inbound pin by name, for the given node.

Args:
    node (MovieGraphNode): 
    pin_name (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.remove_all_outbound_edges"></a>

#### remove_all_outbound_edges

```python
def remove_all_outbound_edges(node: MovieGraphNode) -> bool
```

x.remove_all_outbound_edges(node) -> bool
Convinence function which removes all Outbound (pins on the right side of a node) edges for the given node.

Args:
    node (MovieGraphNode): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.remove_all_inbound_edges"></a>

#### remove_all_inbound_edges

```python
def remove_all_inbound_edges(node: MovieGraphNode) -> bool
```

x.remove_all_inbound_edges(node) -> bool
Convinence function which removes all Inbound (pins on the left side of a node) edges for the given node.

Args:
    node (MovieGraphNode): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.get_variables"></a>

#### get_variables

```python
def get_variables(include_global: bool = False) -> Array[MovieGraphVariable]
```

x.get_variables(include_global=False) -> Array[MovieGraphVariable]
Gets all variables that are available to be used in the graph. Global variables can optionally be included if
bIncludeGlobal is set to true.

Args:
    include_global (bool): 

Returns:
    Array[MovieGraphVariable]:

<a id="unreal.MovieGraphConfig.get_outputs"></a>

#### get_outputs

```python
def get_outputs() -> Array[MovieGraphOutput]
```

x.get_outputs() -> Array[MovieGraphOutput]
Gets all outputs that have been defined on the graph.

Returns:
    Array[MovieGraphOutput]:

<a id="unreal.MovieGraphConfig.get_output_node"></a>

#### get_output_node

```python
def get_output_node() -> MovieGraphNode
```

x.get_output_node() -> MovieGraphNode
Gets the automatically generated "Outputs" node in the Graph.

Returns:
    MovieGraphNode:

<a id="unreal.MovieGraphConfig.get_inputs"></a>

#### get_inputs

```python
def get_inputs() -> Array[MovieGraphInput]
```

x.get_inputs() -> Array[MovieGraphInput]
Gets all inputs that have been defined on the graph.

Returns:
    Array[MovieGraphInput]:

<a id="unreal.MovieGraphConfig.get_input_node"></a>

#### get_input_node

```python
def get_input_node() -> MovieGraphNode
```

x.get_input_node() -> MovieGraphNode
Gets the automatically generated "Inputs" node in the Graph.

Returns:
    MovieGraphNode:

<a id="unreal.MovieGraphConfig.delete_member"></a>

#### delete_member

```python
def delete_member(member_to_delete: MovieGraphMember) -> bool
```

x.delete_member(member_to_delete) -> bool
Remove the specified member (input, output, variable) from the graph.

Args:
    member_to_delete (MovieGraphMember): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.create_node_by_class"></a>

#### create_node_by_class

```python
def create_node_by_class(class_: Class) -> MovieGraphNode
```

x.create_node_by_class(class_) -> MovieGraphNode
Creates the given node type in this graph. Does not create any connections, and a node will not be
considered during evaluation unless it is connected to other nodes in the graph.

Args:
    class_ (type(Class)): 

Returns:
    MovieGraphNode:

<a id="unreal.MovieGraphConfig.create_flattened_graph"></a>

#### create_flattened_graph

```python
def create_flattened_graph(
    context: MovieGraphTraversalContext
) -> Tuple[MovieGraphEvaluatedConfig, str]
```

x.create_flattened_graph(context) -> (MovieGraphEvaluatedConfig, out_error=str)
Given a user-defined evaluation context, evaluate the graph and build a "flattened" list of settings for each branch discovered.
If there was an error while evaluating the graph, nullptr will be returned and OutError will be populated with a description of the problem.

Args:
    context (MovieGraphTraversalContext): 

Returns:
    str: 

    out_error (str):

<a id="unreal.MovieGraphConfig.add_variable"></a>

#### add_variable

```python
def add_variable(custom_base_name: Name = "None") -> MovieGraphVariable
```

x.add_variable(custom_base_name="None") -> MovieGraphVariable
Adds a new variable member with default values to the graph. The new variable will have a base name of
"Variable" unless specified in InCustomBaseName. Returns the new variable on success, else nullptr.

Args:
    custom_base_name (Name): 

Returns:
    MovieGraphVariable:

<a id="unreal.MovieGraphConfig.add_output"></a>

#### add_output

```python
def add_output(base_name: Text = "") -> MovieGraphOutput
```

x.add_output(base_name="") -> MovieGraphOutput
Adds a new output member to the graph. Returns the new output on success, else nullptr.

The default name of the output is "Output". Optionally, InBaseName can be specified to add the output with a specific name. If the name "Output"
(or the custom InBaseName) isn't available, a numerical suffix will be added.

Args:
    base_name (Text): 

Returns:
    MovieGraphOutput:

<a id="unreal.MovieGraphConfig.add_labeled_edge"></a>

#### add_labeled_edge

```python
def add_labeled_edge(from_node: MovieGraphNode, from_pin_label: Name,
                     to_node: MovieGraphNode, to_pin_label: Name) -> bool
```

x.add_labeled_edge(from_node, from_pin_label, to_node, to_pin_label) -> bool
Add a connection in the graph between the given nodes and pin names. Pin name may be empty for basic
nodes (if no name is displayed in the UI). Can be used for either input or output pins.
Returns False if the pin could not be found, or the connection could not be made (type mismatches).

Args:
    from_node (MovieGraphNode): 
    from_pin_label (Name): 
    to_node (MovieGraphNode): 
    to_pin_label (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphConfig.add_input"></a>

#### add_input

```python
def add_input(base_name: Text = "") -> MovieGraphInput
```

x.add_input(base_name="") -> MovieGraphInput
Adds a new input member to the graph. Returns the new input on success, else nullptr.

The default name of the input is "Input". Optionally, InBaseName can be specified to add the input with a specific name. If the name "Input"
(or the custom InBaseName) isn't available, a numerical suffix will be added.

Args:
    base_name (Text): 

Returns:
    MovieGraphInput:

<a id="unreal.MovieGraphTimeStepBase"></a>