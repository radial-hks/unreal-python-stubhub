## SetGeoLayerHighlightParams Objects

```python
class SetGeoLayerHighlightParams(ParamsBase)
```

Set Geo Layer Highlight Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[str]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``highlight`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``style_name`` (str):  [Read-Write]

<a id="unreal.SetGeoLayerHighlightParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[str] = [],
             style_name: str = "",
             highlight: bool = False) -> None
```

<a id="unreal.SetGeoLayerHighlightParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.SetGeoLayerHighlightParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.SetGeoLayerHighlightParams.style_name"></a>

#### style\_name

```python
@property
def style_name() -> str
```

(str):  [Read-Write]

<a id="unreal.SetGeoLayerHighlightParams.style_name"></a>

#### style\_name

```python
@style_name.setter
def style_name(value: str) -> None
```

<a id="unreal.SetGeoLayerHighlightParams.highlight"></a>

#### highlight

```python
@property
def highlight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SetGeoLayerHighlightParams.highlight"></a>

#### highlight

```python
@highlight.setter
def highlight(value: bool) -> None
```

<a id="unreal.CameraPresetRotator"></a>