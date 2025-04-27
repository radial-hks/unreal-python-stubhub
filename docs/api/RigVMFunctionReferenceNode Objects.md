## RigVMFunctionReferenceNode Objects

```python
class RigVMFunctionReferenceNode(RigVMLibraryNode)
```

The Function Reference Node is a library node which references
a library node from a separate function library graph.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMFunctionReferenceNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``referenced_node_ptr`` (RigVMLibraryNode):  [Read-Write]
  deprecated: Property 'ReferencedNodePtr' is deprecated.

<a id="unreal.RigVMFunctionReferenceNode.referenced_node_ptr"></a>

#### referenced_node_ptr

```python
@property
def referenced_node_ptr() -> RigVMLibraryNode
```

(RigVMLibraryNode):  [Read-Write]
deprecated: Property 'ReferencedNodePtr' is deprecated.

<a id="unreal.RigVMFunctionReferenceNode.referenced_node_ptr"></a>

#### referenced_node_ptr

```python
@referenced_node_ptr.setter
def referenced_node_ptr(value: RigVMLibraryNode) -> None
```

<a id="unreal.RigVMFunctionReferenceNode.get_referenced_function_header"></a>

#### get_referenced_function_header

```python
def get_referenced_function_header() -> RigVMGraphFunctionHeader
```

x.get_referenced_function_header() -> RigVMGraphFunctionHeader
Get Referenced Function Header for Blueprint

Returns:
    RigVMGraphFunctionHeader:

<a id="unreal.RigVMFunctionReturnNode"></a>