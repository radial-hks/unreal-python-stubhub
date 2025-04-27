## MovieSceneNiagaraEmitterSection Objects

```python
class MovieSceneNiagaraEmitterSection(MovieSceneNiagaraEmitterSectionBase)
```

Niagara editor movie scene section; represents one emitter in the timeline

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraEditor
- **File**: MovieSceneNiagaraEmitterSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``num_loops`` (int32):  [Read-Write]
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``start_time_included_in_first_loop_only`` (bool):  [Read-Write]
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.NiagaraPythonScriptModuleInput"></a>