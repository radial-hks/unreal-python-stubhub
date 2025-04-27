## NNEDenoiserTemporalAsset Objects

```python
class NNEDenoiserTemporalAsset(DataAsset)
```

Denoiser model data asset

**C++ Source:**

- **Plugin**: NNEDenoiser
- **Module**: NNEDenoiser
- **File**: NNEDenoiserTemporalAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input_mapping`` (DataTable):  [Read-Write] Input mapping table
- ``model_data`` (NNEModelData):  [Read-Write] NNE model data
- ``output_mapping`` (DataTable):  [Read-Write] Output mapping table
- ``tiling_config`` (TilingConfig):  [Read-Write] Tiling configuration

<a id="unreal.NNEDenoiserTemporalAsset.model_data"></a>

#### model_data

```python
@property
def model_data() -> NNEModelData
```

(NNEModelData):  [Read-Write] NNE model data

<a id="unreal.NNEDenoiserTemporalAsset.model_data"></a>

#### model_data

```python
@model_data.setter
def model_data(value: NNEModelData) -> None
```

<a id="unreal.NNEDenoiserTemporalAsset.input_mapping"></a>

#### input_mapping

```python
@property
def input_mapping() -> DataTable
```

(DataTable):  [Read-Write] Input mapping table

<a id="unreal.NNEDenoiserTemporalAsset.input_mapping"></a>

#### input_mapping

```python
@input_mapping.setter
def input_mapping(value: DataTable) -> None
```

<a id="unreal.NNEDenoiserTemporalAsset.output_mapping"></a>

#### output_mapping

```python
@property
def output_mapping() -> DataTable
```

(DataTable):  [Read-Write] Output mapping table

<a id="unreal.NNEDenoiserTemporalAsset.output_mapping"></a>

#### output_mapping

```python
@output_mapping.setter
def output_mapping(value: DataTable) -> None
```

<a id="unreal.NNEDenoiserTemporalAsset.tiling_config"></a>

#### tiling_config

```python
@property
def tiling_config() -> TilingConfig
```

(TilingConfig):  [Read-Write] Tiling configuration

<a id="unreal.NNEDenoiserTemporalAsset.tiling_config"></a>

#### tiling_config

```python
@tiling_config.setter
def tiling_config(value: TilingConfig) -> None
```

<a id="unreal.AbcAssetImportData"></a>