## CameraCalibrationSubsystem Objects

```python
class CameraCalibrationSubsystem(EngineSubsystem)
```

Camera Calibration subsystem

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: CameraCalibrationSubsystem.h

<a id="unreal.CameraCalibrationSubsystem.unregister_distortion_model_handler"></a>

#### unregister_distortion_model_handler

```python
def unregister_distortion_model_handler(
        component: CineCameraComponent,
        handler: LensDistortionModelHandlerBase) -> None
```

x.unregister_distortion_model_handler(component, handler) -> None
Unregister Distortion Model Handler

Args:
    component (CineCameraComponent): 
    handler (LensDistortionModelHandlerBase):

<a id="unreal.CameraCalibrationSubsystem.set_default_lens_file"></a>

#### set_default_lens_file

```python
def set_default_lens_file(new_default_lens_file: LensFile) -> None
```

x.set_default_lens_file(new_default_lens_file) -> None
Get the default lens file.

Args:
    new_default_lens_file (LensFile):

<a id="unreal.CameraCalibrationSubsystem.get_registered_lens_model"></a>

#### get_registered_lens_model

```python
def get_registered_lens_model(model_name: Name) -> Class
```

x.get_registered_lens_model(model_name) -> type(Class)
Return the ULensModel subclass that was registered with the input model name

Args:
    model_name (Name): 

Returns:
    type(Class):

<a id="unreal.CameraCalibrationSubsystem.get_overlay_material_names"></a>

#### get_overlay_material_names

```python
def get_overlay_material_names() -> Array[Name]
```

x.get_overlay_material_names() -> Array[Name]
Returns a list of all overlays known to the subsystem
This includes the default overlays listed in the camera calibration settings
as well as any of overlays that have been registered with this subsystem

Returns:
    Array[Name]:

<a id="unreal.CameraCalibrationSubsystem.get_overlay_material"></a>

#### get_overlay_material

```python
def get_overlay_material(overlay_name: Name) -> MaterialInterface
```

x.get_overlay_material(overlay_name) -> MaterialInterface
Returns the overlay material associated with the input overlay name

Args:
    overlay_name (Name): 

Returns:
    MaterialInterface:

<a id="unreal.CameraCalibrationSubsystem.get_lens_file"></a>

#### get_lens_file

```python
def get_lens_file(picker: LensFilePicker) -> LensFile
```

x.get_lens_file(picker) -> LensFile
Facilitator around the picker to get the desired lens file.

Args:
    picker (LensFilePicker): 

Returns:
    LensFile:

<a id="unreal.CameraCalibrationSubsystem.get_distortion_model_handlers"></a>

#### get_distortion_model_handlers

```python
def get_distortion_model_handlers(
        component: CineCameraComponent
) -> Array[LensDistortionModelHandlerBase]
```

x.get_distortion_model_handlers(component) -> Array[LensDistortionModelHandlerBase]
Get Distortion Model Handlers

Args:
    component (CineCameraComponent): 

Returns:
    Array[LensDistortionModelHandlerBase]:

<a id="unreal.CameraCalibrationSubsystem.get_default_lens_file"></a>

#### get_default_lens_file

```python
def get_default_lens_file() -> LensFile
```

x.get_default_lens_file() -> LensFile
Get the default lens file.

Returns:
    LensFile:

<a id="unreal.CameraCalibrationSubsystem.get_camera_nodal_offset_algos"></a>

#### get_camera_nodal_offset_algos

```python
def get_camera_nodal_offset_algos() -> Array[Name]
```

x.get_camera_nodal_offset_algos() -> Array[Name]
Returns an array with the names of the available nodal offset algorithms

Returns:
    Array[Name]:

<a id="unreal.CameraCalibrationSubsystem.get_camera_nodal_offset_algo"></a>

#### get_camera_nodal_offset_algo

```python
def get_camera_nodal_offset_algo(name: Name) -> Class
```

x.get_camera_nodal_offset_algo(name) -> type(Class)
Returns the nodal offset algorithm by name

Args:
    name (Name): 

Returns:
    type(Class):

<a id="unreal.CameraCalibrationSubsystem.get_camera_image_center_algos"></a>

#### get_camera_image_center_algos

```python
def get_camera_image_center_algos() -> Array[Name]
```

x.get_camera_image_center_algos() -> Array[Name]
Returns an array with the names of the available image center algorithms

Returns:
    Array[Name]:

<a id="unreal.CameraCalibrationSubsystem.get_camera_image_center_algo"></a>

#### get_camera_image_center_algo

```python
def get_camera_image_center_algo(name: Name) -> Class
```

x.get_camera_image_center_algo(name) -> type(Class)
Returns the image center algorithm by name

Args:
    name (Name): 

Returns:
    type(Class):

<a id="unreal.CameraCalibrationSubsystem.get_camera_calibration_steps"></a>

#### get_camera_calibration_steps

```python
def get_camera_calibration_steps() -> Array[Name]
```

x.get_camera_calibration_steps() -> Array[Name]
Returns an array with the names of the available camera calibration steps

Returns:
    Array[Name]:

<a id="unreal.CameraCalibrationSubsystem.get_camera_calibration_step"></a>

#### get_camera_calibration_step

```python
def get_camera_calibration_step(name: Name) -> Class
```

x.get_camera_calibration_step(name) -> type(Class)
Returns the camera calibration step by name

Args:
    name (Name): 

Returns:
    type(Class):

<a id="unreal.CameraCalibrationSubsystem.find_or_create_distortion_model_handler"></a>

#### find_or_create_distortion_model_handler

```python
def find_or_create_distortion_model_handler(
    distortion_handler_picker: DistortionHandlerPicker, lens_model_class: Class
) -> Tuple[LensDistortionModelHandlerBase, DistortionHandlerPicker]
```

x.find_or_create_distortion_model_handler(distortion_handler_picker, lens_model_class) -> (LensDistortionModelHandlerBase, distortion_handler_picker=DistortionHandlerPicker)
Find or Create Distortion Model Handler

Args:
    distortion_handler_picker (DistortionHandlerPicker): 
    lens_model_class (type(Class)): 

Returns:
    DistortionHandlerPicker: 

    distortion_handler_picker (DistortionHandlerPicker):

<a id="unreal.CameraCalibrationSubsystem.find_distortion_model_handler"></a>

#### find_distortion_model_handler

```python
def find_distortion_model_handler(
    distortion_handler_picker: DistortionHandlerPicker,
    update_picker: bool = True
) -> Tuple[LensDistortionModelHandlerBase, DistortionHandlerPicker]
```

x.find_distortion_model_handler(distortion_handler_picker, update_picker=True) -> (LensDistortionModelHandlerBase, distortion_handler_picker=DistortionHandlerPicker)
Find Distortion Model Handler

Args:
    distortion_handler_picker (DistortionHandlerPicker): 
    update_picker (bool): 

Returns:
    DistortionHandlerPicker: 

    distortion_handler_picker (DistortionHandlerPicker):

<a id="unreal.LensFile"></a>