## PCGSampleTextureSettings Objects

```python
class PCGSampleTextureSettings(PCGSettings)
```

Samples color of texture at each point.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSampleTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``clamp_output_density`` (bool):  [Read-Write] Controls whether the output density should be clamped or not.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``density_merge_function`` (PCGDensityMergeOperation):  [Read-Write] Controls the behavior of density computation with respect to initial data.
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``texture_mapping_method`` (PCGTextureMappingMethod):  [Read-Write] Whether to treat the sample positions as being in 0-1 UV space. If method is Planar then the coordinates will be transformed according to the texture settings.
- ``tiling_mode`` (PCGTextureAddressMode):  [Read-Write] Overrides the texture's tiling to wrap or clamp its UVs.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``uv_coordinates_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The attribute that provides sample positions for sampling the texture.

<a id="unreal.PCGSampleTextureSettings.texture_mapping_method"></a>

#### texture_mapping_method

```python
@property
def texture_mapping_method() -> PCGTextureMappingMethod
```

(PCGTextureMappingMethod):  [Read-Write] Whether to treat the sample positions as being in 0-1 UV space. If method is Planar then the coordinates will be transformed according to the texture settings.

<a id="unreal.PCGSampleTextureSettings.texture_mapping_method"></a>

#### texture_mapping_method

```python
@texture_mapping_method.setter
def texture_mapping_method(value: PCGTextureMappingMethod) -> None
```

<a id="unreal.PCGSampleTextureSettings.uv_coordinates_attribute"></a>

#### uv_coordinates_attribute

```python
@property
def uv_coordinates_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The attribute that provides sample positions for sampling the texture.

<a id="unreal.PCGSampleTextureSettings.uv_coordinates_attribute"></a>

#### uv_coordinates_attribute

```python
@uv_coordinates_attribute.setter
def uv_coordinates_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSampleTextureSettings.tiling_mode"></a>

#### tiling_mode

```python
@property
def tiling_mode() -> PCGTextureAddressMode
```

(PCGTextureAddressMode):  [Read-Write] Overrides the texture's tiling to wrap or clamp its UVs.

<a id="unreal.PCGSampleTextureSettings.tiling_mode"></a>

#### tiling_mode

```python
@tiling_mode.setter
def tiling_mode(value: PCGTextureAddressMode) -> None
```

<a id="unreal.PCGSampleTextureSettings.density_merge_function"></a>

#### density_merge_function

```python
@property
def density_merge_function() -> PCGDensityMergeOperation
```

(PCGDensityMergeOperation):  [Read-Write] Controls the behavior of density computation with respect to initial data.

<a id="unreal.PCGSampleTextureSettings.density_merge_function"></a>

#### density_merge_function

```python
@density_merge_function.setter
def density_merge_function(value: PCGDensityMergeOperation) -> None
```

<a id="unreal.PCGSampleTextureSettings.clamp_output_density"></a>

#### clamp_output_density

```python
@property
def clamp_output_density() -> bool
```

(bool):  [Read-Write] Controls whether the output density should be clamped or not.

<a id="unreal.PCGSampleTextureSettings.clamp_output_density"></a>

#### clamp_output_density

```python
@clamp_output_density.setter
def clamp_output_density(value: bool) -> None
```

<a id="unreal.PCGSanityCheckPointDataSettings"></a>