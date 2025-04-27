## LocalPlayer Objects

```python
class LocalPlayer(Player)
```

Each player that is active on the current client/listen server has a LocalPlayer.
It stays active across maps, and there may be several spawned in the case of splitscreen/coop.
There will be 0 spawned on dedicated servers.

**C++ Source:**

- **Module**: Engine
- **File**: LocalPlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sent_split_join`` (bool):  [Read-Only] set when we've sent a split join request

<a id="unreal.FieldSystem"></a>