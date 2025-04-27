## RichCurveExtrapolation Objects

```python
class RichCurveExtrapolation(EnumBase)
```

Enumerates extrapolation options.

**C++ Source:**

- **Module**: Engine
- **File**: RealCurve.h

<a id="unreal.RichCurveExtrapolation.RCCE_CYCLE"></a>

#### RCCE_CYCLE

0: Repeat the curve without an offset.

<a id="unreal.RichCurveExtrapolation.RCCE_CYCLE_WITH_OFFSET"></a>

#### RCCE_CYCLE_WITH_OFFSET

1: Repeat the curve with an offset relative to the first or last key's value.

<a id="unreal.RichCurveExtrapolation.RCCE_OSCILLATE"></a>

#### RCCE_OSCILLATE

2: Sinusoidally extrapolate.

<a id="unreal.RichCurveExtrapolation.RCCE_LINEAR"></a>

#### RCCE_LINEAR

3: Use a linearly increasing value for extrapolation.

<a id="unreal.RichCurveExtrapolation.RCCE_CONSTANT"></a>

#### RCCE_CONSTANT

4: Use a constant value for extrapolation

<a id="unreal.RichCurveExtrapolation.RCCE_NONE"></a>

#### RCCE_NONE

5: No Extrapolation

<a id="unreal.RichCurveTangentMode"></a>