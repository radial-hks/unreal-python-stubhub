## PCGCombinePointsSettings Objects

```python
class PCGCombinePointsSettings(PCGSettings)
```

Combines each point to share a singular bound extent.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCombinePoints.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``center_pivot`` (bool):  [Read-Write] Places the point at the center of the combined bounds.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``point_transform`` (Transform):  [Read-Write] Transform the point and adjust the bounds.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_first_point_transform`` (bool):  [Read-Write] Use the transform of the initial point.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCombinePointsSettings.center_pivot"></a>

#### center_pivot

```python
@property
def center_pivot() -> bool
```

(bool):  [Read-Write] Places the point at the center of the combined bounds.

<a id="unreal.PCGCombinePointsSettings.center_pivot"></a>

#### center_pivot

```python
@center_pivot.setter
def center_pivot(value: bool) -> None
```

<a id="unreal.PCGCombinePointsSettings.use_first_point_transform"></a>

#### use_first_point_transform

```python
@property
def use_first_point_transform() -> bool
```

(bool):  [Read-Write] Use the transform of the initial point.

<a id="unreal.PCGCombinePointsSettings.use_first_point_transform"></a>

#### use_first_point_transform

```python
@use_first_point_transform.setter
def use_first_point_transform(value: bool) -> None
```

<a id="unreal.PCGCombinePointsSettings.point_transform"></a>

#### point_transform

```python
@property
def point_transform() -> Transform
```

(Transform):  [Read-Write] Transform the point and adjust the bounds.

<a id="unreal.PCGCombinePointsSettings.point_transform"></a>

#### point_transform

```python
@point_transform.setter
def point_transform(value: Transform) -> None
```

<a id="unreal.PCGConvexHull2DSettings"></a>