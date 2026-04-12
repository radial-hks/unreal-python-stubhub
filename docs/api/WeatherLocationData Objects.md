## WeatherLocationData Objects

```python
class WeatherLocationData(StructBase)
```

Weather Location Data

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherServiceDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``city_country`` (str):  [Read-Write]
- ``city_id`` (str):  [Read-Write]
- ``city_name`` (str):  [Read-Write]
- ``city_path`` (str):  [Read-Write]
- ``city_timezone`` (str):  [Read-Write]
- ``city_timezone_offset`` (str):  [Read-Write]

<a id="unreal.WeatherLocationData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(city_id: str = "",
             city_name: str = "",
             city_country: str = "",
             city_path: str = "",
             city_timezone: str = "",
             city_timezone_offset: str = "") -> None
```

<a id="unreal.WeatherLocationData.city_id"></a>

#### city\_id

```python
@property
def city_id() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherLocationData.city_id"></a>

#### city\_id

```python
@city_id.setter
def city_id(value: str) -> None
```

<a id="unreal.WeatherLocationData.city_name"></a>

#### city\_name

```python
@property
def city_name() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherLocationData.city_name"></a>

#### city\_name

```python
@city_name.setter
def city_name(value: str) -> None
```

<a id="unreal.WeatherLocationData.city_country"></a>

#### city\_country

```python
@property
def city_country() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherLocationData.city_country"></a>

#### city\_country

```python
@city_country.setter
def city_country(value: str) -> None
```

<a id="unreal.WeatherLocationData.city_path"></a>

#### city\_path

```python
@property
def city_path() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherLocationData.city_path"></a>

#### city\_path

```python
@city_path.setter
def city_path(value: str) -> None
```

<a id="unreal.WeatherLocationData.city_timezone"></a>

#### city\_timezone

```python
@property
def city_timezone() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherLocationData.city_timezone"></a>

#### city\_timezone

```python
@city_timezone.setter
def city_timezone(value: str) -> None
```

<a id="unreal.WeatherLocationData.city_timezone_offset"></a>

#### city\_timezone\_offset

```python
@property
def city_timezone_offset() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherLocationData.city_timezone_offset"></a>

#### city\_timezone\_offset

```python
@city_timezone_offset.setter
def city_timezone_offset(value: str) -> None
```

<a id="unreal.TimeSectionDefine"></a>