## LevelSequencePlayerSnapshot Objects

```python
class LevelSequencePlayerSnapshot(StructBase)
```

Frame snapshot information for a level sequence

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequencePlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_shot`` (LevelSequence):  [Read-Only]
- ``camera_component`` (CameraComponent):  [Read-Only]
- ``current_shot_local_time`` (QualifiedTime):  [Read-Only]
- ``current_shot_name`` (str):  [Read-Only]
- ``current_shot_source_time`` (QualifiedTime):  [Read-Only]
- ``root_name`` (str):  [Read-Only]
- ``root_time`` (QualifiedTime):  [Read-Only]
- ``source_time`` (QualifiedTime):  [Read-Only]
- ``source_timecode`` (str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.__init__"></a>

#### __init__

```python
def __init__(root_name: str = "",
             root_time: QualifiedTime = [[0], [24, 1], 0.000000],
             source_time: QualifiedTime = [[0], [24, 1], 0.000000],
             current_shot_name: str = "",
             current_shot_local_time: QualifiedTime = [[0], [24, 1], 0.000000],
             current_shot_source_time: QualifiedTime = [[0], [24, 1],
                                                        0.000000],
             source_timecode: str = "",
             camera_component: CameraComponent = None,
             active_shot: LevelSequence = None) -> None
```

<a id="unreal.LevelSequencePlayerSnapshot.root_name"></a>

#### root_name

```python
@property
def root_name() -> str
```

(str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.root_time"></a>

#### root_time

```python
@property
def root_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.source_time"></a>

#### source_time

```python
@property
def source_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.current_shot_name"></a>

#### current_shot_name

```python
@property
def current_shot_name() -> str
```

(str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.current_shot_local_time"></a>

#### current_shot_local_time

```python
@property
def current_shot_local_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.current_shot_source_time"></a>

#### current_shot_source_time

```python
@property
def current_shot_source_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.source_timecode"></a>

#### source_timecode

```python
@property
def source_timecode() -> str
```

(str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.camera_component"></a>

#### camera_component

```python
@property
def camera_component() -> CameraComponent
```

(CameraComponent):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.active_shot"></a>

#### active_shot

```python
@property
def active_shot() -> LevelSequence
```

(LevelSequence):  [Read-Only]

<a id="unreal.CSVImportSettings"></a>