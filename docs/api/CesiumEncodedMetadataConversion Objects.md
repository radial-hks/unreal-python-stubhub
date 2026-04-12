## CesiumEncodedMetadataConversion Objects

```python
class CesiumEncodedMetadataConversion(EnumBase)
```

brief: Indicates how a property value from EXT_structural_metadata should be converted to a GPU-accessible type, if possible.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumMetadataEncodingDetails.h

<a id="unreal.CesiumEncodedMetadataConversion.NONE"></a>

#### NONE

0: Do nothing. This is typically used for property types that are
completely unable to be coerced.

<a id="unreal.CesiumEncodedMetadataConversion.COERCE"></a>

#### COERCE

1: Coerce the components of a property value to the specified component type.
If the property contains string values, this attempts to parse numbers from
the strings as uint8s.

<a id="unreal.CesiumEncodedMetadataConversion.PARSE_COLOR_FROM_STRING"></a>

#### PARSE\_COLOR\_FROM\_STRING

2: Attempt to parse a color from a string property value. This supports
the following formats:
- rgb(R, G, B), where R, G, and B are values in the range [0, 255]
- hexcode colors, e.g. #ff0000

<a id="unreal.MetasoundFrontendClassType"></a>