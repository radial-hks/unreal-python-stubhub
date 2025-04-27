## SpawnActorScaleMethod Objects

```python
class SpawnActorScaleMethod(EnumBase)
```

Determines how the transform being passed into actor spawning methods interact with the actor's default root component

**C++ Source:**

- **Module**: Engine
- **File**: Actor.h

<a id="unreal.SpawnActorScaleMethod.OVERRIDE_ROOT_SCALE"></a>

#### OVERRIDE_ROOT_SCALE

0: Ignore the default scale in the actor's root component and hard-set it to the value of SpawnTransform Parameter

<a id="unreal.SpawnActorScaleMethod.MULTIPLY_WITH_ROOT"></a>

#### MULTIPLY_WITH_ROOT

1: Multiply value of the SpawnTransform Parameter with the default scale in the actor's root component

<a id="unreal.AlphaBlendOption"></a>