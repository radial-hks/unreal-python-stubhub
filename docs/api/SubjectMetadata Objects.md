## SubjectMetadata Objects

```python
class SubjectMetadata(StructBase)
```

Subject Metadata

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkAnimationBlueprintStructs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scene_framerate`` (FrameRate):  [Read-Write]
- ``scene_timecode`` (Timecode):  [Read-Write]
- ``string_metadata`` (Map[Name, str]):  [Read-Write]

<a id="unreal.SubjectMetadata.__init__"></a>

#### \_\_init\_\_

```python
def __init__(string_metadata: Map[Name, str] = {},
             scene_timecode: Timecode = [0, 0, 0, 0, 0.000000, False],
             scene_framerate: FrameRate = [60000, 1]) -> None
```

<a id="unreal.SubjectMetadata.string_metadata"></a>

#### string\_metadata

```python
@property
def string_metadata() -> Map[Name, str]
```

(Map[Name, str]):  [Read-Write]

<a id="unreal.SubjectMetadata.string_metadata"></a>

#### string\_metadata

```python
@string_metadata.setter
def string_metadata(value: Map[Name, str]) -> None
```

<a id="unreal.SubjectMetadata.scene_timecode"></a>

#### scene\_timecode

```python
@property
def scene_timecode() -> Timecode
```

(Timecode):  [Read-Write]

<a id="unreal.SubjectMetadata.scene_timecode"></a>

#### scene\_timecode

```python
@scene_timecode.setter
def scene_timecode(value: Timecode) -> None
```

<a id="unreal.SubjectMetadata.scene_framerate"></a>

#### scene\_framerate

```python
@property
def scene_framerate() -> FrameRate
```

(FrameRate):  [Read-Write]

<a id="unreal.SubjectMetadata.scene_framerate"></a>

#### scene\_framerate

```python
@scene_framerate.setter
def scene_framerate(value: FrameRate) -> None
```

<a id="unreal.LiveLinkTransform"></a>