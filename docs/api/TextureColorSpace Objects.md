## TextureColorSpace Objects

```python
class TextureColorSpace(EnumBase)
```

List of (source) texture color spaces, matching the list in ColorManagementDefines.h.

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureColorSpace.TCS_NONE"></a>

#### TCS_NONE

0: No explicit color space definition.

<a id="unreal.TextureColorSpace.TCS_S_RGB"></a>

#### TCS_S_RGB

1: sRGB / Rec709 (BT.709) color primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_REC2020"></a>

#### TCS_REC2020

2: Rec2020 (BT.2020) primaries with D65 white point.

<a id="unreal.TextureColorSpace.TCS_ACESAP0"></a>

#### TCS_ACESAP0

3: ACES AP0 wide gamut primaries, with D60 white point.

<a id="unreal.TextureColorSpace.TCS_ACESAP1"></a>

#### TCS_ACESAP1

4: ACES AP1 / ACEScg wide gamut primaries, with D60 white point.

<a id="unreal.TextureColorSpace.TCS_P3DCI"></a>

#### TCS_P3DCI

5: P3 (Theater) primaries, with DCI Calibration white point.

<a id="unreal.TextureColorSpace.TCS_P3D65"></a>

#### TCS_P3D65

6: P3 (Display) primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_RED_WIDE_GAMUT"></a>

#### TCS_RED_WIDE_GAMUT

7: RED Wide Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_SONY_S_GAMUT3"></a>

#### TCS_SONY_S_GAMUT3

8: Sony S-Gamut/S-Gamut3 primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_SONY_S_GAMUT3_CINE"></a>

#### TCS_SONY_S_GAMUT3_CINE

9: Sony S-Gamut3 Cine primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_ALEXA_WIDE_GAMUT"></a>

#### TCS_ALEXA_WIDE_GAMUT

10: Alexa Wide Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_CANON_CINEMA_GAMUT"></a>

#### TCS_CANON_CINEMA_GAMUT

11: Canon Cinema Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_GO_PRO_PROTUNE_NATIVE"></a>

#### TCS_GO_PRO_PROTUNE_NATIVE

12: GoPro Protune Native primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_PANASONIC_V_GAMUT"></a>

#### TCS_PANASONIC_V_GAMUT

13: Panasonic V-Gamut primaries, with D65 white point.

<a id="unreal.TextureColorSpace.TCS_CUSTOM"></a>

#### TCS_CUSTOM

99: User defined color space and white point.

<a id="unreal.TextureChromaticAdaptationMethod"></a>