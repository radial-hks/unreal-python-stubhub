## LiveLinkSubjectKey Objects

```python
class LiveLinkSubjectKey(StructBase)
```

Structure that identifies an individual subject

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``source`` (Guid):  [Read-Write] The guid for this subjects source
- ``subject_name`` (LiveLinkSubjectName):  [Read-Write] The Name of this subject

<a id="unreal.LiveLinkSubjectKey.__init__"></a>

#### __init__

```python
def __init__(source: Guid = [],
             subject_name: LiveLinkSubjectName = ["None"]) -> None
```

<a id="unreal.LiveLinkSubjectKey.source"></a>

#### source

```python
@property
def source() -> Guid
```

(Guid):  [Read-Only] The guid for this subjects source

<a id="unreal.LiveLinkSubjectKey.subject_name"></a>

#### subject_name

```python
@property
def subject_name() -> LiveLinkSubjectName
```

(LiveLinkSubjectName):  [Read-Only] The Name of this subject

<a id="unreal.LiveLinkSubjectName"></a>