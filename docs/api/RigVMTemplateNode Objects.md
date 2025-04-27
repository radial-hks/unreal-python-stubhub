## RigVMTemplateNode Objects

```python
class RigVMTemplateNode(RigVMNode)
```

The Template Node represents an unresolved function.
Template nodes can morph into all functions implementing
the template's template.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMTemplateNode.h

<a id="unreal.RigVMTemplateNode.is_singleton"></a>

#### is_singleton

```python
def is_singleton() -> bool
```

x.is_singleton() -> bool
Is Singleton

Returns:
    bool:

<a id="unreal.RigVMTemplateNode.is_resolved"></a>

#### is_resolved

```python
def is_resolved() -> bool
```

x.is_resolved() -> bool
returns true if the template node is resolved

Returns:
    bool:

<a id="unreal.RigVMTemplateNode.is_fully_unresolved"></a>

#### is_fully_unresolved

```python
def is_fully_unresolved() -> bool
```

x.is_fully_unresolved() -> bool
returns true if the template is fully unresolved

Returns:
    bool:

<a id="unreal.RigVMTemplateNode.get_script_struct"></a>

#### get_script_struct

```python
def get_script_struct() -> ScriptStruct
```

x.get_script_struct() -> ScriptStruct
Returns the UStruct for this unit node
(the struct declaring the RIGVM_METHOD)

Returns:
    ScriptStruct:

<a id="unreal.RigVMTemplateNode.get_notation"></a>

#### get_notation

```python
def get_notation() -> Name
```

x.get_notation() -> Name
Returns the notation of the node

Returns:
    Name:

<a id="unreal.RigVMLibraryNode"></a>