## CameraFocusSettings Objects

```python
class CameraFocusSettings(StructBase)
```

Settings to control camera focus

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_focus_plane_color`` (Color):  [Read-Write] For customizing the focus plane color, in case the default doesn't show up well in your scene.
- ``draw_debug_focus_plane`` (bool):  [Read-Write] True to draw a translucent plane at the current focus depth, for easy tweaking.
- ``focus_method`` (CameraFocusMethod):  [Read-Write] Which method to use to handle camera focus
- ``focus_offset`` (float):  [Read-Write] Additional focus depth offset, used for manually tweaking if your chosen focus method needs adjustment
- ``focus_smoothing_interp_speed`` (float):  [Read-Write] Controls interpolation speed when smoothing focus distance changes. Ignored if bSmoothFocusChanges is false.
- ``manual_focus_distance`` (float):  [Read-Write] Manually-controlled focus distance (manual focus mode only)
- ``smooth_focus_changes`` (bool):  [Read-Write] True to use interpolation to smooth out changes in focus distance, false for focus distance changes to be instantaneous.
- ``tracking_focus_settings`` (CameraTrackingFocusSettings):  [Read-Write] Settings to control tracking focus (tracking focus mode only)

<a id="unreal.CameraFocusSettings.__init__"></a>

#### __init__

```python
def __init__(
        focus_method: CameraFocusMethod = CameraFocusMethod.DO_NOT_OVERRIDE,
        manual_focus_distance: float = 0.000000,
        tracking_focus_settings: CameraTrackingFocusSettings = [
            None, [0.000000, 0.000000, 0.000000], False
        ],
        smooth_focus_changes: bool = False,
        focus_smoothing_interp_speed: float = 0.000000,
        focus_offset: float = 0.000000) -> None
```

<a id="unreal.CameraFocusSettings.focus_method"></a>

#### focus_method

```python
@property
def focus_method() -> CameraFocusMethod
```

(CameraFocusMethod):  [Read-Write] Which method to use to handle camera focus

<a id="unreal.CameraFocusSettings.focus_method"></a>

#### focus_method

```python
@focus_method.setter
def focus_method(value: CameraFocusMethod) -> None
```

<a id="unreal.CameraFocusSettings.manual_focus_distance"></a>

#### manual_focus_distance

```python
@property
def manual_focus_distance() -> float
```

(float):  [Read-Write] Manually-controlled focus distance (manual focus mode only)

<a id="unreal.CameraFocusSettings.manual_focus_distance"></a>

#### manual_focus_distance

```python
@manual_focus_distance.setter
def manual_focus_distance(value: float) -> None
```

<a id="unreal.CameraFocusSettings.tracking_focus_settings"></a>

#### tracking_focus_settings

```python
@property
def tracking_focus_settings() -> CameraTrackingFocusSettings
```

(CameraTrackingFocusSettings):  [Read-Write] Settings to control tracking focus (tracking focus mode only)

<a id="unreal.CameraFocusSettings.tracking_focus_settings"></a>

#### tracking_focus_settings

```python
@tracking_focus_settings.setter
def tracking_focus_settings(value: CameraTrackingFocusSettings) -> None
```

<a id="unreal.CameraFocusSettings.smooth_focus_changes"></a>

#### smooth_focus_changes

```python
@property
def smooth_focus_changes() -> bool
```

(bool):  [Read-Write] True to use interpolation to smooth out changes in focus distance, false for focus distance changes to be instantaneous.

<a id="unreal.CameraFocusSettings.smooth_focus_changes"></a>

#### smooth_focus_changes

```python
@smooth_focus_changes.setter
def smooth_focus_changes(value: bool) -> None
```

<a id="unreal.CameraFocusSettings.focus_smoothing_interp_speed"></a>

#### focus_smoothing_interp_speed

```python
@property
def focus_smoothing_interp_speed() -> float
```

(float):  [Read-Write] Controls interpolation speed when smoothing focus distance changes. Ignored if bSmoothFocusChanges is false.

<a id="unreal.CameraFocusSettings.focus_smoothing_interp_speed"></a>

#### focus_smoothing_interp_speed

```python
@focus_smoothing_interp_speed.setter
def focus_smoothing_interp_speed(value: float) -> None
```

<a id="unreal.CameraFocusSettings.focus_offset"></a>

#### focus_offset

```python
@property
def focus_offset() -> float
```

(float):  [Read-Write] Additional focus depth offset, used for manually tweaking if your chosen focus method needs adjustment

<a id="unreal.CameraFocusSettings.focus_offset"></a>

#### focus_offset

```python
@focus_offset.setter
def focus_offset(value: float) -> None
```

<a id="unreal.BakingAnimationKeySettings"></a>