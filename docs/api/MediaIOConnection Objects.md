## MediaIOConnection Objects

```python
class MediaIOConnection(StructBase)
```

Identifies an media connection.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaIOCoreDefinitions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``device`` (MediaIODevice):  [Read-Write] The device identifier.
- ``port_identifier`` (int32):  [Read-Write] The port of the video channel on the device.
- ``protocol`` (Name):  [Read-Write] The protocol used by the MediaFramework.
- ``quad_transport_type`` (MediaIOQuadLinkTransportType):  [Read-Write] The type of cable link used for that configuration
- ``transport_type`` (MediaIOTransportType):  [Read-Write] The type of cable link used for that configuration

<a id="unreal.MediaIOConnection.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MediaIOMode"></a>