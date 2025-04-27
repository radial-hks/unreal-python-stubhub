## PCGWriteToNiagaraDataChannelSettings Objects

```python
class PCGWriteToNiagaraDataChannelSettings(PCGSettings)
```

Allow writing attributes to a Niagara Data Channel.

**C++ Source:**

- **Plugin**: PCGNiagaraInterop
- **Module**: PCGNiagaraInterop
- **File**: PCGWriteToNiagaraDataChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``data_channel`` (NiagaraDataChannelAsset):  [Read-Write]
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
- ``niagara_variables_pcg_attribute_mapping`` (Map[Name, PCGAttributePropertyInputSelector]):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``visible_to_cpu`` (bool):  [Read-Write] Data written to this data channel is visible to Niagara CPU emitters
- ``visible_to_game`` (bool):  [Read-Write] Data written to this data channel is visible to Blueprint and C++ logic reading from it
- ``visible_to_gpu`` (bool):  [Read-Write] Data written to this data channel is visible to Niagara GPU emitters

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.data_channel"></a>

#### data_channel

```python
@property
def data_channel() -> NiagaraDataChannelAsset
```

(NiagaraDataChannelAsset):  [Read-Write]

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.data_channel"></a>

#### data_channel

```python
@data_channel.setter
def data_channel(value: NiagaraDataChannelAsset) -> None
```

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.niagara_variables_pcg_attribute_mapping"></a>

#### niagara_variables_pcg_attribute_mapping

```python
@property
def niagara_variables_pcg_attribute_mapping(
) -> Map[Name, PCGAttributePropertyInputSelector]
```

(Map[Name, PCGAttributePropertyInputSelector]):  [Read-Write]

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.niagara_variables_pcg_attribute_mapping"></a>

#### niagara_variables_pcg_attribute_mapping

```python
@niagara_variables_pcg_attribute_mapping.setter
def niagara_variables_pcg_attribute_mapping(
        value: Map[Name, PCGAttributePropertyInputSelector]) -> None
```

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.visible_to_game"></a>

#### visible_to_game

```python
@property
def visible_to_game() -> bool
```

(bool):  [Read-Write] Data written to this data channel is visible to Blueprint and C++ logic reading from it

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.visible_to_game"></a>

#### visible_to_game

```python
@visible_to_game.setter
def visible_to_game(value: bool) -> None
```

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.visible_to_cpu"></a>

#### visible_to_cpu

```python
@property
def visible_to_cpu() -> bool
```

(bool):  [Read-Write] Data written to this data channel is visible to Niagara CPU emitters

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.visible_to_cpu"></a>

#### visible_to_cpu

```python
@visible_to_cpu.setter
def visible_to_cpu(value: bool) -> None
```

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.visible_to_gpu"></a>

#### visible_to_gpu

```python
@property
def visible_to_gpu() -> bool
```

(bool):  [Read-Write] Data written to this data channel is visible to Niagara GPU emitters

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.visible_to_gpu"></a>

#### visible_to_gpu

```python
@visible_to_gpu.setter
def visible_to_gpu(value: bool) -> None
```

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGWriteToNiagaraDataChannelSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGWaterSplineData"></a>