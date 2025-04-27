## MovieGraphImageSequenceOutputNode_MultiLayerEXR Objects

```python
class MovieGraphImageSequenceOutputNode_MultiLayerEXR(
        MovieGraphImageSequenceOutputNode_EXR)
```

Image sequence output node that can write multi-layer EXR files.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MovieGraphImageSequenceOutputNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compression`` (EXRCompressionFormat):  [Read-Write] Which compression method should the resulting EXR file be compressed with.
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``file_name_format`` (str):  [Read-Write] What format string should the final files use? Can include folder prefixes, and format string ({shot_name}, etc.)
- ``ocio_configuration`` (OpenColorIODisplayConfiguration):  [Read-Write] OCIO configuration/transform settings.

  Note: There are differences from the previous implementation in MRQ given that we are now doing CPU-side processing.
  1) This feature only works on desktop platforms when the OpenColorIO library is available.
  2) Users are now responsible for setting the renderer output space to Final Color (HDR) in Linear Working Color Space (SCS_FinalColorHDR).
- ``ocio_context`` (Map[str, str]):  [Read-Write] OCIO context of key-value string pairs, typically used to apply shot-specific looks (such as a CDL color correction, or a 1D grade LUT).

  Notes:
  1) If a configuration asset base context was set, it remains active but can be overridden here with new key-values.
  2) Format tokens such as {shot_name} are supported and will get resolved before submission.
- ``override_compression`` (bool):  [Read-Write]
- ``override_file_name_format`` (bool):  [Read-Write]
- ``override_ocio_configuration`` (bool):  [Read-Write] ~UMovieGraphFileOutputNode Interface
- ``override_ocio_context`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphImageSequenceOutputNode_BMP"></a>