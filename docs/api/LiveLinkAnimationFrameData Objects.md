## LiveLinkAnimationFrameData Objects

```python
class LiveLinkAnimationFrameData(LiveLinkBaseFrameData)
```

Dynamic data for Animation purposes.

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkAnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``transforms`` (Array[Transform]):  [Read-Write] Array of transforms for each bone of the skeleton
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkAnimationFrameData.__init__"></a>

#### __init__

```python
def __init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
             property_values: Array[float] = [],
             transforms: Array[Transform] = []) -> None
```

<a id="unreal.LiveLinkAnimationFrameData.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] Array of transforms for each bone of the skeleton

<a id="unreal.LiveLinkAnimationFrameData.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.LiveLinkBaseBlueprintData"></a>