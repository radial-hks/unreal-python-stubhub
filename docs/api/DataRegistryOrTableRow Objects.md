## DataRegistryOrTableRow Objects

```python
class DataRegistryOrTableRow(StructBase)
```

Defines a DataRegistryId or DataTableRowHandle with a common interface to both

**C++ Source:**

- **Plugin**: DataRegistry
- **Module**: DataRegistry
- **File**: SoftDataRegistryOrTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_registry_id`` (DataRegistryId):  [Read-Write]
- ``data_table_row`` (DataTableRowHandle):  [Read-Write]
- ``use_data_registry_id`` (bool):  [Read-Write]

<a id="unreal.DataRegistryOrTableRow.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data_table_row: DataTableRowHandle = [None, "None"],
             data_registry_id: DataRegistryId = [["None"], "None"]) -> None
```

<a id="unreal.DataRegistryOrTableRow.data_table_row"></a>

#### data\_table\_row

```python
@property
def data_table_row() -> DataTableRowHandle
```

(DataTableRowHandle):  [Read-Write]

<a id="unreal.DataRegistryOrTableRow.data_table_row"></a>

#### data\_table\_row

```python
@data_table_row.setter
def data_table_row(value: DataTableRowHandle) -> None
```

<a id="unreal.DataRegistryOrTableRow.data_registry_id"></a>

#### data\_registry\_id

```python
@property
def data_registry_id() -> DataRegistryId
```

(DataRegistryId):  [Read-Write]

<a id="unreal.DataRegistryOrTableRow.data_registry_id"></a>

#### data\_registry\_id

```python
@data_registry_id.setter
def data_registry_id(value: DataRegistryId) -> None
```

<a id="unreal.ActorInitStateChangedParams"></a>