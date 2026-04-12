## GeoLayerActionParams Objects

```python
class GeoLayerActionParams(EidParams)
```

Geo Layer Action Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_name`` (str):  [Read-Write]
- ``eid`` (Eid):  [Read-Write]
- ``feature_id`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GeoLayerActionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(action_name: str = "", feature_id: str = "") -> None
```

<a id="unreal.GeoLayerActionParams.action_name"></a>

#### action\_name

```python
@property
def action_name() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerActionParams.action_name"></a>

#### action\_name

```python
@action_name.setter
def action_name(value: str) -> None
```

<a id="unreal.GeoLayerActionParams.feature_id"></a>

#### feature\_id

```python
@property
def feature_id() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerActionParams.feature_id"></a>

#### feature\_id

```python
@feature_id.setter
def feature_id(value: str) -> None
```

<a id="unreal.GeoLayerFeatureClickedEventArgs"></a>