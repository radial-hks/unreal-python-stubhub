## CesiumPropertyTablePropertyStatus Objects

```python
class CesiumPropertyTablePropertyStatus(EnumBase)
```

brief: Reports the status of a FCesiumPropertyTableProperty. If the property table property cannot be accessed, this briefly indicates why.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTableProperty.h

<a id="unreal.CesiumPropertyTablePropertyStatus.VALID"></a>

#### VALID

0: The property table property is valid.

<a id="unreal.CesiumPropertyTablePropertyStatus.EMPTY_PROPERTY_WITH_DEFAULT"></a>

#### EMPTY\_PROPERTY\_WITH\_DEFAULT

1: The property table property is empty but has a specified default value.

<a id="unreal.CesiumPropertyTablePropertyStatus.ERROR_INVALID_PROPERTY"></a>

#### ERROR\_INVALID\_PROPERTY

2: The property table property does not exist in the glTF, or the property
    definition itself contains errors.

<a id="unreal.CesiumPropertyTablePropertyStatus.ERROR_INVALID_PROPERTY_DATA"></a>

#### ERROR\_INVALID\_PROPERTY\_DATA

3: The data associated with the property table property is malformed and
    cannot be retrieved.

<a id="unreal.CesiumPropertyTextureStatus"></a>