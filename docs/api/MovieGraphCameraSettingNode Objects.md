## MovieGraphCameraSettingNode Objects

```python
class MovieGraphCameraSettingNode(MovieGraphSettingNode)
```

A node which configures global camera settings that are shared among all renders.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphCameraNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_b_render_all_cameras`` (bool):  [Read-Write]
- ``override_overscan_percentage`` (bool):  [Read-Write]
- ``override_shutter_timing`` (bool):  [Read-Write]
- ``overscan_percentage`` (float):  [Read-Write] Overscan percent enables rendering render additional pixels beyond the set resolution and can be used in conjunction
  with EXR file output to add post-processing effects such as lens distortion.
  Please note that using this feature might affect the results due to auto-exposure and other camera settings.
  On EXR this will produce a 1080p image with extra pixel data hidden around the outside edges for use
  in post production. For all other formats this will increase the final resolution and no pixels will be hidden
  (ie: 1080p with 10.0 overscan will make a 2112x1188 jpg, but a 1080p exr /w 96/54 pixels hidden on each side).

  Note: This uses 0-100 and not 0-1 like the previous system did to bring it in-line with other usages
  of overscan in the engine (nDisplay).
- ``render_all_cameras`` (bool):  [Read-Write] * If enabled Movie Render Queue will examine your Level Sequence for additional cameras and create an additional render for each renderer for that camera.
  * The Camera Cut Track/Section is still used to determine the range of time to render, and then all Camera Actors that are in the level sequence adjacent
  * to the Camera Cut Track will be considered for rendering. They are expected to exist the entire time and do not support rendering sub-ranges.
  *
  * This increases render duration (100% per camera) and has increased VRAM/RAM requirements. However all cameras are rendered on the same engine tick so they
  * should all see a consistent view of the world which can be useful for things like particle effects, etc.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``shutter_timing`` (MoviePipelineShutterTiming):  [Read-Write] Shutter Timing allows you to bias the timing of your shutter angle to either be before, during, or after
  a frame. When set to FrameClose, it means that the motion gathered up to produce frame N comes from
  before and right up to frame N. When set to FrameCenter, the motion represents half the time before the
  frame and half the time after the frame. When set to FrameOpen, the motion represents the time from
  Frame N onwards.

<a id="unreal.MovieGraphCameraSettingNode.override_shutter_timing"></a>

#### override_shutter_timing

```python
@property
def override_shutter_timing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCameraSettingNode.override_shutter_timing"></a>

#### override_shutter_timing

```python
@override_shutter_timing.setter
def override_shutter_timing(value: bool) -> None
```

<a id="unreal.MovieGraphCameraSettingNode.override_overscan_percentage"></a>

#### override_overscan_percentage

```python
@property
def override_overscan_percentage() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCameraSettingNode.override_overscan_percentage"></a>

#### override_overscan_percentage

```python
@override_overscan_percentage.setter
def override_overscan_percentage(value: bool) -> None
```

<a id="unreal.MovieGraphCameraSettingNode.override_b_render_all_cameras"></a>

#### override_b_render_all_cameras

```python
@property
def override_b_render_all_cameras() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphCameraSettingNode.override_b_render_all_cameras"></a>

#### override_b_render_all_cameras

```python
@override_b_render_all_cameras.setter
def override_b_render_all_cameras(value: bool) -> None
```

<a id="unreal.MovieGraphCameraSettingNode.shutter_timing"></a>

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

<a id="unreal.MovieGraphCameraSettingNode.shutter_timing"></a>

#### shutter_timing

```python
@shutter_timing.setter
def shutter_timing(value: MoviePipelineShutterTiming) -> None
```

<a id="unreal.MovieGraphCameraSettingNode.overscan_percentage"></a>

#### overscan_percentage

```python
@property
def overscan_percentage() -> float
```

(float):  [Read-Write] Overscan percent enables rendering render additional pixels beyond the set resolution and can be used in conjunction
with EXR file output to add post-processing effects such as lens distortion.
Please note that using this feature might affect the results due to auto-exposure and other camera settings.
On EXR this will produce a 1080p image with extra pixel data hidden around the outside edges for use
in post production. For all other formats this will increase the final resolution and no pixels will be hidden
(ie: 1080p with 10.0 overscan will make a 2112x1188 jpg, but a 1080p exr /w 96/54 pixels hidden on each side).

Note: This uses 0-100 and not 0-1 like the previous system did to bring it in-line with other usages
of overscan in the engine (nDisplay).

<a id="unreal.MovieGraphCameraSettingNode.overscan_percentage"></a>

#### overscan_percentage

```python
@overscan_percentage.setter
def overscan_percentage(value: float) -> None
```

<a id="unreal.MovieGraphCameraSettingNode.render_all_cameras"></a>

#### render_all_cameras

```python
@property
def render_all_cameras() -> bool
```

(bool):  [Read-Write] * If enabled Movie Render Queue will examine your Level Sequence for additional cameras and create an additional render for each renderer for that camera.
* The Camera Cut Track/Section is still used to determine the range of time to render, and then all Camera Actors that are in the level sequence adjacent
* to the Camera Cut Track will be considered for rendering. They are expected to exist the entire time and do not support rendering sub-ranges.
*
* This increases render duration (100% per camera) and has increased VRAM/RAM requirements. However all cameras are rendered on the same engine tick so they
* should all see a consistent view of the world which can be useful for things like particle effects, etc.

<a id="unreal.MovieGraphCameraSettingNode.render_all_cameras"></a>

#### render_all_cameras

```python
@render_all_cameras.setter
def render_all_cameras(value: bool) -> None
```

<a id="unreal.MovieGraphCollectionNode"></a>