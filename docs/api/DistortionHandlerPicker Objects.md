## DistortionHandlerPicker Objects

```python
class DistortionHandlerPicker(StructBase)
```

Distortion Handler Picker

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: CameraCalibrationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distortion_producer_id`` (Guid):  [Read-Write] UObject that produces the distortion state for the desired distortion handler
- ``handler_display_name`` (str):  [Read-Write] Display name of the desired distortion handler
- ``target_camera_component`` (CineCameraComponent):  [Read-Write] CineCameraComponent with which the desired distortion handler is associated

<a id="unreal.DistortionHandlerPicker.__init__"></a>

#### __init__

```python
def __init__(target_camera_component: CineCameraComponent = None,
             distortion_producer_id: Guid = [],
             handler_display_name: str = "") -> None
```

<a id="unreal.DistortionHandlerPicker.target_camera_component"></a>

#### target_camera_component

```python
@property
def target_camera_component() -> CineCameraComponent
```

(CineCameraComponent):  [Read-Write] CineCameraComponent with which the desired distortion handler is associated

<a id="unreal.DistortionHandlerPicker.target_camera_component"></a>

#### target_camera_component

```python
@target_camera_component.setter
def target_camera_component(value: CineCameraComponent) -> None
```

<a id="unreal.DistortionHandlerPicker.distortion_producer_id"></a>

#### distortion_producer_id

```python
@property
def distortion_producer_id() -> Guid
```

(Guid):  [Read-Write] UObject that produces the distortion state for the desired distortion handler

<a id="unreal.DistortionHandlerPicker.distortion_producer_id"></a>

#### distortion_producer_id

```python
@distortion_producer_id.setter
def distortion_producer_id(value: Guid) -> None
```

<a id="unreal.DistortionHandlerPicker.handler_display_name"></a>

#### handler_display_name

```python
@property
def handler_display_name() -> str
```

(str):  [Read-Write] Display name of the desired distortion handler

<a id="unreal.DistortionHandlerPicker.handler_display_name"></a>

#### handler_display_name

```python
@handler_display_name.setter
def handler_display_name(value: str) -> None
```

<a id="unreal.FocalLengthZoomPoint"></a>