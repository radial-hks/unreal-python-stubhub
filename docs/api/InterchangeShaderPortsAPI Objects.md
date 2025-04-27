## InterchangeShaderPortsAPI Objects

```python
class InterchangeShaderPortsAPI(Object)
```

The Shader Ports API manages a set of inputs and outputs attributes.
This API can be used over any InterchangeBaseNode that wants to support shader ports as attributes.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeShaderGraphNode.h

<a id="unreal.InterchangeShaderPortsAPI.make_input_value_key"></a>

#### make_input_value_key

```python
@classmethod
def make_input_value_key(cls, input_name: str) -> str
```

X.make_input_value_key(input_name) -> str
Makes an attribute key to represent a value being given to an input (that is, Inputs:InputName:Value).

Args:
    input_name (str): 

Returns:
    str:

<a id="unreal.InterchangeShaderPortsAPI.make_input_parameter_key"></a>

#### make_input_parameter_key

```python
@classmethod
def make_input_parameter_key(cls, input_name: str) -> str
```

X.make_input_parameter_key(input_name) -> str
Makes an attribute key to represent a parameter being given to an input (that is, Inputs:InputName:Parameter).
This is more relevant to Materials, but could be used to differentiate between constant values and parameters.

Args:
    input_name (str): 

Returns:
    str:

<a id="unreal.InterchangeShaderPortsAPI.make_input_name"></a>

#### make_input_name

```python
@classmethod
def make_input_name(cls, input_key: str) -> str
```

X.make_input_name(input_key) -> str
From an attribute key associated with an input (that is, Inputs:InputName:Value), retrieves the input name.

Args:
    input_key (str): 

Returns:
    str:

<a id="unreal.InterchangeShaderPortsAPI.make_input_connection_key"></a>

#### make_input_connection_key

```python
@classmethod
def make_input_connection_key(cls, input_name: str) -> str
```

X.make_input_connection_key(input_name) -> str
Makes an attribute key to represent a node being connected to an input (that is, Inputs:InputName:Connect).

Args:
    input_name (str): 

Returns:
    str:

<a id="unreal.InterchangeShaderPortsAPI.is_a_parameter"></a>

#### is_a_parameter

```python
@classmethod
def is_a_parameter(cls, attribute_key: str) -> bool
```

X.is_a_parameter(attribute_key) -> bool
Returns true if the attribute key is an input that represents parameters (ends with ":Parameter").

Args:
    attribute_key (str): 

Returns:
    bool:

<a id="unreal.InterchangeShaderPortsAPI.is_an_input"></a>

#### is_an_input

```python
@classmethod
def is_an_input(cls, attribute_key: str) -> bool
```

X.is_an_input(attribute_key) -> bool
Returns true if the attribute key is associated with an input (starts with "Inputs:").

Args:
    attribute_key (str): 

Returns:
    bool:

<a id="unreal.InterchangeShaderPortsAPI.has_parameter"></a>

#### has_parameter

```python
@classmethod
def has_parameter(cls, interchange_node: InterchangeBaseNode,
                  input_name: Name) -> bool
```

X.has_parameter(interchange_node, input_name) -> bool
Checks whether a particular input exists as a parameter on a given node.

Args:
    interchange_node (InterchangeBaseNode): 
    input_name (Name): 

Returns:
    bool:

<a id="unreal.InterchangeShaderPortsAPI.has_input"></a>

#### has_input

```python
@classmethod
def has_input(cls, interchange_node: InterchangeBaseNode,
              input_name: Name) -> bool
```

X.has_input(interchange_node, input_name) -> bool
Checks whether a particular input exists on a given node.

Args:
    interchange_node (InterchangeBaseNode): 
    input_name (Name): 

Returns:
    bool:

<a id="unreal.InterchangeShaderPortsAPI.get_input_connection"></a>

#### get_input_connection

```python
@classmethod
def get_input_connection(cls, interchange_node: InterchangeBaseNode,
                         input_name: str) -> Optional[Tuple[str, str]]
```

X.get_input_connection(interchange_node, input_name) -> (out_expression_uid=str, output_name=str) or None
Retrieves the node unique id and the output name connected to a given input, if any.

Args:
    interchange_node (InterchangeBaseNode): 
    input_name (str): 

Returns:
    tuple or None: 

    out_expression_uid (str): 

    output_name (str):

<a id="unreal.InterchangeShaderPortsAPI.gather_inputs"></a>

#### gather_inputs

```python
@classmethod
def gather_inputs(cls, interchange_node: InterchangeBaseNode) -> Array[str]
```

X.gather_inputs(interchange_node) -> Array[str]
Retrieves the names of all the inputs for a given node.

Args:
    interchange_node (InterchangeBaseNode): 

Returns:
    Array[str]: 

    out_input_names (Array[str]):

<a id="unreal.InterchangeShaderPortsAPI.connect_ouput_to_input_by_name"></a>

#### connect_ouput_to_input_by_name

```python
@classmethod
def connect_ouput_to_input_by_name(cls, interchange_node: InterchangeBaseNode,
                                   input_name: str, expression_uid: str,
                                   output_name: str) -> bool
```

X.connect_ouput_to_input_by_name(interchange_node, input_name, expression_uid, output_name) -> bool
Adds an input connection attribute.

Args:
    interchange_node (InterchangeBaseNode): The node to create the input on.
    input_name (str): The name to give to the input.
    expression_uid (str): The unique ID of the node to connect to the input.
    output_name (str): The name of the output from ExpressionUid to connect to the input.

Returns:
    bool: True if the input connection was successfully added to the node.

<a id="unreal.InterchangeShaderPortsAPI.connect_ouput_to_input_by_index"></a>

#### connect_ouput_to_input_by_index

```python
@classmethod
def connect_ouput_to_input_by_index(cls, interchange_node: InterchangeBaseNode,
                                    input_name: str, expression_uid: str,
                                    output_index: int) -> bool
```

X.connect_ouput_to_input_by_index(interchange_node, input_name, expression_uid, output_index) -> bool
Adds an input connection attribute.

Args:
    interchange_node (InterchangeBaseNode): The node to create the input on.
    input_name (str): The name to give to the input.
    expression_uid (str): The unique ID of the node to connect to the input.
    output_index (int32): The index of the output from ExpressionUid to connect to the input.

Returns:
    bool: True if the input connection was successfully added to the node. OutputIndex is encoded in a string in the following pattern: ExpressionUid:OutputByIndex:FString::FromInt(OutputIndex) The index should be retrieved using UInterchangeShaderPortsAPI::GetOutputIndexFromName().

<a id="unreal.InterchangeShaderPortsAPI.connect_default_ouput_to_input"></a>

#### connect_default_ouput_to_input

```python
@classmethod
def connect_default_ouput_to_input(cls, interchange_node: InterchangeBaseNode,
                                   input_name: str,
                                   expression_uid: str) -> bool
```

X.connect_default_ouput_to_input(interchange_node, input_name, expression_uid) -> bool
Adds an input connection attribute.

Args:
    interchange_node (InterchangeBaseNode): The node to create the input on.
    input_name (str): The name to give to the input.
    expression_uid (str): The unique ID of the node to connect to the input.

Returns:
    bool: True if the input connection was successfully added to the node.

<a id="unreal.InterchangeFunctionCallShaderNode"></a>