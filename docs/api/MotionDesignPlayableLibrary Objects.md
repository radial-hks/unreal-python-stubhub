## MotionDesignPlayableLibrary Objects

```python
class MotionDesignPlayableLibrary(BlueprintFunctionLibrary)
```

Ava Playable Library

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaPlayableLibrary.h

<a id="unreal.MotionDesignPlayableLibrary.update_playable_remote_control_values"></a>

#### update_playable_remote_control_values

```python
@classmethod
def update_playable_remote_control_values(
        cls, world_context_object: Object) -> bool
```

X.update_playable_remote_control_values(world_context_object) -> bool
Injects the remote control values from current transition for the current playable.
remark: This does nothing if there is no current transition the current playable is part of or if the current level is not managed by a playable.

Args:
    world_context_object (Object): 

Returns:
    bool: true if the values have been injected, false otherwise.

<a id="unreal.MotionDesignPlayableLibrary.set_playable_hidden"></a>

#### set_playable_hidden

```python
@classmethod
def set_playable_hidden(cls, world_context_object: Object,
                        should_be_hidden: bool) -> bool
```

X.set_playable_hidden(world_context_object, should_be_hidden) -> bool
Sets the hidden state of all primitives under this playable. Hidden primitives will not be rendered.
remark: This only works if current level is managed by a playable (i.e. in a rundown or playback graph).

Args:
    world_context_object (Object): 
    should_be_hidden (bool): 

Returns:
    bool: true if the value was set, false otherwise (if not managed by a playable).

<a id="unreal.MotionDesignPlayableLibrary.is_playable_hidden"></a>

#### is_playable_hidden

```python
@classmethod
def is_playable_hidden(cls, world_context_object: Object) -> bool
```

X.is_playable_hidden(world_context_object) -> bool
Returns the current hidden state of this playable.
remark: This only works if current level is managed by a playable (i.e. in a rundown or playback graph).

Args:
    world_context_object (Object): 

Returns:
    bool: true if the hidden state is set, false otherwise or if not managed by a playable.

<a id="unreal.AvaPlayableRemoteProxy"></a>