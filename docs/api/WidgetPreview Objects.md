## WidgetPreview Objects

```python
class WidgetPreview(Object)
```

Widget Preview

**C++ Source:**

- **Plugin**: UMGWidgetPreview
- **Module**: UMGWidgetPreview
- **File**: WidgetPreview.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``slot_widget_types`` (Map[Name, PreviewableWidgetVariant]):  [Read-Write] Widget per-slot, if WidgetType has any.
- ``widget_type`` (PreviewableWidgetVariant):  [Read-Write] Widget to preview.

<a id="unreal.WidgetPreview.widget_type"></a>

#### widget_type

```python
@property
def widget_type() -> PreviewableWidgetVariant
```

(PreviewableWidgetVariant):  [Read-Write] Widget to preview.

<a id="unreal.WidgetPreview.widget_type"></a>

#### widget_type

```python
@widget_type.setter
def widget_type(value: PreviewableWidgetVariant) -> None
```

<a id="unreal.WidgetPreview.slot_widget_types"></a>

#### slot_widget_types

```python
@property
def slot_widget_types() -> Map[Name, PreviewableWidgetVariant]
```

(Map[Name, PreviewableWidgetVariant]):  [Read-Write] Widget per-slot, if WidgetType has any.

<a id="unreal.WidgetPreview.slot_widget_types"></a>

#### slot_widget_types

```python
@slot_widget_types.setter
def slot_widget_types(value: Map[Name, PreviewableWidgetVariant]) -> None
```

<a id="unreal.WidgetPreview.get_widget_slot_names"></a>

#### get_widget_slot_names

```python
def get_widget_slot_names() -> Array[Name]
```

x.get_widget_slot_names() -> Array[Name]
Get Widget Slot Names

Returns:
    Array[Name]:

<a id="unreal.WidgetPreview.get_available_widget_slot_names"></a>

#### get_available_widget_slot_names

```python
def get_available_widget_slot_names() -> Array[Name]
```

x.get_available_widget_slot_names() -> Array[Name]
Returns slot names not already occupied in SlotWidgets.

Returns:
    Array[Name]:

<a id="unreal.WidgetPreviewFactory"></a>