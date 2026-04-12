## WeatherAirData Objects

```python
class WeatherAirData(StructBase)
```

Weather Air Data

**C++ Source:**

- **Plugin**: WdpEnvironment
- **Module**: WdpEnvironment
- **File**: WeatherServiceDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aqi`` (int32):  [Read-Write]
- ``co`` (float):  [Read-Write]
- ``no2`` (int32):  [Read-Write]
- ``o3`` (int32):  [Read-Write]
- ``pm10`` (int32):  [Read-Write]
- ``pm25`` (int32):  [Read-Write] PM2.5
- ``primary_pollutant`` (str):  [Read-Write]
- ``quality`` (str):  [Read-Write]
- ``so2`` (int32):  [Read-Write]

<a id="unreal.WeatherAirData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aqi: int = 0,
             pm25: int = 0,
             pm10: int = 0,
             so2: int = 0,
             no2: int = 0,
             co: float = 0.000000,
             o3: int = 0,
             primary_pollutant: str = "",
             quality: str = "") -> None
```

<a id="unreal.WeatherAirData.aqi"></a>

#### aqi

```python
@property
def aqi() -> int
```

(int32):  [Read-Write]

<a id="unreal.WeatherAirData.aqi"></a>

#### aqi

```python
@aqi.setter
def aqi(value: int) -> None
```

<a id="unreal.WeatherAirData.pm25"></a>

#### pm25

```python
@property
def pm25() -> int
```

(int32):  [Read-Write] PM2.5

<a id="unreal.WeatherAirData.pm25"></a>

#### pm25

```python
@pm25.setter
def pm25(value: int) -> None
```

<a id="unreal.WeatherAirData.pm10"></a>

#### pm10

```python
@property
def pm10() -> int
```

(int32):  [Read-Write]

<a id="unreal.WeatherAirData.pm10"></a>

#### pm10

```python
@pm10.setter
def pm10(value: int) -> None
```

<a id="unreal.WeatherAirData.so2"></a>

#### so2

```python
@property
def so2() -> int
```

(int32):  [Read-Write]

<a id="unreal.WeatherAirData.so2"></a>

#### so2

```python
@so2.setter
def so2(value: int) -> None
```

<a id="unreal.WeatherAirData.no2"></a>

#### no2

```python
@property
def no2() -> int
```

(int32):  [Read-Write]

<a id="unreal.WeatherAirData.no2"></a>

#### no2

```python
@no2.setter
def no2(value: int) -> None
```

<a id="unreal.WeatherAirData.co"></a>

#### co

```python
@property
def co() -> float
```

(float):  [Read-Write]

<a id="unreal.WeatherAirData.co"></a>

#### co

```python
@co.setter
def co(value: float) -> None
```

<a id="unreal.WeatherAirData.o3"></a>

#### o3

```python
@property
def o3() -> int
```

(int32):  [Read-Write]

<a id="unreal.WeatherAirData.o3"></a>

#### o3

```python
@o3.setter
def o3(value: int) -> None
```

<a id="unreal.WeatherAirData.primary_pollutant"></a>

#### primary\_pollutant

```python
@property
def primary_pollutant() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherAirData.primary_pollutant"></a>

#### primary\_pollutant

```python
@primary_pollutant.setter
def primary_pollutant(value: str) -> None
```

<a id="unreal.WeatherAirData.quality"></a>

#### quality

```python
@property
def quality() -> str
```

(str):  [Read-Write]

<a id="unreal.WeatherAirData.quality"></a>

#### quality

```python
@quality.setter
def quality(value: str) -> None
```

<a id="unreal.WeatherCurrentData"></a>