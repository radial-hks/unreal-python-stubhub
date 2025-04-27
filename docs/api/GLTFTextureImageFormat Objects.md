## GLTFTextureImageFormat Objects

```python
class GLTFTextureImageFormat(EnumBase)
```

EGLTFTexture Image Format

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFExportOptions.h

<a id="unreal.GLTFTextureImageFormat.NONE"></a>

#### NONE

0: Don't export any textures.

<a id="unreal.GLTFTextureImageFormat.PNG"></a>

#### PNG

1: Always use PNG (lossless compression).

<a id="unreal.GLTFTextureImageFormat.JPEG"></a>

#### JPEG

2: If texture does not have an alpha channel, use JPEG (lossy compression); otherwise fallback to PNG.

<a id="unreal.GLTFMaterialVariantMode"></a>