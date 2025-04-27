## FrameMetrics Objects

```python
class FrameMetrics(StructBase)
```

Metrics that correspond to a particular frame

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: MovieSceneCaptureProtocolBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_delta`` (float):  [Read-Write] The total amount of time, in seconds, that this specific frame took to render (not accounting for dropped frames)
- ``frame_number`` (int32):  [Read-Write] The index of this frame from the start of the capture, including dropped frames
- ``num_dropped_frames`` (int32):  [Read-Write] The number of frames we dropped in-between this frame, and the last one we captured
- ``total_elapsed_time`` (float):  [Read-Write] The total amount of time, in seconds, since the capture started

<a id="unreal.FrameMetrics.__init__"></a>

#### __init__

```python
def __init__(total_elapsed_time: float = 0.000000,
             frame_delta: float = 0.000000,
             frame_number: int = 0,
             num_dropped_frames: int = 0) -> None
```

<a id="unreal.FrameMetrics.total_elapsed_time"></a>

#### total_elapsed_time

```python
@property
def total_elapsed_time() -> float
```

(float):  [Read-Only] The total amount of time, in seconds, since the capture started

<a id="unreal.FrameMetrics.frame_delta"></a>

#### frame_delta

```python
@property
def frame_delta() -> float
```

(float):  [Read-Only] The total amount of time, in seconds, that this specific frame took to render (not accounting for dropped frames)

<a id="unreal.FrameMetrics.frame_number"></a>

#### frame_number

```python
@property
def frame_number() -> int
```

(int32):  [Read-Only] The index of this frame from the start of the capture, including dropped frames

<a id="unreal.FrameMetrics.num_dropped_frames"></a>

#### num_dropped_frames

```python
@property
def num_dropped_frames() -> int
```

(int32):  [Read-Only] The number of frames we dropped in-between this frame, and the last one we captured

<a id="unreal.CapturedPixelsID"></a>