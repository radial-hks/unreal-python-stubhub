## LiveLinkBasicBlueprintData Objects

```python
class LiveLinkBasicBlueprintData(LiveLinkBaseBlueprintData)
```

Facility structure to handle base data in blueprint

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkBasicTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_data`` (LiveLinkBaseFrameData):  [Read-Write] Dynamic data that can change every frame
- ``static_data`` (LiveLinkBaseStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkBasicBlueprintData.__init__"></a>

#### __init__

```python
def __init__(
    static_data: LiveLinkBaseStaticData = [[]],
    frame_data: LiveLinkBaseFrameData = [[{}, [[0], [24, 1], 0.000000]], []]
) -> None
```

<a id="unreal.LiveLinkBasicBlueprintData.static_data"></a>

#### static_data

```python
@property
def static_data() -> LiveLinkBaseStaticData
```

(LiveLinkBaseStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkBasicBlueprintData.static_data"></a>

#### static_data

```python
@static_data.setter
def static_data(value: LiveLinkBaseStaticData) -> None
```

<a id="unreal.LiveLinkBasicBlueprintData.frame_data"></a>

#### frame_data

```python
@property
def frame_data() -> LiveLinkBaseFrameData
```

(LiveLinkBaseFrameData):  [Read-Write] Dynamic data that can change every frame

<a id="unreal.LiveLinkBasicBlueprintData.frame_data"></a>

#### frame_data

```python
@frame_data.setter
def frame_data(value: LiveLinkBaseFrameData) -> None
```

<a id="unreal.LiveLinkTransformStaticData"></a>