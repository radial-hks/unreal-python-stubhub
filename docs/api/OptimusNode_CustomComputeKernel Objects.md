## OptimusNode_CustomComputeKernel Objects

```python
class OptimusNode_CustomComputeKernel(OptimusNode_ComputeKernelBase)
```

Optimus Node Custom Compute Kernel

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusNode_CustomComputeKernel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_sources`` (Array[ComputeSource]):  [Read-Write] Additional source includes.
- ``category`` (Name):  [Read-Write] FIXME: Use drop-down with a preset list + allow custom entry.
- ``execution_domain`` (OptimusExecutionDomain):  [Read-Write] The execution domain that this kernel operates on. The size of the domain is governed by
  the component binding that flows into the primary input group of this kernel.
- ``group_size`` (IntVector):  [Read-Write] Number of threads in a thread group.
  Thread groups have 3 dimensions.
  It's better to have the total threads (X*Y*Z) be a value divisible by 32.
- ``input_binding_array`` (OptimusParameterBindingArray):  [Read-Write] Input bindings. Each one is a function that should be connected to an implementation in a data interface.
- ``input_bindings`` (Array[OptimusParameterBinding]):  [Read-Write] Input bindings. Each one is a function that should be connected to an implementation in a data interface.
  deprecated: Property 'InputBindings' is deprecated.
- ``kernel_name`` (OptimusValidatedName):  [Read-Write] Name of kernel. This is also used as the entry point function name in generated code.
- ``output_binding_array`` (OptimusParameterBindingArray):  [Read-Write] Output bindings. Each one is a function that should be connected to an implementation in a data interface.
- ``output_bindings`` (Array[OptimusParameterBinding]):  [Read-Write] Output bindings. Each one is a function that should be connected to an implementation in a data interface.
  deprecated: Property 'OutputBindings' is deprecated.
- ``parameters`` (Array[Optimus_ShaderBinding]):  [Read-Write]
  deprecated: Property 'Parameters' is deprecated.
- ``secondary_input_binding_groups`` (Array[OptimusSecondaryInputBindingsGroup]):  [Read-Write] Secondary bindings.
- ``shader_source`` (OptimusShaderText):  [Read-Write] The kernel source code.
  If the code contains more than just the kernel entry function, then place the kernel entry function inside a KERNEL {} block.

<a id="unreal.OptimusNode_CustomComputeKernel.parameters"></a>

#### parameters

```python
@property
def parameters() -> Array[Optimus_ShaderBinding]
```

(Array[Optimus_ShaderBinding]):  [Read-Write]
deprecated: Property 'Parameters' is deprecated.

<a id="unreal.OptimusNode_CustomComputeKernel.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: Array[Optimus_ShaderBinding]) -> None
```

<a id="unreal.OptimusNode_CustomComputeKernel.input_bindings"></a>

#### input_bindings

```python
@property
def input_bindings() -> Array[OptimusParameterBinding]
```

(Array[OptimusParameterBinding]):  [Read-Write] Input bindings. Each one is a function that should be connected to an implementation in a data interface.
deprecated: Property 'InputBindings' is deprecated.

<a id="unreal.OptimusNode_CustomComputeKernel.input_bindings"></a>

#### input_bindings

```python
@input_bindings.setter
def input_bindings(value: Array[OptimusParameterBinding]) -> None
```

<a id="unreal.OptimusNode_CustomComputeKernel.output_bindings"></a>

#### output_bindings

```python
@property
def output_bindings() -> Array[OptimusParameterBinding]
```

(Array[OptimusParameterBinding]):  [Read-Write] Output bindings. Each one is a function that should be connected to an implementation in a data interface.
deprecated: Property 'OutputBindings' is deprecated.

<a id="unreal.OptimusNode_CustomComputeKernel.output_bindings"></a>

#### output_bindings

```python
@output_bindings.setter
def output_bindings(value: Array[OptimusParameterBinding]) -> None
```

<a id="unreal.OptimusNode_FunctionReference"></a>