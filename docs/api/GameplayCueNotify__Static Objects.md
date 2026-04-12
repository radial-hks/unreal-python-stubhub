## GameplayCueNotify\_Static Objects

```python
class GameplayCueNotify_Static(Object)
```

A non instantiated UObject that acts as a handler for a GameplayCue. These are useful for one-off "burst" effects.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueNotify_Static.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gameplay_cue_tag`` (GameplayTag):  [Read-Write] Tag this notify is activated by
- ``is_override`` (bool):  [Read-Write] Does this Cue override other cues, or is it called in addition to them? E.g., If this is Damage.Physical.Slash, we wont call Damage.Physical afer we run this cue.

<a id="unreal.GameplayCueNotify_Static.while_active"></a>

#### while\_active

```python
def while_active(my_target: Actor, parameters: GameplayCueParameters) -> bool
```

x.while_active(my_target, parameters) -> bool
Called when a GameplayCue with duration is first seen as active, even if it wasn't actually just applied (Join in progress, etc)

Args:
    my_target (Actor): 
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.GameplayCueNotify_Static.on_remove"></a>

#### on\_remove

```python
def on_remove(my_target: Actor, parameters: GameplayCueParameters) -> bool
```

x.on_remove(my_target, parameters) -> bool
Called when a GameplayCue with duration is removed

Args:
    my_target (Actor): 
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.GameplayCueNotify_Static.on_execute"></a>

#### on\_execute

```python
def on_execute(my_target: Actor, parameters: GameplayCueParameters) -> bool
```

x.on_execute(my_target, parameters) -> bool
Called when a GameplayCue is executed, this is used for instant effects or periodic ticks

Args:
    my_target (Actor): 
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.GameplayCueNotify_Static.on_active"></a>

#### on\_active

```python
def on_active(my_target: Actor, parameters: GameplayCueParameters) -> bool
```

x.on_active(my_target, parameters) -> bool
Called when a GameplayCue with duration is first activated, this will only be called if the client witnessed the activation

Args:
    my_target (Actor): 
    parameters (GameplayCueParameters): 

Returns:
    bool:

<a id="unreal.GameplayCueNotify_Static.handle_gameplay_cue"></a>

#### handle\_gameplay\_cue

```python
def handle_gameplay_cue(my_target: Actor, event_type: GameplayCueEvent,
                        parameters: GameplayCueParameters) -> None
```

x.handle_gameplay_cue(my_target, event_type, parameters) -> None
Generic Event Graph event that will get called for every event type

Args:
    my_target (Actor): 
    event_type (GameplayCueEvent): 
    parameters (GameplayCueParameters):

<a id="unreal.GameplayCueNotify_UnitTest"></a>