## WDPFocusEntitiesParams Objects

```python
class WDPFocusEntitiesParams(EidArrayParams)
```

WDPFocus Entities Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance_factor`` (float):  [Read-Write] 倍率
- ``eids`` (Array[Eid]):  [Read-Write]
- ``fly_time`` (float):  [Read-Write] 单位: 秒
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPFocusEntitiesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rotation: CameraPresetRotator = [0.000000, 0.000000],
             distance_factor: float = 0.000000,
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPFocusEntitiesParams.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPFocusEntitiesParams.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPFocusEntitiesParams.distance_factor"></a>

#### distance\_factor

```python
@property
def distance_factor() -> float
```

(float):  [Read-Write] 倍率

<a id="unreal.WDPFocusEntitiesParams.distance_factor"></a>

#### distance\_factor

```python
@distance_factor.setter
def distance_factor(value: float) -> None
```

<a id="unreal.WDPFocusEntitiesParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write] 单位: 秒

<a id="unreal.WDPFocusEntitiesParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPFocusBoxParams"></a>