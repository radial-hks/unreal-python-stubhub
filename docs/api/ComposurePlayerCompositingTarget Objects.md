## ComposurePlayerCompositingTarget Objects

```python
class ComposurePlayerCompositingTarget(Object)
```

Object to bind to a APlayerCameraManager with a UTextureRenderTarget2D to be used as a player's render target.
TODO-BADGER:: deprecate this (UComposurePlayerCompositingTarget) once we're comfortable using the new UComposureCompositingTargetComponent in its place

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposurePlayerCompositingTarget.h

<a id="unreal.ComposurePlayerCompositingTarget.set_render_target"></a>

#### set_render_target

```python
def set_render_target(render_target: TextureRenderTarget2D) -> None
```

x.set_render_target(render_target) -> None
Set the render target of the player.

Args:
    render_target (TextureRenderTarget2D):

<a id="unreal.ComposurePlayerCompositingTarget.set_player_camera_manager"></a>

#### set_player_camera_manager

```python
def set_player_camera_manager(
        player_camera_manager: PlayerCameraManager) -> PlayerCameraManager
```

x.set_player_camera_manager(player_camera_manager) -> PlayerCameraManager
Set player camera manager to bind the render target to.

Args:
    player_camera_manager (PlayerCameraManager): 

Returns:
    PlayerCameraManager:

<a id="unreal.ComposurePlayerCompositingTarget.get_player_camera_manager"></a>

#### get_player_camera_manager

```python
def get_player_camera_manager() -> PlayerCameraManager
```

x.get_player_camera_manager() -> PlayerCameraManager
Current player camera manager the target is bind on.

Returns:
    PlayerCameraManager:

<a id="unreal.ComposureCompositingTargetComponent"></a>