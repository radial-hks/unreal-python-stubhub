## MoviePipelineInProcessExecutorSettings Objects

```python
class MoviePipelineInProcessExecutorSettings(DeveloperSettings)
```

This is the implementation responsible for executing the rendering of
multiple movie pipelines after being launched via the command line.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineInProcessExecutorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_command_line_arguments`` (str):  [Read-Write] A list of additional command line arguments to be appended to the new process startup. In the form of "-foo -bar=baz". Can be useful if your game requires certain arguments to start such as disabling log-in screens.
- ``close_editor`` (bool):  [Read-Write] If enabled the editor will close itself when a new process is started. This can be used to gain some performance.
- ``inherited_command_line_arguments`` (str):  [Read-Only] A list of command line arguments which are inherited from the currently running Editor instance that will be automatically appended to the new process.
- ``initial_delay_frame_count`` (int32):  [Read-Write] How long should we wait after being initialized to start doing any work? This can be used
  to work around situations where the game is not fully loaded by the time the pipeline
  is automatically started and it is important that the game is fully loaded before we do
  any work (such as evaluating frames for warm-up).

<a id="unreal.MoviePipelineInProcessExecutorSettings.close_editor"></a>

#### close_editor

```python
@property
def close_editor() -> bool
```

(bool):  [Read-Write] If enabled the editor will close itself when a new process is started. This can be used to gain some performance.

<a id="unreal.MoviePipelineInProcessExecutorSettings.close_editor"></a>

#### close_editor

```python
@close_editor.setter
def close_editor(value: bool) -> None
```

<a id="unreal.MoviePipelineInProcessExecutorSettings.additional_command_line_arguments"></a>

#### additional_command_line_arguments

```python
@property
def additional_command_line_arguments() -> str
```

(str):  [Read-Write] A list of additional command line arguments to be appended to the new process startup. In the form of "-foo -bar=baz". Can be useful if your game requires certain arguments to start such as disabling log-in screens.

<a id="unreal.MoviePipelineInProcessExecutorSettings.additional_command_line_arguments"></a>

#### additional_command_line_arguments

```python
@additional_command_line_arguments.setter
def additional_command_line_arguments(value: str) -> None
```

<a id="unreal.MoviePipelineInProcessExecutorSettings.inherited_command_line_arguments"></a>

#### inherited_command_line_arguments

```python
@property
def inherited_command_line_arguments() -> str
```

(str):  [Read-Only] A list of command line arguments which are inherited from the currently running Editor instance that will be automatically appended to the new process.

<a id="unreal.MoviePipelineInProcessExecutorSettings.initial_delay_frame_count"></a>

#### initial_delay_frame_count

```python
@property
def initial_delay_frame_count() -> int
```

(int32):  [Read-Write] How long should we wait after being initialized to start doing any work? This can be used
to work around situations where the game is not fully loaded by the time the pipeline
is automatically started and it is important that the game is fully loaded before we do
any work (such as evaluating frames for warm-up).

<a id="unreal.MoviePipelineInProcessExecutorSettings.initial_delay_frame_count"></a>

#### initial_delay_frame_count

```python
@initial_delay_frame_count.setter
def initial_delay_frame_count(value: int) -> None
```

<a id="unreal.MoviePipelineOutputBase"></a>