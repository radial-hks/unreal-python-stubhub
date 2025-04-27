## PCGBooleanOperationSettings Objects

```python
class PCGBooleanOperationSettings(PCGDynamicMeshBaseSettings)
```

Do a boolean operation between dynamic meshes.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGBooleanOperation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``boolean_operation`` (GeometryScriptBooleanOperation):  [Read-Write]
- ``boolean_operation_options`` (GeometryScriptMeshBooleanOptions):  [Read-Write]
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
- ``mode`` (PCGBooleanOperationMode):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``tag_inheritance_mode`` (PCGBooleanOperationTagInheritanceMode):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGBooleanOperationSettings.boolean_operation"></a>

#### boolean_operation

```python
@property
def boolean_operation() -> GeometryScriptBooleanOperation
```

(GeometryScriptBooleanOperation):  [Read-Write]

<a id="unreal.PCGBooleanOperationSettings.boolean_operation"></a>

#### boolean_operation

```python
@boolean_operation.setter
def boolean_operation(value: GeometryScriptBooleanOperation) -> None
```

<a id="unreal.PCGBooleanOperationSettings.boolean_operation_options"></a>

#### boolean_operation_options

```python
@property
def boolean_operation_options() -> GeometryScriptMeshBooleanOptions
```

(GeometryScriptMeshBooleanOptions):  [Read-Write]

<a id="unreal.PCGBooleanOperationSettings.boolean_operation_options"></a>

#### boolean_operation_options

```python
@boolean_operation_options.setter
def boolean_operation_options(value: GeometryScriptMeshBooleanOptions) -> None
```

<a id="unreal.PCGBooleanOperationSettings.tag_inheritance_mode"></a>

#### tag_inheritance_mode

```python
@property
def tag_inheritance_mode() -> PCGBooleanOperationTagInheritanceMode
```

(PCGBooleanOperationTagInheritanceMode):  [Read-Write]

<a id="unreal.PCGBooleanOperationSettings.tag_inheritance_mode"></a>

#### tag_inheritance_mode

```python
@tag_inheritance_mode.setter
def tag_inheritance_mode(value: PCGBooleanOperationTagInheritanceMode) -> None
```

<a id="unreal.PCGBooleanOperationSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGBooleanOperationMode
```

(PCGBooleanOperationMode):  [Read-Write]

<a id="unreal.PCGBooleanOperationSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGBooleanOperationMode) -> None
```

<a id="unreal.PCGCreateEmptyDynamicMeshSettings"></a>