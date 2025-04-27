## AISense_Touch Objects

```python
class AISense_Touch(AISense)
```

AISense Touch

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Touch.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense_Touch.report_touch_event"></a>

#### report_touch_event

```python
@classmethod
def report_touch_event(cls, world_context_object: Object,
                       touch_receiver: Actor, other_actor: Actor,
                       location: Vector) -> None
```

X.report_touch_event(world_context_object, touch_receiver, other_actor, location) -> None
Report Touch Event

Args:
    world_context_object (Object): 
    touch_receiver (Actor): 
    other_actor (Actor): 
    location (Vector):

<a id="unreal.PawnSensingComponent"></a>