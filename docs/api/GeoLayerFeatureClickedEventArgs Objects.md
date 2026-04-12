## GeoLayerFeatureClickedEventArgs Objects

```python
class GeoLayerFeatureClickedEventArgs(EventArgsBase)
```

EventPara

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``basic_info`` (str):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``feature_id`` (str):  [Read-Write]

<a id="unreal.GeoLayerFeatureClickedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             feature_id: str = "",
             basic_info: str = "") -> None
```

<a id="unreal.GeoLayerFeatureClickedEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerFeatureClickedEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.GeoLayerFeatureClickedEventArgs.feature_id"></a>

#### feature\_id

```python
@property
def feature_id() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerFeatureClickedEventArgs.feature_id"></a>

#### feature\_id

```python
@feature_id.setter
def feature_id(value: str) -> None
```

<a id="unreal.GeoLayerFeatureClickedEventArgs.basic_info"></a>

#### basic\_info

```python
@property
def basic_info() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerFeatureClickedEventArgs.basic_info"></a>

#### basic\_info

```python
@basic_info.setter
def basic_info(value: str) -> None
```

<a id="unreal.LocalGeoReferenceParams"></a>