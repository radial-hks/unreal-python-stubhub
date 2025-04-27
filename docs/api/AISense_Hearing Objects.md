## AISense_Hearing Objects

```python
class AISense_Hearing(AISense)
```

AISense Hearing

**C++ Source:**

- **Module**: AIModule
- **File**: AISense_Hearing.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_register_all_pawns_as_sources`` (bool):  [Read-Write] If true all newly spawned pawns will get auto registered as source for this sense.
- ``notify_type`` (AISenseNotifyType):  [Read-Write]
- ``wants_new_pawn_notification`` (bool):  [Read-Write] whether this sense is interested in getting notified about new Pawns being spawned
      this can be used for example for automated sense sources registration

<a id="unreal.AISense_Hearing.report_noise_event"></a>

#### report_noise_event

```python
@classmethod
def report_noise_event(cls,
                       world_context_object: Object,
                       noise_location: Vector,
                       loudness: float = 1.000000,
                       instigator: Actor = None,
                       max_range: float = 0.000000,
                       tag: Name = "None") -> None
```

X.report_noise_event(world_context_object, noise_location, loudness=1.000000, instigator=None, max_range=0.000000, tag="None") -> None
Report a noise event.

Args:
    world_context_object (Object): 
    noise_location (Vector): Location of the noise.
    loudness (float): Loudness of the noise. If MaxRange is non-zero, modifies MaxRange, otherwise modifies the squared distance of the sensor's range.
    instigator (Actor): Actor that triggered the noise.
    max_range (float): Max range at which the sound can be heard, multiplied by Loudness. Values <= 0 mean no limit (still limited by listener's range however).
    tag (Name): Identifier for the event.

<a id="unreal.AISense_Prediction"></a>