## WeatherCurrentData Objects

```python
class WeatherCurrentData(StructBase)
```

Weather Current Data

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherServiceDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``code`` (int32):  [Read-Write] Weather index, 0-38
- ``feels_like`` (int32):  [Read-Write] Tempture, unit: ℃
- ``humidity`` (int32):  [Read-Write] Humidity, unit: %
- ``pressure`` (float):  [Read-Write] Pressure, unit: hPa
- ``temperature`` (int32):  [Read-Write] Tempture, unit: ℃
- ``visibility`` (float):  [Read-Write] Visibility, unit: m
- ``weather_description`` (str):  [Read-Write]
- ``wind_direction`` (str):  [Read-Write]
- ``wind_direction_degree`` (int32):  [Read-Write]
- ``wind_scale`` (float):  [Read-Write]
- ``wind_speed`` (float):  [Read-Write] Wind Speed, unit: m/s

<a id="unreal.WeatherCurrentData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(weather_description: str = "",
             code: int = 0,
             temperature: int = 0,
             feels_like: int = 0,
             pressure: float = 0.000000,
             humidity: int = 0,
             visibility: float = 0.000000,
             wind_direction: str = "",
             wind_direction_degree: int = 0,
             wind_speed: float = 0.000000,
             wind_scale: float = 0.000000) -> None
```

<a id="unreal.WeatherCurrentData.weather_description"></a>

#### weather\_description

```python
@property
def weather_description() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherCurrentData.weather_description"></a>

#### weather\_description

```python
@weather_description.setter
def weather_description(value: str) -> None
```

<a id="unreal.WeatherCurrentData.code"></a>

#### code

```python
@property
def code() -> int
```

(int32):  [Read-Write] Weather index, 0-38

<a id="unreal.WeatherCurrentData.code"></a>

#### code

```python
@code.setter
def code(value: int) -> None
```

<a id="unreal.WeatherCurrentData.temperature"></a>

#### temperature

```python
@property
def temperature() -> int
```

(int32):  [Read-Write] Tempture, unit: ℃

<a id="unreal.WeatherCurrentData.temperature"></a>

#### temperature

```python
@temperature.setter
def temperature(value: int) -> None
```

<a id="unreal.WeatherCurrentData.feels_like"></a>

#### feels\_like

```python
@property
def feels_like() -> int
```

(int32):  [Read-Write] Tempture, unit: ℃

<a id="unreal.WeatherCurrentData.feels_like"></a>

#### feels\_like

```python
@feels_like.setter
def feels_like(value: int) -> None
```

<a id="unreal.WeatherCurrentData.pressure"></a>

#### pressure

```python
@property
def pressure() -> float
```

(float):  [Read-Write] Pressure, unit: hPa

<a id="unreal.WeatherCurrentData.pressure"></a>

#### pressure

```python
@pressure.setter
def pressure(value: float) -> None
```

<a id="unreal.WeatherCurrentData.humidity"></a>

#### humidity

```python
@property
def humidity() -> int
```

(int32):  [Read-Write] Humidity, unit: %

<a id="unreal.WeatherCurrentData.humidity"></a>

#### humidity

```python
@humidity.setter
def humidity(value: int) -> None
```

<a id="unreal.WeatherCurrentData.visibility"></a>

#### visibility

```python
@property
def visibility() -> float
```

(float):  [Read-Write] Visibility, unit: m

<a id="unreal.WeatherCurrentData.visibility"></a>

#### visibility

```python
@visibility.setter
def visibility(value: float) -> None
```

<a id="unreal.WeatherCurrentData.wind_direction"></a>

#### wind\_direction

```python
@property
def wind_direction() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherCurrentData.wind_direction"></a>

#### wind\_direction

```python
@wind_direction.setter
def wind_direction(value: str) -> None
```

<a id="unreal.WeatherCurrentData.wind_direction_degree"></a>

#### wind\_direction\_degree

```python
@property
def wind_direction_degree() -> int
```

(int32):  [Read-Write]

<a id="unreal.WeatherCurrentData.wind_direction_degree"></a>

#### wind\_direction\_degree

```python
@wind_direction_degree.setter
def wind_direction_degree(value: int) -> None
```

<a id="unreal.WeatherCurrentData.wind_speed"></a>

#### wind\_speed

```python
@property
def wind_speed() -> float
```

(float):  [Read-Write] Wind Speed, unit: m/s

<a id="unreal.WeatherCurrentData.wind_speed"></a>

#### wind\_speed

```python
@wind_speed.setter
def wind_speed(value: float) -> None
```

<a id="unreal.WeatherCurrentData.wind_scale"></a>

#### wind\_scale

```python
@property
def wind_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.WeatherCurrentData.wind_scale"></a>

#### wind\_scale

```python
@wind_scale.setter
def wind_scale(value: float) -> None
```

<a id="unreal.WeatherLocationData"></a>