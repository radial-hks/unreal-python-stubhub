## MovieSceneConditionCheckFrequency Objects

```python
class MovieSceneConditionCheckFrequency(EnumBase)
```

Defines how often a condition needs to be checked.
*  Most conditions should return 'Once', but if the condition result can change during playback, 'OnTick' can be chosen to have the condition re-evaluated each tick.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneCondition.h

<a id="unreal.MovieSceneConditionCheckFrequency.ONCE"></a>

#### ONCE

0: Condition result will not change during sequence playback and only needs to get checked once.

<a id="unreal.MovieSceneConditionCheckFrequency.ON_TICK"></a>

#### ON_TICK

1: Condition result may change during sequence playback and should be checked per tick.

<a id="unreal.MovieSceneEvaluationType"></a>