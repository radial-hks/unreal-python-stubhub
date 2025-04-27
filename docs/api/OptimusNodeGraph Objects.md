## OptimusNodeGraph Objects

```python
class OptimusNodeGraph(Object)
```

Optimus Node Graph

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusNodeGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``graph_type`` (OptimusNodeGraphType):  [Read-Only] The type of graph this represents.

<a id="unreal.OptimusNodeGraph.graph_type"></a>

#### graph_type

```python
@property
def graph_type() -> OptimusNodeGraphType
```

(OptimusNodeGraphType):  [Read-Only] The type of graph this represents.

<a id="unreal.OptimusNodeGraph.rename_graph_direct"></a>

#### rename_graph_direct

```python
def rename_graph_direct(graph: OptimusNodeGraph, new_name: str) -> bool
```

x.rename_graph_direct(graph, new_name) -> bool
Rename Graph Direct

Args:
    graph (OptimusNodeGraph): 
    new_name (str): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.rename_graph"></a>

#### rename_graph

```python
def rename_graph(graph: OptimusNodeGraph, new_name: str) -> bool
```

x.rename_graph(graph, new_name) -> bool
Rename Graph

Args:
    graph (OptimusNodeGraph): 
    new_name (str): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.remove_nodes"></a>

#### remove_nodes

```python
def remove_nodes(nodes: Array[OptimusNode]) -> bool
```

x.remove_nodes(nodes) -> bool
Remove Nodes

Args:
    nodes (Array[OptimusNode]): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.remove_node"></a>

#### remove_node

```python
def remove_node(node: OptimusNode) -> bool
```

x.remove_node(node) -> bool
Remove Node

Args:
    node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.remove_link"></a>

#### remove_link

```python
def remove_link(node_output_pin: OptimusNodePin,
                node_input_pin: OptimusNodePin) -> bool
```

x.remove_link(node_output_pin, node_input_pin) -> bool

brief: Removes a single link between two nodes. FIXME: Use UOptimusNodeLink instead.

Args:
    node_output_pin (OptimusNodePin): 
    node_input_pin (OptimusNodePin): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.remove_all_links"></a>

#### remove_all_links

```python
def remove_all_links(node_pin: OptimusNodePin) -> bool
```

x.remove_all_links(node_pin) -> bool

brief: Removes all links to the given pin, whether it's an input or an output pin.

Args:
    node_pin (OptimusNodePin): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.move_graph_direct"></a>

#### move_graph_direct

```python
def move_graph_direct(graph: OptimusNodeGraph, insert_before: int) -> bool
```

x.move_graph_direct(graph, insert_before) -> bool
Move Graph Direct

Args:
    graph (OptimusNodeGraph): 
    insert_before (int32): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.is_sub_graph_reference"></a>

#### is_sub_graph_reference

```python
def is_sub_graph_reference(node: OptimusNode) -> bool
```

x.is_sub_graph_reference(node) -> bool
Returns true if the node in question is a function sub-graph node that can be expanded
into a group of nodes using ExpandFunctionToNodes.

Args:
    node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.is_kernel_function"></a>

#### is_kernel_function

```python
def is_kernel_function(node: OptimusNode) -> bool
```

x.is_kernel_function(node) -> bool
Returns true if the node in question is a kernel function node that can be converted to
a custom kernel using ConvertFunctionToCustomKernel.

Args:
    node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.is_function_reference"></a>

#### is_function_reference

```python
def is_function_reference(node: OptimusNode) -> bool
```

x.is_function_reference(node) -> bool
Returns true if the node in question is a function reference node that can be expanded
into a group of nodes using ExpandFunctionToNodes.

Args:
    node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.is_function_graph"></a>

#### is_function_graph

```python
def is_function_graph() -> bool
```

x.is_function_graph() -> bool
Is Function Graph

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.is_execution_graph"></a>

#### is_execution_graph

```python
def is_execution_graph() -> bool
```

x.is_execution_graph() -> bool
Is Execution Graph

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.is_custom_kernel"></a>

#### is_custom_kernel

```python
def is_custom_kernel(node: OptimusNode) -> bool
```

x.is_custom_kernel(node) -> bool
Returns true if the node in question is a custom kernel node that can be converted to
a kernel function with ConvertCustomKernelToFunction.

Args:
    node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.get_graph_type"></a>

#### get_graph_type

```python
def get_graph_type() -> OptimusNodeGraphType
```

x.get_graph_type() -> OptimusNodeGraphType
Get Graph Type

Returns:
    OptimusNodeGraphType:

<a id="unreal.OptimusNodeGraph.get_graphs"></a>

#### get_graphs

```python
def get_graphs() -> Array[OptimusNodeGraph]
```

x.get_graphs() -> Array[OptimusNodeGraph]
Get Graphs

Returns:
    Array[OptimusNodeGraph]:

<a id="unreal.OptimusNodeGraph.get_graph_index"></a>

#### get_graph_index

```python
def get_graph_index() -> int
```

x.get_graph_index() -> int32
Get Graph Index

Returns:
    int32:

<a id="unreal.OptimusNodeGraph.expand_collapsed_nodes"></a>

#### expand_collapsed_nodes

```python
def expand_collapsed_nodes(
        graph_reference_node: OptimusNode) -> Array[OptimusNode]
```

x.expand_collapsed_nodes(graph_reference_node) -> Array[OptimusNode]
Take a function or subgraph node and expand it in-place, replacing the given function
node. The function definition still remains, if a function node was expanded. If a
sub-graph was expanded, the sub-graph is deleted.

Args:
    graph_reference_node (OptimusNode): 

Returns:
    Array[OptimusNode]:

<a id="unreal.OptimusNodeGraph.duplicate_nodes"></a>

#### duplicate_nodes

```python
def duplicate_nodes(nodes: Array[OptimusNode], position: Vector2D) -> bool
```

x.duplicate_nodes(nodes, position) -> bool
Duplicate a collection of nodes from the same graph, using the InPosition position
to be the top-left origin of the pasted nodes.

Args:
    nodes (Array[OptimusNode]): 
    position (Vector2D): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.duplicate_node"></a>

#### duplicate_node

```python
def duplicate_node(node: OptimusNode, position: Vector2D) -> OptimusNode
```

x.duplicate_node(node, position) -> OptimusNode
Duplicate Node

Args:
    node (OptimusNode): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.convert_to_sub_graph"></a>

#### convert_to_sub_graph

```python
def convert_to_sub_graph(function_node: OptimusNode) -> bool
```

x.convert_to_sub_graph(function_node) -> bool
Take a function node convert it to a subgraph node in-place

Args:
    function_node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.convert_to_function"></a>

#### convert_to_function

```python
def convert_to_function(sub_graph_node: OptimusNode) -> bool
```

x.convert_to_function(sub_graph_node) -> bool
Take a subgraph node convert it to a function in-place

Args:
    sub_graph_node (OptimusNode): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.convert_function_to_custom_kernel"></a>

#### convert_function_to_custom_kernel

```python
def convert_function_to_custom_kernel(
        kernel_function: OptimusNode) -> OptimusNode
```

x.convert_function_to_custom_kernel(kernel_function) -> OptimusNode
Takes a kernel function and unpackages to a custom kernel. If the given node is not a
kernel function or cannot be converted, a nullptr is returned.

Args:
    kernel_function (OptimusNode): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.convert_custom_kernel_to_function"></a>

#### convert_custom_kernel_to_function

```python
def convert_custom_kernel_to_function(
        custom_kernel: OptimusNode) -> OptimusNode
```

x.convert_custom_kernel_to_function(custom_kernel) -> OptimusNode
Takes a custom kernel and converts to a packaged function. If the given node is not a
custom kernel or cannot be converted, a nullptr is returned.

Args:
    custom_kernel (OptimusNode): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.collapse_nodes_to_sub_graph"></a>

#### collapse_nodes_to_sub_graph

```python
def collapse_nodes_to_sub_graph(nodes: Array[OptimusNode]) -> OptimusNode
```

x.collapse_nodes_to_sub_graph(nodes) -> OptimusNode
Take a set of nodes and collapse them into a subgraph, replacing the given nodes
with a new subgraph node and returning it.

Args:
    nodes (Array[OptimusNode]): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.collapse_nodes_to_function"></a>

#### collapse_nodes_to_function

```python
def collapse_nodes_to_function(nodes: Array[OptimusNode]) -> OptimusNode
```

x.collapse_nodes_to_function(nodes) -> OptimusNode
Take a set of nodes and collapse them into a single function, replacing the given nodes
with the new function node and returning it. A new function definition is made available
as a new Function graph in the package.

Args:
    nodes (Array[OptimusNode]): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_variable_get_node"></a>

#### add_variable_get_node

```python
def add_variable_get_node(variable_desc: OptimusVariableDescription,
                          position: Vector2D) -> OptimusNode
```

x.add_variable_get_node(variable_desc, position) -> OptimusNode
Add Variable Get Node

Args:
    variable_desc (OptimusVariableDescription): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_value_node"></a>

#### add_value_node

```python
def add_value_node(data_type_ref: OptimusDataTypeRef,
                   position: Vector2D) -> OptimusNode
```

x.add_value_node(data_type_ref, position) -> OptimusNode
Add Value Node

Args:
    data_type_ref (OptimusDataTypeRef): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_resource_set_node"></a>

#### add_resource_set_node

```python
def add_resource_set_node(resource_desc: OptimusResourceDescription,
                          position: Vector2D) -> OptimusNode
```

x.add_resource_set_node(resource_desc, position) -> OptimusNode
Add Resource Set Node

Args:
    resource_desc (OptimusResourceDescription): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_resource_node"></a>

#### add_resource_node

```python
def add_resource_node(resource_desc: OptimusResourceDescription,
                      position: Vector2D) -> OptimusNode
```

x.add_resource_node(resource_desc, position) -> OptimusNode
Add Resource Node

Args:
    resource_desc (OptimusResourceDescription): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_resource_get_node"></a>

#### add_resource_get_node

```python
def add_resource_get_node(resource_desc: OptimusResourceDescription,
                          position: Vector2D) -> OptimusNode
```

x.add_resource_get_node(resource_desc, position) -> OptimusNode
Add Resource Get Node

Args:
    resource_desc (OptimusResourceDescription): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_node"></a>

#### add_node

```python
def add_node(node_class: Class, position: Vector2D) -> OptimusNode
```

x.add_node(node_class, position) -> OptimusNode
TODO: Add magic connection from a pin.

Args:
    node_class (type(Class)): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_loop_terminal_nodes"></a>

#### add_loop_terminal_nodes

```python
def add_loop_terminal_nodes(position: Vector2D) -> Array[OptimusNode]
```

x.add_loop_terminal_nodes(position) -> Array[OptimusNode]
Add Loop Terminal Nodes

Args:
    position (Vector2D): 

Returns:
    Array[OptimusNode]:

<a id="unreal.OptimusNodeGraph.add_link"></a>

#### add_link

```python
def add_link(node_output_pin: OptimusNodePin,
             node_input_pin: OptimusNodePin) -> bool
```

x.add_link(node_output_pin, node_input_pin) -> bool
Add Link

Args:
    node_output_pin (OptimusNodePin): 
    node_input_pin (OptimusNodePin): 

Returns:
    bool:

<a id="unreal.OptimusNodeGraph.add_function_reference_node"></a>

#### add_function_reference_node

```python
def add_function_reference_node(function_graph: OptimusFunctionNodeGraph,
                                position: Vector2D) -> OptimusNode
```

x.add_function_reference_node(function_graph, position) -> OptimusNode
Add Function Reference Node

Args:
    function_graph (OptimusFunctionNodeGraph): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_data_interface_node"></a>

#### add_data_interface_node

```python
def add_data_interface_node(data_interface_class: Class,
                            position: Vector2D) -> OptimusNode
```

x.add_data_interface_node(data_interface_class, position) -> OptimusNode
Add Data Interface Node

Args:
    data_interface_class (type(Class)): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeGraph.add_component_binding_get_node"></a>

#### add_component_binding_get_node

```python
def add_component_binding_get_node(
        component_binding: OptimusComponentSourceBinding,
        position: Vector2D) -> OptimusNode
```

x.add_component_binding_get_node(component_binding, position) -> OptimusNode
Add Component Binding Get Node

Args:
    component_binding (OptimusComponentSourceBinding): 
    position (Vector2D): 

Returns:
    OptimusNode:

<a id="unreal.OptimusNodeSubGraph"></a>