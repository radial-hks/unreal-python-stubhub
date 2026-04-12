## CesiumPropertyTableStatus Objects

```python
class CesiumPropertyTableStatus(EnumBase)
```

brief: Reports the status of a FCesiumPropertyTable. If the property table cannot be accessed, this briefly indicates why.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTable.h

<a id="unreal.CesiumPropertyTableStatus.VALID"></a>

#### VALID

0: The property table is valid.

<a id="unreal.CesiumPropertyTableStatus.ERROR_INVALID_PROPERTY_TABLE"></a>

#### ERROR\_INVALID\_PROPERTY\_TABLE

1: The property table instance was not initialized from an actual glTF
    property table.

<a id="unreal.CesiumPropertyTableStatus.ERROR_INVALID_PROPERTY_TABLE_CLASS"></a>

#### ERROR\_INVALID\_PROPERTY\_TABLE\_CLASS

2: The property table's class could be found in the schema of the metadata
    extension.

<a id="unreal.CesiumPropertyTablePropertyStatus"></a>