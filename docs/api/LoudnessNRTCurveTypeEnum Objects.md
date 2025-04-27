## LoudnessNRTCurveTypeEnum Objects

```python
class LoudnessNRTCurveTypeEnum(EnumBase)
```

ELoudnessNRTCurveTypeEnum

Enumeration of available equal loudness curves. Loudness curves based on IEC 61672-1:2013 Electroacoustics - Sound level meters - Part 1: Specifications.

**C++ Source:**

- **Plugin**: AudioSynesthesia
- **Module**: AudioSynesthesia
- **File**: LoudnessNRT.h

<a id="unreal.LoudnessNRTCurveTypeEnum.A"></a>

#### A

0: Loudness Curve A Weighting. Commonly used in environmental sound measurements. Best for low level sounds.

<a id="unreal.LoudnessNRTCurveTypeEnum.B"></a>

#### B

1: Loudness Curve B Weighting. Relative to "A", gives more precedence to frequencies below 1kHz.

<a id="unreal.LoudnessNRTCurveTypeEnum.C"></a>

#### C

2: Loudness Curve C Weighting. Relative to "A" and "B", gives more precedence to frequencies below 1kHz.

<a id="unreal.LoudnessNRTCurveTypeEnum.D"></a>

#### D

3: Loudness Curve D Weighting. Similar to "B" but with an emphasis on presence in the 2kHz-6KHz frequency range.

<a id="unreal.LoudnessNRTCurveTypeEnum.NONE"></a>

#### NONE

4: No loudness curve weighting.

<a id="unreal.MeterPeakType"></a>