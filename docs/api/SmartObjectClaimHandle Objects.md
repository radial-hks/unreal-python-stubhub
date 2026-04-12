## SmartObjectClaimHandle Objects

```python
class SmartObjectClaimHandle(StructBase)
```

Struct describing a reservation between a user and a smart object slot.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectRuntime.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``slot_handle`` (SmartObjectSlotHandle):  [Read-Write] Handle of the claimed slot.
- ``smart_object_handle`` (SmartObjectHandle):  [Read-Write] Handle to the Smart Object where the claimed slot belongs to.
- ``user_handle`` (SmartObjectUserHandle):  [Read-Write] Handle describing the user which claimed the slot.

<a id="unreal.SmartObjectClaimHandle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(smart_object_handle: SmartObjectHandle = [],
             slot_handle: SmartObjectSlotHandle = []) -> None
```

<a id="unreal.SmartObjectClaimHandle.smart_object_handle"></a>

#### smart\_object\_handle

```python
@property
def smart_object_handle() -> SmartObjectHandle
```

(SmartObjectHandle):  [Read-Only] Handle to the Smart Object where the claimed slot belongs to.

<a id="unreal.SmartObjectClaimHandle.slot_handle"></a>

#### slot\_handle

```python
@property
def slot_handle() -> SmartObjectSlotHandle
```

(SmartObjectSlotHandle):  [Read-Only] Handle of the claimed slot.

<a id="unreal.SmartObjectRequestFilter"></a>