## DisplayClusterProjectionBlueprintAPI Objects

```python
class DisplayClusterProjectionBlueprintAPI(Interface)
```

Display Cluster Projection Blueprint API

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterProjection
- **File**: IDisplayClusterProjectionBlueprintAPI.h

<a id="unreal.DisplayClusterProjectionBlueprintAPI.camera_policy_set_camera"></a>

#### camera_policy_set_camera

```python
def camera_policy_set_camera(viewport_id: str,
                             new_camera: CameraComponent,
                             fov_multiplier: float = 1.000000) -> None
```

x.camera_policy_set_camera(viewport_id, new_camera, fov_multiplier=1.000000) -> None
Camera Policy Set Camera
deprecated: This function is now available in the main blueprint functions list under 'nDisplay' section.

Args:
    viewport_id (str): 
    new_camera (CameraComponent): 
    fov_multiplier (float):

<a id="unreal.DisplayClusterInFrustumFitCameraComponent"></a>