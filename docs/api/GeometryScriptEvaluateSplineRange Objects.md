## GeometryScriptEvaluateSplineRange Objects

```python
class GeometryScriptEvaluateSplineRange(EnumBase)
```

EGeometry Script Evaluate Spline Range

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolyPathFunctions.h

<a id="unreal.GeometryScriptEvaluateSplineRange.FULL_SPLINE"></a>

#### FULL\_SPLINE

0: Evaluate the full spline, ignoring any specified range

<a id="unreal.GeometryScriptEvaluateSplineRange.DISTANCE_RANGE"></a>

#### DISTANCE\_RANGE

1: Evaluate a range specified by distances along the spline

<a id="unreal.GeometryScriptEvaluateSplineRange.TIME_RANGE_CONSTANT_SPEED"></a>

#### TIME\_RANGE\_CONSTANT\_SPEED

2: Evaluate a range specified by times, based on travelling at constant speed along the spline

<a id="unreal.GeometryScriptEvaluateSplineRange.TIME_RANGE_VARIABLE_SPEED"></a>

#### TIME\_RANGE\_VARIABLE\_SPEED

3: Evaluate a range specified by times, based on travelling at a constant rate of spline segments/second

<a id="unreal.GeometryScriptPixelSamplingMethod"></a>