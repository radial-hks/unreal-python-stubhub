## SwapAudioOutputResult Objects

```python
class SwapAudioOutputResult(StructBase)
```

Out structure for use with AudioMixerBlueprintLibrary::SwapAudioOutputDevice

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerBlueprintLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current_device_id`` (str):  [Read-Write] ID of the currently set device.  This is the device at the time of the call, NOT the resulting deviceId
- ``requested_device_id`` (str):  [Read-Write] ID of the requested device.
- ``result`` (SwapAudioOutputDeviceResultState):  [Read-Write] Result of the call

<a id="unreal.SwapAudioOutputResult.__init__"></a>

#### __init__

```python
def __init__(
    current_device_id: str = "",
    requested_device_id: str = "",
    result: SwapAudioOutputDeviceResultState = SwapAudioOutputDeviceResultState
    .FAILURE
) -> None
```

<a id="unreal.SwapAudioOutputResult.current_device_id"></a>

#### current_device_id

```python
@property
def current_device_id() -> str
```

(str):  [Read-Only] ID of the currently set device.  This is the device at the time of the call, NOT the resulting deviceId

<a id="unreal.SwapAudioOutputResult.requested_device_id"></a>

#### requested_device_id

```python
@property
def requested_device_id() -> str
```

(str):  [Read-Only] ID of the requested device.

<a id="unreal.SwapAudioOutputResult.result"></a>

#### result

```python
@property
def result() -> SwapAudioOutputDeviceResultState
```

(SwapAudioOutputDeviceResultState):  [Read-Only] Result of the call

<a id="unreal.NiagaraSimCacheCaptureParameters"></a>