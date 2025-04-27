## AutomatedLevelSequenceCapture Objects

```python
class AutomatedLevelSequenceCapture(MovieSceneCapture)
```

Automated Level Sequence Capture

**C++ Source:**

- **Module**: MovieSceneTools
- **File**: AutomatedLevelSequenceCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_command_line_arguments`` (str):  [Read-Write] Additional command line arguments to pass to the external process when capturing
- ``audio_capture_protocol`` (MovieSceneAudioCaptureProtocolBase):  [Read-Only]
- ``audio_capture_protocol_type`` (SoftClassPath):  [Read-Write] The type of capture protocol to use for audio data.
- ``burn_in_options`` (LevelSequenceBurnInOptions):  [Read-Write]
- ``close_editor_when_capture_starts`` (bool):  [Read-Write] When enabled, the editor will shutdown when the capture starts
- ``custom_end_frame`` (FrameNumber):  [Read-Write] Frame number to end capturing.
- ``custom_start_frame`` (FrameNumber):  [Read-Write] Frame number to start capturing.
- ``delay_before_shot_warm_up`` (float):  [Read-Write] The number of seconds to wait (in real-time) at shot boundaries.  Useful for allowing post processing effects to settle down before capturing the animation.
- ``delay_before_warm_up`` (float):  [Read-Write] The number of seconds to wait (in real-time) before we start playing back the warm up frames.  Useful for allowing post processing effects to settle down before capturing the animation.
- ``delay_every_frame`` (float):  [Read-Write] The number of seconds to wait (in real-time) at every frame.  Useful for allowing post processing effects to settle down before capturing the animation.
- ``image_capture_protocol`` (MovieSceneImageCaptureProtocolBase):  [Read-Only] Capture protocol responsible for actually capturing frame data
- ``image_capture_protocol_type`` (SoftClassPath):  [Read-Write] The type of capture protocol to use for image data
- ``inherited_command_line_arguments`` (str):  [Read-Write] Command line arguments inherited from this process
- ``level_sequence_asset`` (SoftObjectPath):  [Read-Write] A level sequence asset to playback at runtime - used where the level sequence does not already exist in the world.
- ``settings`` (MovieSceneCaptureSettings):  [Read-Write] Settings that define how to capture
- ``shot_name`` (str):  [Read-Write] Optional shot name to render. The frame range to render will be set to the shot frame range.
- ``use_custom_end_frame`` (bool):  [Read-Write] When enabled, the EndFrame setting will override the default ending frame number
- ``use_custom_start_frame`` (bool):  [Read-Write] When enabled, the StartFrame setting will override the default starting frame number
- ``use_separate_process`` (bool):  [Read-Write] Whether to capture the movie in a separate process or not
- ``warm_up_frame_count`` (int32):  [Read-Write] The number of extra frames to play before the sequence's start frame, to "warm up" the animation.  This is useful if your
            animation contains particles or other runtime effects that are spawned into the scene earlier than your capture start frame
- ``write_edit_decision_list`` (bool):  [Read-Write] Whether to write edit decision lists (EDLs) if the sequence contains shots
- ``write_final_cut_pro_xml`` (bool):  [Read-Write] Whether to write Final Cut Pro XML files (XMLs) if the sequence contains shots

<a id="unreal.AutomatedLevelSequenceCapture.level_sequence_asset"></a>

#### level_sequence_asset

```python
@property
def level_sequence_asset() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] A level sequence asset to playback at runtime - used where the level sequence does not already exist in the world.

<a id="unreal.AutomatedLevelSequenceCapture.level_sequence_asset"></a>

#### level_sequence_asset

```python
@level_sequence_asset.setter
def level_sequence_asset(value: SoftObjectPath) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.shot_name"></a>

#### shot_name

```python
@property
def shot_name() -> str
```

(str):  [Read-Write] Optional shot name to render. The frame range to render will be set to the shot frame range.

<a id="unreal.AutomatedLevelSequenceCapture.shot_name"></a>

#### shot_name

```python
@shot_name.setter
def shot_name(value: str) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.use_custom_start_frame"></a>

#### use_custom_start_frame

```python
@property
def use_custom_start_frame() -> bool
```

(bool):  [Read-Write] When enabled, the StartFrame setting will override the default starting frame number

<a id="unreal.AutomatedLevelSequenceCapture.use_custom_start_frame"></a>

#### use_custom_start_frame

```python
@use_custom_start_frame.setter
def use_custom_start_frame(value: bool) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.custom_start_frame"></a>

#### custom_start_frame

```python
@property
def custom_start_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] Frame number to start capturing.

<a id="unreal.AutomatedLevelSequenceCapture.custom_start_frame"></a>

#### custom_start_frame

```python
@custom_start_frame.setter
def custom_start_frame(value: FrameNumber) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.use_custom_end_frame"></a>

#### use_custom_end_frame

```python
@property
def use_custom_end_frame() -> bool
```

(bool):  [Read-Write] When enabled, the EndFrame setting will override the default ending frame number

<a id="unreal.AutomatedLevelSequenceCapture.use_custom_end_frame"></a>

#### use_custom_end_frame

```python
@use_custom_end_frame.setter
def use_custom_end_frame(value: bool) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.custom_end_frame"></a>

#### custom_end_frame

```python
@property
def custom_end_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] Frame number to end capturing.

<a id="unreal.AutomatedLevelSequenceCapture.custom_end_frame"></a>

#### custom_end_frame

```python
@custom_end_frame.setter
def custom_end_frame(value: FrameNumber) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.warm_up_frame_count"></a>

#### warm_up_frame_count

```python
@property
def warm_up_frame_count() -> int
```

(int32):  [Read-Write] The number of extra frames to play before the sequence's start frame, to "warm up" the animation.  This is useful if your
          animation contains particles or other runtime effects that are spawned into the scene earlier than your capture start frame

<a id="unreal.AutomatedLevelSequenceCapture.warm_up_frame_count"></a>

#### warm_up_frame_count

```python
@warm_up_frame_count.setter
def warm_up_frame_count(value: int) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.delay_before_warm_up"></a>

#### delay_before_warm_up

```python
@property
def delay_before_warm_up() -> float
```

(float):  [Read-Write] The number of seconds to wait (in real-time) before we start playing back the warm up frames.  Useful for allowing post processing effects to settle down before capturing the animation.

<a id="unreal.AutomatedLevelSequenceCapture.delay_before_warm_up"></a>

#### delay_before_warm_up

```python
@delay_before_warm_up.setter
def delay_before_warm_up(value: float) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.delay_before_shot_warm_up"></a>

#### delay_before_shot_warm_up

```python
@property
def delay_before_shot_warm_up() -> float
```

(float):  [Read-Write] The number of seconds to wait (in real-time) at shot boundaries.  Useful for allowing post processing effects to settle down before capturing the animation.

<a id="unreal.AutomatedLevelSequenceCapture.delay_before_shot_warm_up"></a>

#### delay_before_shot_warm_up

```python
@delay_before_shot_warm_up.setter
def delay_before_shot_warm_up(value: float) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.delay_every_frame"></a>

#### delay_every_frame

```python
@property
def delay_every_frame() -> float
```

(float):  [Read-Write] The number of seconds to wait (in real-time) at every frame.  Useful for allowing post processing effects to settle down before capturing the animation.

<a id="unreal.AutomatedLevelSequenceCapture.delay_every_frame"></a>

#### delay_every_frame

```python
@delay_every_frame.setter
def delay_every_frame(value: float) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.burn_in_options"></a>

#### burn_in_options

```python
@property
def burn_in_options() -> LevelSequenceBurnInOptions
```

(LevelSequenceBurnInOptions):  [Read-Write]

<a id="unreal.AutomatedLevelSequenceCapture.burn_in_options"></a>

#### burn_in_options

```python
@burn_in_options.setter
def burn_in_options(value: LevelSequenceBurnInOptions) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.write_edit_decision_list"></a>

#### write_edit_decision_list

```python
@property
def write_edit_decision_list() -> bool
```

(bool):  [Read-Write] Whether to write edit decision lists (EDLs) if the sequence contains shots

<a id="unreal.AutomatedLevelSequenceCapture.write_edit_decision_list"></a>

#### write_edit_decision_list

```python
@write_edit_decision_list.setter
def write_edit_decision_list(value: bool) -> None
```

<a id="unreal.AutomatedLevelSequenceCapture.write_final_cut_pro_xml"></a>

#### write_final_cut_pro_xml

```python
@property
def write_final_cut_pro_xml() -> bool
```

(bool):  [Read-Write] Whether to write Final Cut Pro XML files (XMLs) if the sequence contains shots

<a id="unreal.AutomatedLevelSequenceCapture.write_final_cut_pro_xml"></a>

#### write_final_cut_pro_xml

```python
@write_final_cut_pro_xml.setter
def write_final_cut_pro_xml(value: bool) -> None
```

<a id="unreal.MovieSceneUserImportFBXSettings"></a>