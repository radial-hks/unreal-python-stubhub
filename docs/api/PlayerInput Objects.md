## PlayerInput Objects

```python
class PlayerInput(Object)
```

Object within PlayerController that processes player input.
Only exists on the client in network games.
see: https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

**C++ Source:**

- **Module**: Engine
- **File**: PlayerInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_exec_bindings`` (Array[KeyBind]):  [Read-Write] Generic bindings of keys to Exec()-compatible strings for development purposes only
- ``inverted_axis`` (Array[Name]):  [Read-Write] List of Axis Mappings that have been inverted

<a id="unreal.PlayerInput.get_outer_a_player_controller"></a>

#### get_outer_a_player_controller

```python
def get_outer_a_player_controller() -> PlayerController
```

x.get_outer_a_player_controller() -> PlayerController
Return's this object casted to a player controller. This can be null if there is no player controller.

Returns:
    PlayerController:

<a id="unreal.VectorFieldVolume"></a>