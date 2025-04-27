## TurnBasedMatchInterface Objects

```python
class TurnBasedMatchInterface(Interface)
```

Turn Based Match Interface

**C++ Source:**

- **Plugin**: OnlineSubsystem
- **Module**: OnlineSubsystem
- **File**: TurnBasedMatchInterface.h

<a id="unreal.TurnBasedMatchInterface.on_match_received_turn"></a>

#### on_match_received_turn

```python
def on_match_received_turn(match: str, did_become_active: bool) -> None
```

x.on_match_received_turn(match, did_become_active) -> None
On Match Received Turn

Args:
    match (str): 
    did_become_active (bool):

<a id="unreal.TurnBasedMatchInterface.on_match_ended"></a>

#### on_match_ended

```python
def on_match_ended(match: str) -> None
```

x.on_match_ended(match) -> None
On Match Ended

Args:
    match (str):

<a id="unreal.AchievementLibrary"></a>