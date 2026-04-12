## CityInfo Objects

```python
class CityInfo(StructBase)
```

City Info

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherServiceDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``city_id`` (str):  [Read-Write]
- ``city_path`` (str):  [Read-Write]

<a id="unreal.CityInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(city_id: str = "", city_path: str = "") -> None
```

<a id="unreal.CityInfo.city_id"></a>

#### city\_id

```python
@property
def city_id() -> str
```

(str):  [Read-Write]

<a id="unreal.CityInfo.city_id"></a>

#### city\_id

```python
@city_id.setter
def city_id(value: str) -> None
```

<a id="unreal.CityInfo.city_path"></a>

#### city\_path

```python
@property
def city_path() -> str
```

(str):  [Read-Write]

<a id="unreal.CityInfo.city_path"></a>

#### city\_path

```python
@city_path.setter
def city_path(value: str) -> None
```

<a id="unreal.RealtimeWeatherData"></a>