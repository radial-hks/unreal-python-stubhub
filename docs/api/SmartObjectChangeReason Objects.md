## SmartObjectChangeReason Objects

```python
class SmartObjectChangeReason(EnumBase)
```

Describes how Smart Object or slot was changed.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

<a id="unreal.SmartObjectChangeReason.NONE"></a>

#### NONE

0: No Change.

<a id="unreal.SmartObjectChangeReason.ON_EVENT"></a>

#### ON\_EVENT

1: External event sent.

<a id="unreal.SmartObjectChangeReason.ON_TAG_ADDED"></a>

#### ON\_TAG\_ADDED

2: A tag was added.

<a id="unreal.SmartObjectChangeReason.ON_TAG_REMOVED"></a>

#### ON\_TAG\_REMOVED

3: A tag was removed.

<a id="unreal.SmartObjectChangeReason.ON_CLAIMED"></a>

#### ON\_CLAIMED

4: Slot was claimed.

<a id="unreal.SmartObjectChangeReason.ON_OCCUPIED"></a>

#### ON\_OCCUPIED

5: Slot is now occupied

<a id="unreal.SmartObjectChangeReason.ON_RELEASED"></a>

#### ON\_RELEASED

6: Slot claim was released.

<a id="unreal.SmartObjectChangeReason.ON_SLOT_ENABLED"></a>

#### ON\_SLOT\_ENABLED

7: Slot was enabled.

<a id="unreal.SmartObjectChangeReason.ON_SLOT_DISABLED"></a>

#### ON\_SLOT\_DISABLED

8: Slot was disabled.

<a id="unreal.SmartObjectChangeReason.ON_OBJECT_ENABLED"></a>

#### ON\_OBJECT\_ENABLED

9: Object was enabled.

<a id="unreal.SmartObjectChangeReason.ON_OBJECT_DISABLED"></a>

#### ON\_OBJECT\_DISABLED

10: Object was disabled.

<a id="unreal.SmartObjectChangeReason.ON_COMPONENT_BOUND"></a>

#### ON\_COMPONENT\_BOUND

11: Related Smart Object Component is bound to simulation.

<a id="unreal.SmartObjectChangeReason.ON_COMPONENT_UNBOUND"></a>

#### ON\_COMPONENT\_UNBOUND

12: Related Smart Object Component is unbound from simulation.

<a id="unreal.SmartObjectEntrancePriority"></a>