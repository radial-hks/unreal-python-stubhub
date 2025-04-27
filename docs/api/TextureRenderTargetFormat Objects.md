## TextureRenderTargetFormat Objects

```python
class TextureRenderTargetFormat(EnumBase)
```

Subset of EPixelFormat exposed to UTextureRenderTarget2D

**C++ Source:**

- **Module**: Engine
- **File**: TextureRenderTarget2D.h

<a id="unreal.TextureRenderTargetFormat.RTF_R8"></a>

#### RTF_R8

0: R channel, 8 bit per channel fixed point, range [0, 1].

<a id="unreal.TextureRenderTargetFormat.RTF_RG8"></a>

#### RTF_RG8

1: RG channels, 8 bit per channel fixed point, range [0, 1].

<a id="unreal.TextureRenderTargetFormat.RTF_RGBA8"></a>

#### RTF_RGBA8

2: RGBA channels, 8 bit per channel fixed point, range [0, 1].

<a id="unreal.TextureRenderTargetFormat.RTF_RGBA8_SRGB"></a>

#### RTF_RGBA8_SRGB

3: RGBA channels, 8 bit per channel fixed point, range [0, 1]. RGB is encoded with sRGB gamma curve. A is always stored as linear.

<a id="unreal.TextureRenderTargetFormat.RTF_R16F"></a>

#### RTF_R16F

4: R channel, 16 bit per channel floating point, range [-65504, 65504]

<a id="unreal.TextureRenderTargetFormat.RTF_RG16F"></a>

#### RTF_RG16F

5: RG channels, 16 bit per channel floating point, range [-65504, 65504]

<a id="unreal.TextureRenderTargetFormat.RTF_RGBA16F"></a>

#### RTF_RGBA16F

6: RGBA channels, 16 bit per channel floating point, range [-65504, 65504]

<a id="unreal.TextureRenderTargetFormat.RTF_R32F"></a>

#### RTF_R32F

7: R channel, 32 bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38]

<a id="unreal.TextureRenderTargetFormat.RTF_RG32F"></a>

#### RTF_RG32F

8: RG channels, 32 bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38]

<a id="unreal.TextureRenderTargetFormat.RTF_RGBA32F"></a>

#### RTF_RGBA32F

9: RGBA channels, 32 bit per channel floating point, range [-3.402823 x 10^38, 3.402823 x 10^38]

<a id="unreal.TextureRenderTargetFormat.RTF_RGB10A2"></a>

#### RTF_RGB10A2

10: RGBA channels, 10 bit per channel fixed point and 2 bit of alpha

<a id="unreal.TextureRenderTargetSampleCount"></a>