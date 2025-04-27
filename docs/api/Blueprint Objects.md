## Blueprint Objects

```python
class Blueprint(BlueprintCore)
```

Blueprints are special assets that provide an intuitive, node-based interface that can be used to create new types of Actors
and script level events; giving designers and gameplay programmers the tools to quickly create and iterate gameplay from
within Unreal Editor without ever needing to write a line of code.

**C++ Source:**

- **Module**: Engine
- **File**: Blueprint.h

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

<a id="unreal.Blueprint.set_blueprint_variable_instance_editable"></a>

#### set_blueprint_variable_instance_editable

```python
def set_blueprint_variable_instance_editable(variable_name: Name,
                                             instance_editable: bool) -> None
```

x.set_blueprint_variable_instance_editable(variable_name, instance_editable) -> None
Sets "Instance Editable" to true/false on a Blueprint variable

Args:
    variable_name (Name): The variable name
    instance_editable (bool): Toggle InstanceEditable

<a id="unreal.Blueprint.set_blueprint_variable_expose_to_cinematics"></a>

#### set_blueprint_variable_expose_to_cinematics

```python
def set_blueprint_variable_expose_to_cinematics(
        variable_name: Name, expose_to_cinematics: bool) -> None
```

x.set_blueprint_variable_expose_to_cinematics(variable_name, expose_to_cinematics) -> None
Sets "Expose To Cinematics" to true/false on a Blueprint variable

Args:
    variable_name (Name): The variable name
    expose_to_cinematics (bool): Set to true to expose to cinematics

<a id="unreal.Blueprint.set_blueprint_variable_expose_on_spawn"></a>

#### set_blueprint_variable_expose_on_spawn

```python
def set_blueprint_variable_expose_on_spawn(variable_name: Name,
                                           expose_on_spawn: bool) -> None
```

x.set_blueprint_variable_expose_on_spawn(variable_name, expose_on_spawn) -> None
Sets "Expose On Spawn" to true/false on a Blueprint variable

Args:
    variable_name (Name): The variable name
    expose_on_spawn (bool): Set to true to expose on spawn

<a id="unreal.Blueprint.generated_class"></a>

#### generated_class

```python
def generated_class() -> Class
```

x.generated_class() -> type(Class)
Gets the class generated when this blueprint is compiled

Returns:
    type(Class): UClass*                      The generated class

<a id="unreal.UserWidgetBlueprint"></a>