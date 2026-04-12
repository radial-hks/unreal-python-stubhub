## HighlightInfo Objects

```python
class HighlightInfo(StructBase)
```

Highlight Info

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: ChinaMapTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_color`` (LinearColor):  [Read-Write]
- ``mid`` (MaterialInstanceDynamic):  [Read-Write]
- ``smc`` (StaticMeshComponent):  [Read-Write]

<a id="unreal.HighlightInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(smc: StaticMeshComponent = None,
             default_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             mid: MaterialInstanceDynamic = None) -> None
```

<a id="unreal.HighlightInfo.smc"></a>

#### smc

```python
@property
def smc() -> StaticMeshComponent
```

(StaticMeshComponent):  [Read-Write]

<a id="unreal.HighlightInfo.smc"></a>

#### smc

```python
@smc.setter
def smc(value: StaticMeshComponent) -> None
```

<a id="unreal.HighlightInfo.default_color"></a>

#### default\_color

```python
@property
def default_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.HighlightInfo.default_color"></a>

#### default\_color

```python
@default_color.setter
def default_color(value: LinearColor) -> None
```

<a id="unreal.HighlightInfo.mid"></a>

#### mid

```python
@property
def mid() -> MaterialInstanceDynamic
```

(MaterialInstanceDynamic):  [Read-Write]

<a id="unreal.HighlightInfo.mid"></a>

#### mid

```python
@mid.setter
def mid(value: MaterialInstanceDynamic) -> None
```

<a id="unreal.API_HeatPointData"></a>