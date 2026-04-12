## WDPFocusPositionParams Objects

```python
class WDPFocusPositionParams(ParamsBase)
```

WDPFocus Position Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance`` (float):  [Read-Write] 单位: m
- ``fly_time`` (float):  [Read-Write] 单位: 秒
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]
- ``target_position`` (Vector):  [Read-Write]

<a id="unreal.WDPFocusPositionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(target_position: Vector = [0.000000, 0.000000, 0.000000],
             rotation: CameraPresetRotator = [0.000000, 0.000000],
             distance: float = 0.000000,
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPFocusPositionParams.target_position"></a>

#### target\_position

```python
@property
def target_position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPFocusPositionParams.target_position"></a>

#### target\_position

```python
@target_position.setter
def target_position(value: Vector) -> None
```

<a id="unreal.WDPFocusPositionParams.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPFocusPositionParams.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPFocusPositionParams.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write] 单位: m

<a id="unreal.WDPFocusPositionParams.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.WDPFocusPositionParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write] 单位: 秒

<a id="unreal.WDPFocusPositionParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPFocusEntitiesParams"></a>