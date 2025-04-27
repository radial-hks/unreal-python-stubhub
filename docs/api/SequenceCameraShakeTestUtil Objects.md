## SequenceCameraShakeTestUtil Objects

```python
class SequenceCameraShakeTestUtil(BlueprintFunctionLibrary)
```

Sequence Camera Shake Test Util

**C++ Source:**

- **Plugin**: TemplateSequence
- **Module**: TemplateSequence
- **File**: SequenceCameraShakeTestUtil.h

<a id="unreal.SequenceCameraShakeTestUtil.get_post_process_blend_cache"></a>

#### get_post_process_blend_cache

```python
@classmethod
def get_post_process_blend_cache(
        cls, player_controller: PlayerController,
        pp_index: int) -> Optional[Tuple[PostProcessSettings, float]]
```

X.get_post_process_blend_cache(player_controller, pp_index) -> (out_pp_settings=PostProcessSettings, out_pp_blend_weight=float) or None
Get Post Process Blend Cache

Args:
    player_controller (PlayerController): 
    pp_index (int32): 

Returns:
    tuple or None: 

    out_pp_settings (PostProcessSettings): 

    out_pp_blend_weight (float):

<a id="unreal.SequenceCameraShakeTestUtil.get_last_frame_camera_cache_pov"></a>

#### get_last_frame_camera_cache_pov

```python
@classmethod
def get_last_frame_camera_cache_pov(
        cls, player_controller: PlayerController) -> MinimalViewInfo
```

X.get_last_frame_camera_cache_pov(player_controller) -> MinimalViewInfo
Get Last Frame Camera Cache POV

Args:
    player_controller (PlayerController): 

Returns:
    MinimalViewInfo:

<a id="unreal.SequenceCameraShakeTestUtil.get_camera_cache_pov"></a>

#### get_camera_cache_pov

```python
@classmethod
def get_camera_cache_pov(
        cls, player_controller: PlayerController) -> MinimalViewInfo
```

X.get_camera_cache_pov(player_controller) -> MinimalViewInfo
Get Camera Cache POV

Args:
    player_controller (PlayerController): 

Returns:
    MinimalViewInfo:

<a id="unreal.TemplateSequenceTrack"></a>