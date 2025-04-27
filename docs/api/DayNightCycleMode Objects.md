## DayNightCycleMode Objects

```python
class DayNightCycleMode(EnumBase)
```

Enum specifying how to control a day / night cycle from a modifier

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceModifierComponent.h

<a id="unreal.DayNightCycleMode.DEFAULT"></a>

#### DEFAULT

0: (default) Make no changes to the day/night cycle time

<a id="unreal.DayNightCycleMode.FIXED_TIME"></a>

#### FIXED_TIME

1: Force the day/night cycle to be fixed at the specified constant time

<a id="unreal.DayNightCycleMode.START_AT_SPECIFIED_TIME"></a>

#### START_AT_SPECIFIED_TIME

2: Set an initial time for the day/night cycle when the modifier is enabled

<a id="unreal.DayNightCycleMode.RANDOM_FIXED_TIME"></a>

#### RANDOM_FIXED_TIME

3: Use a random, fixed time for the day/night cycle

<a id="unreal.DayNightCycleMode.RANDOM_START_TIME"></a>

#### RANDOM_START_TIME

4: Start the day/night cycle at a random time, and allow it to continue from there

<a id="unreal.DaySequenceModifierMode"></a>