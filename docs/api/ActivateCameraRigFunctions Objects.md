## ActivateCameraRigFunctions Objects

```python
class ActivateCameraRigFunctions(BlueprintFunctionLibrary)
```

Blueprint functions for activating camera rigs in the base/global/visual layers.

These camera rigs run with a global, shared evaluation context that doesn't provide any
meaningful initial result. They are activated on the camera system found to be running
on the given player controller.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: ActivateCameraRigFunctions.h

<a id="unreal.ActivateCameraRigFunctions.activate_persistent_visual_camera_rig"></a>

#### activate\_persistent\_visual\_camera\_rig

```python
@classmethod
def activate_persistent_visual_camera_rig(cls, world_context_object: Object,
                                          player_controller: PlayerController,
                                          camera_rig: CameraRigAsset) -> None
```

X.activate_persistent_visual_camera_rig(world_context_object, player_controller, camera_rig) -> None
Activates the given camera rig prefab in the visual layer.

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    camera_rig (CameraRigAsset):

<a id="unreal.ActivateCameraRigFunctions.activate_visual_camera_rig"></a>

#### activate\_visual\_camera\_rig

```python
@classmethod
def activate_visual_camera_rig(cls, world_context_object: Object,
                               player_controller: PlayerController,
                               camera_rig: CameraRigAsset) -> None
```

deprecated: 'activate_visual_camera_rig' was renamed to 'activate_persistent_visual_camera_rig'.

<a id="unreal.ActivateCameraRigFunctions.activate_persistent_global_camera_rig"></a>

#### activate\_persistent\_global\_camera\_rig

```python
@classmethod
def activate_persistent_global_camera_rig(cls, world_context_object: Object,
                                          player_controller: PlayerController,
                                          camera_rig: CameraRigAsset) -> None
```

X.activate_persistent_global_camera_rig(world_context_object, player_controller, camera_rig) -> None
Activates the given camera rig prefab in the global layer.

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    camera_rig (CameraRigAsset):

<a id="unreal.ActivateCameraRigFunctions.activate_global_camera_rig"></a>

#### activate\_global\_camera\_rig

```python
@classmethod
def activate_global_camera_rig(cls, world_context_object: Object,
                               player_controller: PlayerController,
                               camera_rig: CameraRigAsset) -> None
```

deprecated: 'activate_global_camera_rig' was renamed to 'activate_persistent_global_camera_rig'.

<a id="unreal.ActivateCameraRigFunctions.activate_persistent_base_camera_rig"></a>

#### activate\_persistent\_base\_camera\_rig

```python
@classmethod
def activate_persistent_base_camera_rig(cls, world_context_object: Object,
                                        player_controller: PlayerController,
                                        camera_rig: CameraRigAsset) -> None
```

X.activate_persistent_base_camera_rig(world_context_object, player_controller, camera_rig) -> None
Activates the given camera rig prefab in the base layer.

Args:
    world_context_object (Object): 
    player_controller (PlayerController): 
    camera_rig (CameraRigAsset):

<a id="unreal.ActivateCameraRigFunctions.activate_base_camera_rig"></a>

#### activate\_base\_camera\_rig

```python
@classmethod
def activate_base_camera_rig(cls, world_context_object: Object,
                             player_controller: PlayerController,
                             camera_rig: CameraRigAsset) -> None
```

deprecated: 'activate_base_camera_rig' was renamed to 'activate_persistent_base_camera_rig'.

<a id="unreal.BlueprintCameraPoseFunctionLibrary"></a>