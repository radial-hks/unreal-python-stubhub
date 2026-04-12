## CameraStepZoomParams Objects

```python
class CameraStepZoomParams(ParamsBase)
```

Camera Step Zoom Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``continuous`` (bool):  [Read-Only]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``step`` (float):  [Read-Only]

<a id="unreal.CameraStepZoomParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(step: float = 0.000000, continuous: bool = False) -> None
```

<a id="unreal.CameraStepZoomParams.step"></a>

#### step

```python
@property
def step() -> float
```

(float):  [Read-Only]

<a id="unreal.CameraStepZoomParams.continuous"></a>

#### continuous

```python
@property
def continuous() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DisplayCoordinateParams"></a>