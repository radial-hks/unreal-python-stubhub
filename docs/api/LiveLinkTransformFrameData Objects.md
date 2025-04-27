## LiveLinkTransformFrameData Objects

```python
class LiveLinkTransformFrameData(LiveLinkBaseFrameData)
```

Dynamic data for Transform

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTransformTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``transform`` (Transform):  [Read-Write] Transform of the frame
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkTransformFrameData.__init__"></a>

#### __init__

```python
def __init__(
    meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
    property_values: Array[float] = [],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.LiveLinkTransformFrameData.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] Transform of the frame

<a id="unreal.LiveLinkTransformFrameData.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.LiveLinkCameraFrameData"></a>