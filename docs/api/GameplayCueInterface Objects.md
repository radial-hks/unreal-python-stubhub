## GameplayCueInterface Objects

```python
class GameplayCueInterface(Interface)
```

Gameplay Cue Interface

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayCueInterface.h

<a id="unreal.GameplayCueInterface.forward_gameplay_cue_to_parent"></a>

#### forward\_gameplay\_cue\_to\_parent

```python
def forward_gameplay_cue_to_parent() -> None
```

x.forward_gameplay_cue_to_parent() -> None
Call from a Cue handler event to continue checking for additional, more generic handlers. Called from the ability system blueprint library

<a id="unreal.GameplayCueNotify_Actor"></a>