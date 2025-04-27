## ComputeKernel Objects

```python
class ComputeKernel(Object)
```

Base class representing a kernel that will be run as a shader on the GPU.

**C++ Source:**

- **Plugin**: ComputeFramework
- **Module**: ComputeFramework
- **File**: ComputeKernel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``kernel_flags`` (int32):  [Read-Only] Specifying certain memory access flags allows for optimizations such as kernel fusing.
- ``kernel_source`` (ComputeKernelSource):  [Read-Write] The compute kernel source asset.
  A kernel's source may be authored by different mechanisms; e.g. HLSL text, VPL graph, ML Meta Lang, etc

<a id="unreal.ComputeKernel.kernel_flags"></a>

#### kernel_flags

```python
@property
def kernel_flags() -> int
```

(int32):  [Read-Only] Specifying certain memory access flags allows for optimizations such as kernel fusing.

<a id="unreal.ComputeKernelSource"></a>