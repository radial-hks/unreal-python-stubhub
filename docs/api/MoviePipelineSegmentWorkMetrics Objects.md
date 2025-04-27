## MoviePipelineSegmentWorkMetrics Objects

```python
class MoviePipelineSegmentWorkMetrics(StructBase)
```

Movie Pipeline Segment Work Metrics

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``engine_warm_up_frame_index`` (int32):  [Read-Only] The index of the engine warm up frame that we are working on. No rendering samples are produced for these.
- ``output_frame_index`` (int32):  [Read-Only] Index of the output frame we are working on right now.
- ``output_sub_sample_index`` (int32):  [Read-Only] Which temporal/spatial sub sample are we working on right now. This counts temporal, spatial, and tile samples to accurately reflect how much work is needed for this output frame.
- ``segment_name`` (str):  [Read-Only] The name of the segment (if any)
- ``total_engine_warm_up_frame_count`` (int32):  [Read-Only] The total number of engine warm up frames for this segment.
- ``total_output_frame_count`` (int32):  [Read-Only] The number of output frames we expect to make for this segment.
- ``total_sub_sample_count`` (int32):  [Read-Only] The total number of samples we will have to build to render this output frame.

<a id="unreal.MoviePipelineSegmentWorkMetrics.__init__"></a>

#### __init__

```python
def __init__(segment_name: str = "",
             output_frame_index: int = 0,
             total_output_frame_count: int = 0,
             output_sub_sample_index: int = 0,
             total_sub_sample_count: int = 0,
             engine_warm_up_frame_index: int = 0,
             total_engine_warm_up_frame_count: int = 0) -> None
```

<a id="unreal.MoviePipelineSegmentWorkMetrics.segment_name"></a>

#### segment_name

```python
@property
def segment_name() -> str
```

(str):  [Read-Only] The name of the segment (if any)

<a id="unreal.MoviePipelineSegmentWorkMetrics.output_frame_index"></a>

#### output_frame_index

```python
@property
def output_frame_index() -> int
```

(int32):  [Read-Only] Index of the output frame we are working on right now.

<a id="unreal.MoviePipelineSegmentWorkMetrics.total_output_frame_count"></a>

#### total_output_frame_count

```python
@property
def total_output_frame_count() -> int
```

(int32):  [Read-Only] The number of output frames we expect to make for this segment.

<a id="unreal.MoviePipelineSegmentWorkMetrics.output_sub_sample_index"></a>

#### output_sub_sample_index

```python
@property
def output_sub_sample_index() -> int
```

(int32):  [Read-Only] Which temporal/spatial sub sample are we working on right now. This counts temporal, spatial, and tile samples to accurately reflect how much work is needed for this output frame.

<a id="unreal.MoviePipelineSegmentWorkMetrics.total_sub_sample_count"></a>

#### total_sub_sample_count

```python
@property
def total_sub_sample_count() -> int
```

(int32):  [Read-Only] The total number of samples we will have to build to render this output frame.

<a id="unreal.MoviePipelineSegmentWorkMetrics.engine_warm_up_frame_index"></a>

#### engine_warm_up_frame_index

```python
@property
def engine_warm_up_frame_index() -> int
```

(int32):  [Read-Only] The index of the engine warm up frame that we are working on. No rendering samples are produced for these.

<a id="unreal.MoviePipelineSegmentWorkMetrics.total_engine_warm_up_frame_count"></a>

#### total_engine_warm_up_frame_count

```python
@property
def total_engine_warm_up_frame_count() -> int
```

(int32):  [Read-Only] The total number of engine warm up frames for this segment.

<a id="unreal.MoviePipelineCameraCutInfo"></a>