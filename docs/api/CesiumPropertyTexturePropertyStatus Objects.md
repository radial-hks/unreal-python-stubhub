## CesiumPropertyTexturePropertyStatus Objects

```python
class CesiumPropertyTexturePropertyStatus(EnumBase)
```

brief: Reports the status of a FCesiumPropertyTextureProperty. If the property texture property cannot be accessed, this briefly indicates why.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTextureProperty.h

<a id="unreal.CesiumPropertyTexturePropertyStatus.VALID"></a>

#### VALID

0: The property texture property is valid.

<a id="unreal.CesiumPropertyTexturePropertyStatus.EMPTY_PROPERTY_WITH_DEFAULT"></a>

#### EMPTY\_PROPERTY\_WITH\_DEFAULT

1: The property texture property is empty but has a specified default value.

<a id="unreal.CesiumPropertyTexturePropertyStatus.ERROR_INVALID_PROPERTY"></a>

#### ERROR\_INVALID\_PROPERTY

2: The property texture property does not exist in the glTF, or the property
    definition itself contains errors.

<a id="unreal.CesiumPropertyTexturePropertyStatus.ERROR_INVALID_PROPERTY_DATA"></a>

#### ERROR\_INVALID\_PROPERTY\_DATA

3: The data associated with the property texture property is malformed and
    cannot be retrieved.

<a id="unreal.CesiumPropertyTexturePropertyStatus.ERROR_UNSUPPORTED_PROPERTY"></a>

#### ERROR\_UNSUPPORTED\_PROPERTY

4: The type of this property texture property is not supported.

<a id="unreal.CesiumRasterOverlayLoadType"></a>