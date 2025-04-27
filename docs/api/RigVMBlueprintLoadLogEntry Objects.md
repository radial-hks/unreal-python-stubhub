## RigVMBlueprintLoadLogEntry Objects

```python
class RigVMBlueprintLoadLogEntry(StructBase)
```

Rig VMBlueprint Load Log Entry

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMEditor
- **File**: RigVMEditorBlueprintLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Only]
- ``severity`` (RigVMBlueprintLoadLogSeverity):  [Read-Only]
- ``subject`` (Object):  [Read-Only]

<a id="unreal.RigVMBlueprintLoadLogEntry.__init__"></a>

#### __init__

```python
def __init__(
        severity: RigVMBlueprintLoadLogSeverity = RigVMBlueprintLoadLogSeverity
    .DISPLAY,
        subject: Object = None,
        message: str = "") -> None
```

<a id="unreal.RigVMBlueprintLoadLogEntry.severity"></a>

#### severity

```python
@property
def severity() -> RigVMBlueprintLoadLogSeverity
```

(RigVMBlueprintLoadLogSeverity):  [Read-Only]

<a id="unreal.RigVMBlueprintLoadLogEntry.subject"></a>

#### subject

```python
@property
def subject() -> Object
```

(Object):  [Read-Only]

<a id="unreal.RigVMBlueprintLoadLogEntry.message"></a>

#### message

```python
@property
def message() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMEditorGraphMenuContext"></a>