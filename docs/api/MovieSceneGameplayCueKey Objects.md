## MovieSceneGameplayCueKey Objects

```python
class MovieSceneGameplayCueKey(StructBase)
```

Movie Scene Gameplay Cue Key

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: MovieSceneGameplayCueSections.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ability_level`` (int32):  [Read-Write] If originating from an ability, this will be the level of that ability
- ``attach_socket_name`` (Name):  [Read-Write] When attached to a skeletal mesh component, specifies a socket to trigger the cue at
- ``attach_to_binding`` (bool):  [Read-Write] Attach the gameplay cue to the track's bound object in sequencer
- ``cue`` (GameplayCueTag):  [Read-Write]
- ``effect_causer`` (MovieSceneObjectBindingID):  [Read-Write] The physical actor that actually did the damage, can be a weapon or projectile
- ``gameplay_effect_level`` (int32):  [Read-Write] The level of that GameplayEffect
- ``instigator`` (MovieSceneObjectBindingID):  [Read-Write] Instigator actor, the actor that owns the ability system component.
- ``location`` (Vector):  [Read-Write] Location cue took place at - relative to the attached component if applicable
- ``normal`` (Vector):  [Read-Write] Normal of impact that caused cue
- ``normalized_magnitude`` (float):  [Read-Write] Magnitude of source gameplay effect, normalzed from 0-1. Use this for "how strong is the gameplay effect" (0=min, 1=,max)
- ``physical_material`` (PhysicalMaterial):  [Read-Write] PhysMat of the hit, if there was a hit.

<a id="unreal.MovieSceneGameplayCueKey.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.StateTreeReferenceOverrides"></a>