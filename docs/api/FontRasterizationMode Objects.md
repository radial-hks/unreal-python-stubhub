## FontRasterizationMode Objects

```python
class FontRasterizationMode(EnumBase)
```

Enumerates supported font rasterization modes.

**C++ Source:**

- **Module**: SlateCore
- **File**: FontRasterizationMode.h

<a id="unreal.FontRasterizationMode.BITMAP"></a>

#### BITMAP

0: Glyphs are rasterized directly into alpha mask bitmaps per size and skew.

<a id="unreal.FontRasterizationMode.MSDF"></a>

#### MSDF

1: Glyphs are rasterized into multi-channel signed distance fields, which are size and skew agnostic.

<a id="unreal.FontRasterizationMode.SDF"></a>

#### SDF

2: Glyphs are rasterized into single-channel signed distance fields, which are size and skew agnostic. More memory efficient but corners may appear rounded.

<a id="unreal.FontRasterizationMode.SDF_APPROXIMATION"></a>

#### SDF_APPROXIMATION

3: Glyphs are rasterized into approximate distance fields, which are size and skew agnostic. More memory and computationally efficient but lower quality.

<a id="unreal.AudioOutputTarget"></a>