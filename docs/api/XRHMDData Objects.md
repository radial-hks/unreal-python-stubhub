## XRHMDData Objects

```python
class XRHMDData(StructBase)
```

XRHMDData

**C++ Source:**

- **Module**: HeadMountedDisplay
- **File**: HeadMountedDisplayTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``application_instance_id`` (Guid):  [Read-Write]
- ``device_name`` (Name):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``rotation`` (Quat):  [Read-Write]
- ``tracking_status`` (TrackingStatus):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.XRHMDData.__init__"></a>

#### __init__

```python
def __init__(
        valid: bool = False,
        device_name: Name = "None",
        application_instance_id: Guid = [],
        tracking_status: TrackingStatus = TrackingStatus.NOT_TRACKED,
        position: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.XRHMDData.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.XRHMDData.device_name"></a>

#### device_name

```python
@property
def device_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.XRHMDData.application_instance_id"></a>

#### application_instance_id

```python
@property
def application_instance_id() -> Guid
```

(Guid):  [Read-Only]

<a id="unreal.XRHMDData.tracking_status"></a>

#### tracking_status

```python
@property
def tracking_status() -> TrackingStatus
```

(TrackingStatus):  [Read-Only]

<a id="unreal.XRHMDData.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.XRHMDData.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.XRMotionControllerData"></a>