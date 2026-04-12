## TextureColorSpace Objects

```python
class TextureColorSpace(EnumBase)
```

List of (source) texture color spaces, matching the list in ColorManagementDefines.h.

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureColorSpace.TCS_NONE"></a>

#### TCS\_NONE

0: No explicit color space definition.

<a id="unreal.TextureColorSpace.TCS_S_RGB"></a>

#### TCS\_S\_RGB

1: sRGB / Rec709 (BT.709) color primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_REC2020"></a>

#### TCS\_REC2020

2: Rec2020 (BT.2020) primaries with D65 white point.

<a id="unreal.TextureColorSpace.TCS_ACESAP0"></a>

#### TCS\_ACESAP0

3: ACES AP0 wide gamut primaries, with D60 white point.

<a id="unreal.TextureColorSpace.TCS_ACESAP1"></a>

#### TCS\_ACESAP1

4: ACES AP1 / ACEScg wide gamut primaries, with D60 white point.

<a id="unreal.TextureColorSpace.TCS_P3DCI"></a>

#### TCS\_P3DCI

5: P3 (Theater) primaries, with DCI Calibration white point.

<a id="unreal.TextureColorSpace.TCS_P3D65"></a>

#### TCS\_P3D65

6: P3 (Display) primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_RED_WIDE_GAMUT"></a>

#### TCS\_RED\_WIDE\_GAMUT

7: RED Wide Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_SONY_S_GAMUT3"></a>

#### TCS\_SONY\_S\_GAMUT3

8: Sony S-Gamut/S-Gamut3 primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_SONY_S_GAMUT3_CINE"></a>

#### TCS\_SONY\_S\_GAMUT3\_CINE

9: Sony S-Gamut3 Cine primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_ALEXA_WIDE_GAMUT"></a>

#### TCS\_ALEXA\_WIDE\_GAMUT

10: Alexa Wide Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_CANON_CINEMA_GAMUT"></a>

#### TCS\_CANON\_CINEMA\_GAMUT

11: Canon Cinema Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_GO_PRO_PROTUNE_NATIVE"></a>

#### TCS\_GO\_PRO\_PROTUNE\_NATIVE

12: GoPro Protune Native primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_PANASONIC_V_GAMUT"></a>

#### TCS\_PANASONIC\_V\_GAMUT

13: Panasonic V-Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_CUSTOM"></a>

#### TCS\_CUSTOM

99: User defined color space and white point.

<a id="unreal.TextureChromaticAdaptationMethod"></a>