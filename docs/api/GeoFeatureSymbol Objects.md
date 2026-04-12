## GeoFeatureSymbol Objects

```python
class GeoFeatureSymbol(StructBase)
```

Geo Feature Symbol

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_feature_style`` (GeoFeatureStyle):  [Read-Write]
- ``symbol_params`` (str):  [Read-Write]

<a id="unreal.GeoFeatureSymbol.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    symbol_params: str = "",
    geo_feature_style: GeoFeatureStyle = [
        "", False,
        [
            "#FFFFFFFF", False, "#FFFFFFFF", 1.000000, False, 100.000000,
            "Elevation"
        ], ["#FFFFFFFF", 1.000000, "Plane"], ["#FFFFFFFF", 5.000000, "Circle"],
        ""
    ]
) -> None
```

<a id="unreal.GeoFeatureSymbol.symbol_params"></a>

#### symbol\_params

```python
@property
def symbol_params() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoFeatureSymbol.symbol_params"></a>

#### symbol\_params

```python
@symbol_params.setter
def symbol_params(value: str) -> None
```

<a id="unreal.GeoFeatureSymbol.geo_feature_style"></a>

#### geo\_feature\_style

```python
@property
def geo_feature_style() -> GeoFeatureStyle
```

(GeoFeatureStyle):  [Read-Write]

<a id="unreal.GeoFeatureSymbol.geo_feature_style"></a>

#### geo\_feature\_style

```python
@geo_feature_style.setter
def geo_feature_style(value: GeoFeatureStyle) -> None
```

<a id="unreal.GeoLayerSymbol"></a>