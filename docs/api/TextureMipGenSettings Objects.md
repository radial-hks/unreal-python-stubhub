## TextureMipGenSettings Objects

```python
class TextureMipGenSettings(EnumBase)
```

Texture Mip Gen Settings

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureMipGenSettings.TMGS_FROM_TEXTURE_GROUP"></a>

#### TMGS_FROM_TEXTURE_GROUP

0: Default for the "texture".

<a id="unreal.TextureMipGenSettings.TMGS_SIMPLE_AVERAGE"></a>

#### TMGS_SIMPLE_AVERAGE

1: 2x2 average, default for the "texture group".

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN0"></a>

#### TMGS_SHARPEN0

2: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN1"></a>

#### TMGS_SHARPEN1

3: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN2"></a>

#### TMGS_SHARPEN2

4: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN3"></a>

#### TMGS_SHARPEN3

5: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN4"></a>

#### TMGS_SHARPEN4

6: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN5"></a>

#### TMGS_SHARPEN5

7: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN6"></a>

#### TMGS_SHARPEN6

8: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN7"></a>

#### TMGS_SHARPEN7

9: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN8"></a>

#### TMGS_SHARPEN8

10: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN9"></a>

#### TMGS_SHARPEN9

11: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_SHARPEN10"></a>

#### TMGS_SHARPEN10

12: 8x8 with sharpening: 0=no sharpening but better quality which is softer, 1=little, 5=medium, 10=extreme.

<a id="unreal.TextureMipGenSettings.TMGS_NO_MIPMAPS"></a>

#### TMGS_NO_MIPMAPS

13

<a id="unreal.TextureMipGenSettings.TMGS_LEAVE_EXISTING_MIPS"></a>

#### TMGS_LEAVE_EXISTING_MIPS

14: Do not touch existing mip chain as it contains generated data.

<a id="unreal.TextureMipGenSettings.TMGS_BLUR1"></a>

#### TMGS_BLUR1

15: Blur further (useful for image based reflections).

<a id="unreal.TextureMipGenSettings.TMGS_BLUR2"></a>

#### TMGS_BLUR2

16

<a id="unreal.TextureMipGenSettings.TMGS_BLUR3"></a>

#### TMGS_BLUR3

17

<a id="unreal.TextureMipGenSettings.TMGS_BLUR4"></a>

#### TMGS_BLUR4

18

<a id="unreal.TextureMipGenSettings.TMGS_BLUR5"></a>

#### TMGS_BLUR5

19

<a id="unreal.TextureMipGenSettings.TMGS_UNFILTERED"></a>

#### TMGS_UNFILTERED

20: Use the first texel of each 2x2 (or 2x2x2) group.

<a id="unreal.TextureMipGenSettings.TMGS_ANGULAR"></a>

#### TMGS_ANGULAR

21: Introduce significant amount of blur using angular filtering (only applies to cubemaps, useful for ambient lighting).

<a id="unreal.CompositeTextureMode"></a>