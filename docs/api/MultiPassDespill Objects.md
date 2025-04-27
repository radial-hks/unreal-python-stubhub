## MultiPassDespill Objects

```python
class MultiPassDespill(CompositingElementTransform)
```

Multi Pass Despill

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``key_colors`` (Array[LinearColor]):  [Read-Write]
- ``keyer_material`` (CompositingMaterial):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.MultiPassDespill.key_colors"></a>

#### key_colors

```python
@property
def key_colors() -> Array[LinearColor]
```

(Array[LinearColor]):  [Read-Only]

<a id="unreal.MultiPassDespill.keyer_material"></a>

#### keyer_material

```python
@property
def keyer_material() -> CompositingMaterial
```

(CompositingMaterial):  [Read-Only]

<a id="unreal.AlphaTransformPass"></a>