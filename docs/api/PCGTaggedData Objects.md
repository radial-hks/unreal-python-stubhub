## PCGTaggedData Objects

```python
class PCGTaggedData(StructBase)
```

PCGTagged Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data`` (PCGData):  [Read-Write]
- ``is_used_multiple_times`` (bool):  [Read-Write] Special flag to be modified by execution when a data is used multiple times (in this node or other nodes),
  to enable optimization when they are not. Always assume that it is true by default.
- ``pin`` (Name):  [Read-Write] The label of the pin that this data was either emitted from or received on.
- ``tags`` (Set[str]):  [Read-Write]

<a id="unreal.PCGTaggedData.__init__"></a>

#### __init__

```python
def __init__(data: PCGData = None,
             tags: Set[str] = [],
             pin: Name = "None",
             is_used_multiple_times: bool = False) -> None
```

<a id="unreal.PCGTaggedData.data"></a>

#### data

```python
@property
def data() -> PCGData
```

(PCGData):  [Read-Write]

<a id="unreal.PCGTaggedData.data"></a>

#### data

```python
@data.setter
def data(value: PCGData) -> None
```

<a id="unreal.PCGTaggedData.tags"></a>

#### tags

```python
@property
def tags() -> Set[str]
```

(Set[str]):  [Read-Write]

<a id="unreal.PCGTaggedData.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Set[str]) -> None
```

<a id="unreal.PCGTaggedData.pin"></a>

#### pin

```python
@property
def pin() -> Name
```

(Name):  [Read-Write] The label of the pin that this data was either emitted from or received on.

<a id="unreal.PCGTaggedData.pin"></a>

#### pin

```python
@pin.setter
def pin(value: Name) -> None
```

<a id="unreal.PCGTaggedData.is_used_multiple_times"></a>

#### is_used_multiple_times

```python
@property
def is_used_multiple_times() -> bool
```

(bool):  [Read-Only] Special flag to be modified by execution when a data is used multiple times (in this node or other nodes),
to enable optimization when they are not. Always assume that it is true by default.

<a id="unreal.PCGDeterminismSettings"></a>