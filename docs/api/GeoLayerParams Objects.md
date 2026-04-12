## GeoLayerParams Objects

```python
class GeoLayerParams(StructBase)
```

Geo Layer Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_feature_num`` (int32):  [Read-Write]
- ``feature_type`` (str):  [Read-Write] Polygon/Line/Point...
- ``layer_height_offset`` (float):  [Read-Write]
- ``need_gcj_offset`` (bool):  [Read-Write]
- ``service_layer_name`` (str):  [Read-Write]

<a id="unreal.GeoLayerParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(service_layer_name: str = "",
             feature_type: str = "",
             need_gcj_offset: bool = False,
             batch_feature_num: int = 0,
             layer_height_offset: float = 0.000000) -> None
```

<a id="unreal.GeoLayerParams.service_layer_name"></a>

#### service\_layer\_name

```python
@property
def service_layer_name() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerParams.service_layer_name"></a>

#### service\_layer\_name

```python
@service_layer_name.setter
def service_layer_name(value: str) -> None
```

<a id="unreal.GeoLayerParams.feature_type"></a>

#### feature\_type

```python
@property
def feature_type() -> str
```

(str):  [Read-Write] Polygon/Line/Point...

<a id="unreal.GeoLayerParams.feature_type"></a>

#### feature\_type

```python
@feature_type.setter
def feature_type(value: str) -> None
```

<a id="unreal.GeoLayerParams.need_gcj_offset"></a>

#### need\_gcj\_offset

```python
@property
def need_gcj_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeoLayerParams.need_gcj_offset"></a>

#### need\_gcj\_offset

```python
@need_gcj_offset.setter
def need_gcj_offset(value: bool) -> None
```

<a id="unreal.GeoLayerParams.batch_feature_num"></a>

#### batch\_feature\_num

```python
@property
def batch_feature_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeoLayerParams.batch_feature_num"></a>

#### batch\_feature\_num

```python
@batch_feature_num.setter
def batch_feature_num(value: int) -> None
```

<a id="unreal.GeoLayerParams.layer_height_offset"></a>

#### layer\_height\_offset

```python
@property
def layer_height_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.GeoLayerParams.layer_height_offset"></a>

#### layer\_height\_offset

```python
@layer_height_offset.setter
def layer_height_offset(value: float) -> None
```

<a id="unreal.GISLineDataForGenerator"></a>