## DataLayerCreationParameters Objects

```python
class DataLayerCreationParameters(StructBase)
```

Data Layer Creation Parameters

**C++ Source:**

- **Module**: DataLayerEditor
- **File**: DataLayerEditorSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_layer_asset`` (DataLayerAsset):  [Read-Write] Required. Will assign the asset to the created instance.
- ``is_private`` (bool):  [Read-Write]
- ``world_data_layers`` (WorldDataLayers):  [Read-Write] Optional. Will default at the level WorldDataLayers if unset.

<a id="unreal.DataLayerCreationParameters.__init__"></a>

#### __init__

```python
def __init__(data_layer_asset: DataLayerAsset = None,
             world_data_layers: WorldDataLayers = None,
             is_private: bool = False) -> None
```

<a id="unreal.DataLayerCreationParameters.data_layer_asset"></a>

#### data_layer_asset

```python
@property
def data_layer_asset() -> DataLayerAsset
```

(DataLayerAsset):  [Read-Write] Required. Will assign the asset to the created instance.

<a id="unreal.DataLayerCreationParameters.data_layer_asset"></a>

#### data_layer_asset

```python
@data_layer_asset.setter
def data_layer_asset(value: DataLayerAsset) -> None
```

<a id="unreal.DataLayerCreationParameters.world_data_layers"></a>

#### world_data_layers

```python
@property
def world_data_layers() -> WorldDataLayers
```

(WorldDataLayers):  [Read-Write] Optional. Will default at the level WorldDataLayers if unset.

<a id="unreal.DataLayerCreationParameters.world_data_layers"></a>

#### world_data_layers

```python
@world_data_layers.setter
def world_data_layers(value: WorldDataLayers) -> None
```

<a id="unreal.DataLayerCreationParameters.is_private"></a>

#### is_private

```python
@property
def is_private() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DataLayerCreationParameters.is_private"></a>

#### is_private

```python
@is_private.setter
def is_private(value: bool) -> None
```

<a id="unreal.CameraLookatTrackingSettings"></a>