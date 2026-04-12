## custompoiStyle Objects

```python
class custompoiStyle(StructBase)
```

Custompoi Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CustomPoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``label`` (custompoiStyle_label):  [Read-Write]
- ``marker`` (custompoiStyle_marker):  [Read-Write]

<a id="unreal.custompoiStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    marker: custompoiStyle_marker = [[0.000000, 0.000000], ["", ""]],
    label: custompoiStyle_label = [
        "", [0.000000, 0.000000], [0.000000, 0.000000], ["", "", 0]
    ]
) -> None
```

<a id="unreal.custompoiStyle.marker"></a>

#### marker

```python
@property
def marker() -> custompoiStyle_marker
```

(custompoiStyle_marker):  [Read-Write]

<a id="unreal.custompoiStyle.marker"></a>

#### marker

```python
@marker.setter
def marker(value: custompoiStyle_marker) -> None
```

<a id="unreal.custompoiStyle.label"></a>

#### label

```python
@property
def label() -> custompoiStyle_label
```

(custompoiStyle_label):  [Read-Write]

<a id="unreal.custompoiStyle.label"></a>

#### label

```python
@label.setter
def label(value: custompoiStyle_label) -> None
```

<a id="unreal.CreateCustomPoiParams"></a>