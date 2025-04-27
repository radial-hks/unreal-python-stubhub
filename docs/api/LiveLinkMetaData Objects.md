## LiveLinkMetaData Objects

```python
class LiveLinkMetaData(StructBase)
```

Live Link Meta Data

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scene_time`` (QualifiedTime):  [Read-Write]
- ``string_meta_data`` (Map[Name, str]):  [Read-Write]

<a id="unreal.LiveLinkMetaData.__init__"></a>

#### __init__

```python
def __init__(string_meta_data: Map[Name, str] = {},
             scene_time: QualifiedTime = [[0], [24, 1], 0.000000]) -> None
```

<a id="unreal.LiveLinkMetaData.string_meta_data"></a>

#### string_meta_data

```python
@property
def string_meta_data() -> Map[Name, str]
```

(Map[Name, str]):  [Read-Write]

<a id="unreal.LiveLinkMetaData.string_meta_data"></a>

#### string_meta_data

```python
@string_meta_data.setter
def string_meta_data(value: Map[Name, str]) -> None
```

<a id="unreal.LiveLinkMetaData.scene_time"></a>

#### scene_time

```python
@property
def scene_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Write]

<a id="unreal.LiveLinkMetaData.scene_time"></a>

#### scene_time

```python
@scene_time.setter
def scene_time(value: QualifiedTime) -> None
```

<a id="unreal.LiveLinkAnimationFrameData"></a>