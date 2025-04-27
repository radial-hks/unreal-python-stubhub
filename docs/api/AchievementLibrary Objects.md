## AchievementLibrary Objects

```python
class AchievementLibrary(BlueprintFunctionLibrary)
```

Library of synchronous achievement calls

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: AchievementBlueprintLibrary.h

<a id="unreal.AchievementLibrary.get_cached_achievement_progress"></a>

#### get_cached_achievement_progress

```python
@classmethod
def get_cached_achievement_progress(
        cls, world_context_object: Object, player_controller: PlayerController,
        achievement_id: Name) -> Tuple[bool, float]
```

X.get_cached_achievement_progress(world_context_object, player_controller, achievement_id) -> (found_id=bool, progress=float)
out

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    achievement_id (Name): 

Returns:
    tuple: 

    found_id (bool): 

    progress (float):

<a id="unreal.AchievementLibrary.get_cached_achievement_description"></a>

#### get_cached_achievement_description

```python
@classmethod
def get_cached_achievement_description(
        cls, world_context_object: Object, player_controller: PlayerController,
        achievement_id: Name) -> Tuple[bool, Text, Text, Text, bool]
```

X.get_cached_achievement_description(world_context_object, player_controller, achievement_id) -> (found_id=bool, title=Text, locked_description=Text, unlocked_description=Text, hidden=bool)
out

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    achievement_id (Name): 

Returns:
    tuple: 

    found_id (bool): 

    title (Text): 

    locked_description (Text): 

    unlocked_description (Text): 

    hidden (bool):

<a id="unreal.OnlineBlueprintCallProxyBase"></a>