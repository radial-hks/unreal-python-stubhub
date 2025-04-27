## DaySequenceStaticTimeContributor Objects

```python
class DaySequenceStaticTimeContributor(Object)
```

A Blueprint exposed static time contributor.
Used to contribute to static time blending for the specified Day Sequence Actor without needing to spawn actors and/or components.

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceStaticTime.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] The desired blend weight. Once bound to a Day Sequence Actor, this can be freely changed without rebinding.
- ``static_time`` (float):  [Read-Write] The desired static time. Once bound to a Day Sequence Actor, this can be freely changed without rebinding.
- ``wants_static_time`` (bool):  [Read-Write] Determines whether or not this contributor is effective once we are bound. This can be freely changed to enable/disable the contributor without rebinding.

<a id="unreal.DaySequenceStaticTimeContributor.blend_weight"></a>

#### blend_weight

```python
@property
def blend_weight() -> float
```

(float):  [Read-Write] The desired blend weight. Once bound to a Day Sequence Actor, this can be freely changed without rebinding.

<a id="unreal.DaySequenceStaticTimeContributor.blend_weight"></a>

#### blend_weight

```python
@blend_weight.setter
def blend_weight(value: float) -> None
```

<a id="unreal.DaySequenceStaticTimeContributor.static_time"></a>

#### static_time

```python
@property
def static_time() -> float
```

(float):  [Read-Write] The desired static time. Once bound to a Day Sequence Actor, this can be freely changed without rebinding.

<a id="unreal.DaySequenceStaticTimeContributor.static_time"></a>

#### static_time

```python
@static_time.setter
def static_time(value: float) -> None
```

<a id="unreal.DaySequenceStaticTimeContributor.wants_static_time"></a>

#### wants_static_time

```python
@property
def wants_static_time() -> bool
```

(bool):  [Read-Write] Determines whether or not this contributor is effective once we are bound. This can be freely changed to enable/disable the contributor without rebinding.

<a id="unreal.DaySequenceStaticTimeContributor.wants_static_time"></a>

#### wants_static_time

```python
@wants_static_time.setter
def wants_static_time(value: bool) -> None
```

<a id="unreal.DaySequenceStaticTimeContributor.unbind_from_day_sequence_actor"></a>

#### unbind_from_day_sequence_actor

```python
def unbind_from_day_sequence_actor() -> None
```

x.unbind_from_day_sequence_actor() -> None
Stop contributing static time.

<a id="unreal.DaySequenceStaticTimeContributor.bind_to_day_sequence_actor"></a>

#### bind_to_day_sequence_actor

```python
def bind_to_day_sequence_actor(target_actor: DaySequenceActor,
                               priority: int = 1000) -> None
```

x.bind_to_day_sequence_actor(target_actor, priority=1000) -> None
Begin contributing static time to the specified actor.

Args:
    target_actor (DaySequenceActor): 
    priority (int32):

<a id="unreal.ProceduralDaySequenceBuilder"></a>