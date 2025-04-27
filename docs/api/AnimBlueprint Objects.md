## AnimBlueprint Objects

```python
class AnimBlueprint(Blueprint)
```

An Anim Blueprint is essentially a specialized Blueprint whose graphs control the animation of a Skeletal Mesh.
It can perform blending of animations, directly control the bones of the skeleton, and output a final pose
for a Skeletal Mesh each frame.

**C++ Source:**

- **Module**: Engine
- **File**: AnimBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blueprint_category`` (str):  [Read-Write] The category of the Blueprint, used to organize this Blueprint class when displayed in palette windows
- ``blueprint_description`` (str):  [Read-Write] Shows up in the content browser tooltip when the blueprint is hovered
- ``blueprint_display_name`` (str):  [Read-Write] Overrides the BP's display name in the editor UI
- ``blueprint_namespace`` (str):  [Read-Write] The namespace of this blueprint (if set, the Blueprint will be treated differently for the context menu)
- ``compile_mode`` (BlueprintCompileMode):  [Read-Write] The mode that will be used when compiling this class.
- ``default_binding_class`` (type(Class)):  [Read-Write] The default binding type that any new nodes will use when created
- ``deprecate`` (bool):  [Read-Write] Deprecates the Blueprint, marking the generated class with the CLASS_Deprecated flag
- ``enable_linked_anim_layer_instance_sharing`` (bool):  [Read-Write] If true, linked animation layers will be instantiated only once per AnimClass instead of once per AnimInstance, AnimClass and AnimGroup.
        Extra instances will be created if two or more active anim graph override the same layer Function
- ``generate_abstract_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a abstract class or not.  Should set CLASS_Abstract in the KismetCompiler.
- ``generate_const_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a const class or not.  Should set CLASS_Const in the KismetCompiler.
- ``hide_categories`` (Array[str]):  [Read-Write] Additional HideCategories. These are added to HideCategories from parent.
- ``run_construction_script_in_sequencer`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor in sequencer
- ``run_construction_script_on_drag`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor as you drag it in the editor, or only when the drag operation is complete
- ``should_cook_property_guids_value`` (ShouldCookBlueprintPropertyGuids):  [Read-Write] Whether to include the property GUIDs for the generated class in a cooked build.
  note: This option may slightly increase memory usage in a cooked build, but can avoid needing to add CoreRedirect data for Blueprint classes stored within SaveGame archives.
- ``target_skeleton`` (Skeleton):  [Read-Write] This is the target skeleton asset for anim instances created from this blueprint; all animations
  referenced by the BP should be compatible with this skeleton.  For advanced use only, it is easy
  to cause errors if this is modified without updating or replacing all referenced animations.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``use_multi_threaded_animation_update`` (bool):  [Read-Write] Allows this anim Blueprint to update its native update, blend tree, montages and asset players on
  a worker thread. The compiler will attempt to pick up any issues that may occur with threaded update.
  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded
  Animation Update" should be set.
- ``warn_about_blueprint_usage`` (bool):  [Read-Write] Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint
  is made from the animation graph. This can help track down optimizations that need to be made.

<a id="unreal.AnimBlueprint.get_nodes_of_class"></a>

#### get_nodes_of_class

```python
def get_nodes_of_class(
        node_class: Class,
        include_child_classes: bool = True) -> Array[AnimGraphNode_Base]
```

x.get_nodes_of_class(node_class, include_child_classes=True) -> Array[AnimGraphNode_Base]
Returns all Animation Graph Nodes of the provided Node Class contained by the Animation Blueprint

Args:
    node_class (type(Class)): 
    include_child_classes (bool): 

Returns:
    Array[AnimGraphNode_Base]: 

    graph_nodes (Array[AnimGraphNode_Base]):

<a id="unreal.AnimBlueprint.get_animation_graphs"></a>

#### get_animation_graphs

```python
def get_animation_graphs() -> Array[AnimationGraph]
```

x.get_animation_graphs() -> Array[AnimationGraph]
Returns all Animation Graphs contained by the provided Animation Blueprint

Returns:
    Array[AnimationGraph]: 

    animation_graphs (Array[AnimationGraph]):

<a id="unreal.AnimBlueprint.add_node_asset_override"></a>

#### add_node_asset_override

```python
def add_node_asset_override(target: AnimationAsset,
                            override: AnimationAsset,
                            print_applied_overrides: bool = False) -> None
```

x.add_node_asset_override(target, override, print_applied_overrides=False) -> None
Adds an Animation Asset override for the provided AnimationBlueprint, replacing any instance of Target with Override

Args:
    target (AnimationAsset): The Animation Asset to add an override for (overrides all instances of the asset)
    override (AnimationAsset): The Animation Asset to used to override the Target with (types have to match)
    print_applied_overrides (bool): Flag whether or not to print the applied overrides

<a id="unreal.VimBlueprint"></a>