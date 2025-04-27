## AnimationCurveData Objects

```python
class AnimationCurveData(StructBase)
```

Structure encapsulating animated curve data. Currently only contains Float and Transform curves.

**C++ Source:**

- **Module**: Engine
- **File**: IAnimationDataModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``float_curves`` (Array[FloatCurve]):  [Read-Only] Float-based animation curves
- ``transform_curves`` (Array[TransformCurve]):  [Read-Only] FTransform-based animation curves, used for animation layer editing

<a id="unreal.AnimationCurveData.__init__"></a>

#### __init__

```python
def __init__(float_curves: Array[FloatCurve] = [],
             transform_curves: Array[TransformCurve] = []) -> None
```

<a id="unreal.AnimationCurveData.float_curves"></a>

#### float_curves

```python
@property
def float_curves() -> Array[FloatCurve]
```

(Array[FloatCurve]):  [Read-Only] Float-based animation curves

<a id="unreal.AnimationCurveData.transform_curves"></a>

#### transform_curves

```python
@property
def transform_curves() -> Array[TransformCurve]
```

(Array[TransformCurve]):  [Read-Only] FTransform-based animation curves, used for animation layer editing

<a id="unreal.AnimatedBoneAttribute"></a>