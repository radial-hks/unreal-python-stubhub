## RigVMGraphFunctionIdentifier Objects

```python
class RigVMGraphFunctionIdentifier(StructBase)
```

Rig VMGraph Function Identifier

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMGraphFunctionDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``host_object`` (SoftObjectPath):  [Read-Only] A path to the IRigVMGraphFunctionHost that stores the function information, and compilation data (e.g. RigVMBlueprintGeneratedClass)
- ``library_node`` (SoftObjectPath):  [Read-Write]
  deprecated: Property 'LibraryNode' is deprecated.
- ``library_node_path`` (str):  [Read-Only]

<a id="unreal.RigVMGraphFunctionIdentifier.__init__"></a>

#### __init__

```python
def __init__(host_object: SoftObjectPath = [""]) -> None
```

<a id="unreal.RigVMGraphFunctionIdentifier.library_node"></a>

#### library_node

```python
@property
def library_node() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]
deprecated: Property 'LibraryNode' is deprecated.

<a id="unreal.RigVMGraphFunctionIdentifier.library_node"></a>

#### library_node

```python
@library_node.setter
def library_node(value: SoftObjectPath) -> None
```

<a id="unreal.RigVMGraphFunctionIdentifier.host_object"></a>

#### host_object

```python
@property
def host_object() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only] A path to the IRigVMGraphFunctionHost that stores the function information, and compilation data (e.g. RigVMBlueprintGeneratedClass)

<a id="unreal.RigVMGraphFunctionArgument"></a>