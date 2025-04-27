## MoviePipelineEditorLibrary Objects

```python
class MoviePipelineEditorLibrary(BlueprintFunctionLibrary)
```

Movie Pipeline Editor Blueprint Library

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineEditor
- **File**: MoviePipelineEditorBlueprintLibrary.h

<a id="unreal.MoviePipelineEditorLibrary.warn_user_of_unsaved_map"></a>

#### warn_user_of_unsaved_map

```python
@classmethod
def warn_user_of_unsaved_map(cls) -> None
```

X.warn_user_of_unsaved_map() -> None
Pop a dialog box that specifies that they cannot render due to never saved map. Only shows OK button.

<a id="unreal.MoviePipelineEditorLibrary.save_queue_to_manifest_file"></a>

#### save_queue_to_manifest_file

```python
@classmethod
def save_queue_to_manifest_file(
        cls,
        pipeline_queue: MoviePipelineQueue) -> Tuple[MoviePipelineQueue, str]
```

X.save_queue_to_manifest_file(pipeline_queue) -> (MoviePipelineQueue, out_manifest_file_path=str)
Take the specified Queue, duplicate it and write it to disk in the ../Saved/MovieRenderPipeline/ folder. Returns the duplicated queue.

Args:
    pipeline_queue (MoviePipelineQueue): 

Returns:
    str: 

    out_manifest_file_path (str):

<a id="unreal.MoviePipelineEditorLibrary.resolve_output_directory_from_job"></a>

#### resolve_output_directory_from_job

```python
@classmethod
def resolve_output_directory_from_job(cls,
                                      job: MoviePipelineExecutorJob) -> str
```

X.resolve_output_directory_from_job(job) -> str
Resolves as much of the output directory for this job into a usable directory path as possible. Cannot resolve anything that relies on shot name, frame numbers, etc.

Args:
    job (MoviePipelineExecutorJob): 

Returns:
    str:

<a id="unreal.MoviePipelineEditorLibrary.is_map_valid_for_remote_render"></a>

#### is_map_valid_for_remote_render

```python
@classmethod
def is_map_valid_for_remote_render(
        cls, jobs: Array[MoviePipelineExecutorJob]) -> bool
```

X.is_map_valid_for_remote_render(jobs) -> bool
Checks to see if any of the Jobs try to point to maps that wouldn't be valid on a remote render (ie: unsaved maps)

Args:
    jobs (Array[MoviePipelineExecutorJob]): 

Returns:
    bool:

<a id="unreal.MoviePipelineEditorLibrary.get_display_output_path_from_job"></a>

#### get_display_output_path_from_job

```python
@classmethod
def get_display_output_path_from_job(
        cls, job: MoviePipelineExecutorJob) -> Optional[str]
```

X.get_display_output_path_from_job(job) -> str or None
Returns display string for output directory for this job. Does not resolve the full path from tokens.

Args:
    job (MoviePipelineExecutorJob): 

Returns:
    str or None: 

    out_output_path (str):

<a id="unreal.MoviePipelineEditorLibrary.export_config_to_asset"></a>

#### export_config_to_asset

```python
@classmethod
def export_config_to_asset(
        cls, config: MoviePipelinePrimaryConfig, package_path: str,
        file_name: str,
        save_asset: bool) -> Optional[Tuple[MoviePipelinePrimaryConfig, Text]]
```

X.export_config_to_asset(config, package_path, file_name, save_asset) -> (out_asset=MoviePipelinePrimaryConfig, out_error_reason=Text) or None
Export Config to Asset

Args:
    config (MoviePipelinePrimaryConfig): 
    package_path (str): 
    file_name (str): 
    save_asset (bool): 

Returns:
    tuple or None: 

    out_asset (MoviePipelinePrimaryConfig): 

    out_error_reason (Text):

<a id="unreal.MoviePipelineEditorLibrary.ensure_job_has_default_settings"></a>

#### ensure_job_has_default_settings

```python
@classmethod
def ensure_job_has_default_settings(cls,
                                    job: MoviePipelineExecutorJob) -> None
```

X.ensure_job_has_default_settings(job) -> None
Ensure the job has the settings specified by the project settings added. If they're already added we don't modify the object so that we don't make it confused about whether or not you've modified the preset.

Args:
    job (MoviePipelineExecutorJob):

<a id="unreal.MoviePipelineEditorLibrary.create_job_from_sequence"></a>

#### create_job_from_sequence

```python
@classmethod
def create_job_from_sequence(
        cls, pipeline_queue: MoviePipelineQueue,
        sequence: LevelSequence) -> MoviePipelineExecutorJob
```

X.create_job_from_sequence(pipeline_queue, sequence) -> MoviePipelineExecutorJob
Create a job from a level sequence. Sets the map as the currently editor world, the author, the sequence and the job name as the sequence name on the new job. Returns the newly created job.

Args:
    pipeline_queue (MoviePipelineQueue): 
    sequence (LevelSequence): 

Returns:
    MoviePipelineExecutorJob:

<a id="unreal.MoviePipelineEditorLibrary.convert_manifest_file_to_string"></a>

#### convert_manifest_file_to_string

```python
@classmethod
def convert_manifest_file_to_string(cls, manifest_file_path: str) -> str
```

X.convert_manifest_file_to_string(manifest_file_path) -> str
Loads the specified manifest file and converts it into an FString to be embedded with HTTP REST requests. Use in combination with SaveQueueToManifestFile.

Args:
    manifest_file_path (str): 

Returns:
    str:

<a id="unreal.MoviePipelineFunctionalTestBase"></a>