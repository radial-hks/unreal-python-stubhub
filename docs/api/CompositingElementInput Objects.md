## CompositingElementInput Objects

```python
class CompositingElementInput(CompositingElementPass)
```

Compositing Element Input

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementPasses.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For inputs, all 'Intermediate'
  passes are available to the first transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingElementInput.intermediate"></a>

#### intermediate

```python
@property
def intermediate() -> bool
```

(bool):  [Read-Only] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
When set, render target resources used by this element will be reused. For inputs, all 'Intermediate'
passes are available to the first transform pass, and released after that.

<a id="unreal.CompositingElementInput.generate_input"></a>

#### generate_input

```python
def generate_input() -> Texture
```

x.generate_input() -> Texture
Generate Input

Returns:
    Texture:

<a id="unreal.CompositingMediaInput"></a>