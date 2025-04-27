## ToolMenuInsert Objects

```python
class ToolMenuInsert(StructBase)
```

Tool Menu Insert

**C++ Source:**

- **Module**: ToolMenus
- **File**: ToolMenuMisc.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] Where to insert
- ``position`` (ToolMenuInsertType):  [Read-Write] How to insert

<a id="unreal.ToolMenuInsert.__init__"></a>

#### __init__

```python
def __init__(
        name: Name = "None",
        position: ToolMenuInsertType = ToolMenuInsertType.DEFAULT) -> None
```

<a id="unreal.ToolMenuInsert.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Where to insert

<a id="unreal.ToolMenuInsert.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.ToolMenuInsert.position"></a>

#### position

```python
@property
def position() -> ToolMenuInsertType
```

(ToolMenuInsertType):  [Read-Write] How to insert

<a id="unreal.ToolMenuInsert.position"></a>

#### position

```python
@position.setter
def position(value: ToolMenuInsertType) -> None
```

<a id="unreal.ToolMenuOwner"></a>