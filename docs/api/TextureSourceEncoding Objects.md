## TextureSourceEncoding Objects

```python
class TextureSourceEncoding(EnumBase)
```

List of (advanced) texture source encodings, matching the list in ColorManagementDefines.h.

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureSourceEncoding.TSE_NONE"></a>

#### TSE_NONE

0: The source encoding is not overridden.

<a id="unreal.TextureSourceEncoding.TSE_LINEAR"></a>

#### TSE_LINEAR

1: The source encoding is considered linear (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_RGB"></a>

#### TSE_S_RGB

2: sRGB source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_ST2084"></a>

#### TSE_ST2084

3: SMPTE ST 2084/PQ source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_GAMMA22"></a>

#### TSE_GAMMA22

4: Gamma 2.2 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_BT1886"></a>

#### TSE_BT1886

5: BT1886/Gamma 2.4 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_GAMMA26"></a>

#### TSE_GAMMA26

6: Gamma 2.6 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_CINEON"></a>

#### TSE_CINEON

7: Cineon source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_RED_LOG"></a>

#### TSE_RED_LOG

8: RED Log source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_RED_LOG3G10"></a>

#### TSE_RED_LOG3G10

9: RED Log3G10 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_LOG1"></a>

#### TSE_S_LOG1

10: Sony SLog1 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_LOG2"></a>

#### TSE_S_LOG2

11: Sony SLog2 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_LOG3"></a>

#### TSE_S_LOG3

12: Sony SLog3 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_ALEXA_V3_LOG_C"></a>

#### TSE_ALEXA_V3_LOG_C

13: ARRI Alexa V3 LogC source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_CANON_LOG"></a>

#### TSE_CANON_LOG

14: Canon Log source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_PRO_TUNE"></a>

#### TSE_PRO_TUNE

15: GoPro ProTune source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_V_LOG"></a>

#### TSE_V_LOG

16: Panasonic V-Log source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureColorSpace"></a>