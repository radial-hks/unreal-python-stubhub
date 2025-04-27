## CurveTableRowHandle Objects

```python
class CurveTableRowHandle(StructBase)
```

Handle to a particular row in a table.

**C++ Source:**

- **Module**: Engine
- **File**: CurveTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_table`` (CurveTable):  [Read-Write] Pointer to table we want a row from
- ``row_name`` (Name):  [Read-Write] Name of row in the table that we want

<a id="unreal.CurveTableRowHandle.__init__"></a>

#### __init__

```python
def __init__(curve_table: CurveTable = None, row_name: Name = "None") -> None
```

<a id="unreal.CurveTableRowHandle.curve_table"></a>

#### curve_table

```python
@property
def curve_table() -> CurveTable
```

(CurveTable):  [Read-Write] Pointer to table we want a row from

<a id="unreal.CurveTableRowHandle.curve_table"></a>

#### curve_table

```python
@curve_table.setter
def curve_table(value: CurveTable) -> None
```

<a id="unreal.CurveTableRowHandle.row_name"></a>

#### row_name

```python
@property
def row_name() -> Name
```

(Name):  [Read-Write] Name of row in the table that we want

<a id="unreal.CurveTableRowHandle.row_name"></a>

#### row_name

```python
@row_name.setter
def row_name(value: Name) -> None
```

<a id="unreal.DataDrivenConsoleVariable"></a>