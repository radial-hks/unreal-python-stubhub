## WDPFollowEntityParams Objects

```python
class WDPFollowEntityParams(EidParams)
```

WDPFollow Entity Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distance`` (float):  [Read-Write] 单位: m
- ``eid`` (Eid):  [Read-Write]
- ``follow_rotation`` (CameraPresetRotator):  [Read-Write]
- ``fps`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``use_relative_rotation`` (bool):  [Read-Write]

<a id="unreal.WDPFollowEntityParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(follow_rotation: CameraPresetRotator = [0.000000, 0.000000],
             use_relative_rotation: bool = False,
             distance: float = 0.000000,
             fps: bool = False) -> None
```

<a id="unreal.WDPFollowEntityParams.follow_rotation"></a>

#### follow\_rotation

```python
@property
def follow_rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Write]

<a id="unreal.WDPFollowEntityParams.follow_rotation"></a>

#### follow\_rotation

```python
@follow_rotation.setter
def follow_rotation(value: CameraPresetRotator) -> None
```

<a id="unreal.WDPFollowEntityParams.use_relative_rotation"></a>

#### use\_relative\_rotation

```python
@property
def use_relative_rotation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPFollowEntityParams.use_relative_rotation"></a>

#### use\_relative\_rotation

```python
@use_relative_rotation.setter
def use_relative_rotation(value: bool) -> None
```

<a id="unreal.WDPFollowEntityParams.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write] 单位: m

<a id="unreal.WDPFollowEntityParams.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.WDPFollowEntityParams.fps"></a>

#### fps

```python
@property
def fps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WDPFollowEntityParams.fps"></a>

#### fps

```python
@fps.setter
def fps(value: bool) -> None
```

<a id="unreal.WDPCameraRoamParams"></a>