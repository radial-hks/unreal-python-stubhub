## ProceduralFoliageComponent Objects

```python
class ProceduralFoliageComponent(ActorComponent)
```

Procedural Foliage Component

**C++ Source:**

- **Module**: Foliage
- **File**: ProceduralFoliageComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_bsp`` (bool):  [Read-Write] Whether to place foliage on BSP
- ``allow_foliage`` (bool):  [Read-Write] Whether to place foliage on other blocking foliage geometry
- ``allow_landscape`` (bool):  [Read-Write] Whether to place foliage on landscape
- ``allow_static_mesh`` (bool):  [Read-Write] Whether to place foliage on StaticMesh
- ``allow_translucent`` (bool):  [Read-Write] Whether to place foliage on translucent geometry
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``foliage_spawner`` (ProceduralFoliageSpawner):  [Read-Write] The procedural foliage spawner used to generate foliage instances within this volume.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``show_debug_tiles`` (bool):  [Read-Write] Whether to visualize the tiles used for the foliage spawner simulation
- ``tile_overlap`` (float):  [Read-Write] The amount of overlap between simulation tiles (in cm).

<a id="unreal.ProceduralFoliageComponent.foliage_spawner"></a>

#### foliage_spawner

```python
@property
def foliage_spawner() -> ProceduralFoliageSpawner
```

(ProceduralFoliageSpawner):  [Read-Write] The procedural foliage spawner used to generate foliage instances within this volume.

<a id="unreal.ProceduralFoliageComponent.foliage_spawner"></a>

#### foliage_spawner

```python
@foliage_spawner.setter
def foliage_spawner(value: ProceduralFoliageSpawner) -> None
```

<a id="unreal.ProceduralFoliageComponent.procedural_foliage"></a>

#### procedural_foliage

```python
@property
def procedural_foliage() -> ProceduralFoliageSpawner
```

deprecated: 'procedural_foliage' was renamed to 'foliage_spawner'.

<a id="unreal.ProceduralFoliageComponent.procedural_foliage"></a>

#### procedural_foliage

```python
@procedural_foliage.setter
def procedural_foliage(value: ProceduralFoliageSpawner) -> None
```

<a id="unreal.ProceduralFoliageComponent.tile_overlap"></a>

#### tile_overlap

```python
@property
def tile_overlap() -> float
```

(float):  [Read-Write] The amount of overlap between simulation tiles (in cm).

<a id="unreal.ProceduralFoliageComponent.tile_overlap"></a>

#### tile_overlap

```python
@tile_overlap.setter
def tile_overlap(value: float) -> None
```

<a id="unreal.ProceduralFoliageComponent.overlap"></a>

#### overlap

```python
@property
def overlap() -> float
```

deprecated: 'overlap' was renamed to 'tile_overlap'.

<a id="unreal.ProceduralFoliageComponent.overlap"></a>

#### overlap

```python
@overlap.setter
def overlap(value: float) -> None
```

<a id="unreal.ProceduralFoliageComponent.allow_landscape"></a>

#### allow_landscape

```python
@property
def allow_landscape() -> bool
```

(bool):  [Read-Write] Whether to place foliage on landscape

<a id="unreal.ProceduralFoliageComponent.allow_landscape"></a>

#### allow_landscape

```python
@allow_landscape.setter
def allow_landscape(value: bool) -> None
```

<a id="unreal.ProceduralFoliageComponent.allow_bsp"></a>

#### allow_bsp

```python
@property
def allow_bsp() -> bool
```

(bool):  [Read-Write] Whether to place foliage on BSP

<a id="unreal.ProceduralFoliageComponent.allow_bsp"></a>

#### allow_bsp

```python
@allow_bsp.setter
def allow_bsp(value: bool) -> None
```

<a id="unreal.ProceduralFoliageComponent.allow_static_mesh"></a>

#### allow_static_mesh

```python
@property
def allow_static_mesh() -> bool
```

(bool):  [Read-Write] Whether to place foliage on StaticMesh

<a id="unreal.ProceduralFoliageComponent.allow_static_mesh"></a>

#### allow_static_mesh

```python
@allow_static_mesh.setter
def allow_static_mesh(value: bool) -> None
```

<a id="unreal.ProceduralFoliageComponent.allow_translucent"></a>

#### allow_translucent

```python
@property
def allow_translucent() -> bool
```

(bool):  [Read-Write] Whether to place foliage on translucent geometry

<a id="unreal.ProceduralFoliageComponent.allow_translucent"></a>

#### allow_translucent

```python
@allow_translucent.setter
def allow_translucent(value: bool) -> None
```

<a id="unreal.ProceduralFoliageComponent.allow_foliage"></a>

#### allow_foliage

```python
@property
def allow_foliage() -> bool
```

(bool):  [Read-Write] Whether to place foliage on other blocking foliage geometry

<a id="unreal.ProceduralFoliageComponent.allow_foliage"></a>

#### allow_foliage

```python
@allow_foliage.setter
def allow_foliage(value: bool) -> None
```

<a id="unreal.ProceduralFoliageComponent.show_debug_tiles"></a>

#### show_debug_tiles

```python
@property
def show_debug_tiles() -> bool
```

(bool):  [Read-Write] Whether to visualize the tiles used for the foliage spawner simulation

<a id="unreal.ProceduralFoliageComponent.show_debug_tiles"></a>

#### show_debug_tiles

```python
@show_debug_tiles.setter
def show_debug_tiles(value: bool) -> None
```

<a id="unreal.ProceduralFoliageSpawner"></a>