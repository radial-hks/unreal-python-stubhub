## LiveLinkSubjectProperty Objects

```python
class LiveLinkSubjectProperty(StructBase)
```

Live Link Subject Property

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLinkSequencer
- **File**: TakeRecorderLiveLinkSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``subject_name`` (Name):  [Read-Write]

<a id="unreal.LiveLinkSubjectProperty.__init__"></a>

#### __init__

```python
def __init__(subject_name: Name = "None", enabled: bool = False) -> None
```

<a id="unreal.LiveLinkSubjectProperty.subject_name"></a>

#### subject_name

```python
@property
def subject_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.LiveLinkSubjectProperty.subject_name"></a>

#### subject_name

```python
@subject_name.setter
def subject_name(value: Name) -> None
```

<a id="unreal.LiveLinkSubjectProperty.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LiveLinkSubjectProperty.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.MotionWarpingWindowData"></a>