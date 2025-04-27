## LiveLinkSourceBufferManagementSettings Objects

```python
class LiveLinkSourceBufferManagementSettings(StructBase)
```

Live Link Source Buffer Management Settings

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkSourceSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``detected_frame_rate`` (FrameRate):  [Read-Only] FrameRate taken from one of the subjects. It's expected that all subjects have the same FrameRate
- ``engine_time_clock_offset`` (double):  [Read-Only] Continuously updated clock offset estimator between source clock and engine clock (in seconds)
- ``engine_time_offset`` (float):  [Read-Write] When evaluating with time: how far back from current time should we read the buffer (in seconds)
- ``generate_sub_frame`` (bool):  [Read-Write]
- ``keep_at_least_one_frame`` (bool):  [Read-Write] When cleaning the buffer keep at least one frame, even if the frame doesn't matches the other options.
- ``latest_offset`` (int32):  [Read-Write] When evaluating with latest: how far back from latest frame should we read the buffer
- ``max_number_of_frame_to_buffered`` (int32):  [Read-Write] Maximum number of frames to keep in memory.
- ``smooth_engine_time_offset`` (double):  [Read-Only] Continuously updated offset to achieve a smooth evaluation time (in seconds)
- ``source_timecode_frame_rate`` (FrameRate):  [Read-Write] What is the source frame rate.
  When the refresh rate of the source is bigger than the timecode frame rate, LiveLink will try to generate sub frame numbers.
  note: The source should generate the sub frame numbers. Use this setting when the source is not able to do so.
  note: The generated sub frame numbers will not be saved by Sequencer.
- ``timecode_clock_offset`` (double):  [Read-Only] Continuously updated clock offset estimator between source timecode clock and engine timecode provider clock (in seconds)
- ``timecode_frame_offset`` (float):  [Read-Write] When evaluating with timecode: how far back from current timecode should we read the buffer (in TimecodeFrameRate).
- ``use_timecode_smooth_latest`` (bool):  [Read-Write] When evaluating with timecode, align source timecode using a continuous clock offset to do a smooth latest
  This means that even if engine Timecode and source Timecode are not aligned, the offset between both clocks
  will be tracked to keep them aligned. With an additionnal offset, 1.5 is a good number, you can evaluate
  your subject using the latest frame by keeping just enough margin to have a smooth playback and avoid starving.
- ``valid_engine_time`` (float):  [Read-Write] If the frame is older than ValidTime, remove it from the buffer list (in seconds).
- ``valid_engine_time_enabled`` (bool):  [Read-Write] Enabled the ValidEngineTime setting.
- ``valid_timecode_frame`` (int32):  [Read-Write] If the frame timecode is older than ValidTimecodeFrame, remove it from the buffer list (in TimecodeFrameRate).
- ``valid_timecode_frame_enabled`` (bool):  [Read-Write] If the frame timecode is older than ValidTimecodeFrame, remove it from the buffer list (in TimecodeFrameRate).

<a id="unreal.LiveLinkSourceBufferManagementSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMBlueprintPinId"></a>