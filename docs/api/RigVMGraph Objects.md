## RigVMGraph Objects

```python
class RigVMGraph(Object)
```

The Graph represents a Function definition
using Nodes as statements.
Graphs can be compiled into a URigVM using the
FRigVMCompiler.
Graphs provide access to its Nodes, Pins and
Links.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMGraph.h

<a id="unreal.RigVMGraph.set_schema_class"></a>

#### set_schema_class

```python
def set_schema_class(schema_class: Class) -> None
```

x.set_schema_class(schema_class) -> None
Sets the schema class on the graph

Args:
    schema_class (type(Class)):

<a id="unreal.RigVMGraph.set_default_function_library"></a>

#### set_default_function_library

```python
def set_default_function_library(
        function_library: RigVMFunctionLibrary) -> None
```

x.set_default_function_library(function_library) -> None
Set Default Function Library

Args:
    function_library (RigVMFunctionLibrary):

<a id="unreal.RigVMGraph.is_top_level_graph"></a>

#### is_top_level_graph

```python
def is_top_level_graph() -> bool
```

x.is_top_level_graph() -> bool
Returns true if this graph is the top level graph

Returns:
    bool:

<a id="unreal.RigVMGraph.is_root_graph"></a>

#### is_root_graph

```python
def is_root_graph() -> bool
```

x.is_root_graph() -> bool
Returns true if this graph is a root / top level graph

Returns:
    bool:

<a id="unreal.RigVMGraph.is_node_selected"></a>

#### is_node_selected

```python
def is_node_selected(node_name: Name) -> bool
```

x.is_node_selected(node_name) -> bool
Returns true if a Node with a given name is selected.

Args:
    node_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMGraph.get_variable_descriptions"></a>

#### get_variable_descriptions

```python
def get_variable_descriptions() -> Array[RigVMGraphVariableDescription]
```

x.get_variable_descriptions() -> Array[RigVMGraphVariableDescription]
Returns a list of unique Variable descriptions within this Graph.
Multiple Variable Nodes can share the same description.

Returns:
    Array[RigVMGraphVariableDescription]:

<a id="unreal.RigVMGraph.get_select_nodes"></a>

#### get_select_nodes

```python
def get_select_nodes() -> Array[Name]
```

x.get_select_nodes() -> Array[Name]
Returns the names of all currently selected Nodes.

Returns:
    Array[Name]:

<a id="unreal.RigVMGraph.get_schema_class"></a>

#### get_schema_class

```python
def get_schema_class() -> Class
```

x.get_schema_class() -> type(Class)
Returns the schema class used by this graph

Returns:
    type(Class):

<a id="unreal.RigVMGraph.get_schema"></a>

#### get_schema

```python
def get_schema() -> RigVMSchema
```

x.get_schema() -> RigVMSchema
Returns the schema used by this graph

Returns:
    RigVMSchema:

<a id="unreal.RigVMGraph.get_root_graph"></a>

#### get_root_graph

```python
def get_root_graph() -> RigVMGraph
```

x.get_root_graph() -> RigVMGraph
Returns the root / top level parent graph of this graph (or this if it is the root graph)

Returns:
    RigVMGraph:

<a id="unreal.RigVMGraph.get_return_node"></a>

#### get_return_node

```python
def get_return_node() -> RigVMFunctionReturnNode
```

x.get_return_node() -> RigVMFunctionReturnNode
Returns the return node of this graph

Returns:
    RigVMFunctionReturnNode:

<a id="unreal.RigVMGraph.get_parent_graph"></a>

#### get_parent_graph

```python
def get_parent_graph() -> RigVMGraph
```

x.get_parent_graph() -> RigVMGraph
Returns the parent graph of this graph

Returns:
    RigVMGraph:

<a id="unreal.RigVMGraph.get_output_arguments"></a>

#### get_output_arguments

```python
def get_output_arguments() -> Array[RigVMGraphVariableDescription]
```

x.get_output_arguments() -> Array[RigVMGraphVariableDescription]
Returns the output arguments of this graph

Returns:
    Array[RigVMGraphVariableDescription]:

<a id="unreal.RigVMGraph.get_nodes"></a>

#### get_nodes

```python
def get_nodes() -> Array[RigVMNode]
```

x.get_nodes() -> Array[RigVMNode]
Returns all of the Nodes within this Graph.

Returns:
    Array[RigVMNode]:

<a id="unreal.RigVMGraph.get_node_path"></a>

#### get_node_path

```python
def get_node_path() -> str
```

x.get_node_path() -> str
Returns the path of this graph as defined by its invoking nodes

Returns:
    str:

<a id="unreal.RigVMGraph.get_local_variables"></a>

#### get_local_variables

```python
def get_local_variables(
    include_input_arguments: bool = False
) -> Array[RigVMGraphVariableDescription]
```

x.get_local_variables(include_input_arguments=False) -> Array[RigVMGraphVariableDescription]
Returns the local variables of this function

Args:
    include_input_arguments (bool): 

Returns:
    Array[RigVMGraphVariableDescription]:

<a id="unreal.RigVMGraph.get_links"></a>

#### get_links

```python
def get_links() -> Array[RigVMLink]
```

x.get_links() -> Array[RigVMLink]
Returns all of the Links within this Graph.

Returns:
    Array[RigVMLink]:

<a id="unreal.RigVMGraph.get_input_arguments"></a>

#### get_input_arguments

```python
def get_input_arguments() -> Array[RigVMGraphVariableDescription]
```

x.get_input_arguments() -> Array[RigVMGraphVariableDescription]
Returns the input arguments of this graph

Returns:
    Array[RigVMGraphVariableDescription]:

<a id="unreal.RigVMGraph.get_graph_name"></a>

#### get_graph_name

```python
def get_graph_name() -> str
```

x.get_graph_name() -> str
Returns the name of this graph (as defined by the node path)

Returns:
    str:

<a id="unreal.RigVMGraph.get_graph_depth"></a>

#### get_graph_depth

```python
def get_graph_depth() -> int
```

x.get_graph_depth() -> int32
Returns the root / top level parent graph of this graph (or this if it is the root graph)

Returns:
    int32:

<a id="unreal.RigVMGraph.get_event_names"></a>

#### get_event_names

```python
def get_event_names() -> Array[Name]
```

x.get_event_names() -> Array[Name]
Returns array of event names

Returns:
    Array[Name]:

<a id="unreal.RigVMGraph.get_entry_node"></a>

#### get_entry_node

```python
def get_entry_node() -> RigVMFunctionEntryNode
```

x.get_entry_node() -> RigVMFunctionEntryNode
Returns the entry node of this graph

Returns:
    RigVMFunctionEntryNode:

<a id="unreal.RigVMGraph.get_default_function_library"></a>

#### get_default_function_library

```python
def get_default_function_library() -> RigVMFunctionLibrary
```

x.get_default_function_library() -> RigVMFunctionLibrary
Returns the locally available function library

Returns:
    RigVMFunctionLibrary:

<a id="unreal.RigVMGraph.get_contained_graphs"></a>

#### get_contained_graphs

```python
def get_contained_graphs(recursive: bool = False) -> Array[RigVMGraph]
```

x.get_contained_graphs(recursive=False) -> Array[RigVMGraph]
Returns all of the contained graphs

Args:
    recursive (bool): 

Returns:
    Array[RigVMGraph]:

<a id="unreal.RigVMGraph.find_pin"></a>

#### find_pin

```python
def find_pin(pin_path: str) -> RigVMPin
```

x.find_pin(pin_path) -> RigVMPin
Returns a Pin given its path, for example "Node.Color.R".

Args:
    pin_path (str): 

Returns:
    RigVMPin:

<a id="unreal.RigVMGraph.find_node_by_name"></a>

#### find_node_by_name

```python
def find_node_by_name(node_name: Name) -> RigVMNode
```

x.find_node_by_name(node_name) -> RigVMNode
Returns a Node given its name (or nullptr).

Args:
    node_name (Name): 

Returns:
    RigVMNode:

<a id="unreal.RigVMGraph.find_node"></a>

#### find_node

```python
def find_node(node_path: str) -> RigVMNode
```

x.find_node(node_path) -> RigVMNode
Returns a Node given its path (or nullptr).
(for now this is the same as finding a node by its name.)

Args:
    node_path (str): 

Returns:
    RigVMNode:

<a id="unreal.RigVMGraph.find_link"></a>

#### find_link

```python
def find_link(link_pin_path_representation: str) -> RigVMLink
```

x.find_link(link_pin_path_representation) -> RigVMLink
Returns a link given its string representation,
for example "NodeA.Color.R -> NodeB.Translation.X"

Args:
    link_pin_path_representation (str): 

Returns:
    RigVMLink:

<a id="unreal.RigVMGraph.contains_link"></a>

#### contains_link

```python
def contains_link(pin_path_representation: str) -> bool
```

x.contains_link(pin_path_representation) -> bool
Returns true if the graph contains a link given its string representation

Args:
    pin_path_representation (str): 

Returns:
    bool:

<a id="unreal.RigVMFunctionLibrary"></a>