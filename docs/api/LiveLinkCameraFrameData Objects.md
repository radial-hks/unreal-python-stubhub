## LiveLinkCameraFrameData Objects

```python
class LiveLinkCameraFrameData(LiveLinkTransformFrameData)
```

Dynamic data for camera

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkCameraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aperture`` (float):  [Read-Write] Aperture of the camera in terms of f-stop
- ``aspect_ratio`` (float):  [Read-Write] Aspect Ratio of the camera (Width / Heigth)
- ``field_of_view`` (float):  [Read-Write] Field of View of the camera in degrees
- ``focal_length`` (float):  [Read-Write] Focal length of the camera
- ``focus_distance`` (float):  [Read-Write] Focus distance of the camera in cm. Works only in manual focus method
- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``projection_mode`` (LiveLinkCameraProjectionMode):  [Read-Write] ProjectionMode of the camera (Perspective, Orthographic, etc...)
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``transform`` (Transform):  [Read-Write] Transform of the frame
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkCameraFrameData.__init__"></a>

#### __init__

```python
def __init__(
    meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
    property_values: Array[float] = [],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]],
    field_of_view: float = 0.000000,
    aspect_ratio: float = 0.000000,
    focal_length: float = 0.000000,
    aperture: float = 0.000000,
    focus_distance: float = 0.000000,
    projection_mode: LiveLinkCameraProjectionMode = LiveLinkCameraProjectionMode
    .PERSPECTIVE
) -> None
```

<a id="unreal.LiveLinkCameraFrameData.field_of_view"></a>

#### field_of_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write] Field of View of the camera in degrees

<a id="unreal.LiveLinkCameraFrameData.field_of_view"></a>

#### field_of_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.LiveLinkCameraFrameData.aspect_ratio"></a>

#### aspect_ratio

```python
@property
def aspect_ratio() -> float
```

(float):  [Read-Write] Aspect Ratio of the camera (Width / Heigth)

<a id="unreal.LiveLinkCameraFrameData.aspect_ratio"></a>

#### aspect_ratio

```python
@aspect_ratio.setter
def aspect_ratio(value: float) -> None
```

<a id="unreal.LiveLinkCameraFrameData.focal_length"></a>

#### focal_length

```python
@property
def focal_length() -> float
```

(float):  [Read-Write] Focal length of the camera

<a id="unreal.LiveLinkCameraFrameData.focal_length"></a>

#### focal_length

```python
@focal_length.setter
def focal_length(value: float) -> None
```

<a id="unreal.LiveLinkCameraFrameData.aperture"></a>

#### aperture

```python
@property
def aperture() -> float
```

(float):  [Read-Write] Aperture of the camera in terms of f-stop

<a id="unreal.LiveLinkCameraFrameData.aperture"></a>

#### aperture

```python
@aperture.setter
def aperture(value: float) -> None
```

<a id="unreal.LiveLinkCameraFrameData.focus_distance"></a>

#### focus_distance

```python
@property
def focus_distance() -> float
```

(float):  [Read-Write] Focus distance of the camera in cm. Works only in manual focus method

<a id="unreal.LiveLinkCameraFrameData.focus_distance"></a>

#### focus_distance

```python
@focus_distance.setter
def focus_distance(value: float) -> None
```

<a id="unreal.LiveLinkCameraFrameData.projection_mode"></a>

#### projection_mode

```python
@property
def projection_mode() -> LiveLinkCameraProjectionMode
```

(LiveLinkCameraProjectionMode):  [Read-Write] ProjectionMode of the camera (Perspective, Orthographic, etc...)

<a id="unreal.LiveLinkCameraFrameData.projection_mode"></a>

#### projection_mode

```python
@projection_mode.setter
def projection_mode(value: LiveLinkCameraProjectionMode) -> None
```

<a id="unreal.LiveLinkCameraBlueprintData"></a>