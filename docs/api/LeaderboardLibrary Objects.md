## LeaderboardLibrary Objects

```python
class LeaderboardLibrary(BlueprintFunctionLibrary)
```

A beacon host used for taking reservations for an existing game session

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: LeaderboardBlueprintLibrary.h

<a id="unreal.LeaderboardLibrary.write_leaderboard_integer"></a>

#### write_leaderboard_integer

```python
@classmethod
def write_leaderboard_integer(cls, player_controller: PlayerController,
                              stat_name: Name, stat_value: int) -> bool
```

X.write_leaderboard_integer(player_controller, stat_name, stat_value) -> bool
Writes an integer value to the specified leaderboard

Args:
    player_controller (PlayerController): 
    stat_name (Name): 
    stat_value (int32): 

Returns:
    bool:

<a id="unreal.LeaderboardFlushCallbackProxy"></a>