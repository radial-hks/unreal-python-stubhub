## TimecodeBoneMethod Objects

```python
class TimecodeBoneMethod(StructBase)
```

Timecode Bone Method

**C++ Source:**

- **Module**: SequenceRecorder
- **File**: AnimationRecorder.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_mode`` (TimecodeBoneMode):  [Read-Write] The timecode bone mode
- ``bone_name`` (Name):  [Read-Write] Name of the bone to assign timecode values to

<a id="unreal.TimecodeBoneMethod.__init__"></a>

#### \_\_init\_\_

```python
def __init__(bone_mode: TimecodeBoneMode = TimecodeBoneMode.ALL,
             bone_name: Name = "None") -> None
```

<a id="unreal.TimecodeBoneMethod.bone_mode"></a>

#### bone\_mode

```python
@property
def bone_mode() -> TimecodeBoneMode
```

(TimecodeBoneMode):  [Read-Write] The timecode bone mode

<a id="unreal.TimecodeBoneMethod.bone_mode"></a>

#### bone\_mode

```python
@bone_mode.setter
def bone_mode(value: TimecodeBoneMode) -> None
```

<a id="unreal.TimecodeBoneMethod.bone_name"></a>

#### bone\_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Write] Name of the bone to assign timecode values to

<a id="unreal.TimecodeBoneMethod.bone_name"></a>

#### bone\_name

```python
@bone_name.setter
def bone_name(value: Name) -> None
```

<a id="unreal.CurveEditorBakeFilterRange"></a>