## WidgetNavigationData Objects

```python
class WidgetNavigationData(StructBase)
```

Widget Navigation Data

**C++ Source:**

- **Module**: UMG
- **File**: WidgetNavigation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rule`` (UINavigationRule):  [Read-Write]
- ``widget_to_focus`` (Name):  [Read-Write] This either the widget to focus, OR the name of the function to call.

<a id="unreal.WidgetNavigationData.__init__"></a>

#### __init__

```python
def __init__(rule: UINavigationRule = UINavigationRule.ESCAPE,
             widget_to_focus: Name = "None") -> None
```

<a id="unreal.WidgetNavigationData.rule"></a>

#### rule

```python
@property
def rule() -> UINavigationRule
```

(UINavigationRule):  [Read-Only]

<a id="unreal.WidgetNavigationData.widget_to_focus"></a>

#### widget_to_focus

```python
@property
def widget_to_focus() -> Name
```

(Name):  [Read-Only] This either the widget to focus, OR the name of the function to call.

<a id="unreal.MovieSceneDynamicBindingPayloadVariable"></a>