## MoviePipelineLibrary Objects

```python
class MoviePipelineLibrary(BlueprintFunctionLibrary)
```

Movie Pipeline Blueprint Library

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineBlueprintLibrary.h

<a id="unreal.MoviePipelineLibrary.update_job_shot_list_from_sequence"></a>

#### update_job_shot_list_from_sequence

```python
@classmethod
def update_job_shot_list_from_sequence(cls, sequence: LevelSequence,
                                       job: MoviePipelineExecutorJob) -> bool
```

X.update_job_shot_list_from_sequence(sequence, job) -> bool
Scan the provided sequence in the job to see which camera cut sections we would try to render and update the job's shotlist.

Args:
    sequence (LevelSequence): 
    job (MoviePipelineExecutorJob): 

Returns:
    bool: 

    shots_changed (bool):

<a id="unreal.MoviePipelineLibrary.resolve_version_number"></a>

#### resolve_version_number

```python
@classmethod
def resolve_version_number(cls,
                           params: MoviePipelineFilenameResolveParams,
                           get_next_version: bool = True) -> int
```

X.resolve_version_number(params, get_next_version=True) -> int32
If version number is manually specified by the Job, returns that. Otherwise search the Output Directory for the highest version already existing (and increment it by one if bGetNextVersion is true).

Args:
    params (MoviePipelineFilenameResolveParams): 
    get_next_version (bool): 

Returns:
    int32:

<a id="unreal.MoviePipelineLibrary.resolve_filename_format_arguments"></a>

#### resolve_filename_format_arguments

```python
@classmethod
def resolve_filename_format_arguments(
    cls, format_string: str, params: MoviePipelineFilenameResolveParams
) -> Tuple[str, MoviePipelineFormatArgs]
```

X.resolve_filename_format_arguments(format_string, params) -> (out_final_path=str, out_merged_format_args=MoviePipelineFormatArgs)
Resolves the provided InFormatString by converting {format_strings} into settings provided by the primary config.

Args:
    format_string (str): A format string (in the form of "{format_key1}_{format_key2}") to resolve.
    params (MoviePipelineFilenameResolveParams): The parameters to resolve the format string with. See FMoviePipelineFilenameResolveParams properties for details. Expected that you fill out all of the parameters so that they can be used to resolve strings, otherwise default values may be used.

Returns:
    tuple: 

    out_final_path (str): The final filepath based on a combination of the format string and the Resolve Params.

    out_merged_format_args (MoviePipelineFormatArgs):

<a id="unreal.MoviePipelineLibrary.load_manifest_file_from_string"></a>

#### load_manifest_file_from_string

```python
@classmethod
def load_manifest_file_from_string(
        cls, manifest_file_path: str) -> MoviePipelineQueue
```

X.load_manifest_file_from_string(manifest_file_path) -> MoviePipelineQueue
Loads the specified manifest file and converts it into an UMoviePipelineQueue. Use in combination with SaveQueueToManifestFile.

Args:
    manifest_file_path (str): 

Returns:
    MoviePipelineQueue:

<a id="unreal.MoviePipelineLibrary.get_root_timecode"></a>

#### get_root_timecode

```python
@classmethod
def get_root_timecode(cls, movie_pipeline: MoviePipeline) -> Timecode
```

X.get_root_timecode(movie_pipeline) -> Timecode
Get Root Timecode

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    Timecode:

<a id="unreal.MoviePipelineLibrary.get_root_frame_number"></a>

#### get_root_frame_number

```python
@classmethod
def get_root_frame_number(cls, movie_pipeline: MoviePipeline) -> FrameNumber
```

X.get_root_frame_number(movie_pipeline) -> FrameNumber
Get Root Frame Number

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    FrameNumber:

<a id="unreal.MoviePipelineLibrary.get_pipeline_state"></a>

#### get_pipeline_state

```python
@classmethod
def get_pipeline_state(cls,
                       pipeline: MoviePipeline) -> MovieRenderPipelineState
```

X.get_pipeline_state(pipeline) -> MovieRenderPipelineState
Get the current state of the specified Pipeline. See EMovieRenderPipelineState for more detail about each state.

Args:
    pipeline (MoviePipeline): The pipeline to get the state for.

Returns:
    MovieRenderPipelineState: Current State.

<a id="unreal.MoviePipelineLibrary.get_overall_segment_counts"></a>

#### get_overall_segment_counts

```python
@classmethod
def get_overall_segment_counts(
        cls, movie_pipeline: MoviePipeline) -> Tuple[int, int]
```

X.get_overall_segment_counts(movie_pipeline) -> (out_current_index=int32, out_total_count=int32)
Get Overall Segment Counts

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    tuple: 

    out_current_index (int32): 

    out_total_count (int32):

<a id="unreal.MoviePipelineLibrary.get_overall_output_frames"></a>

#### get_overall_output_frames

```python
@classmethod
def get_overall_output_frames(
        cls, movie_pipeline: MoviePipeline) -> Tuple[int, int]
```

X.get_overall_output_frames(movie_pipeline) -> (out_current_index=int32, out_total_count=int32)
Get Overall Output Frames

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    tuple: 

    out_current_index (int32): 

    out_total_count (int32):

<a id="unreal.MoviePipelineLibrary.get_movie_pipeline_engine_changelist_label"></a>

#### get_movie_pipeline_engine_changelist_label

```python
@classmethod
def get_movie_pipeline_engine_changelist_label(
        cls, movie_pipeline: MoviePipeline) -> Text
```

X.get_movie_pipeline_engine_changelist_label(movie_pipeline) -> Text
Get a string to represent the Changelist Number for the burn in. This can be driven by a Modular Feature if you want to permanently replace it with different information.

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    Text:

<a id="unreal.MoviePipelineLibrary.get_map_package_name"></a>

#### get_map_package_name

```python
@classmethod
def get_map_package_name(cls, job: MoviePipelineExecutorJob) -> str
```

X.get_map_package_name(job) -> str
Get the package name for the map in this job. The level travel command requires the package path and not the asset path.

Args:
    job (MoviePipelineExecutorJob): 

Returns:
    str:

<a id="unreal.MoviePipelineLibrary.get_job_name"></a>

#### get_job_name

```python
@classmethod
def get_job_name(cls, movie_pipeline: MoviePipeline) -> Text
```

X.get_job_name(movie_pipeline) -> Text
Get Job Name

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    Text:

<a id="unreal.MoviePipelineLibrary.get_job_initialization_time"></a>

#### get_job_initialization_time

```python
@classmethod
def get_job_initialization_time(cls,
                                movie_pipeline: MoviePipeline) -> DateTime
```

X.get_job_initialization_time(movie_pipeline) -> DateTime
Get Job Initialization Time

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    DateTime:

<a id="unreal.MoviePipelineLibrary.get_job_author"></a>

#### get_job_author

```python
@classmethod
def get_job_author(cls, movie_pipeline: MoviePipeline) -> Text
```

X.get_job_author(movie_pipeline) -> Text
Get Job Author

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    Text:

<a id="unreal.MoviePipelineLibrary.get_estimated_time_remaining"></a>

#### get_estimated_time_remaining

```python
@classmethod
def get_estimated_time_remaining(
        cls, pipeline: MoviePipeline) -> Optional[Timespan]
```

X.get_estimated_time_remaining(pipeline) -> Timespan or None
Get the estimated amount of time remaining for the current pipeline. Based on looking at the total
amount of samples to render vs. how many have been completed so far. Inaccurate when Time Dilation
is used, and gets more accurate over the course of the render.

Args:
    pipeline (MoviePipeline): The pipeline to get the time estimate from.

Returns:
    Timespan or None: True if a valid estimate can be calculated, or false if it is not ready yet (ie: not enough samples rendered)

    out_estimate (Timespan): The resulting estimate, or FTimespan() if estimate is not valid.

<a id="unreal.MoviePipelineLibrary.get_effective_output_resolution"></a>

#### get_effective_output_resolution

```python
@classmethod
def get_effective_output_resolution(
        cls,
        primary_config: MoviePipelinePrimaryConfig,
        pipeline_executor_shot: MoviePipelineExecutorShot,
        default_overscan: float = 0.000000) -> IntPoint
```

X.get_effective_output_resolution(primary_config, pipeline_executor_shot, default_overscan=0.000000) -> IntPoint
In case of Overscan percentage being higher than 0 we render additional pixels. This function returns the resolution with overscan taken into account.

Args:
    primary_config (MoviePipelinePrimaryConfig): 
    pipeline_executor_shot (MoviePipelineExecutorShot): 
    default_overscan (float): 

Returns:
    IntPoint:

<a id="unreal.MoviePipelineLibrary.get_current_version_number"></a>

#### get_current_version_number

```python
@classmethod
def get_current_version_number(cls, movie_pipeline: MoviePipeline) -> int
```

X.get_current_version_number(movie_pipeline) -> int32
Retrieves the cached version number calculated for the current shot, which depends on where the version token was used in the File Name Output
ie: If {version} comes before {shot_name} then all shots will use the same version number, but if it comes afterwards then each shot may
have a different version (which is the highest number found of that particular shot). This function should retrieve what is used in the
filename writing step either way.

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    int32:

<a id="unreal.MoviePipelineLibrary.get_current_shot_timecode"></a>

#### get_current_shot_timecode

```python
@classmethod
def get_current_shot_timecode(cls, movie_pipeline: MoviePipeline) -> Timecode
```

X.get_current_shot_timecode(movie_pipeline) -> Timecode
Get Current Shot Timecode

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    Timecode:

<a id="unreal.MoviePipelineLibrary.get_current_shot_frame_number"></a>

#### get_current_shot_frame_number

```python
@classmethod
def get_current_shot_frame_number(
        cls, movie_pipeline: MoviePipeline) -> FrameNumber
```

X.get_current_shot_frame_number(movie_pipeline) -> FrameNumber
Get Current Shot Frame Number

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    FrameNumber:

<a id="unreal.MoviePipelineLibrary.get_current_sequence"></a>

#### get_current_sequence

```python
@classmethod
def get_current_sequence(cls, movie_pipeline: MoviePipeline) -> LevelSequence
```

X.get_current_sequence(movie_pipeline) -> LevelSequence
Get Current Sequence

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    LevelSequence:

<a id="unreal.MoviePipelineLibrary.get_current_segment_work_metrics"></a>

#### get_current_segment_work_metrics

```python
@classmethod
def get_current_segment_work_metrics(
        cls, movie_pipeline: MoviePipeline) -> MoviePipelineSegmentWorkMetrics
```

X.get_current_segment_work_metrics(movie_pipeline) -> MoviePipelineSegmentWorkMetrics
Get Current Segment Work Metrics

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    MoviePipelineSegmentWorkMetrics:

<a id="unreal.MoviePipelineLibrary.get_current_segment_state"></a>

#### get_current_segment_state

```python
@classmethod
def get_current_segment_state(
        cls, movie_pipeline: MoviePipeline) -> MovieRenderShotState
```

X.get_current_segment_state(movie_pipeline) -> MovieRenderShotState
Get Current Segment State

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    MovieRenderShotState:

<a id="unreal.MoviePipelineLibrary.get_current_segment_name"></a>

#### get_current_segment_name

```python
@classmethod
def get_current_segment_name(
        cls, movie_pipeline: MoviePipeline) -> Tuple[Text, Text]
```

X.get_current_segment_name(movie_pipeline) -> (out_outer_name=Text, out_inner_name=Text)
Get Current Segment Name

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    tuple: 

    out_outer_name (Text): 

    out_inner_name (Text):

<a id="unreal.MoviePipelineLibrary.get_current_focus_distance"></a>

#### get_current_focus_distance

```python
@classmethod
def get_current_focus_distance(cls, movie_pipeline: MoviePipeline) -> float
```

X.get_current_focus_distance(movie_pipeline) -> float
Get Current Focus Distance

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    float:

<a id="unreal.MoviePipelineLibrary.get_current_focal_length"></a>

#### get_current_focal_length

```python
@classmethod
def get_current_focal_length(cls, movie_pipeline: MoviePipeline) -> float
```

X.get_current_focal_length(movie_pipeline) -> float
Get Current Focal Length

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    float:

<a id="unreal.MoviePipelineLibrary.get_current_executor_shot"></a>

#### get_current_executor_shot

```python
@classmethod
def get_current_executor_shot(
        cls, movie_pipeline: MoviePipeline) -> MoviePipelineExecutorShot
```

X.get_current_executor_shot(movie_pipeline) -> MoviePipelineExecutorShot
Get Current Executor Shot

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    MoviePipelineExecutorShot:

<a id="unreal.MoviePipelineLibrary.get_current_aperture"></a>

#### get_current_aperture

```python
@classmethod
def get_current_aperture(cls, movie_pipeline: MoviePipeline) -> float
```

X.get_current_aperture(movie_pipeline) -> float
Get Current Aperture

Args:
    movie_pipeline (MoviePipeline): 

Returns:
    float:

<a id="unreal.MoviePipelineLibrary.get_completion_percentage"></a>

#### get_completion_percentage

```python
@classmethod
def get_completion_percentage(cls, pipeline: MoviePipeline) -> float
```

X.get_completion_percentage(pipeline) -> float
Gets the completion percent of the Pipeline in 0-1

Args:
    pipeline (MoviePipeline): 

Returns:
    float:

<a id="unreal.MoviePipelineLibrary.find_or_get_default_setting_for_shot"></a>

#### find_or_get_default_setting_for_shot

```python
@classmethod
def find_or_get_default_setting_for_shot(
        cls, setting_type: Class, primary_config: MoviePipelinePrimaryConfig,
        shot: MoviePipelineExecutorShot) -> MoviePipelineSetting
```

X.find_or_get_default_setting_for_shot(setting_type, primary_config, shot) -> MoviePipelineSetting
Allows access to a setting of provided type for specific shot.

Args:
    setting_type (type(Class)): 
    primary_config (MoviePipelinePrimaryConfig): 
    shot (MoviePipelineExecutorShot): 

Returns:
    MoviePipelineSetting:

<a id="unreal.MoviePipelineLibrary.duplicate_sequence"></a>

#### duplicate_sequence

```python
@classmethod
def duplicate_sequence(cls, outer: Object,
                       sequence: MovieSceneSequence) -> MovieSceneSequence
```

X.duplicate_sequence(outer, sequence) -> MovieSceneSequence
Duplicates the specified sequence using a medium depth copy. Standard duplication will only duplicate
the top level Sequence (since shots and sub-sequences are other standalone assets) so this function
recursively duplicates the given sequence, shot and subsequence and then fixes up the references to
point to newly duplicated sequences.

Use at your own risk. Some features may not work when duplicated (complex object binding arrangements,
blueprint GetSequenceBinding nodes, etc.) but can be useful when wanting to create a bunch of variations
with minor differences (such as swapping out an actor, track, etc.)

This does not duplicate any assets that the sequence points to outside of Shots/Subsequences.

Args:
    outer (Object): The Outer of the newly duplicated object. Leave null for TransientPackage();
    sequence (MovieSceneSequence): The sequence to recursively duplicate.

Returns:
    MovieSceneSequence: The duplicated sequence, or null if no sequence was provided to duplicate.

<a id="unreal.MoviePipelineCameraSetting"></a>