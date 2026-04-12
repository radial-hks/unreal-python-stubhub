## CameraStepMoveParams Objects

```python
class CameraStepMoveParams(ParamsBase)
```

Camera Step Move Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``continuous`` (bool):  [Read-Only]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``move_direction`` (WDPDirection):  [Read-Only]
- ``step`` (float):  [Read-Only]

<a id="unreal.CameraStepMoveParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(move_direction: WDPDirection = WDPDirection.E_FORWARD,
             step: float = 0.000000,
             continuous: bool = False) -> None
```

<a id="unreal.CameraStepMoveParams.move_direction"></a>

#### move\_direction

```python
@property
def move_direction() -> WDPDirection
```

(WDPDirection):  [Read-Only]

<a id="unreal.CameraStepMoveParams.step"></a>

#### step

```python
@property
def step() -> float
```

(float):  [Read-Only]

<a id="unreal.CameraStepMoveParams.continuous"></a>

#### continuous

```python
@property
def continuous() -> bool
```

(bool):  [Read-Only]

<a id="unreal.CameraStepRotateParams"></a>