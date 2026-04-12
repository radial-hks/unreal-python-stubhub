## SetGeoLayerOutLineParams Objects

```python
class SetGeoLayerOutLineParams(ParamsBase)
```

Set Geo Layer Out Line Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[str]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``out_line`` (bool):  [Read-Write]
- ``style_name`` (str):  [Read-Write]

<a id="unreal.SetGeoLayerOutLineParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[str] = [],
             style_name: str = "",
             out_line: bool = False) -> None
```

<a id="unreal.SetGeoLayerOutLineParams.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.SetGeoLayerOutLineParams.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.SetGeoLayerOutLineParams.style_name"></a>

#### style\_name

```python
@property
def style_name() -> str
```

(str):  [Read-Write]

<a id="unreal.SetGeoLayerOutLineParams.style_name"></a>

#### style\_name

```python
@style_name.setter
def style_name(value: str) -> None
```

<a id="unreal.SetGeoLayerOutLineParams.out_line"></a>

#### out\_line

```python
@property
def out_line() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SetGeoLayerOutLineParams.out_line"></a>

#### out\_line

```python
@out_line.setter
def out_line(value: bool) -> None
```

<a id="unreal.SetGeoLayerHighlightParams"></a>