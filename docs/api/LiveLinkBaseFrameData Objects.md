## LiveLinkBaseFrameData Objects

```python
class LiveLinkBaseFrameData(StructBase)
```

Base data structure for each frame coming in for a subject
note: subclass can't contains reference to UObject

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkBaseFrameData.__init__"></a>

#### __init__

```python
def __init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
             property_values: Array[float] = []) -> None
```

<a id="unreal.LiveLinkBaseFrameData.meta_data"></a>

#### meta_data

```python
@property
def meta_data() -> LiveLinkMetaData
```

(LiveLinkMetaData):  [Read-Write] Frame's metadata.

<a id="unreal.LiveLinkBaseFrameData.meta_data"></a>

#### meta_data

```python
@meta_data.setter
def meta_data(value: LiveLinkMetaData) -> None
```

<a id="unreal.LiveLinkBaseFrameData.property_values"></a>

#### property_values

```python
@property
def property_values() -> Array[float]
```

(Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.

<a id="unreal.LiveLinkBaseFrameData.property_values"></a>

#### property_values

```python
@property_values.setter
def property_values(value: Array[float]) -> None
```

<a id="unreal.LiveLinkMetaData"></a>