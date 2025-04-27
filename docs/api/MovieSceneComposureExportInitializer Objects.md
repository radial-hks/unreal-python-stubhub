## MovieSceneComposureExportInitializer Objects

```python
class MovieSceneComposureExportInitializer(Object)
```

Object passed to comp shot elements to initialize them for export.
Currenly only allows scene captures to initialize a new extension that can capture GBuffers and other buffer visualization targets

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: MovieSceneComposureExportSectionTemplate.h

<a id="unreal.MovieSceneComposureExportInitializer.export_scene_capture_buffers"></a>

#### export_scene_capture_buffers

```python
def export_scene_capture_buffers(comp_shot_element: CompositingElement,
                                 scene_capture: SceneCaptureComponent2D,
                                 buffers_to_export: Array[str]) -> None
```

x.export_scene_capture_buffers(comp_shot_element, scene_capture, buffers_to_export) -> None
Initialize the export to capture the specified named buffer visualization targets from a scene capture

Args:
    comp_shot_element (CompositingElement): 
    scene_capture (SceneCaptureComponent2D): 
    buffers_to_export (Array[str]):

<a id="unreal.MovieSceneComposureExportTrack"></a>