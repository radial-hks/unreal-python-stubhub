## DataTableCategoryHandle Objects

```python
class DataTableCategoryHandle(StructBase)
```

Handle to a particular set of rows in a table

**C++ Source:**

- **Module**: Engine
- **File**: DataTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``column_name`` (Name):  [Read-Write] Name of column in the table that we want
- ``data_table`` (DataTable):  [Read-Write] Pointer to table we want a row from
- ``row_contents`` (Name):  [Read-Write] Contents of rows in the table that we want

<a id="unreal.DataTableCategoryHandle.__init__"></a>

#### __init__

```python
def __init__(data_table: DataTable = None,
             column_name: Name = "None",
             row_contents: Name = "None") -> None
```

<a id="unreal.DataTableCategoryHandle.data_table"></a>

#### data_table

```python
@property
def data_table() -> DataTable
```

(DataTable):  [Read-Write] Pointer to table we want a row from

<a id="unreal.DataTableCategoryHandle.data_table"></a>

#### data_table

```python
@data_table.setter
def data_table(value: DataTable) -> None
```

<a id="unreal.DataTableCategoryHandle.column_name"></a>

#### column_name

```python
@property
def column_name() -> Name
```

(Name):  [Read-Write] Name of column in the table that we want

<a id="unreal.DataTableCategoryHandle.column_name"></a>

#### column_name

```python
@column_name.setter
def column_name(value: Name) -> None
```

<a id="unreal.DataTableCategoryHandle.row_contents"></a>

#### row_contents

```python
@property
def row_contents() -> Name
```

(Name):  [Read-Write] Contents of rows in the table that we want

<a id="unreal.DataTableCategoryHandle.row_contents"></a>

#### row_contents

```python
@row_contents.setter
def row_contents(value: Name) -> None
```

<a id="unreal.DialogueContext"></a>