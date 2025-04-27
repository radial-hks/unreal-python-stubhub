## MovieGraphWarmUpSettingNode Objects

```python
class MovieGraphWarmUpSettingNode(MovieGraphSettingNode)
```

Movie Graph Warm Up Setting Node

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphWarmUpSettingNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``emulate_motion_blur`` (bool):  [Read-Write] If true, we will evaluate frame 0, and then wait NumWarmUpFrames frames, rendering each one as we go. Then we will evaluate frame 1, and then frame 0 again. This emulates motion blur on the first frame (which normally needs data before frame 0). If false, we will "walk" towards the first frame of the shot, starting NumWarmUpFrames before the shot normally starts.
- ``num_warm_up_frames`` (int32):  [Read-Write] At the start of each shot, how many frames should we run the engine (without writing renders to disk) to warm up various systems.
- ``override_b_emulate_motion_blur`` (bool):  [Read-Write]
- ``override_num_warm_up_frames`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphWarmUpSettingNode.override_num_warm_up_frames"></a>

#### override_num_warm_up_frames

```python
@property
def override_num_warm_up_frames() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphWarmUpSettingNode.override_num_warm_up_frames"></a>

#### override_num_warm_up_frames

```python
@override_num_warm_up_frames.setter
def override_num_warm_up_frames(value: bool) -> None
```

<a id="unreal.MovieGraphWarmUpSettingNode.override_b_emulate_motion_blur"></a>

#### override_b_emulate_motion_blur

```python
@property
def override_b_emulate_motion_blur() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphWarmUpSettingNode.override_b_emulate_motion_blur"></a>

#### override_b_emulate_motion_blur

```python
@override_b_emulate_motion_blur.setter
def override_b_emulate_motion_blur(value: bool) -> None
```

<a id="unreal.MovieGraphWarmUpSettingNode.num_warm_up_frames"></a>

#### num_warm_up_frames

```python
@property
def num_warm_up_frames() -> int
```

(int32):  [Read-Write] At the start of each shot, how many frames should we run the engine (without writing renders to disk) to warm up various systems.

<a id="unreal.MovieGraphWarmUpSettingNode.num_warm_up_frames"></a>

#### num_warm_up_frames

```python
@num_warm_up_frames.setter
def num_warm_up_frames(value: int) -> None
```

<a id="unreal.MovieGraphWarmUpSettingNode.emulate_motion_blur"></a>

#### emulate_motion_blur

```python
@property
def emulate_motion_blur() -> bool
```

(bool):  [Read-Write] If true, we will evaluate frame 0, and then wait NumWarmUpFrames frames, rendering each one as we go. Then we will evaluate frame 1, and then frame 0 again. This emulates motion blur on the first frame (which normally needs data before frame 0). If false, we will "walk" towards the first frame of the shot, starting NumWarmUpFrames before the shot normally starts.

<a id="unreal.MovieGraphWarmUpSettingNode.emulate_motion_blur"></a>

#### emulate_motion_blur

```python
@emulate_motion_blur.setter
def emulate_motion_blur(value: bool) -> None
```

<a id="unreal.MovieJobVariableAssignmentContainer"></a>