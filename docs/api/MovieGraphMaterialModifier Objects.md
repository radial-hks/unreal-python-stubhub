## MovieGraphMaterialModifier Objects

```python
class MovieGraphMaterialModifier(MovieGraphCollectionModifier)
```

Modifies actor materials.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material`` (MaterialInterface):  [Read-Write]
- ``override_material`` (bool):  [Read-Write]

<a id="unreal.MovieGraphMaterialModifier.override_material"></a>

#### override_material

```python
@property
def override_material() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphMaterialModifier.override_material"></a>

#### override_material

```python
@override_material.setter
def override_material(value: bool) -> None
```

<a id="unreal.MovieGraphMaterialModifier.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.MovieGraphMaterialModifier.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.MovieGraphMaterialModifier.undo_modifier"></a>

#### undo_modifier

```python
def undo_modifier() -> None
```

x.undo_modifier() -> None
Undo Modifier

<a id="unreal.MovieGraphMaterialModifier.set_material"></a>

#### set_material

```python
def set_material(material: MaterialInterface) -> None
```

x.set_material(material) -> None
Set Material

Args:
    material (MaterialInterface):

<a id="unreal.MovieGraphMaterialModifier.apply_modifier"></a>

#### apply_modifier

```python
def apply_modifier(world: World) -> None
```

x.apply_modifier(world) -> None
Apply Modifier

Args:
    world (World):

<a id="unreal.MoviePipelineMaterialModifier"></a>