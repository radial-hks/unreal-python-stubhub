## ModifyCurveApplyMode Objects

```python
class ModifyCurveApplyMode(EnumBase)
```

EModify Curve Apply Mode

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_ModifyCurve.h

<a id="unreal.ModifyCurveApplyMode.ADD"></a>

#### ADD

0: Add new value to input curve value

<a id="unreal.ModifyCurveApplyMode.SCALE"></a>

#### SCALE

1: Scale input value by new value

<a id="unreal.ModifyCurveApplyMode.BLEND"></a>

#### BLEND

2: Blend input with new curve value, using Alpha setting on the node

<a id="unreal.ModifyCurveApplyMode.WEIGHTED_MOVING_AVERAGE"></a>

#### WEIGHTED_MOVING_AVERAGE

3: Blend the new curve value with the last curve value using Alpha to determine the weighting (.5 is a moving average, higher values react to new values faster, lower slower)

<a id="unreal.ModifyCurveApplyMode.REMAP_CURVE"></a>

#### REMAP_CURVE

4: Remaps the new curve value between the CurveValues entry and 1.0 (.5 in CurveValues makes 0.51 map to 0.02)

<a id="unreal.RBFSolverType"></a>