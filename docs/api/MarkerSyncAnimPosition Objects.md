## MarkerSyncAnimPosition Objects

```python
class MarkerSyncAnimPosition(StructBase)
```

Represent a current play position in an animation
based on sync markers

**C++ Source:**

- **Module**: Engine
- **File**: AnimationAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``next_marker_name`` (Name):  [Read-Write] The marker we are heading towards
- ``position_between_markers`` (float):  [Read-Write] Value between 0 and 1 representing where we are:
        0   we are at PreviousMarker
        1   we are at NextMarker
        0.5 we are half way between the two
- ``previous_marker_name`` (Name):  [Read-Write] The marker we have passed

<a id="unreal.MarkerSyncAnimPosition.__init__"></a>

#### __init__

```python
def __init__(previous_marker_name: Name = "None",
             next_marker_name: Name = "None",
             position_between_markers: float = 0.000000) -> None
```

<a id="unreal.MarkerSyncAnimPosition.previous_marker_name"></a>

#### previous_marker_name

```python
@property
def previous_marker_name() -> Name
```

(Name):  [Read-Write] The marker we have passed

<a id="unreal.MarkerSyncAnimPosition.previous_marker_name"></a>

#### previous_marker_name

```python
@previous_marker_name.setter
def previous_marker_name(value: Name) -> None
```

<a id="unreal.MarkerSyncAnimPosition.next_marker_name"></a>

#### next_marker_name

```python
@property
def next_marker_name() -> Name
```

(Name):  [Read-Write] The marker we are heading towards

<a id="unreal.MarkerSyncAnimPosition.next_marker_name"></a>

#### next_marker_name

```python
@next_marker_name.setter
def next_marker_name(value: Name) -> None
```

<a id="unreal.MarkerSyncAnimPosition.position_between_markers"></a>

#### position_between_markers

```python
@property
def position_between_markers() -> float
```

(float):  [Read-Write] Value between 0 and 1 representing where we are:
      0   we are at PreviousMarker
      1   we are at NextMarker
      0.5 we are half way between the two

<a id="unreal.MarkerSyncAnimPosition.position_between_markers"></a>

#### position_between_markers

```python
@position_between_markers.setter
def position_between_markers(value: float) -> None
```

<a id="unreal.AnimExecutionContext"></a>