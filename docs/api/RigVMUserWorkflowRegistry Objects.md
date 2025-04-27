## RigVMUserWorkflowRegistry Objects

```python
class RigVMUserWorkflowRegistry(Object)
```

Rig VMUser Workflow Registry

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMUserWorkflowRegistry.h

<a id="unreal.RigVMUserWorkflowRegistry.unregister_provider"></a>

#### unregister_provider

```python
def unregister_provider(handle: int) -> None
```

x.unregister_provider(handle) -> None
Unregister Provider

Args:
    handle (int32):

<a id="unreal.RigVMUserWorkflowRegistry.register_provider"></a>

#### register_provider

```python
def register_provider(struct: ScriptStruct,
                      provider: RigVMUserWorkflowProvider) -> int
```

x.register_provider(struct, provider) -> int32
Register Provider

Args:
    struct (ScriptStruct): 
    provider (RigVMUserWorkflowProvider): 

Returns:
    int32:

<a id="unreal.RigVMUserWorkflowRegistry.get_workflows"></a>

#### get_workflows

```python
def get_workflows(type: RigVMUserWorkflowType, struct: ScriptStruct,
                  subject: Object) -> Array[RigVMUserWorkflow]
```

x.get_workflows(type, struct, subject) -> Array[RigVMUserWorkflow]
Get Workflows

Args:
    type (RigVMUserWorkflowType): 
    struct (ScriptStruct): 
    subject (Object): 

Returns:
    Array[RigVMUserWorkflow]:

<a id="unreal.RigVMUserWorkflowRegistry.get"></a>

#### get

```python
@classmethod
def get(cls) -> RigVMUserWorkflowRegistry
```

X.get() -> RigVMUserWorkflowRegistry
Get

Returns:
    RigVMUserWorkflowRegistry:

<a id="unreal.ControlRigShapeLibraryLink"></a>