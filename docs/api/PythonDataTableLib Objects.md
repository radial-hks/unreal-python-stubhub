## PythonDataTableLib Objects

```python
class PythonDataTableLib(BlueprintFunctionLibrary)
```

Python Data Table Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonDataTableLib.h

<a id="unreal.PythonDataTableLib.set_property_by_string_at"></a>

#### set\_property\_by\_string\_at

```python
@classmethod
def set_property_by_string_at(cls, data_table: DataTable, row_index: int,
                              column_index: int, value_as_string: str) -> bool
```

X.set_property_by_string_at(data_table, row_index, column_index, value_as_string) -> bool
Set the specified cell's property in datatable

Args:
    data_table (DataTable): The DataTable you want to query.
    row_index (int32): The Row index of the cell. The title is not include
    column_index (int32): The Column index of the cell. The title is not include
    value_as_string (str): The new property in string format.

Returns:
    bool: True if the new property has been set

<a id="unreal.PythonDataTableLib.set_property_by_string"></a>

#### set\_property\_by\_string

```python
@classmethod
def set_property_by_string(cls, data_table: DataTable, row_name: Name,
                           column_name: Name, value_as_string: str) -> bool
```

X.set_property_by_string(data_table, row_name, column_name, value_as_string) -> bool
Set the specified cell's property in datatable

Args:
    data_table (DataTable): The DataTable you want to query.
    row_name (Name): The Row name of the cell.
    column_name (Name): The Column name of the cell.
    value_as_string (str): The new property in string format.

Returns:
    bool: True if the new property has been set

<a id="unreal.PythonDataTableLib.reset_row"></a>

#### reset\_row

```python
@classmethod
def reset_row(cls, data_table: DataTable, row_name: Name) -> bool
```

X.reset_row(data_table, row_name) -> bool
Reset the specified row in the given datatable to default values.

Args:
    data_table (DataTable): The DataTable you want to modify.
    row_name (Name): The Row Name

Returns:
    bool: True if the row has been reset

<a id="unreal.PythonDataTableLib.rename_row"></a>

#### rename\_row

```python
@classmethod
def rename_row(cls, data_table: DataTable, old_name: Name,
               new_name: Name) -> bool
```

X.rename_row(data_table, old_name, new_name) -> bool
Rename the specified row in the given datatable

Args:
    data_table (DataTable): The DataTable you want to modify.
    old_name (Name): The old Row Name
    new_name (Name): The new Row Name

Returns:
    bool: True if the row has been renamed

<a id="unreal.PythonDataTableLib.remove_row"></a>

#### remove\_row

```python
@classmethod
def remove_row(cls, data_table: DataTable, row_name: Name) -> bool
```

X.remove_row(data_table, row_name) -> bool
Remove the specified row of the given datatable

Args:
    data_table (DataTable): The DataTable you want to modify.
    row_name (Name): The Row Name

Returns:
    bool: True if the row has been removed

<a id="unreal.PythonDataTableLib.move_row"></a>

#### move\_row

```python
@classmethod
def move_row(cls,
             data_table: DataTable,
             row_name: Name,
             up: bool,
             num_rows_to_move_by: int = 1) -> bool
```

X.move_row(data_table, row_name, up, num_rows_to_move_by=1) -> bool
Reset the specified row in the given datatable to default values.

Args:
    data_table (DataTable): The DataTable you want to modify.
    row_name (Name): The Row Name of the 'source row'
    up (bool): Move up or not
    num_rows_to_move_by (int32): Number of rows to move by.

Returns:
    bool: True if the row has been moved

<a id="unreal.PythonDataTableLib.get_table_as_json"></a>

#### get\_table\_as\_json

```python
@classmethod
def get_table_as_json(cls, data_table: DataTable) -> str
```

X.get_table_as_json(data_table) -> str
Get the datatable content as JSON

Args:
    data_table (DataTable): The DataTable you want to query.

Returns:
    str: The datatable content as JSON

<a id="unreal.PythonDataTableLib.get_shape"></a>

#### get\_shape

```python
@classmethod
def get_shape(cls, data_table: DataTable) -> Array[int]
```

X.get_shape(data_table) -> Array[int32]
Get the Shape of the given datatable. The title and the row names are not included.

Args:
    data_table (DataTable): The DataTable you want to query.

Returns:
    Array[int32]: return the row number and column number of the datatable: [RowNumber, ColumnNumber]

<a id="unreal.PythonDataTableLib.get_row_names"></a>

#### get\_row\_names

```python
@classmethod
def get_row_names(cls, data_table: DataTable) -> Array[Name]
```

X.get_row_names(data_table) -> Array[Name]
Get the Row names of the given datatable.

Args:
    data_table (DataTable): The DataTable you want to query.

Returns:
    Array[Name]: The row names list.

<a id="unreal.PythonDataTableLib.get_row_name"></a>

#### get\_row\_name

```python
@classmethod
def get_row_name(cls, data_table: DataTable, row_id: int) -> Name
```

X.get_row_name(data_table, row_id) -> Name
Gets the Row name of the specified row in datatable

Args:
    data_table (DataTable): The DataTable you want to modify.
    row_id (int32): The index of the row

Returns:
    Name: The Row name

<a id="unreal.PythonDataTableLib.get_property_as_string_at"></a>

#### get\_property\_as\_string\_at

```python
@classmethod
def get_property_as_string_at(cls, data_table: DataTable, row_id: int,
                              column_id: int) -> str
```

X.get_property_as_string_at(data_table, row_id, column_id) -> str
Get the specified cell's value as string in datatable

Args:
    data_table (DataTable): The DataTable you want to query.
    row_id (int32): The Row index of the cell. The title is not include
    column_id (int32): The Column index of the cell. The title is not include

Returns:
    str: The property of the cell as string.

<a id="unreal.PythonDataTableLib.get_property_as_string"></a>

#### get\_property\_as\_string

```python
@classmethod
def get_property_as_string(cls, data_table: DataTable, row_name: Name,
                           column_name: Name) -> str
```

X.get_property_as_string(data_table, row_name, column_name) -> str
Get the specified cell's value as string in datatable

Args:
    data_table (DataTable): The DataTable you want to query.
    row_name (Name): The Row name of the cell.
    column_name (Name): The Column name of the cell.

Returns:
    str: The property of the cell as string.

<a id="unreal.PythonDataTableLib.get_flatten_data_table"></a>

#### get\_flatten\_data\_table

```python
@classmethod
def get_flatten_data_table(cls,
                           data_table: DataTable,
                           include_header: bool = False) -> Array[str]
```

X.get_flatten_data_table(data_table, include_header=False) -> Array[str]
Get the content of datatable as a 1D string List.
note: The length of return value will equal RowNumber * ColumnNumber, when bIncludeHeader set to false

Args:
    data_table (DataTable): The DataTable you want to modify
    include_header (bool): Whether include the title and row name column.

Returns:
    Array[str]: The content in 1D string List

<a id="unreal.PythonDataTableLib.get_data_table_struct_path"></a>

#### get\_data\_table\_struct\_path

```python
@classmethod
def get_data_table_struct_path(cls, data_table: DataTable) -> str
```

X.get_data_table_struct_path(data_table) -> str
Get the row struct's path of the given  DataTable.

Args:
    data_table (DataTable): The DataTable for query.

Returns:
    str: The package path of struct, empty string if failed.

<a id="unreal.PythonDataTableLib.get_data_table_struct"></a>

#### get\_data\_table\_struct

```python
@classmethod
def get_data_table_struct(cls, data_table: DataTable) -> ScriptStruct
```

X.get_data_table_struct(data_table) -> ScriptStruct
Get the row struct of the given DataTable.

Args:
    data_table (DataTable): The DataTable for query.

Returns:
    ScriptStruct: The row struct of the datatable.

<a id="unreal.PythonDataTableLib.get_column_names"></a>

#### get\_column\_names

```python
@classmethod
def get_column_names(cls,
                     data_table: DataTable,
                     friendly_name: bool = True,
                     include_name: bool = False) -> Array[Name]
```

X.get_column_names(data_table, friendly_name=True, include_name=False) -> Array[Name]
Get the Column names of the given datatable.

Args:
    data_table (DataTable): The DataTable you want to query.
    friendly_name (bool): Get the Friendly Name or Raw Name.
    include_name (bool): Include the Row Name Column or not.

Returns:
    Array[Name]: The Column names list.

<a id="unreal.PythonDataTableLib.get_column_name"></a>

#### get\_column\_name

```python
@classmethod
def get_column_name(cls,
                    data_table: DataTable,
                    column_id: int,
                    friendly_name: bool = True) -> Name
```

X.get_column_name(data_table, column_id, friendly_name=True) -> Name
Gets the Column name of the specified column in datatable

Args:
    data_table (DataTable): The DataTable you want to modify
    column_id (int32): The index of the column
    friendly_name (bool): Whether get the friendly name or raw name or not

Returns:
    Name: The Row name

<a id="unreal.PythonDataTableLib.duplicate_row"></a>

#### duplicate\_row

```python
@classmethod
def duplicate_row(cls, data_table: DataTable, source_row_name: Name,
                  row_name: Name) -> bool
```

X.duplicate_row(data_table, source_row_name, row_name) -> bool
Duplicate a row in the given datatable

Args:
    data_table (DataTable): The DataTable you want to modify.
    source_row_name (Name): The Row Name of the source Row
    row_name (Name): The Row Name of new line

Returns:
    bool: True if the row has been duplicated

<a id="unreal.PythonDataTableLib.add_row"></a>

#### add\_row

```python
@classmethod
def add_row(cls, data_table: DataTable, row_name: Name) -> bool
```

X.add_row(data_table, row_name) -> bool
Add a row in the given datatable

Args:
    data_table (DataTable): The DataTable you want to modify.
    row_name (Name): The Row Name of new line

Returns:
    bool: True if the row has been added

<a id="unreal.PythonEnumLib"></a>