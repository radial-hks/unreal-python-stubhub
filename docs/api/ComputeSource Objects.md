## ComputeSource Objects

```python
class ComputeSource(Object)
```

Class representing some source for inclusion in a UComputeKernel.
We derive from this for each authoring mechanism. (HLSL text, VPL graph, ML Meta Lang, etc.)

**C++ Source:**

- **Plugin**: ComputeFramework
- **Module**: ComputeFramework
- **File**: ComputeSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_sources`` (Array[ComputeSource]):  [Read-Write] Array of additional source objects. This allows us to specify source dependencies.

<a id="unreal.ComputeSourceFromText"></a>