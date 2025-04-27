## PCGLoopSettings Objects

```python
class PCGLoopSettings(PCGSubgraphSettings)
```

PCGLoop Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGLoopElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``feedback_pins`` (str):  [Read-Write] Comma-separated list of pin names that will act as feedback pins, namely that in a given iteration it will receive the data from the output pin of the same name of the previous loop iteration.
  These pins can have initial data, in which case only the first iteration will get this data.
- ``loop_pins`` (str):  [Read-Write] Comma-separated list of pin names on which we will loop by-element in a step-wise fashion; if more than one is provided, it is expected that they all have the same number of data.
  If none are provided, the first connected pin will taken as the pin to loop on.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``subgraph_instance`` (PCGGraphInstance):  [Read-Only]
- ``subgraph_override`` (PCGGraphInterface):  [Read-Write]
- ``tokenize_on_white_space`` (bool):  [Read-Write]
- ``use_graph_default_pin_usage`` (bool):  [Read-Write] Controls whether the pin usage (normal, loop, feedback) will be taken from the subgraph to execute or from the manually provided list.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGLoopSettings.use_graph_default_pin_usage"></a>

#### use_graph_default_pin_usage

```python
@property
def use_graph_default_pin_usage() -> bool
```

(bool):  [Read-Write] Controls whether the pin usage (normal, loop, feedback) will be taken from the subgraph to execute or from the manually provided list.

<a id="unreal.PCGLoopSettings.use_graph_default_pin_usage"></a>

#### use_graph_default_pin_usage

```python
@use_graph_default_pin_usage.setter
def use_graph_default_pin_usage(value: bool) -> None
```

<a id="unreal.PCGLoopSettings.loop_pins"></a>

#### loop_pins

```python
@property
def loop_pins() -> str
```

(str):  [Read-Write] Comma-separated list of pin names on which we will loop by-element in a step-wise fashion; if more than one is provided, it is expected that they all have the same number of data.
If none are provided, the first connected pin will taken as the pin to loop on.

<a id="unreal.PCGLoopSettings.loop_pins"></a>

#### loop_pins

```python
@loop_pins.setter
def loop_pins(value: str) -> None
```

<a id="unreal.PCGLoopSettings.feedback_pins"></a>

#### feedback_pins

```python
@property
def feedback_pins() -> str
```

(str):  [Read-Write] Comma-separated list of pin names that will act as feedback pins, namely that in a given iteration it will receive the data from the output pin of the same name of the previous loop iteration.
These pins can have initial data, in which case only the first iteration will get this data.

<a id="unreal.PCGLoopSettings.feedback_pins"></a>

#### feedback_pins

```python
@feedback_pins.setter
def feedback_pins(value: str) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings"></a>