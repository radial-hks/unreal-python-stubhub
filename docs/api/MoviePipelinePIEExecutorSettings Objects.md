## MoviePipelinePIEExecutorSettings Objects

```python
class MoviePipelinePIEExecutorSettings(DeveloperSettings)
```

This is the implementation responsible for executing the rendering of
multiple movie pipelines within the editor using PIE.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MoviePipelinePIEExecutorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``initial_delay_frame_count`` (int32):  [Read-Write] How long should we wait after being initialized to start doing any work? This can be used
  to work around situations where the game is not fully loaded by the time the pipeline
  is automatically started and it is important that the game is fully loaded before we do
  any work (such as evaluating frames for warm-up).
- ``resize_pie_window_to_output_resolution`` (bool):  [Read-Write] Should the PIE Window be created at the same resolution as the MRQ Output? By default we create the window at 720p for a nicer
  user experience, but this can be used to work around a widget scaling issue with UMG Widgets when using the UI Renderer
  setting. PIE is still limited by your monitor's resolution so you will need a monitor at least as big as your requested output
  for this to work (or can be combined with launching the editor with -ForceRes).

  Warning: Don't use this setting in combination with HighResTiling, as the main backbuffer will have to get resized to your final
  output resolution which will be too large.

<a id="unreal.MoviePipelinePIEExecutorSettings.initial_delay_frame_count"></a>

#### initial_delay_frame_count

```python
@property
def initial_delay_frame_count() -> int
```

(int32):  [Read-Write] How long should we wait after being initialized to start doing any work? This can be used
to work around situations where the game is not fully loaded by the time the pipeline
is automatically started and it is important that the game is fully loaded before we do
any work (such as evaluating frames for warm-up).

<a id="unreal.MoviePipelinePIEExecutorSettings.initial_delay_frame_count"></a>

#### initial_delay_frame_count

```python
@initial_delay_frame_count.setter
def initial_delay_frame_count(value: int) -> None
```

<a id="unreal.MoviePipelinePIEExecutorSettings.resize_pie_window_to_output_resolution"></a>

#### resize_pie_window_to_output_resolution

```python
@property
def resize_pie_window_to_output_resolution() -> bool
```

(bool):  [Read-Write] Should the PIE Window be created at the same resolution as the MRQ Output? By default we create the window at 720p for a nicer
user experience, but this can be used to work around a widget scaling issue with UMG Widgets when using the UI Renderer
setting. PIE is still limited by your monitor's resolution so you will need a monitor at least as big as your requested output
for this to work (or can be combined with launching the editor with -ForceRes).

Warning: Don't use this setting in combination with HighResTiling, as the main backbuffer will have to get resized to your final
output resolution which will be too large.

<a id="unreal.MoviePipelinePIEExecutorSettings.resize_pie_window_to_output_resolution"></a>

#### resize_pie_window_to_output_resolution

```python
@resize_pie_window_to_output_resolution.setter
def resize_pie_window_to_output_resolution(value: bool) -> None
```

<a id="unreal.MovieGraphConfigFactory"></a>