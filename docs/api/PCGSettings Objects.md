## PCGSettings Objects

```python
class PCGSettings(PCGSettingsInterface)
```

Base class for settings-as-data in the PCG framework

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSettings.h

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
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSettings.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSettings.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.PCGSettings.determinism_settings"></a>

#### determinism_settings

```python
@property
def determinism_settings() -> PCGDeterminismSettings
```

(PCGDeterminismSettings):  [Read-Write]

<a id="unreal.PCGSettings.determinism_settings"></a>

#### determinism_settings

```python
@determinism_settings.setter
def determinism_settings(value: PCGDeterminismSettings) -> None
```

<a id="unreal.PCGSettings.expose_to_library"></a>

#### expose_to_library

```python
@property
def expose_to_library() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSettings.expose_to_library"></a>

#### expose_to_library

```python
@expose_to_library.setter
def expose_to_library(value: bool) -> None
```

<a id="unreal.PCGSettings.category"></a>

#### category

```python
@property
def category() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PCGSettings.category"></a>

#### category

```python
@category.setter
def category(value: Text) -> None
```

<a id="unreal.PCGSettings.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Write]

<a id="unreal.PCGSettings.description"></a>

#### description

```python
@description.setter
def description(value: Text) -> None
```

<a id="unreal.PCGSettings.use_seed"></a>

#### use_seed

```python
@property
def use_seed() -> bool
```

(bool):  [Read-Write]
deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSettings.use_seed"></a>

#### use_seed

```python
@use_seed.setter
def use_seed(value: bool) -> None
```

<a id="unreal.PCGSettings.bp_get_type_union_of_incident_edges"></a>

#### bp_get_type_union_of_incident_edges

```python
def bp_get_type_union_of_incident_edges(pin_label: Name) -> int
```

x.bp_get_type_union_of_incident_edges(pin_label) -> int32
Bitwise union of the allowed types of each incident edge on pin. Returns None type if no common bits, or no edges. Use the BP function helpers to extract the types from the result.

Args:
    pin_label (Name): 

Returns:
    int32:

<a id="unreal.PCGAddComponentSettings"></a>