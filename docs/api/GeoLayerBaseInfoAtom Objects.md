## GeoLayerBaseInfoAtom Objects

```python
class GeoLayerBaseInfoAtom(EntityAtomBase)
```

Geo Layer Base Info Atom

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerBaseInfoAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_feature_style`` (GeoFeatureStyle):  [Read-Write]
- ``geo_layer_operation`` (GeoLayerOperation):  [Read-Write]
- ``geo_layer_params`` (GeoLayerParams):  [Read-Write]
- ``geo_layer_symbol`` (GeoLayerSymbol):  [Read-Write]
- ``geo_layer_type`` (str):  [Read-Write]
- ``geo_layer_url`` (str):  [Read-Write]

<a id="unreal.GeoLayerBaseInfoAtom.geo_layer_url"></a>

#### geo\_layer\_url

```python
@property
def geo_layer_url() -> str
```

(str):  [Read-Only]

<a id="unreal.GeoLayerBaseInfoAtom.geo_layer_type"></a>

#### geo\_layer\_type

```python
@property
def geo_layer_type() -> str
```

(str):  [Read-Only]

<a id="unreal.GeoLayerBaseInfoAtom.geo_layer_params"></a>

#### geo\_layer\_params

```python
@property
def geo_layer_params() -> GeoLayerParams
```

(GeoLayerParams):  [Read-Only]

<a id="unreal.GeoLayerBaseInfoAtom.geo_feature_style"></a>

#### geo\_feature\_style

```python
@property
def geo_feature_style() -> GeoFeatureStyle
```

(GeoFeatureStyle):  [Read-Only]

<a id="unreal.GeoLayerBaseInfoAtom.geo_layer_symbol"></a>

#### geo\_layer\_symbol

```python
@property
def geo_layer_symbol() -> GeoLayerSymbol
```

(GeoLayerSymbol):  [Read-Only]

<a id="unreal.GeoLayerBaseInfoAtom.geo_layer_operation"></a>

#### geo\_layer\_operation

```python
@property
def geo_layer_operation() -> GeoLayerOperation
```

(GeoLayerOperation):  [Read-Write]

<a id="unreal.GeoLayerBaseInfoAtom.geo_layer_operation"></a>

#### geo\_layer\_operation

```python
@geo_layer_operation.setter
def geo_layer_operation(value: GeoLayerOperation) -> None
```

<a id="unreal.GeoLayerVisibleAtom"></a>