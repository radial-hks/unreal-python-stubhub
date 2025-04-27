## AlphaTransformPass Objects

```python
class AlphaTransformPass(CompositingElementTransform)
```

Alpha Transform Pass

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_scale`` (float):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingOpenColorIOPass"></a>