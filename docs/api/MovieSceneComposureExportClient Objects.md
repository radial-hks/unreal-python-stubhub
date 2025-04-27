## MovieSceneComposureExportClient Objects

```python
class MovieSceneComposureExportClient(Interface)
```

Movie Scene Composure Export Client

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: IMovieSceneComposureExportClient.h

<a id="unreal.MovieSceneComposureExportClient.initialize_for_export"></a>

#### initialize_for_export

```python
def initialize_for_export(
        export_initializer: MovieSceneComposureExportInitializer) -> None
```

x.initialize_for_export(export_initializer) -> None
Initialize this object for export by setting up any of the necessary scene view extensions with the specified initializer.

Args:
    export_initializer (MovieSceneComposureExportInitializer):

<a id="unreal.MovieSceneComposureExportInitializer"></a>