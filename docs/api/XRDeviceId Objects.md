## XRDeviceId Objects

```python
class XRDeviceId(StructBase)
```

XRDevice Id

**C++ Source:**

- **Module**: HeadMountedDisplay
- **File**: IIdentifiableXRDevice.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device_id`` (int32):  [Read-Write]
- ``system_name`` (Name):  [Read-Write]

<a id="unreal.XRDeviceId.__init__"></a>

#### \_\_init\_\_

```python
def __init__(system_name: Name = "None", device_id: int = 0) -> None
```

<a id="unreal.XRDeviceId.system_name"></a>

#### system\_name

```python
@property
def system_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.XRDeviceId.device_id"></a>

#### device\_id

```python
@property
def device_id() -> int
```

(int32):  [Read-Only]

<a id="unreal.PostProcessSettings"></a>