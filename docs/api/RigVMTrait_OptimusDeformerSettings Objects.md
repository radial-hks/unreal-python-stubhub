## RigVMTrait_OptimusDeformerSettings Objects

```python
class RigVMTrait_OptimusDeformerSettings(RigVMTrait)
```

Rig VMTrait Optimus Deformer Settings

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: RigUnit_Optimus.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``deform_child_components`` (bool):  [Read-Write] Whether to apply the deformer to all child components as well
- ``exclude_child_components_with_tag`` (Name):  [Read-Write] Deformer won't be applied to child components that have the specified component tag
- ``execution_group`` (int32):  [Read-Write] Deformers are first sorted by execution group index, then by the order in which they are added
- ``execution_phase`` (OptimusDeformerExecutionPhase):  [Read-Write]

<a id="unreal.RigVMTrait_OptimusDeformerSettings.__init__"></a>

#### __init__

```python
def __init__(execution_phase:
             OptimusDeformerExecutionPhase = OptimusDeformerExecutionPhase.
             AFTER_DEFAULT_DEFORMER,
             execution_group: int = 0,
             deform_child_components: bool = False,
             exclude_child_components_with_tag: Name = "None") -> None
```

<a id="unreal.RigVMTrait_OptimusDeformerSettings.execution_phase"></a>

#### execution_phase

```python
@property
def execution_phase() -> OptimusDeformerExecutionPhase
```

(OptimusDeformerExecutionPhase):  [Read-Write]

<a id="unreal.RigVMTrait_OptimusDeformerSettings.execution_phase"></a>

#### execution_phase

```python
@execution_phase.setter
def execution_phase(value: OptimusDeformerExecutionPhase) -> None
```

<a id="unreal.RigVMTrait_OptimusDeformerSettings.execution_group"></a>

#### execution_group

```python
@property
def execution_group() -> int
```

(int32):  [Read-Write] Deformers are first sorted by execution group index, then by the order in which they are added

<a id="unreal.RigVMTrait_OptimusDeformerSettings.execution_group"></a>

#### execution_group

```python
@execution_group.setter
def execution_group(value: int) -> None
```

<a id="unreal.RigVMTrait_OptimusDeformerSettings.deform_child_components"></a>

#### deform_child_components

```python
@property
def deform_child_components() -> bool
```

(bool):  [Read-Write] Whether to apply the deformer to all child components as well

<a id="unreal.RigVMTrait_OptimusDeformerSettings.deform_child_components"></a>

#### deform_child_components

```python
@deform_child_components.setter
def deform_child_components(value: bool) -> None
```

<a id="unreal.RigVMTrait_OptimusDeformerSettings.exclude_child_components_with_tag"></a>

#### exclude_child_components_with_tag

```python
@property
def exclude_child_components_with_tag() -> Name
```

(Name):  [Read-Write] Deformer won't be applied to child components that have the specified component tag

<a id="unreal.RigVMTrait_OptimusDeformerSettings.exclude_child_components_with_tag"></a>

#### exclude_child_components_with_tag

```python
@exclude_child_components_with_tag.setter
def exclude_child_components_with_tag(value: Name) -> None
```

<a id="unreal.RigUnit_AddOptimusDeformer"></a>