## RigVMPin Objects

```python
class RigVMPin(Object)
```

The Pin represents a single connector / pin on a node in the RigVM model.
Pins can be connected based on rules. Pins also provide access to a 'PinPath',
which essentially represents . separated list of names to reach the pin within
the owning graph. PinPaths are unique.
In comparison to the EdGraph Pin the URigVMPin supports the concept of 'SubPins',
so child / parent relationships between pins. A FVector Pin for example might
have its X, Y and Z components as SubPins. Array Pins will have its elements as
SubPins, and so on.
A URigVMPin is owned solely by a URigVMNode.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMPin.h

<a id="unreal.RigVMPin.should_only_show_sub_pins"></a>

#### should_only_show_sub_pins

```python
def should_only_show_sub_pins() -> bool
```

x.should_only_show_sub_pins() -> bool
Returns true if this pin is an array that should be displayed as elements only

Returns:
    bool:

<a id="unreal.RigVMPin.should_hide_sub_pins"></a>

#### should_hide_sub_pins

```python
def should_hide_sub_pins() -> bool
```

x.should_hide_sub_pins() -> bool
Returns true if this pin's subpins should be hidden in the UI

Returns:
    bool:

<a id="unreal.RigVMPin.requires_watch"></a>

#### requires_watch

```python
def requires_watch(check_exposed_pin_chain: bool = False) -> bool
```

x.requires_watch(check_exposed_pin_chain=False) -> bool
Returns true if the pin should be watched

Args:
    check_exposed_pin_chain (bool): 

Returns:
    bool:

<a id="unreal.RigVMPin.is_wild_card"></a>

#### is_wild_card

```python
def is_wild_card() -> bool
```

x.is_wild_card() -> bool
Returns true if the C++ data type is unknown

Returns:
    bool:

<a id="unreal.RigVMPin.is_valid_default_value"></a>

#### is_valid_default_value

```python
def is_valid_default_value(default_value: str) -> bool
```

x.is_valid_default_value(default_value) -> bool
Returns true if the default value provided is valid

Args:
    default_value (str): 

Returns:
    bool:

<a id="unreal.RigVMPin.is_u_object"></a>

#### is_u_object

```python
def is_u_object() -> bool
```

x.is_u_object() -> bool
Returns true if the data type of the Pin is a uobject

Returns:
    bool:

<a id="unreal.RigVMPin.is_trait_pin"></a>

#### is_trait_pin

```python
def is_trait_pin() -> bool
```

x.is_trait_pin() -> bool
Returns true if this pin represents a trait

Returns:
    bool:

<a id="unreal.RigVMPin.is_struct_member"></a>

#### is_struct_member

```python
def is_struct_member() -> bool
```

x.is_struct_member() -> bool
Returns true if the Pin is a SubPin within a struct

Returns:
    bool:

<a id="unreal.RigVMPin.is_struct"></a>

#### is_struct

```python
def is_struct() -> bool
```

x.is_struct() -> bool
Returns true if the data type of the Pin is a struct

Returns:
    bool:

<a id="unreal.RigVMPin.is_string_type"></a>

#### is_string_type

```python
def is_string_type() -> bool
```

x.is_string_type() -> bool
Returns true if the C++ data type is FString or FName

Returns:
    bool:

<a id="unreal.RigVMPin.is_root_pin"></a>

#### is_root_pin

```python
def is_root_pin() -> bool
```

x.is_root_pin() -> bool
Returns true if this pin is a root pin

Returns:
    bool:

<a id="unreal.RigVMPin.is_reference_counted_container"></a>

#### is_reference_counted_container

```python
def is_reference_counted_container() -> bool
```

x.is_reference_counted_container() -> bool
Returns true if this data type is referenced counted

Returns:
    bool:

<a id="unreal.RigVMPin.is_linked_to"></a>

#### is_linked_to

```python
def is_linked_to(pin: RigVMPin) -> bool
```

x.is_linked_to(pin) -> bool
Returns true if this Pin is linked to another Pin

Args:
    pin (RigVMPin): 

Returns:
    bool:

<a id="unreal.RigVMPin.is_lazy"></a>

#### is_lazy

```python
def is_lazy() -> bool
```

x.is_lazy() -> bool
Returns true if this pin's value may be executed lazily

Returns:
    bool:

<a id="unreal.RigVMPin.is_interface"></a>

#### is_interface

```python
def is_interface() -> bool
```

x.is_interface() -> bool
Returns true if the data type of the Pin is a interface

Returns:
    bool:

<a id="unreal.RigVMPin.is_fixed_size_array"></a>

#### is_fixed_size_array

```python
def is_fixed_size_array() -> bool
```

x.is_fixed_size_array() -> bool
Returns true if this pin is an array that should be displayed as elements only

Returns:
    bool:

<a id="unreal.RigVMPin.is_expanded"></a>

#### is_expanded

```python
def is_expanded() -> bool
```

x.is_expanded() -> bool
Returns true if the pin is currently expanded

Returns:
    bool:

<a id="unreal.RigVMPin.is_execute_context"></a>

#### is_execute_context

```python
def is_execute_context() -> bool
```

x.is_execute_context() -> bool
Returns true if the C++ data type is an execute context

Returns:
    bool:

<a id="unreal.RigVMPin.is_enum"></a>

#### is_enum

```python
def is_enum() -> bool
```

x.is_enum() -> bool
Returns true if the data type of the Pin is a enum

Returns:
    bool:

<a id="unreal.RigVMPin.is_dynamic_array"></a>

#### is_dynamic_array

```python
def is_dynamic_array() -> bool
```

x.is_dynamic_array() -> bool
Returns true if this pin represents a dynamic array

Returns:
    bool:

<a id="unreal.RigVMPin.is_defined_as_constant"></a>

#### is_defined_as_constant

```python
def is_defined_as_constant() -> bool
```

x.is_defined_as_constant() -> bool
Returns true if the pin is defined as a constant value / literal

Returns:
    bool:

<a id="unreal.RigVMPin.is_array_element"></a>

#### is_array_element

```python
def is_array_element() -> bool
```

x.is_array_element() -> bool
Returns true if the Pin is a SubPin within an array

Returns:
    bool:

<a id="unreal.RigVMPin.is_array"></a>

#### is_array

```python
def is_array() -> bool
```

x.is_array() -> bool
Returns true if the data type of the Pin is an array

Returns:
    bool:

<a id="unreal.RigVMPin.has_user_provided_default_value"></a>

#### has_user_provided_default_value

```python
def has_user_provided_default_value() -> bool
```

x.has_user_provided_default_value() -> bool
Returns true if the default value was ever changed by the user

Returns:
    bool:

<a id="unreal.RigVMPin.get_tool_tip_text"></a>

#### get_tool_tip_text

```python
def get_tool_tip_text() -> Text
```

x.get_tool_tip_text() -> Text
Returns the tooltip of this pin

Returns:
    Text:

<a id="unreal.RigVMPin.get_target_links"></a>

#### get_target_links

```python
def get_target_links(recursive: bool = False) -> Array[RigVMLink]
```

x.get_target_links(recursive=False) -> Array[RigVMLink]
Returns all of the target links,
using this Pin as the source.

Args:
    recursive (bool): 

Returns:
    Array[RigVMLink]:

<a id="unreal.RigVMPin.get_sub_pins"></a>

#### get_sub_pins

```python
def get_sub_pins() -> Array[RigVMPin]
```

x.get_sub_pins() -> Array[RigVMPin]
Returns all of the SubPins of this one.

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMPin.get_sub_pin_path"></a>

#### get_sub_pin_path

```python
def get_sub_pin_path(parent_pin: RigVMPin,
                     include_parent_pin_name: bool = False) -> str
```

x.get_sub_pin_path(parent_pin, include_parent_pin_name=False) -> str
Returns a . separated path containing all names of the pin and its owners
until we hit the provided parent pin.

Args:
    parent_pin (RigVMPin): 
    include_parent_pin_name (bool): 

Returns:
    str:

<a id="unreal.RigVMPin.get_source_links"></a>

#### get_source_links

```python
def get_source_links(recursive: bool = False) -> Array[RigVMLink]
```

x.get_source_links(recursive=False) -> Array[RigVMLink]
Returns all of the source pins
using this Pin as the target.

Args:
    recursive (bool): 

Returns:
    Array[RigVMLink]:

<a id="unreal.RigVMPin.get_segment_path"></a>

#### get_segment_path

```python
def get_segment_path(include_root_pin: bool = False) -> str
```

x.get_segment_path(include_root_pin=False) -> str
Returns a . separated path containing all names of the pin within its main
memory owner / storage. This is typically used to create an offset pointer
within memory (FRigVMRegisterOffset).
So for example for a PinPath such as "Node.Transform.Translation.X" the
corresponding SegmentPath is "Translation.X", since the transform is the
storage / memory.

Args:
    include_root_pin (bool): 

Returns:
    str:

<a id="unreal.RigVMPin.get_script_struct"></a>

#### get_script_struct

```python
def get_script_struct() -> ScriptStruct
```

x.get_script_struct() -> ScriptStruct
Returns the struct of the data type of the Pin,
or nullptr otherwise.

Returns:
    ScriptStruct:

<a id="unreal.RigVMPin.get_root_pin"></a>

#### get_root_pin

```python
def get_root_pin() -> RigVMPin
```

x.get_root_pin() -> RigVMPin
Returns the top-most parent Pin, so for example
for "Node.Transform.Translation.X" this returns
the Pin for "Node.Transform".

Returns:
    RigVMPin:

<a id="unreal.RigVMPin.get_pin_path"></a>

#### get_pin_path

```python
def get_pin_path(use_node_path: bool = False) -> str
```

x.get_pin_path(use_node_path=False) -> str
Returns a . separated path containing all names of the pin and its owners,
this includes the node name, for example "Node.Color.R"

Args:
    use_node_path (bool): 

Returns:
    str:

<a id="unreal.RigVMPin.get_pin_index"></a>

#### get_pin_index

```python
def get_pin_index() -> int
```

x.get_pin_index() -> int32
Returns the index of the Pin within the node / parent Pin

Returns:
    int32:

<a id="unreal.RigVMPin.get_pin_for_link"></a>

#### get_pin_for_link

```python
def get_pin_for_link() -> RigVMPin
```

x.get_pin_for_link() -> RigVMPin
Returns the pin to be used for a link.
This might differ from this actual pin, since
the pin might contain injected nodes.

Returns:
    RigVMPin:

<a id="unreal.RigVMPin.get_parent_pin"></a>

#### get_parent_pin

```python
def get_parent_pin() -> RigVMPin
```

x.get_parent_pin() -> RigVMPin
Returns the parent Pin - or nullptr if the Pin
is nested directly below a node.

Returns:
    RigVMPin:

<a id="unreal.RigVMPin.get_original_pin_from_injected_node"></a>

#### get_original_pin_from_injected_node

```python
def get_original_pin_from_injected_node() -> RigVMPin
```

x.get_original_pin_from_injected_node() -> RigVMPin
Returns the original pin for a pin on an injected
node. This can be used to determine where a link
should go in the user interface

Returns:
    RigVMPin:

<a id="unreal.RigVMPin.get_original_default_value"></a>

#### get_original_default_value

```python
def get_original_default_value() -> str
```

x.get_original_default_value() -> str
Get Original Default Value

Returns:
    str:

<a id="unreal.RigVMPin.get_node"></a>

#### get_node

```python
def get_node() -> RigVMNode
```

x.get_node() -> RigVMNode
Returns the node of this Pin.

Returns:
    RigVMNode:

<a id="unreal.RigVMPin.get_meta_data"></a>

#### get_meta_data

```python
def get_meta_data(key: Name) -> str
```

x.get_meta_data(key) -> str
Returns the keyed metadata associated with this pin, if any

Args:
    key (Name): 

Returns:
    str:

<a id="unreal.RigVMPin.get_links"></a>

#### get_links

```python
def get_links() -> Array[RigVMLink]
```

x.get_links() -> Array[RigVMLink]
Returns all of the links linked to this Pin.

Returns:
    Array[RigVMLink]:

<a id="unreal.RigVMPin.get_linked_target_pins"></a>

#### get_linked_target_pins

```python
def get_linked_target_pins(recursive: bool = False) -> Array[RigVMPin]
```

x.get_linked_target_pins(recursive=False) -> Array[RigVMPin]
Returns all of the linked target Pins,
using this Pin as the source.

Args:
    recursive (bool): 

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMPin.get_linked_source_pins"></a>

#### get_linked_source_pins

```python
def get_linked_source_pins(recursive: bool = False) -> Array[RigVMPin]
```

x.get_linked_source_pins(recursive=False) -> Array[RigVMPin]
Returns all of the linked source Pins,
using this Pin as the target.

Args:
    recursive (bool): 

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMPin.get_index_in_category"></a>

#### get_index_in_category

```python
def get_index_in_category() -> int
```

x.get_index_in_category() -> int32
Returns index within a category on a pin. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Returns:
    int32:

<a id="unreal.RigVMPin.get_graph"></a>

#### get_graph

```python
def get_graph() -> RigVMGraph
```

x.get_graph() -> RigVMGraph
Returns the graph of this Pin.

Returns:
    RigVMGraph:

<a id="unreal.RigVMPin.get_enum"></a>

#### get_enum

```python
def get_enum() -> Enum
```

x.get_enum() -> Enum
Returns the enum of the data type of the Pin,
or nullptr otherwise.

Returns:
    Enum:

<a id="unreal.RigVMPin.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Name
```

x.get_display_name() -> Name
Returns the display label of the pin

Returns:
    Name:

<a id="unreal.RigVMPin.get_direction"></a>

#### get_direction

```python
def get_direction() -> RigVMPinDirection
```

x.get_direction() -> RigVMPinDirection
Returns the direction of the pin

Returns:
    RigVMPinDirection:

<a id="unreal.RigVMPin.get_default_value_type"></a>

#### get_default_value_type

```python
def get_default_value_type() -> RigVMPinDefaultValueType
```

x.get_default_value_type() -> RigVMPinDefaultValueType
Returns true if the pin can / may provide a default value

Returns:
    RigVMPinDefaultValueType:

<a id="unreal.RigVMPin.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> str
```

x.get_default_value() -> str
Returns the default value of the Pin as a string.
Note that this value is computed based on the Pin's
SubPins - so for example for a FVector typed Pin
the default value is actually composed out of the
default values of the X, Y and Z SubPins.

Returns:
    str:

<a id="unreal.RigVMPin.get_custom_widget_name"></a>

#### get_custom_widget_name

```python
def get_custom_widget_name() -> Name
```

x.get_custom_widget_name() -> Name
Returns the name of a custom widget to be used
for editing the Pin.

Returns:
    Name:

<a id="unreal.RigVMPin.get_cpp_type_object"></a>

#### get_cpp_type_object

```python
def get_cpp_type_object() -> Object
```

x.get_cpp_type_object() -> Object
Returns the struct of the data type of the Pin,
or nullptr otherwise.

Returns:
    Object:

<a id="unreal.RigVMPin.get_cpp_type"></a>

#### get_cpp_type

```python
def get_cpp_type() -> str
```

x.get_cpp_type() -> str
Returns the C++ data type of the pin

Returns:
    str:

<a id="unreal.RigVMPin.get_category"></a>

#### get_category

```python
def get_category() -> str
```

x.get_category() -> str
Returns the category on a pin. The category is UI relevant only and used
to order pins in the user interface of the node as well as on the details panel.

Returns:
    str:

<a id="unreal.RigVMPin.get_array_size"></a>

#### get_array_size

```python
def get_array_size() -> int
```

x.get_array_size() -> int32
Returns the number of elements within an array Pin

Returns:
    int32:

<a id="unreal.RigVMPin.get_array_element_cpp_type"></a>

#### get_array_element_cpp_type

```python
def get_array_element_cpp_type() -> str
```

x.get_array_element_cpp_type() -> str
Returns the C++ data type of an element of the Pin array

Returns:
    str:

<a id="unreal.RigVMPin.get_all_sub_pins_recursively"></a>

#### get_all_sub_pins_recursively

```python
def get_all_sub_pins_recursively() -> Array[RigVMPin]
```

x.get_all_sub_pins_recursively() -> Array[RigVMPin]
Returns all of the SubPins of this one including sub-sub-pins

Returns:
    Array[RigVMPin]:

<a id="unreal.RigVMPin.get_absolute_pin_index"></a>

#### get_absolute_pin_index

```python
def get_absolute_pin_index() -> int
```

x.get_absolute_pin_index() -> int32
Returns the absolute index of the Pin within the node / parent Pin

Returns:
    int32:

<a id="unreal.RigVMPin.find_sub_pin"></a>

#### find_sub_pin

```python
def find_sub_pin(pin_path: str) -> RigVMPin
```

x.find_sub_pin(pin_path) -> RigVMPin
Returns a SubPin given a name / path or nullptr.

Args:
    pin_path (str): 

Returns:
    RigVMPin:

<a id="unreal.RigVMPin.find_link_for_pin"></a>

#### find_link_for_pin

```python
def find_link_for_pin(other_pin: RigVMPin) -> RigVMLink
```

x.find_link_for_pin(other_pin) -> RigVMLink
Returns the link that represents the connection
between this pin and InOtherPin. nullptr is returned
if the pins are not connected.

Args:
    other_pin (RigVMPin): 

Returns:
    RigVMLink:

<a id="unreal.RigVMPin.contains_wild_card_sub_pin"></a>

#### contains_wild_card_sub_pin

```python
def contains_wild_card_sub_pin() -> bool
```

x.contains_wild_card_sub_pin() -> bool
Returns true if any of the subpins is a wildcard

Returns:
    bool:

<a id="unreal.RigVMPin.can_provide_default_value"></a>

#### can_provide_default_value

```python
def can_provide_default_value() -> bool
```

x.can_provide_default_value() -> bool
Returns true if the pin can / may provide a default value

Returns:
    bool:

<a id="unreal.RigVMUserWorkflowRegistry"></a>