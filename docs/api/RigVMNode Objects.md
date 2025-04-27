## RigVMNode Objects

```python
class RigVMNode(Object)
```

The Node represents a single statement within a Graph.
Nodes can represent values such as Variables / Parameters,
they can represent Function Invocations or Control Flow
logic statements (such as If conditions of For loops).
Additionally Nodes are used to represent Comment statements.
Nodes contain Pins to represent parameters for Function
Invocations or Value access on Variables / Parameters.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMNode.h

<a id="unreal.RigVMNode.set_has_breakpoint"></a>

#### set_has_breakpoint

```python
def set_has_breakpoint(value: bool) -> None
```

x.set_has_breakpoint(value) -> None
Set Has Breakpoint

Args:
    value (bool):

<a id="unreal.RigVMNode.set_execution_is_halted_at_this_node"></a>

#### set_execution_is_halted_at_this_node

```python
def set_execution_is_halted_at_this_node(value: bool) -> None
```

x.set_execution_is_halted_at_this_node(value) -> None
Set Execution Is Halted at This Node

Args:
    value (bool):

<a id="unreal.RigVMNode.is_visible_in_ui"></a>

#### is_visible_in_ui

```python
def is_visible_in_ui() -> bool
```

x.is_visible_in_ui() -> bool
Returns true if this should be visible in the UI

Returns:
    bool:

<a id="unreal.RigVMNode.is_trait_pin"></a>

#### is_trait_pin

```python
def is_trait_pin(name: Name) -> bool
```

x.is_trait_pin(name) -> bool
Is Trait Pin

Args:
    name (Name): 

Returns:
    bool:

<a id="unreal.RigVMNode.is_selected"></a>

#### is_selected

```python
def is_selected() -> bool
```

x.is_selected() -> bool
Returns true if this Node is currently selected.

Returns:
    bool:

<a id="unreal.RigVMNode.is_pure"></a>

#### is_pure

```python
def is_pure() -> bool
```

x.is_pure() -> bool
Returns true if this Node has no side-effects
and no internal state.

Returns:
    bool:

<a id="unreal.RigVMNode.is_pin_category_expanded"></a>

#### is_pin_category_expanded

```python
def is_pin_category_expanded(category: str) -> bool
```

x.is_pin_category_expanded(category) -> bool
Returns all pins for a given category

Args:
    category (str): 

Returns:
    bool:

<a id="unreal.RigVMNode.is_mutable"></a>

#### is_mutable

```python
def is_mutable() -> bool
```

x.is_mutable() -> bool
Returns true if this Node has side effects or
internal state.

Returns:
    bool:

<a id="unreal.RigVMNode.is_loop_node"></a>

#### is_loop_node

```python
def is_loop_node() -> bool
```

x.is_loop_node() -> bool
return true if this node is a loop node

Returns:
    bool:

<a id="unreal.RigVMNode.is_linked_to"></a>

#### is_linked_to

```python
def is_linked_to(node: RigVMNode) -> bool
```

x.is_linked_to(node) -> bool
Returns true if this Node is linked to another
given node through any of the Nodes' Pins.

Args:
    node (RigVMNode): 

Returns:
    bool:

<a id="unreal.RigVMNode.is_input_aggregate"></a>

#### is_input_aggregate

```python
def is_input_aggregate() -> bool
```

x.is_input_aggregate() -> bool
Is Input Aggregate

Returns:
    bool:

<a id="unreal.RigVMNode.is_injected"></a>

#### is_injected

```python
def is_injected() -> bool
```

x.is_injected() -> bool
Returns true if this is an injected node.
Injected nodes are managed by pins are are not visible to the user.

Returns:
    bool:

<a id="unreal.RigVMNode.is_event"></a>

#### is_event

```python
def is_event() -> bool
```

x.is_event() -> bool
Returns true if this Node is the beginning of a scope

Returns:
    bool:

<a id="unreal.RigVMNode.is_defined_as_varying"></a>

#### is_defined_as_varying

```python
def is_defined_as_varying() -> bool
```

x.is_defined_as_varying() -> bool
Returns true if the node is defined as non-varying

Returns:
    bool:

<a id="unreal.RigVMNode.is_defined_as_constant"></a>

#### is_defined_as_constant

```python
def is_defined_as_constant() -> bool
```

x.is_defined_as_constant() -> bool
Returns true if the node is defined as non-varying

Returns:
    bool:

<a id="unreal.RigVMNode.is_control_flow_node"></a>

#### is_control_flow_node

```python
def is_control_flow_node() -> bool
```

x.is_control_flow_node() -> bool
return true if this node is a control flow node

Returns:
    bool:

<a id="unreal.RigVMNode.is_aggregate"></a>

#### is_aggregate

```python
def is_aggregate() -> bool
```

x.is_aggregate() -> bool
Is Aggregate

Returns:
    bool:

<a id="unreal.RigVMNode.has_pin_of_direction"></a>

#### has_pin_of_direction

```python
def has_pin_of_direction(direction: RigVMPinDirection) -> bool
```

x.has_pin_of_direction(direction) -> bool
Returns true if the node has any pins of the provided direction

Args:
    direction (RigVMPinDirection): 

Returns:
    bool:

<a id="unreal.RigVMNode.has_output_pin"></a>

#### has_output_pin

```python
def has_output_pin(include_io: bool = True) -> bool
```

x.has_output_pin(include_io=True) -> bool
Returns true if the node has any output pins

Args:
    include_io (bool): 

Returns:
    bool:

<a id="unreal.RigVMNode.has_orphaned_pins"></a>

#### has_orphaned_pins

```python
def has_orphaned_pins() -> bool
```

x.has_orphaned_pins() -> bool
Returns true if the node has orphaned pins - which leads to a compiler error

Returns:
    bool:

<a id="unreal.RigVMNode.has_lazy_pin"></a>

#### has_lazy_pin

```python
def has_lazy_pin(only_consider_pins_with_links: bool = False) -> bool
```

x.has_lazy_pin(only_consider_pins_with_links=False) -> bool
Returns true if the node has any lazily evaluating pins

Args:
    only_consider_pins_with_links (bool): 

Returns:
    bool:

<a id="unreal.RigVMNode.has_io_pin"></a>

#### has_io_pin

```python
def has_io_pin() -> bool
```

x.has_io_pin() -> bool
Returns true if the node has any io pins

Returns:
    bool:

<a id="unreal.RigVMNode.has_input_pin"></a>

#### has_input_pin

```python
def has_input_pin(include_io: bool = True) -> bool
```

x.has_input_pin(include_io=True) -> bool
Returns true if the node has any input pins

Args:
    include_io (bool): 

Returns:
    bool:

<a id="unreal.RigVMNode.has_breakpoint"></a>

#### has_breakpoint

```python
def has_breakpoint() -> bool
```

x.has_breakpoint() -> bool
Has Breakpoint

Returns:
    bool:

<a id="unreal.RigVMNode.get_trait_pins"></a>

#### get_trait_pins

```python
def get_trait_pins() -> Array[RigVMPin]
```

x.get_trait_pins() -> Array[RigVMPin]
Get Trait Pins

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.get_tool_tip_text"></a>

#### get_tool_tip_text

```python
def get_tool_tip_text() -> Text
```

x.get_tool_tip_text() -> Text
Returns the tooltip of this node

Returns:
    Text:

<a id="unreal.RigVMNode.get_supported_workflows"></a>

#### get_supported_workflows

```python
def get_supported_workflows(type: RigVMUserWorkflowType,
                            subject: Object) -> Array[RigVMUserWorkflow]
```

x.get_supported_workflows(type, subject) -> Array[RigVMUserWorkflow]
returns all supported workflows of the node

Args:
    type (RigVMUserWorkflowType): 
    subject (Object): 

Returns:
    Array[RigVMUserWorkflow]:

<a id="unreal.RigVMNode.get_sub_pin_categories"></a>

#### get_sub_pin_categories

```python
def get_sub_pin_categories(category: str,
                           only_existing: bool = False,
                           recursive: bool = False) -> Array[str]
```

x.get_sub_pin_categories(category, only_existing=False, recursive=False) -> Array[str]
Returns all sub user defined categories of a given parent category

Args:
    category (str): 
    only_existing (bool): 
    recursive (bool): 

Returns:
    Array[str]:

<a id="unreal.RigVMNode.get_size"></a>

#### get_size

```python
def get_size() -> Vector2D
```

x.get_size() -> Vector2D
Returns the 2d size of this node - used for UI.

Returns:
    Vector2D:

<a id="unreal.RigVMNode.get_second_aggregate_pin"></a>

#### get_second_aggregate_pin

```python
def get_second_aggregate_pin() -> RigVMPin
```

x.get_second_aggregate_pin() -> RigVMPin
Get Second Aggregate Pin

Returns:
    RigVMPin:

<a id="unreal.RigVMNode.get_root_graph"></a>

#### get_root_graph

```python
def get_root_graph() -> RigVMGraph
```

x.get_root_graph() -> RigVMGraph
Returns the top level / root Graph of this Node

Returns:
    RigVMGraph:

<a id="unreal.RigVMNode.get_previous_f_name"></a>

#### get_previous_f_name

```python
def get_previous_f_name() -> Name
```

x.get_previous_f_name() -> Name
Returns the name of the node prior to the renaming

Returns:
    Name:

<a id="unreal.RigVMNode.get_position"></a>

#### get_position

```python
def get_position() -> Vector2D
```

x.get_position() -> Vector2D
Returns the 2d position of this node - used for UI.

Returns:
    Vector2D:

<a id="unreal.RigVMNode.get_pins_for_category"></a>

#### get_pins_for_category

```python
def get_pins_for_category(category: str) -> Array[RigVMPin]
```

x.get_pins_for_category(category) -> Array[RigVMPin]
Returns all pins for a given category

Args:
    category (str): 

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.get_pins"></a>

#### get_pins

```python
def get_pins() -> Array[RigVMPin]
```

x.get_pins() -> Array[RigVMPin]
Returns all of the top-level Pins of this Node.

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.get_pin_category_name"></a>

#### get_pin_category_name

```python
def get_pin_category_name(category: str) -> str
```

x.get_pin_category_name(category) -> str
Returns the name of pin category

Args:
    category (str): 

Returns:
    str:

<a id="unreal.RigVMNode.get_pin_categories"></a>

#### get_pin_categories

```python
def get_pin_categories() -> Array[str]
```

x.get_pin_categories() -> Array[str]
Returns all user defined categories on this node

Returns:
    Array[str]:

<a id="unreal.RigVMNode.get_parent_pin_category"></a>

#### get_parent_pin_category

```python
def get_parent_pin_category(category: str, only_existing: bool = False) -> str
```

x.get_parent_pin_category(category, only_existing=False) -> str
Returns the parent pin category of the given category (or an empty string in case there's no parent)

Args:
    category (str): 
    only_existing (bool): 

Returns:
    str:

<a id="unreal.RigVMNode.get_parent_pin_categories"></a>

#### get_parent_pin_categories

```python
def get_parent_pin_categories(category: str,
                              only_existing: bool = False,
                              include_self: bool = False) -> Array[str]
```

x.get_parent_pin_categories(category, only_existing=False, include_self=False) -> Array[str]
Returns all parent categories of a given

Args:
    category (str): 
    only_existing (bool): 
    include_self (bool): 

Returns:
    Array[str]:

<a id="unreal.RigVMNode.get_orphaned_pins"></a>

#### get_orphaned_pins

```python
def get_orphaned_pins() -> Array[RigVMPin]
```

x.get_orphaned_pins() -> Array[RigVMPin]
Returns all of the top-level orphaned Pins of this Node.

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.get_opposite_aggregate_pin"></a>

#### get_opposite_aggregate_pin

```python
def get_opposite_aggregate_pin() -> RigVMPin
```

x.get_opposite_aggregate_pin() -> RigVMPin
Get Opposite Aggregate Pin

Returns:
    RigVMPin:

<a id="unreal.RigVMNode.get_node_title"></a>

#### get_node_title

```python
def get_node_title() -> str
```

x.get_node_title() -> str
Returns the title of this Node - used for UI.

Returns:
    str:

<a id="unreal.RigVMNode.get_node_path"></a>

#### get_node_path

```python
def get_node_path(recursive: bool = False) -> str
```

x.get_node_path(recursive=False) -> str
Returns the a . separated string containing all of the
names used to reach this Node within the Graph.
(for now this is the same as the Node's name)

Args:
    recursive (bool): 

Returns:
    str:

<a id="unreal.RigVMNode.get_node_layout"></a>

#### get_node_layout

```python
def get_node_layout(include_empty_categories: bool = False) -> RigVMNodeLayout
```

x.get_node_layout(include_empty_categories=False) -> RigVMNodeLayout
Returns the pin UI layout for this node

Args:
    include_empty_categories (bool): 

Returns:
    RigVMNodeLayout:

<a id="unreal.RigVMNode.get_node_index"></a>

#### get_node_index

```python
def get_node_index() -> int
```

x.get_node_index() -> int32
Returns the current index of the Node within the Graph.

Returns:
    int32:

<a id="unreal.RigVMNode.get_node_color"></a>

#### get_node_color

```python
def get_node_color() -> LinearColor
```

x.get_node_color() -> LinearColor
Returns the color of this node - used for UI.

Returns:
    LinearColor:

<a id="unreal.RigVMNode.get_next_aggregate_name"></a>

#### get_next_aggregate_name

```python
def get_next_aggregate_name(last_aggregate_pin_name: Name) -> Name
```

x.get_next_aggregate_name(last_aggregate_pin_name) -> Name
Get Next Aggregate Name

Args:
    last_aggregate_pin_name (Name): 

Returns:
    Name:

<a id="unreal.RigVMNode.get_links"></a>

#### get_links

```python
def get_links() -> Array[RigVMLink]
```

x.get_links() -> Array[RigVMLink]
Returns all links to any pin on this node

Returns:
    Array[RigVMLink]:

<a id="unreal.RigVMNode.get_linked_target_nodes"></a>

#### get_linked_target_nodes

```python
def get_linked_target_nodes() -> Array[RigVMNode]
```

x.get_linked_target_nodes() -> Array[RigVMNode]
Returns a list of Nodes connected as targets to
this Node as the source.

Returns:
    Array[RigVMNode]:

<a id="unreal.RigVMNode.get_linked_source_nodes"></a>

#### get_linked_source_nodes

```python
def get_linked_source_nodes() -> Array[RigVMNode]
```

x.get_linked_source_nodes() -> Array[RigVMNode]
Returns a list of Nodes connected as sources to
this Node as the target.

Returns:
    Array[RigVMNode]:

<a id="unreal.RigVMNode.get_injection_info"></a>

#### get_injection_info

```python
def get_injection_info() -> RigVMInjectionInfo
```

x.get_injection_info() -> RigVMInjectionInfo
Returns the injection info of this Node (or nullptr)

Returns:
    RigVMInjectionInfo:

<a id="unreal.RigVMNode.get_graph_depth"></a>

#### get_graph_depth

```python
def get_graph_depth() -> int
```

x.get_graph_depth() -> int32
Returns the graph nesting depth of this node

Returns:
    int32:

<a id="unreal.RigVMNode.get_graph"></a>

#### get_graph

```python
def get_graph() -> RigVMGraph
```

x.get_graph() -> RigVMGraph
Returns the Graph of this Node

Returns:
    RigVMGraph:

<a id="unreal.RigVMNode.get_first_aggregate_pin"></a>

#### get_first_aggregate_pin

```python
def get_first_aggregate_pin() -> RigVMPin
```

x.get_first_aggregate_pin() -> RigVMPin
Get First Aggregate Pin

Returns:
    RigVMPin:

<a id="unreal.RigVMNode.get_event_name"></a>

#### get_event_name

```python
def get_event_name() -> Name
```

x.get_event_name() -> Name
Returns the name of the event

Returns:
    Name:

<a id="unreal.RigVMNode.get_all_pins_recursively"></a>

#### get_all_pins_recursively

```python
def get_all_pins_recursively() -> Array[RigVMPin]
```

x.get_all_pins_recursively() -> Array[RigVMPin]
Returns all of the Pins of this Node (including SubPins).

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.get_aggregate_outputs"></a>

#### get_aggregate_outputs

```python
def get_aggregate_outputs() -> Array[RigVMPin]
```

x.get_aggregate_outputs() -> Array[RigVMPin]
Get Aggregate Outputs

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.get_aggregate_inputs"></a>

#### get_aggregate_inputs

```python
def get_aggregate_inputs() -> Array[RigVMPin]
```

x.get_aggregate_inputs() -> Array[RigVMPin]
Get Aggregate Inputs

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMNode.find_root_pin_by_name"></a>

#### find_root_pin_by_name

```python
def find_root_pin_by_name(pin_name: Name) -> RigVMPin
```

x.find_root_pin_by_name(pin_name) -> RigVMPin
Returns a root pin given its name

Args:
    pin_name (Name): 

Returns:
    RigVMPin:

<a id="unreal.RigVMNode.find_pin"></a>

#### find_pin

```python
def find_pin(pin_path: str) -> RigVMPin
```

x.find_pin(pin_path) -> RigVMPin
Returns a Pin given it's partial pin path below
this node (for example: "Color.R")

Args:
    pin_path (str): 

Returns:
    RigVMPin:

<a id="unreal.RigVMNode.find_function_for_node"></a>

#### find_function_for_node

```python
def find_function_for_node() -> RigVMLibraryNode
```

x.find_function_for_node() -> RigVMLibraryNode
Find Function for Node

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMNode.execution_is_halted_at_this_node"></a>

#### execution_is_halted_at_this_node

```python
def execution_is_halted_at_this_node() -> bool
```

x.execution_is_halted_at_this_node() -> bool
Execution Is Halted at This Node

Returns:
    bool:

<a id="unreal.RigVMNode.can_only_exist_once"></a>

#### can_only_exist_once

```python
def can_only_exist_once() -> bool
```

x.can_only_exist_once() -> bool
Returns true if this node can only exist once in a graph

Returns:
    bool:

<a id="unreal.RigVMNode.can_be_upgraded"></a>

#### can_be_upgraded

```python
def can_be_upgraded() -> bool
```

x.can_be_upgraded() -> bool
returns true if the node can be upgraded

Returns:
    bool:

<a id="unreal.RigVMTemplateNode"></a>