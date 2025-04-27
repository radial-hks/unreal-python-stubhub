## ObjectMixerBlueprintObjectFilter Objects

```python
class ObjectMixerBlueprintObjectFilter(ObjectMixerObjectFilter)
```

Script class for filtering object types to Object Mixer.
Blueprint classes should inherit directly from this class.

**C++ Source:**

- **Plugin**: ObjectMixer
- **Module**: ObjectMixerEditor
- **File**: ObjectMixerEditorObjectFilter.h

<a id="unreal.ObjectMixerBlueprintObjectFilter.should_include_unsupported_properties"></a>

#### should_include_unsupported_properties

```python
def should_include_unsupported_properties() -> bool
```

x.should_include_unsupported_properties() -> bool
If true, properties that are not visible in the details panel and properties not supported by SSingleProperty will be selectable.
Defaults to false.

Returns:
    bool:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_show_transient_objects"></a>

#### get_show_transient_objects

```python
def get_show_transient_objects() -> bool
```

x.get_show_transient_objects() -> bool
Determines if transient objects (such as Sequencer Spawnables) should be shown in the list. False by default.

Returns:
    bool:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_properties_that_require_list_refresh"></a>

#### get_properties_that_require_list_refresh

```python
def get_properties_that_require_list_refresh() -> Set[Name]
```

x.get_properties_that_require_list_refresh() -> Set[Name]
If a property is changed that has a name found in this set, the panel will be refreshed.
Add a property name to this list if you expect the list to change in some way after changing that property.

Returns:
    Set[Name]:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_object_mixer_property_inheritance_inclusion_options"></a>

#### get_object_mixer_property_inheritance_inclusion_options

```python
def get_object_mixer_property_inheritance_inclusion_options(
) -> ObjectMixerInheritanceInclusionOptions
```

x.get_object_mixer_property_inheritance_inclusion_options() -> ObjectMixerInheritanceInclusionOptions
Specify whether we should return only the properties of the specified classes or the properties of parent and child classes.
Defaults to 'None' which only considers the properties of the specified classes.
If you're not seeing all the properties you expected, try overloading this function.

Returns:
    ObjectMixerInheritanceInclusionOptions:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_object_mixer_placement_class_inclusion_options"></a>

#### get_object_mixer_placement_class_inclusion_options

```python
def get_object_mixer_placement_class_inclusion_options(
) -> ObjectMixerInheritanceInclusionOptions
```

x.get_object_mixer_placement_class_inclusion_options() -> ObjectMixerInheritanceInclusionOptions
Specify whether we should return only the specified classes or the parent and child classes in placement mode.
Defaults to 'None' which only considers the specified classes.

Returns:
    ObjectMixerInheritanceInclusionOptions:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_object_classes_to_place"></a>

#### get_object_classes_to_place

```python
def get_object_classes_to_place() -> Set[Class]
```

x.get_object_classes_to_place() -> Set[type(Class)]
Return the basic actor types you want to be able to place using the Add button.
Note that only subclasses of AActor are supported and only those which have a registered factory.
This includes most engine actor types.

Returns:
    Set[type(Class)]:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_object_classes_to_filter"></a>

#### get_object_classes_to_filter

```python
def get_object_classes_to_filter() -> Set[Class]
```

x.get_object_classes_to_filter() -> Set[type(Class)]
Return the basic object types you want to filter for in your level.
For example, if you want to work with Lights, return ULightComponentBase.
If you also want to see the properties for parent or child classes,
override the GetObjectMixerPropertyInheritanceInclusionOptions and GetForceAddedColumns functions.

Returns:
    Set[type(Class)]:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_force_added_columns"></a>

#### get_force_added_columns

```python
def get_force_added_columns() -> Set[Name]
```

x.get_force_added_columns() -> Set[Name]
Specify a list of property names found in parent classes you want to show that aren't in the specified classes.
Note that properties specified here do not override the properties specified in GetColumnsToExclude().
For example, a ULightComponent displays "LightColor" in the editor's details panel,
but ULightComponent itself doesn't have a property named "LightColor". Instead it's in its parent class, ULightComponentBase.
In this scenario, ULightComponent is specified and PropertyInheritanceInclusionOptions is None, so "LightColor" won't appear by default.
Specify "LightColor" in this function to ensure that "LightColor" will appear as a column as long as
the property is accessible to one of the specified classes regardless of which parent class it comes from.

Returns:
    Set[Name]:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_columns_to_show_by_default"></a>

#### get_columns_to_show_by_default

```python
def get_columns_to_show_by_default() -> Set[Name]
```

x.get_columns_to_show_by_default() -> Set[Name]
Specify a list of property names corresponding to columns you want to show by default.
For example, you can specify "Intensity" and "LightColor" to show only those property columns by default in the UI.
Columns not specified will not be shown by default but can be enabled by the user in the UI.

Returns:
    Set[Name]:

<a id="unreal.ObjectMixerBlueprintObjectFilter.get_columns_to_exclude"></a>

#### get_columns_to_exclude

```python
def get_columns_to_exclude() -> Set[Name]
```

x.get_columns_to_exclude() -> Set[Name]
Specify a list of property names corresponding to columns you don't want to ever show.
For example, you can specify "Intensity" and "LightColor" to ensure that they can't be enabled or shown in the UI.
Columns not specified can be enabled by the user in the UI.

Returns:
    Set[Name]:

<a id="unreal.ObjectMixerEditorUWidget"></a>