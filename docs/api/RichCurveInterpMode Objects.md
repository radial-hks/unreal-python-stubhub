## RichCurveInterpMode Objects

```python
class RichCurveInterpMode(EnumBase)
```

Method of interpolation between this key and the next.

**C++ Source:**

- **Module**: Engine
- **File**: RealCurve.h

<a id="unreal.RichCurveInterpMode.RCIM_LINEAR"></a>

#### RCIM\_LINEAR

0: Use linear interpolation between values.

<a id="unreal.RichCurveInterpMode.RCIM_CONSTANT"></a>

#### RCIM\_CONSTANT

1: Use a constant value. Represents stepped values.

<a id="unreal.RichCurveInterpMode.RCIM_CUBIC"></a>

#### RCIM\_CUBIC

2: Cubic interpolation. See TangentMode for different cubic interpolation options.

<a id="unreal.RichCurveExtrapolation"></a>