## RigVMLibraryNode Objects

```python
class RigVMLibraryNode(RigVMTemplateNode)
```

The Library Node represents a function invocation of a
function specified somewhere else. The function can be
expressed as a sub-graph (RigVMGroupNode) or as a
referenced function (RigVMFunctionNode).

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMLibraryNode.h

<a id="unreal.RigVMLibraryNode.get_matching_variants"></a>

#### get_matching_variants

```python
def get_matching_variants() -> Array[RigVMVariantRef]
```

x.get_matching_variants() -> Array[RigVMVariantRef]
Get Matching Variants

Returns:
    Array[RigVMVariantRef]:

<a id="unreal.RigVMLibraryNode.get_library"></a>

#### get_library

```python
def get_library() -> RigVMFunctionLibrary
```

x.get_library() -> RigVMFunctionLibrary
Get Library

Returns:
    RigVMFunctionLibrary:

<a id="unreal.RigVMLibraryNode.get_function_variant"></a>

#### get_function_variant

```python
def get_function_variant() -> RigVMVariant
```

x.get_function_variant() -> RigVMVariant
Get Function Variant

Returns:
    RigVMVariant:

<a id="unreal.RigVMLibraryNode.get_contained_graph"></a>

#### get_contained_graph

```python
def get_contained_graph() -> RigVMGraph
```

x.get_contained_graph() -> RigVMGraph
Get Contained Graph

Returns:
    RigVMGraph:

<a id="unreal.RigVMCollapseNode"></a>