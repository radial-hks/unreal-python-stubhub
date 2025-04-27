## DisplayClusterProjectionBlueprintLib Objects

```python
class DisplayClusterProjectionBlueprintLib(BlueprintFunctionLibrary)
```

Blueprint API function library

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterProjection
- **File**: DisplayClusterProjectionBlueprintLib.h

<a id="unreal.DisplayClusterProjectionBlueprintLib.get_api"></a>

#### get_api

```python
@classmethod
def get_api(cls) -> DisplayClusterProjectionBlueprintAPI
```

X.get_api() -> DisplayClusterProjectionBlueprintAPI
Get API
deprecated: GetAPI has been deprecated. All functions are now available in the main blueprint functions list under 'nDisplay' category.

Returns:
    DisplayClusterProjectionBlueprintAPI: 

    out_api (DisplayClusterProjectionBlueprintAPI):

<a id="unreal.DisplayClusterProjectionBlueprintLib.camera_policy_set_camera"></a>

#### camera_policy_set_camera

```python
@classmethod
def camera_policy_set_camera(cls,
                             viewport_id: str,
                             new_camera: CameraComponent,
                             fov_multiplier: float = 1.000000) -> None
```

X.camera_policy_set_camera(viewport_id, new_camera, fov_multiplier=1.000000) -> None
Sets camera up for 'camera' projection policy.

Args:
    viewport_id (str): 
    new_camera (CameraComponent): 
    fov_multiplier (float):

<a id="unreal.DisplayClusterProjectionBlueprintAPI"></a>