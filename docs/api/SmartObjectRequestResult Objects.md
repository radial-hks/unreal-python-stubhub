## SmartObjectRequestResult Objects

```python
class SmartObjectRequestResult(StructBase)
```

Struct that holds the object and slot selected by processing a smart object request.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``slot_handle`` (SmartObjectSlotHandle):  [Read-Only]
- ``smart_object_handle`` (SmartObjectHandle):  [Read-Only]

<a id="unreal.SmartObjectRequestResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(smart_object_handle: SmartObjectHandle = [],
             slot_handle: SmartObjectSlotHandle = []) -> None
```

<a id="unreal.SmartObjectRequestResult.smart_object_handle"></a>

#### smart\_object\_handle

```python
@property
def smart_object_handle() -> SmartObjectHandle
```

(SmartObjectHandle):  [Read-Only]

<a id="unreal.SmartObjectRequestResult.slot_handle"></a>

#### slot\_handle

```python
@property
def slot_handle() -> SmartObjectSlotHandle
```

(SmartObjectSlotHandle):  [Read-Only]

<a id="unreal.SmartObjectSlotEntranceHandle"></a>