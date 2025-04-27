## CompositingInputInterface Objects

```python
class CompositingInputInterface(Interface)
```

Compositing Input Interface

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementInputs.h

<a id="unreal.CompositingInputInterface.on_frame_end"></a>

#### on_frame_end

```python
def on_frame_end(proxy: CompositingInputInterfaceProxy) -> None
```

x.on_frame_end(proxy) -> None
On Frame End

Args:
    proxy (CompositingInputInterfaceProxy):

<a id="unreal.CompositingInputInterface.on_frame_begin"></a>

#### on_frame_begin

```python
def on_frame_begin(proxy: CompositingInputInterfaceProxy,
                   camera_cut_this_frame: bool) -> None
```

x.on_frame_begin(proxy, camera_cut_this_frame) -> None
On Frame Begin

Args:
    proxy (CompositingInputInterfaceProxy): 
    camera_cut_this_frame (bool):

<a id="unreal.CompositingInputInterface.generate_input"></a>

#### generate_input

```python
def generate_input(proxy: CompositingInputInterfaceProxy) -> Texture
```

x.generate_input(proxy) -> Texture
Generate Input

Args:
    proxy (CompositingInputInterfaceProxy): 

Returns:
    Texture:

<a id="unreal.CompositingInputInterfaceProxy"></a>