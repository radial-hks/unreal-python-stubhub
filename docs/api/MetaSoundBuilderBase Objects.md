## MetaSoundBuilderBase Objects

```python
class MetaSoundBuilderBase(Object)
```

Base implementation of MetaSound builder

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundBuilderBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_name`` (MetasoundFrontendClassName):  [Read-Write]
  deprecated: 5.5 - No longer used. ClassName should be queried from associated FrontendBuilder's MetaSound
- ``is_attached`` (bool):  [Read-Write]
  deprecated: 5.4 - All source builders now operate on an underlying document source document that is also used to audition.

<a id="unreal.MetaSoundBuilderBase.class_name"></a>

#### class_name

```python
@property
def class_name() -> MetasoundFrontendClassName
```

(MetasoundFrontendClassName):  [Read-Write]
deprecated: 5.5 - No longer used. ClassName should be queried from associated FrontendBuilder's MetaSound

<a id="unreal.MetaSoundBuilderBase.class_name"></a>

#### class_name

```python
@class_name.setter
def class_name(value: MetasoundFrontendClassName) -> None
```

<a id="unreal.MetaSoundBuilderBase.is_attached"></a>

#### is_attached

```python
@property
def is_attached() -> bool
```

(bool):  [Read-Write]
deprecated: 5.4 - All source builders now operate on an underlying document source document that is also used to audition.

<a id="unreal.MetaSoundBuilderBase.is_attached"></a>

#### is_attached

```python
@is_attached.setter
def is_attached(value: bool) -> None
```

<a id="unreal.MetaSoundBuilderBase.set_node_input_default"></a>

#### set_node_input_default

```python
def set_node_input_default(
        node_input_handle: MetaSoundBuilderNodeInputHandle,
        literal: MetasoundFrontendLiteral) -> MetaSoundBuilderResult
```

x.set_node_input_default(node_input_handle, literal) -> MetaSoundBuilderResult
Sets the node's input default value (used if no connection to the given node input is present)

Args:
    node_input_handle (MetaSoundBuilderNodeInputHandle): 
    literal (MetasoundFrontendLiteral): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_output_name"></a>

#### set_graph_output_name

```python
def set_graph_output_name(output_name: Name,
                          new_name: Name) -> MetaSoundBuilderResult
```

x.set_graph_output_name(output_name, new_name) -> MetaSoundBuilderResult
Sets the given graph output's name to the new name.
Result succeeds if the name was successfully changed or the new name is the same as the old name, and fails if the given output name doesn't exist.

Args:
    output_name (Name): 
    new_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_output_data_type"></a>

#### set_graph_output_data_type

```python
def set_graph_output_data_type(output_name: Name,
                               data_type: Name) -> MetaSoundBuilderResult
```

x.set_graph_output_data_type(output_name, data_type) -> MetaSoundBuilderResult
Disconnects the given graph output's respective template nodes and sets the graph output's DataType should it not match the current DataType.
Result succeeds if the DataType was successfully changed or if the provided DataType is already the output's current DataType.

Args:
    output_name (Name): 
    data_type (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_output_access_type"></a>

#### set_graph_output_access_type

```python
def set_graph_output_access_type(
        output_name: Name, access_type: MetasoundFrontendVertexAccessType
) -> MetaSoundBuilderResult
```

x.set_graph_output_access_type(output_name, access_type) -> MetaSoundBuilderResult
Disconnects the given graph output's respective template nodes and sets the graph output's AccessType should it not match the current AccessType.
Result succeeds if the AccessType was successfully changed or if the provided AccessType is already the output's current AccessType.

Args:
    output_name (Name): 
    access_type (MetasoundFrontendVertexAccessType): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_input_name"></a>

#### set_graph_input_name

```python
def set_graph_input_name(input_name: Name,
                         new_name: Name) -> MetaSoundBuilderResult
```

x.set_graph_input_name(input_name, new_name) -> MetaSoundBuilderResult
Sets the given graph input's name to the new name.
Result succeeds if the name was successfully changed or the new name is the same as the old name, and fails if the given input name doesn't exist.

Args:
    input_name (Name): 
    new_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_input_default"></a>

#### set_graph_input_default

```python
def set_graph_input_default(
        input_name: Name,
        literal: MetasoundFrontendLiteral) -> MetaSoundBuilderResult
```

x.set_graph_input_default(input_name, literal) -> MetaSoundBuilderResult
Sets the input node's default value, overriding the default provided by the referenced graph if the graph is a preset.

Args:
    input_name (Name): 
    literal (MetasoundFrontendLiteral): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_input_data_type"></a>

#### set_graph_input_data_type

```python
def set_graph_input_data_type(input_name: Name,
                              data_type: Name) -> MetaSoundBuilderResult
```

x.set_graph_input_data_type(input_name, data_type) -> MetaSoundBuilderResult
Disconnects the given graph input's respective template nodes and sets the graph input's DataType should it not match the current DataType.
Result succeeds if the DataType was successfully changed or if the provided DataType is already the input's current DataType.

Args:
    input_name (Name): 
    data_type (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.set_graph_input_access_type"></a>

#### set_graph_input_access_type

```python
def set_graph_input_access_type(
        input_name: Name, access_type: MetasoundFrontendVertexAccessType
) -> MetaSoundBuilderResult
```

x.set_graph_input_access_type(input_name, access_type) -> MetaSoundBuilderResult
Disconnects the given graph input's respective template nodes and sets the graph input's AccessType should it not match the current AccessType.
Result succeeds if the AccessType was successfully changed or if the provided AccessType is already the input's current AccessType.

Args:
    input_name (Name): 
    access_type (MetasoundFrontendVertexAccessType): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.remove_unused_dependencies"></a>

#### remove_unused_dependencies

```python
def remove_unused_dependencies() -> None
```

x.remove_unused_dependencies() -> None
Removes dependencies in document that are no longer referenced by nodes

<a id="unreal.MetaSoundBuilderBase.remove_node_input_default"></a>

#### remove_node_input_default

```python
def remove_node_input_default(
        input_handle: MetaSoundBuilderNodeInputHandle
) -> MetaSoundBuilderResult
```

x.remove_node_input_default(input_handle) -> MetaSoundBuilderResult
Removes node input literal default if set, reverting the value to be whatever the node class defaults the value to.
Returns success if value was removed, false if not removed (i.e. wasn't set to begin with).

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.remove_node"></a>

#### remove_node

```python
def remove_node(
        node_handle: MetaSoundNodeHandle,
        remove_unused_dependencies: bool = True) -> MetaSoundBuilderResult
```

x.remove_node(node_handle, remove_unused_dependencies=True) -> MetaSoundBuilderResult
Removes node and any associated connections from the builder's MetaSound. (Advanced) Optionally, remove unused dependencies
from the internal dependendency list on successful removal of node.

Args:
    node_handle (MetaSoundNodeHandle): 
    remove_unused_dependencies (bool): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.remove_interface"></a>

#### remove_interface

```python
def remove_interface(interface_name: Name) -> MetaSoundBuilderResult
```

x.remove_interface(interface_name) -> MetaSoundBuilderResult
Removes the interface with the given name from the builder's MetaSound. Removes any graph inputs
and outputs associated with the given interface and their respective connections (if any).

Args:
    interface_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.remove_graph_output"></a>

#### remove_graph_output

```python
def remove_graph_output(name: Name) -> MetaSoundBuilderResult
```

x.remove_graph_output(name) -> MetaSoundBuilderResult
Removes graph output if it exists; sets result to succeeded if it was removed and failed if it was not.

Args:
    name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.remove_graph_input"></a>

#### remove_graph_input

```python
def remove_graph_input(name: Name) -> MetaSoundBuilderResult
```

x.remove_graph_input(name) -> MetaSoundBuilderResult
Removes graph input if it exists; sets result to succeeded if it was removed and failed if it was not.

Args:
    name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.nodes_are_connected"></a>

#### nodes_are_connected

```python
def nodes_are_connected(output_handle: MetaSoundBuilderNodeOutputHandle,
                        input_handle: MetaSoundBuilderNodeInputHandle) -> bool
```

x.nodes_are_connected(output_handle, input_handle) -> bool
Returns if a given node output and node input are connected.

Args:
    output_handle (MetaSoundBuilderNodeOutputHandle): 
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.node_output_is_connected"></a>

#### node_output_is_connected

```python
def node_output_is_connected(
        output_handle: MetaSoundBuilderNodeOutputHandle) -> bool
```

x.node_output_is_connected(output_handle) -> bool
Returns if a given node output is connected.

Args:
    output_handle (MetaSoundBuilderNodeOutputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.node_input_is_connected"></a>

#### node_input_is_connected

```python
def node_input_is_connected(
        input_handle: MetaSoundBuilderNodeInputHandle) -> bool
```

x.node_input_is_connected(input_handle) -> bool
Returns if a given node input has connections.

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.is_preset"></a>

#### is_preset

```python
def is_preset() -> bool
```

x.is_preset() -> bool
Returns whether this is a preset.

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.interface_is_declared"></a>

#### interface_is_declared

```python
def interface_is_declared(interface_name: Name) -> bool
```

x.interface_is_declared(interface_name) -> bool
Returns if a given interface is declared.

Args:
    interface_name (Name): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.get_root_graph_class_name"></a>

#### get_root_graph_class_name

```python
def get_root_graph_class_name() -> MetasoundFrontendClassName
```

x.get_root_graph_class_name() -> MetasoundFrontendClassName
Returns the MetaSound asset's graph class name (used by the MetaSound Node Class Registry)

Returns:
    MetasoundFrontendClassName:

<a id="unreal.MetaSoundBuilderBase.get_referenced_preset_asset"></a>

#### get_referenced_preset_asset

```python
def get_referenced_preset_asset() -> Object
```

x.get_referenced_preset_asset() -> Object
Return the asset referenced by this preset builder. Returns nullptr if the builder is not a preset.

Returns:
    Object:

<a id="unreal.MetaSoundBuilderBase.get_node_output_is_constructor_pin"></a>

#### get_node_output_is_constructor_pin

```python
def get_node_output_is_constructor_pin(
        output_handle: MetaSoundBuilderNodeOutputHandle) -> bool
```

x.get_node_output_is_constructor_pin(output_handle) -> bool
Returns whether the given node output is a constructor pin

Args:
    output_handle (MetaSoundBuilderNodeOutputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.get_node_output_data"></a>

#### get_node_output_data

```python
def get_node_output_data(
    output_handle: MetaSoundBuilderNodeOutputHandle
) -> Tuple[Name, Name, MetaSoundBuilderResult]
```

x.get_node_output_data(output_handle) -> (name=Name, data_type=Name, out_result=MetaSoundBuilderResult)
Returns node output's data if valid (including things like name and datatype).

Args:
    output_handle (MetaSoundBuilderNodeOutputHandle): 

Returns:
    tuple: 

    name (Name): 

    data_type (Name): 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.get_node_input_is_constructor_pin"></a>

#### get_node_input_is_constructor_pin

```python
def get_node_input_is_constructor_pin(
        input_handle: MetaSoundBuilderNodeInputHandle) -> bool
```

x.get_node_input_is_constructor_pin(input_handle) -> bool
Returns whether the given node input is a constructor pin

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.get_node_input_default"></a>

#### get_node_input_default

```python
def get_node_input_default(
    input_handle: MetaSoundBuilderNodeInputHandle
) -> Tuple[MetasoundFrontendLiteral, MetaSoundBuilderResult]
```

x.get_node_input_default(input_handle) -> (MetasoundFrontendLiteral, out_result=MetaSoundBuilderResult)
Returns node input's literal value if set on graph, otherwise fails and returns default literal.

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.get_node_input_data"></a>

#### get_node_input_data

```python
def get_node_input_data(
    input_handle: MetaSoundBuilderNodeInputHandle
) -> Tuple[Name, Name, MetaSoundBuilderResult]
```

x.get_node_input_data(input_handle) -> (name=Name, data_type=Name, out_result=MetaSoundBuilderResult)
Returns node input's data if valid (including things like name and datatype).

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    tuple: 

    name (Name): 

    data_type (Name): 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.get_node_input_class_default"></a>

#### get_node_input_class_default

```python
def get_node_input_class_default(
    input_handle: MetaSoundBuilderNodeInputHandle
) -> Tuple[MetasoundFrontendLiteral, MetaSoundBuilderResult]
```

x.get_node_input_class_default(input_handle) -> (MetasoundFrontendLiteral, out_result=MetaSoundBuilderResult)
Returns node input's class literal value if set, otherwise fails and returns default literal.

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_outputs_by_data_type"></a>

#### find_node_outputs_by_data_type

```python
def find_node_outputs_by_data_type(
    node_handle: MetaSoundNodeHandle, data_type: Name
) -> Tuple[Array[MetaSoundBuilderNodeOutputHandle], MetaSoundBuilderResult]
```

x.find_node_outputs_by_data_type(node_handle, data_type) -> (Array[MetaSoundBuilderNodeOutputHandle], out_result=MetaSoundBuilderResult)
Returns node outputs by the given DataType (ex. "Audio", "Trigger", "String", "Bool", "Float", "Int32", etc.).

Args:
    node_handle (MetaSoundNodeHandle): 
    data_type (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_outputs"></a>

#### find_node_outputs

```python
def find_node_outputs(
    node_handle: MetaSoundNodeHandle
) -> Tuple[Array[MetaSoundBuilderNodeOutputHandle], MetaSoundBuilderResult]
```

x.find_node_outputs(node_handle) -> (Array[MetaSoundBuilderNodeOutputHandle], out_result=MetaSoundBuilderResult)
Returns all node outputs.

Args:
    node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_output_parent"></a>

#### find_node_output_parent

```python
def find_node_output_parent(
    output_handle: MetaSoundBuilderNodeOutputHandle
) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
```

x.find_node_output_parent(output_handle) -> (MetaSoundNodeHandle, out_result=MetaSoundBuilderResult)
Returns output's parent node if the input is valid, otherwise returns invalid node handle.

Args:
    output_handle (MetaSoundBuilderNodeOutputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_output_by_name"></a>

#### find_node_output_by_name

```python
def find_node_output_by_name(
    node_handle: MetaSoundNodeHandle, output_name: Name
) -> Tuple[MetaSoundBuilderNodeOutputHandle, MetaSoundBuilderResult]
```

x.find_node_output_by_name(node_handle, output_name) -> (MetaSoundBuilderNodeOutputHandle, out_result=MetaSoundBuilderResult)
Returns node output by the given name.

Args:
    node_handle (MetaSoundNodeHandle): 
    output_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_inputs_by_data_type"></a>

#### find_node_inputs_by_data_type

```python
def find_node_inputs_by_data_type(
    node_handle: MetaSoundNodeHandle, data_type: Name
) -> Tuple[Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
```

x.find_node_inputs_by_data_type(node_handle, data_type) -> (Array[MetaSoundBuilderNodeInputHandle], out_result=MetaSoundBuilderResult)
Returns node inputs by the given DataType (ex. "Audio", "Trigger", "String", "Bool", "Float", "Int32", etc.).

Args:
    node_handle (MetaSoundNodeHandle): 
    data_type (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_inputs"></a>

#### find_node_inputs

```python
def find_node_inputs(
    node_handle: MetaSoundNodeHandle
) -> Tuple[Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
```

x.find_node_inputs(node_handle) -> (Array[MetaSoundBuilderNodeInputHandle], out_result=MetaSoundBuilderResult)
Returns all node inputs.

Args:
    node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_input_parent"></a>

#### find_node_input_parent

```python
def find_node_input_parent(
    input_handle: MetaSoundBuilderNodeInputHandle
) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
```

x.find_node_input_parent(input_handle) -> (MetaSoundNodeHandle, out_result=MetaSoundBuilderResult)
Returns input's parent node if the input is valid, otherwise returns invalid node handle.

Args:
    input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_input_by_name"></a>

#### find_node_input_by_name

```python
def find_node_input_by_name(
    node_handle: MetaSoundNodeHandle, input_name: Name
) -> Tuple[MetaSoundBuilderNodeInputHandle, MetaSoundBuilderResult]
```

x.find_node_input_by_name(node_handle, input_name) -> (MetaSoundBuilderNodeInputHandle, out_result=MetaSoundBuilderResult)
Returns node input by the given name if it exists, or an invalid handle if not found.

Args:
    node_handle (MetaSoundNodeHandle): 
    input_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_node_class_version"></a>

#### find_node_class_version

```python
def find_node_class_version(
    node_handle: MetaSoundNodeHandle
) -> Tuple[MetasoundFrontendVersion, MetaSoundBuilderResult]
```

x.find_node_class_version(node_handle) -> (MetasoundFrontendVersion, out_result=MetaSoundBuilderResult)
Returns output's parent node if the input is valid, otherwise returns invalid node handle.

Args:
    node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_interface_output_nodes"></a>

#### find_interface_output_nodes

```python
def find_interface_output_nodes(
    interface_name: Name
) -> Tuple[Array[MetaSoundNodeHandle], MetaSoundBuilderResult]
```

x.find_interface_output_nodes(interface_name) -> (Array[MetaSoundNodeHandle], out_result=MetaSoundBuilderResult)
Returns output nodes associated with a given interface.

Args:
    interface_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_interface_input_nodes"></a>

#### find_interface_input_nodes

```python
def find_interface_input_nodes(
    interface_name: Name
) -> Tuple[Array[MetaSoundNodeHandle], MetaSoundBuilderResult]
```

x.find_interface_input_nodes(interface_name) -> (Array[MetaSoundNodeHandle], out_result=MetaSoundBuilderResult)
Returns input nodes associated with a given interface.

Args:
    interface_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_graph_output_node"></a>

#### find_graph_output_node

```python
def find_graph_output_node(
        output_name: Name
) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
```

x.find_graph_output_node(output_name) -> (MetaSoundNodeHandle, out_result=MetaSoundBuilderResult)
Returns graph output node by the given name if it exists, or an invalid handle if not found.

Args:
    output_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.find_graph_input_node"></a>

#### find_graph_input_node

```python
def find_graph_input_node(
        input_name: Name
) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
```

x.find_graph_input_node(input_name) -> (MetaSoundNodeHandle, out_result=MetaSoundBuilderResult)
Returns graph input node by the given name if it exists, or an invalid handle if not found.

Args:
    input_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.disconnect_nodes_by_interface_bindings"></a>

#### disconnect_nodes_by_interface_bindings

```python
def disconnect_nodes_by_interface_bindings(
        from_node_handle: MetaSoundNodeHandle,
        to_node_handle: MetaSoundNodeHandle) -> MetaSoundBuilderResult
```

x.disconnect_nodes_by_interface_bindings(from_node_handle, to_node_handle) -> MetaSoundBuilderResult
Disconnects two nodes using defined MetaSound Interface Bindings registered with the MetaSound Interface registry. Returns success if
all connections were found and removed, failed if any connections were not.

Args:
    from_node_handle (MetaSoundNodeHandle): 
    to_node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.disconnect_nodes"></a>

#### disconnect_nodes

```python
def disconnect_nodes(
    node_output_handle: MetaSoundBuilderNodeOutputHandle,
    node_input_handle: MetaSoundBuilderNodeInputHandle
) -> MetaSoundBuilderResult
```

x.disconnect_nodes(node_output_handle, node_input_handle) -> MetaSoundBuilderResult
Disconnects node output to a node input. Returns success if connection was removed, failed if not.

Args:
    node_output_handle (MetaSoundBuilderNodeOutputHandle): 
    node_input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.disconnect_node_output"></a>

#### disconnect_node_output

```python
def disconnect_node_output(
    node_output_handle: MetaSoundBuilderNodeOutputHandle
) -> MetaSoundBuilderResult
```

x.disconnect_node_output(node_output_handle) -> MetaSoundBuilderResult
Removes all connections from a given node output. Returns success if all connections were removed, failed if not.

Args:
    node_output_handle (MetaSoundBuilderNodeOutputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.disconnect_node_input"></a>

#### disconnect_node_input

```python
def disconnect_node_input(
    node_input_handle: MetaSoundBuilderNodeInputHandle
) -> MetaSoundBuilderResult
```

x.disconnect_node_input(node_input_handle) -> MetaSoundBuilderResult
Removes connection to a given node input. Returns success if connection was removed, failed if not.

Args:
    node_input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.convert_to_preset"></a>

#### convert_to_preset

```python
def convert_to_preset(
    referenced_node_class: MetaSoundDocumentInterface
) -> MetaSoundBuilderResult
```

x.convert_to_preset(referenced_node_class) -> MetaSoundBuilderResult
Convert this builder to a MetaSound source preset with the given referenced source builder

Args:
    referenced_node_class (MetaSoundDocumentInterface): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.convert_from_preset"></a>

#### convert_from_preset

```python
def convert_from_preset() -> MetaSoundBuilderResult
```

x.convert_from_preset() -> MetaSoundBuilderResult
Converts this preset to a fully accessible MetaSound; sets result to succeeded if it was converted successfully and failed if it was not.

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.contains_node_output"></a>

#### contains_node_output

```python
def contains_node_output(output: MetaSoundBuilderNodeOutputHandle) -> bool
```

x.contains_node_output(output) -> bool
Returns whether node output exists.

Args:
    output (MetaSoundBuilderNodeOutputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.contains_node_input"></a>

#### contains_node_input

```python
def contains_node_input(input: MetaSoundBuilderNodeInputHandle) -> bool
```

x.contains_node_input(input) -> bool
Returns whether node input exists.

Args:
    input (MetaSoundBuilderNodeInputHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.contains_node"></a>

#### contains_node

```python
def contains_node(node: MetaSoundNodeHandle) -> bool
```

x.contains_node(node) -> bool
Returns whether node exists.

Args:
    node (MetaSoundNodeHandle): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderBase.connect_nodes_by_interface_bindings"></a>

#### connect_nodes_by_interface_bindings

```python
def connect_nodes_by_interface_bindings(
        from_node_handle: MetaSoundNodeHandle,
        to_node_handle: MetaSoundNodeHandle) -> MetaSoundBuilderResult
```

x.connect_nodes_by_interface_bindings(from_node_handle, to_node_handle) -> MetaSoundBuilderResult
Connects two nodes using defined MetaSound Interface Bindings registered with the MetaSound Interface registry.

Args:
    from_node_handle (MetaSoundNodeHandle): 
    to_node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.connect_nodes"></a>

#### connect_nodes

```python
def connect_nodes(
    node_output_handle: MetaSoundBuilderNodeOutputHandle,
    node_input_handle: MetaSoundBuilderNodeInputHandle
) -> MetaSoundBuilderResult
```

x.connect_nodes(node_output_handle, node_input_handle) -> MetaSoundBuilderResult
Connects node output to a node input. Does *NOT* provide loop detection for performance reasons.  Loop detection is checked on class registration when built or played.
Returns succeeded if connection made, failed if connection already exists with input, the data types do not match, or the connection is not supported due to access type
incompatibility (ex. constructor input to non-constructor input).

Args:
    node_output_handle (MetaSoundBuilderNodeOutputHandle): 
    node_input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.connect_node_output_to_graph_output"></a>

#### connect_node_output_to_graph_output

```python
def connect_node_output_to_graph_output(
    graph_output_name: Name,
    node_output_handle: MetaSoundBuilderNodeOutputHandle
) -> MetaSoundBuilderResult
```

x.connect_node_output_to_graph_output(graph_output_name, node_output_handle) -> MetaSoundBuilderResult
Connects a given node output to the graph output with the given name.

Args:
    graph_output_name (Name): 
    node_output_handle (MetaSoundBuilderNodeOutputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.connect_node_outputs_to_matching_graph_interface_outputs"></a>

#### connect_node_outputs_to_matching_graph_interface_outputs

```python
def connect_node_outputs_to_matching_graph_interface_outputs(
    node_handle: MetaSoundNodeHandle
) -> Tuple[Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
```

x.connect_node_outputs_to_matching_graph_interface_outputs(node_handle) -> (Array[MetaSoundBuilderNodeInputHandle], out_result=MetaSoundBuilderResult)
Connects a given node's outputs to all graph outputs for shared interfaces implemented on both the node's referenced class and the builder's MetaSound graph. Returns inputs of connected output nodes.

Args:
    node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.connect_node_input_to_graph_input"></a>

#### connect_node_input_to_graph_input

```python
def connect_node_input_to_graph_input(
    graph_input_name: Name, node_input_handle: MetaSoundBuilderNodeInputHandle
) -> MetaSoundBuilderResult
```

x.connect_node_input_to_graph_input(graph_input_name, node_input_handle) -> MetaSoundBuilderResult
Connects a given node input to the graph input with the given name.

Args:
    graph_input_name (Name): 
    node_input_handle (MetaSoundBuilderNodeInputHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.connect_node_inputs_to_matching_graph_interface_inputs"></a>

#### connect_node_inputs_to_matching_graph_interface_inputs

```python
def connect_node_inputs_to_matching_graph_interface_inputs(
    node_handle: MetaSoundNodeHandle
) -> Tuple[Array[MetaSoundBuilderNodeOutputHandle], MetaSoundBuilderResult]
```

x.connect_node_inputs_to_matching_graph_interface_inputs(node_handle) -> (Array[MetaSoundBuilderNodeOutputHandle], out_result=MetaSoundBuilderResult)
Connects a given node's inputs to all graph inputs for shared interfaces implemented on both the node's referenced class and the builder's MetaSound graph. Returns outputs of connected input nodes.

Args:
    node_handle (MetaSoundNodeHandle): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.build_new_meta_sound"></a>

#### build_new_meta_sound

```python
def build_new_meta_sound(name_base: Name) -> MetaSoundDocumentInterface
```

x.build_new_meta_sound(name_base) -> MetaSoundDocumentInterface
Builds a transient MetaSound with the provided builder options, copying the underlying MetaSound
managed by this builder and registering it with the MetaSound Node Registry as a unique class. If
existing MetaSound exists with the provided NameBase, will make object with unique name with the given
NameBase as prefix.

Args:
    name_base (Name): 

Returns:
    MetaSoundDocumentInterface:

<a id="unreal.MetaSoundBuilderBase.build_and_overwrite_meta_sound"></a>

#### build_and_overwrite_meta_sound

```python
def build_and_overwrite_meta_sound(
        existing_meta_sound: MetaSoundDocumentInterface,
        force_unique_class_name: bool = False) -> None
```

x.build_and_overwrite_meta_sound(existing_meta_sound, force_unique_class_name=False) -> None
Copies a transient MetaSound with the provided builder options, copying the underlying MetaSound
managed by this builder and registering it with the MetaSound Node Registry as a unique name.
If 'Force Unique Class Name' is true, registers MetaSound as a new class in the registry, potentially
invalidating existing references in other MetaSounds. Not permissible to overwrite MetaSound asset,
only transient MetaSound (see EditorSubsystem for overwriting assets at edit time).

Args:
    existing_meta_sound (MetaSoundDocumentInterface): 
    force_unique_class_name (bool):

<a id="unreal.MetaSoundBuilderBase.build"></a>

#### build

```python
def build(parent: Object,
          options: MetaSoundBuilderOptions) -> MetaSoundDocumentInterface
```

x.build(parent, options) -> MetaSoundDocumentInterface
Build

Args:
    parent (Object): 
    options (MetaSoundBuilderOptions): 

Returns:
    MetaSoundDocumentInterface:

<a id="unreal.MetaSoundBuilderBase.add_node_by_class_name"></a>

#### add_node_by_class_name

```python
def add_node_by_class_name(
    class_name: MetasoundFrontendClassName,
    major_version: int = 1
) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
```

x.add_node_by_class_name(class_name, major_version=1) -> (MetaSoundNodeHandle, out_result=MetaSoundBuilderResult)
Adds node referencing the highest native class version of the given class name to the document.
Returns a node handle to the created node if successful, or an invalid handle if it failed.

Args:
    class_name (MetasoundFrontendClassName): 
    major_version (int32): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.add_node"></a>

#### add_node

```python
def add_node(
    node_class: MetaSoundDocumentInterface
) -> Tuple[MetaSoundNodeHandle, MetaSoundBuilderResult]
```

x.add_node(node_class) -> (MetaSoundNodeHandle, out_result=MetaSoundBuilderResult)
Adds a node to the graph using the provided MetaSound asset as its defining NodeClass.
Returns a node handle to the created node if successful, or an invalid handle if it failed.

Args:
    node_class (MetaSoundDocumentInterface): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.add_interface"></a>

#### add_interface

```python
def add_interface(interface_name: Name) -> MetaSoundBuilderResult
```

x.add_interface(interface_name) -> MetaSoundBuilderResult
Adds an interface registered with the given name to the graph, adding associated input and output nodes.

Args:
    interface_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.add_graph_output_node"></a>

#### add_graph_output_node

```python
def add_graph_output_node(
    name: Name,
    data_type: Name,
    default_value: MetasoundFrontendLiteral,
    is_constructor_output: bool = False
) -> Tuple[MetaSoundBuilderNodeInputHandle, MetaSoundBuilderResult]
```

x.add_graph_output_node(name, data_type, default_value, is_constructor_output=False) -> (MetaSoundBuilderNodeInputHandle, out_result=MetaSoundBuilderResult)
Adds a graph output node with the given name, DataType, and sets output node's input to default value.
Returns the new output node's input handle if it was successfully created, or an invalid handle if it failed.

Args:
    name (Name): 
    data_type (Name): 
    default_value (MetasoundFrontendLiteral): 
    is_constructor_output (bool): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderBase.add_graph_input_node"></a>

#### add_graph_input_node

```python
def add_graph_input_node(
    name: Name,
    data_type: Name,
    default_value: MetasoundFrontendLiteral,
    is_constructor_input: bool = False
) -> Tuple[MetaSoundBuilderNodeOutputHandle, MetaSoundBuilderResult]
```

x.add_graph_input_node(name, data_type, default_value, is_constructor_input=False) -> (MetaSoundBuilderNodeOutputHandle, out_result=MetaSoundBuilderResult)
Adds a graph input node with the given name, DataType, and sets the graph input to default value.
Returns the new input node's output handle if it was successfully created, or an invalid handle if it failed.

Args:
    name (Name): 
    data_type (Name): 
    default_value (MetasoundFrontendLiteral): 
    is_constructor_input (bool): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundPatchBuilder"></a>