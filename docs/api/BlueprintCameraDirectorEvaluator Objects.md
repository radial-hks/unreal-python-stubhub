## BlueprintCameraDirectorEvaluator Objects

```python
class BlueprintCameraDirectorEvaluator(Object)
```

Base class for a Blueprint camera director evaluator.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraDirector.h

<a id="unreal.BlueprintCameraDirectorEvaluator.set_initial_context_camera_pose"></a>

#### set_initial_context_camera_pose

```python
def set_initial_context_camera_pose(camera_pose: BlueprintCameraPose) -> None
```

x.set_initial_context_camera_pose(camera_pose) -> None
Sets the initial evaluation context camera pose.
WARNING: this will change the initial pose of ALL running camera rigs!

Args:
    camera_pose (BlueprintCameraPose):

<a id="unreal.BlueprintCameraDirectorEvaluator.run_camera_director"></a>

#### run_camera_director

```python
def run_camera_director(
        params: BlueprintCameraDirectorEvaluationParams) -> None
```

x.run_camera_director(params) -> None
Override this method in Blueprint to execute the custom logic that determines
what camera rig(s) should be active every frame.

Args:
    params (BlueprintCameraDirectorEvaluationParams):

<a id="unreal.BlueprintCameraDirectorEvaluator.get_initial_context_variable_table"></a>

#### get_initial_context_variable_table

```python
def get_initial_context_variable_table() -> BlueprintCameraVariableTable
```

x.get_initial_context_variable_table() -> BlueprintCameraVariableTable
Gets the initial evaluation context camera variable table.
WARNING: setting variables here will affect ALL running camera rigs!

Returns:
    BlueprintCameraVariableTable:

<a id="unreal.BlueprintCameraDirectorEvaluator.get_initial_context_camera_pose"></a>

#### get_initial_context_camera_pose

```python
def get_initial_context_camera_pose() -> BlueprintCameraPose
```

x.get_initial_context_camera_pose() -> BlueprintCameraPose
Gets the initial evaluation context camera pose.

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraDirectorEvaluator.get_camera_rig"></a>

#### get_camera_rig

```python
def get_camera_rig(camera_rig: CameraRigAsset) -> CameraRigAsset
```

x.get_camera_rig(camera_rig) -> CameraRigAsset
Gets a camera rig from the referencing camera asset.

Args:
    camera_rig (CameraRigAsset): 

Returns:
    CameraRigAsset:

<a id="unreal.BlueprintCameraDirectorEvaluator.find_evaluation_context_owner_actor"></a>

#### find_evaluation_context_owner_actor

```python
def find_evaluation_context_owner_actor(actor_class: Class) -> Actor
```

x.find_evaluation_context_owner_actor(actor_class) -> Actor
A utility function that tries to find if an actor owns the evaluation context.
Handles the situation where the evaluation context is an actor component (like a
UGameplayCameraComponent) or an actor itself.

Args:
    actor_class (type(Class)): 

Returns:
    Actor:

<a id="unreal.BlueprintCameraDirectorEvaluator.deactivate_persistent_visual_camera_rig"></a>

#### deactivate_persistent_visual_camera_rig

```python
def deactivate_persistent_visual_camera_rig(
        camera_rig_prefab: CameraRigAsset) -> None
```

x.deactivate_persistent_visual_camera_rig(camera_rig_prefab) -> None
Deactivates the given camera rig prefab in the visual layer.

Args:
    camera_rig_prefab (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.deactivate_persistent_global_camera_rig"></a>

#### deactivate_persistent_global_camera_rig

```python
def deactivate_persistent_global_camera_rig(
        camera_rig_prefab: CameraRigAsset) -> None
```

x.deactivate_persistent_global_camera_rig(camera_rig_prefab) -> None
Deactivates the given camera rig prefab in the global layer.

Args:
    camera_rig_prefab (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.deactivate_persistent_base_camera_rig"></a>

#### deactivate_persistent_base_camera_rig

```python
def deactivate_persistent_base_camera_rig(
        camera_rig_prefab: CameraRigAsset) -> None
```

x.deactivate_persistent_base_camera_rig(camera_rig_prefab) -> None
Deactivates the given camera rig prefab in the base layer.

Args:
    camera_rig_prefab (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.deactivate_camera_director"></a>

#### deactivate_camera_director

```python
def deactivate_camera_director(
        params: BlueprintCameraDirectorDeactivateParams) -> None
```

x.deactivate_camera_director(params) -> None
Override this method in Blueprint to execute custom logic when this
camera director gets deactivated.

Args:
    params (BlueprintCameraDirectorDeactivateParams):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_persistent_visual_camera_rig"></a>

#### activate_persistent_visual_camera_rig

```python
def activate_persistent_visual_camera_rig(
        camera_rig_prefab: CameraRigAsset) -> None
```

x.activate_persistent_visual_camera_rig(camera_rig_prefab) -> None
Activates the given camera rig prefab in the visual layer.

Args:
    camera_rig_prefab (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_persistent_global_camera_rig"></a>

#### activate_persistent_global_camera_rig

```python
def activate_persistent_global_camera_rig(
        camera_rig_prefab: CameraRigAsset) -> None
```

x.activate_persistent_global_camera_rig(camera_rig_prefab) -> None
Activates the given camera rig prefab in the global layer.

Args:
    camera_rig_prefab (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_persistent_base_camera_rig"></a>

#### activate_persistent_base_camera_rig

```python
def activate_persistent_base_camera_rig(
        camera_rig_prefab: CameraRigAsset) -> None
```

x.activate_persistent_base_camera_rig(camera_rig_prefab) -> None
Activates the given camera rig prefab in the base layer.

Args:
    camera_rig_prefab (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_camera_rig_via_proxy"></a>

#### activate_camera_rig_via_proxy

```python
def activate_camera_rig_via_proxy(
        camera_rig_proxy: CameraRigProxyAsset) -> None
```

x.activate_camera_rig_via_proxy(camera_rig_proxy) -> None
Specifies a camera rig to be active this frame, via a proxy which is later resolved
via the proxy table of the Blueprint camera director.

Args:
    camera_rig_proxy (CameraRigProxyAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_camera_rig_prefab"></a>

#### activate_camera_rig_prefab

```python
def activate_camera_rig_prefab(camera_rig: CameraRigAsset) -> None
```

x.activate_camera_rig_prefab(camera_rig) -> None
Specifies an external camera rig prefab asset to be active this frame.

Args:
    camera_rig (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_camera_rig"></a>

#### activate_camera_rig

```python
def activate_camera_rig(camera_rig: CameraRigAsset) -> None
```

x.activate_camera_rig(camera_rig) -> None
Specifies a camera rig to be active this frame.

Args:
    camera_rig (CameraRigAsset):

<a id="unreal.BlueprintCameraDirectorEvaluator.activate_camera_director"></a>

#### activate_camera_director

```python
def activate_camera_director(
        params: BlueprintCameraDirectorActivateParams) -> None
```

x.activate_camera_director(params) -> None
Override this method in Blueprint to execute custom logic when this
camera director gets activated.

Args:
    params (BlueprintCameraDirectorActivateParams):

<a id="unreal.CameraDirectorStateTreeSchema"></a>