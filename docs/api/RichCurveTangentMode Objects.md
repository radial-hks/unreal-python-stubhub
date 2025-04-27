## RichCurveTangentMode Objects

```python
class RichCurveTangentMode(EnumBase)
```

If using RCIM_Cubic, this enum describes how the tangents should be controlled in editor.

**C++ Source:**

- **Module**: Engine
- **File**: RichCurve.h

<a id="unreal.RichCurveTangentMode.RCTM_AUTO"></a>

#### RCTM_AUTO

0: Automatically calculates tangents to create smooth curves between values.

<a id="unreal.RichCurveTangentMode.RCTM_USER"></a>

#### RCTM_USER

1: User specifies the tangent as a unified tangent where the two tangents are locked to each other, presenting a consistent curve before and after.

<a id="unreal.RichCurveTangentMode.RCTM_BREAK"></a>

#### RCTM_BREAK

2: User specifies the tangent as two separate broken tangents on each side of the key which can allow a sharp change in evaluation before or after.

<a id="unreal.RichCurveTangentMode.RCTM_SMART_AUTO"></a>

#### RCTM_SMART_AUTO

4: New Auto tangent that creates smoother curves than Auto.

<a id="unreal.RichCurveTangentWeightMode"></a>