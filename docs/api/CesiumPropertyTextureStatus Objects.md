## CesiumPropertyTextureStatus Objects

```python
class CesiumPropertyTextureStatus(EnumBase)
```

namespace CesiumGltf

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPropertyTexture.h

<a id="unreal.CesiumPropertyTextureStatus.VALID"></a>

#### VALID

0: The property texture is valid.

<a id="unreal.CesiumPropertyTextureStatus.ERROR_INVALID_PROPERTY_TEXTURE"></a>

#### ERROR\_INVALID\_PROPERTY\_TEXTURE

1: The property texture instance was not initialized from an actual glTF
  property texture.

<a id="unreal.CesiumPropertyTextureStatus.ERROR_INVALID_PROPERTY_TEXTURE_CLASS"></a>

#### ERROR\_INVALID\_PROPERTY\_TEXTURE\_CLASS

2: The property texture's class could be found in the schema of the metadata
  extension.

<a id="unreal.CesiumPropertyTexturePropertyStatus"></a>