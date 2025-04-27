## PCGDebugVisualizationSettings Objects

```python
class PCGDebugVisualizationSettings(StructBase)
```

PCGDebug Visualization Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDebug.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_override`` (MaterialInterface):  [Read-Write]
- ``point_mesh`` (StaticMesh):  [Read-Write]
- ``point_scale`` (float):  [Read-Write]
- ``scale_method`` (PCGDebugVisScaleMethod):  [Read-Write]

<a id="unreal.PCGDebugVisualizationSettings.__init__"></a>

#### __init__

```python
def __init__(
        point_scale: float = 0.000000,
        scale_method: PCGDebugVisScaleMethod = PCGDebugVisScaleMethod.RELATIVE,
        point_mesh: StaticMesh = None,
        material_override: MaterialInterface = None) -> None
```

<a id="unreal.PCGDebugVisualizationSettings.point_scale"></a>

#### point_scale

```python
@property
def point_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGDebugVisualizationSettings.point_scale"></a>

#### point_scale

```python
@point_scale.setter
def point_scale(value: float) -> None
```

<a id="unreal.PCGDebugVisualizationSettings.scale_method"></a>

#### scale_method

```python
@property
def scale_method() -> PCGDebugVisScaleMethod
```

(PCGDebugVisScaleMethod):  [Read-Write]

<a id="unreal.PCGDebugVisualizationSettings.scale_method"></a>

#### scale_method

```python
@scale_method.setter
def scale_method(value: PCGDebugVisScaleMethod) -> None
```

<a id="unreal.PCGDebugVisualizationSettings.point_mesh"></a>

#### point_mesh

```python
@property
def point_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.PCGDebugVisualizationSettings.point_mesh"></a>

#### point_mesh

```python
@point_mesh.setter
def point_mesh(value: StaticMesh) -> None
```

<a id="unreal.PCGDebugVisualizationSettings.material_override"></a>

#### material_override

```python
@property
def material_override() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.PCGDebugVisualizationSettings.material_override"></a>

#### material_override

```python
@material_override.setter
def material_override(value: MaterialInterface) -> None
```

<a id="unreal.PCGPoint"></a>