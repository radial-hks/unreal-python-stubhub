## RigVMCompiler Objects

```python
class RigVMCompiler(Object)
```

Rig VMCompiler

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMCompiler.h

<a id="unreal.RigVMCompiler.compile_vm"></a>

#### compile_vm

```python
def compile_vm(graphs: Array[RigVMGraph], controller: RigVMController,
               out_vm: RigVM) -> Optional[RigVMExtendedExecuteContext]
```

x.compile_vm(graphs, controller, out_vm) -> RigVMExtendedExecuteContext or None
Compile VM

Args:
    graphs (Array[RigVMGraph]): 
    controller (RigVMController): 
    out_vm (RigVM): 

Returns:
    RigVMExtendedExecuteContext or None: 

    context (RigVMExtendedExecuteContext):

<a id="unreal.RigVMCompiler.compile"></a>

#### compile

```python
def compile(graphs: Array[RigVMGraph], controller: RigVMController,
            out_vm: RigVM) -> bool
```

x.compile(graphs, controller, out_vm) -> bool
Compile
deprecated: Compile is deprecated, use CompileVM with Context parameter.

Args:
    graphs (Array[RigVMGraph]): 
    controller (RigVMController): 
    out_vm (RigVM): 

Returns:
    bool:

<a id="unreal.RigVMNode"></a>