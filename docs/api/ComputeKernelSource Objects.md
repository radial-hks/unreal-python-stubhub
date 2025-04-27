## ComputeKernelSource Objects

```python
class ComputeKernelSource(Object)
```

Class representing the source for a UComputeKernel
We derive from this for each authoring mechanism. (HLSL text, VPL graph, ML Meta Lang, etc.)

**C++ Source:**

- **Plugin**: ComputeFramework
- **Module**: ComputeFramework
- **File**: ComputeKernelSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_sources`` (Array[ComputeSource]):  [Read-Write] An array of additional independent source assets that the kernel source depends on.
- ``definitions_set`` (ComputeKernelDefinitionSet):  [Read-Only] Base environment defines for kernel compilation. These will be extended by further defines declared in any linked data providers.
- ``entry_point`` (str):  [Read-Only] Kernel entry point.
- ``external_inputs`` (Array[ShaderFunctionDefinition]):  [Read-Only] Named external inputs for the kernel. These must be fulfilled by linked data providers.
- ``external_outputs`` (Array[ShaderFunctionDefinition]):  [Read-Only] Named external outputs for the kernel. These must be fulfilled by linked data providers.
- ``group_size`` (IntVector):  [Read-Only] Kernel group size.
- ``permutation_set`` (ComputeKernelPermutationSet):  [Read-Only] Base permutations exposed by the kernel. These will be extended by further permutations declared in any linked data providers.

<a id="unreal.ComputeKernelFromText"></a>