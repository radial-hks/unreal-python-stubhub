## LiveLinkTransformBlueprintData Objects

```python
class LiveLinkTransformBlueprintData(LiveLinkBaseBlueprintData)
```

Facility structure to handle transform data in blueprint

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTransformTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_data`` (LiveLinkTransformFrameData):  [Read-Write] Dynamic data that can change every frame
- ``static_data`` (LiveLinkTransformStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkTransformBlueprintData.__init__"></a>

#### __init__

```python
def __init__(
    static_data: LiveLinkTransformStaticData = [True, True, False, []],
    frame_data: LiveLinkTransformFrameData = [[[0.000000, 0.000000, 0.000000],
                                               [-0.000000, 0.000000, 0.000000],
                                               [1.000000, 1.000000, 1.000000]],
                                              [{}, [[0], [24, 1], 0.000000]],
                                              []]
) -> None
```

<a id="unreal.LiveLinkTransformBlueprintData.static_data"></a>

#### static_data

```python
@property
def static_data() -> LiveLinkTransformStaticData
```

(LiveLinkTransformStaticData):  [Read-Write] Static data that should not change every frame

<a id="unreal.LiveLinkTransformBlueprintData.static_data"></a>

#### static_data

```python
@static_data.setter
def static_data(value: LiveLinkTransformStaticData) -> None
```

<a id="unreal.LiveLinkTransformBlueprintData.frame_data"></a>

#### frame_data

```python
@property
def frame_data() -> LiveLinkTransformFrameData
```

(LiveLinkTransformFrameData):  [Read-Write] Dynamic data that can change every frame

<a id="unreal.LiveLinkTransformBlueprintData.frame_data"></a>

#### frame_data

```python
@frame_data.setter
def frame_data(value: LiveLinkTransformFrameData) -> None
```

<a id="unreal.LiveLinkCurveConversionSettings"></a>