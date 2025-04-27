## CheatManager Objects

```python
class CheatManager(Object)
```

Cheat Manager is a central blueprint to implement test and debug code and actions that are not to ship with the game.
As the Cheat Manager is not instanced in shipping builds, it is for debugging purposes only

**C++ Source:**

- **Module**: Engine
- **File**: CheatManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_camera_controller_class`` (type(Class)):  [Read-Write] Debug camera - used to have independent camera without stopping gameplay

<a id="unreal.CheatManager.debug_camera_controller_class"></a>

#### debug_camera_controller_class

```python
@property
def debug_camera_controller_class() -> Class
```

(type(Class)):  [Read-Only] Debug camera - used to have independent camera without stopping gameplay

<a id="unreal.CheatManager.walk"></a>

#### walk

```python
def walk() -> None
```

x.walk() -> None
Return to walking movement mode from Fly or Ghost cheat.

<a id="unreal.CheatManager.teleport"></a>

#### teleport

```python
def teleport() -> None
```

x.teleport() -> None
Teleport to surface player is looking at.

<a id="unreal.CheatManager.slomo"></a>

#### slomo

```python
def slomo(new_time_dilation: float) -> None
```

x.slomo(new_time_dilation) -> None
Modify time dilation to change apparent speed of passage of time. e.g. "Slomo 0.1" makes everything move very slowly, while "Slomo 10" makes everything move very fast.

Args:
    new_time_dilation (float):

<a id="unreal.CheatManager.receive_init_cheat_manager"></a>

#### receive_init_cheat_manager

```python
def receive_init_cheat_manager() -> None
```

x.receive_init_cheat_manager() -> None
BP implementable event for when CheatManager is created to allow any needed initialization.

<a id="unreal.CheatManager.receive_end_play"></a>

#### receive_end_play

```python
def receive_end_play() -> None
```

x.receive_end_play() -> None
This is the End Play event for the CheatManager

<a id="unreal.CheatManager.players_only"></a>

#### players_only

```python
def players_only() -> None
```

x.players_only() -> None
Freeze everything in the level except for players.

<a id="unreal.CheatManager.god"></a>

#### god

```python
def god() -> None
```

x.god() -> None
Invulnerability cheat.

<a id="unreal.CheatManager.ghost"></a>

#### ghost

```python
def ghost() -> None
```

x.ghost() -> None
Pawn no longer collides with the world, and can fly

<a id="unreal.CheatManager.get_player_controller"></a>

#### get_player_controller

```python
def get_player_controller() -> PlayerController
```

x.get_player_controller() -> PlayerController
Get Player Controller

Returns:
    PlayerController:

<a id="unreal.CheatManager.freeze_frame"></a>

#### freeze_frame

```python
def freeze_frame(delay: float) -> None
```

x.freeze_frame(delay) -> None
Pause the game for Delay seconds.

Args:
    delay (float):

<a id="unreal.CheatManager.fly"></a>

#### fly

```python
def fly() -> None
```

x.fly() -> None
Pawn can fly.

<a id="unreal.CheatManager.enable_debug_camera"></a>

#### enable_debug_camera

```python
def enable_debug_camera() -> None
```

x.enable_debug_camera() -> None
Switch controller to debug camera without locking gameplay and with locking local player controller input

<a id="unreal.CheatManager.disable_debug_camera"></a>

#### disable_debug_camera

```python
def disable_debug_camera() -> None
```

x.disable_debug_camera() -> None
Switch controller from debug camera back to normal controller

<a id="unreal.CheatManager.destroy_target"></a>

#### destroy_target

```python
def destroy_target() -> None
```

x.destroy_target() -> None
Destroy the actor you're looking at.

<a id="unreal.CheatManager.damage_target"></a>

#### damage_target

```python
def damage_target(damage_amount: float) -> None
```

x.damage_target(damage_amount) -> None
Damage the actor you're looking at (sourced from the player).

Args:
    damage_amount (float):

<a id="unreal.CheatManager.change_size"></a>

#### change_size

```python
def change_size(f: float) -> None
```

x.change_size(f) -> None
Scale the player's size to be F * default size.

Args:
    f (float):

<a id="unreal.CheatManagerExtension"></a>