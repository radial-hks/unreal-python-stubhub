## ObjectMixerWidgetUserConfig Objects

```python
class ObjectMixerWidgetUserConfig(StructBase)
```

User Configurable Variables

**C++ Source:**

- **Plugin**: ObjectMixer
- **Module**: ObjectMixerEditor
- **File**: ObjectMixerEditorUWidget.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_filter_class`` (type(Class)):  [Read-Write] Sets the default filter class to determine what objects and properties to display in this Object Mixer instance.

<a id="unreal.ObjectMixerWidgetUserConfig.__init__"></a>

#### __init__

```python
def __init__(default_filter_class: Class = None) -> None
```

<a id="unreal.ObjectMixerWidgetUserConfig.default_filter_class"></a>

#### default_filter_class

```python
@property
def default_filter_class() -> Class
```

(type(Class)):  [Read-Write] Sets the default filter class to determine what objects and properties to display in this Object Mixer instance.

<a id="unreal.ObjectMixerWidgetUserConfig.default_filter_class"></a>

#### default_filter_class

```python
@default_filter_class.setter
def default_filter_class(value: Class) -> None
```

<a id="unreal.AnimLayerPropertyAndChannels"></a>