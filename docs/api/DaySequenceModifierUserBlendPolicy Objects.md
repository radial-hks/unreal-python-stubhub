## DaySequenceModifierUserBlendPolicy Objects

```python
class DaySequenceModifierUserBlendPolicy(EnumBase)
```

Enum specifying how the modifier resolves the user specified blend weight against the internal blend weight.

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceModifierComponent.h

<a id="unreal.DaySequenceModifierUserBlendPolicy.IGNORED"></a>

#### IGNORED

0: User specified weights are ignored (i.e. the effective weight is InternallyComputedWeight

<a id="unreal.DaySequenceModifierUserBlendPolicy.MINIMUM"></a>

#### MINIMUM

1: (default) The effective weight is FMath::Min(InternallyComputedWeight, UserSpecifiedWeight

<a id="unreal.DaySequenceModifierUserBlendPolicy.MAXIMUM"></a>

#### MAXIMUM

2: The effective weight is FMath::Max(InternallyComputedWeight, UserSpecifiedWeight

<a id="unreal.DaySequenceModifierUserBlendPolicy.OVERRIDE"></a>

#### OVERRIDE

3: The effective weight is UserSpecifiedWeight

<a id="unreal.FloatArrayToIntArrayFunctionEnum"></a>