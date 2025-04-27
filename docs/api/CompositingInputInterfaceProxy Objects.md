## CompositingInputInterfaceProxy Objects

```python
class CompositingInputInterfaceProxy(CompositingElementInput)
```

Compositing Input Interface Proxy

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementInputs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compositing_input`` (CompositingInputInterface):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For inputs, all 'Intermediate'
  passes are available to the first transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingInputInterfaceProxy.compositing_input"></a>

#### compositing_input

```python
@property
def compositing_input() -> CompositingInputInterface
```

(CompositingInputInterface):  [Read-Write]

<a id="unreal.CompositingInputInterfaceProxy.compositing_input"></a>

#### compositing_input

```python
@compositing_input.setter
def compositing_input(value: CompositingInputInterface) -> None
```

<a id="unreal.CompositingElementOutput"></a>