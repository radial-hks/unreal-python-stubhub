## SmartObjectSlotValidationParams Objects

```python
class SmartObjectSlotValidationParams(StructBase)
```

Parameters for Smart Object navigation and collision validation.

**C++ Source:**

- **Plugin**: SmartObjects
- **Module**: SmartObjectsModule
- **File**: SmartObjectTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ground_trace_parameters`` (SmartObjectTraceParams):  [Read-Write] Trace parameters used for finding navigation location on ground.
- ``navigation_filter`` (type(Class)):  [Read-Write] Navigation filter used to validate entrance locations.
- ``search_extents`` (Vector):  [Read-Write] How far we allow the validated location to be from the specified navigation location.
- ``transition_trace_parameters`` (SmartObjectTraceParams):  [Read-Write] Trace parameters user for checking if the transition between navigation location and slot is unblocked.
- ``use_navigation_capsule_size`` (bool):  [Read-Write] If true, the capsule size is queried from the user actor via INavAgentInterface.
- ``user_capsule`` (SmartObjectUserCapsuleParams):  [Read-Write] Dimensions of the capsule used for testing if user can fit into a specific location.
  If bUseNavigationCapsuleSize is set, the capsule size from the Actor navigation settings is used if the actor is present (otherwise we fallback to the UserCapsule).

<a id="unreal.SmartObjectSlotValidationParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.StateTreeStateParameters"></a>