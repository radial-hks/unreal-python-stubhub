## StringTableLibrary Objects

```python
class StringTableLibrary(BlueprintFunctionLibrary)
```

Kismet String Table Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetStringTableLibrary.h

<a id="unreal.StringTableLibrary.is_registered_table_id"></a>

#### is_registered_table_id

```python
@classmethod
def is_registered_table_id(cls, table_id: Name) -> bool
```

X.is_registered_table_id(table_id) -> bool
Returns true if the given table ID corresponds to a registered string table.

Args:
    table_id (Name): 

Returns:
    bool:

<a id="unreal.StringTableLibrary.is_registered_table_entry"></a>

#### is_registered_table_entry

```python
@classmethod
def is_registered_table_entry(cls, table_id: Name, key: str) -> bool
```

X.is_registered_table_entry(table_id, key) -> bool
Returns true if the given table ID corresponds to a registered string table, and that table has.

Args:
    table_id (Name): 
    key (str): 

Returns:
    bool:

<a id="unreal.StringTableLibrary.get_table_namespace"></a>

#### get_table_namespace

```python
@classmethod
def get_table_namespace(cls, table_id: Name) -> str
```

X.get_table_namespace(table_id) -> str
Returns the namespace of the given string table.

Args:
    table_id (Name): 

Returns:
    str:

<a id="unreal.StringTableLibrary.get_table_entry_source_string"></a>

#### get_table_entry_source_string

```python
@classmethod
def get_table_entry_source_string(cls, table_id: Name, key: str) -> str
```

X.get_table_entry_source_string(table_id, key) -> str
Returns the source string of the given string table entry (or an empty string).

Args:
    table_id (Name): 
    key (str): 

Returns:
    str:

<a id="unreal.StringTableLibrary.get_table_entry_meta_data"></a>

#### get_table_entry_meta_data

```python
@classmethod
def get_table_entry_meta_data(cls, table_id: Name, key: str,
                              meta_data_id: Name) -> str
```

X.get_table_entry_meta_data(table_id, key, meta_data_id) -> str
Returns the specified meta-data of the given string table entry (or an empty string).

Args:
    table_id (Name): 
    key (str): 
    meta_data_id (Name): 

Returns:
    str:

<a id="unreal.StringTableLibrary.get_registered_string_tables"></a>

#### get_registered_string_tables

```python
@classmethod
def get_registered_string_tables(cls) -> Array[Name]
```

X.get_registered_string_tables() -> Array[Name]
Returns an array of all registered string table IDs

Returns:
    Array[Name]:

<a id="unreal.StringTableLibrary.get_meta_data_ids_from_string_table_entry"></a>

#### get_meta_data_ids_from_string_table_entry

```python
@classmethod
def get_meta_data_ids_from_string_table_entry(cls, table_id: Name,
                                              key: str) -> Array[Name]
```

X.get_meta_data_ids_from_string_table_entry(table_id, key) -> Array[Name]
Returns an array of all meta-data IDs within the given string table entry

Args:
    table_id (Name): 
    key (str): 

Returns:
    Array[Name]:

<a id="unreal.StringTableLibrary.get_keys_from_string_table"></a>

#### get_keys_from_string_table

```python
@classmethod
def get_keys_from_string_table(cls, table_id: Name) -> Array[str]
```

X.get_keys_from_string_table(table_id) -> Array[str]
Returns an array of all keys within the given string table

Args:
    table_id (Name): 

Returns:
    Array[str]:

<a id="unreal.Field"></a>