## ControlRigWorkflowOptions Objects

```python
class ControlRigWorkflowOptions(RigVMUserWorkflowOptions)
```

Control Rig Workflow Options

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigNodeWorkflow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hierarchy`` (RigHierarchy):  [Read-Write]
- ``selection`` (Array[RigElementKey]):  [Read-Write]
- ``subject`` (Object):  [Read-Write]
- ``workflow`` (RigVMUserWorkflow):  [Read-Write]

<a id="unreal.ControlRigWorkflowOptions.hierarchy"></a>

#### hierarchy

```python
@property
def hierarchy() -> RigHierarchy
```

(RigHierarchy):  [Read-Write]

<a id="unreal.ControlRigWorkflowOptions.hierarchy"></a>

#### hierarchy

```python
@hierarchy.setter
def hierarchy(value: RigHierarchy) -> None
```

<a id="unreal.ControlRigWorkflowOptions.selection"></a>

#### selection

```python
@property
def selection() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write]

<a id="unreal.ControlRigWorkflowOptions.selection"></a>

#### selection

```python
@selection.setter
def selection(value: Array[RigElementKey]) -> None
```

<a id="unreal.ControlRigWorkflowOptions.ensure_at_least_one_rig_element_selected"></a>

#### ensure_at_least_one_rig_element_selected

```python
def ensure_at_least_one_rig_element_selected() -> bool
```

x.ensure_at_least_one_rig_element_selected() -> bool
Ensure at Least One Rig Element Selected

Returns:
    bool:

<a id="unreal.ControlRigTransformWorkflowOptions"></a>