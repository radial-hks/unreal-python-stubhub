## WDPSetCameraPoseParams Objects

```python
class WDPSetCameraPoseParams(ParamsBase)
```

WDPSet Camera Pose Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fly_time`` (float):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``rotation`` (CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPSetCameraPoseParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: CameraPresetRotator = [0.000000, 0.000000],
             fly_time: float = 0.000000) -> None
```

<a id="unreal.WDPSetCameraPoseParams.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.WDPSetCameraPoseParams.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.WDPSetCameraPoseParams.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPSetCameraPoseParams.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPSetCameraPoseParams.fly_time"></a>

#### fly\_time

```python
@property
def fly_time() -> float
```

(float):  [Read-Write]

<a id="unreal.WDPSetCameraPoseParams.fly_time"></a>

#### fly\_time

```python
@fly_time.setter
def fly_time(value: float) -> None
```

<a id="unreal.WDPResetCameraPoseParams"></a>