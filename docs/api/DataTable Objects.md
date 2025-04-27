## DataTable Objects

```python
class DataTable(Object)
```

Imported spreadsheet table.

**C++ Source:**

- **Module**: Engine
- **File**: DataTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] The file this data table was imported from, may be empty
- ``ignore_extra_fields`` (bool):  [Read-Write] Set to true to ignore extra fields in the import data, if false it will warn about them
- ``ignore_missing_fields`` (bool):  [Read-Write] Set to true to ignore any fields that are expected but missing, if false it will warn about them
- ``import_key_field`` (str):  [Read-Write] Explicit field in import data to use as key. If this is empty it uses Name for JSON and the first field found for CSV
- ``preserve_existing_values`` (bool):  [Read-Write] Set to true to preserve existing values for any fields that are expected but missing in the CSV file. If false, missing fields will be populated with default values.
- ``row_struct`` (ScriptStruct):  [Read-Only] Structure to use for each row of the table, must inherit from FTableRowBase
- ``strip_from_client_builds`` (bool):  [Read-Write] Set to true to not cook this data table into client builds. Useful for sensitive tables that only servers should know about.

<a id="unreal.DataTable.get_row_struct"></a>

#### get_row_struct

```python
def get_row_struct() -> ScriptStruct
```

x.get_row_struct() -> ScriptStruct
Get the row struct used by the given Data Table, if any

Returns:
    ScriptStruct:

<a id="unreal.DataTable.get_row_names"></a>

#### get_row_names

```python
def get_row_names() -> Array[Name]
```

x.get_row_names() -> Array[Name]
Get Data Table Row Names

Returns:
    Array[Name]: 

    out_row_names (Array[Name]):

<a id="unreal.DataTable.get_column_names"></a>

#### get_column_names

```python
def get_column_names() -> Array[Name]
```

x.get_column_names() -> Array[Name]
Get the name of each column in this Data Table.
note: These are always the raw property names (
see: GetDataTableColumnAsString) rather than the friendly export name that would be used in a CSV/JSON export (
see: GetDataTableColumnNameFromExportName).

Returns:
    Array[Name]: 

    out_column_names (Array[Name]):

<a id="unreal.DataTable.get_column_name_from_export_name"></a>

#### get_column_name_from_export_name

```python
def get_column_name_from_export_name(
        column_export_name: str) -> Optional[Name]
```

x.get_column_name_from_export_name(column_export_name) -> Name or None
Get the raw property name of a data table column from its friendly export name.

Args:
    column_export_name (str): 

Returns:
    Name or None: True if a column was found for the friendly name, false otherwise.

    out_column_name (Name):

<a id="unreal.DataTable.get_column_export_names"></a>

#### get_column_export_names

```python
def get_column_export_names() -> Array[str]
```

x.get_column_export_names() -> Array[str]
Get the friendly export name of each column in this Data Table.
see: GetDataTableColumnNameFromExportName.

Returns:
    Array[str]: 

    out_export_column_names (Array[str]):

<a id="unreal.DataTable.get_column_as_string"></a>

#### get_column_as_string

```python
def get_column_as_string(property_name: Name) -> Array[str]
```

x.get_column_as_string(property_name) -> Array[str]
Export from the DataTable all the row for one column. Export it as string. The row name is not included.
see: GetDataTableColumnNames.
see: GetDataTableColumnNameFromExportName.

Args:
    property_name (Name): 

Returns:
    Array[str]:

<a id="unreal.DataTable.fill_from_json_string"></a>

#### fill_from_json_string

```python
def fill_from_json_string(json_string: str,
                          import_row_struct: ScriptStruct = None) -> bool
```

x.fill_from_json_string(json_string, import_row_struct=None) -> bool
Empty and fill a Data Table from JSON string.

Args:
    json_string (str): The Data that representing the contents of a JSON file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTable.fill_from_json_file"></a>

#### fill_from_json_file

```python
def fill_from_json_file(json_file_path: str,
                        import_row_struct: ScriptStruct = None) -> bool
```

x.fill_from_json_file(json_file_path, import_row_struct=None) -> bool
Empty and fill a Data Table from JSON file.

Args:
    json_file_path (str): The file path of the JSON file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTable.fill_from_csv_string"></a>

#### fill_from_csv_string

```python
def fill_from_csv_string(csv_string: str,
                         import_row_struct: ScriptStruct = None) -> bool
```

x.fill_from_csv_string(csv_string, import_row_struct=None) -> bool
Empty and fill a Data Table from CSV string.

Args:
    csv_string (str): The Data that representing the contents of a CSV file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTable.fill_from_csv_file"></a>

#### fill_from_csv_file

```python
def fill_from_csv_file(csv_file_path: str,
                       import_row_struct: ScriptStruct = None) -> bool
```

x.fill_from_csv_file(csv_file_path, import_row_struct=None) -> bool
Empty and fill a Data Table from CSV file.

Args:
    csv_file_path (str): The file path of the CSV file.
    import_row_struct (ScriptStruct): Optional row struct to apply on import. If set will also force the import to run automated (no questions or dialogs).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTable.export_to_json_string"></a>

#### export_to_json_string

```python
def export_to_json_string() -> Optional[str]
```

x.export_to_json_string() -> str or None
Export a Data Table to JSON string.

Returns:
    str or None: True if the operation succeeds, check the log for errors if it didn't succeed.

    out_json_string (str): Output representing the contents of a JSON file.

<a id="unreal.DataTable.export_to_json_file"></a>

#### export_to_json_file

```python
def export_to_json_file(json_file_path: str) -> bool
```

x.export_to_json_file(json_file_path) -> bool
Export a Data Table to JSON file.

Args:
    json_file_path (str): The file path of the JSON file to write (output file is UTF-8).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTable.export_to_csv_string"></a>

#### export_to_csv_string

```python
def export_to_csv_string() -> Optional[str]
```

x.export_to_csv_string() -> str or None
Export a Data Table to CSV string.

Returns:
    str or None: True if the operation succeeds, check the log for errors if it didn't succeed.

    out_csv_string (str): Output representing the contents of a CSV file.

<a id="unreal.DataTable.export_to_csv_file"></a>

#### export_to_csv_file

```python
def export_to_csv_file(csv_file_path: str) -> bool
```

x.export_to_csv_file(csv_file_path) -> bool
Export a Data Table to CSV file.

Args:
    csv_file_path (str): The file path of the CSV file to write (output file is UTF-8).

Returns:
    bool: True if the operation succeeds, check the log for errors if it didn't succeed.

<a id="unreal.DataTable.does_row_exist"></a>

#### does_row_exist

```python
def does_row_exist(row_name: Name) -> bool
```

x.does_row_exist(row_name) -> bool
Returns whether or not Table contains a row named RowName

Args:
    row_name (Name): 

Returns:
    bool:

<a id="unreal.MirrorDataTable"></a>