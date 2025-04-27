## BaseWidgetBlueprint Objects

```python
class BaseWidgetBlueprint(UserWidgetBlueprint)
```

Base Widget Blueprint

**C++ Source:**

- **Module**: UnrealEd
- **File**: BaseWidgetBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blueprint_category`` (str):  [Read-Write] The category of the Blueprint, used to organize this Blueprint class when displayed in palette windows
- ``blueprint_description`` (str):  [Read-Write] Shows up in the content browser tooltip when the blueprint is hovered
- ``blueprint_display_name`` (str):  [Read-Write] Overrides the BP's display name in the editor UI
- ``blueprint_namespace`` (str):  [Read-Write] The namespace of this blueprint (if set, the Blueprint will be treated differently for the context menu)
- ``compile_mode`` (BlueprintCompileMode):  [Read-Write] The mode that will be used when compiling this class.
- ``deprecate`` (bool):  [Read-Write] Deprecates the Blueprint, marking the generated class with the CLASS_Deprecated flag
- ``generate_abstract_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a abstract class or not.  Should set CLASS_Abstract in the KismetCompiler.
- ``generate_const_class`` (bool):  [Read-Write] Whether or not this blueprint's class is a const class or not.  Should set CLASS_Const in the KismetCompiler.
- ``hide_categories`` (Array[str]):  [Read-Write] Additional HideCategories. These are added to HideCategories from parent.
- ``run_construction_script_in_sequencer`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor in sequencer
- ``run_construction_script_on_drag`` (bool):  [Read-Write] whether or not you want to continuously rerun the construction script for an actor as you drag it in the editor, or only when the drag operation is complete
- ``should_cook_property_guids_value`` (ShouldCookBlueprintPropertyGuids):  [Read-Write] Whether to include the property GUIDs for the generated class in a cooked build.
  note: This option may slightly increase memory usage in a cooked build, but can avoid needing to add CoreRedirect data for Blueprint classes stored within SaveGame archives.
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.WidgetBlueprint"></a>