## LiveLinkCustomTimeStep Objects

```python
class LiveLinkCustomTimeStep(GenlockedCustomTimeStep)
```

Control the Engine TimeStep via a live link source

Philosophy:

  * Quantized time steps based on live link expected data rate.
  * Made for Live Link sources can receive data asynchronously, and therefore trigger the waiting game thread.

  * FApp::GetDeltaTime
      - Forced to a multiple of the desired FrameTime.
      - This multiple will depend on Frame Id increment and user settings.

  * FApp::GetCurrentTime
      - Incremented in multiples of the desired FrameTime.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkCustomTimeStep.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_rate_divider`` (uint32):  [Read-Write] Allows genlock to period to be a multiple of the live link data period. For example a value of 2 will run at half the live link data rate
- ``live_link_data_rate`` (FrameRate):  [Read-Write] Expected Live Link data rate. If real rate differs, then delta times will contract/expand with respect to real time
- ``lock_step_mode`` (bool):  [Read-Write] Lockstep mode means that we only allow FrameRateDivider data frames of the selected subject per engine loop.
  The idea here is to process all packets and avoid Live Link evaluation to skip frames when the engine hitches,
  and the live link transport will serve as implicit FIFO buffer. However if the Engine cannot keep up with the data rate,
  a large delay will be introduced and the transport buffer will eventually start dropping data.
- ``subject_key`` (LiveLinkSubjectKey):  [Read-Write] The specific subject that we listen to.
- ``timeout_in_seconds`` (double):  [Read-Write] Determines how long it should wait for live link data before deciding that it is not in synchronized state anymore

<a id="unreal.LiveLinkTransformDeadbandPreProcessor"></a>