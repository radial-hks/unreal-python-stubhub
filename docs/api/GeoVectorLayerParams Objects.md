## GeoVectorLayerParams Objects

```python
class GeoVectorLayerParams(StructBase)
```

Geo Vector Layer Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISLayer
- **File**: MagicGISVectorLayerDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_feature_num`` (int32):  [Read-Write]
- ``feature_type`` (str):  [Read-Write]
- ``need_gcj_offset`` (bool):  [Read-Write]
- ``service_layer_name`` (str):  [Read-Write]

<a id="unreal.GeoVectorLayerParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(service_layer_name: str = "",
             feature_type: str = "",
             need_gcj_offset: bool = False,
             batch_feature_num: int = 0) -> None
```

<a id="unreal.GeoVectorLayerParams.service_layer_name"></a>

#### service\_layer\_name

```python
@property
def service_layer_name() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoVectorLayerParams.service_layer_name"></a>

#### service\_layer\_name

```python
@service_layer_name.setter
def service_layer_name(value: str) -> None
```

<a id="unreal.GeoVectorLayerParams.feature_type"></a>

#### feature\_type

```python
@property
def feature_type() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoVectorLayerParams.feature_type"></a>

#### feature\_type

```python
@feature_type.setter
def feature_type(value: str) -> None
```

<a id="unreal.GeoVectorLayerParams.need_gcj_offset"></a>

#### need\_gcj\_offset

```python
@property
def need_gcj_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeoVectorLayerParams.need_gcj_offset"></a>

#### need\_gcj\_offset

```python
@need_gcj_offset.setter
def need_gcj_offset(value: bool) -> None
```

<a id="unreal.GeoVectorLayerParams.batch_feature_num"></a>

#### batch\_feature\_num

```python
@property
def batch_feature_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeoVectorLayerParams.batch_feature_num"></a>

#### batch\_feature\_num

```python
@batch_feature_num.setter
def batch_feature_num(value: int) -> None
```

<a id="unreal.GeoLayerCreateParams"></a>