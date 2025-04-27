## RigVMUserWorkflowOptions Objects

```python
class RigVMUserWorkflowOptions(Object)
```

Rig VMUser Workflow Options

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMUserWorkflow.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``subject`` (Object):  [Read-Write]
- ``workflow`` (RigVMUserWorkflow):  [Read-Write]

<a id="unreal.RigVMUserWorkflowOptions.subject"></a>

#### subject

```python
@property
def subject() -> Object
```

(Object):  [Read-Only]

<a id="unreal.RigVMUserWorkflowOptions.workflow"></a>

#### workflow

```python
@property
def workflow() -> RigVMUserWorkflow
```

(RigVMUserWorkflow):  [Read-Only]

<a id="unreal.RigVMUserWorkflowOptions.requires_dialog"></a>

#### requires_dialog

```python
def requires_dialog() -> bool
```

x.requires_dialog() -> bool
Requires Dialog

Returns:
    bool:

<a id="unreal.RigVMUserWorkflowOptions.report_warning"></a>

#### report_warning

```python
def report_warning(message: str) -> None
```

x.report_warning(message) -> None
Report Warning

Args:
    message (str):

<a id="unreal.RigVMUserWorkflowOptions.report_info"></a>

#### report_info

```python
def report_info(message: str) -> None
```

x.report_info(message) -> None
Report Info

Args:
    message (str):

<a id="unreal.RigVMUserWorkflowOptions.report_error"></a>

#### report_error

```python
def report_error(message: str) -> None
```

x.report_error(message) -> None
Report Error

Args:
    message (str):

<a id="unreal.RigVMUserWorkflowOptions.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Is Valid

Returns:
    bool:

<a id="unreal.RigVMHost"></a>