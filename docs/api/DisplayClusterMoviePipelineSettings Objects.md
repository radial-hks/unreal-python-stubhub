## DisplayClusterMoviePipelineSettings Objects

```python
class DisplayClusterMoviePipelineSettings(MoviePipelineSetting)
```

nDisplay settings for MoviePipeline

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterMoviePipeline
- **File**: DisplayClusterMoviePipelineSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``configuration`` (DisplayClusterMoviePipelineConfiguration):  [Read-Write] Reference to Display Cluster Root Actor
  If not set, the first available in the scene will be set.

<a id="unreal.DisplayClusterMoviePipelineSettings.configuration"></a>

#### configuration

```python
@property
def configuration() -> DisplayClusterMoviePipelineConfiguration
```

(DisplayClusterMoviePipelineConfiguration):  [Read-Write] Reference to Display Cluster Root Actor
If not set, the first available in the scene will be set.

<a id="unreal.DisplayClusterMoviePipelineSettings.configuration"></a>

#### configuration

```python
@configuration.setter
def configuration(value: DisplayClusterMoviePipelineConfiguration) -> None
```

<a id="unreal.DisplayClusterMoviePipelineViewportPassBase"></a>