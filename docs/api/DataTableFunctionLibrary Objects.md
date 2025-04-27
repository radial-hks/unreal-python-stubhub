## DataTableFunctionLibrary Objects

```python
class DataTableFunctionLibrary(BlueprintFunctionLibrary)
```

Data Table Function Library

**C++ Source:**

- **Module**: Engine
- **File**: DataTableFunctionLibrary.h

<a id="unreal.DataTableFunctionLibrary.remove_data_table_row"></a>

#### remove_data_table_row

```python
@classmethod
def remove_data_table_row(cls, data_table: DataTable, row_name: Name) -> None
```

X.remove_data_table_row(data_table, row_name) -> None
Removes the row with the provided name from a Data Table.

Args:
    data_table (DataTable): 
    row_name (Name):

<a id="unreal.DataTableFunctionLibrary.get_data_table_row_struct"></a>

#### get_data_table_row_struct

```python
@classmethod
def get_data_table_row_struct(cls, table: DataTable) -> ScriptStruct
```

X.get_data_table_row_struct(table) -> ScriptStruct
Get the row struct used by the given Data Table, if any

Args:
    table (DataTable): 

Returns:
    ScriptStruct:

<a id="unreal.DataTableFunctionLibrary.get_data_table_row_names"></a>

#### get_data_table_row_names

```python
@classmethod
def get_data_table_row_names(cls, table: DataTable) -> Array[Name]
```

X.get_data_table_row_names(table) -> Array[Name]
Get Data Table Row Names

Args:
    table (DataTable): 

Returns:
    Array[Name]: 

    out_row_names (Array[Name]):

<a id="unreal.DataTableFunctionLibrary.get_data_table_column_names"></a>

#### get_data_table_column_names

```python
@classmethod
def get_data_table_column_names(cls, table: DataTable) -> Array[Name]
```

X.get_data_table_column_names(table) -> Array[Name]
Get the name of each column in this Data Table.
note: These are always the raw property names (
see: GetDataTableColumnAsString) rather than the friendly export name that would be used in a CSV/JSON export (
see: GetDataTableColumnNameFromExportName).

Args:
    table (DataTable): 

Returns:
    Array[Name]: 

    out_column_names (Array[Name]):

<a id="unreal.DataTableFunctionLibrary.get_data_table_column_name_from_export_name"></a>

#### get_data_table_column_name_from_export_name

```python
@classmethod
def get_data_table_column_name_from_export_name(
        cls, table: DataTable, column_export_name: str) -> Optional[Name]
```

X.get_data_table_column_name_from_export_name(table, column_export_name) -> Name or None
Get the raw property name of a data table column from its friendly export name.

Args:
    table (DataTable): 
    column_export_name (str): 

Returns:
    Name or None: True if a column was found for the friendly name, false otherwise.

    out_column_name (Name):

<a id="unreal.DataTableFunctionLibrary.get_data_table_column_export_names"></a>

#### get_data_table_column_export_names

```python
@classmethod
def get_data_table_column_export_names(cls, table: DataTable) -> Array[str]
```

X.get_data_table_column_export_names(table) -> Array[str]
Get the friendly export name of each column in this Data Table.
see: GetDataTableColumnNameFromExportName.

Args:
    table (DataTable): 

Returns:
    Array[str]: 

    out_export_column_names (Array[str]):

<a id="unreal.DataTableFunctionLibrary.get_data_table_column_as_string"></a>

#### get_data_table_column_as_string

```python
@classmethod
def get_data_table_column_as_string(cls, data_table: DataTable,
                                    property_name: Name) -> Array[str]
```

X.get_data_table_column_as_string(data_table, property_name) -> Array[str]
Export from the DataTable all the row for one column. Export it as string. The row name is not included.
see: GetDataTableColumnNames.
see: GetDataTableColumnNameFromExportName.

Args:
    data_table (DataTable): 
    property_name (Name): 

Returns:
    Array[str]:

<a id="unreal.DataTableFunctionLibrary.fill_data_table_from_json_string"></a>

#### fill_data_table_from_json_string

```python
@classmethod
def fill_data_table_from_json_string(
        cls,
        data_table: DataTable,
        json_string: str,
        import_row_struct: ScriptStruct = None) -> bool
```

X.fill_data_table_from_json_string(data_table, json_string, import_row_struct=None) -> bool
Empty and fill a Data Table from JSON string.

Args:
    data_table (DataTable): 
    json_string (str): The Data that representing the contents of a JSON file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTableFunctionLibrary.fill_data_table_from_json_file"></a>

#### fill_data_table_from_json_file

```python
@classmethod
def fill_data_table_from_json_file(
        cls,
        data_table: DataTable,
        json_file_path: str,
        import_row_struct: ScriptStruct = None) -> bool
```

X.fill_data_table_from_json_file(data_table, json_file_path, import_row_struct=None) -> bool
Empty and fill a Data Table from JSON file.

Args:
    data_table (DataTable): 
    json_file_path (str): The file path of the JSON file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTableFunctionLibrary.fill_data_table_from_csv_string"></a>

#### fill_data_table_from_csv_string

```python
@classmethod
def fill_data_table_from_csv_string(
        cls,
        data_table: DataTable,
        csv_string: str,
        import_row_struct: ScriptStruct = None) -> bool
```

X.fill_data_table_from_csv_string(data_table, csv_string, import_row_struct=None) -> bool
Empty and fill a Data Table from CSV string.

Args:
    data_table (DataTable): 
    csv_string (str): The Data that representing the contents of a CSV file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTableFunctionLibrary.fill_data_table_from_csv_file"></a>

#### fill_data_table_from_csv_file

```python
@classmethod
def fill_data_table_from_csv_file(
        cls,
        data_table: DataTable,
        csv_file_path: str,
        import_row_struct: ScriptStruct = None) -> bool
```

X.fill_data_table_from_csv_file(data_table, csv_file_path, import_row_struct=None) -> bool
Empty and fill a Data Table from CSV file.

Args:
    data_table (DataTable): 
    csv_file_path (str): The file path of the CSV file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTableFunctionLibrary.export_data_table_to_json_string"></a>

#### export_data_table_to_json_string

```python
@classmethod
def export_data_table_to_json_string(cls,
                                     data_table: DataTable) -> Optional[str]
```

X.export_data_table_to_json_string(data_table) -> str or None
Export a Data Table to JSON string.

Args:
    data_table (DataTable): 

Returns:
    str or None: True if the operation succeeds, check the log for errors if it didn't succeed.

    out_json_string (str): Output representing the contents of a JSON file.

<a id="unreal.DataTableFunctionLibrary.export_data_table_to_json_file"></a>

#### export_data_table_to_json_file

```python
@classmethod
def export_data_table_to_json_file(cls, data_table: DataTable,
                                   json_file_path: str) -> bool
```

X.export_data_table_to_json_file(data_table, json_file_path) -> bool
Export a Data Table to JSON file.

Args:
    data_table (DataTable): 
    json_file_path (str): The file path of the JSON file to write (output file is UTF-8).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTableFunctionLibrary.export_data_table_to_csv_string"></a>

#### export_data_table_to_csv_string

```python
@classmethod
def export_data_table_to_csv_string(cls,
                                    data_table: DataTable) -> Optional[str]
```

X.export_data_table_to_csv_string(data_table) -> str or None
Export a Data Table to CSV string.

Args:
    data_table (DataTable): 

Returns:
    str or None: True if the operation succeeds, check the log for errors if it didn't succeed.

    out_csv_string (str): Output representing the contents of a CSV file.

<a id="unreal.DataTableFunctionLibrary.export_data_table_to_csv_file"></a>

#### export_data_table_to_csv_file

```python
@classmethod
def export_data_table_to_csv_file(cls, data_table: DataTable,
                                  csv_file_path: str) -> bool
```

X.export_data_table_to_csv_file(data_table, csv_file_path) -> bool
Export a Data Table to CSV file.

Args:
    data_table (DataTable): 
    csv_file_path (str): The file path of the CSV file to write (output file is UTF-8).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTableFunctionLibrary.evaluate_curve_table_row"></a>

#### evaluate_curve_table_row

```python
@classmethod
def evaluate_curve_table_row(
        cls, curve_table: CurveTable, row_name: Name, xy: float,
        context_string: str) -> Tuple[EvaluateCurveTableResult, float]
```

X.evaluate_curve_table_row(curve_table, row_name, xy, context_string) -> (out_result=EvaluateCurveTableResult, out_xy=float)
Evaluate Curve Table Row

Args:
    curve_table (CurveTable): 
    row_name (Name): 
    xy (float): 
    context_string (str): 

Returns:
    tuple: 

    out_result (EvaluateCurveTableResult): 

    out_xy (float):

<a id="unreal.DataTableFunctionLibrary.does_data_table_row_exist"></a>

#### does_data_table_row_exist

```python
@classmethod
def does_data_table_row_exist(cls, table: DataTable, row_name: Name) -> bool
```

X.does_data_table_row_exist(table, row_name) -> bool
Returns whether or not Table contains a row named RowName

Args:
    table (DataTable): 
    row_name (Name): 

Returns:
    bool:

<a id="unreal.DebugCameraController"></a>