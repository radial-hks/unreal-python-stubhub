## GeoLayerCreateParams Objects

```python
class GeoLayerCreateParams(ParamsBase)
```

Geo Layer Create Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_feature_style`` (GeoFeatureStyle):  [Read-Write]
- ``geo_layer_operation`` (GeoLayerOperation):  [Read-Write]
- ``geo_layer_params`` (GeoLayerParams):  [Read-Write]
- ``geo_layer_symbol`` (GeoLayerSymbol):  [Read-Write]
- ``geo_layer_type`` (str):  [Read-Write]
- ``geo_layer_url`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(geo_layer_url: str = "",
             geo_layer_type: str = "",
             geo_layer_params: GeoLayerParams = [
                 "", "Polygon", False, 4000, 0.000000
             ],
             geo_feature_style: GeoFeatureStyle = [
                 "", False,
                 [
                     "#FFFFFFFF", False, "#FFFFFFFF", 1.000000, False,
                     100.000000, "Elevation"
                 ], ["#FFFFFFFF", 1.000000, "Plane"],
                 ["#FFFFFFFF", 5.000000, "Circle"], ""
             ],
             geo_layer_symbol: GeoLayerSymbol = ["", "", []],
             geo_layer_operation: GeoLayerOperation = [8.000000]) -> None
```

<a id="unreal.GeoLayerCreateParams.geo_layer_url"></a>

#### geo\_layer\_url

```python
@property
def geo_layer_url() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.geo_layer_url"></a>

#### geo\_layer\_url

```python
@geo_layer_url.setter
def geo_layer_url(value: str) -> None
```

<a id="unreal.GeoLayerCreateParams.geo_layer_type"></a>

#### geo\_layer\_type

```python
@property
def geo_layer_type() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.geo_layer_type"></a>

#### geo\_layer\_type

```python
@geo_layer_type.setter
def geo_layer_type(value: str) -> None
```

<a id="unreal.GeoLayerCreateParams.geo_layer_params"></a>

#### geo\_layer\_params

```python
@property
def geo_layer_params() -> GeoLayerParams
```

(GeoLayerParams):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.geo_layer_params"></a>

#### geo\_layer\_params

```python
@geo_layer_params.setter
def geo_layer_params(value: GeoLayerParams) -> None
```

<a id="unreal.GeoLayerCreateParams.geo_feature_style"></a>

#### geo\_feature\_style

```python
@property
def geo_feature_style() -> GeoFeatureStyle
```

(GeoFeatureStyle):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.geo_feature_style"></a>

#### geo\_feature\_style

```python
@geo_feature_style.setter
def geo_feature_style(value: GeoFeatureStyle) -> None
```

<a id="unreal.GeoLayerCreateParams.geo_layer_symbol"></a>

#### geo\_layer\_symbol

```python
@property
def geo_layer_symbol() -> GeoLayerSymbol
```

(GeoLayerSymbol):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.geo_layer_symbol"></a>

#### geo\_layer\_symbol

```python
@geo_layer_symbol.setter
def geo_layer_symbol(value: GeoLayerSymbol) -> None
```

<a id="unreal.GeoLayerCreateParams.geo_layer_operation"></a>

#### geo\_layer\_operation

```python
@property
def geo_layer_operation() -> GeoLayerOperation
```

(GeoLayerOperation):  [Read-Write]

<a id="unreal.GeoLayerCreateParams.geo_layer_operation"></a>

#### geo\_layer\_operation

```python
@geo_layer_operation.setter
def geo_layer_operation(value: GeoLayerOperation) -> None
```

<a id="unreal.GeoLayerUpdateParams"></a>