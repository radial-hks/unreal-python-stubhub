## GenlockedFixedRateCustomTimeStep Objects

```python
class GenlockedFixedRateCustomTimeStep(GenlockedCustomTimeStep)
```

Control the Engine TimeStep via a fixed frame rate.

Philosophy:

  * Quantized increments but keeping up with platform time.

  * FApp::GetDeltaTime
      - Forced to a multiple of the desired FrameTime.

  * FApp::GetCurrentTime
      - Incremented in multiples of the desired FrameTime.
      - Corresponds to platform time minus any fractional FrameTime.

**C++ Source:**

- **Module**: TimeManagement
- **File**: GenlockedFixedRateCustomTimeStep.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``force_single_frame_delta_time`` (bool):  [Read-Write] When true, delta time will always be 1/FrameRate, regardless of how much real time has elapsed
- ``frame_rate`` (FrameRate):  [Read-Write] Desired frame rate
- ``should_block`` (bool):  [Read-Write] Indicates that this custom time step should block to enforce the specified frame rate. Set to false if this is enforced elsewhere.

<a id="unreal.TimecodeProvider"></a>