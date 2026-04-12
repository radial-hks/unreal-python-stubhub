## CurveBlendOption Objects

```python
class CurveBlendOption(EnumBase)
```

ECurve Blend Option

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.CurveBlendOption.OVERRIDE"></a>

#### OVERRIDE

0: Last pose that contains valid curve value override it.

<a id="unreal.CurveBlendOption.DO_NOT_OVERRIDE"></a>

#### DO\_NOT\_OVERRIDE

1: Only set the value if the previous pose doesn't have the curve value.

<a id="unreal.CurveBlendOption.NORMALIZE_BY_WEIGHT"></a>

#### NORMALIZE\_BY\_WEIGHT

2: Normalize By Sum of Weight and use it to blend.

<a id="unreal.CurveBlendOption.BLEND_BY_WEIGHT"></a>

#### BLEND\_BY\_WEIGHT

3: Blend By Weight without normalizing

<a id="unreal.CurveBlendOption.USE_BASE_POSE"></a>

#### USE\_BASE\_POSE

4: Use Base Pose for all curve values. Do not blend

<a id="unreal.CurveBlendOption.USE_MAX_VALUE"></a>

#### USE\_MAX\_VALUE

5: Find the highest curve value from multiple poses and use that.

<a id="unreal.CurveBlendOption.USE_MIN_VALUE"></a>

#### USE\_MIN\_VALUE

6: Find the lowest curve value from multiple poses and use that.

<a id="unreal.ModifyCurveApplyMode"></a>