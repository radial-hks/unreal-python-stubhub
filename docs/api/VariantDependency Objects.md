## VariantDependency Objects

```python
class VariantDependency(StructBase)
```

Variant Dependency

**C++ Source:**

- **Plugin**: VariantManagerContent
- **Module**: VariantManagerContent
- **File**: Variant.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``variant`` (Variant):  [Read-Write]
- ``variant_set`` (VariantSet):  [Read-Write]

<a id="unreal.VariantDependency.__init__"></a>

#### __init__

```python
def __init__(variant_set: VariantSet = None,
             variant: Variant = None,
             enabled: bool = False) -> None
```

<a id="unreal.VariantDependency.variant_set"></a>

#### variant_set

```python
@property
def variant_set() -> VariantSet
```

(VariantSet):  [Read-Only]

<a id="unreal.VariantDependency.variant"></a>

#### variant

```python
@property
def variant() -> Variant
```

(Variant):  [Read-Only]

<a id="unreal.VariantDependency.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DatasmithAssetImportOptions"></a>