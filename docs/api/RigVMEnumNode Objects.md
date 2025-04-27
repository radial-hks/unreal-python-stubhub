## RigVMEnumNode Objects

```python
class RigVMEnumNode(RigVMNode)
```

The Enum Node represents a constant enum value for use within the graph.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMEnumNode.h

<a id="unreal.RigVMEnumNode.get_enum"></a>

#### get_enum

```python
def get_enum() -> Enum
```

x.get_enum() -> Enum
Returns the enum itself

Returns:
    Enum:

<a id="unreal.RigVMEnumNode.get_cpp_type_object"></a>

#### get_cpp_type_object

```python
def get_cpp_type_object() -> Object
```

x.get_cpp_type_object() -> Object
Returns the C++ data type struct of the parameter (or nullptr)

Returns:
    Object:

<a id="unreal.RigVMEnumNode.get_cpp_type"></a>

#### get_cpp_type

```python
def get_cpp_type() -> str
```

x.get_cpp_type() -> str
Returns the C++ data type of the parameter

Returns:
    str:

<a id="unreal.RigVMFunctionInterfaceNode"></a>