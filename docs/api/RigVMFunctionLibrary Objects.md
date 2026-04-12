## RigVMFunctionLibrary Objects

```python
class RigVMFunctionLibrary(RigVMGraph)
```

The Function Library is a graph used only to store
the sub graphs used for functions.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMFunctionLibrary.h

<a id="unreal.RigVMFunctionLibrary.get_references_for_function"></a>

#### get\_references\_for\_function

```python
def get_references_for_function(
        function_name: Name) -> Array[RigVMFunctionReferenceNode]
```

x.get_references_for_function(function_name) -> Array[RigVMFunctionReferenceNode]
Returns all references for a given function name

Args:
    function_name (Name): 

Returns:
    Array[RigVMFunctionReferenceNode]:

<a id="unreal.RigVMFunctionLibrary.get_reference_paths_for_function"></a>

#### get\_reference\_paths\_for\_function

```python
def get_reference_paths_for_function(function_name: Name) -> Array[str]
```

x.get_reference_paths_for_function(function_name) -> Array[str]
Returns all references for a given function name

Args:
    function_name (Name): 

Returns:
    Array[str]:

<a id="unreal.RigVMFunctionLibrary.get_functions"></a>

#### get\_functions

```python
def get_functions() -> Array[RigVMLibraryNode]
```

x.get_functions() -> Array[RigVMLibraryNode]
Returns all of the stored functions

Returns:
    Array[RigVMLibraryNode]:

<a id="unreal.RigVMFunctionLibrary.find_function_for_node"></a>

#### find\_function\_for\_node

```python
def find_function_for_node(node: RigVMNode) -> RigVMLibraryNode
```

x.find_function_for_node(node) -> RigVMLibraryNode
Finds a function by a node within a function (or a sub graph of that)

Args:
    node (RigVMNode): 

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMFunctionLibrary.find_function"></a>

#### find\_function

```python
def find_function(function_name: Name) -> RigVMLibraryNode
```

x.find_function(function_name) -> RigVMLibraryNode
Finds a function by name

Args:
    function_name (Name): 

Returns:
    RigVMLibraryNode:

<a id="unreal.RigVMLink"></a>