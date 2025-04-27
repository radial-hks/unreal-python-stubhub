## InterpCurveMode Objects

```python
class InterpCurveMode(EnumBase)
```

Describes shape of an interpolation curve (mirrored from InterpCurvePoint.h).

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

<a id="unreal.InterpCurveMode.CIM_LINEAR"></a>

#### CIM_LINEAR

0: A straight line between two keypoint values.

<a id="unreal.InterpCurveMode.CIM_CURVE_AUTO"></a>

#### CIM_CURVE_AUTO

1: A cubic-hermite curve between two keypoints, using Arrive/Leave tangents. These tangents will be automatically
              updated when points are moved, etc.  Tangents are unclamped and will plateau at curve start and end points.

<a id="unreal.InterpCurveMode.CIM_CONSTANT"></a>

#### CIM_CONSTANT

2: The out value is held constant until the next key, then will jump to that value.

<a id="unreal.InterpCurveMode.CIM_CURVE_USER"></a>

#### CIM_CURVE_USER

3: A smooth curve just like CIM_Curve, but tangents are not automatically updated so you can have manual control over them (eg. in Curve Editor).

<a id="unreal.InterpCurveMode.CIM_CURVE_BREAK"></a>

#### CIM_CURVE_BREAK

4: A curve like CIM_Curve, but the arrive and leave tangents are not forced to be the same, so you can create a 'corner' at this key.

<a id="unreal.InterpCurveMode.CIM_CURVE_AUTO_CLAMPED"></a>

#### CIM_CURVE_AUTO_CLAMPED

5: A cubic-hermite curve between two keypoints, using Arrive/Leave tangents. These tangents will be automatically
          updated when points are moved, etc.  Tangents are clamped and will plateau at curve start and end points.

<a id="unreal.TypedElementChildInclusionMethod"></a>