## XRMotionControllerData Objects

```python
class XRMotionControllerData(StructBase)
```

XRMotion Controller Data

**C++ Source:**

- **Module**: HeadMountedDisplay
- **File**: HeadMountedDisplayTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aim_position`` (Vector):  [Read-Write] For handheld controllers, gives a vector for pointing at objects
- ``aim_rotation`` (Quat):  [Read-Write] For handheld controllers, gives a quaternion for pointing at objects
- ``application_instance_id`` (Guid):  [Read-Write]
- ``device_name`` (Name):  [Read-Write]
- ``device_visual_type`` (XRVisualType):  [Read-Write]
- ``grip_position`` (Vector):  [Read-Write] Vector representing an object being held in the player's hand
- ``grip_rotation`` (Quat):  [Read-Write] Quaternion representing an object being held in the player's hand
- ``hand_index`` (ControllerHand):  [Read-Write]
- ``hand_key_positions`` (Array[Vector]):  [Read-Write] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).
- ``hand_key_radii`` (Array[float]):  [Read-Write] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).
- ``hand_key_rotations`` (Array[Quat]):  [Read-Write] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).
- ``is_grasped`` (bool):  [Read-Write]
- ``palm_position`` (Vector):  [Read-Write] For handheld controllers, gives a vector for representing the hand
- ``palm_rotation`` (Quat):  [Read-Write] For handheld controllers, gives a quaternion for representing the hand
- ``tracking_status`` (TrackingStatus):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.XRMotionControllerData.__init__"></a>

#### __init__

```python
def __init__(valid: bool = False,
             device_name: Name = "None",
             application_instance_id: Guid = [],
             device_visual_type: XRVisualType = XRVisualType.CONTROLLER,
             hand_index: ControllerHand = ControllerHand.LEFT,
             tracking_status: TrackingStatus = TrackingStatus.NOT_TRACKED,
             grip_position: Vector = [0.000000, 0.000000, 0.000000],
             grip_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             aim_position: Vector = [0.000000, 0.000000, 0.000000],
             aim_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             palm_position: Vector = [0.000000, 0.000000, 0.000000],
             palm_rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             hand_key_positions: Array[Vector] = [],
             hand_key_rotations: Array[Quat] = [],
             hand_key_radii: Array[float] = [],
             is_grasped: bool = False) -> None
```

<a id="unreal.XRMotionControllerData.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.XRMotionControllerData.device_name"></a>

#### device_name

```python
@property
def device_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.XRMotionControllerData.application_instance_id"></a>

#### application_instance_id

```python
@property
def application_instance_id() -> Guid
```

(Guid):  [Read-Only]

<a id="unreal.XRMotionControllerData.device_visual_type"></a>

#### device_visual_type

```python
@property
def device_visual_type() -> XRVisualType
```

(XRVisualType):  [Read-Only]

<a id="unreal.XRMotionControllerData.hand_index"></a>

#### hand_index

```python
@property
def hand_index() -> ControllerHand
```

(ControllerHand):  [Read-Only]

<a id="unreal.XRMotionControllerData.tracking_status"></a>

#### tracking_status

```python
@property
def tracking_status() -> TrackingStatus
```

(TrackingStatus):  [Read-Only]

<a id="unreal.XRMotionControllerData.grip_position"></a>

#### grip_position

```python
@property
def grip_position() -> Vector
```

(Vector):  [Read-Only] Vector representing an object being held in the player's hand

<a id="unreal.XRMotionControllerData.grip_rotation"></a>

#### grip_rotation

```python
@property
def grip_rotation() -> Quat
```

(Quat):  [Read-Only] Quaternion representing an object being held in the player's hand

<a id="unreal.XRMotionControllerData.aim_position"></a>

#### aim_position

```python
@property
def aim_position() -> Vector
```

(Vector):  [Read-Only] For handheld controllers, gives a vector for pointing at objects

<a id="unreal.XRMotionControllerData.aim_rotation"></a>

#### aim_rotation

```python
@property
def aim_rotation() -> Quat
```

(Quat):  [Read-Only] For handheld controllers, gives a quaternion for pointing at objects

<a id="unreal.XRMotionControllerData.palm_position"></a>

#### palm_position

```python
@property
def palm_position() -> Vector
```

(Vector):  [Read-Only] For handheld controllers, gives a vector for representing the hand

<a id="unreal.XRMotionControllerData.palm_rotation"></a>

#### palm_rotation

```python
@property
def palm_rotation() -> Quat
```

(Quat):  [Read-Only] For handheld controllers, gives a quaternion for representing the hand

<a id="unreal.XRMotionControllerData.hand_key_positions"></a>

#### hand_key_positions

```python
@property
def hand_key_positions() -> Array[Vector]
```

(Array[Vector]):  [Read-Only] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

<a id="unreal.XRMotionControllerData.hand_key_rotations"></a>

#### hand_key_rotations

```python
@property
def hand_key_rotations() -> Array[Quat]
```

(Array[Quat]):  [Read-Only] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

<a id="unreal.XRMotionControllerData.hand_key_radii"></a>

#### hand_key_radii

```python
@property
def hand_key_radii() -> Array[float]
```

(Array[float]):  [Read-Only] The indices of this array are the values of EHandKeypoint (Palm, Wrist, ThumbMetacarpal, etc).

<a id="unreal.XRMotionControllerData.is_grasped"></a>

#### is_grasped

```python
@property
def is_grasped() -> bool
```

(bool):  [Read-Only]

<a id="unreal.XRMotionControllerState"></a>