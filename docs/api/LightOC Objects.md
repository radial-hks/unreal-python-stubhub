## LightOC Objects

```python
class LightOC(StructBase)
```

Light OC

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: TOD_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``close_light_interval`` (float):  [Read-Write] 根据日出时间提前（负值）或延后（正值）关灯，0代表日出就立刻关灯
- ``open_light_interval`` (float):  [Read-Write] 根据日落时间提前（负值）或延后（正值）开灯，0代表日落就立刻开灯
- ``tag`` (Name):  [Read-Write]

<a id="unreal.LightOC.__init__"></a>

#### \_\_init\_\_

```python
def __init__(tag: Name = "None",
             close_light_interval: float = 0.000000,
             open_light_interval: float = 0.000000) -> None
```

<a id="unreal.LightOC.tag"></a>

#### tag

```python
@property
def tag() -> Name
```

(Name):  [Read-Write]

<a id="unreal.LightOC.tag"></a>

#### tag

```python
@tag.setter
def tag(value: Name) -> None
```

<a id="unreal.LightOC.close_light_interval"></a>

#### close\_light\_interval

```python
@property
def close_light_interval() -> float
```

(float):  [Read-Write] 根据日出时间提前（负值）或延后（正值）关灯，0代表日出就立刻关灯

<a id="unreal.LightOC.close_light_interval"></a>

#### close\_light\_interval

```python
@close_light_interval.setter
def close_light_interval(value: float) -> None
```

<a id="unreal.LightOC.open_light_interval"></a>

#### open\_light\_interval

```python
@property
def open_light_interval() -> float
```

(float):  [Read-Write] 根据日落时间提前（负值）或延后（正值）开灯，0代表日落就立刻开灯

<a id="unreal.LightOC.open_light_interval"></a>

#### open\_light\_interval

```python
@open_light_interval.setter
def open_light_interval(value: float) -> None
```

<a id="unreal.LightArray"></a>