## MetasoundGeneratorHandle Objects

```python
class MetasoundGeneratorHandle(Object)
```

Blueprint-facing interface to a FMetasoundGenerator on a UAudioComponent.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundGeneratorHandle.h

<a id="unreal.MetasoundGeneratorHandle.watch_output"></a>

#### watch_output

```python
def watch_output(output_name: Name,
                 on_output_value_changed: OnMetasoundOutputValueChanged,
                 analyzer_name: Name = "None",
                 analyzer_output_name: Name = "None") -> bool
```

x.watch_output(output_name, on_output_value_changed, analyzer_name="None", analyzer_output_name="None") -> bool
Watch an output value.

Args:
    output_name (Name): The user-specified name of the output in the Metasound
    on_output_value_changed (OnMetasoundOutputValueChanged): The event to fire when the output's value changes
    analyzer_name (Name): (optional) The name of the analyzer to use on the output, defaults to a passthrough
    analyzer_output_name (Name): (optional) The name of the output on the analyzer to watch, defaults to the passthrough output

Returns:
    bool: true if the watch setup succeeded, false otherwise

<a id="unreal.MetasoundGeneratorHandle.update_watchers"></a>

#### update_watchers

```python
def update_watchers() -> None
```

x.update_watchers() -> None
Update Watchers

<a id="unreal.MetasoundGeneratorHandle.get_cpu_core_utilization"></a>

#### get_cpu_core_utilization

```python
def get_cpu_core_utilization() -> float
```

x.get_cpu_core_utilization() -> double
Get the CPU usage as "fraction of real time" used to render this metasound.
NOTE: The MetasoundSource asset MUST have had its EnableRenderTiming function called
before the metasound is started!

Returns:
    double:

<a id="unreal.MetasoundGeneratorHandle.enable_runtime_render_timing"></a>

#### enable_runtime_render_timing

```python
def enable_runtime_render_timing(enable: bool) -> None
```

x.enable_runtime_render_timing(enable) -> None
Enable the profiling of the MetaSound render for this playing instance. You
must call this before calling "GetRuntimeCPUCoreUtilization" (below) or you will just
get 0.0 back for core utilization.

Args:
    enable (bool):

<a id="unreal.MetasoundGeneratorHandle.create_meta_sound_generator_handle"></a>

#### create_meta_sound_generator_handle

```python
@classmethod
def create_meta_sound_generator_handle(
        cls, on_component: AudioComponent) -> MetasoundGeneratorHandle
```

X.create_meta_sound_generator_handle(on_component) -> MetasoundGeneratorHandle
Create Meta Sound Generator Handle

Args:
    on_component (AudioComponent): 

Returns:
    MetasoundGeneratorHandle:

<a id="unreal.MetasoundGeneratorHandle.apply_parameter_pack"></a>

#### apply_parameter_pack

```python
def apply_parameter_pack(pack: MetasoundParameterPack) -> bool
```

x.apply_parameter_pack(pack) -> bool
Makes a copy of the supplied parameter pack and passes it to the MetaSoundGenerator
for asynchronous processing. IT ALSO caches this copy so that if the AudioComponent
is virtualized the parameter pack will be sent again when/if the AudioComponent is
"unvirtualized".

Args:
    pack (MetasoundParameterPack): 

Returns:
    bool:

<a id="unreal.AudioEngineSubsystem"></a>