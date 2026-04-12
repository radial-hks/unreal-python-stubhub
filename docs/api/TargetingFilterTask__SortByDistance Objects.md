## TargetingFilterTask\_SortByDistance Objects

```python
class TargetingFilterTask_SortByDistance(TargetingSortTask_Base)
```

class: UTargetingFilterTask_SortByDistance Simple sorting filter based on the distance to the source actor. Note: This filter will use the FTargetingDefaultResultsSet and use the Score factor defined for each target to store the distance and sort by that value.

**C++ Source:**

- **Plugin**: TargetingSystem
- **Module**: TargetingSystem
- **File**: TargetingFilterTask_SortByDistance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ascending`` (bool):  [Read-Write]
- ``distance_to_collision_channel`` (CollisionChannel):  [Read-Write] Collision channel used to determine the closest point on a actor's collider.
  Colliders will only be considered if they block this channel
- ``stable_sort`` (bool):  [Read-Write] Should this task use a (slightly slower) sorting algorithm that preserves the relative ordering of targets with equal scores?
- ``use_distance_to_nearest_blocking_collider`` (bool):  [Read-Write] Use the distance to the nearest blocking collision surface on each actor instead of the distance to the actor's location

<a id="unreal.GenericSmartObject"></a>