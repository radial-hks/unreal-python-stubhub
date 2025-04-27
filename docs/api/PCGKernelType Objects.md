## PCGKernelType Objects

```python
class PCGKernelType(EnumBase)
```

Type of kernel allows us to make decisions about execution automatically, streamlining authoring.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCustomHLSL.h

<a id="unreal.PCGKernelType.POINT_PROCESSOR"></a>

#### POINT_PROCESSOR

0: Kernel executes on each point in first input pin.

<a id="unreal.PCGKernelType.POINT_GENERATOR"></a>

#### POINT_GENERATOR

1: Kernel executes for fixed number of points, configurable on node.

<a id="unreal.PCGKernelType.CUSTOM"></a>

#### CUSTOM

2: Execution thread counts and output buffer sizes configurable on node. All data read/write indices must be manually bounds checked.

<a id="unreal.PCGDispatchThreadCount"></a>