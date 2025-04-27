## PCGCustomHLSLSettings Objects

```python
class PCGCustomHLSLSettings(PCGSettings)
```

Produces a HLSL compute shader which will be executed on the GPU.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCustomHLSL.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dispatch_thread_count`` (PCGDispatchThreadCount):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``fixed_thread_count`` (int32):  [Read-Write]
- ``helper_declarations`` (str):  [Read-Only] Helper data and functions that can be used from the shader code. Intended to be viewed using the Node Source Editor window.
- ``input_declarations`` (str):  [Read-Only] Inputs data accessors that can be used from the shader code. Intended to be viewed using the Node Source Editor window.
- ``input_pins`` (Array[PCGPinProperties]):  [Read-Write]
- ``kernel_type`` (PCGKernelType):  [Read-Write]
- ``mute_unwritten_pin_data_errors`` (bool):  [Read-Write] Mute uninitialized data warnings.
- ``output_declarations`` (str):  [Read-Only] Output data accessors that can be used from the shader code. Intended to be viewed using the Node Source Editor window.
- ``output_pins`` (Array[PCGPinPropertiesGPU]):  [Read-Write]
- ``point_count`` (int32):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``shader_functions`` (str):  [Read-Write] Optional functions that can be called from the source. Intended to be edited using the Node Source Editor window.
- ``shader_source`` (str):  [Read-Write] Shader code that forms the body of the kernel. Intended to be edited using the Node Source Editor window.
- ``thread_count_input_pin_labels`` (Array[Name]):  [Read-Write]
- ``thread_count_multiplier`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCollisionWrapperData"></a>