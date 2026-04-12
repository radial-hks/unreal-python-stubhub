## poiStyle Objects

```python
class poiStyle(StructBase)
```

Poi Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``label`` (poiStyle_label):  [Read-Write]
- ``marker`` (poiStyle_marker):  [Read-Write]

<a id="unreal.poiStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    marker: poiStyle_marker = [[0.000000, 0.000000], ["", ""]],
    label: poiStyle_label = [
        "", [0.000000, 0.000000], [0.000000, 0.000000], ["", "", 0]
    ]
) -> None
```

<a id="unreal.poiStyle.marker"></a>

#### marker

```python
@property
def marker() -> poiStyle_marker
```

(poiStyle_marker):  [Read-Write]

<a id="unreal.poiStyle.marker"></a>

#### marker

```python
@marker.setter
def marker(value: poiStyle_marker) -> None
```

<a id="unreal.poiStyle.label"></a>

#### label

```python
@property
def label() -> poiStyle_label
```

(poiStyle_label):  [Read-Write]

<a id="unreal.poiStyle.label"></a>

#### label

```python
@label.setter
def label(value: poiStyle_label) -> None
```

<a id="unreal.CreatePoiParams"></a>