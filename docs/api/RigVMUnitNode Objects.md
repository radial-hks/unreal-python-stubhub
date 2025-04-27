## RigVMUnitNode Objects

```python
class RigVMUnitNode(RigVMTemplateNode)
```

The Struct Node represents a Function Invocation of a RIGVM_METHOD
declared on a USTRUCT. Struct Nodes have input / output pins for all
struct UPROPERTY members.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMUnitNode.h

<a id="unreal.RigVMUnitNode.get_struct_default_value"></a>

#### get_struct_default_value

```python
def get_struct_default_value() -> str
```

x.get_struct_default_value() -> str
Returns the default value for the struct as text

Returns:
    str:

<a id="unreal.RigVMUnitNode.get_method_name"></a>

#### get_method_name

```python
def get_method_name() -> Name
```

x.get_method_name() -> Name
Returns the name of the declared RIGVM_METHOD

Returns:
    Name:

<a id="unreal.RigVMStructNode"></a>