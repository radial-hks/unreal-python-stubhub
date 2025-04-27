## MoviePipelineSetting Objects

```python
class MoviePipelineSetting(Object)
```

A base class for all Movie Render Pipeline settings.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineSetting.h

<a id="unreal.MoviePipelineSetting.set_is_enabled"></a>

#### set_is_enabled

```python
def set_is_enabled(enabled: bool) -> None
```

x.set_is_enabled(enabled) -> None
Set Is Enabled

Args:
    enabled (bool):

<a id="unreal.MoviePipelineSetting.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
Is this setting enabled by the user in the UI?

Returns:
    bool:

<a id="unreal.MoviePipelineSetting.build_new_process_command_line_args"></a>

#### build_new_process_command_line_args

```python
def build_new_process_command_line_args(
    out_unreal_url_params: Array[str], out_command_line_args: Array[str],
    out_device_profile_cvars: Array[str], out_exec_cmds: Array[str]
) -> Tuple[Array[str], Array[str], Array[str], Array[str]]
```

x.build_new_process_command_line_args(out_unreal_url_params, out_command_line_args, out_device_profile_cvars, out_exec_cmds) -> (out_unreal_url_params=Array[str], out_command_line_args=Array[str], out_device_profile_cvars=Array[str], out_exec_cmds=Array[str])
When rendering in a new process some settings may need to provide command line arguments
to affect engine settings that need to be set before most of the engine boots up. This function
allows a setting to provide these when the user wants to run in a separate process. This won't
be used when running in the current process because it is too late to modify the command line.

Args:
    out_unreal_url_params (Array[str]): 
    out_command_line_args (Array[str]): 
    out_device_profile_cvars (Array[str]): 
    out_exec_cmds (Array[str]): 

Returns:
    tuple: 

    out_unreal_url_params (Array[str]): 

    out_command_line_args (Array[str]): 

    out_device_profile_cvars (Array[str]): 

    out_exec_cmds (Array[str]):

<a id="unreal.MoviePipelineHighResSetting"></a>