## ComputeSourceFromText Objects

```python
class ComputeSourceFromText(ComputeSource)
```

Class responsible for loading HLSL text and parsing any metadata available.

**C++ Source:**

- **Plugin**: ComputeFramework
- **Module**: ComputeFramework
- **File**: ComputeSourceFromText.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_sources`` (Array[ComputeSource]):  [Read-Write] Array of additional source objects. This allows us to specify source dependencies.
- ``source_file`` (FilePath):  [Read-Write] Filepath to the source file containing the kernel entry points and all options for parsing.

<a id="unreal.LevelVariantSets"></a>