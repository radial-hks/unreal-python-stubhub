## SlatePostSettings Objects

```python
class SlatePostSettings(StructBase)
```

Settings for a particular Slate Post RT.
Notably if enabled & blur by default. To be updated with additional effects & to be expandable in game code / settings.

**C++ Source:**

- **Module**: SlateRHIRenderer
- **File**: SlateRHIRendererSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] Should this post buffer be enabled for updating
- ``post_processor_class`` (type(Class)):  [Read-Write] Copy of actually loaded post processor class

<a id="unreal.SlatePostSettings.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             post_processor_class: Class = None) -> None
```

<a id="unreal.SlatePostSettings.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Should this post buffer be enabled for updating

<a id="unreal.SlatePostSettings.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.SlatePostSettings.post_processor_class"></a>

#### post_processor_class

```python
@property
def post_processor_class() -> Class
```

(type(Class)):  [Read-Write] Copy of actually loaded post processor class

<a id="unreal.SlatePostSettings.post_processor_class"></a>

#### post_processor_class

```python
@post_processor_class.setter
def post_processor_class(value: Class) -> None
```

<a id="unreal.RadialBoxSettings"></a>