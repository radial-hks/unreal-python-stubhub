## RigVMEditorMenuContext Objects

```python
class RigVMEditorMenuContext(Object)
```

Rig VMEditor Menu Context

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMEditor
- **File**: RigVMEditorMenuContext.h

<a id="unreal.RigVMEditorMenuContext.is_alt_down"></a>

#### is_alt_down

```python
def is_alt_down() -> bool
```

x.is_alt_down() -> bool
Returns true if either alt key is down

Returns:
    bool:

<a id="unreal.RigVMEditorMenuContext.get_rig_vm_host"></a>

#### get_rig_vm_host

```python
def get_rig_vm_host() -> RigVMHost
```

x.get_rig_vm_host() -> RigVMHost
Get the active rigvm host instance in the viewport

Returns:
    RigVMHost:

<a id="unreal.RigVMEditorMenuContext.get_rig_vm_blueprint"></a>

#### get_rig_vm_blueprint

```python
def get_rig_vm_blueprint() -> RigVMBlueprint
```

x.get_rig_vm_blueprint() -> RigVMBlueprint
Get the rigvm blueprint that we are editing

Returns:
    RigVMBlueprint:

<a id="unreal.RigVMEditorMenuContext.get_graph_menu_context"></a>

#### get_graph_menu_context

```python
def get_graph_menu_context() -> RigVMEditorGraphMenuContext
```

x.get_graph_menu_context() -> RigVMEditorGraphMenuContext
Returns context for graph node context menu

Returns:
    RigVMEditorGraphMenuContext:

<a id="unreal.RigVMBlueprintLibrary"></a>