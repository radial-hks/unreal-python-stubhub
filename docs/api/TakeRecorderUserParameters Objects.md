## TakeRecorderUserParameters Objects

```python
class TakeRecorderUserParameters(StructBase)
```

Take Recorder User Parameters

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_lock`` (bool):  [Read-Write] Whether to lock the level sequence when done recording
- ``auto_serialize`` (bool):  [Read-Write] Whether to incrementally serialize and store some data while recording
- ``countdown_seconds`` (float):  [Read-Write] Delay that we will use before starting recording
- ``engine_time_dilation`` (float):  [Read-Write] The engine time dilation to apply during the recording
- ``maximize_viewport`` (bool):  [Read-Write] Whether to maximize the viewport (enter Immersive Mode) when recording
- ``reduce_keys_tolerance`` (float):  [Read-Write] Tolerance to use when reducing keys
- ``remove_redundant_tracks`` (bool):  [Read-Write] Recommended for use with recorded spawnables. Beware that changes to actor instances in the map after recording may alter the recording when played back
- ``reset_playhead`` (bool):  [Read-Write] Reset playhead to beginning of the playback range when starting recording
- ``save_recorded_assets`` (bool):  [Read-Write] Whether to save recorded level sequences and assets when done recording
- ``stop_at_playback_end`` (bool):  [Read-Write] Automatically stop recording when reaching the end of the playback range

<a id="unreal.TakeRecorderUserParameters.__init__"></a>

#### __init__

```python
def __init__(maximize_viewport: bool = False,
             countdown_seconds: float = 0.000000,
             engine_time_dilation: float = 0.000000,
             reset_playhead: bool = False,
             stop_at_playback_end: bool = False,
             remove_redundant_tracks: bool = False,
             reduce_keys_tolerance: float = 0.000000,
             save_recorded_assets: bool = False,
             auto_lock: bool = False,
             auto_serialize: bool = False) -> None
```

<a id="unreal.TakeRecorderUserParameters.maximize_viewport"></a>

#### maximize_viewport

```python
@property
def maximize_viewport() -> bool
```

(bool):  [Read-Write] Whether to maximize the viewport (enter Immersive Mode) when recording

<a id="unreal.TakeRecorderUserParameters.maximize_viewport"></a>

#### maximize_viewport

```python
@maximize_viewport.setter
def maximize_viewport(value: bool) -> None
```

<a id="unreal.TakeRecorderUserParameters.countdown_seconds"></a>

#### countdown_seconds

```python
@property
def countdown_seconds() -> float
```

(float):  [Read-Write] Delay that we will use before starting recording

<a id="unreal.TakeRecorderUserParameters.countdown_seconds"></a>

#### countdown_seconds

```python
@countdown_seconds.setter
def countdown_seconds(value: float) -> None
```

<a id="unreal.TakeRecorderUserParameters.engine_time_dilation"></a>

#### engine_time_dilation

```python
@property
def engine_time_dilation() -> float
```

(float):  [Read-Write] The engine time dilation to apply during the recording

<a id="unreal.TakeRecorderUserParameters.engine_time_dilation"></a>

#### engine_time_dilation

```python
@engine_time_dilation.setter
def engine_time_dilation(value: float) -> None
```

<a id="unreal.TakeRecorderUserParameters.reset_playhead"></a>

#### reset_playhead

```python
@property
def reset_playhead() -> bool
```

(bool):  [Read-Write] Reset playhead to beginning of the playback range when starting recording

<a id="unreal.TakeRecorderUserParameters.reset_playhead"></a>

#### reset_playhead

```python
@reset_playhead.setter
def reset_playhead(value: bool) -> None
```

<a id="unreal.TakeRecorderUserParameters.stop_at_playback_end"></a>

#### stop_at_playback_end

```python
@property
def stop_at_playback_end() -> bool
```

(bool):  [Read-Write] Automatically stop recording when reaching the end of the playback range

<a id="unreal.TakeRecorderUserParameters.stop_at_playback_end"></a>

#### stop_at_playback_end

```python
@stop_at_playback_end.setter
def stop_at_playback_end(value: bool) -> None
```

<a id="unreal.TakeRecorderUserParameters.remove_redundant_tracks"></a>

#### remove_redundant_tracks

```python
@property
def remove_redundant_tracks() -> bool
```

(bool):  [Read-Write] Recommended for use with recorded spawnables. Beware that changes to actor instances in the map after recording may alter the recording when played back

<a id="unreal.TakeRecorderUserParameters.remove_redundant_tracks"></a>

#### remove_redundant_tracks

```python
@remove_redundant_tracks.setter
def remove_redundant_tracks(value: bool) -> None
```

<a id="unreal.TakeRecorderUserParameters.reduce_keys_tolerance"></a>

#### reduce_keys_tolerance

```python
@property
def reduce_keys_tolerance() -> float
```

(float):  [Read-Write] Tolerance to use when reducing keys

<a id="unreal.TakeRecorderUserParameters.reduce_keys_tolerance"></a>

#### reduce_keys_tolerance

```python
@reduce_keys_tolerance.setter
def reduce_keys_tolerance(value: float) -> None
```

<a id="unreal.TakeRecorderUserParameters.save_recorded_assets"></a>

#### save_recorded_assets

```python
@property
def save_recorded_assets() -> bool
```

(bool):  [Read-Write] Whether to save recorded level sequences and assets when done recording

<a id="unreal.TakeRecorderUserParameters.save_recorded_assets"></a>

#### save_recorded_assets

```python
@save_recorded_assets.setter
def save_recorded_assets(value: bool) -> None
```

<a id="unreal.TakeRecorderUserParameters.auto_lock"></a>

#### auto_lock

```python
@property
def auto_lock() -> bool
```

(bool):  [Read-Write] Whether to lock the level sequence when done recording

<a id="unreal.TakeRecorderUserParameters.auto_lock"></a>

#### auto_lock

```python
@auto_lock.setter
def auto_lock(value: bool) -> None
```

<a id="unreal.TakeRecorderUserParameters.auto_serialize"></a>

#### auto_serialize

```python
@property
def auto_serialize() -> bool
```

(bool):  [Read-Write] Whether to incrementally serialize and store some data while recording

<a id="unreal.TakeRecorderUserParameters.auto_serialize"></a>

#### auto_serialize

```python
@auto_serialize.setter
def auto_serialize(value: bool) -> None
```

<a id="unreal.TakeRecorderProjectParameters"></a>