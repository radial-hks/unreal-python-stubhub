## RigVMUserWorkflow Objects

```python
class RigVMUserWorkflow(StructBase)
```

Rig VMUser Workflow

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMUserWorkflow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_perform_workflow`` (RigVMPeformUserWorkflowDynamicDelegate):  [Read-Write]
- ``options_class`` (type(Class)):  [Read-Write]
- ``title`` (str):  [Read-Write]
- ``tooltip`` (str):  [Read-Write]
- ``type`` (RigVMUserWorkflowType):  [Read-Write]

<a id="unreal.RigVMUserWorkflow.__init__"></a>

#### __init__

```python
def __init__(
        title: str = "",
        tooltip: str = "",
        type: RigVMUserWorkflowType = 0,
        on_perform_workflow:
    RigVMPeformUserWorkflowDynamicDelegate = RigVMPeformUserWorkflowDynamicDelegate(
    ),
        options_class: Class = None) -> None
```

<a id="unreal.RigVMUserWorkflow.title"></a>

#### title

```python
@property
def title() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMUserWorkflow.title"></a>

#### title

```python
@title.setter
def title(value: str) -> None
```

<a id="unreal.RigVMUserWorkflow.tooltip"></a>

#### tooltip

```python
@property
def tooltip() -> str
```

(str):  [Read-Write]

<a id="unreal.RigVMUserWorkflow.tooltip"></a>

#### tooltip

```python
@tooltip.setter
def tooltip(value: str) -> None
```

<a id="unreal.RigVMUserWorkflow.type"></a>

#### type

```python
@property
def type() -> RigVMUserWorkflowType
```

(RigVMUserWorkflowType):  [Read-Write]

<a id="unreal.RigVMUserWorkflow.type"></a>

#### type

```python
@type.setter
def type(value: RigVMUserWorkflowType) -> None
```

<a id="unreal.RigVMUserWorkflow.on_perform_workflow"></a>

#### on_perform_workflow

```python
@property
def on_perform_workflow() -> RigVMPeformUserWorkflowDynamicDelegate
```

(RigVMPeformUserWorkflowDynamicDelegate):  [Read-Write]

<a id="unreal.RigVMUserWorkflow.on_perform_workflow"></a>

#### on_perform_workflow

```python
@on_perform_workflow.setter
def on_perform_workflow(value: RigVMPeformUserWorkflowDynamicDelegate) -> None
```

<a id="unreal.RigVMUserWorkflow.options_class"></a>

#### options_class

```python
@property
def options_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.RigVMUserWorkflow.options_class"></a>

#### options_class

```python
@options_class.setter
def options_class(value: Class) -> None
```

<a id="unreal.RigElementKey"></a>