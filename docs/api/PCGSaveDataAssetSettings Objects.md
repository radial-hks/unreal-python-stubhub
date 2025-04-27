## PCGSaveDataAssetSettings Objects

```python
class PCGSaveDataAssetSettings(PCGSettings)
```

Node that will save input data to a PCG data asset

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSaveAssetElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_color`` (LinearColor):  [Read-Write]
- ``asset_description`` (str):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``custom_data_collection_exporter_class`` (type(Class)):  [Read-Write]
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
- ``params`` (PCGAssetExporterParameters):  [Read-Write]
- ``pins`` (Array[PCGPinProperties]):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSaveDataAssetSettings.pins"></a>

#### pins

```python
@property
def pins() -> Array[PCGPinProperties]
```

(Array[PCGPinProperties]):  [Read-Write]

<a id="unreal.PCGSaveDataAssetSettings.pins"></a>

#### pins

```python
@pins.setter
def pins(value: Array[PCGPinProperties]) -> None
```

<a id="unreal.PCGSaveDataAssetSettings.custom_data_collection_exporter_class"></a>

#### custom_data_collection_exporter_class

```python
@property
def custom_data_collection_exporter_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.PCGSaveDataAssetSettings.custom_data_collection_exporter_class"></a>

#### custom_data_collection_exporter_class

```python
@custom_data_collection_exporter_class.setter
def custom_data_collection_exporter_class(value: Class) -> None
```

<a id="unreal.PCGSaveDataAssetSettings.params"></a>

#### params

```python
@property
def params() -> PCGAssetExporterParameters
```

(PCGAssetExporterParameters):  [Read-Write]

<a id="unreal.PCGSaveDataAssetSettings.params"></a>

#### params

```python
@params.setter
def params(value: PCGAssetExporterParameters) -> None
```

<a id="unreal.PCGSaveDataAssetSettings.asset_description"></a>

#### asset_description

```python
@property
def asset_description() -> str
```

(str):  [Read-Write]

<a id="unreal.PCGSaveDataAssetSettings.asset_description"></a>

#### asset_description

```python
@asset_description.setter
def asset_description(value: str) -> None
```

<a id="unreal.PCGSaveDataAssetSettings.asset_color"></a>

#### asset_color

```python
@property
def asset_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.PCGSaveDataAssetSettings.asset_color"></a>

#### asset_color

```python
@asset_color.setter
def asset_color(value: LinearColor) -> None
```

<a id="unreal.PCGSchedulingPolicyBase"></a>