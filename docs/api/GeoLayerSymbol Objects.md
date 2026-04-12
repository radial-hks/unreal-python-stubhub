## GeoLayerSymbol Objects

```python
class GeoLayerSymbol(StructBase)
```

Geo Layer Symbol

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_feature_symbol_array`` (Array[GeoFeatureSymbol]):  [Read-Write]
- ``symbol_field`` (str):  [Read-Write]
- ``symbol_scheme`` (str):  [Read-Write]

<a id="unreal.GeoLayerSymbol.__init__"></a>

#### \_\_init\_\_

```python
def __init__(symbol_field: str = "",
             symbol_scheme: str = "",
             geo_feature_symbol_array: Array[GeoFeatureSymbol] = []) -> None
```

<a id="unreal.GeoLayerSymbol.symbol_field"></a>

#### symbol\_field

```python
@property
def symbol_field() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerSymbol.symbol_field"></a>

#### symbol\_field

```python
@symbol_field.setter
def symbol_field(value: str) -> None
```

<a id="unreal.GeoLayerSymbol.symbol_scheme"></a>

#### symbol\_scheme

```python
@property
def symbol_scheme() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerSymbol.symbol_scheme"></a>

#### symbol\_scheme

```python
@symbol_scheme.setter
def symbol_scheme(value: str) -> None
```

<a id="unreal.GeoLayerSymbol.geo_feature_symbol_array"></a>

#### geo\_feature\_symbol\_array

```python
@property
def geo_feature_symbol_array() -> Array[GeoFeatureSymbol]
```

(Array[GeoFeatureSymbol]):  [Read-Write]

<a id="unreal.GeoLayerSymbol.geo_feature_symbol_array"></a>

#### geo\_feature\_symbol\_array

```python
@geo_feature_symbol_array.setter
def geo_feature_symbol_array(value: Array[GeoFeatureSymbol]) -> None
```

<a id="unreal.GeoLayerOperation"></a>