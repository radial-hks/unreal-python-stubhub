## LiveLinkCameraStaticData Objects

```python
class LiveLinkCameraStaticData(LiveLinkTransformStaticData)
```

Static data for Camera data.

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkCameraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``film_back_height`` (float):  [Read-Write] Used with CinematicCamera. Values greater than 0 will be applied
- ``film_back_width`` (float):  [Read-Write] Used with CinematicCamera. Values greater than 0 will be applied
- ``is_aperture_supported`` (bool):  [Read-Write] Whether Aperture in frame data can be used
- ``is_aspect_ratio_supported`` (bool):  [Read-Write] Whether AspectRatio in frame data can be used
- ``is_depth_of_field_supported`` (bool):  [Read-Write] Set to false to force the camera to disable depth of field
- ``is_field_of_view_supported`` (bool):  [Read-Write] Whether FieldOfView in frame data can be used
- ``is_focal_length_supported`` (bool):  [Read-Write] Whether FocalLength in frame data can be used
- ``is_focus_distance_supported`` (bool):  [Read-Write] Whether FocusDistance in frame data can be used
- ``is_location_supported`` (bool):  [Read-Write] Whether location in frame data should be used
- ``is_projection_mode_supported`` (bool):  [Read-Write] Whether ProjectionMode in frame data can be used
- ``is_rotation_supported`` (bool):  [Read-Write] Whether rotation in frame data should be used
- ``is_scale_supported`` (bool):  [Read-Write] Whether scale in frame data should be used
- ``property_names`` (Array[Name]):  [Read-Write] Names for each curve values that will be sent for each frame

<a id="unreal.LiveLinkCameraStaticData.__init__"></a>

#### __init__

```python
def __init__(property_names: Array[Name] = [],
             is_location_supported: bool = False,
             is_rotation_supported: bool = False,
             is_scale_supported: bool = False,
             is_field_of_view_supported: bool = False,
             is_aspect_ratio_supported: bool = False,
             is_focal_length_supported: bool = False,
             is_projection_mode_supported: bool = False,
             film_back_width: float = 0.000000,
             film_back_height: float = 0.000000,
             is_aperture_supported: bool = False,
             is_focus_distance_supported: bool = False,
             is_depth_of_field_supported: bool = False) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_field_of_view_supported"></a>

#### is_field_of_view_supported

```python
@property
def is_field_of_view_supported() -> bool
```

(bool):  [Read-Write] Whether FieldOfView in frame data can be used

<a id="unreal.LiveLinkCameraStaticData.is_field_of_view_supported"></a>

#### is_field_of_view_supported

```python
@is_field_of_view_supported.setter
def is_field_of_view_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_aspect_ratio_supported"></a>

#### is_aspect_ratio_supported

```python
@property
def is_aspect_ratio_supported() -> bool
```

(bool):  [Read-Write] Whether AspectRatio in frame data can be used

<a id="unreal.LiveLinkCameraStaticData.is_aspect_ratio_supported"></a>

#### is_aspect_ratio_supported

```python
@is_aspect_ratio_supported.setter
def is_aspect_ratio_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_focal_length_supported"></a>

#### is_focal_length_supported

```python
@property
def is_focal_length_supported() -> bool
```

(bool):  [Read-Write] Whether FocalLength in frame data can be used

<a id="unreal.LiveLinkCameraStaticData.is_focal_length_supported"></a>

#### is_focal_length_supported

```python
@is_focal_length_supported.setter
def is_focal_length_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_projection_mode_supported"></a>

#### is_projection_mode_supported

```python
@property
def is_projection_mode_supported() -> bool
```

(bool):  [Read-Write] Whether ProjectionMode in frame data can be used

<a id="unreal.LiveLinkCameraStaticData.is_projection_mode_supported"></a>

#### is_projection_mode_supported

```python
@is_projection_mode_supported.setter
def is_projection_mode_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData.film_back_width"></a>

#### film_back_width

```python
@property
def film_back_width() -> float
```

(float):  [Read-Write] Used with CinematicCamera. Values greater than 0 will be applied

<a id="unreal.LiveLinkCameraStaticData.film_back_width"></a>

#### film_back_width

```python
@film_back_width.setter
def film_back_width(value: float) -> None
```

<a id="unreal.LiveLinkCameraStaticData.film_back_height"></a>

#### film_back_height

```python
@property
def film_back_height() -> float
```

(float):  [Read-Write] Used with CinematicCamera. Values greater than 0 will be applied

<a id="unreal.LiveLinkCameraStaticData.film_back_height"></a>

#### film_back_height

```python
@film_back_height.setter
def film_back_height(value: float) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_aperture_supported"></a>

#### is_aperture_supported

```python
@property
def is_aperture_supported() -> bool
```

(bool):  [Read-Write] Whether Aperture in frame data can be used

<a id="unreal.LiveLinkCameraStaticData.is_aperture_supported"></a>

#### is_aperture_supported

```python
@is_aperture_supported.setter
def is_aperture_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_focus_distance_supported"></a>

#### is_focus_distance_supported

```python
@property
def is_focus_distance_supported() -> bool
```

(bool):  [Read-Write] Whether FocusDistance in frame data can be used

<a id="unreal.LiveLinkCameraStaticData.is_focus_distance_supported"></a>

#### is_focus_distance_supported

```python
@is_focus_distance_supported.setter
def is_focus_distance_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData.is_depth_of_field_supported"></a>

#### is_depth_of_field_supported

```python
@property
def is_depth_of_field_supported() -> bool
```

(bool):  [Read-Write] Set to false to force the camera to disable depth of field

<a id="unreal.LiveLinkCameraStaticData.is_depth_of_field_supported"></a>

#### is_depth_of_field_supported

```python
@is_depth_of_field_supported.setter
def is_depth_of_field_supported(value: bool) -> None
```

<a id="unreal.LiveLinkTransformFrameData"></a>