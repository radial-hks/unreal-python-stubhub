## AvaSequence Objects

```python
class AvaSequence(LevelSequence)
```

Ava Sequence

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequence.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``marks`` (Set[AvaMark]):  [Read-Write] The list of Marks in this Sequence
- ``preview_mark_label`` (str):  [Read-Write] The Mark to use to Preview the Sequence
- ``tag`` (AvaTagHandle):  [Read-Write]

<a id="unreal.AvaSequence.set_mark"></a>

#### set_mark

```python
def set_mark(mark_label: str, mark: AvaMark) -> bool
```

x.set_mark(mark_label, mark) -> bool
Set Mark

Args:
    mark_label (str): 
    mark (AvaMark): 

Returns:
    bool:

<a id="unreal.AvaSequence.set_label"></a>

#### set_label

```python
def set_label(label: Name) -> None
```

x.set_label(label) -> None
Set Label

Args:
    label (Name):

<a id="unreal.AvaSequence.get_start_time"></a>

#### get_start_time

```python
def get_start_time() -> float
```

x.get_start_time() -> double
Gets the Start Time of this Sequence

Returns:
    double:

<a id="unreal.AvaSequence.get_sequence_tag"></a>

#### get_sequence_tag

```python
def get_sequence_tag() -> AvaTagHandle
```

x.get_sequence_tag() -> AvaTagHandle
Get Sequence Tag

Returns:
    AvaTagHandle:

<a id="unreal.AvaSequence.get_marks"></a>

#### get_marks

```python
def get_marks() -> Set[AvaMark]
```

x.get_marks() -> Set[AvaMark]
Get Marks

Returns:
    Set[AvaMark]:

<a id="unreal.AvaSequence.get_mark"></a>

#### get_mark

```python
def get_mark(mark_label: str) -> Optional[AvaMark]
```

x.get_mark(mark_label) -> AvaMark or None
Get Mark

Args:
    mark_label (str): 

Returns:
    AvaMark or None: 

    out_mark (AvaMark):

<a id="unreal.AvaSequence.get_label"></a>

#### get_label

```python
def get_label() -> Name
```

x.get_label() -> Name
Get Label

Returns:
    Name:

<a id="unreal.AvaSequence.get_end_time"></a>

#### get_end_time

```python
def get_end_time() -> float
```

x.get_end_time() -> double
Gets the End Time of this Sequence

Returns:
    double:

<a id="unreal.AvaAnimation"></a>