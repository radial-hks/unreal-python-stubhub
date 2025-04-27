## PCGDataAsset Objects

```python
class PCGDataAsset(Object)
```

Container for PCG data exported as standalone objects

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDataAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Text):  [Read-Write] Controls in what category the asset will appear in the palette & contextual menus.
- ``color`` (LinearColor):  [Read-Write] Custom node color to use for this specific asset
- ``data`` (PCGDataCollection):  [Read-Only] Contains direct data owned by this data asset
- ``description`` (Text):  [Read-Write] Additional description (tooltip) shown on the asset/loader node.
- ``exporter_class`` (Class):  [Read-Only] Custom exporter class that was used to create this PCG asset. Should derive from UPCGAssetExporter. Can be left empty.
- ``expose_to_library`` (bool):  [Read-Write] Controls whether the asset will be visible from the palette & contextual menus.
- ``name`` (str):  [Read-Write] Alternative name (instead of asset name), can be left empty
- ``object_path`` (SoftObjectPath):  [Read-Only] Reference to originating object (often will be a level)
- ``settings_class`` (type(Class)):  [Read-Only] Custom class to create settings/node in the graph when dragged in the editor. Can be left empty.

<a id="unreal.PCGDataAsset.data"></a>

#### data

```python
@property
def data() -> PCGDataCollection
```

(PCGDataCollection):  [Read-Only] Contains direct data owned by this data asset

<a id="unreal.PCGDataAsset.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] Alternative name (instead of asset name), can be left empty

<a id="unreal.PCGDataAsset.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.PCGDataAsset.exporter_class"></a>

#### exporter_class

```python
@property
def exporter_class() -> Class
```

(Class):  [Read-Only] Custom exporter class that was used to create this PCG asset. Should derive from UPCGAssetExporter. Can be left empty.

<a id="unreal.PCGDataAsset.settings_class"></a>

#### settings_class

```python
@property
def settings_class() -> Class
```

(type(Class)):  [Read-Only] Custom class to create settings/node in the graph when dragged in the editor. Can be left empty.

<a id="unreal.PCGDataAsset.object_path"></a>

#### object_path

```python
@property
def object_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only] Reference to originating object (often will be a level)

<a id="unreal.PCGDataAsset.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] Custom node color to use for this specific asset

<a id="unreal.PCGDataAsset.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.PCGDataAsset.expose_to_library"></a>

#### expose_to_library

```python
@property
def expose_to_library() -> bool
```

(bool):  [Read-Write] Controls whether the asset will be visible from the palette & contextual menus.

<a id="unreal.PCGDataAsset.expose_to_library"></a>

#### expose_to_library

```python
@expose_to_library.setter
def expose_to_library(value: bool) -> None
```

<a id="unreal.PCGDataAsset.category"></a>

#### category

```python
@property
def category() -> Text
```

(Text):  [Read-Write] Controls in what category the asset will appear in the palette & contextual menus.

<a id="unreal.PCGDataAsset.category"></a>

#### category

```python
@category.setter
def category(value: Text) -> None
```

<a id="unreal.PCGDataAsset.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Write] Additional description (tooltip) shown on the asset/loader node.

<a id="unreal.PCGDataAsset.description"></a>

#### description

```python
@description.setter
def description(value: Text) -> None
```

<a id="unreal.PCGExternalDataSettings"></a>