## TriggerState Objects

```python
class TriggerState(EnumBase)
```

Trigger states are a light weight interpretation of the provided input values used in trigger UpdateState responses.

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

<a id="unreal.TriggerState.NONE"></a>

#### NONE

0: No inputs

<a id="unreal.TriggerState.ONGOING"></a>

#### ONGOING

1: Triggering is being monitored, but not yet been confirmed (e.g. a time based trigger that requires the trigger state to be maintained over several frames)

<a id="unreal.TriggerState.TRIGGERED"></a>

#### TRIGGERED

2: The trigger state has been met

<a id="unreal.TriggerType"></a>