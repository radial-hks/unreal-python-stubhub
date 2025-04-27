## RigVMVariableNode Objects

```python
class RigVMVariableNode(RigVMNode)
```

The Variable Node represents a mutable value / local state within the
the Function / Graph. Variable Node's can be a getter or a setter.
Getters are pure nodes with just an output value pin, while setters
are mutable nodes with an execute and input value pin.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMVariableNode.h

<a id="unreal.RigVMVariableNode.is_local_variable"></a>

#### is_local_variable

```python
def is_local_variable() -> bool
```

x.is_local_variable() -> bool
Returns true if this variable is a local variable

Returns:
    bool:

<a id="unreal.RigVMVariableNode.is_input_argument"></a>

#### is_input_argument

```python
def is_input_argument() -> bool
```

x.is_input_argument() -> bool
Returns true if this variable is an input argument

Returns:
    bool:

<a id="unreal.RigVMVariableNode.is_getter"></a>

#### is_getter

```python
def is_getter() -> bool
```

x.is_getter() -> bool
Returns true if this node is a variable getter

Returns:
    bool:

<a id="unreal.RigVMVariableNode.is_external_variable"></a>

#### is_external_variable

```python
def is_external_variable() -> bool
```

x.is_external_variable() -> bool
Returns true if this variable is an external variable

Returns:
    bool:

<a id="unreal.RigVMVariableNode.get_variable_name"></a>

#### get_variable_name

```python
def get_variable_name() -> Name
```

x.get_variable_name() -> Name
Returns the name of the variable

Returns:
    Name:

<a id="unreal.RigVMVariableNode.get_variable_description"></a>

#### get_variable_description

```python
def get_variable_description() -> RigVMGraphVariableDescription
```

x.get_variable_description() -> RigVMGraphVariableDescription
Returns this variable node's variable description

Returns:
    RigVMGraphVariableDescription:

<a id="unreal.RigVMVariableNode.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> str
```

x.get_default_value() -> str
Returns the default value of the variable as a string

Returns:
    str:

<a id="unreal.RigVMVariableNode.get_cpp_type_object"></a>

#### get_cpp_type_object

```python
def get_cpp_type_object() -> Object
```

x.get_cpp_type_object() -> Object
Returns the C++ data type struct of the variable (or nullptr)

Returns:
    Object:

<a id="unreal.RigVMVariableNode.get_cpp_type"></a>

#### get_cpp_type

```python
def get_cpp_type() -> str
```

x.get_cpp_type() -> str
Returns the C++ data type of the variable

Returns:
    str:

<a id="unreal.RigVMController"></a>