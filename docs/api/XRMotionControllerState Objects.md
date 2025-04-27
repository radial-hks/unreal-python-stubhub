## XRMotionControllerState Objects

```python
class XRMotionControllerState(StructBase)
```

XRMotion Controller State

**C++ Source:**

- **Module**: HeadMountedDisplay
- **File**: HeadMountedDisplayTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``application_instance_id`` (Guid):  [Read-Write]
- ``controller_location`` (Vector):  [Read-Write]
- ``controller_rotation`` (Quat):  [Read-Write]
- ``device_name`` (Name):  [Read-Write]
- ``hand`` (ControllerHand):  [Read-Write]
- ``tracking_status`` (TrackingStatus):  [Read-Write] If a controller pose has been provided this frame the TrackingStatus will be Tracked.
- ``valid`` (bool):  [Read-Write] The state is valid if a pose has ever been provided.
- ``xr_controller_pose_type`` (XRControllerPoseType):  [Read-Write]
- ``xr_space_type`` (XRSpaceType):  [Read-Write]

<a id="unreal.XRMotionControllerState.__init__"></a>

#### __init__

```python
def __init__(
    valid: bool = False,
    device_name: Name = "None",
    application_instance_id: Guid = [],
    xr_space_type: XRSpaceType = XRSpaceType.UNREAL_WORLD_SPACE,
    hand: ControllerHand = ControllerHand.LEFT,
    tracking_status: TrackingStatus = TrackingStatus.NOT_TRACKED,
    xr_controller_pose_type: XRControllerPoseType = XRControllerPoseType.AIM,
    controller_location: Vector = [0.000000, 0.000000, 0.000000],
    controller_rotation: Quat = [0.000000, 0.000000, 0.000000,
                                 1.000000]) -> None
```

<a id="unreal.XRMotionControllerState.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only] The state is valid if a pose has ever been provided.

<a id="unreal.XRMotionControllerState.device_name"></a>

#### device_name

```python
@property
def device_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.XRMotionControllerState.application_instance_id"></a>

#### application_instance_id

```python
@property
def application_instance_id() -> Guid
```

(Guid):  [Read-Only]

<a id="unreal.XRMotionControllerState.xr_space_type"></a>

#### xr_space_type

```python
@property
def xr_space_type() -> XRSpaceType
```

(XRSpaceType):  [Read-Only]

<a id="unreal.XRMotionControllerState.hand"></a>

#### hand

```python
@property
def hand() -> ControllerHand
```

(ControllerHand):  [Read-Only]

<a id="unreal.XRMotionControllerState.tracking_status"></a>

#### tracking_status

```python
@property
def tracking_status() -> TrackingStatus
```

(TrackingStatus):  [Read-Only] If a controller pose has been provided this frame the TrackingStatus will be Tracked.

<a id="unreal.XRMotionControllerState.xr_controller_pose_type"></a>

#### xr_controller_pose_type

```python
@property
def xr_controller_pose_type() -> XRControllerPoseType
```

(XRControllerPoseType):  [Read-Only]

<a id="unreal.XRMotionControllerState.controller_location"></a>

#### controller_location

```python
@property
def controller_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.XRMotionControllerState.controller_rotation"></a>

#### controller_rotation

```python
@property
def controller_rotation() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.XRHandTrackingState"></a>