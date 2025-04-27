## EditorUtilitySubsystem Objects

```python
class EditorUtilitySubsystem(EditorSubsystem)
```

Editor Utility Subsystem

**C++ Source:**

- **Module**: Blutility
- **File**: EditorUtilitySubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_begin_pie`` (OnEditorUtilityPIEEvent):  [Read-Write] Expose Begin PIE to blueprints.
- ``on_end_pie`` (OnEditorUtilityPIEEvent):  [Read-Write] Expose End PIE to blueprints.

<a id="unreal.EditorUtilitySubsystem.on_begin_pie"></a>

#### on_begin_pie

```python
@property
def on_begin_pie() -> OnEditorUtilityPIEEvent
```

(OnEditorUtilityPIEEvent):  [Read-Write] Expose Begin PIE to blueprints.

<a id="unreal.EditorUtilitySubsystem.on_begin_pie"></a>

#### on_begin_pie

```python
@on_begin_pie.setter
def on_begin_pie(value: OnEditorUtilityPIEEvent) -> None
```

<a id="unreal.EditorUtilitySubsystem.on_end_pie"></a>

#### on_end_pie

```python
@property
def on_end_pie() -> OnEditorUtilityPIEEvent
```

(OnEditorUtilityPIEEvent):  [Read-Write] Expose End PIE to blueprints.

<a id="unreal.EditorUtilitySubsystem.on_end_pie"></a>

#### on_end_pie

```python
@on_end_pie.setter
def on_end_pie(value: OnEditorUtilityPIEEvent) -> None
```

<a id="unreal.EditorUtilitySubsystem.unregister_tab_by_id"></a>

#### unregister_tab_by_id

```python
def unregister_tab_by_id(tab_id: Name) -> bool
```

x.unregister_tab_by_id(tab_id) -> bool
Given an ID for a tab, try to close and unregister a tab that was registered through this subsystem

Args:
    tab_id (Name): 

Returns:
    bool:

<a id="unreal.EditorUtilitySubsystem.try_run_class"></a>

#### try_run_class

```python
def try_run_class(object_class: Class) -> bool
```

x.try_run_class(object_class) -> bool
Try Run Class

Args:
    object_class (type(Class)): 

Returns:
    bool:

<a id="unreal.EditorUtilitySubsystem.try_run"></a>

#### try_run

```python
def try_run(asset: Object) -> bool
```

x.try_run(asset) -> bool
Try Run

Args:
    asset (Object): 

Returns:
    bool:

<a id="unreal.EditorUtilitySubsystem.spawn_registered_tab_by_id"></a>

#### spawn_registered_tab_by_id

```python
def spawn_registered_tab_by_id(new_tab_id: Name) -> bool
```

x.spawn_registered_tab_by_id(new_tab_id) -> bool
Given an ID for a tab, try to find a tab spawner that matches, and then spawn a tab. Returns true if it was able to find a matching tab spawner

Args:
    new_tab_id (Name): 

Returns:
    bool:

<a id="unreal.EditorUtilitySubsystem.spawn_and_register_tab_with_id_generated_class"></a>

#### spawn_and_register_tab_with_id_generated_class

```python
def spawn_and_register_tab_with_id_generated_class(
        generated_widget_blueprint: WidgetBlueprintGeneratedClass,
        tab_id: Name) -> EditorUtilityWidget
```

x.spawn_and_register_tab_with_id_generated_class(generated_widget_blueprint, tab_id) -> EditorUtilityWidget
Unlike SpawnAndRegisterTabAndGetID allows spawn tab while providing TabID from Python scripts or BP

Args:
    generated_widget_blueprint (type(WidgetBlueprintGeneratedClass)): 
    tab_id (Name): 

Returns:
    EditorUtilityWidget:

<a id="unreal.EditorUtilitySubsystem.spawn_and_register_tab_with_id"></a>

#### spawn_and_register_tab_with_id

```python
def spawn_and_register_tab_with_id(blueprint: EditorUtilityWidgetBlueprint,
                                   tab_id: Name) -> EditorUtilityWidget
```

x.spawn_and_register_tab_with_id(blueprint, tab_id) -> EditorUtilityWidget
Unlike SpawnAndRegisterTabAndGetID allows spawn tab while providing TabID from Python scripts or BP

Args:
    blueprint (EditorUtilityWidgetBlueprint): 
    tab_id (Name): 

Returns:
    EditorUtilityWidget:

<a id="unreal.EditorUtilitySubsystem.spawn_and_register_tab_generated_class"></a>

#### spawn_and_register_tab_generated_class

```python
def spawn_and_register_tab_generated_class(
    generated_widget_blueprint: WidgetBlueprintGeneratedClass
) -> EditorUtilityWidget
```

x.spawn_and_register_tab_generated_class(generated_widget_blueprint) -> EditorUtilityWidget
Spawn and Register Tab Generated Class

Args:
    generated_widget_blueprint (type(WidgetBlueprintGeneratedClass)): 

Returns:
    EditorUtilityWidget:

<a id="unreal.EditorUtilitySubsystem.spawn_and_register_tab_and_get_id_generated_class"></a>

#### spawn_and_register_tab_and_get_id_generated_class

```python
def spawn_and_register_tab_and_get_id_generated_class(
    generated_widget_blueprint: WidgetBlueprintGeneratedClass
) -> Tuple[EditorUtilityWidget, Name]
```

x.spawn_and_register_tab_and_get_id_generated_class(generated_widget_blueprint) -> (EditorUtilityWidget, new_tab_id=Name)
Spawn and Register Tab and Get IDGenerated Class

Args:
    generated_widget_blueprint (type(WidgetBlueprintGeneratedClass)): 

Returns:
    Name: 

    new_tab_id (Name):

<a id="unreal.EditorUtilitySubsystem.spawn_and_register_tab_and_get_id"></a>

#### spawn_and_register_tab_and_get_id

```python
def spawn_and_register_tab_and_get_id(
    blueprint: EditorUtilityWidgetBlueprint
) -> Tuple[EditorUtilityWidget, Name]
```

x.spawn_and_register_tab_and_get_id(blueprint) -> (EditorUtilityWidget, new_tab_id=Name)
Spawn and Register Tab and Get ID

Args:
    blueprint (EditorUtilityWidgetBlueprint): 

Returns:
    Name: 

    new_tab_id (Name):

<a id="unreal.EditorUtilitySubsystem.spawn_and_register_tab"></a>

#### spawn_and_register_tab

```python
def spawn_and_register_tab(
        blueprint: EditorUtilityWidgetBlueprint) -> EditorUtilityWidget
```

x.spawn_and_register_tab(blueprint) -> EditorUtilityWidget
Spawn and Register Tab

Args:
    blueprint (EditorUtilityWidgetBlueprint): 

Returns:
    EditorUtilityWidget:

<a id="unreal.EditorUtilitySubsystem.release_instance_of_asset"></a>

#### release_instance_of_asset

```python
def release_instance_of_asset(asset: Object) -> None
```

x.release_instance_of_asset(asset) -> None
Allow startup object to be garbage collected

Args:
    asset (Object):

<a id="unreal.EditorUtilitySubsystem.register_tab_and_get_id_generated_class"></a>

#### register_tab_and_get_id_generated_class

```python
def register_tab_and_get_id_generated_class(
        generated_widget_blueprint: WidgetBlueprintGeneratedClass) -> Name
```

x.register_tab_and_get_id_generated_class(generated_widget_blueprint) -> Name
Register Tab and Get IDGenerated Class

Args:
    generated_widget_blueprint (type(WidgetBlueprintGeneratedClass)): 

Returns:
    Name: 

    new_tab_id (Name):

<a id="unreal.EditorUtilitySubsystem.register_tab_and_get_id"></a>

#### register_tab_and_get_id

```python
def register_tab_and_get_id(blueprint: EditorUtilityWidgetBlueprint) -> Name
```

x.register_tab_and_get_id(blueprint) -> Name
Register Tab and Get ID

Args:
    blueprint (EditorUtilityWidgetBlueprint): 

Returns:
    Name: 

    new_tab_id (Name):

<a id="unreal.EditorUtilitySubsystem.register_and_execute_task"></a>

#### register_and_execute_task

```python
def register_and_execute_task(
        new_task: EditorUtilityTask,
        optional_parent_task: EditorUtilityTask = None) -> None
```

x.register_and_execute_task(new_task, optional_parent_task=None) -> None
Register and Execute Task

Args:
    new_task (EditorUtilityTask): 
    optional_parent_task (EditorUtilityTask):

<a id="unreal.EditorUtilitySubsystem.find_utility_widget_from_blueprint"></a>

#### find_utility_widget_from_blueprint

```python
def find_utility_widget_from_blueprint(
        blueprint: EditorUtilityWidgetBlueprint) -> EditorUtilityWidget
```

x.find_utility_widget_from_blueprint(blueprint) -> EditorUtilityWidget
Given an editor utility widget blueprint, get the widget it creates. This will return a null pointer if the widget is not currently in a tab.

Args:
    blueprint (EditorUtilityWidgetBlueprint): 

Returns:
    EditorUtilityWidget:

<a id="unreal.EditorUtilitySubsystem.does_tab_exist"></a>

#### does_tab_exist

```python
def does_tab_exist(new_tab_id: Name) -> bool
```

x.does_tab_exist(new_tab_id) -> bool
Given an ID for a tab, try to find an existing tab. Returns true if it found a tab.

Args:
    new_tab_id (Name): 

Returns:
    bool:

<a id="unreal.EditorUtilitySubsystem.close_tab_by_id"></a>

#### close_tab_by_id

```python
def close_tab_by_id(new_tab_id: Name) -> bool
```

x.close_tab_by_id(new_tab_id) -> bool
Given an ID for a tab, try to find and close an existing tab. Returns true if it found a tab to close.

Args:
    new_tab_id (Name): 

Returns:
    bool:

<a id="unreal.EditorUtilitySubsystem.can_run"></a>

#### can_run

```python
def can_run(asset: Object) -> bool
```

x.can_run(asset) -> bool
Can Run

Args:
    asset (Object): 

Returns:
    bool:

<a id="unreal.EditorUtilityTask"></a>