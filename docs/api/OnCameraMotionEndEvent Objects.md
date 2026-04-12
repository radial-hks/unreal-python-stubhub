## OnCameraMotionEndEvent Objects

```python
class OnCameraMotionEndEvent(EventArgsBase)
```

On Camera Motion End Event

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_motion_reason`` (str):  [Read-Write]
- ``eids`` (Array[str]):  [Read-Write]

<a id="unreal.OnCameraMotionEndEvent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(camera_motion_reason: str = "", eids: Array[str] = []) -> None
```

<a id="unreal.OnCameraMotionEndEvent.camera_motion_reason"></a>

#### camera\_motion\_reason

```python
@property
def camera_motion_reason() -> str
```

(str):  [Read-Write]

<a id="unreal.OnCameraMotionEndEvent.camera_motion_reason"></a>

#### camera\_motion\_reason

```python
@camera_motion_reason.setter
def camera_motion_reason(value: str) -> None
```

<a id="unreal.OnCameraMotionEndEvent.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.OnCameraMotionEndEvent.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.WdpFocusToAllEntitiesParams"></a>