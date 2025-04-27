## DaySequenceSubsystem Objects

```python
class DaySequenceSubsystem(WorldSubsystem)
```

Day Sequence Subsystem

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_day_sequence_actor_set`` (OnDaySequenceActorSet):  [Read-Write] Blueprint exposed delegate that is broadcast when the active DaySequenceActor changes.

<a id="unreal.DaySequenceSubsystem.on_day_sequence_actor_set"></a>

#### on_day_sequence_actor_set

```python
@property
def on_day_sequence_actor_set() -> OnDaySequenceActorSet
```

(OnDaySequenceActorSet):  [Read-Write] Blueprint exposed delegate that is broadcast when the active DaySequenceActor changes.

<a id="unreal.DaySequenceSubsystem.on_day_sequence_actor_set"></a>

#### on_day_sequence_actor_set

```python
@on_day_sequence_actor_set.setter
def on_day_sequence_actor_set(value: OnDaySequenceActorSet) -> None
```

<a id="unreal.DaySequenceSubsystem.set_day_sequence_actor"></a>

#### set_day_sequence_actor

```python
def set_day_sequence_actor(actor: DaySequenceActor) -> None
```

x.set_day_sequence_actor(actor) -> None
Set Day Sequence Actor

Args:
    actor (DaySequenceActor):

<a id="unreal.DaySequenceSubsystem.get_day_sequence_actor"></a>

#### get_day_sequence_actor

```python
def get_day_sequence_actor(
        find_fallback_on_null: bool = True) -> DaySequenceActor
```

x.get_day_sequence_actor(find_fallback_on_null=True) -> DaySequenceActor
Get Day Sequence Actor

Args:
    find_fallback_on_null (bool): 

Returns:
    DaySequenceActor:

<a id="unreal.DaySequenceTrack"></a>