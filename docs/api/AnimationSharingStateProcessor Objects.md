## AnimationSharingStateProcessor Objects

```python
class AnimationSharingStateProcessor(Object)
```

Animation Sharing State Processor

**C++ Source:**

- **Plugin**: AnimationSharing
- **Module**: AnimationSharing
- **File**: AnimationSharingTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation_state_enum`` (Enum):  [Read-Write]

<a id="unreal.AnimationSharingStateProcessor.process_actor_state"></a>

#### process_actor_state

```python
def process_actor_state(actor: Actor, current_state: int,
                        on_demand_state: int) -> Tuple[int, bool]
```

x.process_actor_state(actor, current_state, on_demand_state) -> (out_state=int32, should_process=bool)
Process Actor State

Args:
    actor (Actor): 
    current_state (uint8): 
    on_demand_state (uint8): 

Returns:
    tuple: 

    out_state (int32): 

    should_process (bool):

<a id="unreal.AnimationSharingStateProcessor.get_animation_state_enum"></a>

#### get_animation_state_enum

```python
def get_animation_state_enum() -> Enum
```

x.get_animation_state_enum() -> Enum
Get Animation State Enum

Returns:
    Enum:

<a id="unreal.AnimSharingStateInstance"></a>