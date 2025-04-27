## MoviePipelineCameraSetting Objects

```python
class MoviePipelineCameraSetting(MoviePipelineSetting)
```

Movie Pipeline Camera Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineCameraSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``override_camera_overscan`` (bool):  [Read-Write] If true, the camera settings overscan value will override any overscan on the cameras when rendering;
  otherwise, the overscan value on the cameras will be used.
- ``overscan_percentage`` (float):  [Read-Write] Overscan percent allows to render additional pixels beyond the set resolution and can be used in conjunction
  with EXR file output to add post-processing effects such as lens distortion.
  Please note that using this feature might affect the results due to auto-exposure and other camera settings.
  On EXR this will produce a 1080p image with extra pixel data hidden around the outside edges for use
  in post production. For all other formats this will increase the final resolution and no pixels will be hidden
  (ie: 1080p /w 0.1 overscan will make a 2112x1188 jpg, but a 1080p exr /w 96/54 pixels hidden on each side)
- ``render_all_cameras`` (bool):  [Read-Write] If true, when a Camera Cut section is found we will also render any other cameras within the same sequence (not parent, nor child sequences though).
  These cameras are rendered at the same time as the primary camera meaning all cameras capture the same world state. Do note that this multiplies
  render times and memory requirements!
- ``shutter_timing`` (MoviePipelineShutterTiming):  [Read-Write] Shutter Timing allows you to bias the timing of your shutter angle to either be before, during, or after
  a frame. When set to FrameClose, it means that the motion gathered up to produce frame N comes from
  before and right up to frame N. When set to FrameCenter, the motion represents half the time before the
  frame and half the time after the frame. When set to FrameOpen, the motion represents the time from
  Frame N onwards.

<a id="unreal.MoviePipelineCameraSetting.shutter_timing"></a>

#### shutter_timing

```python
@property
def shutter_timing() -> MoviePipelineShutterTiming
```

(MoviePipelineShutterTiming):  [Read-Write] Shutter Timing allows you to bias the timing of your shutter angle to either be before, during, or after
a frame. When set to FrameClose, it means that the motion gathered up to produce frame N comes from
before and right up to frame N. When set to FrameCenter, the motion represents half the time before the
frame and half the time after the frame. When set to FrameOpen, the motion represents the time from
Frame N onwards.

<a id="unreal.MoviePipelineCameraSetting.shutter_timing"></a>

#### shutter_timing

```python
@shutter_timing.setter
def shutter_timing(value: MoviePipelineShutterTiming) -> None
```

<a id="unreal.MoviePipelineCameraSetting.override_camera_overscan"></a>

#### override_camera_overscan

```python
@property
def override_camera_overscan() -> bool
```

(bool):  [Read-Write] If true, the camera settings overscan value will override any overscan on the cameras when rendering;
otherwise, the overscan value on the cameras will be used.

<a id="unreal.MoviePipelineCameraSetting.override_camera_overscan"></a>

#### override_camera_overscan

```python
@override_camera_overscan.setter
def override_camera_overscan(value: bool) -> None
```

<a id="unreal.MoviePipelineCameraSetting.overscan_percentage"></a>

#### overscan_percentage

```python
@property
def overscan_percentage() -> float
```

(float):  [Read-Write] Overscan percent allows to render additional pixels beyond the set resolution and can be used in conjunction
with EXR file output to add post-processing effects such as lens distortion.
Please note that using this feature might affect the results due to auto-exposure and other camera settings.
On EXR this will produce a 1080p image with extra pixel data hidden around the outside edges for use
in post production. For all other formats this will increase the final resolution and no pixels will be hidden
(ie: 1080p /w 0.1 overscan will make a 2112x1188 jpg, but a 1080p exr /w 96/54 pixels hidden on each side)

<a id="unreal.MoviePipelineCameraSetting.overscan_percentage"></a>

#### overscan_percentage

```python
@overscan_percentage.setter
def overscan_percentage(value: float) -> None
```

<a id="unreal.MoviePipelineCameraSetting.render_all_cameras"></a>

#### render_all_cameras

```python
@property
def render_all_cameras() -> bool
```

(bool):  [Read-Write] If true, when a Camera Cut section is found we will also render any other cameras within the same sequence (not parent, nor child sequences though).
These cameras are rendered at the same time as the primary camera meaning all cameras capture the same world state. Do note that this multiplies
render times and memory requirements!

<a id="unreal.MoviePipelineCameraSetting.render_all_cameras"></a>

#### render_all_cameras

```python
@render_all_cameras.setter
def render_all_cameras(value: bool) -> None
```

<a id="unreal.MoviePipelineColorSetting"></a>