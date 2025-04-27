## RevisionInfo Objects

```python
class RevisionInfo(StructBase)
```

Revision information for a single revision of a file in source control

**C++ Source:**

- **Module**: AssetDefinition
- **File**: AssetDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``changelist`` (int32):  [Read-Write]
- ``date`` (DateTime):  [Read-Write]
- ``revision`` (str):  [Read-Write]

<a id="unreal.RevisionInfo.__init__"></a>

#### __init__

```python
def __init__(revision: str = "",
             changelist: int = 0,
             date: DateTime = []) -> None
```

<a id="unreal.RevisionInfo.revision"></a>

#### revision

```python
@property
def revision() -> str
```

(str):  [Read-Write]

<a id="unreal.RevisionInfo.revision"></a>

#### revision

```python
@revision.setter
def revision(value: str) -> None
```

<a id="unreal.RevisionInfo.changelist"></a>

#### changelist

```python
@property
def changelist() -> int
```

(int32):  [Read-Write]

<a id="unreal.RevisionInfo.changelist"></a>

#### changelist

```python
@changelist.setter
def changelist(value: int) -> None
```

<a id="unreal.RevisionInfo.date"></a>

#### date

```python
@property
def date() -> DateTime
```

(DateTime):  [Read-Write]

<a id="unreal.RevisionInfo.date"></a>

#### date

```python
@date.setter
def date(value: DateTime) -> None
```

<a id="unreal.EdGraphPinType"></a>