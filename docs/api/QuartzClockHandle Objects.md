## QuartzClockHandle Objects

```python
class QuartzClockHandle(Object)
```

This class is a BP / Game thread wrapper around FQuartzClockProxy
   (to talk to the underlying clock)

...and inherits from FQuartzTickableObject
   (to listen to the underlying clock)

It can subscribe to Quantized Event & Metronome delegates to synchronize
gameplay & VFX to Quartz events fired from the Audio Engine

**C++ Source:**

- **Module**: AudioMixer
- **File**: AudioMixerClockHandle.h

<a id="unreal.QuartzClockHandle.unsubscribe_from_time_division"></a>

#### unsubscribe_from_time_division

```python
def unsubscribe_from_time_division(
        world_context_object: Object,
        quantization_boundary: QuartzCommandQuantization) -> QuartzClockHandle
```

x.unsubscribe_from_time_division(world_context_object, quantization_boundary) -> QuartzClockHandle
Unsubscribe from Time Division

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzCommandQuantization): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.unsubscribe_from_all_time_divisions"></a>

#### unsubscribe_from_all_time_divisions

```python
def unsubscribe_from_all_time_divisions(
        world_context_object: Object) -> QuartzClockHandle
```

x.unsubscribe_from_all_time_divisions(world_context_object) -> QuartzClockHandle
Unsubscribe from All Time Divisions

Args:
    world_context_object (Object): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.subscribe_to_quantization_event"></a>

#### subscribe_to_quantization_event

```python
def subscribe_to_quantization_event(
        world_context_object: Object,
        quantization_boundary: QuartzCommandQuantization,
        on_quantization_event: OnQuartzMetronomeEventBP) -> QuartzClockHandle
```

x.subscribe_to_quantization_event(world_context_object, quantization_boundary, on_quantization_event) -> QuartzClockHandle
Metronome subscription

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzCommandQuantization): 
    on_quantization_event (OnQuartzMetronomeEventBP): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.subscribe_to_all_quantization_events"></a>

#### subscribe_to_all_quantization_events

```python
def subscribe_to_all_quantization_events(
        world_context_object: Object,
        on_quantization_event: OnQuartzMetronomeEventBP) -> QuartzClockHandle
```

x.subscribe_to_all_quantization_events(world_context_object, on_quantization_event) -> QuartzClockHandle
Subscribe to All Quantization Events

Args:
    world_context_object (Object): 
    on_quantization_event (OnQuartzMetronomeEventBP): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.stop_clock"></a>

#### stop_clock

```python
def stop_clock(world_context_object: Object,
               cancel_pending_events: bool) -> QuartzClockHandle
```

x.stop_clock(world_context_object, cancel_pending_events) -> QuartzClockHandle
Stop Clock

Args:
    world_context_object (Object): 
    cancel_pending_events (bool): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.start_other_clock"></a>

#### start_other_clock

```python
def start_other_clock(world_context_object: Object, other_clock_name: Name,
                      quantization_boundary: QuartzQuantizationBoundary,
                      delegate: OnQuartzCommandEventBP) -> None
```

x.start_other_clock(world_context_object, other_clock_name, quantization_boundary, delegate) -> None
"other" clock manipulation

Args:
    world_context_object (Object): 
    other_clock_name (Name): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP):

<a id="unreal.QuartzClockHandle.start_clock"></a>

#### start_clock

```python
def start_clock(world_context_object: Object) -> QuartzClockHandle
```

x.start_clock(world_context_object) -> QuartzClockHandle
Clock manipulation

Args:
    world_context_object (Object): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.set_ticks_per_second"></a>

#### set_ticks_per_second

```python
def set_ticks_per_second(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP,
        ticks_per_second: float = 10.000000) -> QuartzClockHandle
```

x.set_ticks_per_second(world_context_object, quantization_boundary, delegate, ticks_per_second=10.000000) -> QuartzClockHandle
Set Ticks Per Second

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 
    ticks_per_second (float): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.set_thirty_second_notes_per_minute"></a>

#### set_thirty_second_notes_per_minute

```python
def set_thirty_second_notes_per_minute(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP,
        thirty_seconds_notes_per_minute: float = 960.000000
) -> QuartzClockHandle
```

x.set_thirty_second_notes_per_minute(world_context_object, quantization_boundary, delegate, thirty_seconds_notes_per_minute=960.000000) -> QuartzClockHandle
Set Thirty Second Notes Per Minute

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 
    thirty_seconds_notes_per_minute (float): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.set_seconds_per_tick"></a>

#### set_seconds_per_tick

```python
def set_seconds_per_tick(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP,
        seconds_per_tick: float = 0.250000) -> QuartzClockHandle
```

x.set_seconds_per_tick(world_context_object, quantization_boundary, delegate, seconds_per_tick=0.250000) -> QuartzClockHandle
Set Seconds Per Tick

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 
    seconds_per_tick (float): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.set_milliseconds_per_tick"></a>

#### set_milliseconds_per_tick

```python
def set_milliseconds_per_tick(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP,
        milliseconds_per_tick: float = 100.000000) -> QuartzClockHandle
```

x.set_milliseconds_per_tick(world_context_object, quantization_boundary, delegate, milliseconds_per_tick=100.000000) -> QuartzClockHandle
Metronome Alteration (setters)

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 
    milliseconds_per_tick (float): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.set_beats_per_minute"></a>

#### set_beats_per_minute

```python
def set_beats_per_minute(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP,
        beats_per_minute: float = 60.000000) -> QuartzClockHandle
```

x.set_beats_per_minute(world_context_object, quantization_boundary, delegate, beats_per_minute=60.000000) -> QuartzClockHandle
Set Beats Per Minute

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 
    beats_per_minute (float): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.resume_clock"></a>

#### resume_clock

```python
def resume_clock(world_context_object: Object) -> QuartzClockHandle
```

x.resume_clock(world_context_object) -> QuartzClockHandle
Resume Clock

Args:
    world_context_object (Object): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.reset_transport_quantized"></a>

#### reset_transport_quantized

```python
def reset_transport_quantized(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP) -> QuartzClockHandle
```

x.reset_transport_quantized(world_context_object, quantization_boundary, delegate) -> QuartzClockHandle
Reset Transport Quantized

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.reset_transport"></a>

#### reset_transport

```python
def reset_transport(world_context_object: Object,
                    delegate: OnQuartzCommandEventBP) -> None
```

x.reset_transport(world_context_object, delegate) -> None
Reset Transport

Args:
    world_context_object (Object): 
    delegate (OnQuartzCommandEventBP):

<a id="unreal.QuartzClockHandle.pause_clock"></a>

#### pause_clock

```python
def pause_clock(world_context_object: Object) -> QuartzClockHandle
```

x.pause_clock(world_context_object) -> QuartzClockHandle
Pause Clock

Args:
    world_context_object (Object): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzClockHandle.notify_on_quantization_boundary"></a>

#### notify_on_quantization_boundary

```python
def notify_on_quantization_boundary(
        world_context_object: Object,
        quantization_boundary: QuartzQuantizationBoundary,
        delegate: OnQuartzCommandEventBP,
        ms_offset: float = 0.000000) -> None
```

x.notify_on_quantization_boundary(world_context_object, quantization_boundary, delegate, ms_offset=0.000000) -> None
Notify on Quantization Boundary

Args:
    world_context_object (Object): 
    quantization_boundary (QuartzQuantizationBoundary): 
    delegate (OnQuartzCommandEventBP): 
    ms_offset (float):

<a id="unreal.QuartzClockHandle.is_clock_running"></a>

#### is_clock_running

```python
def is_clock_running(world_context_object: Object) -> bool
```

x.is_clock_running(world_context_object) -> bool
Is Clock Running

Args:
    world_context_object (Object): 

Returns:
    bool:

<a id="unreal.QuartzClockHandle.get_ticks_per_second"></a>

#### get_ticks_per_second

```python
def get_ticks_per_second(world_context_object: Object) -> float
```

x.get_ticks_per_second(world_context_object) -> float
Get Ticks Per Second

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzClockHandle.get_thirty_second_notes_per_minute"></a>

#### get_thirty_second_notes_per_minute

```python
def get_thirty_second_notes_per_minute(world_context_object: Object) -> float
```

x.get_thirty_second_notes_per_minute(world_context_object) -> float
Get Thirty Second Notes Per Minute

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzClockHandle.get_seconds_per_tick"></a>

#### get_seconds_per_tick

```python
def get_seconds_per_tick(world_context_object: Object) -> float
```

x.get_seconds_per_tick(world_context_object) -> float
Get Seconds Per Tick

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzClockHandle.get_milliseconds_per_tick"></a>

#### get_milliseconds_per_tick

```python
def get_milliseconds_per_tick(world_context_object: Object) -> float
```

x.get_milliseconds_per_tick(world_context_object) -> float
Metronome getters

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzClockHandle.get_estimated_run_time"></a>

#### get_estimated_run_time

```python
def get_estimated_run_time(world_context_object: Object) -> float
```

x.get_estimated_run_time(world_context_object) -> float
Returns the amount of time, in seconds, the clock has been running. Caution: due to latency, this will not be perfectly accurate

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzClockHandle.get_duration_of_quantization_type_in_seconds"></a>

#### get_duration_of_quantization_type_in_seconds

```python
def get_duration_of_quantization_type_in_seconds(
        world_context_object: Object,
        quantization_type: QuartzCommandQuantization,
        multiplier: float = 1.000000) -> float
```

x.get_duration_of_quantization_type_in_seconds(world_context_object, quantization_type, multiplier=1.000000) -> float
Returns the duration in seconds of the given Quantization Type

Args:
    world_context_object (Object): 
    quantization_type (QuartzCommandQuantization): 
    multiplier (float): 

Returns:
    float: The duration, in seconds, of a multiplier amount of the Quantization Type, or -1 in the case the clock is invalid

<a id="unreal.QuartzClockHandle.get_current_timestamp"></a>

#### get_current_timestamp

```python
def get_current_timestamp(
        world_context_object: Object) -> QuartzTransportTimeStamp
```

x.get_current_timestamp(world_context_object) -> QuartzTransportTimeStamp
Retrieves a timestamp for the clock

Args:
    world_context_object (Object): 

Returns:
    QuartzTransportTimeStamp:

<a id="unreal.QuartzClockHandle.get_beats_per_minute"></a>

#### get_beats_per_minute

```python
def get_beats_per_minute(world_context_object: Object) -> float
```

x.get_beats_per_minute(world_context_object) -> float
Get Beats Per Minute

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzClockHandle.get_beat_progress_percent"></a>

#### get_beat_progress_percent

```python
def get_beat_progress_percent(
        quantization_boundary:
    QuartzCommandQuantization = QuartzCommandQuantization.BEAT,
        phase_offset: float = 0.000000,
        ms_offset: float = 0.000000) -> float
```

x.get_beat_progress_percent(quantization_boundary=QuartzCommandQuantization.BEAT, phase_offset=0.000000, ms_offset=0.000000) -> float
Returns the current progress until the next occurrence of the provided musical duration as a float value from 0 (previous beat) to 1 (next beat).
This is useful for indexing into curves to animate parameters to musical time.
Ms and Phase offsets are combined internally.

Args:
    quantization_boundary (QuartzCommandQuantization): 
    phase_offset (float): 
    ms_offset (float): 

Returns:
    float:

<a id="unreal.WorldSubsystem"></a>