## DisplayClusterWarpCameraProjectionMode Objects

```python
class DisplayClusterWarpCameraProjectionMode(EnumBase)
```

Projection mode for the camera that is used as an image source
This projection does not directly use slices from the camera image,
but calculates the camera sub-frustum used to render the sub-images of camera for a particular viewport.
Since the aspect ratio of the AABB geometry in the viewport cannot be equal
to the aspect ratio of the camera, we must use several methods to fit the camera to the geometry.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterWarp
- **File**: DisplayClusterWarpBlueprint_Enums.h

<a id="unreal.DisplayClusterWarpCameraProjectionMode.FIT"></a>

#### FIT

0: Fit the stage geometry entirely within the camera's frustum

<a id="unreal.DisplayClusterWarpCameraProjectionMode.FILL"></a>

#### FILL

1: Fill the camera's frustum entire with the stage geometry

<a id="unreal.DisplayClusterWarpCameraViewTarget"></a>