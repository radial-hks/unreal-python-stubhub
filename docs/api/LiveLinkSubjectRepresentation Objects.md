## LiveLinkSubjectRepresentation Objects

```python
class LiveLinkSubjectRepresentation(StructBase)
```

Live Link Subject Representation

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkRole.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``role`` (type(Class)):  [Read-Write]
- ``subject`` (LiveLinkSubjectName):  [Read-Write]

<a id="unreal.LiveLinkSubjectRepresentation.__init__"></a>

#### __init__

```python
def __init__(subject: LiveLinkSubjectName = ["None"],
             role: Class = None) -> None
```

<a id="unreal.LiveLinkSubjectRepresentation.subject"></a>

#### subject

```python
@property
def subject() -> LiveLinkSubjectName
```

(LiveLinkSubjectName):  [Read-Write]

<a id="unreal.LiveLinkSubjectRepresentation.subject"></a>

#### subject

```python
@subject.setter
def subject(value: LiveLinkSubjectName) -> None
```

<a id="unreal.LiveLinkSubjectRepresentation.role"></a>

#### role

```python
@property
def role() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.LiveLinkSubjectRepresentation.role"></a>

#### role

```python
@role.setter
def role(value: Class) -> None
```

<a id="unreal.LiveLinkTransformBlueprintData"></a>