## PCGIndirectionSettings Objects

```python
class PCGIndirectionSettings(PCGSettings)
```

PCGIndirection Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGIndirectionElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blueprint_element_class`` (type(Class)):  [Read-Write] The blueprint element class used to define the pin interface for this node instance
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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``proxy_interface_mode`` (PCGProxyInterfaceMode):  [Read-Write] Defines which interface to use for populating pins
- ``seed`` (int32):  [Read-Write]
- ``settings`` (PCGSettings):  [Read-Write] The element settings, which can be overriden, that will be used during the proxy execution
- ``settings_class`` (type(Class)):  [Read-Write] The element settings class used to define the pin interface for this node instance
- ``tag_outputs_based_on_output_pins`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGIndirectionSettings.proxy_interface_mode"></a>

#### proxy_interface_mode

```python
@property
def proxy_interface_mode() -> PCGProxyInterfaceMode
```

(PCGProxyInterfaceMode):  [Read-Write] Defines which interface to use for populating pins

<a id="unreal.PCGIndirectionSettings.proxy_interface_mode"></a>

#### proxy_interface_mode

```python
@proxy_interface_mode.setter
def proxy_interface_mode(value: PCGProxyInterfaceMode) -> None
```

<a id="unreal.PCGIndirectionSettings.settings"></a>

#### settings

```python
@property
def settings() -> PCGSettings
```

(PCGSettings):  [Read-Write] The element settings, which can be overriden, that will be used during the proxy execution

<a id="unreal.PCGIndirectionSettings.settings"></a>

#### settings

```python
@settings.setter
def settings(value: PCGSettings) -> None
```

<a id="unreal.PCGIndirectionSettings.tag_outputs_based_on_output_pins"></a>

#### tag_outputs_based_on_output_pins

```python
@property
def tag_outputs_based_on_output_pins() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGIndirectionSettings.tag_outputs_based_on_output_pins"></a>

#### tag_outputs_based_on_output_pins

```python
@tag_outputs_based_on_output_pins.setter
def tag_outputs_based_on_output_pins(value: bool) -> None
```

<a id="unreal.PCGInnerIntersectionSettings"></a>