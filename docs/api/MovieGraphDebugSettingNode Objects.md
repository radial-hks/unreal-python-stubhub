## MovieGraphDebugSettingNode Objects

```python
class MovieGraphDebugSettingNode(MovieGraphSettingNode)
```

A node which configures various debug settings that may be useful when debugging an issue.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphDebugNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``capture_frames_with_render_doc`` (bool):  [Read-Write] If true, automatically trigger RenderDoc to capture rendering information. RenderDoc plugin must be enabled,
  and the editor must have been launched with -AttachRenderDoc. Resulting capture will be in /Saved/RenderDocCaptures.
- ``capture_unreal_insights_trace`` (bool):  [Read-Write] If true, automatically capture an Unreal Insights trace file for the duration of the render.
  Resulting capture will be in the global Output Directory for the job.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_b_capture_frames_with_render_doc`` (bool):  [Read-Write]
- ``override_b_capture_unreal_insights_trace`` (bool):  [Read-Write]
- ``override_unreal_insights_trace_file_name_format`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``unreal_insights_trace_file_name_format`` (str):  [Read-Write] If true, automatically capture an Unreal Insights trace file for the duration of the render.
  Resulting capture will be in the global Output Directory for the job.

<a id="unreal.MovieGraphDebugSettingNode.override_b_capture_frames_with_render_doc"></a>

#### override_b_capture_frames_with_render_doc

```python
@property
def override_b_capture_frames_with_render_doc() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDebugSettingNode.override_b_capture_frames_with_render_doc"></a>

#### override_b_capture_frames_with_render_doc

```python
@override_b_capture_frames_with_render_doc.setter
def override_b_capture_frames_with_render_doc(value: bool) -> None
```

<a id="unreal.MovieGraphDebugSettingNode.override_b_capture_unreal_insights_trace"></a>

#### override_b_capture_unreal_insights_trace

```python
@property
def override_b_capture_unreal_insights_trace() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDebugSettingNode.override_b_capture_unreal_insights_trace"></a>

#### override_b_capture_unreal_insights_trace

```python
@override_b_capture_unreal_insights_trace.setter
def override_b_capture_unreal_insights_trace(value: bool) -> None
```

<a id="unreal.MovieGraphDebugSettingNode.override_unreal_insights_trace_file_name_format"></a>

#### override_unreal_insights_trace_file_name_format

```python
@property
def override_unreal_insights_trace_file_name_format() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDebugSettingNode.override_unreal_insights_trace_file_name_format"></a>

#### override_unreal_insights_trace_file_name_format

```python
@override_unreal_insights_trace_file_name_format.setter
def override_unreal_insights_trace_file_name_format(value: bool) -> None
```

<a id="unreal.MovieGraphDebugSettingNode.capture_frames_with_render_doc"></a>

#### capture_frames_with_render_doc

```python
@property
def capture_frames_with_render_doc() -> bool
```

(bool):  [Read-Write] If true, automatically trigger RenderDoc to capture rendering information. RenderDoc plugin must be enabled,
and the editor must have been launched with -AttachRenderDoc. Resulting capture will be in /Saved/RenderDocCaptures.

<a id="unreal.MovieGraphDebugSettingNode.capture_frames_with_render_doc"></a>

#### capture_frames_with_render_doc

```python
@capture_frames_with_render_doc.setter
def capture_frames_with_render_doc(value: bool) -> None
```

<a id="unreal.MovieGraphDebugSettingNode.capture_unreal_insights_trace"></a>

#### capture_unreal_insights_trace

```python
@property
def capture_unreal_insights_trace() -> bool
```

(bool):  [Read-Write] If true, automatically capture an Unreal Insights trace file for the duration of the render.
Resulting capture will be in the global Output Directory for the job.

<a id="unreal.MovieGraphDebugSettingNode.capture_unreal_insights_trace"></a>

#### capture_unreal_insights_trace

```python
@capture_unreal_insights_trace.setter
def capture_unreal_insights_trace(value: bool) -> None
```

<a id="unreal.MovieGraphDebugSettingNode.unreal_insights_trace_file_name_format"></a>

#### unreal_insights_trace_file_name_format

```python
@property
def unreal_insights_trace_file_name_format() -> str
```

(str):  [Read-Write] If true, automatically capture an Unreal Insights trace file for the duration of the render.
Resulting capture will be in the global Output Directory for the job.

<a id="unreal.MovieGraphDebugSettingNode.unreal_insights_trace_file_name_format"></a>

#### unreal_insights_trace_file_name_format

```python
@unreal_insights_trace_file_name_format.setter
def unreal_insights_trace_file_name_format(value: str) -> None
```

<a id="unreal.MovieGraphDefaultAudioRenderer"></a>