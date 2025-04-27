## TriggerEvent Objects

```python
class TriggerEvent(EnumBase)
```

Trigger events are the Action's interpretation of all Trigger State transitions that occurred for the action in the last tick

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: InputTriggers.h

<a id="unreal.TriggerEvent.TRIGGERED"></a>

#### TRIGGERED

1: Triggering occurred after one or more processing ticks

<a id="unreal.TriggerEvent.STARTED"></a>

#### STARTED

2: An event has occurred that has begun Trigger evaluation. Note: Triggered may also occur this frame, but this event will always be fired first.

<a id="unreal.TriggerEvent.ONGOING"></a>

#### ONGOING

4: Triggering is still being processed. For example, an action with a "Press and Hold" trigger
will be "Ongoing" while the user is holding down the key but the time threshold has not been met yet.

<a id="unreal.TriggerEvent.CANCELED"></a>

#### CANCELED

8: Triggering has been canceled. For example,  the user has let go of a key before the "Press and Hold" time threshold.
The action has started to be evaluated, but never completed.

<a id="unreal.TriggerEvent.COMPLETED"></a>

#### COMPLETED

16: The trigger state has transitioned from Triggered to None this frame, i.e. Triggering has finished.
Note: Using this event restricts you to one set of triggers for Started/Completed events. You may prefer two actions, each with its own trigger rules.
Completed will not fire if any trigger reports Ongoing on the same frame, but both should fire. e.g. Tick 2 of Hold (= Ongoing) + Pressed (= None) combo will raise Ongoing event only.

<a id="unreal.DisplayClusterOperationMode"></a>