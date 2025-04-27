## PCGNormalToDensitySettings Objects

```python
class PCGNormalToDensitySettings(PCGSettings)
```

Finds the angle against the specified direction and applies that to the density

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGNormalToDensity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``density_mode`` (PCGNormalToDensityMode):  [Read-Write] The operator to apply to the output density
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``normal`` (Vector):  [Read-Write] The normal to compare against
- ``offset`` (double):  [Read-Write] This is biases the value towards or against the normal (positive or negative)
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``strength`` (double):  [Read-Write] This applies a curve to scale the result density with Result = Result^(1/Strength)
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGNormalToDensitySettings.normal"></a>

#### normal

```python
@property
def normal() -> Vector
```

(Vector):  [Read-Write] The normal to compare against

<a id="unreal.PCGNormalToDensitySettings.normal"></a>

#### normal

```python
@normal.setter
def normal(value: Vector) -> None
```

<a id="unreal.PCGNormalToDensitySettings.offset"></a>

#### offset

```python
@property
def offset() -> float
```

(double):  [Read-Write] This is biases the value towards or against the normal (positive or negative)

<a id="unreal.PCGNormalToDensitySettings.offset"></a>

#### offset

```python
@offset.setter
def offset(value: float) -> None
```

<a id="unreal.PCGNormalToDensitySettings.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(double):  [Read-Write] This applies a curve to scale the result density with Result = Result^(1/Strength)

<a id="unreal.PCGNormalToDensitySettings.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.PCGNormalToDensitySettings.density_mode"></a>

#### density_mode

```python
@property
def density_mode() -> PCGNormalToDensityMode
```

(PCGNormalToDensityMode):  [Read-Write] The operator to apply to the output density

<a id="unreal.PCGNormalToDensitySettings.density_mode"></a>

#### density_mode

```python
@density_mode.setter
def density_mode(value: PCGNormalToDensityMode) -> None
```

<a id="unreal.PCGNumberOfElementsBaseSettings"></a>