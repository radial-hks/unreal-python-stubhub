## LiveLinkLightBlueprintData Objects

```python
class LiveLinkLightBlueprintData(LiveLinkBaseBlueprintData)
```

Facility structure to handle light data in blueprint

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkLightTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_data`` (LiveLinkLightFrameData):  [Read-Write] Dynamic data that can change every frame
- ``static_data`` (LiveLinkLightStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkLightBlueprintData.__init__"></a>

#### __init__

```python
def __init__(
    static_data: LiveLinkLightStaticData = [
        False, False, False, False, False, False, False, False, False, True,
        True, False, []
    ],
    frame_data: LiveLinkLightFrameData = [
        6500.000000, 3.141593, [255, 255, 255, 255], 0.000000, 44.000000,
        1000.000000, 0.000000, 0.000000, 0.000000,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], [{}, [[0], [24, 1], 0.000000]], []
    ]
) -> None
```

<a id="unreal.LiveLinkLightBlueprintData.static_data"></a>

#### static_data

```python
@property
def static_data() -> LiveLinkLightStaticData
```

(LiveLinkLightStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkLightBlueprintData.static_data"></a>

#### static_data

```python
@static_data.setter
def static_data(value: LiveLinkLightStaticData) -> None
```

<a id="unreal.LiveLinkLightBlueprintData.frame_data"></a>

#### frame_data

```python
@property
def frame_data() -> LiveLinkLightFrameData
```

(LiveLinkLightFrameData):  [Read-Write] Dynamic data that can change every frame

<a id="unreal.LiveLinkLightBlueprintData.frame_data"></a>

#### frame_data

```python
@frame_data.setter
def frame_data(value: LiveLinkLightFrameData) -> None
```

<a id="unreal.LiveLinkSubjectKey"></a>