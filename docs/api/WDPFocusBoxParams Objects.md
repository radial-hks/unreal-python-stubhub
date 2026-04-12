## WDPFocusBoxParams Objects

```python
class WDPFocusBoxParams(ParamsBase)
```

WDPFocus Box Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``distance_factor`` (float):  [Read-Write] 倍率
- ``fly_time`` (float):  [Read-Write] 单位: 秒
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.WDPFocusBoxParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             distance_factor: float = 0.000000,
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPFocusBoxParams.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.WDPFocusBoxParams.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.WDPFocusBoxParams.distance_factor"></a>

#### distance\_factor

```python
@property
def distance_factor() -> float
```

(float):  [Read-Write] 倍率

<a id="unreal.WDPFocusBoxParams.distance_factor"></a>

#### distance\_factor

```python
@distance_factor.setter
def distance_factor(value: float) -> None
```

<a id="unreal.WDPFocusBoxParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write] 单位: 秒

<a id="unreal.WDPFocusBoxParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPFocusNodesParams"></a>