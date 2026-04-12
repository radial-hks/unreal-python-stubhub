## WDPCameraMoveTransformParams Objects

```python
class WDPCameraMoveTransformParams(WDPCameraBaseTransformParams)
```

WDPCamera Move Transform Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (str):  [Read-Write] 移动： forward/backward/left/right/up/down
  旋转： up/down/right/left
  Around: right/left/cw/clockwise/ccw/anticlockwise
- ``distance`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``velocity`` (float):  [Read-Write] 移动速度，m/s
  旋转速度/Around速度. degree/s

<a id="unreal.WDPCameraMoveTransformParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction: str = "",
             velocity: float = 0.000000,
             distance: float = 0.000000) -> None
```

<a id="unreal.WDPCameraMoveTransformParams.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPCameraMoveTransformParams.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.WDPCameraRotateTransformParams"></a>