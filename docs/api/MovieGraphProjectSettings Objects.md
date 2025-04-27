## MovieGraphProjectSettings Objects

```python
class MovieGraphProjectSettings(DeveloperSettings)
```

Settings that apply to the Movie Graph.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphProjectSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_named_resolutions`` (Array[MovieGraphNamedResolution]):  [Read-Write] A list of default resolutions to render with, defined in Config/BaseMovieRenderPipeline.ini or Project Settings.
  These resolutions will appear in the MovieGraph's various output settings nodes.

<a id="unreal.MovieGraphRemoveRenderSettingNode"></a>