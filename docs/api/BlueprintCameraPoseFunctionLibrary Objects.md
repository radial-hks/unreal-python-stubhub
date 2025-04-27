## BlueprintCameraPoseFunctionLibrary Objects

```python
class BlueprintCameraPoseFunctionLibrary(BlueprintFunctionLibrary)
```

Utility Blueprint functions for camera poses.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraPose.h

<a id="unreal.BlueprintCameraPoseFunctionLibrary.set_transform"></a>

#### set_transform

```python
@classmethod
def set_transform(cls, camera_pose: BlueprintCameraPose,
                  transform: Transform) -> BlueprintCameraPose
```

X.set_transform(camera_pose, transform) -> BlueprintCameraPose
Creates a copy of the given camera pose with the given location and rotation.

Args:
    camera_pose (BlueprintCameraPose): 
    transform (Transform): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.set_target_distance"></a>

#### set_target_distance

```python
@classmethod
def set_target_distance(cls, camera_pose: BlueprintCameraPose,
                        target_distance: float) -> BlueprintCameraPose
```

X.set_target_distance(camera_pose, target_distance) -> BlueprintCameraPose
Creates a copy of the given camera pose with the given target distance.

Args:
    camera_pose (BlueprintCameraPose): 
    target_distance (double): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.set_rotation"></a>

#### set_rotation

```python
@classmethod
def set_rotation(cls, camera_pose: BlueprintCameraPose,
                 rotation: Rotator) -> BlueprintCameraPose
```

X.set_rotation(camera_pose, rotation) -> BlueprintCameraPose
Creates a copy of the given camera pose with the given rotation.

Args:
    camera_pose (BlueprintCameraPose): 
    rotation (Rotator): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.set_location"></a>

#### set_location

```python
@classmethod
def set_location(cls, camera_pose: BlueprintCameraPose,
                 location: Vector) -> BlueprintCameraPose
```

X.set_location(camera_pose, location) -> BlueprintCameraPose
Creates a copy of the given camera pose with the given location.

Args:
    camera_pose (BlueprintCameraPose): 
    location (Vector): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.set_focal_length"></a>

#### set_focal_length

```python
@classmethod
def set_focal_length(cls, camera_pose: BlueprintCameraPose,
                     focal_length: float) -> BlueprintCameraPose
```

X.set_focal_length(camera_pose, focal_length) -> BlueprintCameraPose
Creates a copy of the given camera pose with the given focal length.

Args:
    camera_pose (BlueprintCameraPose): 
    focal_length (float): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.set_field_of_view"></a>

#### set_field_of_view

```python
@classmethod
def set_field_of_view(cls, camera_pose: BlueprintCameraPose,
                      field_of_view: float) -> BlueprintCameraPose
```

X.set_field_of_view(camera_pose, field_of_view) -> BlueprintCameraPose
Creates a copy of the given camera pose with the given field of view.

Args:
    camera_pose (BlueprintCameraPose): 
    field_of_view (float): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.make_camera_pose_from_cine_camera_component"></a>

#### make_camera_pose_from_cine_camera_component

```python
@classmethod
def make_camera_pose_from_cine_camera_component(
        cls, camera_component: CineCameraComponent) -> BlueprintCameraPose
```

X.make_camera_pose_from_cine_camera_component(camera_component) -> BlueprintCameraPose
Creates a new camera pose given a cine-camera component.

Args:
    camera_component (CineCameraComponent): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.make_camera_pose_from_camera_component"></a>

#### make_camera_pose_from_camera_component

```python
@classmethod
def make_camera_pose_from_camera_component(
        cls, camera_component: CameraComponent) -> BlueprintCameraPose
```

X.make_camera_pose_from_camera_component(camera_component) -> BlueprintCameraPose
Creates a new camera pose given a camera component.

Args:
    camera_component (CameraComponent): 

Returns:
    BlueprintCameraPose:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_transform"></a>

#### get_transform

```python
@classmethod
def get_transform(cls, camera_pose: BlueprintCameraPose) -> Transform
```

X.get_transform(camera_pose) -> Transform
Gets the transform matrix of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    Transform:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_target_distance"></a>

#### get_target_distance

```python
@classmethod
def get_target_distance(cls, camera_pose: BlueprintCameraPose) -> float
```

X.get_target_distance(camera_pose) -> double
Gets the target distance of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    double:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_target_at_distance"></a>

#### get_target_at_distance

```python
@classmethod
def get_target_at_distance(cls, camera_pose: BlueprintCameraPose,
                           target_distance: float) -> Vector
```

X.get_target_at_distance(camera_pose, target_distance) -> Vector
Gets the target of the camera pose given a specific target distance.

Args:
    camera_pose (BlueprintCameraPose): 
    target_distance (double): 

Returns:
    Vector:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_target"></a>

#### get_target

```python
@classmethod
def get_target(cls, camera_pose: BlueprintCameraPose) -> Vector
```

X.get_target(camera_pose) -> Vector
Gets the target of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    Vector:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_sensor_aspect_ratio"></a>

#### get_sensor_aspect_ratio

```python
@classmethod
def get_sensor_aspect_ratio(cls, camera_pose: BlueprintCameraPose) -> float
```

X.get_sensor_aspect_ratio(camera_pose) -> double
Gets the effective aspect ratio of the camera pose, computed from the sensor size.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    double:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_rotation"></a>

#### get_rotation

```python
@classmethod
def get_rotation(cls, camera_pose: BlueprintCameraPose) -> Rotator
```

X.get_rotation(camera_pose) -> Rotator
Gets the rotation of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    Rotator:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_location"></a>

#### get_location

```python
@classmethod
def get_location(cls, camera_pose: BlueprintCameraPose) -> Vector
```

X.get_location(camera_pose) -> Vector
Gets the location of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    Vector:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_focal_length"></a>

#### get_focal_length

```python
@classmethod
def get_focal_length(cls, camera_pose: BlueprintCameraPose) -> float
```

X.get_focal_length(camera_pose) -> double
Gets the focal length of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    double:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_field_of_view"></a>

#### get_field_of_view

```python
@classmethod
def get_field_of_view(cls, camera_pose: BlueprintCameraPose) -> float
```

X.get_field_of_view(camera_pose) -> double
Gets the field of view of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    double:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_effective_field_of_view"></a>

#### get_effective_field_of_view

```python
@classmethod
def get_effective_field_of_view(cls,
                                camera_pose: BlueprintCameraPose) -> float
```

X.get_effective_field_of_view(camera_pose) -> double
Gets the effective field of view of the camera pose, possibly computed from focal length.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    double:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_aim_ray"></a>

#### get_aim_ray

```python
@classmethod
def get_aim_ray(cls, camera_pose: BlueprintCameraPose) -> Ray
```

X.get_aim_ray(camera_pose) -> Ray
Gets the aim ray of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    Ray:

<a id="unreal.BlueprintCameraPoseFunctionLibrary.get_aim_dir"></a>

#### get_aim_dir

```python
@classmethod
def get_aim_dir(cls, camera_pose: BlueprintCameraPose) -> Vector
```

X.get_aim_dir(camera_pose) -> Vector
Gets the facing direction of the camera pose.

Args:
    camera_pose (BlueprintCameraPose): 

Returns:
    Vector:

<a id="unreal.BlueprintCameraVariableTableFunctionLibrary"></a>