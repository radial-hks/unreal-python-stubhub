## LiveLinkGamepadInputDeviceBlueprintData Objects

```python
class LiveLinkGamepadInputDeviceBlueprintData(LiveLinkBaseBlueprintData)
```

Facility structure to handle Preston MDR data in blueprint

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkInputDeviceTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_data`` (LiveLinkGamepadInputDeviceFrameData):  [Read-Write] Dynamic data that can change every frame
- ``static_data`` (LiveLinkGamepadInputDeviceStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkGamepadInputDeviceBlueprintData.__init__"></a>

#### __init__

```python
def __init__(
    static_data: LiveLinkGamepadInputDeviceStaticData = [[]],
    frame_data: LiveLinkGamepadInputDeviceFrameData = [
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,
        0.000000, 0.000000, 0.000000, 0.000000, [{}, [[0], [24, 1], 0.000000]],
        []
    ]
) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceBlueprintData.static_data"></a>

#### static_data

```python
@property
def static_data() -> LiveLinkGamepadInputDeviceStaticData
```

(LiveLinkGamepadInputDeviceStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkGamepadInputDeviceBlueprintData.static_data"></a>

#### static_data

```python
@static_data.setter
def static_data(value: LiveLinkGamepadInputDeviceStaticData) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceBlueprintData.frame_data"></a>

#### frame_data

```python
@property
def frame_data() -> LiveLinkGamepadInputDeviceFrameData
```

(LiveLinkGamepadInputDeviceFrameData):  [Read-Write] Dynamic data that can change every frame

<a id="unreal.LiveLinkGamepadInputDeviceBlueprintData.frame_data"></a>

#### frame_data

```python
@frame_data.setter
def frame_data(value: LiveLinkGamepadInputDeviceFrameData) -> None
```

<a id="unreal.LiveLinkLightStaticData"></a>