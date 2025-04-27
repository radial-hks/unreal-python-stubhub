## LensDistortionModelHandlerBase Objects

```python
class LensDistortionModelHandlerBase(Object)
```

Asset user data that can be used on Camera Actors to manage lens distortion state and utilities

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensDistortionModelHandlerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_filmback`` (CameraFilmbackSettings):  [Read-Write] Filmback settings of the camera that is being used for distortion
- ``current_state`` (LensDistortionState):  [Read-Write] Current state as set by the most recent call to Update()
- ``display_name`` (str):  [Read-Only] Display name, used to identify handler in-editor details panels
- ``distortion_post_process_mid`` (MaterialInstanceDynamic):  [Read-Only] Dynamically created post-process material instance for the currently specified lens model
- ``lens_model_class`` (type(Class)):  [Read-Only] Lens Model describing how to interpret the distortion parameters
- ``overscan_factor`` (float):  [Read-Only] Computed overscan factor needed to scale the camera's FOV (read-only)

<a id="unreal.LensDistortionModelHandlerBase.lens_model_class"></a>

#### lens_model_class

```python
@property
def lens_model_class() -> Class
```

(type(Class)):  [Read-Only] Lens Model describing how to interpret the distortion parameters

<a id="unreal.LensDistortionModelHandlerBase.distortion_post_process_mid"></a>

#### distortion_post_process_mid

```python
@property
def distortion_post_process_mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Only] Dynamically created post-process material instance for the currently specified lens model

<a id="unreal.LensDistortionModelHandlerBase.current_state"></a>

#### current_state

```python
@property
def current_state() -> LensDistortionState
```

(LensDistortionState):  [Read-Only] Current state as set by the most recent call to Update()

<a id="unreal.LensDistortionModelHandlerBase.camera_filmback"></a>

#### camera_filmback

```python
@property
def camera_filmback() -> CameraFilmbackSettings
```

(CameraFilmbackSettings):  [Read-Write] Filmback settings of the camera that is being used for distortion

<a id="unreal.LensDistortionModelHandlerBase.camera_filmback"></a>

#### camera_filmback

```python
@camera_filmback.setter
def camera_filmback(value: CameraFilmbackSettings) -> None
```

<a id="unreal.LensDistortionModelHandlerBase.overscan_factor"></a>

#### overscan_factor

```python
@property
def overscan_factor() -> float
```

(float):  [Read-Only] Computed overscan factor needed to scale the camera's FOV (read-only)

<a id="unreal.LensDistortionModelHandlerBase.set_distortion_state"></a>

#### set_distortion_state

```python
def set_distortion_state(new_state: LensDistortionState) -> None
```

x.set_distortion_state(new_state) -> None
Update the lens distortion state, recompute the overscan factor, and set all material parameters

Args:
    new_state (LensDistortionState):

<a id="unreal.LensDistortionModelHandlerBase.is_model_supported"></a>

#### is_model_supported

```python
def is_model_supported(model_to_support: Class) -> bool
```

x.is_model_supported(model_to_support) -> bool
Returns true if the input model is supported by this model handler, false otherwise.

Args:
    model_to_support (type(Class)): 

Returns:
    bool:

<a id="unreal.LensDistortionModelHandlerBase.get_undistortion_displacement_map"></a>

#### get_undistortion_displacement_map

```python
def get_undistortion_displacement_map() -> TextureRenderTarget2D
```

x.get_undistortion_displacement_map() -> TextureRenderTarget2D
Get the UV displacement map used to undistort a distorted image

Returns:
    TextureRenderTarget2D:

<a id="unreal.LensDistortionModelHandlerBase.get_distortion_displacement_map"></a>

#### get_distortion_displacement_map

```python
def get_distortion_displacement_map() -> TextureRenderTarget2D
```

x.get_distortion_displacement_map() -> TextureRenderTarget2D
Get the UV displacement map used to distort an undistorted image

Returns:
    TextureRenderTarget2D:

<a id="unreal.AnamorphicLensDistortionModelHandler"></a>