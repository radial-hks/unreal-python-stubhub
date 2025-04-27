## XRHandTrackingState Objects

```python
class XRHandTrackingState(StructBase)
```

XRHand Tracking State

**C++ Source:**

- **Module**: HeadMountedDisplay
- **File**: HeadMountedDisplayTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``application_instance_id`` (Guid):  [Read-Write]
- ``device_name`` (Name):  [Read-Write]
- ``hand`` (ControllerHand):  [Read-Write]
- ``hand_key_locations`` (Array[Vector]):  [Read-Write] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).
- ``hand_key_radii`` (Array[float]):  [Read-Write] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).
- ``hand_key_rotations`` (Array[Quat]):  [Read-Write] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).
- ``tracking_status`` (TrackingStatus):  [Read-Write]
- ``valid`` (bool):  [Read-Write] The state is valid if poses have ever been provided.
- ``xr_space_type`` (XRSpaceType):  [Read-Write]

<a id="unreal.XRHandTrackingState.__init__"></a>

#### __init__

```python
def __init__(valid: bool = False,
             device_name: Name = "None",
             application_instance_id: Guid = [],
             xr_space_type: XRSpaceType = XRSpaceType.UNREAL_WORLD_SPACE,
             hand: ControllerHand = ControllerHand.LEFT,
             tracking_status: TrackingStatus = TrackingStatus.NOT_TRACKED,
             hand_key_locations: Array[Vector] = [],
             hand_key_rotations: Array[Quat] = [],
             hand_key_radii: Array[float] = []) -> None
```

<a id="unreal.XRHandTrackingState.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only] The state is valid if poses have ever been provided.

<a id="unreal.XRHandTrackingState.device_name"></a>

#### device_name

```python
@property
def device_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.XRHandTrackingState.application_instance_id"></a>

#### application_instance_id

```python
@property
def application_instance_id() -> Guid
```

(Guid):  [Read-Only]

<a id="unreal.XRHandTrackingState.xr_space_type"></a>

#### xr_space_type

```python
@property
def xr_space_type() -> XRSpaceType
```

(XRSpaceType):  [Read-Only]

<a id="unreal.XRHandTrackingState.hand"></a>

#### hand

```python
@property
def hand() -> ControllerHand
```

(ControllerHand):  [Read-Only]

<a id="unreal.XRHandTrackingState.tracking_status"></a>

#### tracking_status

```python
@property
def tracking_status() -> TrackingStatus
```

(TrackingStatus):  [Read-Only]

<a id="unreal.XRHandTrackingState.hand_key_locations"></a>

#### hand_key_locations

```python
@property
def hand_key_locations() -> Array[Vector]
```

(Array[Vector]):  [Read-Only] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

<a id="unreal.XRHandTrackingState.hand_key_rotations"></a>

#### hand_key_rotations

```python
@property
def hand_key_rotations() -> Array[Quat]
```

(Array[Quat]):  [Read-Only] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

<a id="unreal.XRHandTrackingState.hand_key_radii"></a>

#### hand_key_radii

```python
@property
def hand_key_radii() -> Array[float]
```

(Array[float]):  [Read-Only] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

<a id="unreal.XRDeviceId"></a>