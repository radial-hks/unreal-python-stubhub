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

#### SINUSOIDAL\_IN

2: Sinusoidal in interpolation.

<a id="unreal.EasingFunc.SINUSOIDAL_OUT"></a>

#### SINUSOIDAL\_OUT

3: Sinusoidal out interpolation.

<a id="unreal.EasingFunc.SINUSOIDAL_IN_OUT"></a>

#### SINUSOIDAL\_IN\_OUT

4: Sinusoidal in/out interpolation.

<a id="unreal.EasingFunc.EASE_IN"></a>

#### EASE\_IN

5: Smoothly accelerates, but does not decelerate into the target.  Ease amount controlled by BlendExp.

<a id="unreal.EasingFunc.EASE_OUT"></a>

#### EASE\_OUT

6: Immediately accelerates, but smoothly decelerates into the target.  Ease amount controlled by BlendExp.

<a id="unreal.EasingFunc.EASE_IN_OUT"></a>

#### EASE\_IN\_OUT

7: Smoothly accelerates and decelerates.  Ease amount controlled by BlendExp.

<a id="unreal.EasingFunc.EXPO_IN"></a>

#### EXPO\_IN

8: Easing in using an exponential

<a id="unreal.EasingFunc.EXPO_OUT"></a>

#### EXPO\_OUT

9: Easing out using an exponential

<a id="unreal.EasingFunc.EXPO_IN_OUT"></a>

#### EXPO\_IN\_OUT

10: Easing in/out using an exponential method

<a id="unreal.EasingFunc.CIRCULAR_IN"></a>

#### CIRCULAR\_IN

11: Easing is based on a half circle.

<a id="unreal.EasingFunc.CIRCULAR_OUT"></a>

#### CIRCULAR\_OUT

12: Easing is based on an inverted half circle.

<a id="unreal.EasingFunc.CIRCULAR_IN_OUT"></a>

#### CIRCULAR\_IN\_OUT

13: Easing is based on two half circles.

<a id="unreal.LerpInterpolationMode"></a>