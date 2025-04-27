## PixelDepthOffsetMode Objects

```python
class PixelDepthOffsetMode(EnumBase)
```

Determines how the pixel depth offset is evaluated and applied. Must match PODM_LEGACY in MaterialTemplace.ush.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.PixelDepthOffsetMode.PDOM_LEGACY"></a>

#### PDOM_LEGACY

0: This is the legacy mode where PDO is applied differently for Depth (along View Forward) and world position (along Camera Vector).

<a id="unreal.PixelDepthOffsetMode.PDOM_ALONG_CAMERA_VECTOR"></a>

#### PDOM_ALONG_CAMERA_VECTOR

1: PDO is applied along the Camera Vector for Depth and World Position altogether.

<a id="unreal.PropertyEditorTestEnum"></a>