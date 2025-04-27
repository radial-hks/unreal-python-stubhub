## PropertyAnimatorCoreSystemMode Objects

```python
class PropertyAnimatorCoreSystemMode(EnumBase)
```

Enumerates all possible modes for the machine clock time source

**C++ Source:**

- **Plugin**: PropertyAnimatorCore
- **Module**: PropertyAnimatorCore
- **File**: PropertyAnimatorCoreSystemTimeSource.h

<a id="unreal.PropertyAnimatorCoreSystemMode.LOCAL_TIME"></a>

#### LOCAL_TIME

0: Local time of the machine

<a id="unreal.PropertyAnimatorCoreSystemMode.UTC_TIME"></a>

#### UTC_TIME

1: Universal time = Greenwich Mean Time

<a id="unreal.PropertyAnimatorCoreSystemMode.COUNTDOWN"></a>

#### COUNTDOWN

2: Specified duration elapsing until it reaches 0

<a id="unreal.PropertyAnimatorCoreSystemMode.STOPWATCH"></a>

#### STOPWATCH

3: Current time elapsed since the time source is active

<a id="unreal.PropertyAnimatorCoreMachineClockMode"></a>