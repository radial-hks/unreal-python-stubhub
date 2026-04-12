## TextureSourceEncoding Objects

```python
class TextureSourceEncoding(EnumBase)
```

List of (advanced) texture source encodings, matching the list in ColorManagementDefines.h.

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureSourceEncoding.TSE_NONE"></a>

#### TSE\_NONE

0: The source encoding is not overridden.

<a id="unreal.TextureSourceEncoding.TSE_LINEAR"></a>

#### TSE\_LINEAR

1: The source encoding is considered linear (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_RGB"></a>

#### TSE\_S\_RGB

2: sRGB source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_ST2084"></a>

#### TSE\_ST2084

3: SMPTE ST 2084/PQ source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_GAMMA22"></a>

#### TSE\_GAMMA22

4: Gamma 2.2 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_BT1886"></a>

#### TSE\_BT1886

5: BT1886/Gamma 2.4 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_GAMMA26"></a>

#### TSE\_GAMMA26

6: Gamma 2.6 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_CINEON"></a>

#### TSE\_CINEON

7: Cineon source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_RED_LOG"></a>

#### TSE\_RED\_LOG

8: RED Log source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_RED_LOG3G10"></a>

#### TSE\_RED\_LOG3G10

9: RED Log3G10 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_LOG1"></a>

#### TSE\_S\_LOG1

10: Sony SLog1 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_LOG2"></a>

#### TSE\_S\_LOG2

11: Sony SLog2 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_S_LOG3"></a>

#### TSE\_S\_LOG3

12: Sony SLog3 source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_ALEXA_V3_LOG_C"></a>

#### TSE\_ALEXA\_V3\_LOG\_C

13: ARRI Alexa V3 LogC source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_CANON_LOG"></a>

#### TSE\_CANON\_LOG

14: Canon Log source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_PRO_TUNE"></a>

#### TSE\_PRO\_TUNE

15: GoPro ProTune source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureSourceEncoding.TSE_V_LOG"></a>

#### TSE\_V\_LOG

16: Panasonic V-Log source encoding to be linearized (before optional sRGB encoding is applied).

<a id="unreal.TextureColorSpace"></a>