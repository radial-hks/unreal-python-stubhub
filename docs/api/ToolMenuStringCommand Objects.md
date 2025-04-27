## ToolMenuStringCommand Objects

```python
class ToolMenuStringCommand(StructBase)
```

Tool Menu String Command

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuMisc.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_type`` (Name):  [Read-Write] Which command handler to use when type is custom
- ``string`` (str):  [Read-Write] String to pass to command handler
- ``type`` (ToolMenuStringCommandType):  [Read-Write] Which command handler to use

<a id="unreal.ToolMenuStringCommand.__init__"></a>

#### __init__

```python
def __init__(
        type: ToolMenuStringCommandType = ToolMenuStringCommandType.COMMAND,
        custom_type: Name = "None",
        string: str = "") -> None
```

<a id="unreal.ToolMenuStringCommand.type"></a>

#### type

```python
@property
def type() -> ToolMenuStringCommandType
```

(ToolMenuStringCommandType):  [Read-Write] Which command handler to use

<a id="unreal.ToolMenuStringCommand.type"></a>

#### type

```python
@type.setter
def type(value: ToolMenuStringCommandType) -> None
```

<a id="unreal.ToolMenuStringCommand.custom_type"></a>

#### custom_type

```python
@property
def custom_type() -> Name
```

(Name):  [Read-Write] Which command handler to use when type is custom

<a id="unreal.ToolMenuStringCommand.custom_type"></a>

#### custom_type

```python
@custom_type.setter
def custom_type(value: Name) -> None
```

<a id="unreal.ToolMenuStringCommand.string"></a>

#### string

```python
@property
def string() -> str
```

(str):  [Read-Write] String to pass to command handler

<a id="unreal.ToolMenuStringCommand.string"></a>

#### string

```python
@string.setter
def string(value: str) -> None
```

<a id="unreal.ToolMenuInsert"></a>