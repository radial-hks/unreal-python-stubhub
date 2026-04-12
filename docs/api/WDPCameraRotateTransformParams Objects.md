## WDPCameraRotateTransformParams Objects

```python
class WDPCameraRotateTransformParams(WDPCameraBaseTransformParams)
```

WDPCamera Rotate Transform Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``direction`` (str):  [Read-Write] 移动： forward/backward/left/right/up/down
  旋转： up/down/right/left
  Around: right/left/cw/clockwise/ccw/anticlockwise
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``velocity`` (float):  [Read-Write] 移动速度，m/s
  旋转速度/Around速度. degree/s

<a id="unreal.WDPCameraRotateTransformParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction: str = "",
             velocity: float = 0.000000,
             angle: float = 0.000000) -> None
```

<a id="unreal.WDPCameraRotateTransformParams.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPCameraRotateTransformParams.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.WDPCameraAroundParams"></a>