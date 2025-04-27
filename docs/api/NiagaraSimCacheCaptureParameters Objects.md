## NiagaraSimCacheCaptureParameters Objects

```python
class NiagaraSimCacheCaptureParameters(StructBase)
```

Niagara Sim Cache Capture Parameters

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSimCacheCapture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``append_to_sim_cache`` (bool):  [Read-Write] When enabled we will append to the existing simulation cache rather than destroying the existing contents.
- ``capture_all_frames_immediatly`` (bool):  [Read-Write] When enabled we will capture all the requested frames immediatly.
  This will capture the simulation outside of the main work tick, i.e. if you request a 10 frame capture we will loop capturing 10 frames on the capture call rather than over 10 world ticks.
- ``capture_fixed_number_of_frames`` (bool):  [Read-Write] When enabled we capture NumFrames number of frames, otherwise the capture will continue until cancelled or the simulation is complete.
- ``capture_rate`` (int32):  [Read-Write] Allows for reducing the frequency of captured frames in relation to the simulation's frames. The ratio is 1 / CaptureRate, so a CaptureRate of 2 would captures frames 0, 2, 4, etc.
- ``immediate_capture_delta_time`` (float):  [Read-Write] The delta time in seconds to use when manually advancing the simulation.Defaults to 1 / 60th of a second(0.01666).
- ``num_frames`` (int32):  [Read-Write] The max number of frames to capture. The capture will stop when the simulation completes or we have rendered this many frames, whichever happens first.
  Set to 0 to capture until simulation completes.
- ``timeout_frame_count`` (int32):  [Read-Write] When we fail to capture a new frame after this many frames the capture will complete automatically.
- ``use_timeout`` (bool):  [Read-Write] When enabled the capture will time out if we reach the defined number of frames without anything new to capture.

<a id="unreal.NiagaraSimCacheCaptureParameters.__init__"></a>

#### __init__

```python
def __init__(append_to_sim_cache: bool = False,
             capture_fixed_number_of_frames: bool = False,
             num_frames: int = 0,
             capture_rate: int = 0,
             use_timeout: bool = False,
             timeout_frame_count: int = 0,
             capture_all_frames_immediatly: bool = False,
             immediate_capture_delta_time: float = 0.000000) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.append_to_sim_cache"></a>

#### append_to_sim_cache

```python
@property
def append_to_sim_cache() -> bool
```

(bool):  [Read-Write] When enabled we will append to the existing simulation cache rather than destroying the existing contents.

<a id="unreal.NiagaraSimCacheCaptureParameters.append_to_sim_cache"></a>

#### append_to_sim_cache

```python
@append_to_sim_cache.setter
def append_to_sim_cache(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.capture_fixed_number_of_frames"></a>

#### capture_fixed_number_of_frames

```python
@property
def capture_fixed_number_of_frames() -> bool
```

(bool):  [Read-Write] When enabled we capture NumFrames number of frames, otherwise the capture will continue until cancelled or the simulation is complete.

<a id="unreal.NiagaraSimCacheCaptureParameters.capture_fixed_number_of_frames"></a>

#### capture_fixed_number_of_frames

```python
@capture_fixed_number_of_frames.setter
def capture_fixed_number_of_frames(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.num_frames"></a>

#### num_frames

```python
@property
def num_frames() -> int
```

(int32):  [Read-Write] The max number of frames to capture. The capture will stop when the simulation completes or we have rendered this many frames, whichever happens first.
Set to 0 to capture until simulation completes.

<a id="unreal.NiagaraSimCacheCaptureParameters.num_frames"></a>

#### num_frames

```python
@num_frames.setter
def num_frames(value: int) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.capture_rate"></a>

#### capture_rate

```python
@property
def capture_rate() -> int
```

(int32):  [Read-Write] Allows for reducing the frequency of captured frames in relation to the simulation's frames. The ratio is 1 / CaptureRate, so a CaptureRate of 2 would captures frames 0, 2, 4, etc.

<a id="unreal.NiagaraSimCacheCaptureParameters.capture_rate"></a>

#### capture_rate

```python
@capture_rate.setter
def capture_rate(value: int) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.use_timeout"></a>

#### use_timeout

```python
@property
def use_timeout() -> bool
```

(bool):  [Read-Write] When enabled the capture will time out if we reach the defined number of frames without anything new to capture.

<a id="unreal.NiagaraSimCacheCaptureParameters.use_timeout"></a>

#### use_timeout

```python
@use_timeout.setter
def use_timeout(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.timeout_frame_count"></a>

#### timeout_frame_count

```python
@property
def timeout_frame_count() -> int
```

(int32):  [Read-Write] When we fail to capture a new frame after this many frames the capture will complete automatically.

<a id="unreal.NiagaraSimCacheCaptureParameters.timeout_frame_count"></a>

#### timeout_frame_count

```python
@timeout_frame_count.setter
def timeout_frame_count(value: int) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.capture_all_frames_immediatly"></a>

#### capture_all_frames_immediatly

```python
@property
def capture_all_frames_immediatly() -> bool
```

(bool):  [Read-Write] When enabled we will capture all the requested frames immediatly.
This will capture the simulation outside of the main work tick, i.e. if you request a 10 frame capture we will loop capturing 10 frames on the capture call rather than over 10 world ticks.

<a id="unreal.NiagaraSimCacheCaptureParameters.capture_all_frames_immediatly"></a>

#### capture_all_frames_immediatly

```python
@capture_all_frames_immediatly.setter
def capture_all_frames_immediatly(value: bool) -> None
```

<a id="unreal.NiagaraSimCacheCaptureParameters.immediate_capture_delta_time"></a>

#### immediate_capture_delta_time

```python
@property
def immediate_capture_delta_time() -> float
```

(float):  [Read-Write] The delta time in seconds to use when manually advancing the simulation.Defaults to 1 / 60th of a second(0.01666).

<a id="unreal.NiagaraSimCacheCaptureParameters.immediate_capture_delta_time"></a>

#### immediate_capture_delta_time

```python
@immediate_capture_delta_time.setter
def immediate_capture_delta_time(value: float) -> None
```

<a id="unreal.NiagaraSimCacheCreateParameters"></a>