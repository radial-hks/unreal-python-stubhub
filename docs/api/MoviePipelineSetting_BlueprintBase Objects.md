## MoviePipelineSetting_BlueprintBase Objects

```python
class MoviePipelineSetting_BlueprintBase(MoviePipelineSetting)
```

A base class for all Movie Render Pipeline settings which can be implemented in Blueprints. This features
a slightly different API than the regular UMoviePipelineSetting to make the Blueprint integration nicer
without breaking the C++ API backwards compatibility.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineSettingBlueprintBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_be_disabled`` (bool):  [Read-Write]
- ``category_text`` (Text):  [Read-Write]
- ``is_valid_on_primary`` (bool):  [Read-Write]
- ``is_valid_on_shots`` (bool):  [Read-Write]

<a id="unreal.MoviePipelineSetting_BlueprintBase.receive_teardown_for_pipeline_impl"></a>

#### receive_teardown_for_pipeline_impl

```python
def receive_teardown_for_pipeline_impl(pipeline: MoviePipeline) -> None
```

x.receive_teardown_for_pipeline_impl(pipeline) -> None
Receive Teardown for Pipeline Impl

Args:
    pipeline (MoviePipeline):

<a id="unreal.MoviePipelineSetting_BlueprintBase.receive_setup_for_pipeline_impl"></a>

#### receive_setup_for_pipeline_impl

```python
def receive_setup_for_pipeline_impl(pipeline: MoviePipeline) -> None
```

x.receive_setup_for_pipeline_impl(pipeline) -> None
Receive Setup for Pipeline Impl

Args:
    pipeline (MoviePipeline):

<a id="unreal.MoviePipelineSetting_BlueprintBase.receive_get_format_arguments"></a>

#### receive_get_format_arguments

```python
def receive_get_format_arguments(
    out_format_args: MoviePipelineFormatArgs
) -> Tuple[MoviePipelineFormatArgs, MoviePipelineFormatArgs]
```

x.receive_get_format_arguments(out_format_args) -> (MoviePipelineFormatArgs, out_format_args=MoviePipelineFormatArgs)
Receive Get Format Arguments

Args:
    out_format_args (MoviePipelineFormatArgs): 

Returns:
    MoviePipelineFormatArgs: 

    out_format_args (MoviePipelineFormatArgs):

<a id="unreal.MoviePipelineSetting_BlueprintBase.receive_get_footer_text"></a>

#### receive_get_footer_text

```python
def receive_get_footer_text(job: MoviePipelineExecutorJob) -> Text
```

x.receive_get_footer_text(job) -> Text
Receive Get Footer Text

Args:
    job (MoviePipelineExecutorJob): 

Returns:
    Text:

<a id="unreal.MoviePipelineSetting_BlueprintBase.on_engine_tick_begin_frame"></a>

#### on_engine_tick_begin_frame

```python
def on_engine_tick_begin_frame() -> None
```

x.on_engine_tick_begin_frame() -> None
Tick

<a id="unreal.MoviePipelineViewFamilySetting"></a>