## AISense_Damage Objects

```python
class AISense_Damage(AISense)
```

AISense Damage

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Damage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense_Damage.report_damage_event"></a>

#### report_damage_event

```python
@classmethod
def report_damage_event(cls,
                        world_context_object: Object,
                        damaged_actor: Actor,
                        instigator: Actor,
                        damage_amount: float,
                        event_location: Vector,
                        hit_location: Vector,
                        tag: Name = "None") -> None
```

X.report_damage_event(world_context_object, damaged_actor, instigator, damage_amount, event_location, hit_location, tag="None") -> None
EventLocation will be reported as Instigator's location at the moment of event happening

Args:
    world_context_object (Object): 
    damaged_actor (Actor): 
    instigator (Actor): 
    damage_amount (float): 
    event_location (Vector): 
    hit_location (Vector): 
    tag (Name):

<a id="unreal.AISense_Hearing"></a>