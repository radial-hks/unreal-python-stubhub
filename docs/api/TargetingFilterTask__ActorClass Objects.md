## TargetingFilterTask\_ActorClass Objects

```python
class TargetingFilterTask_ActorClass(TargetingFilterTask_BasicFilterTemplate)
```

class: UTargetingFilterTask_ActorClass Simple filtering task where we check the targets class type against the required and ignored class types.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingFilterTask_ActorClass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ignored_actor_class_filters`` (Array[type(Class)]):  [Read-Write] The set of ignored actor classes (must NOT be one of these types)
- ``required_actor_class_filters`` (Array[type(Class)]):  [Read-Write] The set of required actor classes (must be one of these types to not be filtered out)

<a id="unreal.TargetingPreset"></a>