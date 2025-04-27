## MovieSceneComposureExportPass Objects

```python
class MovieSceneComposureExportPass(StructBase)
```

Export configuration options for a single internal pass on an ACompositingElement, or its output pass (where TransformPassName is None)

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: MovieSceneComposureExportTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exported_as`` (Name):  [Read-Write] The name to use for this pass when rendering out
- ``rename_pass`` (bool):  [Read-Write] Whether to rename this pass when rendering out
- ``transform_pass_name`` (Name):  [Read-Write] The name of the transform pass in the comp to export. None signifies the element's output.

<a id="unreal.MovieSceneComposureExportPass.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.GenerateStaticMeshLODProcess_PreprocessSettings"></a>