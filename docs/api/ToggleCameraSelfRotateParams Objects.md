## ToggleCameraSelfRotateParams Objects

```python
class ToggleCameraSelfRotateParams(EidParams)
```

Toggle Camera Self Rotate Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``self_rotate`` (bool):  [Read-Write]

<a id="unreal.ToggleCameraSelfRotateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(self_rotate: bool = False) -> None
```

<a id="unreal.ToggleCameraSelfRotateParams.self_rotate"></a>

#### self\_rotate

```python
@property
def self_rotate() -> bool
```

(bool):  [Read-Only]

<a id="unreal.OnCameraMotionStartEvent"></a>