## CesiumFeatureIdTextureStatus Objects

```python
class CesiumFeatureIdTextureStatus(EnumBase)
```

brief: Reports the status of a FCesiumFeatureIdTexture. If the feature ID texture cannot be accessed, this briefly indicates why.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeatureIdTexture.h

<a id="unreal.CesiumFeatureIdTextureStatus.VALID"></a>

#### VALID

0: The feature ID texture is valid.

<a id="unreal.CesiumFeatureIdTextureStatus.ERROR_INVALID_TEXTURE"></a>

#### ERROR\_INVALID\_TEXTURE

1: The feature ID texture cannot be found in the glTF, or the texture itself
    has errors.

<a id="unreal.CesiumFeatureIdTextureStatus.ERROR_INVALID_TEXTURE_ACCESS"></a>

#### ERROR\_INVALID\_TEXTURE\_ACCESS

2: The feature ID texture is being read in an invalid way -- for example,
    trying to read nonexistent image channels.

<a id="unreal.CesiumFlyToRotation"></a>