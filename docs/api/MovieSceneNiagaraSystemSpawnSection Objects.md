## MovieSceneNiagaraSystemSpawnSection Objects

```python
class MovieSceneNiagaraSystemSpawnSection(MovieSceneSection)
```

Movie Scene Niagara System Spawn Section

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: MovieSceneNiagaraSystemSpawnSection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``age_update_mode`` (NiagaraAgeUpdateMode):  [Read-Write] Specifies how sequencer should update the age of the controlled niagara system.
- ``allow_scalability`` (bool):  [Read-Write]
- ``color_tint`` (Color):  [Read-Write] The color tint for this section
- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this section evaluates at runtime.
- ``easing`` (MovieSceneEasingSettings):  [Read-Write]
- ``eval_options`` (MovieSceneSectionEvalOptions):  [Read-Write]
- ``is_active`` (bool):  [Read-Write] Toggle whether this section is active/inactive
- ``is_locked`` (bool):  [Read-Write] Toggle whether this section is locked/unlocked
- ``post_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to continue 'postrolling' this section for after evaluation has ended.
- ``pre_roll_frames`` (FrameNumber):  [Read-Write] The amount of time to prepare this section for evaluation before it actually starts.
- ``section_end_behavior`` (NiagaraSystemSpawnSectionEndBehavior):  [Read-Write] Specifies what should happen to the niagara system when section evaluation finishes.
- ``section_evaluate_behavior`` (NiagaraSystemSpawnSectionEvaluateBehavior):  [Read-Write] Specifies what should happen to the niagara system when section is evaluating from the 2nd frame until the last frame.
- ``section_range`` (MovieSceneFrameRange):  [Read-Write] The range in which this section is active
- ``section_start_behavior`` (NiagaraSystemSpawnSectionStartBehavior):  [Read-Write] Specifies what should happen to the niagara system from before the section evaluates up until the first frame of the section.
- ``timecode_source`` (MovieSceneTimecodeSource):  [Read-Write] The timecode at which this movie scene section is based (ie. when it was recorded)

<a id="unreal.MovieSceneNiagaraTrack"></a>