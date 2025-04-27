## PCGDataCollectionExporter Objects

```python
class PCGDataCollectionExporter(PCGAssetExporter)
```

Default exporter to save data collections, with no capacity for update.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSaveAssetElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_color`` (LinearColor):  [Read-Only]
- ``asset_description`` (str):  [Read-Only]
- ``data`` (PCGDataCollection):  [Read-Only]

<a id="unreal.PCGDataCollectionExporter.data"></a>

#### data

```python
@property
def data() -> PCGDataCollection
```

(PCGDataCollection):  [Read-Only]

<a id="unreal.PCGDataCollectionExporter.asset_description"></a>

#### asset_description

```python
@property
def asset_description() -> str
```

(str):  [Read-Only]

<a id="unreal.PCGDataCollectionExporter.asset_color"></a>

#### asset_color

```python
@property
def asset_color() -> LinearColor
```

(LinearColor):  [Read-Only]

<a id="unreal.PCGSaveDataAssetSettings"></a>