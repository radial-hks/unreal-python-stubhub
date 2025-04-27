## RigVMParameterNode Objects

```python
class RigVMParameterNode(RigVMNode)
```

The Parameter Node represents an input or output argument / parameter
of the Function / Graph. Parameter Node have only a single value pin.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMParameterNode.h

<a id="unreal.RigVMParameterNode.is_input"></a>

#### is_input

```python
def is_input() -> bool
```

x.is_input() -> bool
Returns true if this node is an input

Returns:
    bool:

<a id="unreal.RigVMParameterNode.get_parameter_name"></a>

#### get_parameter_name

```python
def get_parameter_name() -> Name
```

x.get_parameter_name() -> Name
Returns the name of the parameter

Returns:
    Name:

<a id="unreal.RigVMParameterNode.get_parameter_description"></a>

#### get_parameter_description

```python
def get_parameter_description() -> RigVMGraphParameterDescription
```

x.get_parameter_description() -> RigVMGraphParameterDescription
Returns this parameter node's parameter description

Returns:
    RigVMGraphParameterDescription:

<a id="unreal.RigVMParameterNode.get_default_value"></a>

#### get_default_value

```python
def get_default_value() -> str
```

x.get_default_value() -> str
Returns the default value of the parameter as a string

Returns:
    str:

<a id="unreal.RigVMParameterNode.get_cpp_type_object"></a>

#### get_cpp_type_object

```python
def get_cpp_type_object() -> Object
```

x.get_cpp_type_object() -> Object
Returns the C++ data type struct of the parameter (or nullptr)

Returns:
    Object:

<a id="unreal.RigVMParameterNode.get_cpp_type"></a>

#### get_cpp_type

```python
def get_cpp_type() -> str
```

x.get_cpp_type() -> str
Returns the C++ data type of the parameter

Returns:
    str:

<a id="unreal.RigVMRerouteNode"></a>