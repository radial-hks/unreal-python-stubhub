## WaterBodyType Objects

```python
class WaterBodyType(EnumBase)
```

EWater Body Type

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterBodyTypes.h

<a id="unreal.WaterBodyType.RIVER"></a>

#### RIVER

0: Rivers defined by a spline down the middle

<a id="unreal.WaterBodyType.LAKE"></a>

#### LAKE

1: Lakes defined by a close loop spline around the shore with water in the middle

<a id="unreal.WaterBodyType.OCEAN"></a>

#### OCEAN

2: Ocean defined by a shoreline spline and rendered out to a far distance

<a id="unreal.WaterBodyType.TRANSITION"></a>

#### TRANSITION

3: A custom water body that can be used for gameplay reasons.  Uses a spline down the middle to encode gameplay data. Requires a custom mesh to render, doesn't affect landscape

<a id="unreal.WaterBrushFalloffMode"></a>