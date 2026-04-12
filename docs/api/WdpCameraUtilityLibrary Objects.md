## WdpCameraUtilityLibrary Objects

```python
class WdpCameraUtilityLibrary(BlueprintFunctionLibrary)
```

Wdp Camera Utility Library

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpCameraUtilityLibrary.h

<a id="unreal.WdpCameraUtilityLibrary.sort_vectors_by_distance"></a>

#### sort\_vectors\_by\_distance

```python
@classmethod
def sort_vectors_by_distance(cls, relative_to: Vector,
                             array: Array[Vector]) -> Array[Vector]
```

X.sort_vectors_by_distance(relative_to, array) -> Array[Vector]
将Vector按照距离排序

Args:
    relative_to (Vector): 
    array (Array[Vector]): 

Returns:
    Array[Vector]: 

    return_value (Array[Vector]):

<a id="unreal.WdpCameraUtilityLibrary.sort_actors_by_location"></a>

#### sort\_actors\_by\_location

```python
@classmethod
def sort_actors_by_location(cls, relative_to: Vector,
                            array: Array[Actor]) -> Array[Actor]
```

X.sort_actors_by_location(relative_to, array) -> Array[Actor]
将Actor按目标点位置排序

Args:
    relative_to (Vector): 
    array (Array[Actor]): 

Returns:
    Array[Actor]: 

    return_value (Array[Actor]):

<a id="unreal.WdpCameraUtilityLibrary.sort_actors_by_distance2d"></a>

#### sort\_actors\_by\_distance2d

```python
@classmethod
def sort_actors_by_distance2d(cls, relative_to: Actor,
                              array: Array[Actor]) -> Array[Actor]
```

X.sort_actors_by_distance2d(relative_to, array) -> Array[Actor]
将Actor按XY距离排序

Args:
    relative_to (Actor): 
    array (Array[Actor]): 

Returns:
    Array[Actor]: 

    return_value (Array[Actor]):

<a id="unreal.WdpCameraUtilityLibrary.sort_actors_by_distance"></a>

#### sort\_actors\_by\_distance

```python
@classmethod
def sort_actors_by_distance(cls, relative_to: Actor,
                            array: Array[Actor]) -> Array[Actor]
```

X.sort_actors_by_distance(relative_to, array) -> Array[Actor]
将Actor按距离排序

Args:
    relative_to (Actor): 
    array (Array[Actor]): 

Returns:
    Array[Actor]: 

    return_value (Array[Actor]):

<a id="unreal.WdpCameraUtilityLibrary.hex_to_color"></a>

#### hex\_to\_color

```python
@classmethod
def hex_to_color(cls, hex: str) -> Color
```

X.hex_to_color(hex) -> Color
将Hex Code转换为颜色

Args:
    hex (str): 

Returns:
    Color:

<a id="unreal.WdpCameraUtilityLibrary.get_hit_result_at_screen_position"></a>

#### get\_hit\_result\_at\_screen\_position

```python
@classmethod
def get_hit_result_at_screen_position(
        cls, player_controller: PlayerController, screen_position: Vector2D,
        trace_channel: TraceTypeQuery,
        trace_complex: bool) -> Optional[HitResult]
```

X.get_hit_result_at_screen_position(player_controller, screen_position, trace_channel, trace_complex) -> HitResult or None
获取屏幕空间坐标的碰撞

Args:
    player_controller (PlayerController): 
    screen_position (Vector2D): 
    trace_channel (TraceTypeQuery): 
    trace_complex (bool): 

Returns:
    HitResult or None: 

    hit_result (HitResult):

<a id="unreal.WdpCameraUtilityLibrary.flush_inputs"></a>

#### flush\_inputs

```python
@classmethod
def flush_inputs(cls, player_controller: PlayerController) -> None
```

X.flush_inputs(player_controller) -> None
清空Coltroller的输入缓存

Args:
    player_controller (PlayerController):

<a id="unreal.WdpCameraUtilityLibrary.find_interp_value_from_float_key_map"></a>

#### find\_interp\_value\_from\_float\_key\_map

```python
@classmethod
def find_interp_value_from_float_key_map(
        cls, data: Map[float, float], input_time: float,
        interp_mode: RichCurveInterpMode) -> Optional[float]
```

X.find_interp_value_from_float_key_map(data, input_time, interp_mode) -> double or None
时间轴的Datetime KeyMap动画关键帧插值计算 使用float

Args:
    data (Map[double, double]): 
    input_time (double): 
    interp_mode (RichCurveInterpMode): 

Returns:
    double or None: 

    out_value (double):

<a id="unreal.WdpCameraUtilityLibrary.find_interp_value_from_date_time_key_map"></a>

#### find\_interp\_value\_from\_date\_time\_key\_map

```python
@classmethod
def find_interp_value_from_date_time_key_map(
        cls, data: Map[DateTime, float], input_time: DateTime,
        interp_mode: RichCurveInterpMode) -> Optional[float]
```

X.find_interp_value_from_date_time_key_map(data, input_time, interp_mode) -> double or None
时间轴的Datetime KeyMap动画关键帧插值计算 使用Datetime

Args:
    data (Map[DateTime, double]): 
    input_time (DateTime): 
    interp_mode (RichCurveInterpMode): 

Returns:
    double or None: 

    out_value (double):

<a id="unreal.WdpCameraUtilityLibrary.distance_sort_map"></a>

#### distance\_sort\_map

```python
@classmethod
def distance_sort_map(cls, map: Map[Vector, int],
                      origin: Vector) -> Array[int]
```

X.distance_sort_map(map, origin) -> Array[int32]
3DUI使用的距离排序Map Index

Args:
    map (Map[Vector, int32]): 
    origin (Vector): 

Returns:
    Array[int32]:

<a id="unreal.WdpCameraUtilityLibrary.date_time_to_string"></a>

#### date\_time\_to\_string

```python
@classmethod
def date_time_to_string(cls,
                        date_time: DateTime,
                        format: str = "%Y-%m-%d %H:%M:%S") -> str
```

X.date_time_to_string(date_time, format="%Y-%m-%d %H:%M:%S") -> str
DateTime转换为String
       * The format works as follows:
       * case TCHAR('a'): Result += IsMorning() ? TEXT("am") : TEXT("pm"); break;
       * case TCHAR('A'): Result += IsMorning() ? TEXT("AM") : TEXT("PM"); break;
       * case TCHAR('d'): Result += FString::Printf(TEXT("%02i"), GetDay()); break;
       * case TCHAR('D'): Result += FString::Printf(TEXT("%03i"), GetDayOfYear()); break;
       * case TCHAR('m'): Result += FString::Printf(TEXT("%02i"), GetMonth()); break;
       * case TCHAR('y'): Result += FString::Printf(TEXT("%02i"), GetYear() % 100); break;
       * case TCHAR('Y'): Result += FString::Printf(TEXT("%04i"), GetYear()); break;
       * case TCHAR('h'): Result += FString::Printf(TEXT("%02i"), GetHour12()); break;
       * case TCHAR('H'): Result += FString::Printf(TEXT("%02i"), GetHour()); break;
       * case TCHAR('M'): Result += FString::Printf(TEXT("%02i"), GetMinute()); break;
       * case TCHAR('S'): Result += FString::Printf(TEXT("%02i"), GetSecond()); break;
       * case TCHAR('s'): Result += FString::Printf(TEXT("%03i"), GetMillisecond()); break;

Args:
    date_time (DateTime): 
    format (str): 

Returns:
    str: 

    string (str):

<a id="unreal.WdpCameraUtilityLibrary.convert_vector_array_to_vector2d"></a>

#### convert\_vector\_array\_to\_vector2d

```python
@classmethod
def convert_vector_array_to_vector2d(cls,
                                     array: Array[Vector]) -> Array[Vector2D]
```

X.convert_vector_array_to_vector2d(array) -> Array[Vector2D]
将Vector数组转换成Vector2D数组

Args:
    array (Array[Vector]): 

Returns:
    Array[Vector2D]:

<a id="unreal.WdpCameraUtilityLibrary.color_to_hex"></a>

#### color\_to\_hex

```python
@classmethod
def color_to_hex(cls, color: Color) -> str
```

X.color_to_hex(color) -> str
将颜色转换为Hex Code

Args:
    color (Color): 

Returns:
    str:

<a id="unreal.WdpCameraUtilityLibrary.clear_on_screen_debug_messages"></a>

#### clear\_on\_screen\_debug\_messages

```python
@classmethod
def clear_on_screen_debug_messages(cls) -> None
```

X.clear_on_screen_debug_messages() -> None
清除屏幕上全部消息

<a id="unreal.WdpCommonInput"></a>