## PCGQualitySelectSettings Objects

```python
class PCGQualitySelectSettings(PCGSettings)
```

Selects from input pins based on 'pcg.Quality' setting.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGQualitySelect.h

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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_cinematic_pin`` (bool):  [Read-Write]
- ``use_epic_pin`` (bool):  [Read-Write]
- ``use_high_pin`` (bool):  [Read-Write]
- ``use_low_pin`` (bool):  [Read-Write]
- ``use_medium_pin`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGQualitySelectSettings.use_low_pin"></a>

#### use_low_pin

```python
@property
def use_low_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGQualitySelectSettings.use_low_pin"></a>

#### use_low_pin

```python
@use_low_pin.setter
def use_low_pin(value: bool) -> None
```

<a id="unreal.PCGQualitySelectSettings.use_medium_pin"></a>

#### use_medium_pin

```python
@property
def use_medium_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGQualitySelectSettings.use_medium_pin"></a>

#### use_medium_pin

```python
@use_medium_pin.setter
def use_medium_pin(value: bool) -> None
```

<a id="unreal.PCGQualitySelectSettings.use_high_pin"></a>

#### use_high_pin

```python
@property
def use_high_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGQualitySelectSettings.use_high_pin"></a>

#### use_high_pin

```python
@use_high_pin.setter
def use_high_pin(value: bool) -> None
```

<a id="unreal.PCGQualitySelectSettings.use_epic_pin"></a>

#### use_epic_pin

```python
@property
def use_epic_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGQualitySelectSettings.use_epic_pin"></a>

#### use_epic_pin

```python
@use_epic_pin.setter
def use_epic_pin(value: bool) -> None
```

<a id="unreal.PCGQualitySelectSettings.use_cinematic_pin"></a>

#### use_cinematic_pin

```python
@property
def use_cinematic_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGQualitySelectSettings.use_cinematic_pin"></a>

#### use_cinematic_pin

```python
@use_cinematic_pin.setter
def use_cinematic_pin(value: bool) -> None
```

<a id="unreal.PCGRandomChoiceSettings"></a>