## MoviePipelineImageSequenceOutput_EXR Objects

```python
class MoviePipelineImageSequenceOutput_EXR(MoviePipelineImageSequenceOutputBase
                                           )
```

Movie Pipeline Image Sequence Output EXR

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MoviePipelineEXROutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compression`` (EXRCompressionFormat):  [Read-Write] Which compression method should the resulting EXR file be compressed with
- ``multilayer`` (bool):  [Read-Write] Should we write all render passes to the same exr file? Not all software supports multi-layer exr files.

<a id="unreal.MoviePipelineImageSequenceOutput_EXR.compression"></a>

#### compression

```python
@property
def compression() -> EXRCompressionFormat
```

(EXRCompressionFormat):  [Read-Write] Which compression method should the resulting EXR file be compressed with

<a id="unreal.MoviePipelineImageSequenceOutput_EXR.compression"></a>

#### compression

```python
@compression.setter
def compression(value: EXRCompressionFormat) -> None
```

<a id="unreal.MoviePipelineImageSequenceOutput_EXR.multilayer"></a>

#### multilayer

```python
@property
def multilayer() -> bool
```

(bool):  [Read-Write] Should we write all render passes to the same exr file? Not all software supports multi-layer exr files.

<a id="unreal.MoviePipelineImageSequenceOutput_EXR.multilayer"></a>

#### multilayer

```python
@multilayer.setter
def multilayer(value: bool) -> None
```

<a id="unreal.MoviePipelineImageSequenceOutput_BMP"></a>