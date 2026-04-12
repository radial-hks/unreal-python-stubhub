## ZoneGraphDisturbanceAnnotationBPLibrary Objects

```python
class ZoneGraphDisturbanceAnnotationBPLibrary(BlueprintFunctionLibrary)
```

Set of utilities for dealing with Disturbance Annotation.

**C++ Source:**

- **Plugin**: ZoneGraphAnnotations
- **Module**: ZoneGraphAnnotations
- **File**: ZoneGraphDisturbanceAnnotationBPLibrary.h

<a id="unreal.ZoneGraphDisturbanceAnnotationBPLibrary.trigger_danger"></a>

#### trigger\_danger

```python
@classmethod
def trigger_danger(cls, world_context_object: Object, instigator: Actor,
                   position: Vector, radius: float, duration: float) -> None
```

X.trigger_danger(world_context_object, instigator, position, radius, duration) -> None
* Triggers Danger event at specific location.
*

Args:
    world_context_object (Object): 
    instigator (Actor): (optional) identifies this event coming from specific Instigator, only one danger will persist per instigator. *
    position (Vector): Position of the danger. *
    radius (float): Radius of the danger. *
    duration (float): Duration of the danger.

<a id="unreal.ZoneGraphFleeBehaviorBPLibrary"></a>