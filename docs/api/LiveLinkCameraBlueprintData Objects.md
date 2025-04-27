## LiveLinkCameraBlueprintData Objects

```python
class LiveLinkCameraBlueprintData(LiveLinkBaseBlueprintData)
```

Facility structure to handle camera data in blueprint

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkCameraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_data`` (LiveLinkCameraFrameData):  [Read-Write] Dynamic data that can change every frame
- ``static_data`` (LiveLinkCameraStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkCameraBlueprintData.__init__"></a>

#### __init__

```python
def __init__(
    static_data: LiveLinkCameraStaticData = [
        False, False, False, False, -1.000000, -1.000000, False, False, True,
        True, True, False, []
    ],
    frame_data: LiveLinkCameraFrameData = [
        90.000000, 1.777778, 50.000000, 2.800000, 100000.000000,
        LiveLinkCameraProjectionMode.PERSPECTIVE,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], [{}, [[0], [24, 1], 0.000000]], []
    ]
) -> None
```

<a id="unreal.LiveLinkCameraBlueprintData.static_data"></a>

#### static_data

```python
@property
def static_data() -> LiveLinkCameraStaticData
```

(LiveLinkCameraStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkCameraBlueprintData.static_data"></a>

#### static_data

```python
@static_data.setter
def static_data(value: LiveLinkCameraStaticData) -> None
```

<a id="unreal.LiveLinkCameraBlueprintData.frame_data"></a>

#### frame_data

```python
@property
def frame_data() -> LiveLinkCameraFrameData
```

(LiveLinkCameraFrameData):  [Read-Write] Dynamic data that can change every frame

<a id="unreal.LiveLinkCameraBlueprintData.frame_data"></a>

#### frame_data

```python
@frame_data.setter
def frame_data(value: LiveLinkCameraFrameData) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceStaticData"></a>