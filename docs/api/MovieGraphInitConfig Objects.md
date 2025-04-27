## MovieGraphInitConfig Objects

```python
class MovieGraphInitConfig(StructBase)
```

Movie Graph Init Config

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``audio_renderer_class`` (type(Class)):  [Read-Write] Which class should the UMovieGraphPipeline use to generate audio. Defaults to
  UMovieGraphDefaultAudioOutput.
- ``data_source_class`` (type(Class)):  [Read-Write] Which class should the UMovieGraphPipeline use to build time ranges from, and
  during evaluation, send callbacks about the time actually evaluated so you
  can sync with an external source. Defaults to UMovieGraphSequenceDataSource.
- ``render_viewport`` (bool):  [Read-Write] Should the UMovieGraphPipeline render the full player viewport? Defaults
  to false (so no 3d content is rendered) so we can display the UMG widgets
  and MRQ rendering always happens in an off-screen render target.
- ``renderer_class`` (type(Class)):  [Read-Write] Which class should the UMovieGraphPipeline use to look for render layers and
  request renders from. Defaults to UMovieGraphDefaultRenderer.

<a id="unreal.MovieGraphInitConfig.__init__"></a>

#### __init__

```python
def __init__(renderer_class: Class = None,
             data_source_class: Class = None,
             audio_renderer_class: Class = None,
             render_viewport: bool = False) -> None
```

<a id="unreal.MovieGraphInitConfig.renderer_class"></a>

#### renderer_class

```python
@property
def renderer_class() -> Class
```

(type(Class)):  [Read-Write] Which class should the UMovieGraphPipeline use to look for render layers and
request renders from. Defaults to UMovieGraphDefaultRenderer.

<a id="unreal.MovieGraphInitConfig.renderer_class"></a>

#### renderer_class

```python
@renderer_class.setter
def renderer_class(value: Class) -> None
```

<a id="unreal.MovieGraphInitConfig.data_source_class"></a>

#### data_source_class

```python
@property
def data_source_class() -> Class
```

(type(Class)):  [Read-Write] Which class should the UMovieGraphPipeline use to build time ranges from, and
during evaluation, send callbacks about the time actually evaluated so you
can sync with an external source. Defaults to UMovieGraphSequenceDataSource.

<a id="unreal.MovieGraphInitConfig.data_source_class"></a>

#### data_source_class

```python
@data_source_class.setter
def data_source_class(value: Class) -> None
```

<a id="unreal.MovieGraphInitConfig.audio_renderer_class"></a>

#### audio_renderer_class

```python
@property
def audio_renderer_class() -> Class
```

(type(Class)):  [Read-Write] Which class should the UMovieGraphPipeline use to generate audio. Defaults to
UMovieGraphDefaultAudioOutput.

<a id="unreal.MovieGraphInitConfig.audio_renderer_class"></a>

#### audio_renderer_class

```python
@audio_renderer_class.setter
def audio_renderer_class(value: Class) -> None
```

<a id="unreal.MovieGraphInitConfig.render_viewport"></a>

#### render_viewport

```python
@property
def render_viewport() -> bool
```

(bool):  [Read-Write] Should the UMovieGraphPipeline render the full player viewport? Defaults
to false (so no 3d content is rendered) so we can display the UMG widgets
and MRQ rendering always happens in an off-screen render target.

<a id="unreal.MovieGraphInitConfig.render_viewport"></a>

#### render_viewport

```python
@render_viewport.setter
def render_viewport(value: bool) -> None
```

<a id="unreal.MovieGraphResolveArgs"></a>