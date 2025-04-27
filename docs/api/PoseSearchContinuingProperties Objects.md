## PoseSearchContinuingProperties Objects

```python
class PoseSearchContinuingProperties(StructBase)
```

Pose Search Continuing Properties

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``playing_asset`` (Object):  [Read-Write] Currently playing animation
- ``playing_asset_accumulated_time`` (float):  [Read-Write] Currently playing animation accumulated time

<a id="unreal.PoseSearchContinuingProperties.__init__"></a>

#### __init__

```python
def __init__(playing_asset: Object = None,
             playing_asset_accumulated_time: float = 0.000000) -> None
```

<a id="unreal.PoseSearchContinuingProperties.playing_asset"></a>

#### playing_asset

```python
@property
def playing_asset() -> Object
```

(Object):  [Read-Write] Currently playing animation

<a id="unreal.PoseSearchContinuingProperties.playing_asset"></a>

#### playing_asset

```python
@playing_asset.setter
def playing_asset(value: Object) -> None
```

<a id="unreal.PoseSearchContinuingProperties.playing_asset_accumulated_time"></a>

#### playing_asset_accumulated_time

```python
@property
def playing_asset_accumulated_time() -> float
```

(float):  [Read-Write] Currently playing animation accumulated time

<a id="unreal.PoseSearchContinuingProperties.playing_asset_accumulated_time"></a>

#### playing_asset_accumulated_time

```python
@playing_asset_accumulated_time.setter
def playing_asset_accumulated_time(value: float) -> None
```

<a id="unreal.PoseSearchDatabaseSequenceEx"></a>