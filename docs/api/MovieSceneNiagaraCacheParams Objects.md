## MovieSceneNiagaraCacheParams Objects

```python
class MovieSceneNiagaraCacheParams(MovieSceneBaseCacheParams)
```

Movie Scene Niagara Cache Params

**C++ Source:**

- **Plugin**: NiagaraSimCaching
- **Module**: NiagaraSimCaching
- **File**: MovieSceneNiagaraCacheSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_parameters`` (NiagaraSimCacheCreateParameters):  [Read-Write]
- ``cache_replay_play_mode`` (NiagaraSimCacheSectionPlayMode):  [Read-Write] What should the effect do when the track has no cache data to display
- ``end_frame_offset`` (FrameNumber):  [Read-Write] The offset into the end of the animation clip
- ``first_loop_start_frame_offset`` (FrameNumber):  [Read-Write] The offset for the first loop of the animation clip
- ``lock_cache_to_read_only`` (bool):  [Read-Write] If true then the section properties might still be changed (so the section itself is not locked), but the cache cannot be rerecorded to prevent accidentally overriding the data within
- ``override_quality_level`` (bool):  [Read-Write]
- ``play_rate`` (float):  [Read-Write] The playback rate of the animation clip
- ``record_quality_level`` (PerQualityLevels):  [Read-Write] If set, then the engine scalability setting will be overriden with this value when recording a new cache for this track
- ``reverse`` (bool):  [Read-Write] Reverse the playback of the animation clip
- ``section_stretch_mode`` (NiagaraSimCacheSectionStretchMode):  [Read-Write] What should the effect do when the cache section is stretched?
- ``sim_cache`` (NiagaraSimCache):  [Read-Write] The sim cache this section plays and records into
- ``start_frame_offset`` (FrameNumber):  [Read-Write] The offset into the beginning of the animation clip

<a id="unreal.MovieSceneNiagaraCacheParams.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.WaveTableBankEntry"></a>