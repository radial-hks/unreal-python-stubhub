## PCGTransformPointsSettings Objects

```python
class PCGTransformPointsSettings(PCGSettings)
```

PCGTransform Points Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGTransformPoints.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_offset`` (bool):  [Read-Write] Set offset in world space
- ``absolute_rotation`` (bool):  [Read-Write] Set rotation directly instead of additively
- ``absolute_scale`` (bool):  [Read-Write] Set scale directly instead of multiplicatively
- ``apply_to_attribute`` (bool):  [Read-Write]
- ``attribute_name`` (Name):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
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
- ``offset_max`` (Vector):  [Read-Write]
- ``offset_min`` (Vector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``recompute_seed`` (bool):  [Read-Write] Recompute the seed for each new point using its new location
- ``rotation_max`` (Rotator):  [Read-Write]
- ``rotation_min`` (Rotator):  [Read-Write]
- ``scale_max`` (Vector):  [Read-Write]
- ``scale_min`` (Vector):  [Read-Write]
- ``seed`` (int32):  [Read-Write]
- ``uniform_scale`` (bool):  [Read-Write] Scale uniformly on each axis. Uses the X component of ScaleMin and ScaleMax.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGTransformPointsSettings.apply_to_attribute"></a>

#### apply_to_attribute

```python
@property
def apply_to_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.apply_to_attribute"></a>

#### apply_to_attribute

```python
@apply_to_attribute.setter
def apply_to_attribute(value: bool) -> None
```

<a id="unreal.PCGTransformPointsSettings.attribute_name"></a>

#### attribute_name

```python
@property
def attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.attribute_name"></a>

#### attribute_name

```python
@attribute_name.setter
def attribute_name(value: Name) -> None
```

<a id="unreal.PCGTransformPointsSettings.offset_min"></a>

#### offset_min

```python
@property
def offset_min() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.offset_min"></a>

#### offset_min

```python
@offset_min.setter
def offset_min(value: Vector) -> None
```

<a id="unreal.PCGTransformPointsSettings.offset_max"></a>

#### offset_max

```python
@property
def offset_max() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.offset_max"></a>

#### offset_max

```python
@offset_max.setter
def offset_max(value: Vector) -> None
```

<a id="unreal.PCGTransformPointsSettings.absolute_offset"></a>

#### absolute_offset

```python
@property
def absolute_offset() -> bool
```

(bool):  [Read-Write] Set offset in world space

<a id="unreal.PCGTransformPointsSettings.absolute_offset"></a>

#### absolute_offset

```python
@absolute_offset.setter
def absolute_offset(value: bool) -> None
```

<a id="unreal.PCGTransformPointsSettings.rotation_min"></a>

#### rotation_min

```python
@property
def rotation_min() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.rotation_min"></a>

#### rotation_min

```python
@rotation_min.setter
def rotation_min(value: Rotator) -> None
```

<a id="unreal.PCGTransformPointsSettings.rotation_max"></a>

#### rotation_max

```python
@property
def rotation_max() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.rotation_max"></a>

#### rotation_max

```python
@rotation_max.setter
def rotation_max(value: Rotator) -> None
```

<a id="unreal.PCGTransformPointsSettings.absolute_rotation"></a>

#### absolute_rotation

```python
@property
def absolute_rotation() -> bool
```

(bool):  [Read-Write] Set rotation directly instead of additively

<a id="unreal.PCGTransformPointsSettings.absolute_rotation"></a>

#### absolute_rotation

```python
@absolute_rotation.setter
def absolute_rotation(value: bool) -> None
```

<a id="unreal.PCGTransformPointsSettings.scale_min"></a>

#### scale_min

```python
@property
def scale_min() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.scale_min"></a>

#### scale_min

```python
@scale_min.setter
def scale_min(value: Vector) -> None
```

<a id="unreal.PCGTransformPointsSettings.scale_max"></a>

#### scale_max

```python
@property
def scale_max() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGTransformPointsSettings.scale_max"></a>

#### scale_max

```python
@scale_max.setter
def scale_max(value: Vector) -> None
```

<a id="unreal.PCGTransformPointsSettings.absolute_scale"></a>

#### absolute_scale

```python
@property
def absolute_scale() -> bool
```

(bool):  [Read-Write] Set scale directly instead of multiplicatively

<a id="unreal.PCGTransformPointsSettings.absolute_scale"></a>

#### absolute_scale

```python
@absolute_scale.setter
def absolute_scale(value: bool) -> None
```

<a id="unreal.PCGTransformPointsSettings.uniform_scale"></a>

#### uniform_scale

```python
@property
def uniform_scale() -> bool
```

(bool):  [Read-Write] Scale uniformly on each axis. Uses the X component of ScaleMin and ScaleMax.

<a id="unreal.PCGTransformPointsSettings.uniform_scale"></a>

#### uniform_scale

```python
@uniform_scale.setter
def uniform_scale(value: bool) -> None
```

<a id="unreal.PCGTransformPointsSettings.recompute_seed"></a>

#### recompute_seed

```python
@property
def recompute_seed() -> bool
```

(bool):  [Read-Write] Recompute the seed for each new point using its new location

<a id="unreal.PCGTransformPointsSettings.recompute_seed"></a>

#### recompute_seed

```python
@recompute_seed.setter
def recompute_seed(value: bool) -> None
```

<a id="unreal.PCGGetLandscapeSettings"></a>