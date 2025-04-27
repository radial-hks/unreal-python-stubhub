## MovieSceneAnimatorEvalTimeMode Objects

```python
class MovieSceneAnimatorEvalTimeMode(EnumBase)
```

Enumerates all possible ways of interpreting time

**C++ Source:**

- **Plugin**: PropertyAnimatorCore
- **Module**: PropertyAnimatorCore
- **File**: MovieSceneAnimatorTypes.h

<a id="unreal.MovieSceneAnimatorEvalTimeMode.SEQUENCE"></a>

#### SEQUENCE

0: The sequence time, if the section has an offset, it won't matter

<a id="unreal.MovieSceneAnimatorEvalTimeMode.SECTION"></a>

#### SECTION

1: The section time, takes into account any offset the section has

<a id="unreal.MovieSceneAnimatorEvalTimeMode.CUSTOM"></a>

#### CUSTOM

2: Custom provided time, interpolate between start and end time based on progress

<a id="unreal.Text3DCharacterEffectOrder"></a>