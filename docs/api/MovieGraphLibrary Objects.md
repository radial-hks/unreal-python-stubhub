## MovieGraphLibrary Objects

```python
class MovieGraphLibrary(BlueprintFunctionLibrary)
```

Movie Graph Blueprint Library

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphBlueprintLibrary.h

<a id="unreal.MovieGraphLibrary.resolve_version_number"></a>

#### resolve_version_number

```python
@classmethod
def resolve_version_number(cls,
                           params: MovieGraphFilenameResolveParams,
                           get_next_version: bool = True) -> int
```

X.resolve_version_number(params, get_next_version=True) -> int32
If the version number is explicitly specified on the Output Setting node, returns that. Otherwise searches the
output directory for the highest version that already exists (and increments it by one if bGetNextVersion is
true). Returns -1 if the version could not be resolved.

Args:
    params (MovieGraphFilenameResolveParams): 
    get_next_version (bool): 

Returns:
    int32:

<a id="unreal.MovieGraphLibrary.resolve_filename_format_arguments"></a>

#### resolve_filename_format_arguments

```python
@classmethod
def resolve_filename_format_arguments(
    cls, format_string: str, params: MovieGraphFilenameResolveParams
) -> Tuple[str, MovieGraphResolveArgs]
```

X.resolve_filename_format_arguments(format_string, params) -> (str, out_merged_format_args=MovieGraphResolveArgs)
Takes a Movie Graph format string (in the form of {token}), a list of parameters (which normally come from the running UMovieGraphPipeline) and
resolves them into a string. Unknown tokens are ignored. Which tokens can be resolved depends on the contents of InParams, tokens from settings
rely on a evaluated config being provided, etc.

Args:
    format_string (str): Format string to attempt to resolve. Leave blank if just the format args should be populated.
    params (MovieGraphFilenameResolveParams): A list of parameters to use as source data for the resolve step. Normally comes from the UMovieGraphPipeline instance, - but takes (mostly) POD here to allow using this function outside of the render runtime.

Returns:
    MovieGraphResolveArgs: The resolved format string. Returns an empty string if InFormatString is blank.

    out_merged_format_args (MovieGraphResolveArgs): The set of KVP for both filename formats and file metadata that is generated as a result of this. Provided in case you - needed to do your own string resolving with the final dataset.

<a id="unreal.MovieGraphLibrary.named_resolution_from_size"></a>

#### named_resolution_from_size

```python
@classmethod
def named_resolution_from_size(cls, res_x: int,
                               res_y: int) -> MovieGraphNamedResolution
```

X.named_resolution_from_size(res_x, res_y) -> MovieGraphNamedResolution
Create a Named Resolution from the given resolution. Given named resolution will be named "Custom".

Args:
    res_x (int32): 
    res_y (int32): 

Returns:
    MovieGraphNamedResolution:

<a id="unreal.MovieGraphLibrary.named_resolution_from_profile"></a>

#### named_resolution_from_profile

```python
@classmethod
def named_resolution_from_profile(
        cls, resolution_profile_name: Name) -> MovieGraphNamedResolution
```

X.named_resolution_from_profile(resolution_profile_name) -> MovieGraphNamedResolution
Create a Named Resolution from the profile name. Throws a Kismet Exception if the profile name isn't found.
The known profiles can be found in UMovieGraphProjectSettings's CDO.

Args:
    resolution_profile_name (Name): 

Returns:
    MovieGraphNamedResolution:

<a id="unreal.MovieGraphLibrary.is_named_resolution_valid"></a>

#### is_named_resolution_valid

```python
@classmethod
def is_named_resolution_valid(cls, resolution_profile_name: Name) -> bool
```

X.is_named_resolution_valid(resolution_profile_name) -> bool
Utility function for checking if a given resolution profile name is valid, since NamedResolutionFromProfile
will throw a kismet exception, but blueprints can't actually try/catch them.

Args:
    resolution_profile_name (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphLibrary.get_root_timecode"></a>

#### get_root_timecode

```python
@classmethod
def get_root_timecode(cls,
                      movie_graph_pipeline: MovieGraphPipeline) -> Timecode
```

X.get_root_timecode(movie_graph_pipeline) -> Timecode
Gets the timecode of the current render at the root (sequence) level.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get timecode information from.

Returns:
    Timecode:

<a id="unreal.MovieGraphLibrary.get_root_frame_number"></a>

#### get_root_frame_number

```python
@classmethod
def get_root_frame_number(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> FrameNumber
```

X.get_root_frame_number(movie_graph_pipeline) -> FrameNumber
Gets the frame number of the current render at the root (sequence) level.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get frame number information from.

Returns:
    FrameNumber:

<a id="unreal.MovieGraphLibrary.get_pipeline_state"></a>

#### get_pipeline_state

```python
@classmethod
def get_pipeline_state(
        cls,
        movie_graph_pipeline: MovieGraphPipeline) -> MovieRenderPipelineState
```

X.get_pipeline_state(movie_graph_pipeline) -> MovieRenderPipelineState
Get the current state of the specified pipeline. See EMovieRenderPipelineState for more detail about each state.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the state for.

Returns:
    MovieRenderPipelineState: The current state.

<a id="unreal.MovieGraphLibrary.get_overall_segment_counts"></a>

#### get_overall_segment_counts

```python
@classmethod
def get_overall_segment_counts(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> Tuple[int, int]
```

X.get_overall_segment_counts(movie_graph_pipeline) -> (out_current_index=int32, out_total_count=int32)
Gets the number of segments (shots) that will be rendered.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get segment information from.

Returns:
    tuple: 

    out_current_index (int32): 

    out_total_count (int32):

<a id="unreal.MovieGraphLibrary.get_overall_output_frames"></a>

#### get_overall_output_frames

```python
@classmethod
def get_overall_output_frames(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> Tuple[int, int]
```

X.get_overall_output_frames(movie_graph_pipeline) -> (out_current_index=int32, out_total_count=int32)
Determines the overall current frame number and total number of frames.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the frame information from.

Returns:
    tuple: 

    out_current_index (int32): The current frame number.

    out_total_count (int32): The total number of frames.

<a id="unreal.MovieGraphLibrary.get_job_name"></a>

#### get_job_name

```python
@classmethod
def get_job_name(cls, movie_graph_pipeline: MovieGraphPipeline) -> Text
```

X.get_job_name(movie_graph_pipeline) -> Text
Gets the name of the current job.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the job name from.

Returns:
    Text:

<a id="unreal.MovieGraphLibrary.get_job_initialization_time"></a>

#### get_job_initialization_time

```python
@classmethod
def get_job_initialization_time(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> DateTime
```

X.get_job_initialization_time(movie_graph_pipeline) -> DateTime
Gets the time the job was initialized.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the job initialization time from.

Returns:
    DateTime:

<a id="unreal.MovieGraphLibrary.get_job_author"></a>

#### get_job_author

```python
@classmethod
def get_job_author(cls, movie_graph_pipeline: MovieGraphPipeline) -> Text
```

X.get_job_author(movie_graph_pipeline) -> Text
Gets the author of the current job, or the logged in user's username if the job has no specified author.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the job author from.

Returns:
    Text:

<a id="unreal.MovieGraphLibrary.get_estimated_time_remaining"></a>

#### get_estimated_time_remaining

```python
@classmethod
def get_estimated_time_remaining(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> Optional[Timespan]
```

X.get_estimated_time_remaining(movie_graph_pipeline) -> Timespan or None
Get the estimated amount of time remaining for the current pipeline. Based on looking at the total
amount of samples to render vs. how many have been completed so far. Inaccurate when Time Dilation
is used, and gets more accurate over the course of the render.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the time estimate from.

Returns:
    Timespan or None: True if a valid estimate can be calculated, or false if it is not ready yet (ie: not enough samples rendered)

    out_estimate (Timespan): The resulting estimate, or FTimespan() if estimate is not valid.

<a id="unreal.MovieGraphLibrary.get_effective_output_resolution"></a>

#### get_effective_output_resolution

```python
@classmethod
def get_effective_output_resolution(
        cls,
        evaluated_graph: MovieGraphEvaluatedConfig,
        default_overscan: float = 0.000000) -> IntPoint
```

X.get_effective_output_resolution(evaluated_graph, default_overscan=0.000000) -> IntPoint
In case of overscan percentage being higher than 0, additional pixels are rendered. This function returns the resolution with overscan taken into account.

Args:
    evaluated_graph (MovieGraphEvaluatedConfig): The evaluated graph that will provide context for resolving the resolution
    default_overscan (float): The default overscan to use if there are no camera settings that provide an overscan override value, from 0.0 to 1.0

Returns:
    IntPoint: The output resolution, taking into account overscan

<a id="unreal.MovieGraphLibrary.get_effective_frame_rate"></a>

#### get_effective_frame_rate

```python
@classmethod
def get_effective_frame_rate(cls, node: MovieGraphGlobalOutputSettingNode,
                             default_rate: FrameRate) -> FrameRate
```

X.get_effective_frame_rate(node, default_rate) -> FrameRate
If InNode is valid, inspects the provided OutputsettingNode to determine if it wants to override the
Frame Rate, and if so, returns the overwritten frame rate. If nullptr, or it does not have the
bOverride_bUseCustomFrameRate flag set, then InDefaultrate is returned.

Args:
    node (MovieGraphGlobalOutputSettingNode): Optional, setting to inspect for a custom framerate.
    default_rate (FrameRate): The frame rate to use if the node is nullptr or doesn't want to override the rate.

Returns:
    FrameRate: The effective frame rate (taking into account the node's desire to override it).

<a id="unreal.MovieGraphLibrary.get_current_version_number"></a>

#### get_current_version_number

```python
@classmethod
def get_current_version_number(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> int
```

X.get_current_version_number(movie_graph_pipeline) -> int32
Retrieves the cached version number calculated for the current shot, which depends on where the version token was used in the File Name Output
ie: If {version} comes before {shot_name} then all shots will use the same version number, but if it comes afterwards then each shot may
have a different version (which is the highest number found of that particular shot). This function should retrieve what is used in the
filename writing step either way.

Args:
    movie_graph_pipeline (MovieGraphPipeline): 

Returns:
    int32:

<a id="unreal.MovieGraphLibrary.get_current_shot_timecode"></a>

#### get_current_shot_timecode

```python
@classmethod
def get_current_shot_timecode(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> Timecode
```

X.get_current_shot_timecode(movie_graph_pipeline) -> Timecode
Gets the timecode of the current render at the shot level.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get timecode information from.

Returns:
    Timecode:

<a id="unreal.MovieGraphLibrary.get_current_shot_frame_number"></a>

#### get_current_shot_frame_number

```python
@classmethod
def get_current_shot_frame_number(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> FrameNumber
```

X.get_current_shot_frame_number(movie_graph_pipeline) -> FrameNumber
Gets the frame number of the current render at the shot level.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get frame number information from.

Returns:
    FrameNumber:

<a id="unreal.MovieGraphLibrary.get_current_segment_work_metrics"></a>

#### get_current_segment_work_metrics

```python
@classmethod
def get_current_segment_work_metrics(
    cls, movie_graph_pipeline: MovieGraphPipeline
) -> MoviePipelineSegmentWorkMetrics
```

X.get_current_segment_work_metrics(movie_graph_pipeline) -> MoviePipelineSegmentWorkMetrics
Gets the work metrics for the segment (shot) that is currently being rendered.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get segment information from.

Returns:
    MoviePipelineSegmentWorkMetrics:

<a id="unreal.MovieGraphLibrary.get_current_segment_state"></a>

#### get_current_segment_state

```python
@classmethod
def get_current_segment_state(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> MovieRenderShotState
```

X.get_current_segment_state(movie_graph_pipeline) -> MovieRenderShotState
Gets the state of the segment (shot) currently being rendered.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get segment information from.

Returns:
    MovieRenderShotState:

<a id="unreal.MovieGraphLibrary.get_current_segment_name"></a>

#### get_current_segment_name

```python
@classmethod
def get_current_segment_name(
        cls, movie_graph_pipeline: MovieGraphPipeline) -> Tuple[Text, Text]
```

X.get_current_segment_name(movie_graph_pipeline) -> (out_outer_name=Text, out_inner_name=Text)
Gets the name of the segment (shot) currently being rendered.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get segment information from.

Returns:
    tuple: 

    out_outer_name (Text): 

    out_inner_name (Text):

<a id="unreal.MovieGraphLibrary.get_current_focus_distance"></a>

#### get_current_focus_distance

```python
@classmethod
def get_current_focus_distance(cls,
                               movie_graph_pipeline: MovieGraphPipeline,
                               camera_index: int = -1) -> float
```

X.get_current_focus_distance(movie_graph_pipeline, camera_index=-1) -> float
Gets the focus distance for the camera currently in use.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the camera information from.
    camera_index (int32): 

Returns:
    float:

<a id="unreal.MovieGraphLibrary.get_current_focal_length"></a>

#### get_current_focal_length

```python
@classmethod
def get_current_focal_length(cls,
                             movie_graph_pipeline: MovieGraphPipeline,
                             camera_index: int = -1) -> float
```

X.get_current_focal_length(movie_graph_pipeline, camera_index=-1) -> float
Gets the focal length for the camera currently in use.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the camera information from.
    camera_index (int32): 

Returns:
    float:

<a id="unreal.MovieGraphLibrary.get_current_executor_shot"></a>

#### get_current_executor_shot

```python
@classmethod
def get_current_executor_shot(
        cls, movie_pipeline: MovieGraphPipeline) -> MoviePipelineExecutorShot
```

X.get_current_executor_shot(movie_pipeline) -> MoviePipelineExecutorShot
Gets the current shot being rendered by the graph (could be nullptr if rendering hasn't started or has moved to Finalize!)

Args:
    movie_pipeline (MovieGraphPipeline): 

Returns:
    MoviePipelineExecutorShot:

<a id="unreal.MovieGraphLibrary.get_current_cine_camera"></a>

#### get_current_cine_camera

```python
@classmethod
def get_current_cine_camera(cls,
                            movie_graph_pipeline: MovieGraphPipeline,
                            camera_index: int = -1) -> CineCameraComponent
```

X.get_current_cine_camera(movie_graph_pipeline, camera_index=-1) -> CineCameraComponent
Gets the currently active cine camera, or nullptr if one was not found.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the camera from.
    camera_index (int32): 

Returns:
    CineCameraComponent:

<a id="unreal.MovieGraphLibrary.get_current_aperture"></a>

#### get_current_aperture

```python
@classmethod
def get_current_aperture(cls,
                         movie_graph_pipeline: MovieGraphPipeline,
                         camera_index: int = -1) -> float
```

X.get_current_aperture(movie_graph_pipeline, camera_index=-1) -> float
Gets the aperture for the camera currently in use.

Args:
    movie_graph_pipeline (MovieGraphPipeline): The pipeline to get the camera information from.
    camera_index (int32): 

Returns:
    float:

<a id="unreal.MovieGraphLibrary.get_completion_percentage"></a>

#### get_completion_percentage

```python
@classmethod
def get_completion_percentage(cls, pipeline: MovieGraphPipeline) -> float
```

X.get_completion_percentage(pipeline) -> float
Gets the completion percent of the Pipeline in 0-1

Args:
    pipeline (MovieGraphPipeline): 

Returns:
    float:

<a id="unreal.MovieGraphBranchNode"></a>