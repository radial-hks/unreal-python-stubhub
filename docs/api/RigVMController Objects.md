## RigVMController Objects

```python
class RigVMController(Object)
```

The Controller is the sole authority to perform changes
on the Graph. The Controller itself is stateless.
The Controller offers a Modified event to subscribe to
for user interface views - so they can be informed about
any change that's happening within the Graph.
The Controller routes all changes through the Graph itself,
so you can have N Controllers performing edits on 1 Graph,
and N Views subscribing to 1 Controller.
In Python you can also subscribe to this event to be
able to react to topological changes of the Graph there.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``modified_event`` (RigVMGraphModifiedDynamicEvent):  [Read-Write]

<a id="unreal.RigVMController.modified_event"></a>

#### modified_event

```python
@property
def modified_event() -> RigVMGraphModifiedDynamicEvent
```

(RigVMGraphModifiedDynamicEvent):  [Read-Only]

<a id="unreal.RigVMController.upgrade_nodes"></a>

#### upgrade_nodes

```python
def upgrade_nodes(node_names: Array[Name],
                  recursive: bool = True,
                  setup_undo_redo: bool = True,
                  print_python_command: bool = False) -> Array[RigVMNode]
```

x.upgrade_nodes(node_names, recursive=True, setup_undo_redo=True, print_python_command=False) -> Array[RigVMNode]
Upgrades a set of nodes with each corresponding next known version

Args:
    node_names (Array[Name]): 
    recursive (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    Array[RigVMNode]:

<a id="unreal.RigVMController.unresolve_template_nodes"></a>

#### unresolve_template_nodes

```python
def unresolve_template_nodes(node_names: Array[Name],
                             setup_undo_redo: bool = True,
                             print_python_command: bool = False) -> bool
```

x.unresolve_template_nodes(node_names, setup_undo_redo=True, print_python_command=False) -> bool
Turns a resolved templated node(s) back into its template.

Args:
    node_names (Array[Name]): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.undo"></a>

#### undo

```python
def undo() -> bool
```

x.undo() -> bool
Un-does the last action on the stack.
Note: This should really only be used for unit tests,
use the GEditor's main Undo method instead.

Returns:
    bool:

<a id="unreal.RigVMController.unbind_pin_from_variable"></a>

#### unbind_pin_from_variable

```python
def unbind_pin_from_variable(pin_path: str,
                             setup_undo_redo: bool = True,
                             print_python_command: bool = False) -> bool
```

x.unbind_pin_from_variable(pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Removes the binging of a pin to a variable
This causes a PinBoundVariableChanged modified event.

Args:
    pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.swap_function_reference_by_name"></a>

#### swap_function_reference_by_name

```python
def swap_function_reference_by_name(
        function_reference_node_name: Name,
        new_function_identifier: RigVMGraphFunctionIdentifier,
        setup_orphan_pins: bool,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.swap_function_reference_by_name(function_reference_node_name, new_function_identifier, setup_orphan_pins, setup_undo_redo=True, print_python_command=False) -> bool
Swap Function Reference by Name

Args:
    function_reference_node_name (Name): 
    new_function_identifier (RigVMGraphFunctionIdentifier): 
    setup_orphan_pins (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.swap_function_reference"></a>

#### swap_function_reference

```python
def swap_function_reference(
        function_reference_node: RigVMFunctionReferenceNode,
        new_function_identifier: RigVMGraphFunctionIdentifier,
        setup_orphan_pins: bool,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.swap_function_reference(function_reference_node, new_function_identifier, setup_orphan_pins, setup_undo_redo=True, print_python_command=False) -> bool
Swap Function Reference

Args:
    function_reference_node (RigVMFunctionReferenceNode): 
    new_function_identifier (RigVMGraphFunctionIdentifier): 
    setup_orphan_pins (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.swap_all_function_references"></a>

#### swap_all_function_references

```python
def swap_all_function_references(
        old_function_identifier: RigVMGraphFunctionIdentifier,
        new_function_identifier: RigVMGraphFunctionIdentifier,
        setup_orphan_pins: bool,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.swap_all_function_references(old_function_identifier, new_function_identifier, setup_orphan_pins, setup_undo_redo=True, print_python_command=False) -> bool
Swap All Function References

Args:
    old_function_identifier (RigVMGraphFunctionIdentifier): 
    new_function_identifier (RigVMGraphFunctionIdentifier): 
    setup_orphan_pins (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.split_function_variant"></a>

#### split_function_variant

```python
def split_function_variant(function_name: Name,
                           setup_undo_redo: bool = True,
                           print_python_command: bool = False) -> bool
```

x.split_function_variant(function_name, setup_undo_redo=True, print_python_command=False) -> bool
Resets the function's guid to a new one and splits it from the former variant set

Args:
    function_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_unit_node_defaults"></a>

#### set_unit_node_defaults

```python
def set_unit_node_defaults(node: RigVMUnitNode,
                           defaults: str,
                           setup_undo_redo: bool = True,
                           print_python_command: bool = False) -> bool
```

x.set_unit_node_defaults(node, defaults, setup_undo_redo=True, print_python_command=False) -> bool
Adds a Function / Struct Node to the edited Graph.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

Args:
    node (RigVMUnitNode): 
    defaults (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_schema_class"></a>

#### set_schema_class

```python
def set_schema_class(schema_class: Class) -> None
```

x.set_schema_class(schema_class) -> None
Sets the schema class on the controller

Args:
    schema_class (type(Class)):

<a id="unreal.RigVMController.set_schema"></a>

#### set_schema

```python
def set_schema(schema: RigVMSchema) -> None
```

x.set_schema(schema) -> None
Set Schema
deprecated: Function has been deprecated, please use SetSchemaClass instead.

Args:
    schema (RigVMSchema):

<a id="unreal.RigVMController.set_remapped_variable"></a>

#### set_remapped_variable

```python
def set_remapped_variable(function_ref_node: RigVMFunctionReferenceNode,
                          inner_variable_name: Name,
                          outer_variable_name: Name,
                          setup_undo_redo: bool = True) -> bool
```

x.set_remapped_variable(function_ref_node, inner_variable_name, outer_variable_name, setup_undo_redo=True) -> bool
Sets the remapped variable on a function reference node

Args:
    function_ref_node (RigVMFunctionReferenceNode): 
    inner_variable_name (Name): 
    outer_variable_name (Name): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_is_watched"></a>

#### set_pin_is_watched

```python
def set_pin_is_watched(pin_path: str,
                       is_watched: bool,
                       setup_undo_redo: bool = True) -> bool
```

x.set_pin_is_watched(pin_path, is_watched, setup_undo_redo=True) -> bool
Sets the pin to be watched (or not)
This causes a PinWatchedChanged modified event.

Args:
    pin_path (str): 
    is_watched (bool): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_index_in_category"></a>

#### set_pin_index_in_category

```python
def set_pin_index_in_category(pin_path: str,
                              index_in_category: int,
                              setup_undo_redo: bool = True,
                              print_python_command: bool = False) -> bool
```

x.set_pin_index_in_category(pin_path, index_in_category, setup_undo_redo=True, print_python_command=False) -> bool
Changes a pin category's expansion state. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    pin_path (str): 
    index_in_category (int32): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_expansion"></a>

#### set_pin_expansion

```python
def set_pin_expansion(pin_path: str,
                      is_expanded: bool,
                      setup_undo_redo: bool = True,
                      print_python_command: bool = False) -> bool
```

x.set_pin_expansion(pin_path, is_expanded, setup_undo_redo=True, print_python_command=False) -> bool
Sets the pin to be expanded or not
This causes a PinExpansionChanged modified event.

Args:
    pin_path (str): 
    is_expanded (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_display_name"></a>

#### set_pin_display_name

```python
def set_pin_display_name(pin_path: str,
                         display_name: str,
                         setup_undo_redo: bool = True,
                         print_python_command: bool = False) -> bool
```

x.set_pin_display_name(pin_path, display_name, setup_undo_redo=True, print_python_command=False) -> bool
Sets the pin display name. The display name is UI relevant only.

Args:
    pin_path (str): 
    display_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_default_value"></a>

#### set_pin_default_value

```python
def set_pin_default_value(pin_path: str,
                          default_value: str,
                          resize_arrays: bool = True,
                          setup_undo_redo: bool = True,
                          merge_undo_action: bool = False,
                          print_python_command: bool = False,
                          set_value_on_linked_pins: bool = True) -> bool
```

x.set_pin_default_value(pin_path, default_value, resize_arrays=True, setup_undo_redo=True, merge_undo_action=False, print_python_command=False, set_value_on_linked_pins=True) -> bool
Sets the default value of a pin given its pinpath.
This causes a PinDefaultValueChanged modified event.

Args:
    pin_path (str): 
    default_value (str): 
    resize_arrays (bool): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 
    set_value_on_linked_pins (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_category_index"></a>

#### set_pin_category_index

```python
def set_pin_category_index(node_name: Name,
                           pin_category: str,
                           new_index: int,
                           setup_undo_redo: bool = True,
                           print_python_command: bool = False) -> bool
```

x.set_pin_category_index(node_name, pin_category, new_index, setup_undo_redo=True, print_python_command=False) -> bool
Changes a pin category's index. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    node_name (Name): 
    pin_category (str): 
    new_index (int32): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_category_expansion"></a>

#### set_pin_category_expansion

```python
def set_pin_category_expansion(node_name: Name,
                               pin_category: str,
                               is_expanded: bool,
                               setup_undo_redo: bool = True,
                               print_python_command: bool = False) -> bool
```

x.set_pin_category_expansion(node_name, pin_category, is_expanded, setup_undo_redo=True, print_python_command=False) -> bool
Changes a pin category's expansion state. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    node_name (Name): 
    pin_category (str): 
    is_expanded (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_pin_category"></a>

#### set_pin_category

```python
def set_pin_category(pin_path: str,
                     category: str,
                     setup_undo_redo: bool = True,
                     print_python_command: bool = False) -> bool
```

x.set_pin_category(pin_path, category, setup_undo_redo=True, print_python_command=False) -> bool
Sets the pin category. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    pin_path (str): 
    category (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_size_by_name"></a>

#### set_node_size_by_name

```python
def set_node_size_by_name(node_name: Name,
                          size: Vector2D,
                          setup_undo_redo: bool = True,
                          merge_undo_action: bool = False,
                          print_python_command: bool = False) -> bool
```

x.set_node_size_by_name(node_name, size, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the size of a node in the graph by name.
This causes a NodeSizeChanged modified event.

Args:
    node_name (Name): 
    size (Vector2D): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_size"></a>

#### set_node_size

```python
def set_node_size(node: RigVMNode,
                  size: Vector2D,
                  setup_undo_redo: bool = True,
                  merge_undo_action: bool = False,
                  print_python_command: bool = False) -> bool
```

x.set_node_size(node, size, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the size of a node in the graph.
This causes a NodeSizeChanged modified event.

Args:
    node (RigVMNode): 
    size (Vector2D): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_selection"></a>

#### set_node_selection

```python
def set_node_selection(node_names: Array[Name],
                       setup_undo_redo: bool = True,
                       print_python_command: bool = False) -> bool
```

x.set_node_selection(node_names, setup_undo_redo=True, print_python_command=False) -> bool
Selects the nodes given the selection
This might cause several NodeDeselected modified event.

Args:
    node_names (Array[Name]): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_position_by_name"></a>

#### set_node_position_by_name

```python
def set_node_position_by_name(node_name: Name,
                              position: Vector2D,
                              setup_undo_redo: bool = True,
                              merge_undo_action: bool = False,
                              print_python_command: bool = False) -> bool
```

x.set_node_position_by_name(node_name, position, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the position of a node in the graph by name.
This causes a NodePositionChanged modified event.

Args:
    node_name (Name): 
    position (Vector2D): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_position"></a>

#### set_node_position

```python
def set_node_position(node: RigVMNode,
                      position: Vector2D,
                      setup_undo_redo: bool = True,
                      merge_undo_action: bool = False,
                      print_python_command: bool = False) -> bool
```

x.set_node_position(node, position, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the position of a node in the graph.
This causes a NodePositionChanged modified event.

Args:
    node (RigVMNode): 
    position (Vector2D): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_layout"></a>

#### set_node_layout

```python
def set_node_layout(node_name: Name,
                    layout: RigVMNodeLayout,
                    setup_undo_redo: bool = True,
                    print_python_command: bool = False) -> bool
```

x.set_node_layout(node_name, layout, setup_undo_redo=True, print_python_command=False) -> bool
Applies a complete node layout to a node

Args:
    node_name (Name): 
    layout (RigVMNodeLayout): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_keywords_by_name"></a>

#### set_node_keywords_by_name

```python
def set_node_keywords_by_name(node_name: Name,
                              keywords: str,
                              setup_undo_redo: bool = True,
                              merge_undo_action: bool = False) -> bool
```

x.set_node_keywords_by_name(node_name, keywords, setup_undo_redo=True, merge_undo_action=False) -> bool
Sets the keywords of a node in the graph.
This causes a NodeKeywordsChanged modified event.

Args:
    node_name (Name): 
    keywords (str): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_keywords"></a>

#### set_node_keywords

```python
def set_node_keywords(node: RigVMCollapseNode,
                      keywords: str,
                      setup_undo_redo: bool = True,
                      merge_undo_action: bool = False,
                      print_python_command: bool = False) -> bool
```

x.set_node_keywords(node, keywords, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the keywords of a node in the graph.
This causes a NodeKeywordsChanged modified event.

Args:
    node (RigVMCollapseNode): 
    keywords (str): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_description_by_name"></a>

#### set_node_description_by_name

```python
def set_node_description_by_name(node_name: Name,
                                 description: str,
                                 setup_undo_redo: bool = True,
                                 merge_undo_action: bool = False) -> bool
```

x.set_node_description_by_name(node_name, description, setup_undo_redo=True, merge_undo_action=False) -> bool
Sets the keywords of a node in the graph.
This causes a NodeDescriptionChanged modified event.

Args:
    node_name (Name): 
    description (str): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_description"></a>

#### set_node_description

```python
def set_node_description(node: RigVMCollapseNode,
                         description: str,
                         setup_undo_redo: bool = True,
                         merge_undo_action: bool = False,
                         print_python_command: bool = False) -> bool
```

x.set_node_description(node, description, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the function description of a node in the graph.
This causes a NodeDescriptionChanged modified event.

Args:
    node (RigVMCollapseNode): 
    description (str): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_color_by_name"></a>

#### set_node_color_by_name

```python
def set_node_color_by_name(node_name: Name,
                           color: LinearColor,
                           setup_undo_redo: bool = True,
                           merge_undo_action: bool = False) -> bool
```

x.set_node_color_by_name(node_name, color, setup_undo_redo=True, merge_undo_action=False) -> bool
Sets the color of a node in the graph by name.
This causes a NodeColorChanged modified event.

Args:
    node_name (Name): 
    color (LinearColor): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_color"></a>

#### set_node_color

```python
def set_node_color(node: RigVMNode,
                   color: LinearColor,
                   setup_undo_redo: bool = True,
                   merge_undo_action: bool = False,
                   print_python_command: bool = False) -> bool
```

x.set_node_color(node, color, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the color of a node in the graph.
This causes a NodeColorChanged modified event.

Args:
    node (RigVMNode): 
    color (LinearColor): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_category_by_name"></a>

#### set_node_category_by_name

```python
def set_node_category_by_name(node_name: Name,
                              category: str,
                              setup_undo_redo: bool = True,
                              merge_undo_action: bool = False) -> bool
```

x.set_node_category_by_name(node_name, category, setup_undo_redo=True, merge_undo_action=False) -> bool
Sets the category of a node in the graph.
This causes a NodeCategoryChanged modified event.

Args:
    node_name (Name): 
    category (str): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_node_category"></a>

#### set_node_category

```python
def set_node_category(node: RigVMCollapseNode,
                      category: str,
                      setup_undo_redo: bool = True,
                      merge_undo_action: bool = False,
                      print_python_command: bool = False) -> bool
```

x.set_node_category(node, category, setup_undo_redo=True, merge_undo_action=False, print_python_command=False) -> bool
Sets the category of a node in the graph.
This causes a NodeCategoryChanged modified event.

Args:
    node (RigVMCollapseNode): 
    category (str): 
    setup_undo_redo (bool): 
    merge_undo_action (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_local_variable_type_from_object_path"></a>

#### set_local_variable_type_from_object_path

```python
def set_local_variable_type_from_object_path(
        variable_name: Name,
        cpp_type: str,
        cpp_type_object_path: str,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.set_local_variable_type_from_object_path(variable_name, cpp_type, cpp_type_object_path, setup_undo_redo=True, print_python_command=False) -> bool
Set Local Variable Type from Object Path

Args:
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_local_variable_type"></a>

#### set_local_variable_type

```python
def set_local_variable_type(variable_name: Name,
                            cpp_type: str,
                            cpp_type_object: Object,
                            setup_undo_redo: bool = True,
                            print_python_command: bool = False) -> bool
```

x.set_local_variable_type(variable_name, cpp_type, cpp_type_object, setup_undo_redo=True, print_python_command=False) -> bool
Sets the type of the local variable

Args:
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object (Object): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_local_variable_default_value"></a>

#### set_local_variable_default_value

```python
def set_local_variable_default_value(
        variable_name: Name,
        default_value: str,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.set_local_variable_default_value(variable_name, default_value, setup_undo_redo=True, print_python_command=False) -> bool
Set Local Variable Default Value

Args:
    variable_name (Name): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_is_running_unit_test"></a>

#### set_is_running_unit_test

```python
def set_is_running_unit_test(is_running: bool) -> None
```

x.set_is_running_unit_test(is_running) -> None
Helper function to disable a series of checks that can be ignored during a unit test

Args:
    is_running (bool):

<a id="unreal.RigVMController.set_graph"></a>

#### set_graph

```python
def set_graph(graph: RigVMGraph) -> None
```

x.set_graph(graph) -> None
Sets the currently edited Graph of this controller.
This causes a GraphChanged modified event.
deprecated: Function has been deprecated, please rely on GetControllerForGraph instead.

Args:
    graph (RigVMGraph):

<a id="unreal.RigVMController.set_exposed_pin_index"></a>

#### set_exposed_pin_index

```python
def set_exposed_pin_index(pin_name: Name,
                          new_index: int,
                          setup_undo_redo: bool = True,
                          print_python_command: bool = False) -> bool
```

x.set_exposed_pin_index(pin_name, new_index, setup_undo_redo=True, print_python_command=False) -> bool
Sets the index for an exposed pin. This can be used to move the pin up and down on the node.

Args:
    pin_name (Name): 
    new_index (int32): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_comment_text_by_name"></a>

#### set_comment_text_by_name

```python
def set_comment_text_by_name(node_name: Name,
                             comment_text: str,
                             comment_font_size: int,
                             comment_bubble_visible: bool,
                             comment_color_bubble: bool,
                             setup_undo_redo: bool = True,
                             print_python_command: bool = False) -> bool
```

x.set_comment_text_by_name(node_name, comment_text, comment_font_size, comment_bubble_visible, comment_color_bubble, setup_undo_redo=True, print_python_command=False) -> bool
Sets the comment text and properties of a comment node in the graph by name.
This causes a CommentTextChanged modified event.

Args:
    node_name (Name): 
    comment_text (str): 
    comment_font_size (int32): 
    comment_bubble_visible (bool): 
    comment_color_bubble (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_comment_text"></a>

#### set_comment_text

```python
def set_comment_text(node: RigVMNode,
                     comment_text: str,
                     comment_font_size: int,
                     comment_bubble_visible: bool,
                     comment_color_bubble: bool,
                     setup_undo_redo: bool = True,
                     print_python_command: bool = False) -> bool
```

x.set_comment_text(node, comment_text, comment_font_size, comment_bubble_visible, comment_color_bubble, setup_undo_redo=True, print_python_command=False) -> bool
Sets the comment text and properties of a comment node in the graph.
This causes a CommentTextChanged modified event.

Args:
    node (RigVMNode): 
    comment_text (str): 
    comment_font_size (int32): 
    comment_bubble_visible (bool): 
    comment_color_bubble (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_array_pin_size"></a>

#### set_array_pin_size

```python
def set_array_pin_size(array_pin_path: str,
                       size: int,
                       default_value: str = "",
                       setup_undo_redo: bool = True,
                       print_python_command: bool = False) -> bool
```

x.set_array_pin_size(array_pin_path, size, default_value="", setup_undo_redo=True, print_python_command=False) -> bool
Sets the size of the array pin
This causes a PinArraySizeChanged modified event.

Args:
    array_pin_path (str): 
    size (int32): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.set_action_stack"></a>

#### set_action_stack

```python
def set_action_stack(action_stack: RigVMActionStack) -> None
```

x.set_action_stack(action_stack) -> None
Set Action Stack

Args:
    action_stack (RigVMActionStack):

<a id="unreal.RigVMController.select_node_by_name"></a>

#### select_node_by_name

```python
def select_node_by_name(node_name: Name,
                        select: bool = True,
                        setup_undo_redo: bool = True) -> bool
```

x.select_node_by_name(node_name, select=True, setup_undo_redo=True) -> bool
Selects a single node in the graph by name.
This causes a NodeSelected / NodeDeselected modified event.

Args:
    node_name (Name): 
    select (bool): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.select_node"></a>

#### select_node

```python
def select_node(node: RigVMNode,
                select: bool = True,
                setup_undo_redo: bool = True,
                print_python_command: bool = False) -> bool
```

x.select_node(node, select=True, setup_undo_redo=True, print_python_command=False) -> bool
Selects a single node in the graph.
This causes a NodeSelected / NodeDeselected modified event.

Args:
    node (RigVMNode): 
    select (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.resolve_wild_card_pin"></a>

#### resolve_wild_card_pin

```python
def resolve_wild_card_pin(pin_path: str,
                          cpp_type: str,
                          cpp_type_object_path: Name,
                          setup_undo_redo: bool = True,
                          print_python_command: bool = False) -> bool
```

x.resolve_wild_card_pin(pin_path, cpp_type, cpp_type_object_path, setup_undo_redo=True, print_python_command=False) -> bool
Resolves a wildcard pin on any node

Args:
    pin_path (str): 
    cpp_type (str): 
    cpp_type_object_path (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.reset_pin_default_value"></a>

#### reset_pin_default_value

```python
def reset_pin_default_value(pin_path: str,
                            setup_undo_redo: bool = True,
                            print_python_command: bool = False) -> bool
```

x.reset_pin_default_value(pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Resets the default value of a pin given its pinpath.
This causes a PinDefaultValueChanged modified event.

Args:
    pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.replace_parameter_node_with_variable"></a>

#### replace_parameter_node_with_variable

```python
def replace_parameter_node_with_variable(
        node_name: Name, variable_name: Name, cpp_type: str,
        cpp_type_object: Object, setup_undo_redo: bool) -> RigVMVariableNode
```

x.replace_parameter_node_with_variable(node_name, variable_name, cpp_type, cpp_type_object, setup_undo_redo) -> RigVMVariableNode
Refreshes the variable node with the new data

Args:
    node_name (Name): 
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object (Object): 
    setup_undo_redo (bool): 

Returns:
    RigVMVariableNode:

<a id="unreal.RigVMController.rename_variable"></a>

#### rename_variable

```python
def rename_variable(old_name: Name,
                    new_name: Name,
                    setup_undo_redo: bool = True) -> bool
```

x.rename_variable(old_name, new_name, setup_undo_redo=True) -> bool
Renames a variable in the graph.
This causes a VariableRenamed modified event.
deprecated: Function 'RenameVariable' is deprecated.

Args:
    old_name (Name): 
    new_name (Name): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.rename_pin_category"></a>

#### rename_pin_category

```python
def rename_pin_category(node_name: Name,
                        old_pin_category: str,
                        new_pin_category: str,
                        setup_undo_redo: bool = True,
                        print_python_command: bool = False) -> bool
```

x.rename_pin_category(node_name, old_pin_category, new_pin_category, setup_undo_redo=True, print_python_command=False) -> bool
Renames a pin category. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    node_name (Name): 
    old_pin_category (str): 
    new_pin_category (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.rename_parameter"></a>

#### rename_parameter

```python
def rename_parameter(old_name: Name,
                     new_name: Name,
                     setup_undo_redo: bool = True) -> bool
```

x.rename_parameter(old_name, new_name, setup_undo_redo=True) -> bool
Renames a parameter in the graph.
This causes a ParameterRenamed modified event.
deprecated: Function 'RenameParameter' is deprecated.

Args:
    old_name (Name): 
    new_name (Name): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.rename_node"></a>

#### rename_node

```python
def rename_node(node: RigVMNode,
                new_name: Name,
                setup_undo_redo: bool = True,
                print_python_command: bool = False) -> bool
```

x.rename_node(node, new_name, setup_undo_redo=True, print_python_command=False) -> bool
Renames a node in the graph
This causes a NodeRenamed modified event.

Args:
    node (RigVMNode): 
    new_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.rename_local_variable"></a>

#### rename_local_variable

```python
def rename_local_variable(variable_name: Name,
                          new_variable_name: Name,
                          setup_undo_redo: bool = True,
                          print_python_command: bool = False) -> bool
```

x.rename_local_variable(variable_name, new_variable_name, setup_undo_redo=True, print_python_command=False) -> bool
Rename a local variable from the graph

Args:
    variable_name (Name): 
    new_variable_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.rename_function"></a>

#### rename_function

```python
def rename_function(old_function_name: Name,
                    new_function_name: Name,
                    setup_undo_redo: bool = True) -> bool
```

x.rename_function(old_function_name, new_function_name, setup_undo_redo=True) -> bool
Renames a function in the function library

Args:
    old_function_name (Name): 
    new_function_name (Name): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.rename_exposed_pin"></a>

#### rename_exposed_pin

```python
def rename_exposed_pin(old_pin_name: Name,
                       new_pin_name: Name,
                       setup_undo_redo: bool = True,
                       print_python_command: bool = False) -> bool
```

x.rename_exposed_pin(old_pin_name, new_pin_name, setup_undo_redo=True, print_python_command=False) -> bool
Renames an exposed pin in the graph controlled by this

Args:
    old_pin_name (Name): 
    new_pin_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_trait"></a>

#### remove_trait

```python
def remove_trait(node_name: Name,
                 trait_name: Name,
                 setup_undo_redo: bool = True,
                 print_python_command: bool = False) -> bool
```

x.remove_trait(node_name, trait_name, setup_undo_redo=True, print_python_command=False) -> bool
Removes a trait from a node

Args:
    node_name (Name): 
    trait_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_tag_from_function_variant"></a>

#### remove_tag_from_function_variant

```python
def remove_tag_from_function_variant(
        function_name: Name,
        tag_name: Name,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.remove_tag_from_function_variant(function_name, tag_name, setup_undo_redo=True, print_python_command=False) -> bool
Adds a tag to a function variant

Args:
    function_name (Name): 
    tag_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_pin_category"></a>

#### remove_pin_category

```python
def remove_pin_category(node_name: Name,
                        pin_category: str,
                        setup_undo_redo: bool = True,
                        print_python_command: bool = False) -> bool
```

x.remove_pin_category(node_name, pin_category, setup_undo_redo=True, print_python_command=False) -> bool
Removes a pin category. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    node_name (Name): 
    pin_category (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_nodes_by_name"></a>

#### remove_nodes_by_name

```python
def remove_nodes_by_name(node_names: Array[Name],
                         setup_undo_redo: bool = True,
                         print_python_command: bool = False) -> bool
```

x.remove_nodes_by_name(node_names, setup_undo_redo=True, print_python_command=False) -> bool
Removes a list of nodes from the graph given the names
This causes a NodeRemoved modified event.

Args:
    node_names (Array[Name]): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_nodes"></a>

#### remove_nodes

```python
def remove_nodes(nodes: Array[RigVMNode],
                 setup_undo_redo: bool = True,
                 print_python_command: bool = False) -> bool
```

x.remove_nodes(nodes, setup_undo_redo=True, print_python_command=False) -> bool
Removes a list of nodes from the graph
This causes a NodeRemoved modified event.

Args:
    nodes (Array[RigVMNode]): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_node_by_name"></a>

#### remove_node_by_name

```python
def remove_node_by_name(node_name: Name,
                        setup_undo_redo: bool = True,
                        print_python_command: bool = False) -> bool
```

x.remove_node_by_name(node_name, setup_undo_redo=True, print_python_command=False) -> bool
Removes a node from the graph given the node's name.
This causes a NodeRemoved modified event.

Args:
    node_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_node"></a>

#### remove_node

```python
def remove_node(node: RigVMNode,
                setup_undo_redo: bool = True,
                print_python_command: bool = False) -> bool
```

x.remove_node(node, setup_undo_redo=True, print_python_command=False) -> bool
Removes a node from the graph
This causes a NodeRemoved modified event.

Args:
    node (RigVMNode): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_local_variable"></a>

#### remove_local_variable

```python
def remove_local_variable(variable_name: Name,
                          setup_undo_redo: bool = True,
                          print_python_command: bool = False) -> bool
```

x.remove_local_variable(variable_name, setup_undo_redo=True, print_python_command=False) -> bool
Remove a local variable from the graph

Args:
    variable_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_injected_node"></a>

#### remove_injected_node

```python
def remove_injected_node(pin_path: str,
                         as_input: bool,
                         setup_undo_redo: bool = True,
                         print_python_command: bool = False) -> bool
```

x.remove_injected_node(pin_path, as_input, setup_undo_redo=True, print_python_command=False) -> bool
Removes an injected node
This causes a NodeRemoved modified event.

Args:
    pin_path (str): 
    as_input (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_function_from_library"></a>

#### remove_function_from_library

```python
def remove_function_from_library(function_name: Name,
                                 setup_undo_redo: bool = True) -> bool
```

x.remove_function_from_library(function_name, setup_undo_redo=True) -> bool
Removes a function from a function library graph

Args:
    function_name (Name): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_exposed_pin"></a>

#### remove_exposed_pin

```python
def remove_exposed_pin(pin_name: Name,
                       setup_undo_redo: bool = True,
                       print_python_command: bool = False) -> bool
```

x.remove_exposed_pin(pin_name, setup_undo_redo=True, print_python_command=False) -> bool
Removes an exposed pin from the graph controlled by this

Args:
    pin_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_array_pin"></a>

#### remove_array_pin

```python
def remove_array_pin(array_element_pin_path: str,
                     setup_undo_redo: bool = True,
                     print_python_command: bool = False) -> bool
```

x.remove_array_pin(array_element_pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Removes an array element pin from an array pin.
This causes a PinArraySizeChanged modified event.

Args:
    array_element_pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.remove_aggregate_pin"></a>

#### remove_aggregate_pin

```python
def remove_aggregate_pin(pin_path: str,
                         setup_undo_redo: bool = True,
                         print_python_command: bool = False) -> bool
```

x.remove_aggregate_pin(pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Remove Aggregate Pin

Args:
    pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.refresh_variable_node"></a>

#### refresh_variable_node

```python
def refresh_variable_node(node_name: Name,
                          variable_name: Name,
                          cpp_type: str,
                          cpp_type_object: Object,
                          setup_undo_redo: bool,
                          setup_orphan_pins: bool = True) -> None
```

x.refresh_variable_node(node_name, variable_name, cpp_type, cpp_type_object, setup_undo_redo, setup_orphan_pins=True) -> None
Refreshes the variable node with the new data

Args:
    node_name (Name): 
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object (Object): 
    setup_undo_redo (bool): 
    setup_orphan_pins (bool):

<a id="unreal.RigVMController.redo"></a>

#### redo

```python
def redo() -> bool
```

x.redo() -> bool
Re-does the last action on the stack.
Note: This should really only be used for unit tests,
use the GEditor's main Undo method instead.

Returns:
    bool:

<a id="unreal.RigVMController.push_graph"></a>

#### push_graph

```python
def push_graph(graph: RigVMGraph, setup_undo_redo: bool = True) -> bool
```

x.push_graph(graph, setup_undo_redo=True) -> bool
Pushes a new graph to the stack
This causes a GraphChanged modified event.
deprecated: Function has been deprecated, please rely on GetControllerForGraph instead.

Args:
    graph (RigVMGraph): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.promote_pin_to_variable"></a>

#### promote_pin_to_variable

```python
def promote_pin_to_variable(pin_path: str,
                            create_variable_node: bool,
                            node_position: Vector2D = [0.000000, 0.000000],
                            setup_undo_redo: bool = True,
                            print_python_command: bool = False) -> bool
```

x.promote_pin_to_variable(pin_path, create_variable_node, node_position=[0.000000, 0.000000], setup_undo_redo=True, print_python_command=False) -> bool
Promotes a pin to a variable

Args:
    pin_path (str): 
    create_variable_node (bool): 
    node_position (Vector2D): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.promote_function_reference_node_to_collapse_node"></a>

#### promote_function_reference_node_to_collapse_node

```python
def promote_function_reference_node_to_collapse_node(
        node_name: Name,
        setup_undo_redo: bool = True,
        print_python_command: bool = False,
        remove_function_definition: bool = False) -> Name
```

x.promote_function_reference_node_to_collapse_node(node_name, setup_undo_redo=True, print_python_command=False, remove_function_definition=False) -> Name
Turns a collapse node into a function node

Args:
    node_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 
    remove_function_definition (bool): 

Returns:
    Name:

<a id="unreal.RigVMController.promote_collapse_node_to_function_reference_node"></a>

#### promote_collapse_node_to_function_reference_node

```python
def promote_collapse_node_to_function_reference_node(
        node_name: Name,
        setup_undo_redo: bool = True,
        print_python_command: bool = False,
        existing_function_definition_path: str = "") -> Name
```

x.promote_collapse_node_to_function_reference_node(node_name, setup_undo_redo=True, print_python_command=False, existing_function_definition_path="") -> Name
Turns a collapse node into a function node

Args:
    node_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 
    existing_function_definition_path (str): 

Returns:
    Name:

<a id="unreal.RigVMController.pop_graph"></a>

#### pop_graph

```python
def pop_graph(setup_undo_redo: bool = True) -> RigVMGraph
```

x.pop_graph(setup_undo_redo=True) -> RigVMGraph
Pops the last graph off the stack
This causes a GraphChanged modified event.
deprecated: Function has been deprecated, please rely on GetControllerForGraph instead.

Args:
    setup_undo_redo (bool): 

Returns:
    RigVMGraph:

<a id="unreal.RigVMController.perform_user_workflow"></a>

#### perform_user_workflow

```python
def perform_user_workflow(workflow: RigVMUserWorkflow,
                          options: RigVMUserWorkflowOptions,
                          setup_undo_redo: bool = True) -> bool
```

x.perform_user_workflow(workflow, options, setup_undo_redo=True) -> bool
performs all actions representing the workflow

Args:
    workflow (RigVMUserWorkflow): 
    options (RigVMUserWorkflowOptions): 
    setup_undo_redo (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.open_undo_bracket"></a>

#### open_undo_bracket

```python
def open_undo_bracket(title: str) -> bool
```

x.open_undo_bracket(title) -> bool
Opens an undo bracket / scoped transaction for
a series of actions to be performed as one step on the
Undo stack. This is primarily useful for Python.
This causes a UndoBracketOpened modified event.

Args:
    title (str): 

Returns:
    bool:

<a id="unreal.RigVMController.mark_function_as_public"></a>

#### mark_function_as_public

```python
def mark_function_as_public(function_name: Name,
                            is_public: bool,
                            setup_undo_redo: bool = True,
                            print_python_command: bool = False) -> bool
```

x.mark_function_as_public(function_name, is_public, setup_undo_redo=True, print_python_command=False) -> bool
Mark a function as public/private in the function library

Args:
    function_name (Name): 
    is_public (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.make_variable_node_from_binding"></a>

#### make_variable_node_from_binding

```python
def make_variable_node_from_binding(
        pin_path: str,
        node_position: Vector2D = [0.000000, 0.000000],
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.make_variable_node_from_binding(pin_path, node_position=[0.000000, 0.000000], setup_undo_redo=True, print_python_command=False) -> bool
Turns a binding to a variable node

Args:
    pin_path (str): 
    node_position (Vector2D): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.make_options_for_workflow"></a>

#### make_options_for_workflow

```python
def make_options_for_workflow(
        subject: Object,
        workflow: RigVMUserWorkflow) -> RigVMUserWorkflowOptions
```

x.make_options_for_workflow(subject, workflow) -> RigVMUserWorkflowOptions
creates the options struct for a given workflow

Args:
    subject (Object): 
    workflow (RigVMUserWorkflow): 

Returns:
    RigVMUserWorkflowOptions:

<a id="unreal.RigVMController.make_bindings_from_variable_node"></a>

#### make_bindings_from_variable_node

```python
def make_bindings_from_variable_node(
        node_name: Name,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.make_bindings_from_variable_node(node_name, setup_undo_redo=True, print_python_command=False) -> bool
Turns a variable node into one or more bindings

Args:
    node_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.localize_functions"></a>

#### localize_functions

```python
def localize_functions(
    function_definitions: Array[RigVMGraphFunctionIdentifier],
    localize_dependent_private_functions: bool = True,
    setup_undo_redo: bool = True,
    print_python_command: bool = False
) -> Map[RigVMGraphFunctionIdentifier, RigVMLibraryNode]
```

x.localize_functions(function_definitions, localize_dependent_private_functions=True, setup_undo_redo=True, print_python_command=False) -> Map[RigVMGraphFunctionIdentifier, RigVMLibraryNode]
Copies a series of function declaratioms into this graph's local function library

Args:
    function_definitions (Array[RigVMGraphFunctionIdentifier]): 
    localize_dependent_private_functions (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    Map[RigVMGraphFunctionIdentifier, RigVMLibraryNode]:

<a id="unreal.RigVMController.localize_function_from_path"></a>

#### localize_function_from_path

```python
def localize_function_from_path(
        host_path: str,
        function_name: Name,
        localize_dependent_private_functions: bool = True,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMLibraryNode
```

x.localize_function_from_path(host_path, function_name, localize_dependent_private_functions=True, setup_undo_redo=True, print_python_command=False) -> RigVMLibraryNode
Copies a function declaration into this graph's local function library

Args:
    host_path (str): 
    function_name (Name): 
    localize_dependent_private_functions (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMController.localize_function"></a>

#### localize_function

```python
def localize_function(function_definition: RigVMGraphFunctionIdentifier,
                      localize_dependent_private_functions: bool = True,
                      setup_undo_redo: bool = True,
                      print_python_command: bool = False) -> RigVMLibraryNode
```

x.localize_function(function_definition, localize_dependent_private_functions=True, setup_undo_redo=True, print_python_command=False) -> RigVMLibraryNode
Localize Function

Args:
    function_definition (RigVMGraphFunctionIdentifier): 
    localize_dependent_private_functions (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMController.join_function_variant"></a>

#### join_function_variant

```python
def join_function_variant(function_name: Name,
                          guid: Guid,
                          setup_undo_redo: bool = True,
                          print_python_command: bool = False) -> bool
```

x.join_function_variant(function_name, guid, setup_undo_redo=True, print_python_command=False) -> bool
Merges the function's guid with a provided one to join the variant set

Args:
    function_name (Name): 
    guid (Guid): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.is_transacting"></a>

#### is_transacting

```python
def is_transacting() -> bool
```

x.is_transacting() -> bool
Returns true if the controller is currently transacting

Returns:
    bool:

<a id="unreal.RigVMController.is_reporting_enabled"></a>

#### is_reporting_enabled

```python
def is_reporting_enabled() -> bool
```

x.is_reporting_enabled() -> bool
Returns true if reporting is enabled

Returns:
    bool:

<a id="unreal.RigVMController.is_function_public"></a>

#### is_function_public

```python
def is_function_public(function_name: Name) -> bool
```

x.is_function_public(function_name) -> bool
Returns true if a function is marked as public in the function library

Args:
    function_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMController.insert_array_pin"></a>

#### insert_array_pin

```python
def insert_array_pin(array_pin_path: str,
                     index: int = -1,
                     default_value: str = "",
                     setup_undo_redo: bool = True,
                     print_python_command: bool = False) -> str
```

x.insert_array_pin(array_pin_path, index=-1, default_value="", setup_undo_redo=True, print_python_command=False) -> str
Inserts an array element pin into an array pin.
This causes a PinArraySizeChanged modified event.

Args:
    array_pin_path (str): 
    index (int32): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    str:

<a id="unreal.RigVMController.import_nodes_from_text"></a>

#### import_nodes_from_text

```python
def import_nodes_from_text(text: str,
                           setup_undo_redo: bool = True,
                           print_python_commands: bool = False) -> Array[Name]
```

x.import_nodes_from_text(text, setup_undo_redo=True, print_python_commands=False) -> Array[Name]
Exports the given nodes as text

Args:
    text (str): 
    setup_undo_redo (bool): 
    print_python_commands (bool): 

Returns:
    Array[Name]:

<a id="unreal.RigVMController.get_unit_structs_for_template"></a>

#### get_unit_structs_for_template

```python
@classmethod
def get_unit_structs_for_template(cls, notation: Name) -> Array[ScriptStruct]
```

X.get_unit_structs_for_template(notation) -> Array[ScriptStruct]
Returns all supported unit structs for a given template notation

Args:
    notation (Name): 

Returns:
    Array[ScriptStruct]:

<a id="unreal.RigVMController.get_top_level_graph"></a>

#### get_top_level_graph

```python
def get_top_level_graph() -> RigVMGraph
```

x.get_top_level_graph() -> RigVMGraph
Returns the top level graph

Returns:
    RigVMGraph:

<a id="unreal.RigVMController.get_template_for_unit_struct"></a>

#### get_template_for_unit_struct

```python
@classmethod
def get_template_for_unit_struct(cls,
                                 function: ScriptStruct,
                                 method_name: str = "Execute") -> str
```

X.get_template_for_unit_struct(function, method_name="Execute") -> str
Returns the template for a given function (or an empty string)

Args:
    function (ScriptStruct): 
    method_name (str): 

Returns:
    str:

<a id="unreal.RigVMController.get_schema"></a>

#### get_schema

```python
def get_schema() -> RigVMSchema
```

x.get_schema() -> RigVMSchema
Returns the schema used by this controller

Returns:
    RigVMSchema:

<a id="unreal.RigVMController.get_registered_unit_structs"></a>

#### get_registered_unit_structs

```python
@classmethod
def get_registered_unit_structs(cls) -> Array[ScriptStruct]
```

X.get_registered_unit_structs() -> Array[ScriptStruct]
Returns all registered unit structs

Returns:
    Array[ScriptStruct]:

<a id="unreal.RigVMController.get_registered_templates"></a>

#### get_registered_templates

```python
@classmethod
def get_registered_templates(cls) -> Array[str]
```

X.get_registered_templates() -> Array[str]
Returns all registered template notations

Returns:
    Array[str]:

<a id="unreal.RigVMController.get_pin_default_value"></a>

#### get_pin_default_value

```python
def get_pin_default_value(pin_path: str) -> str
```

x.get_pin_default_value(pin_path) -> str
Returns the default value of a pin given its pinpath.

Args:
    pin_path (str): 

Returns:
    str:

<a id="unreal.RigVMController.get_graph"></a>

#### get_graph

```python
def get_graph() -> RigVMGraph
```

x.get_graph() -> RigVMGraph
Returns the currently edited Graph of this controller.

Returns:
    RigVMGraph:

<a id="unreal.RigVMController.get_controller_for_graph"></a>

#### get_controller_for_graph

```python
def get_controller_for_graph(graph: RigVMGraph) -> RigVMController
```

x.get_controller_for_graph(graph) -> RigVMController
Returns another controller for a given graph

Args:
    graph (RigVMGraph): 

Returns:
    RigVMController:

<a id="unreal.RigVMController.get_action_stack"></a>

#### get_action_stack

```python
def get_action_stack() -> RigVMActionStack
```

x.get_action_stack() -> RigVMActionStack
Get Action Stack

Returns:
    RigVMActionStack:

<a id="unreal.RigVMController.generate_python_commands"></a>

#### generate_python_commands

```python
def generate_python_commands() -> Array[str]
```

x.generate_python_commands() -> Array[str]
Generate Python Commands

Returns:
    Array[str]:

<a id="unreal.RigVMController.find_variants_of_function"></a>

#### find_variants_of_function

```python
def find_variants_of_function(function_name: Name) -> Array[RigVMVariantRef]
```

x.find_variants_of_function(function_name) -> Array[RigVMVariantRef]
Returns all variant refs related to the given function

Args:
    function_name (Name): 

Returns:
    Array[RigVMVariantRef]:

<a id="unreal.RigVMController.find_graph_function_identifier"></a>

#### find_graph_function_identifier

```python
def find_graph_function_identifier(
        host_path: str, function_name: Name) -> RigVMGraphFunctionIdentifier
```

x.find_graph_function_identifier(host_path, function_name) -> RigVMGraphFunctionIdentifier
Find Graph Function Identifier

Args:
    host_path (str): 
    function_name (Name): 

Returns:
    RigVMGraphFunctionIdentifier:

<a id="unreal.RigVMController.find_graph_function_header_by_name"></a>

#### find_graph_function_header_by_name

```python
def find_graph_function_header_by_name(
        host_path: str, function_name: Name) -> RigVMGraphFunctionHeader
```

x.find_graph_function_header_by_name(host_path, function_name) -> RigVMGraphFunctionHeader
Find Graph Function Header by Name

Args:
    host_path (str): 
    function_name (Name): 

Returns:
    RigVMGraphFunctionHeader:

<a id="unreal.RigVMController.find_graph_function_header"></a>

#### find_graph_function_header

```python
def find_graph_function_header(
    function_identifier: RigVMGraphFunctionIdentifier
) -> RigVMGraphFunctionHeader
```

x.find_graph_function_header(function_identifier) -> RigVMGraphFunctionHeader
Find Graph Function Header

Args:
    function_identifier (RigVMGraphFunctionIdentifier): 

Returns:
    RigVMGraphFunctionHeader:

<a id="unreal.RigVMController.export_selected_nodes_to_text"></a>

#### export_selected_nodes_to_text

```python
def export_selected_nodes_to_text(include_exterior_links: bool = False) -> str
```

x.export_selected_nodes_to_text(include_exterior_links=False) -> str
Exports the selected nodes as text

Args:
    include_exterior_links (bool): 

Returns:
    str:

<a id="unreal.RigVMController.export_nodes_to_text"></a>

#### export_nodes_to_text

```python
def export_nodes_to_text(node_names: Array[Name],
                         include_exterior_links: bool = False) -> str
```

x.export_nodes_to_text(node_names, include_exterior_links=False) -> str
Exports the given nodes as text

Args:
    node_names (Array[Name]): 
    include_exterior_links (bool): 

Returns:
    str:

<a id="unreal.RigVMController.expand_library_node"></a>

#### expand_library_node

```python
def expand_library_node(
        node_name: Name,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> Array[RigVMNode]
```

x.expand_library_node(node_name, setup_undo_redo=True, print_python_command=False) -> Array[RigVMNode]
Turns a library node into its contained nodes

Args:
    node_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    Array[RigVMNode]:

<a id="unreal.RigVMController.enable_reporting"></a>

#### enable_reporting

```python
def enable_reporting(enabled: bool = True) -> None
```

x.enable_reporting(enabled=True) -> None
Enables or disables the error reporting of this Controller.

Args:
    enabled (bool):

<a id="unreal.RigVMController.eject_node_from_pin"></a>

#### eject_node_from_pin

```python
def eject_node_from_pin(pin_path: str,
                        setup_undo_redo: bool = True,
                        print_python_command: bool = False) -> RigVMNode
```

x.eject_node_from_pin(pin_path, setup_undo_redo=True, print_python_command=False) -> RigVMNode
Ejects the last injected node on a pin

Args:
    pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.duplicate_array_pin"></a>

#### duplicate_array_pin

```python
def duplicate_array_pin(array_element_pin_path: str,
                        setup_undo_redo: bool = True,
                        print_python_command: bool = False) -> str
```

x.duplicate_array_pin(array_element_pin_path, setup_undo_redo=True, print_python_command=False) -> str
Duplicates an array element pin.
This causes a PinArraySizeChanged modified event.

Args:
    array_element_pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    str:

<a id="unreal.RigVMController.create_function_variant"></a>

#### create_function_variant

```python
def create_function_variant(
        function_name: Name,
        variant_name: Name = "None",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMLibraryNode
```

x.create_function_variant(function_name, variant_name="None", setup_undo_redo=True, print_python_command=False) -> RigVMLibraryNode
Creates a variant of a function given the name of an existing function variant

Args:
    function_name (Name): 
    variant_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMController.collapse_nodes"></a>

#### collapse_nodes

```python
def collapse_nodes(node_names: Array[Name],
                   collapse_node_name: str = "",
                   setup_undo_redo: bool = True,
                   print_python_command: bool = False,
                   is_aggregate: bool = False) -> RigVMCollapseNode
```

x.collapse_nodes(node_names, collapse_node_name="", setup_undo_redo=True, print_python_command=False, is_aggregate=False) -> RigVMCollapseNode
Turns a series of nodes into a Collapse node

Args:
    node_names (Array[Name]): 
    collapse_node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 
    is_aggregate (bool): 

Returns:
    RigVMCollapseNode:

<a id="unreal.RigVMController.close_undo_bracket"></a>

#### close_undo_bracket

```python
def close_undo_bracket() -> bool
```

x.close_undo_bracket() -> bool
Closes an undo bracket / scoped transaction.
This is primarily useful for Python.
This causes a UndoBracketClosed modified event.

Returns:
    bool:

<a id="unreal.RigVMController.clear_pin_category"></a>

#### clear_pin_category

```python
def clear_pin_category(pin_path: str,
                       setup_undo_redo: bool = True,
                       print_python_command: bool = False) -> bool
```

x.clear_pin_category(pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Clears the pin category. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.clear_node_selection"></a>

#### clear_node_selection

```python
def clear_node_selection(setup_undo_redo: bool = True,
                         print_python_command: bool = False) -> bool
```

x.clear_node_selection(setup_undo_redo=True, print_python_command=False) -> bool
Deselects all currently selected nodes in the graph.
This might cause several NodeDeselected modified event.

Args:
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.clear_node_layout"></a>

#### clear_node_layout

```python
def clear_node_layout(node_name: Name,
                      setup_undo_redo: bool = True,
                      print_python_command: bool = False) -> bool
```

x.clear_node_layout(node_name, setup_undo_redo=True, print_python_command=False) -> bool
Removes any layout information from a node

Args:
    node_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.clear_array_pin"></a>

#### clear_array_pin

```python
def clear_array_pin(array_pin_path: str,
                    setup_undo_redo: bool = True,
                    print_python_command: bool = False) -> bool
```

x.clear_array_pin(array_pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Removes all (but one) array element pin from an array pin.
This causes a PinArraySizeChanged modified event.

Args:
    array_pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.change_exposed_pin_type"></a>

#### change_exposed_pin_type

```python
def change_exposed_pin_type(
        pin_name: Name,
        cpp_type: str,
        cpp_type_object_path: Name,
        setup_undo_redo: bool,
        setup_orphan_pins: bool = True,
        print_python_command: bool = False) -> Optional[bool]
```

x.change_exposed_pin_type(pin_name, cpp_type, cpp_type_object_path, setup_undo_redo, setup_orphan_pins=True, print_python_command=False) -> bool or None
Changes the type of an exposed pin in the graph controlled by this

Args:
    pin_name (Name): 
    cpp_type (str): 
    cpp_type_object_path (Name): 
    setup_undo_redo (bool): 
    setup_orphan_pins (bool): 
    print_python_command (bool): 

Returns:
    bool or None: 

    setup_undo_redo (bool):

<a id="unreal.RigVMController.can_import_nodes_from_text"></a>

#### can_import_nodes_from_text

```python
def can_import_nodes_from_text(text: str) -> bool
```

x.can_import_nodes_from_text(text) -> bool
Exports the given nodes as text

Args:
    text (str): 

Returns:
    bool:

<a id="unreal.RigVMController.cancel_undo_bracket"></a>

#### cancel_undo_bracket

```python
def cancel_undo_bracket() -> bool
```

x.cancel_undo_bracket() -> bool
Cancels an undo bracket / scoped transaction.
This is primarily useful for Python.
This causes a UndoBracketCanceled modified event.

Returns:
    bool:

<a id="unreal.RigVMController.break_link"></a>

#### break_link

```python
def break_link(output_pin_path: str,
               input_pin_path: str,
               setup_undo_redo: bool = True,
               print_python_command: bool = False) -> bool
```

x.break_link(output_pin_path, input_pin_path, setup_undo_redo=True, print_python_command=False) -> bool
Removes a link from the graph.
This causes a LinkRemoved modified event.

Args:
    output_pin_path (str): 
    input_pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.break_all_links"></a>

#### break_all_links

```python
def break_all_links(pin_path: str,
                    as_input: bool = True,
                    setup_undo_redo: bool = True,
                    print_python_command: bool = False) -> bool
```

x.break_all_links(pin_path, as_input=True, setup_undo_redo=True, print_python_command=False) -> bool
Removes all links on a given pin from the graph.
This might cause multiple LinkRemoved modified event.

Args:
    pin_path (str): 
    as_input (bool): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.bind_pin_to_variable"></a>

#### bind_pin_to_variable

```python
def bind_pin_to_variable(pin_path: str,
                         new_bound_variable_path: str,
                         setup_undo_redo: bool = True,
                         print_python_command: bool = False) -> bool
```

x.bind_pin_to_variable(pin_path, new_bound_variable_path, setup_undo_redo=True, print_python_command=False) -> bool
Binds a pin to a variable (or removes the binding given NAME_None)
This causes a PinBoundVariableChanged modified event.

Args:
    pin_path (str): 
    new_bound_variable_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.add_variable_node_from_object_path"></a>

#### add_variable_node_from_object_path

```python
def add_variable_node_from_object_path(
        variable_name: Name,
        cpp_type: str,
        cpp_type_object_path: str,
        is_getter: bool,
        default_value: str,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMVariableNode
```

x.add_variable_node_from_object_path(variable_name, cpp_type, cpp_type_object_path, is_getter, default_value, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMVariableNode
Adds a Variable Node to the edited Graph given a struct object path name.
Variables represent local work state for the function and
can be read from (bIsGetter == true) or written to (bIsGetter == false).
This causes a NodeAdded modified event.

Args:
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object_path (str): 
    is_getter (bool): 
    default_value (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMVariableNode:

<a id="unreal.RigVMController.add_variable_node"></a>

#### add_variable_node

```python
def add_variable_node(variable_name: Name,
                      cpp_type: str,
                      cpp_type_object: Object,
                      is_getter: bool,
                      default_value: str,
                      position: Vector2D = [0.000000, 0.000000],
                      node_name: str = "",
                      setup_undo_redo: bool = True,
                      print_python_command: bool = False) -> RigVMVariableNode
```

x.add_variable_node(variable_name, cpp_type, cpp_type_object, is_getter, default_value, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMVariableNode
Adds a Variable Node to the edited Graph.
Variables represent local work state for the function and
can be read from and written to.
This causes a NodeAdded modified event.

Args:
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object (Object): 
    is_getter (bool): 
    default_value (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMVariableNode:

<a id="unreal.RigVMController.add_unit_node_with_defaults"></a>

#### add_unit_node_with_defaults

```python
def add_unit_node_with_defaults(
        script_struct: ScriptStruct,
        defaults: str,
        method_name: Name = "Execute",
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMUnitNode
```

x.add_unit_node_with_defaults(script_struct, defaults, method_name="Execute", position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMUnitNode
Adds a Function / Struct Node to the edited Graph.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

Args:
    script_struct (ScriptStruct): 
    defaults (str): 
    method_name (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMUnitNode:

<a id="unreal.RigVMController.add_unit_node_from_struct_path"></a>

#### add_unit_node_from_struct_path

```python
def add_unit_node_from_struct_path(
        script_struct_path: str,
        method_name: Name = "Execute",
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMUnitNode
```

x.add_unit_node_from_struct_path(script_struct_path, method_name="Execute", position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMUnitNode
Adds a Function / Struct Node to the edited Graph given its struct object path name.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

Args:
    script_struct_path (str): 
    method_name (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMUnitNode:

<a id="unreal.RigVMController.add_unit_node"></a>

#### add_unit_node

```python
def add_unit_node(script_struct: ScriptStruct,
                  method_name: Name = "Execute",
                  position: Vector2D = [0.000000, 0.000000],
                  node_name: str = "",
                  setup_undo_redo: bool = True,
                  print_python_command: bool = False) -> RigVMUnitNode
```

x.add_unit_node(script_struct, method_name="Execute", position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMUnitNode
Adds a Function / Struct Node to the edited Graph.
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

Args:
    script_struct (ScriptStruct): 
    method_name (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMUnitNode:

<a id="unreal.RigVMController.add_trait"></a>

#### add_trait

```python
def add_trait(node_name: Name,
              trait_type_object_path: Name,
              trait_name: Name = "None",
              default_value: str = "",
              pin_index: int = -1,
              setup_undo_redo: bool = True,
              print_python_command: bool = False) -> Name
```

x.add_trait(node_name, trait_type_object_path, trait_name="None", default_value="", pin_index=-1, setup_undo_redo=True, print_python_command=False) -> Name
Adds a trait to a node

Args:
    node_name (Name): 
    trait_type_object_path (Name): 
    trait_name (Name): 
    default_value (str): 
    pin_index (int32): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    Name:

<a id="unreal.RigVMController.add_template_node"></a>

#### add_template_node

```python
def add_template_node(notation: Name,
                      position: Vector2D = [0.000000, 0.000000],
                      node_name: str = "",
                      setup_undo_redo: bool = True,
                      print_python_command: bool = False) -> RigVMTemplateNode
```

x.add_template_node(notation, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMTemplateNode
Adds a template node to the graph.

Args:
    notation (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMTemplateNode:

<a id="unreal.RigVMController.add_tag_to_function_variant"></a>

#### add_tag_to_function_variant

```python
def add_tag_to_function_variant(function_name: Name,
                                tag: RigVMTag,
                                setup_undo_redo: bool = True,
                                print_python_command: bool = False) -> bool
```

x.add_tag_to_function_variant(function_name, tag, setup_undo_redo=True, print_python_command=False) -> bool
Adds a tag to a function variant

Args:
    function_name (Name): 
    tag (RigVMTag): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.add_select_node_from_struct"></a>

#### add_select_node_from_struct

```python
def add_select_node_from_struct(script_struct: ScriptStruct,
                                position: Vector2D = [0.000000, 0.000000],
                                node_name: str = "",
                                setup_undo_redo: bool = True) -> RigVMNode
```

x.add_select_node_from_struct(script_struct, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True) -> RigVMNode
Add Select Node from Struct

Args:
    script_struct (ScriptStruct): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_select_node"></a>

#### add_select_node

```python
def add_select_node(cpp_type: str,
                    cpp_type_object_path: Name,
                    position: Vector2D = [0.000000, 0.000000],
                    node_name: str = "",
                    setup_undo_redo: bool = True,
                    print_python_command: bool = False) -> RigVMNode
```

x.add_select_node(cpp_type, cpp_type_object_path, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMNode
Adds a select node to the graph.
Select nodes can be used to pick between multiple values based on an index.

Args:
    cpp_type (str): 
    cpp_type_object_path (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_reroute_node_on_pin"></a>

#### add_reroute_node_on_pin

```python
def add_reroute_node_on_pin(
        pin_path: str,
        as_input: bool,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMRerouteNode
```

x.add_reroute_node_on_pin(pin_path, as_input, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMRerouteNode
Adds a Reroute Node on an existing Pin to the editor Graph.
Reroute Nodes can be used to visually improve the data flow,
they don't require any additional memory though and are purely
cosmetic. This causes a NodeAdded modified event.

Args:
    pin_path (str): 
    as_input (bool): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMRerouteNode:

<a id="unreal.RigVMController.add_reroute_node_on_link_path"></a>

#### add_reroute_node_on_link_path

```python
def add_reroute_node_on_link_path(
        link_pin_path_representation: str,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMRerouteNode
```

x.add_reroute_node_on_link_path(link_pin_path_representation, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMRerouteNode
Adds a Reroute Node on an existing Link to the edited Graph given the Link's string representation.
Reroute Nodes can be used to visually improve the data flow,
they don't require any additional memory though and are purely
cosmetic. This causes a NodeAdded modified event.

Args:
    link_pin_path_representation (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMRerouteNode:

<a id="unreal.RigVMController.add_reroute_node_on_link"></a>

#### add_reroute_node_on_link

```python
def add_reroute_node_on_link(
        link: RigVMLink,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMRerouteNode
```

x.add_reroute_node_on_link(link, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMRerouteNode
Adds a Reroute Node on an existing Link to the edited Graph.
Reroute Nodes can be used to visually improve the data flow,
they don't require any additional memory though and are purely
cosmetic. This causes a NodeAdded modified event.

Args:
    link (RigVMLink): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMRerouteNode:

<a id="unreal.RigVMController.add_parameter_node_from_object_path"></a>

#### add_parameter_node_from_object_path

```python
def add_parameter_node_from_object_path(
        parameter_name: Name,
        cpp_type: str,
        cpp_type_object_path: str,
        is_input: bool,
        default_value: str,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMParameterNode
```

x.add_parameter_node_from_object_path(parameter_name, cpp_type, cpp_type_object_path, is_input, default_value, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMParameterNode
Adds a Parameter Node to the edited Graph given a struct object path name.
Parameters represent input or output arguments to the Graph / Function.
Input Parameters are constant values / literals.
This causes a NodeAdded modified event.
deprecated: Function 'AddParameterNodeFromObjectPath' is deprecated.

Args:
    parameter_name (Name): 
    cpp_type (str): 
    cpp_type_object_path (str): 
    is_input (bool): 
    default_value (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMParameterNode:

<a id="unreal.RigVMController.add_parameter_node"></a>

#### add_parameter_node

```python
def add_parameter_node(
        parameter_name: Name,
        cpp_type: str,
        cpp_type_object: Object,
        is_input: bool,
        default_value: str,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMParameterNode
```

x.add_parameter_node(parameter_name, cpp_type, cpp_type_object, is_input, default_value, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMParameterNode
Adds a Parameter Node to the edited Graph.
Parameters represent input or output arguments to the Graph / Function.
Input Parameters are constant values / literals.
This causes a NodeAdded modified event.
deprecated: Function 'AddParameterNode' is deprecated.

Args:
    parameter_name (Name): 
    cpp_type (str): 
    cpp_type_object (Object): 
    is_input (bool): 
    default_value (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMParameterNode:

<a id="unreal.RigVMController.add_local_variable_from_object_path"></a>

#### add_local_variable_from_object_path

```python
def add_local_variable_from_object_path(
        variable_name: Name,
        cpp_type: str,
        cpp_type_object_path: str,
        default_value: str,
        setup_undo_redo: bool = True) -> RigVMGraphVariableDescription
```

x.add_local_variable_from_object_path(variable_name, cpp_type, cpp_type_object_path, default_value, setup_undo_redo=True) -> RigVMGraphVariableDescription
Add a local variable to the graph given a struct object path name.

Args:
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object_path (str): 
    default_value (str): 
    setup_undo_redo (bool): 

Returns:
    RigVMGraphVariableDescription:

<a id="unreal.RigVMController.add_local_variable"></a>

#### add_local_variable

```python
def add_local_variable(
        variable_name: Name,
        cpp_type: str,
        cpp_type_object: Object,
        default_value: str,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMGraphVariableDescription
```

x.add_local_variable(variable_name, cpp_type, cpp_type_object, default_value, setup_undo_redo=True, print_python_command=False) -> RigVMGraphVariableDescription
Add a local variable to the graph

Args:
    variable_name (Name): 
    cpp_type (str): 
    cpp_type_object (Object): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMGraphVariableDescription:

<a id="unreal.RigVMController.add_link"></a>

#### add_link

```python
def add_link(output_pin_path: str,
             input_pin_path: str,
             setup_undo_redo: bool = True,
             print_python_command: bool = False,
             user_direction: RigVMPinDirection = RigVMPinDirection.OUTPUT,
             create_cast_node: bool = False) -> bool
```

x.add_link(output_pin_path, input_pin_path, setup_undo_redo=True, print_python_command=False, user_direction=RigVMPinDirection.OUTPUT, create_cast_node=False) -> bool
Adds a link to the graph.
This causes a LinkAdded modified event.

Args:
    output_pin_path (str): 
    input_pin_path (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 
    user_direction (RigVMPinDirection): 
    create_cast_node (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.add_invoke_entry_node"></a>

#### add_invoke_entry_node

```python
def add_invoke_entry_node(
        entry_name: Name,
        position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMInvokeEntryNode
```

x.add_invoke_entry_node(entry_name, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMInvokeEntryNode
Adds an entry invocation node
This causes a NodeAdded modified event.

Args:
    entry_name (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMInvokeEntryNode:

<a id="unreal.RigVMController.add_injected_node_from_struct_path"></a>

#### add_injected_node_from_struct_path

```python
def add_injected_node_from_struct_path(
        pin_path: str,
        as_input: bool,
        script_struct_path: str,
        method_name: Name,
        input_pin_name: Name,
        output_pin_name: Name,
        node_name: str = "",
        setup_undo_redo: bool = True) -> RigVMInjectionInfo
```

x.add_injected_node_from_struct_path(pin_path, as_input, script_struct_path, method_name, input_pin_name, output_pin_name, node_name="", setup_undo_redo=True) -> RigVMInjectionInfo
Adds a Function / Struct Node to the edited Graph as an injected node
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

Args:
    pin_path (str): 
    as_input (bool): 
    script_struct_path (str): 
    method_name (Name): 
    input_pin_name (Name): 
    output_pin_name (Name): 
    node_name (str): 
    setup_undo_redo (bool): 

Returns:
    RigVMInjectionInfo:

<a id="unreal.RigVMController.add_injected_node"></a>

#### add_injected_node

```python
def add_injected_node(
        pin_path: str,
        as_input: bool,
        script_struct: ScriptStruct,
        method_name: Name,
        input_pin_name: Name,
        output_pin_name: Name,
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMInjectionInfo
```

x.add_injected_node(pin_path, as_input, script_struct, method_name, input_pin_name, output_pin_name, node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMInjectionInfo
Adds a Function / Struct Node to the edited Graph as an injected node
UnitNode represent a RIGVM_METHOD declaration on a USTRUCT.
This causes a NodeAdded modified event.

Args:
    pin_path (str): 
    as_input (bool): 
    script_struct (ScriptStruct): 
    method_name (Name): 
    input_pin_name (Name): 
    output_pin_name (Name): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMInjectionInfo:

<a id="unreal.RigVMController.add_if_node_from_struct"></a>

#### add_if_node_from_struct

```python
def add_if_node_from_struct(script_struct: ScriptStruct,
                            position: Vector2D = [0.000000, 0.000000],
                            node_name: str = "",
                            setup_undo_redo: bool = True) -> RigVMNode
```

x.add_if_node_from_struct(script_struct, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True) -> RigVMNode
Add if Node from Struct

Args:
    script_struct (ScriptStruct): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_if_node"></a>

#### add_if_node

```python
def add_if_node(cpp_type: str,
                cpp_type_object_path: Name,
                position: Vector2D = [0.000000, 0.000000],
                node_name: str = "",
                setup_undo_redo: bool = True,
                print_python_command: bool = False) -> RigVMNode
```

x.add_if_node(cpp_type, cpp_type_object_path, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMNode
Adds an if node to the graph.
If nodes can be used to pick between two values based on a condition.

Args:
    cpp_type (str): 
    cpp_type_object_path (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_function_to_library"></a>

#### add_function_to_library

```python
def add_function_to_library(
        function_name: Name,
        mutable: bool,
        node_position: Vector2D = [0.000000, 0.000000],
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMLibraryNode
```

x.add_function_to_library(function_name, mutable, node_position=[0.000000, 0.000000], setup_undo_redo=True, print_python_command=False) -> RigVMLibraryNode
Adds a function definition to a function library graph

Args:
    function_name (Name): 
    mutable (bool): 
    node_position (Vector2D): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMController.add_function_reference_node_from_description"></a>

#### add_function_reference_node_from_description

```python
def add_function_reference_node_from_description(
        function_definition: RigVMGraphFunctionHeader,
        node_position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMFunctionReferenceNode
```

x.add_function_reference_node_from_description(function_definition, node_position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMFunctionReferenceNode
Adds a function reference / invocation to the graph

Args:
    function_definition (RigVMGraphFunctionHeader): 
    node_position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMFunctionReferenceNode:

<a id="unreal.RigVMController.add_function_reference_node"></a>

#### add_function_reference_node

```python
def add_function_reference_node(
        function_definition: RigVMLibraryNode,
        node_position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMFunctionReferenceNode
```

x.add_function_reference_node(function_definition, node_position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMFunctionReferenceNode
Add Function Reference Node

Args:
    function_definition (RigVMLibraryNode): 
    node_position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMFunctionReferenceNode:

<a id="unreal.RigVMController.add_free_reroute_node"></a>

#### add_free_reroute_node

```python
def add_free_reroute_node(cpp_type: str,
                          cpp_type_object_path: Name,
                          is_constant: bool,
                          custom_widget_name: Name,
                          default_value: str,
                          position: Vector2D = [0.000000, 0.000000],
                          node_name: str = "",
                          setup_undo_redo: bool = True) -> RigVMRerouteNode
```

x.add_free_reroute_node(cpp_type, cpp_type_object_path, is_constant, custom_widget_name, default_value, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True) -> RigVMRerouteNode
Adds a free Reroute Node

Args:
    cpp_type (str): 
    cpp_type_object_path (Name): 
    is_constant (bool): 
    custom_widget_name (Name): 
    default_value (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 

Returns:
    RigVMRerouteNode:

<a id="unreal.RigVMController.add_external_function_reference_node"></a>

#### add_external_function_reference_node

```python
def add_external_function_reference_node(
        host_path: str,
        function_name: Name,
        node_position: Vector2D = [0.000000, 0.000000],
        node_name: str = "",
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> RigVMFunctionReferenceNode
```

x.add_external_function_reference_node(host_path, function_name, node_position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMFunctionReferenceNode
Add External Function Reference Node

Args:
    host_path (str): 
    function_name (Name): 
    node_position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMFunctionReferenceNode:

<a id="unreal.RigVMController.add_exposed_pin"></a>

#### add_exposed_pin

```python
def add_exposed_pin(pin_name: Name,
                    direction: RigVMPinDirection,
                    cpp_type: str,
                    cpp_type_object_path: Name,
                    default_value: str,
                    setup_undo_redo: bool = True,
                    print_python_command: bool = False) -> Name
```

x.add_exposed_pin(pin_name, direction, cpp_type, cpp_type_object_path, default_value, setup_undo_redo=True, print_python_command=False) -> Name
Adds an exposed pin to the graph controlled by this

Args:
    pin_name (Name): 
    direction (RigVMPinDirection): 
    cpp_type (str): 
    cpp_type_object_path (Name): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    Name:

<a id="unreal.RigVMController.add_enum_node"></a>

#### add_enum_node

```python
def add_enum_node(cpp_type_object_path: Name,
                  position: Vector2D = [0.000000, 0.000000],
                  node_name: str = "",
                  setup_undo_redo: bool = True,
                  print_python_command: bool = False) -> RigVMEnumNode
```

x.add_enum_node(cpp_type_object_path, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMEnumNode
Adds an enum node to the graph
Enum nodes can be used to represent constant enum values within the graph

Args:
    cpp_type_object_path (Name): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMEnumNode:

<a id="unreal.RigVMController.add_empty_pin_category"></a>

#### add_empty_pin_category

```python
def add_empty_pin_category(node_name: Name,
                           category: str,
                           setup_undo_redo: bool = True,
                           print_python_command: bool = False) -> bool
```

x.add_empty_pin_category(node_name, category, setup_undo_redo=True, print_python_command=False) -> bool
Adds a new pin category. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Args:
    node_name (Name): 
    category (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.add_default_tag_to_function_variant"></a>

#### add_default_tag_to_function_variant

```python
def add_default_tag_to_function_variant(
        function_name: Name,
        tag_name: Name,
        setup_undo_redo: bool = True,
        print_python_command: bool = False) -> bool
```

x.add_default_tag_to_function_variant(function_name, tag_name, setup_undo_redo=True, print_python_command=False) -> bool
Adds a default tag to a function variant

Args:
    function_name (Name): 
    tag_name (Name): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    bool:

<a id="unreal.RigVMController.add_comment_node"></a>

#### add_comment_node

```python
def add_comment_node(comment_text: str,
                     position: Vector2D = [0.000000, 0.000000],
                     size: Vector2D = [400.000000, 300.000000],
                     color: LinearColor = [
                         0.000000, 0.000000, 0.000000, 1.000000
                     ],
                     node_name: str = "",
                     setup_undo_redo: bool = True,
                     print_python_command: bool = False) -> RigVMCommentNode
```

x.add_comment_node(comment_text, position=[0.000000, 0.000000], size=[400.000000, 300.000000], color=[0.000000, 0.000000, 0.000000, 1.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMCommentNode
Adds a Comment Node to the edited Graph.
Comments can be used to annotate the Graph.
This causes a NodeAdded modified event.

Args:
    comment_text (str): 
    position (Vector2D): 
    size (Vector2D): 
    color (LinearColor): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMCommentNode:

<a id="unreal.RigVMController.add_branch_node"></a>

#### add_branch_node

```python
def add_branch_node(position: Vector2D = [0.000000, 0.000000],
                    node_name: str = "",
                    setup_undo_redo: bool = True,
                    print_python_command: bool = False) -> RigVMNode
```

x.add_branch_node(position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False) -> RigVMNode
Adds a branch node to the graph.
Branch nodes can be used to split the execution of into multiple branches,
allowing to drive behavior by logic.

Args:
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_array_pin"></a>

#### add_array_pin

```python
def add_array_pin(array_pin_path: str,
                  default_value: str = "",
                  setup_undo_redo: bool = True,
                  print_python_command: bool = False) -> str
```

x.add_array_pin(array_pin_path, default_value="", setup_undo_redo=True, print_python_command=False) -> str
Adds an array element pin to the end of an array pin.
This causes a PinArraySizeChanged modified event.

Args:
    array_pin_path (str): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    str:

<a id="unreal.RigVMController.add_array_node_from_object_path"></a>

#### add_array_node_from_object_path

```python
def add_array_node_from_object_path(op_code: RigVMOpCode,
                                    cpp_type: str,
                                    cpp_type_object_path: str,
                                    position: Vector2D = [0.000000, 0.000000],
                                    node_name: str = "",
                                    setup_undo_redo: bool = True,
                                    print_python_command: bool = False,
                                    is_patching: bool = False) -> RigVMNode
```

x.add_array_node_from_object_path(op_code, cpp_type, cpp_type_object_path, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False, is_patching=False) -> RigVMNode
Adds a Array Node to the edited Graph given a struct object path name.
This causes a NodeAdded modified event.

Args:
    op_code (RigVMOpCode): 
    cpp_type (str): 
    cpp_type_object_path (str): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 
    is_patching (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_array_node"></a>

#### add_array_node

```python
def add_array_node(op_code: RigVMOpCode,
                   cpp_type: str,
                   cpp_type_object: Object,
                   position: Vector2D = [0.000000, 0.000000],
                   node_name: str = "",
                   setup_undo_redo: bool = True,
                   print_python_command: bool = False,
                   is_patching: bool = False) -> RigVMNode
```

x.add_array_node(op_code, cpp_type, cpp_type_object, position=[0.000000, 0.000000], node_name="", setup_undo_redo=True, print_python_command=False, is_patching=False) -> RigVMNode
Adds a Array Node to the edited Graph.
This causes a NodeAdded modified event.

Args:
    op_code (RigVMOpCode): 
    cpp_type (str): 
    cpp_type_object (Object): 
    position (Vector2D): 
    node_name (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 
    is_patching (bool): 

Returns:
    RigVMNode:

<a id="unreal.RigVMController.add_aggregate_pin"></a>

#### add_aggregate_pin

```python
def add_aggregate_pin(node_name: str,
                      pin_name: str,
                      default_value: str = "",
                      setup_undo_redo: bool = True,
                      print_python_command: bool = False) -> str
```

x.add_aggregate_pin(node_name, pin_name, default_value="", setup_undo_redo=True, print_python_command=False) -> str
Add Aggregate Pin

Args:
    node_name (str): 
    pin_name (str): 
    default_value (str): 
    setup_undo_redo (bool): 
    print_python_command (bool): 

Returns:
    str:

<a id="unreal.RigVMGraph"></a>