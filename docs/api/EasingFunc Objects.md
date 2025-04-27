## EasingFunc Objects

```python
class EasingFunc(EnumBase)
```

Provides different easing functions that can be used in blueprints

**C++ Source:**

- **Module**: Engine
- **File**: KismetMathLibrary.h

<a id="unreal.EasingFunc.LINEAR"></a>

#### LINEAR

0: Simple linear interpolation.

<a id="unreal.EasingFunc.STEP"></a>

#### STEP

1: Simple step interpolation.

<a id="unreal.EasingFunc.SINUSOIDAL_IN"></a>

#### SINUSOIDAL_IN

2: Sinusoidal in interpolation.

<a id="unreal.EasingFunc.SINUSOIDAL_OUT"></a>

#### SINUSOIDAL_OUT

3: Sinusoidal out interpolation.

<a id="unreal.EasingFunc.SINUSOIDAL_IN_OUT"></a>

#### SINUSOIDAL_IN_OUT

4: Sinusoidal in/out interpolation.

<a id="unreal.EasingFunc.EASE_IN"></a>

#### EASE_IN

5: Smoothly accelerates, but does not decelerate into the target.  Ease amount controlled by BlendExp.

<a id="unreal.EasingFunc.EASE_OUT"></a>

#### EASE_OUT

6: Immediately accelerates, but smoothly decelerates into the target.  Ease amount controlled by BlendExp.

<a id="unreal.EasingFunc.EASE_IN_OUT"></a>

#### EASE_IN_OUT

7: Smoothly accelerates and decelerates.  Ease amount controlled by BlendExp.

<a id="unreal.EasingFunc.EXPO_IN"></a>

#### EXPO_IN

8: Easing in using an exponential

<a id="unreal.EasingFunc.EXPO_OUT"></a>

#### EXPO_OUT

9: Easing out using an exponential

<a id="unreal.EasingFunc.EXPO_IN_OUT"></a>

#### EXPO_IN_OUT

10: Easing in/out using an exponential method

<a id="unreal.EasingFunc.CIRCULAR_IN"></a>

#### CIRCULAR_IN

11: Easing is based on a half circle.

<a id="unreal.EasingFunc.CIRCULAR_OUT"></a>

#### CIRCULAR_OUT

12: Easing is based on an inverted half circle.

<a id="unreal.EasingFunc.CIRCULAR_IN_OUT"></a>

#### CIRCULAR_IN_OUT

13: Easing is based on two half circles.

<a id="unreal.LerpInterpolationMode"></a>