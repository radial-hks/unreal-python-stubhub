## TakeRecorderLiveLinkSource Objects

```python
class TakeRecorderLiveLinkSource(TakeRecorderSource)
```

A recording source that records LiveLink

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLinkSequencer
- **File**: TakeRecorderLiveLinkSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``discard_samples_before_start`` (bool):  [Read-Write] If true discard livelink samples with timecode that occurs before the start of recording
- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``reduce_keys`` (bool):  [Read-Write] Whether to perform key-reduction algorithms as part of the recording
- ``save_subject_settings`` (bool):  [Read-Write] Whether we should save subject settings in the the live link section. If not, we'll create one with subject information with no settings
- ``subject_name`` (Name):  [Read-Write] Name of the subject to record
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]
- ``use_source_timecode`` (bool):  [Read-Write] Whether the livelink subject's timecode or the system time should be used for the recording.
  note: If set, the livelink subject's timecode will be used even if it does not match the engine timecode.

<a id="unreal.TakeRecorderLiveLinkSource.reduce_keys"></a>

#### reduce_keys

```python
@property
def reduce_keys() -> bool
```

(bool):  [Read-Write] Whether to perform key-reduction algorithms as part of the recording

<a id="unreal.TakeRecorderLiveLinkSource.reduce_keys"></a>

#### reduce_keys

```python
@reduce_keys.setter
def reduce_keys(value: bool) -> None
```

<a id="unreal.TakeRecorderLiveLinkSource.subject_name"></a>

#### subject_name

```python
@property
def subject_name() -> Name
```

(Name):  [Read-Write] Name of the subject to record

<a id="unreal.TakeRecorderLiveLinkSource.subject_name"></a>

#### subject_name

```python
@subject_name.setter
def subject_name(value: Name) -> None
```

<a id="unreal.TakeRecorderLiveLinkSource.save_subject_settings"></a>

#### save_subject_settings

```python
@property
def save_subject_settings() -> bool
```

(bool):  [Read-Write] Whether we should save subject settings in the the live link section. If not, we'll create one with subject information with no settings

<a id="unreal.TakeRecorderLiveLinkSource.save_subject_settings"></a>

#### save_subject_settings

```python
@save_subject_settings.setter
def save_subject_settings(value: bool) -> None
```

<a id="unreal.TakeRecorderLiveLinkSource.use_source_timecode"></a>

#### use_source_timecode

```python
@property
def use_source_timecode() -> bool
```

(bool):  [Read-Write] Whether the livelink subject's timecode or the system time should be used for the recording.
note: If set, the livelink subject's timecode will be used even if it does not match the engine timecode.

<a id="unreal.TakeRecorderLiveLinkSource.use_source_timecode"></a>

#### use_source_timecode

```python
@use_source_timecode.setter
def use_source_timecode(value: bool) -> None
```

<a id="unreal.TakeRecorderLiveLinkSource.discard_samples_before_start"></a>

#### discard_samples_before_start

```python
@property
def discard_samples_before_start() -> bool
```

(bool):  [Read-Write] If true discard livelink samples with timecode that occurs before the start of recording

<a id="unreal.TakeRecorderLiveLinkSource.discard_samples_before_start"></a>

#### discard_samples_before_start

```python
@discard_samples_before_start.setter
def discard_samples_before_start(value: bool) -> None
```

<a id="unreal.AnimNotifyState_MotionWarping"></a>