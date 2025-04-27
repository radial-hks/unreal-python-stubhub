## RigVMArrayNode Objects

```python
class RigVMArrayNode(RigVMTemplateNode)
```

The Array Node represents one of a series available
array operations such as SetNum, GetAtIndex etc.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMArrayNode.h

<a id="unreal.RigVMArrayNode.get_op_code"></a>

#### get_op_code

```python
def get_op_code() -> RigVMOpCode
```

x.get_op_code() -> RigVMOpCode
Returns the op code of this node

Returns:
    RigVMOpCode:

<a id="unreal.RigVMArrayNode.get_cpp_type_object"></a>

#### get_cpp_type_object

```python
def get_cpp_type_object() -> Object
```

x.get_cpp_type_object() -> Object
Returns the C++ data type struct of the array (or nullptr)

Returns:
    Object:

<a id="unreal.RigVMArrayNode.get_cpp_type"></a>

#### get_cpp_type

```python
def get_cpp_type() -> str
```

x.get_cpp_type() -> str
Returns the C++ data type of the element

Returns:
    str:

<a id="unreal.RigVMBranchNode"></a>