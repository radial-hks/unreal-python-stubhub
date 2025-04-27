## PCGBoundsModifierSettings Objects

```python
class PCGBoundsModifierSettings(PCGSettings)
```

This class controls/sets up a node that modifies the min/max bounds of the input points.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGBoundsModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_steepness`` (bool):  [Read-Write]
- ``bounds_max`` (Vector):  [Read-Write]
- ``bounds_min`` (Vector):  [Read-Write]
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
- ``mode`` (PCGBoundsModifierMode):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``steepness`` (float):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGBoundsModifierSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGBoundsModifierMode
```

(PCGBoundsModifierMode):  [Read-Write]

<a id="unreal.PCGBoundsModifierSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGBoundsModifierMode) -> None
```

<a id="unreal.PCGBoundsModifierSettings.bounds_min"></a>

#### bounds_min

```python
@property
def bounds_min() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGBoundsModifierSettings.bounds_min"></a>

#### bounds_min

```python
@bounds_min.setter
def bounds_min(value: Vector) -> None
```

<a id="unreal.PCGBoundsModifierSettings.bounds_max"></a>

#### bounds_max

```python
@property
def bounds_max() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGBoundsModifierSettings.bounds_max"></a>

#### bounds_max

```python
@bounds_max.setter
def bounds_max(value: Vector) -> None
```

<a id="unreal.PCGBoundsModifierSettings.affect_steepness"></a>

#### affect_steepness

```python
@property
def affect_steepness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGBoundsModifierSettings.affect_steepness"></a>

#### affect_steepness

```python
@affect_steepness.setter
def affect_steepness(value: bool) -> None
```

<a id="unreal.PCGBoundsModifierSettings.steepness"></a>

#### steepness

```python
@property
def steepness() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGBoundsModifierSettings.steepness"></a>

#### steepness

```python
@steepness.setter
def steepness(value: float) -> None
```

<a id="unreal.PCGCollapseSettings"></a>