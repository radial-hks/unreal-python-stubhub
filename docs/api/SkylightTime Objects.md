## SkylightTime Objects

```python
class SkylightTime(ParamsBase)
```

Skylight Time

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpEnvironmentAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration_seconds`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``realtime`` (bool):  [Read-Write]
- ``skylight_time`` (str):  [Read-Write]

<a id="unreal.SkylightTime.__init__"></a>

#### \_\_init\_\_

```python
def __init__(skylight_time: str = "",
             duration_seconds: float = 0.000000,
             realtime: bool = False) -> None
```

<a id="unreal.SkylightTime.skylight_time"></a>

#### skylight\_time

```python
@property
def skylight_time() -> str
```

(str):  [Read-Write]

<a id="unreal.SkylightTime.skylight_time"></a>

#### skylight\_time

```python
@skylight_time.setter
def skylight_time(value: str) -> None
```

<a id="unreal.SkylightTime.duration_seconds"></a>

#### duration\_seconds

```python
@property
def duration_seconds() -> float
```

(float):  [Read-Write]

<a id="unreal.SkylightTime.duration_seconds"></a>

#### duration\_seconds

```python
@duration_seconds.setter
def duration_seconds(value: float) -> None
```

<a id="unreal.SkylightTime.realtime"></a>

#### realtime

```python
@property
def realtime() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkylightTime.realtime"></a>

#### realtime

```python
@realtime.setter
def realtime(value: bool) -> None
```

<a id="unreal.SkylightTimeResult"></a>