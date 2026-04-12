## WDPCameraAroundParams Objects

```python
class WDPCameraAroundParams(ParamsBase)
```

WDPCamera Around Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (str):  [Read-Write] Around: right/left/cw/clockwise/ccw/anticlockwise
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``velocity`` (float):  [Read-Write] 移动速度，m/s
  旋转速度/Around速度. degree/s

<a id="unreal.WDPCameraAroundParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction: str = "", velocity: float = 0.000000) -> None
```

<a id="unreal.WDPCameraAroundParams.direction"></a>

#### direction

```python
@property
def direction() -> str
```

(str):  [Read-Write] Around: right/left/cw/clockwise/ccw/anticlockwise

<a id="unreal.WDPCameraAroundParams.direction"></a>

#### direction

```python
@direction.setter
def direction(value: str) -> None
```

<a id="unreal.WDPCameraAroundParams.velocity"></a>

#### velocity

```python
@property
def velocity() -> float
```

(float):  [Read-Write] 移动速度，m/s
旋转速度/Around速度. degree/s

<a id="unreal.WDPCameraAroundParams.velocity"></a>

#### velocity

```python
@velocity.setter
def velocity(value: float) -> None
```

<a id="unreal.WDPFocusPositionParams"></a>