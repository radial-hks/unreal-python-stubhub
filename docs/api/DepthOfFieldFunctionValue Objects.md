## DepthOfFieldFunctionValue Objects

```python
class DepthOfFieldFunctionValue(EnumBase)
```

Note: The index is used to map the enum to different code in the shader

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionDepthOfFieldFunction.h

<a id="unreal.DepthOfFieldFunctionValue.TDOF_NEAR_AND_FAR_MASK"></a>

#### TDOF_NEAR_AND_FAR_MASK

0: 0:in Focus .. 1:Near or Far.

<a id="unreal.DepthOfFieldFunctionValue.TDOF_NEAR_MASK"></a>

#### TDOF_NEAR_MASK

1: 0:in Focus or Far .. 1:Near.

<a id="unreal.DepthOfFieldFunctionValue.TDOF_FAR_MASK"></a>

#### TDOF_FAR_MASK

2: 0:in Focus or Near .. 1:Far.

<a id="unreal.DepthOfFieldFunctionValue.TDOF_CIRCLE_OF_CONFUSION_RADIUS"></a>

#### TDOF_CIRCLE_OF_CONFUSION_RADIUS

3: in pixels, only works for CircleDOF, use Abs for the actual radius as the sign of the value indicates near out of focus, positive indicates far out of focus

<a id="unreal.FloatToIntMode"></a>