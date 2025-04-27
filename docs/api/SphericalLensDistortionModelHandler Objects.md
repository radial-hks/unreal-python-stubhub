## SphericalLensDistortionModelHandler Objects

```python
class SphericalLensDistortionModelHandler(LensDistortionModelHandlerBase)
```

Lens distortion handler for a spherical lens model that implements the Brown-Conrady polynomial model

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: SphericalLensDistortionModelHandler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_filmback`` (CameraFilmbackSettings):  [Read-Write] Filmback settings of the camera that is being used for distortion
- ``current_state`` (LensDistortionState):  [Read-Write] Current state as set by the most recent call to Update()
- ``display_name`` (str):  [Read-Only] Display name, used to identify handler in-editor details panels
- ``distortion_post_process_mid`` (MaterialInstanceDynamic):  [Read-Only] Dynamically created post-process material instance for the currently specified lens model
- ``lens_model_class`` (type(Class)):  [Read-Only] Lens Model describing how to interpret the distortion parameters
- ``overscan_factor`` (float):  [Read-Only] Computed overscan factor needed to scale the camera's FOV (read-only)

<a id="unreal.SphericalLensModel"></a>