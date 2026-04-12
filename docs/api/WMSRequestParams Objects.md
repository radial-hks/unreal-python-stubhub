## WMSRequestParams Objects

```python
class WMSRequestParams(StructBase)
```

WMSRequest Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISLayer
- **File**: MagicGISDynamicLayerDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``request_map_height`` (str):  [Read-Write]
- ``request_map_width`` (str):  [Read-Write]
- ``request_version`` (str):  [Read-Write]
- ``service_layer_identifier`` (str):  [Read-Write]

<a id="unreal.WMSRequestParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(service_layer_identifier: str = "",
             request_map_width: str = "",
             request_map_height: str = "",
             request_version: str = "") -> None
```

<a id="unreal.WMSRequestParams.service_layer_identifier"></a>

#### service\_layer\_identifier

```python
@property
def service_layer_identifier() -> str
```

(str):  [Read-Write]

<a id="unreal.WMSRequestParams.service_layer_identifier"></a>

#### service\_layer\_identifier

```python
@service_layer_identifier.setter
def service_layer_identifier(value: str) -> None
```

<a id="unreal.WMSRequestParams.request_map_width"></a>

#### request\_map\_width

```python
@property
def request_map_width() -> str
```

(str):  [Read-Write]

<a id="unreal.WMSRequestParams.request_map_width"></a>

#### request\_map\_width

```python
@request_map_width.setter
def request_map_width(value: str) -> None
```

<a id="unreal.WMSRequestParams.request_map_height"></a>

#### request\_map\_height

```python
@property
def request_map_height() -> str
```

(str):  [Read-Write]

<a id="unreal.WMSRequestParams.request_map_height"></a>

#### request\_map\_height

```python
@request_map_height.setter
def request_map_height(value: str) -> None
```

<a id="unreal.WMSRequestParams.request_version"></a>

#### request\_version

```python
@property
def request_version() -> str
```

(str):  [Read-Write]

<a id="unreal.WMSRequestParams.request_version"></a>

#### request\_version

```python
@request_version.setter
def request_version(value: str) -> None
```

<a id="unreal.WMTSRequestParams"></a>