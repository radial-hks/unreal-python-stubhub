## FCTweenBlueprintLibrary Objects

```python
class FCTweenBlueprintLibrary(BlueprintFunctionLibrary)
```

FCTween Blueprint Library

**C++ Source:**

- **Plugin**: FCTween
- **Module**: FCTween
- **File**: FCTweenBlueprintLibrary.h

<a id="unreal.FCTweenBlueprintLibrary.ensure_tween_capacity"></a>

#### ensure_tween_capacity

```python
@classmethod
def ensure_tween_capacity(cls,
                          num_float_tweens: int = 75,
                          num_vector_tweens: int = 50,
                          num_vector2d_tweens: int = 50,
                          num_quat_tweens: int = 10) -> None
```

X.ensure_tween_capacity(num_float_tweens=75, num_vector_tweens=50, num_vector2d_tweens=50, num_quat_tweens=10) -> None
Make sure there are at least these many of each type of tween available in memory. Call this only once, probably in a
GameInstance blueprint, if you need more initial memory reserved on game startup.

Args:
    num_float_tweens (int32): 
    num_vector_tweens (int32): 
    num_vector2d_tweens (int32): 
    num_quat_tweens (int32):

<a id="unreal.FCTweenBlueprintLibrary.ease_with_params"></a>

#### ease_with_params

```python
@classmethod
def ease_with_params(cls,
                     t: float,
                     ease_type: FCEase,
                     param1: float = 0.000000,
                     param2: float = 0.000000) -> float
```

X.ease_with_params(t, ease_type, param1=0.000000, param2=0.000000) -> float
Ease with overriding parameters that affect Elastic, Back, Stepped, and Smoothstep. 0 means no override

Args:
    t (float): the percent complete, 0-1
    ease_type (FCEase): The easing function to interpolate with
    param1 (float): Elastic: Amplitude (1.0) / Back: Overshoot (1.70158) / Stepped: Steps (10) / Smoothstep: x0 (0)
    param2 (float): Elastic: Period (0.2) / Smoothstep: x1 (1)

Returns:
    float:

<a id="unreal.FCTweenBlueprintLibrary.ease"></a>

#### ease

```python
@classmethod
def ease(cls, t: float, ease_type: FCEase) -> float
```

X.ease(t, ease_type) -> float
Ease with overriding parameters

Args:
    t (float): the percent complete, 0-1
    ease_type (FCEase): The easing function to interpolate with

Returns:
    float:

<a id="unreal.FCTweenBPAction"></a>