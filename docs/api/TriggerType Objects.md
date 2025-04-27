## TriggerType Objects

```python
class TriggerType(EnumBase)
```

Trigger type determine how the trigger contributes to an action's overall trigger event the behavior of the trigger

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

<a id="unreal.TriggerType.EXPLICIT"></a>

#### EXPLICIT

0: Input may trigger if any explicit trigger is triggered.

<a id="unreal.TriggerType.IMPLICIT"></a>

#### IMPLICIT

1: Input may trigger only if all implicit triggers are triggered.

<a id="unreal.TriggerType.BLOCKER"></a>

#### BLOCKER

2: Inverted trigger that will block all other triggers when IsBlocking returns true

<a id="unreal.DisplayClusterTargetCameraType"></a>