## PCGPrintElementSettings Objects

```python
class PCGPrintElementSettings(PCGSettings)
```

Issues a specified message to the log, and optionally to the graph and/or screen.
Note: This node will not function in shipping builds.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPrintElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``custom_prefix`` (str):  [Read-Write] A prefix to which the core message will be appended.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``display_on_node`` (bool):  [Read-Write] Display warnings or errors on this node.
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enable_print`` (bool):  [Read-Write] Enable the functionality of this node. Disable to bypass printing.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``prefix_with_component`` (bool):  [Read-Write] Prefix the message with the name of the component.
- ``prefix_with_graph`` (bool):  [Read-Write] Prefix the message with the name of the graph.
- ``prefix_with_node`` (bool):  [Read-Write] Prefix the message with the name of the node.
- ``prefix_with_owner`` (bool):  [Read-Write] Prefix the message with the name of the component's owner.
- ``print_per_component`` (bool):  [Read-Write] Use the component as part of the key hash and print a message for each component with this node.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``print_string`` (str):  [Read-Write] The core message to print to the logger, graph, and/or screen.
- ``print_to_screen`` (bool):  [Read-Write] Print the message to the editor viewport.
- ``print_to_screen_color`` (Color):  [Read-Write] The color of the on screen message.
- ``print_to_screen_duration`` (double):  [Read-Write] The duration (in seconds) of the on screen message.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``verbosity`` (PCGPrintVerbosity):  [Read-Write] The verbosity level of the printed message.

<a id="unreal.PCGPrintElementSettings.print_string"></a>

#### print_string

```python
@property
def print_string() -> str
```

(str):  [Read-Write] The core message to print to the logger, graph, and/or screen.

<a id="unreal.PCGPrintElementSettings.print_string"></a>

#### print_string

```python
@print_string.setter
def print_string(value: str) -> None
```

<a id="unreal.PCGPrintElementSettings.verbosity"></a>

#### verbosity

```python
@property
def verbosity() -> PCGPrintVerbosity
```

(PCGPrintVerbosity):  [Read-Write] The verbosity level of the printed message.

<a id="unreal.PCGPrintElementSettings.verbosity"></a>

#### verbosity

```python
@verbosity.setter
def verbosity(value: PCGPrintVerbosity) -> None
```

<a id="unreal.PCGPrintElementSettings.custom_prefix"></a>

#### custom_prefix

```python
@property
def custom_prefix() -> str
```

(str):  [Read-Write] A prefix to which the core message will be appended.

<a id="unreal.PCGPrintElementSettings.custom_prefix"></a>

#### custom_prefix

```python
@custom_prefix.setter
def custom_prefix(value: str) -> None
```

<a id="unreal.PCGPrintElementSettings.display_on_node"></a>

#### display_on_node

```python
@property
def display_on_node() -> bool
```

(bool):  [Read-Write] Display warnings or errors on this node.

<a id="unreal.PCGPrintElementSettings.display_on_node"></a>

#### display_on_node

```python
@display_on_node.setter
def display_on_node(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.print_per_component"></a>

#### print_per_component

```python
@property
def print_per_component() -> bool
```

(bool):  [Read-Write] Use the component as part of the key hash and print a message for each component with this node.

<a id="unreal.PCGPrintElementSettings.print_per_component"></a>

#### print_per_component

```python
@print_per_component.setter
def print_per_component(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.print_to_screen"></a>

#### print_to_screen

```python
@property
def print_to_screen() -> bool
```

(bool):  [Read-Write] Print the message to the editor viewport.

<a id="unreal.PCGPrintElementSettings.print_to_screen"></a>

#### print_to_screen

```python
@print_to_screen.setter
def print_to_screen(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.print_to_screen_duration"></a>

#### print_to_screen_duration

```python
@property
def print_to_screen_duration() -> float
```

(double):  [Read-Write] The duration (in seconds) of the on screen message.

<a id="unreal.PCGPrintElementSettings.print_to_screen_duration"></a>

#### print_to_screen_duration

```python
@print_to_screen_duration.setter
def print_to_screen_duration(value: float) -> None
```

<a id="unreal.PCGPrintElementSettings.print_to_screen_color"></a>

#### print_to_screen_color

```python
@property
def print_to_screen_color() -> Color
```

(Color):  [Read-Write] The color of the on screen message.

<a id="unreal.PCGPrintElementSettings.print_to_screen_color"></a>

#### print_to_screen_color

```python
@print_to_screen_color.setter
def print_to_screen_color(value: Color) -> None
```

<a id="unreal.PCGPrintElementSettings.prefix_with_owner"></a>

#### prefix_with_owner

```python
@property
def prefix_with_owner() -> bool
```

(bool):  [Read-Write] Prefix the message with the name of the component's owner.

<a id="unreal.PCGPrintElementSettings.prefix_with_owner"></a>

#### prefix_with_owner

```python
@prefix_with_owner.setter
def prefix_with_owner(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.prefix_with_component"></a>

#### prefix_with_component

```python
@property
def prefix_with_component() -> bool
```

(bool):  [Read-Write] Prefix the message with the name of the component.

<a id="unreal.PCGPrintElementSettings.prefix_with_component"></a>

#### prefix_with_component

```python
@prefix_with_component.setter
def prefix_with_component(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.prefix_with_graph"></a>

#### prefix_with_graph

```python
@property
def prefix_with_graph() -> bool
```

(bool):  [Read-Write] Prefix the message with the name of the graph.

<a id="unreal.PCGPrintElementSettings.prefix_with_graph"></a>

#### prefix_with_graph

```python
@prefix_with_graph.setter
def prefix_with_graph(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.prefix_with_node"></a>

#### prefix_with_node

```python
@property
def prefix_with_node() -> bool
```

(bool):  [Read-Write] Prefix the message with the name of the node.

<a id="unreal.PCGPrintElementSettings.prefix_with_node"></a>

#### prefix_with_node

```python
@prefix_with_node.setter
def prefix_with_node(value: bool) -> None
```

<a id="unreal.PCGPrintElementSettings.enable_print"></a>

#### enable_print

```python
@property
def enable_print() -> bool
```

(bool):  [Read-Write] Enable the functionality of this node. Disable to bypass printing.

<a id="unreal.PCGPrintElementSettings.enable_print"></a>

#### enable_print

```python
@enable_print.setter
def enable_print(value: bool) -> None
```

<a id="unreal.PCGPrintGrammarSettings"></a>