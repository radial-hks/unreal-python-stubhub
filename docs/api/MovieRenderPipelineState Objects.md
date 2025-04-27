## MovieRenderPipelineState Objects

```python
class MovieRenderPipelineState(EnumBase)
```

What is the current overall state of the Pipeline? States are processed in order from first to
last and all states will be hit (though there is no guarantee the state will not be transitioned
away from on the same frame it entered it). Used to help track overall progress and validate
code flow.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

<a id="unreal.MovieRenderPipelineState.UNINITIALIZED"></a>

#### UNINITIALIZED

0: The pipeline has not been initialized yet. Only valid operation is to call Initialize.

<a id="unreal.MovieRenderPipelineState.PRODUCING_FRAMES"></a>

#### PRODUCING_FRAMES

1: The pipeline has been initialized and is now controlling time and working on producing frames.

<a id="unreal.MovieRenderPipelineState.FINALIZE"></a>

#### FINALIZE

2: All desired frames have been produced. Audio is already finalized. Outputs have a chance to finish long processing tasks.

<a id="unreal.MovieRenderPipelineState.EXPORT"></a>

#### EXPORT

3: All outputs have finished writing to disk or otherwise processing. Additional exports that may have needed information about the produced file can now be run.

<a id="unreal.MovieRenderPipelineState.FINISHED"></a>

#### FINISHED

4: The pipeline has been shut down. It is an error to shut it down again.

<a id="unreal.MovieRenderShotState"></a>