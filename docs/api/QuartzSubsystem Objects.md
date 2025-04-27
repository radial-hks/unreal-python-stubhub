## QuartzSubsystem Objects

```python
class QuartzSubsystem(TickableWorldSubsystem)
```

Quartz Subsystem

**C++ Source:**

- **Module**: AudioMixer
- **File**: QuartzSubsystem.h

<a id="unreal.QuartzSubsystem.set_quartz_subsystem_tickable_when_paused"></a>

#### set_quartz_subsystem_tickable_when_paused

```python
def set_quartz_subsystem_tickable_when_paused(
        tickable_when_paused: bool) -> None
```

x.set_quartz_subsystem_tickable_when_paused(tickable_when_paused) -> None
Set Quartz Subsystem Tickable when Paused

Args:
    tickable_when_paused (bool):

<a id="unreal.QuartzSubsystem.is_quartz_enabled"></a>

#### is_quartz_enabled

```python
def is_quartz_enabled() -> bool
```

x.is_quartz_enabled() -> bool
Is Quartz Enabled

Returns:
    bool:

<a id="unreal.QuartzSubsystem.is_clock_running"></a>

#### is_clock_running

```python
def is_clock_running(world_context_object: Object, clock_name: Name) -> bool
```

x.is_clock_running(world_context_object, clock_name) -> bool
returns true if the clock is running

Args:
    world_context_object (Object): 
    clock_name (Name): 

Returns:
    bool:

<a id="unreal.QuartzSubsystem.get_round_trip_min_latency"></a>

#### get_round_trip_min_latency

```python
def get_round_trip_min_latency(world_context_object: Object) -> float
```

x.get_round_trip_min_latency(world_context_object) -> float
Get Round Trip Min Latency

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_round_trip_max_latency"></a>

#### get_round_trip_max_latency

```python
def get_round_trip_max_latency(world_context_object: Object) -> float
```

x.get_round_trip_max_latency(world_context_object) -> float
Get Round Trip Max Latency

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_round_trip_average_latency"></a>

#### get_round_trip_average_latency

```python
def get_round_trip_average_latency(world_context_object: Object) -> float
```

x.get_round_trip_average_latency(world_context_object) -> float
latency data (Round trip)

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_handle_for_clock"></a>

#### get_handle_for_clock

```python
def get_handle_for_clock(world_context_object: Object,
                         clock_name: Name) -> QuartzClockHandle
```

x.get_handle_for_clock(world_context_object, clock_name) -> QuartzClockHandle
get handle for existing clock

Args:
    world_context_object (Object): 
    clock_name (Name): 

Returns:
    QuartzClockHandle:

<a id="unreal.QuartzSubsystem.get_game_thread_to_audio_render_thread_min_latency"></a>

#### get_game_thread_to_audio_render_thread_min_latency

```python
def get_game_thread_to_audio_render_thread_min_latency(
        world_context_object: Object) -> float
```

x.get_game_thread_to_audio_render_thread_min_latency(world_context_object) -> float
Get Game Thread to Audio Render Thread Min Latency

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_game_thread_to_audio_render_thread_max_latency"></a>

#### get_game_thread_to_audio_render_thread_max_latency

```python
def get_game_thread_to_audio_render_thread_max_latency(
        world_context_object: Object) -> float
```

x.get_game_thread_to_audio_render_thread_max_latency(world_context_object) -> float
Get Game Thread to Audio Render Thread Max Latency

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_game_thread_to_audio_render_thread_average_latency"></a>

#### get_game_thread_to_audio_render_thread_average_latency

```python
def get_game_thread_to_audio_render_thread_average_latency(
        world_context_object: Object) -> float
```

x.get_game_thread_to_audio_render_thread_average_latency(world_context_object) -> float
latency data (Game thread -> Audio Render Thread)

Args:
    world_context_object (Object): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_estimated_clock_run_time"></a>

#### get_estimated_clock_run_time

```python
def get_estimated_clock_run_time(world_context_object: Object,
                                 clock_name: Name) -> float
```

x.get_estimated_clock_run_time(world_context_object, clock_name) -> float
Returns the amount of time, in seconds, the clock has been running. Caution: due to latency, this will not be perfectly accurate

Args:
    world_context_object (Object): 
    clock_name (Name): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_duration_of_quantization_type_in_seconds"></a>

#### get_duration_of_quantization_type_in_seconds

```python
def get_duration_of_quantization_type_in_seconds(
        world_context_object: Object,
        clock_name: Name,
        quantization_type: QuartzCommandQuantization,
        multiplier: float = 1.000000) -> float
```

x.get_duration_of_quantization_type_in_seconds(world_context_object, clock_name, quantization_type, multiplier=1.000000) -> float
Returns the duration in seconds of the given Quantization Type

Args:
    world_context_object (Object): 
    clock_name (Name): 
    quantization_type (QuartzCommandQuantization): 
    multiplier (float): 

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_current_clock_timestamp"></a>

#### get_current_clock_timestamp

```python
def get_current_clock_timestamp(world_context_object: Object,
                                clock_name: Name) -> QuartzTransportTimeStamp
```

x.get_current_clock_timestamp(world_context_object, clock_name) -> QuartzTransportTimeStamp
Retrieves a timestamp for the clock

Args:
    world_context_object (Object): 
    clock_name (Name): 

Returns:
    QuartzTransportTimeStamp:

<a id="unreal.QuartzSubsystem.get_audio_render_thread_to_game_thread_min_latency"></a>

#### get_audio_render_thread_to_game_thread_min_latency

```python
def get_audio_render_thread_to_game_thread_min_latency() -> float
```

x.get_audio_render_thread_to_game_thread_min_latency() -> float
Get Audio Render Thread to Game Thread Min Latency

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_audio_render_thread_to_game_thread_max_latency"></a>

#### get_audio_render_thread_to_game_thread_max_latency

```python
def get_audio_render_thread_to_game_thread_max_latency() -> float
```

x.get_audio_render_thread_to_game_thread_max_latency() -> float
Get Audio Render Thread to Game Thread Max Latency

Returns:
    float:

<a id="unreal.QuartzSubsystem.get_audio_render_thread_to_game_thread_average_latency"></a>

#### get_audio_render_thread_to_game_thread_average_latency

```python
def get_audio_render_thread_to_game_thread_average_latency() -> float
```

x.get_audio_render_thread_to_game_thread_average_latency() -> float
latency data (Audio Render Thread -> Game thread)

Returns:
    float:

<a id="unreal.QuartzSubsystem.does_clock_exist"></a>

#### does_clock_exist

```python
def does_clock_exist(world_context_object: Object, clock_name: Name) -> bool
```

x.does_clock_exist(world_context_object, clock_name) -> bool
returns true if the clock exists

Args:
    world_context_object (Object): 
    clock_name (Name): 

Returns:
    bool:

<a id="unreal.QuartzSubsystem.delete_clock_by_name"></a>

#### delete_clock_by_name

```python
def delete_clock_by_name(world_context_object: Object,
                         clock_name: Name) -> None
```

x.delete_clock_by_name(world_context_object, clock_name) -> None
delete an existing clock given its name

Args:
    world_context_object (Object): 
    clock_name (Name):

<a id="unreal.QuartzSubsystem.delete_clock_by_handle"></a>

#### delete_clock_by_handle

```python
def delete_clock_by_handle(
        world_context_object: Object,
        clock_handle: QuartzClockHandle) -> QuartzClockHandle
```

x.delete_clock_by_handle(world_context_object, clock_handle) -> QuartzClockHandle
delete an existing clock given its clock handle

Args:
    world_context_object (Object): 
    clock_handle (QuartzClockHandle): 

Returns:
    QuartzClockHandle: 

    clock_handle (QuartzClockHandle):

<a id="unreal.QuartzSubsystem.create_new_clock"></a>

#### create_new_clock

```python
def create_new_clock(
        world_context_object: Object,
        clock_name: Name,
        settings: QuartzClockSettings,
        override_settings_if_clock_exists: bool = False,
        use_audio_engine_clock_manager: bool = True) -> QuartzClockHandle
```

x.create_new_clock(world_context_object, clock_name, settings, override_settings_if_clock_exists=False, use_audio_engine_clock_manager=True) -> QuartzClockHandle
Clock Creation
create a new clock (or return handle if clock already exists)

Args:
    world_context_object (Object): 
    clock_name (Name): 
    settings (QuartzClockSettings): 
    override_settings_if_clock_exists (bool): 
    use_audio_engine_clock_manager (bool): 

Returns:
    QuartzClockHandle:

<a id="unreal.StreamableRenderAsset"></a>