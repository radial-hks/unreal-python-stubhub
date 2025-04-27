## MediaIOOutputConfiguration Objects

```python
class MediaIOOutputConfiguration(StructBase)
```

Configuration of a device output.

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaIOCoreDefinitions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``key_port_identifier`` (int32):  [Read-Only] The port of the video channel on the device to output the key to.
  note: 'Frame Buffer Pixel Format' must be set to at least 8 bits of alpha.
  note: 'Enable alpha channel support in post-processing' must be set to 'Allow through tonemapper'.
- ``media_configuration`` (MediaIOConfiguration):  [Read-Only] The signal output format.
- ``output_reference`` (MediaIOReferenceType):  [Read-Only] The Device output sync with either its internal clock, an external reference, or an other input.
- ``output_type`` (MediaIOOutputType):  [Read-Only] Whether to output the fill or the fill and key.
- ``reference_port_identifier`` (int32):  [Read-Only] The port of the video channel on the device to output the synchronize to.

<a id="unreal.MediaIOOutputConfiguration.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AvaRundownMacroKeyBinding"></a>