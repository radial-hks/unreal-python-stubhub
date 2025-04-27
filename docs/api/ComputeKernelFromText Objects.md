## ComputeKernelFromText Objects

```python
class ComputeKernelFromText(ComputeKernelSource)
```

Class responsible for loading HLSL text and parsing the options available.

**C++ Source:**

- **Plugin**: ComputeFramework
- **Module**: ComputeFramework
- **File**: ComputeKernelFromText.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_sources`` (Array[ComputeSource]):  [Read-Write] An array of additional independent source assets that the kernel source depends on.
- ``definitions_set`` (ComputeKernelDefinitionSet):  [Read-Only] Base environment defines for kernel compilation. These will be extended by further defines declared in any linked data providers.
- ``entry_point`` (str):  [Read-Only] Kernel entry point.
- ``external_inputs`` (Array[ShaderFunctionDefinition]):  [Read-Only] Named external inputs for the kernel. These must be fulfilled by linked data providers.
- ``external_outputs`` (Array[ShaderFunctionDefinition]):  [Read-Only] Named external outputs for the kernel. These must be fulfilled by linked data providers.
- ``group_size`` (IntVector):  [Read-Only] Kernel group size.
- ``permutation_set`` (ComputeKernelPermutationSet):  [Read-Only] Base permutations exposed by the kernel. These will be extended by further permutations declared in any linked data providers.
- ``source_file`` (FilePath):  [Read-Write] Filepath to the source file containing the kernel entry points and all options for parsing.

<a id="unreal.ComputeSource"></a>