## DaySequenceModifierMode Objects

```python
class DaySequenceModifierMode(EnumBase)
```

Enum that defines modifier behavior for auto enabling and computing the internal blend weight.

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceModifierComponent.h

<a id="unreal.DaySequenceModifierMode.GLOBAL"></a>

#### GLOBAL

0: Blend weight is always 1.0.

<a id="unreal.DaySequenceModifierMode.VOLUME"></a>

#### VOLUME

1: Blend weight smoothly moves between 0.0 and 1.0 as the blend target crosses the volume boundary.

<a id="unreal.DaySequenceModifierBlendMode"></a>