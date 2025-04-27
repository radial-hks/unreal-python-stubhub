## PCGLoadDataAssetSettings Objects

```python
class PCGLoadDataAssetSettings(PCGSettings)
```

Loader/Executor of PCG data assets

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGLoadAssetElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset`` (PCGDataAsset):  [Read-Write]
- ``asset_color`` (LinearColor):  [Read-Only] Cached from the data when loaded
- ``asset_description`` (Text):  [Read-Only] Cached from the data when loaded
- ``asset_name`` (str):  [Read-Only] Cached from the data when loaded
- ``asset_reference_selector`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``data_index_tag`` (Name):  [Read-Write]
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
- ``input_index_tag`` (Name):  [Read-Write]
- ``load_from_input`` (bool):  [Read-Write]
- ``pins`` (Array[PCGPinProperties]):  [Read-Only]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write] By default, data table loading is asynchronous, can force it synchronous if needed.
- ``tag_outputs_based_on_output_pins`` (bool):  [Read-Only] Controls whether the data output from the loaded asset will be passed to the default pin with tags or on the proper pins.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``warn_if_no_asset`` (bool):  [Read-Write] Warns if asset is null or couldn't be loaded

<a id="unreal.PCGLoadDataAssetSettings.asset"></a>

#### asset

```python
@property
def asset() -> PCGDataAsset
```

(PCGDataAsset):  [Read-Write]

<a id="unreal.PCGLoadDataAssetSettings.asset"></a>

#### asset

```python
@asset.setter
def asset(value: PCGDataAsset) -> None
```

<a id="unreal.PCGLoadDataAssetSettings.pins"></a>

#### pins

```python
@property
def pins() -> Array[PCGPinProperties]
```

(Array[PCGPinProperties]):  [Read-Only]

<a id="unreal.PCGLoadDataAssetSettings.asset_name"></a>

#### asset_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Only] Cached from the data when loaded

<a id="unreal.PCGLoadDataAssetSettings.asset_description"></a>

#### asset_description

```python
@property
def asset_description() -> Text
```

(Text):  [Read-Only] Cached from the data when loaded

<a id="unreal.PCGLoadDataAssetSettings.asset_color"></a>

#### asset_color

```python
@property
def asset_color() -> LinearColor
```

(LinearColor):  [Read-Only] Cached from the data when loaded

<a id="unreal.PCGLoadDataAssetSettings.load_from_input"></a>

#### load_from_input

```python
@property
def load_from_input() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGLoadDataAssetSettings.load_from_input"></a>

#### load_from_input

```python
@load_from_input.setter
def load_from_input(value: bool) -> None
```

<a id="unreal.PCGLoadDataAssetSettings.asset_reference_selector"></a>

#### asset_reference_selector

```python
@property
def asset_reference_selector() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGLoadDataAssetSettings.asset_reference_selector"></a>

#### asset_reference_selector

```python
@asset_reference_selector.setter
def asset_reference_selector(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGLoadDataAssetSettings.input_index_tag"></a>

#### input_index_tag

```python
@property
def input_index_tag() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGLoadDataAssetSettings.input_index_tag"></a>

#### input_index_tag

```python
@input_index_tag.setter
def input_index_tag(value: Name) -> None
```

<a id="unreal.PCGLoadDataAssetSettings.data_index_tag"></a>

#### data_index_tag

```python
@property
def data_index_tag() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGLoadDataAssetSettings.data_index_tag"></a>

#### data_index_tag

```python
@data_index_tag.setter
def data_index_tag(value: Name) -> None
```

<a id="unreal.PCGLoadDataAssetSettings.warn_if_no_asset"></a>

#### warn_if_no_asset

```python
@property
def warn_if_no_asset() -> bool
```

(bool):  [Read-Write] Warns if asset is null or couldn't be loaded

<a id="unreal.PCGLoadDataAssetSettings.warn_if_no_asset"></a>

#### warn_if_no_asset

```python
@warn_if_no_asset.setter
def warn_if_no_asset(value: bool) -> None
```

<a id="unreal.PCGLoadDataAssetSettings.tag_outputs_based_on_output_pins"></a>

#### tag_outputs_based_on_output_pins

```python
@property
def tag_outputs_based_on_output_pins() -> bool
```

(bool):  [Read-Only] Controls whether the data output from the loaded asset will be passed to the default pin with tags or on the proper pins.

<a id="unreal.PCGLoadDataAssetSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, data table loading is asynchronous, can force it synchronous if needed.

<a id="unreal.PCGLoadDataAssetSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGMakeConcreteSettings"></a>