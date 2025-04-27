## DMMaterialLayer Objects

```python
class DMMaterialLayer(StructBase)
```

DMMaterial Layer

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DMMaterialLayer_Deprecated.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base`` (DMMaterialStage):  [Read-Only]
- ``base_enabled`` (bool):  [Read-Only]
- ``enabled`` (bool):  [Read-Only]
- ``layer_name`` (Text):  [Read-Only]
- ``linked_u_vs`` (bool):  [Read-Only]
- ``mask`` (DMMaterialStage):  [Read-Only]
- ``mask_enabled`` (bool):  [Read-Only]
- ``material_property`` (DMMaterialPropertyType):  [Read-Only]

<a id="unreal.DMMaterialLayer.__init__"></a>

#### __init__

```python
def __init__(material_property: DMMaterialPropertyType = DMMaterialPropertyType
             .NONE,
             layer_name: Text = "",
             base: DMMaterialStage = None,
             mask: DMMaterialStage = None,
             enabled: bool = False,
             base_enabled: bool = False,
             mask_enabled: bool = False,
             linked_u_vs: bool = False) -> None
```

<a id="unreal.DMMaterialLayer.material_property"></a>

#### material_property

```python
@property
def material_property() -> DMMaterialPropertyType
```

(DMMaterialPropertyType):  [Read-Only]

<a id="unreal.DMMaterialLayer.layer_name"></a>

#### layer_name

```python
@property
def layer_name() -> Text
```

(Text):  [Read-Only]

<a id="unreal.DMMaterialLayer.base"></a>

#### base

```python
@property
def base() -> DMMaterialStage
```

(DMMaterialStage):  [Read-Only]

<a id="unreal.DMMaterialLayer.mask"></a>

#### mask

```python
@property
def mask() -> DMMaterialStage
```

(DMMaterialStage):  [Read-Only]

<a id="unreal.DMMaterialLayer.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialLayer.base_enabled"></a>

#### base_enabled

```python
@property
def base_enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialLayer.mask_enabled"></a>

#### mask_enabled

```python
@property
def mask_enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialLayer.linked_u_vs"></a>

#### linked_u_vs

```python
@property
def linked_u_vs() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialEffectList"></a>