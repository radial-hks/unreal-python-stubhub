## TurnBasedLibrary Objects

```python
class TurnBasedLibrary(BlueprintFunctionLibrary)
```

Library of synchronous achievement calls

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: TurnBasedBlueprintLibrary.h

<a id="unreal.TurnBasedLibrary.register_turn_based_match_interface_object"></a>

#### register_turn_based_match_interface_object

```python
@classmethod
def register_turn_based_match_interface_object(
        cls, world_context_object: Object, player_controller: PlayerController,
        object: Object) -> None
```

X.register_turn_based_match_interface_object(world_context_object, player_controller, object) -> None
Register Turn Based Match Interface Object

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    object (Object):

<a id="unreal.TurnBasedLibrary.get_player_display_name"></a>

#### get_player_display_name

```python
@classmethod
def get_player_display_name(cls, world_context_object: Object,
                            player_controller: PlayerController, match_id: str,
                            player_index: int) -> str
```

X.get_player_display_name(world_context_object, player_controller, match_id, player_index) -> str
out

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    match_id (str): 
    player_index (int32): 

Returns:
    str: 

    player_display_name (str):

<a id="unreal.TurnBasedLibrary.get_my_player_index"></a>

#### get_my_player_index

```python
@classmethod
def get_my_player_index(cls, world_context_object: Object,
                        player_controller: PlayerController,
                        match_id: str) -> int
```

X.get_my_player_index(world_context_object, player_controller, match_id) -> int32
out

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    match_id (str): 

Returns:
    int32: 

    player_index (int32):

<a id="unreal.TurnBasedLibrary.get_is_my_turn"></a>

#### get_is_my_turn

```python
@classmethod
def get_is_my_turn(cls, world_context_object: Object,
                   player_controller: PlayerController, match_id: str) -> bool
```

X.get_is_my_turn(world_context_object, player_controller, match_id) -> bool
out

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    match_id (str): 

Returns:
    bool: 

    is_my_turn (bool):

<a id="unreal.VoipListenerSynthComponent"></a>