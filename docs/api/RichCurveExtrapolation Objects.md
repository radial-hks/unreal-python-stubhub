## RichCurveExtrapolation Objects

```python
class RichCurveExtrapolation(EnumBase)
```

Enumerates extrapolation options.

**C++ Source:**

- **Module**: Engine
- **File**: RealCurve.h

<a id="unreal.RichCurveExtrapolation.RCCE_CYCLE"></a>

#### RCCE\_CYCLE

0: Repeat the curve without an offset.

<a id="unreal.RichCurveExtrapolation.RCCE_CYCLE_WITH_OFFSET"></a>

#### RCCE\_CYCLE\_WITH\_OFFSET

1: Repeat the curve with an offset relative to the first or last key's value.

<a id="unreal.RichCurveExtrapolation.RCCE_OSCILLATE"></a>

#### RCCE\_OSCILLATE

2: Sinusoidally extrapolate.

<a id="unreal.RichCurveExtrapolation.RCCE_LINEAR"></a>

#### RCCE\_LINEAR

3: Use a linearly increasing value for extrapolation.

<a id="unreal.RichCurveExtrapolation.RCCE_CONSTANT"></a>

#### RCCE\_CONSTANT

4: Use a constant value for extrapolation

<a id="unreal.RichCurveExtrapolation.RCCE_NONE"></a>

#### RCCE\_NONE

5: No Extrapolation

<a id="unreal.RichCurveTangentMode"></a>