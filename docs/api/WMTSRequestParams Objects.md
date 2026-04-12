## WMTSRequestParams Objects

```python
class WMTSRequestParams(StructBase)
```

WMTSRequest Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISLayer
- **File**: MagicGISDynamicLayerDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``service_layer_identifier`` (str):  [Read-Write]
- ``service_matrix_set_identifier`` (str):  [Read-Write]

<a id="unreal.WMTSRequestParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(service_layer_identifier: str = "",
             service_matrix_set_identifier: str = "") -> None
```

<a id="unreal.WMTSRequestParams.service_layer_identifier"></a>

#### service\_layer\_identifier

```python
@property
def service_layer_identifier() -> str
```

(str):  [Read-Write]

<a id="unreal.WMTSRequestParams.service_layer_identifier"></a>

#### service\_layer\_identifier

```python
@service_layer_identifier.setter
def service_layer_identifier(value: str) -> None
```

<a id="unreal.WMTSRequestParams.service_matrix_set_identifier"></a>

#### service\_matrix\_set\_identifier

```python
@property
def service_matrix_set_identifier() -> str
```

(str):  [Read-Write]

<a id="unreal.WMTSRequestParams.service_matrix_set_identifier"></a>

#### service\_matrix\_set\_identifier

```python
@service_matrix_set_identifier.setter
def service_matrix_set_identifier(value: str) -> None
```

<a id="unreal.HttpESRIFeatureServiceLayerDefine"></a>