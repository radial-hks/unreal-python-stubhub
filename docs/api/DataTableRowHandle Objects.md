## DataTableRowHandle Objects

```python
class DataTableRowHandle(StructBase)
```

Handle to a particular row in a table

**C++ Source:**

- **Module**: Engine
- **File**: DataTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_table`` (DataTable):  [Read-Write] Pointer to table we want a row from
- ``row_name`` (Name):  [Read-Write] Name of row in the table that we want

<a id="unreal.DataTableRowHandle.__init__"></a>

#### __init__

```python
def __init__(data_table: DataTable = None, row_name: Name = "None") -> None
```

<a id="unreal.DataTableRowHandle.data_table"></a>

#### data_table

```python
@property
def data_table() -> DataTable
```

(DataTable):  [Read-Write] Pointer to table we want a row from

<a id="unreal.DataTableRowHandle.data_table"></a>

#### data_table

```python
@data_table.setter
def data_table(value: DataTable) -> None
```

<a id="unreal.DataTableRowHandle.row_name"></a>

#### row_name

```python
@property
def row_name() -> Name
```

(Name):  [Read-Write] Name of row in the table that we want

<a id="unreal.DataTableRowHandle.row_name"></a>

#### row_name

```python
@row_name.setter
def row_name(value: Name) -> None
```

<a id="unreal.DataTableCategoryHandle"></a>