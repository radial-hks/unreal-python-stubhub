## CameraStepRotateParams Objects

```python
class CameraStepRotateParams(ParamsBase)
```

Camera Step Rotate Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``continuous`` (bool):  [Read-Only]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``rotate_direction`` (WdpCameraRotateDir):  [Read-Only]
- ``step`` (float):  [Read-Only]

<a id="unreal.CameraStepRotateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rotate_direction: WdpCameraRotateDir = WdpCameraRotateDir.E_PITCH,
             step: float = 0.000000,
             continuous: bool = False) -> None
```

<a id="unreal.CameraStepRotateParams.rotate_direction"></a>

#### rotate\_direction

```python
@property
def rotate_direction() -> WdpCameraRotateDir
```

(WdpCameraRotateDir):  [Read-Only]

<a id="unreal.CameraStepRotateParams.step"></a>

#### step

```python
@property
def step() -> float
```

(float):  [Read-Only]

<a id="unreal.CameraStepRotateParams.continuous"></a>

#### continuous

```python
@property
def continuous() -> bool
```

(bool):  [Read-Only]

<a id="unreal.CameraStepZoomParams"></a>