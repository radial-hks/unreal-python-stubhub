## CesiumFeatureIdAttributeStatus Objects

```python
class CesiumFeatureIdAttributeStatus(EnumBase)
```

brief: Reports the status of a FCesiumFeatureIdAttribute. If the feature ID attribute cannot be accessed, this briefly indicates why.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeatureIdAttribute.h

<a id="unreal.CesiumFeatureIdAttributeStatus.VALID"></a>

#### VALID

0: The feature ID attribute is valid.

<a id="unreal.CesiumFeatureIdAttributeStatus.ERROR_INVALID_ATTRIBUTE"></a>

#### ERROR\_INVALID\_ATTRIBUTE

1: The feature ID attribute does not exist in the glTF primitive.

<a id="unreal.CesiumFeatureIdAttributeStatus.ERROR_INVALID_ACCESSOR"></a>

#### ERROR\_INVALID\_ACCESSOR

2: The feature ID attribute uses an invalid accessor in the glTF.

<a id="unreal.CesiumFeatureIdSetType"></a>