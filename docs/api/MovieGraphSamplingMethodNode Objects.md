## MovieGraphSamplingMethodNode Objects

```python
class MovieGraphSamplingMethodNode(MovieGraphSettingNode)
```

A node which configures sampling properties for renderers.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSamplingMethodNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_sampling_method_class`` (bool):  [Read-Write]
- ``override_temporal_sample_count`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``temporal_sample_count`` (int32):  [Read-Write] The number of temporal samples which should be taken on one frame. Applies only to linear sampling.

<a id="unreal.MovieGraphSamplingMethodNode.override_sampling_method_class"></a>

#### override_sampling_method_class

```python
@property
def override_sampling_method_class() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphSamplingMethodNode.override_sampling_method_class"></a>

#### override_sampling_method_class

```python
@override_sampling_method_class.setter
def override_sampling_method_class(value: bool) -> None
```

<a id="unreal.MovieGraphSamplingMethodNode.override_temporal_sample_count"></a>

#### override_temporal_sample_count

```python
@property
def override_temporal_sample_count() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphSamplingMethodNode.override_temporal_sample_count"></a>

#### override_temporal_sample_count

```python
@override_temporal_sample_count.setter
def override_temporal_sample_count(value: bool) -> None
```

<a id="unreal.MovieGraphSamplingMethodNode.temporal_sample_count"></a>

#### temporal_sample_count

```python
@property
def temporal_sample_count() -> int
```

(int32):  [Read-Write] The number of temporal samples which should be taken on one frame. Applies only to linear sampling.

<a id="unreal.MovieGraphSamplingMethodNode.temporal_sample_count"></a>

#### temporal_sample_count

```python
@temporal_sample_count.setter
def temporal_sample_count(value: int) -> None
```

<a id="unreal.MovieGraphSelectNode"></a>