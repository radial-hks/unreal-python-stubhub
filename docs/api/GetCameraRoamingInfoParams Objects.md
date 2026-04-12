## GetCameraRoamingInfoParams Objects

```python
class GetCameraRoamingInfoParams(ParamsBase)
```

Get Camera Roaming Info Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpCameraControlAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_roam_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GetCameraRoamingInfoParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(camera_roam_eid: int = 0) -> None
```

<a id="unreal.GetCameraRoamingInfoParams.camera_roam_eid"></a>

#### camera\_roam\_eid

```python
@property
def camera_roam_eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.GetCameraRoamingInfoParams.camera_roam_eid"></a>

#### camera\_roam\_eid

```python
@camera_roam_eid.setter
def camera_roam_eid(value: int) -> None
```

<a id="unreal.GetCameraRoamingInfoResult"></a>