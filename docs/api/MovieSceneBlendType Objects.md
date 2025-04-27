## MovieSceneBlendType Objects

```python
class MovieSceneBlendType(EnumBase)
```

Movie scene blend type enumeration

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneBlendType.h

<a id="unreal.MovieSceneBlendType.ABSOLUTE"></a>

#### ABSOLUTE

1: Blends all other weighted values together as an average of the total weight

<a id="unreal.MovieSceneBlendType.ADDITIVE"></a>

#### ADDITIVE

2: Applies this value as a sum total of all other additives

<a id="unreal.MovieSceneBlendType.RELATIVE"></a>

#### RELATIVE

4: Applies this value as a sum total of all other additives and the initial value before the animation

<a id="unreal.MovieSceneBlendType.ADDITIVE_FROM_BASE"></a>

#### ADDITIVE_FROM_BASE

8: Applies this value as an additive equal to the difference between the current value and the first value

<a id="unreal.MovieSceneBlendType.OVERRIDE"></a>

#### OVERRIDE

16: The value will override the current value

<a id="unreal.UpdatePositionMethod"></a>