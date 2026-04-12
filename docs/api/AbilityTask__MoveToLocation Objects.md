## AbilityTask\_MoveToLocation Objects

```python
class AbilityTask_MoveToLocation(AbilityTask)
```

Move to a location, ignoring clipping, over a given length of time. Ends when the TargetLocation is reached.
This will RESET your character's current movement mode! If you wish to maintain PHYS_Flying or PHYS_Custom, you must
reset it on completion.!

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_MoveToLocation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_target_location_reached`` (MoveToLocationDelegate):  [Read-Write]

<a id="unreal.AbilityTask_MoveToLocation.on_target_location_reached"></a>

#### on\_target\_location\_reached

```python
@property
def on_target_location_reached() -> MoveToLocationDelegate
```

(MoveToLocationDelegate):  [Read-Write]

<a id="unreal.AbilityTask_MoveToLocation.on_target_location_reached"></a>

#### on\_target\_location\_reached

```python
@on_target_location_reached.setter
def on_target_location_reached(value: MoveToLocationDelegate) -> None
```

<a id="unreal.AbilityTask_NetworkSyncPoint"></a>