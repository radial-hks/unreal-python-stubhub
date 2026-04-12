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

#### \_\_init\_\_

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

#### root\_name

```python
@property
def root_name() -> str
```

(str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.root_time"></a>

#### root\_time

```python
@property
def root_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.source_time"></a>

#### source\_time

```python
@property
def source_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.current_shot_name"></a>

#### current\_shot\_name

```python
@property
def current_shot_name() -> str
```

(str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.current_shot_local_time"></a>

#### current\_shot\_local\_time

```python
@property
def current_shot_local_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.current_shot_source_time"></a>

#### current\_shot\_source\_time

```python
@property
def current_shot_source_time() -> QualifiedTime
```

(QualifiedTime):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.source_timecode"></a>

#### source\_timecode

```python
@property
def source_timecode() -> str
```

(str):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.camera_component"></a>

#### camera\_component

```python
@property
def camera_component() -> CameraComponent
```

(CameraComponent):  [Read-Only]

<a id="unreal.LevelSequencePlayerSnapshot.active_shot"></a>

#### active\_shot

```python
@property
def active_shot() -> LevelSequence
```

(LevelSequence):  [Read-Only]

<a id="unreal.CSVImportSettings"></a>