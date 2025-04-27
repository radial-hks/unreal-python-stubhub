## PCGCreateCollisionDataSettings Objects

```python
class PCGCreateCollisionDataSettings(PCGSettings)
```

PCGCreate Collision Data Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreateCollisionData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``collision_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``collision_query_flag`` (PCGCollisionQueryFlag):  [Read-Write] Controls how shapes are selected from collision. Performance warning on using complex shapes.
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
- ``synchronous_load`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``warn_if_attribute_could_not_be_used`` (bool):  [Read-Write]

<a id="unreal.PCGCreateCollisionDataSettings.collision_attribute"></a>

#### collision_attribute

```python
@property
def collision_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGCreateCollisionDataSettings.collision_attribute"></a>

#### collision_attribute

```python
@collision_attribute.setter
def collision_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGCreateCollisionDataSettings.collision_query_flag"></a>

#### collision_query_flag

```python
@property
def collision_query_flag() -> PCGCollisionQueryFlag
```

(PCGCollisionQueryFlag):  [Read-Write] Controls how shapes are selected from collision. Performance warning on using complex shapes.

<a id="unreal.PCGCreateCollisionDataSettings.collision_query_flag"></a>

#### collision_query_flag

```python
@collision_query_flag.setter
def collision_query_flag(value: PCGCollisionQueryFlag) -> None
```

<a id="unreal.PCGCreateCollisionDataSettings.warn_if_attribute_could_not_be_used"></a>

#### warn_if_attribute_could_not_be_used

```python
@property
def warn_if_attribute_could_not_be_used() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGCreateCollisionDataSettings.warn_if_attribute_could_not_be_used"></a>

#### warn_if_attribute_could_not_be_used

```python
@warn_if_attribute_could_not_be_used.setter
def warn_if_attribute_could_not_be_used(value: bool) -> None
```

<a id="unreal.PCGCreateCollisionDataSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGCreateCollisionDataSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGCreatePointsSphereSettings"></a>