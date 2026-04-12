## SmartObjectTraceParams Objects

```python
class SmartObjectTraceParams(StructBase)
```

Struct used to define how traces should be handled.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_profile`` (CollisionProfileName):  [Read-Write] Collision profile to use to determine collisions.
- ``object_types`` (Array[ObjectTypeQuery]):  [Read-Write] Object types to use to determine collisions.
- ``trace_channel`` (TraceTypeQuery):  [Read-Write] Trace channel to use to determine collisions.
- ``trace_complex`` (bool):  [Read-Write] Whether we should trace against complex collision
- ``type`` (SmartObjectTraceType):  [Read-Write] Type of trace to use.

<a id="unreal.SmartObjectTraceParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.ControlRigAnimNodeEventName"></a>