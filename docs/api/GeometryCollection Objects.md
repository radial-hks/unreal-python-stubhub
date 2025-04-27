## GeometryCollection Objects

```python
class GeometryCollection(Object)
```

UGeometryCollectionObject (UObject)

UObject wrapper for the FGeometryCollection

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Write] Importing data and options used for this geometry collection
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``auto_instance_meshes`` (Array[GeometryCollectionAutoInstanceMesh]):  [Read-Write] List of unique static mesh / materials pairs for auto instancing.
- ``auto_instance_transform_remap_indices`` (Array[int32]):  [Read-Only] cache transform remapping for instanced meshes indices
- ``breadth_first_transform_indices`` (Array[int32]):  [Read-Only] cache transform indices in breadth-first order
- ``cluster_connection_type`` (ClusterConnectionTypeEnum):  [Read-Write]
- ``cluster_group_index`` (int32):  [Read-Write] Maximum level for cluster breaks.
- ``collision_object_reduction_percentage`` (float):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``collision_particles_fraction`` (float):  [Read-Write] Number of particles on the triangulated surface to use for collisions.
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``collision_type`` (CollisionTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``connection_graph_bounds_filtering_margin`` (float):  [Read-Write]
- ``convert_vertex_colors_to_srgb`` (bool):  [Read-Write] Convert vertex colors to sRGB for rendering. Exposed to avoid changing vertex color rendering for legacy assets; should typically be true for new geometry collections.
- ``custom_renderer_type`` (type(Class)):  [Read-Write] Custom class type that will be used to render the geometry collection instead of using the native rendering.
- ``damage_model`` (DamageModelTypeEnum):  [Read-Write] Damage model to use for evaluating destruction.
- ``damage_propagation_data`` (GeometryCollectionDamagePropagationData):  [Read-Write] Data about how damage propagation shoudl behave.
- ``damage_threshold`` (Array[float]):  [Read-Write] Damage threshold for clusters at different levels.
- ``dataflow_asset`` (Dataflow):  [Read-Write] Dataflow
- ``dataflow_terminal`` (str):  [Read-Write]
- ``density_from_physics_material`` (bool):  [Read-Write] Whether to use density ( for mass computation ) from physics material ( if physics material is not set, use the component one or defaults )
- ``embedded_geometry_exemplar`` (Array[GeometryCollectionEmbeddedExemplar]):  [Read-Write] References for embedded geometry generation
- ``enable_clustering`` (bool):  [Read-Write]
- ``enable_nanite`` (bool):  [Read-Write] Enable support for Nanite.
- ``enable_nanite_fallback`` (bool):  [Read-Write] Enable Non-Nanite fallback mesh when Nanite support is enabled.
- ``enable_remove_pieces_on_fracture`` (bool):  [Read-Write] Enable remove pieces on fracture
  deprecated: Use remove on break feature instead ( Fracture editor tools ).
- ``geometry_source`` (Array[GeometryCollectionSource]):  [Read-Write]
- ``implicit_type`` (ImplicitTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``import_collision_from_source`` (bool):  [Read-Write] whether to import collision from the source asset
- ``mass`` (float):  [Read-Write] Total Mass of Collection. If density, units are in kg/m^3 ( only enabled if physics material is not set )
- ``mass_as_density`` (bool):  [Read-Write] Mass As Density, units are in kg/m^3 ( only enabled if physics material is not set )
- ``materials`` (Array[MaterialInterface]):  [Read-Write]
- ``max_cluster_level`` (int32):  [Read-Write] Maximum level for cluster breaks.
- ``max_cluster_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``max_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``maximum_collision_particles`` (int32):  [Read-Write] Max number of particles.
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``maximum_sleep_time`` (Vector2D):  [Read-Write] How long may the particle sleep before initiating removal (in seconds).
- ``min_cluster_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``min_level_set_resolution`` (int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
  deprecated: This property is deprecated. Use the default SizeSpecificData instead.
- ``minimum_mass_clamp`` (float):  [Read-Write] Smallest allowable mass (def:0.1)
- ``optimize_convexes`` (bool):  [Read-Write] whether to optimize convexes for collisions. If true the convex optimizer will generate at runtime one
  single convex shape for physics collisions ignoring all the user defined ones.
  Enable p.Chaos.Convex.SimplifyUnion cvar to be able to use it (experimental)
- ``overrides`` (Map[str, str]):  [Read-Write]
- ``per_cluster_only_damage_threshold`` (bool):  [Read-Write] compatibility check, when true, only cluster compute damage from parameters and propagate to direct children
  when false, each child will compute it's damage threshold allowing for more precise and intuitive destruction behavior
- ``physics_material`` (PhysicalMaterial):  [Read-Write] Physics material to use for the geometry collection
- ``removal_duration`` (Vector2D):  [Read-Write] How long does the removal process take (in seconds).
- ``remove_on_fracture_materials`` (Array[MaterialInterface]):  [Read-Write] Materials relating to remove on fracture
  deprecated: Use remove on break feature instead ( Fracture editor tools ).
- ``remove_on_max_sleep`` (bool):  [Read-Write] Remove particle from simulation and dissolve rendered geometry once sleep threshold has been exceeded.
- ``root_index`` (int32):  [Read-Only] cached root index for faster queries
- ``root_proxy`` (SoftObjectPath):  [Read-Write] static mesh to use as a proxy for rendering until the geometry collection is broken
  deprecated: This property is deprecated. Use RootProxyData instead.
- ``root_proxy_data`` (GeometryCollectionProxyMeshData):  [Read-Write] Static mesh to use as a proxy for rendering until the geometry collection is broken.
- ``scale_on_removal`` (bool):  [Read-Write] When enabled, particle will scale down (shrink) when using being removed ( using both remove on sleep or remove on break ) - Enabled by default
- ``size_specific_data`` (Array[GeometryCollectionSizeSpecificData]):  [Read-Write] * Size Specfic Data reflects the default geometry to bind to rigid bodies smaller
  * than the max size volume. This can also be empty to reflect no collision geometry
  * for the collection.
- ``slow_moving_as_sleeping`` (bool):  [Read-Write] when on non-sleeping, slow moving pieces will be considered as sleeping, this helps removal of jittery but not really moving objects.
- ``slow_moving_velocity_threshold`` (float):  [Read-Write] When slow moving detection is on, this defines the linear velocity thresholds in cm/s to consider the object as sleeping .
- ``strip_on_cook`` (bool):  [Read-Write] Strip unnecessary data from the Geometry Collection to keep the memory footprint as small as possible.
- ``strip_render_data_on_cook`` (bool):  [Read-Write] Strip unnecessary render data from the Geometry Collection to keep the memory footprint as small as possible.
  This may be used if the cooked build uses a custom renderer such as the ISMPool renderer.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``use_full_precision_u_vs`` (bool):  [Read-Write] Whether to use full precision UVs when rendering this geometry. (Does not apply to Nanite rendering)
- ``use_material_damage_modifiers`` (bool):  [Read-Write] When on , use the modifiers on the material to adjust the user defined damage threshold values
- ``use_size_specific_damage_threshold`` (bool):  [Read-Write] whether to use size specific damage threshold instead of level based ones ( see Size Specific Data array ).

<a id="unreal.GeometryCollection.damage_model"></a>

#### damage_model

```python
@property
def damage_model() -> DamageModelTypeEnum
```

(DamageModelTypeEnum):  [Read-Write] Damage model to use for evaluating destruction.

<a id="unreal.GeometryCollection.damage_model"></a>

#### damage_model

```python
@damage_model.setter
def damage_model(value: DamageModelTypeEnum) -> None
```

<a id="unreal.GeometryCollection.use_material_damage_modifiers"></a>

#### use_material_damage_modifiers

```python
@property
def use_material_damage_modifiers() -> bool
```

(bool):  [Read-Write] When on , use the modifiers on the material to adjust the user defined damage threshold values

<a id="unreal.GeometryCollection.use_material_damage_modifiers"></a>

#### use_material_damage_modifiers

```python
@use_material_damage_modifiers.setter
def use_material_damage_modifiers(value: bool) -> None
```

<a id="unreal.GeometryCollection.geometry_source"></a>

#### geometry_source

```python
@property
def geometry_source() -> Array[GeometryCollectionSource]
```

(Array[GeometryCollectionSource]):  [Read-Write]

<a id="unreal.GeometryCollection.geometry_source"></a>

#### geometry_source

```python
@geometry_source.setter
def geometry_source(value: Array[GeometryCollectionSource]) -> None
```

<a id="unreal.GeometryCollection.strip_on_cook"></a>

#### strip_on_cook

```python
@property
def strip_on_cook() -> bool
```

(bool):  [Read-Write] Strip unnecessary data from the Geometry Collection to keep the memory footprint as small as possible.

<a id="unreal.GeometryCollection.strip_on_cook"></a>

#### strip_on_cook

```python
@strip_on_cook.setter
def strip_on_cook(value: bool) -> None
```

<a id="unreal.GeometryCollection.strip_render_data_on_cook"></a>

#### strip_render_data_on_cook

```python
@property
def strip_render_data_on_cook() -> bool
```

(bool):  [Read-Write] Strip unnecessary render data from the Geometry Collection to keep the memory footprint as small as possible.
This may be used if the cooked build uses a custom renderer such as the ISMPool renderer.

<a id="unreal.GeometryCollection.strip_render_data_on_cook"></a>

#### strip_render_data_on_cook

```python
@strip_render_data_on_cook.setter
def strip_render_data_on_cook(value: bool) -> None
```

<a id="unreal.GeometryCollection.custom_renderer_type"></a>

#### custom_renderer_type

```python
@property
def custom_renderer_type() -> Class
```

(type(Class)):  [Read-Write] Custom class type that will be used to render the geometry collection instead of using the native rendering.

<a id="unreal.GeometryCollection.custom_renderer_type"></a>

#### custom_renderer_type

```python
@custom_renderer_type.setter
def custom_renderer_type(value: Class) -> None
```

<a id="unreal.GeometryCollection.root_proxy_data"></a>

#### root_proxy_data

```python
@property
def root_proxy_data() -> GeometryCollectionProxyMeshData
```

(GeometryCollectionProxyMeshData):  [Read-Write] Static mesh to use as a proxy for rendering until the geometry collection is broken.

<a id="unreal.GeometryCollection.root_proxy_data"></a>

#### root_proxy_data

```python
@root_proxy_data.setter
def root_proxy_data(value: GeometryCollectionProxyMeshData) -> None
```

<a id="unreal.GeometryCollection.enable_nanite"></a>

#### enable_nanite

```python
@property
def enable_nanite() -> bool
```

(bool):  [Read-Write] Enable support for Nanite.

<a id="unreal.GeometryCollection.enable_nanite"></a>

#### enable_nanite

```python
@enable_nanite.setter
def enable_nanite(value: bool) -> None
```

<a id="unreal.GeometryCollection.convert_vertex_colors_to_srgb"></a>

#### convert_vertex_colors_to_srgb

```python
@property
def convert_vertex_colors_to_srgb() -> bool
```

(bool):  [Read-Write] Convert vertex colors to sRGB for rendering. Exposed to avoid changing vertex color rendering for legacy assets; should typically be true for new geometry collections.

<a id="unreal.GeometryCollection.convert_vertex_colors_to_srgb"></a>

#### convert_vertex_colors_to_srgb

```python
@convert_vertex_colors_to_srgb.setter
def convert_vertex_colors_to_srgb(value: bool) -> None
```

<a id="unreal.GeometryCollection.collision_type"></a>

#### collision_type

```python
@property
def collision_type() -> CollisionTypeEnum
```

(CollisionTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.collision_type"></a>

#### collision_type

```python
@collision_type.setter
def collision_type(value: CollisionTypeEnum) -> None
```

<a id="unreal.GeometryCollection.implicit_type"></a>

#### implicit_type

```python
@property
def implicit_type() -> ImplicitTypeEnum
```

(ImplicitTypeEnum):  [Read-Write] *  CollisionType defines how to initialize the rigid collision structures.
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.implicit_type"></a>

#### implicit_type

```python
@implicit_type.setter
def implicit_type(value: ImplicitTypeEnum) -> None
```

<a id="unreal.GeometryCollection.min_level_set_resolution"></a>

#### min_level_set_resolution

```python
@property
def min_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.min_level_set_resolution"></a>

#### min_level_set_resolution

```python
@min_level_set_resolution.setter
def min_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollection.max_level_set_resolution"></a>

#### max_level_set_resolution

```python
@property
def max_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.max_level_set_resolution"></a>

#### max_level_set_resolution

```python
@max_level_set_resolution.setter
def max_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollection.min_cluster_level_set_resolution"></a>

#### min_cluster_level_set_resolution

```python
@property
def min_cluster_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 5)
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.min_cluster_level_set_resolution"></a>

#### min_cluster_level_set_resolution

```python
@min_cluster_level_set_resolution.setter
def min_cluster_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollection.max_cluster_level_set_resolution"></a>

#### max_cluster_level_set_resolution

```python
@property
def max_cluster_level_set_resolution() -> int
```

(int32):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.max_cluster_level_set_resolution"></a>

#### max_cluster_level_set_resolution

```python
@max_cluster_level_set_resolution.setter
def max_cluster_level_set_resolution(value: int) -> None
```

<a id="unreal.GeometryCollection.collision_object_reduction_percentage"></a>

#### collision_object_reduction_percentage

```python
@property
def collision_object_reduction_percentage() -> float
```

(float):  [Read-Write] *  Resolution on the smallest axes for the level set. (def: 10)
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.collision_object_reduction_percentage"></a>

#### collision_object_reduction_percentage

```python
@collision_object_reduction_percentage.setter
def collision_object_reduction_percentage(value: float) -> None
```

<a id="unreal.GeometryCollection.root_proxy"></a>

#### root_proxy

```python
@property
def root_proxy() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] static mesh to use as a proxy for rendering until the geometry collection is broken
deprecated: This property is deprecated. Use RootProxyData instead.

<a id="unreal.GeometryCollection.root_proxy"></a>

#### root_proxy

```python
@root_proxy.setter
def root_proxy(value: SoftObjectPath) -> None
```

<a id="unreal.GeometryCollection.physics_material"></a>

#### physics_material

```python
@property
def physics_material() -> PhysicalMaterial
```

(PhysicalMaterial):  [Read-Only] Physics material to use for the geometry collection

<a id="unreal.GeometryCollection.density_from_physics_material"></a>

#### density_from_physics_material

```python
@property
def density_from_physics_material() -> bool
```

(bool):  [Read-Write] Whether to use density ( for mass computation ) from physics material ( if physics material is not set, use the component one or defaults )

<a id="unreal.GeometryCollection.density_from_physics_material"></a>

#### density_from_physics_material

```python
@density_from_physics_material.setter
def density_from_physics_material(value: bool) -> None
```

<a id="unreal.GeometryCollection.mass_as_density"></a>

#### mass_as_density

```python
@property
def mass_as_density() -> bool
```

(bool):  [Read-Write] Mass As Density, units are in kg/m^3 ( only enabled if physics material is not set )

<a id="unreal.GeometryCollection.mass_as_density"></a>

#### mass_as_density

```python
@mass_as_density.setter
def mass_as_density(value: bool) -> None
```

<a id="unreal.GeometryCollection.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write] Total Mass of Collection. If density, units are in kg/m^3 ( only enabled if physics material is not set )

<a id="unreal.GeometryCollection.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.GeometryCollection.minimum_mass_clamp"></a>

#### minimum_mass_clamp

```python
@property
def minimum_mass_clamp() -> float
```

(float):  [Read-Only] Smallest allowable mass (def:0.1)

<a id="unreal.GeometryCollection.import_collision_from_source"></a>

#### import_collision_from_source

```python
@property
def import_collision_from_source() -> bool
```

(bool):  [Read-Write] whether to import collision from the source asset

<a id="unreal.GeometryCollection.import_collision_from_source"></a>

#### import_collision_from_source

```python
@import_collision_from_source.setter
def import_collision_from_source(value: bool) -> None
```

<a id="unreal.GeometryCollection.optimize_convexes"></a>

#### optimize_convexes

```python
@property
def optimize_convexes() -> bool
```

(bool):  [Read-Write] whether to optimize convexes for collisions. If true the convex optimizer will generate at runtime one
single convex shape for physics collisions ignoring all the user defined ones.
Enable p.Chaos.Convex.SimplifyUnion cvar to be able to use it (experimental)

<a id="unreal.GeometryCollection.optimize_convexes"></a>

#### optimize_convexes

```python
@optimize_convexes.setter
def optimize_convexes(value: bool) -> None
```

<a id="unreal.GeometryCollection.collision_particles_fraction"></a>

#### collision_particles_fraction

```python
@property
def collision_particles_fraction() -> float
```

(float):  [Read-Write] Number of particles on the triangulated surface to use for collisions.
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.collision_particles_fraction"></a>

#### collision_particles_fraction

```python
@collision_particles_fraction.setter
def collision_particles_fraction(value: float) -> None
```

<a id="unreal.GeometryCollection.maximum_collision_particles"></a>

#### maximum_collision_particles

```python
@property
def maximum_collision_particles() -> int
```

(int32):  [Read-Write] Max number of particles.
deprecated: This property is deprecated. Use the default SizeSpecificData instead.

<a id="unreal.GeometryCollection.maximum_collision_particles"></a>

#### maximum_collision_particles

```python
@maximum_collision_particles.setter
def maximum_collision_particles(value: int) -> None
```

<a id="unreal.GeometryCollection.scale_on_removal"></a>

#### scale_on_removal

```python
@property
def scale_on_removal() -> bool
```

(bool):  [Read-Write] When enabled, particle will scale down (shrink) when using being removed ( using both remove on sleep or remove on break ) - Enabled by default

<a id="unreal.GeometryCollection.scale_on_removal"></a>

#### scale_on_removal

```python
@scale_on_removal.setter
def scale_on_removal(value: bool) -> None
```

<a id="unreal.GeometryCollection.remove_on_max_sleep"></a>

#### remove_on_max_sleep

```python
@property
def remove_on_max_sleep() -> bool
```

(bool):  [Read-Only] Remove particle from simulation and dissolve rendered geometry once sleep threshold has been exceeded.

<a id="unreal.GeometryCollection.maximum_sleep_time"></a>

#### maximum_sleep_time

```python
@property
def maximum_sleep_time() -> Vector2D
```

(Vector2D):  [Read-Only] How long may the particle sleep before initiating removal (in seconds).

<a id="unreal.GeometryCollection.removal_duration"></a>

#### removal_duration

```python
@property
def removal_duration() -> Vector2D
```

(Vector2D):  [Read-Only] How long does the removal process take (in seconds).

<a id="unreal.GeometryCollection.slow_moving_as_sleeping"></a>

#### slow_moving_as_sleeping

```python
@property
def slow_moving_as_sleeping() -> bool
```

(bool):  [Read-Only] when on non-sleeping, slow moving pieces will be considered as sleeping, this helps removal of jittery but not really moving objects.

<a id="unreal.GeometryCollection.slow_moving_velocity_threshold"></a>

#### slow_moving_velocity_threshold

```python
@property
def slow_moving_velocity_threshold() -> float
```

(float):  [Read-Only] When slow moving detection is on, this defines the linear velocity thresholds in cm/s to consider the object as sleeping .

<a id="unreal.GeometryCollection.enable_remove_pieces_on_fracture"></a>

#### enable_remove_pieces_on_fracture

```python
@property
def enable_remove_pieces_on_fracture() -> bool
```

(bool):  [Read-Write] Enable remove pieces on fracture
deprecated: Use remove on break feature instead ( Fracture editor tools ).

<a id="unreal.GeometryCollection.enable_remove_pieces_on_fracture"></a>

#### enable_remove_pieces_on_fracture

```python
@enable_remove_pieces_on_fracture.setter
def enable_remove_pieces_on_fracture(value: bool) -> None
```

<a id="unreal.GeometryCollection.remove_on_fracture_materials"></a>

#### remove_on_fracture_materials

```python
@property
def remove_on_fracture_materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write] Materials relating to remove on fracture
deprecated: Use remove on break feature instead ( Fracture editor tools ).

<a id="unreal.GeometryCollection.remove_on_fracture_materials"></a>

#### remove_on_fracture_materials

```python
@remove_on_fracture_materials.setter
def remove_on_fracture_materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.GeometryCollection.asset_import_data"></a>

#### asset_import_data

```python
@property
def asset_import_data() -> AssetImportData
```

(AssetImportData):  [Read-Write] Importing data and options used for this geometry collection

<a id="unreal.GeometryCollection.asset_import_data"></a>

#### asset_import_data

```python
@asset_import_data.setter
def asset_import_data(value: AssetImportData) -> None
```

<a id="unreal.GeometryCollection.dataflow_asset"></a>

#### dataflow_asset

```python
@property
def dataflow_asset() -> Dataflow
```

(Dataflow):  [Read-Write] Dataflow

<a id="unreal.GeometryCollection.dataflow_asset"></a>

#### dataflow_asset

```python
@dataflow_asset.setter
def dataflow_asset(value: Dataflow) -> None
```

<a id="unreal.GeometryCollection.overrides"></a>

#### overrides

```python
@property
def overrides() -> Map[str, str]
```

(Map[str, str]):  [Read-Write]

<a id="unreal.GeometryCollection.overrides"></a>

#### overrides

```python
@overrides.setter
def overrides(value: Map[str, str]) -> None
```

<a id="unreal.GeometryCollection.set_enable_nanite"></a>

#### set_enable_nanite

```python
def set_enable_nanite(value: bool) -> None
```

x.set_enable_nanite(value) -> None
Set Enable Nanite

Args:
    value (bool):

<a id="unreal.GeometryCollection.set_convert_vertex_colors_to_srgb"></a>

#### set_convert_vertex_colors_to_srgb

```python
def set_convert_vertex_colors_to_srgb(value: bool) -> None
```

x.set_convert_vertex_colors_to_srgb(value) -> None
Set Convert Vertex Colors to SRGB

Args:
    value (bool):

<a id="unreal.GeometryCollection.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.GeometryCollection.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.GeometryCollection.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.GeometryCollectionRenderLevelSetActor"></a>