## SmartObjectSlotState Objects

```python
class SmartObjectSlotState(EnumBase)
```

Enumeration to represent the runtime state of a slot

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectRuntime.h

<a id="unreal.SmartObjectSlotState.INVALID"></a>

#### INVALID

0

<a id="unreal.SmartObjectSlotState.FREE"></a>

#### FREE

1: Slot is available

<a id="unreal.SmartObjectSlotState.CLAIMED"></a>

#### CLAIMED

2: Slot is claimed but interaction is not active yet

<a id="unreal.SmartObjectSlotState.OCCUPIED"></a>

#### OCCUPIED

3: Slot is claimed and interaction is active

<a id="unreal.SmartObjectSlotState.DISABLED"></a>

#### DISABLED

4: Slot can no longer be claimed or used since the parent object and its slot are disabled (e.g. instance tags)

<a id="unreal.StateTreeStateType"></a>