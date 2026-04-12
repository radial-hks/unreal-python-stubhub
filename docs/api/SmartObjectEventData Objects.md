## SmartObjectEventData Objects

```python
class SmartObjectEventData(StructBase)
```

Struct describing a change in Smart Object or Slot.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``reason`` (SmartObjectChangeReason):  [Read-Write] Change reason.
- ``slot_handle`` (SmartObjectSlotHandle):  [Read-Write] Handle to the changed slot, if invalid, the event is for the object.
- ``smart_object_handle`` (SmartObjectHandle):  [Read-Write] Handle to the changed Smart Object.
- ``tag`` (GameplayTag):  [Read-Write] Added/Removed tag, or event tag, depending on Reason.

<a id="unreal.SmartObjectEventData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(smart_object_handle: SmartObjectHandle = [],
             slot_handle: SmartObjectSlotHandle = [],
             reason: SmartObjectChangeReason = SmartObjectChangeReason.NONE,
             tag: GameplayTag = ["None"]) -> None
```

<a id="unreal.SmartObjectEventData.smart_object_handle"></a>

#### smart\_object\_handle

```python
@property
def smart_object_handle() -> SmartObjectHandle
```

(SmartObjectHandle):  [Read-Only] Handle to the changed Smart Object.

<a id="unreal.SmartObjectEventData.slot_handle"></a>

#### slot\_handle

```python
@property
def slot_handle() -> SmartObjectSlotHandle
```

(SmartObjectSlotHandle):  [Read-Only] Handle to the changed slot, if invalid, the event is for the object.

<a id="unreal.SmartObjectEventData.reason"></a>

#### reason

```python
@property
def reason() -> SmartObjectChangeReason
```

(SmartObjectChangeReason):  [Read-Only] Change reason.

<a id="unreal.SmartObjectEventData.tag"></a>

#### tag

```python
@property
def tag() -> GameplayTag
```

(GameplayTag):  [Read-Only] Added/Removed tag, or event tag, depending on Reason.

<a id="unreal.SmartObjectSlotHandle"></a>