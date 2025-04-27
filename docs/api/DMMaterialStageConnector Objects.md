## DMMaterialStageConnector Objects

```python
class DMMaterialStageConnector(StructBase)
```

An input or output form a material source/stage (e.g. RGB out.)

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMEDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index`` (int32):  [Read-Only] This is the index of the input connector on the UMaterialExpression node (not on the stage's input array or the inputconnectors array.)
- ``name`` (Text):  [Read-Only]
- ``type`` (DMValueType):  [Read-Only]

<a id="unreal.DMMaterialStageConnector.__init__"></a>

#### __init__

```python
def __init__(index: int = 0,
             name: Text = "",
             type: DMValueType = DMValueType.VT_NONE) -> None
```

<a id="unreal.DMMaterialStageConnector.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only] This is the index of the input connector on the UMaterialExpression node (not on the stage's input array or the inputconnectors array.)

<a id="unreal.DMMaterialStageConnector.name"></a>

#### name

```python
@property
def name() -> Text
```

(Text):  [Read-Only]

<a id="unreal.DMMaterialStageConnector.type"></a>

#### type

```python
@property
def type() -> DMValueType
```

(DMValueType):  [Read-Only]

<a id="unreal.DMMaterialStageConnection"></a>