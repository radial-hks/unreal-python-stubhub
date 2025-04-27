## AvaBroadcastRenderTargetMediaOutput Objects

```python
class AvaBroadcastRenderTargetMediaOutput(MediaOutput)
```

Capture a Media to a render target.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaBroadcastRenderTargetMediaOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``invert_key_output`` (bool):  [Read-Write] Invert the key (alpha channel).
- ``number_of_texture_buffers`` (int32):  [Read-Write] Number of texture used to transfer the texture from the GPU to the system memory.
  A smaller number is most likely to block the GPU (wait for the transfer to complete).
  A bigger number is most likely to increase latency.
  note: Some Capture are not are executed on the GPU. If it's the case then no buffer will be needed and no buffer will be created.
- ``render_target`` (TextureRenderTarget2D):  [Read-Write] Specify the render target to be capturing to.

<a id="unreal.AvaBroadcastRenderTargetMediaOutput.invert_key_output"></a>

#### invert_key_output

```python
@property
def invert_key_output() -> bool
```

(bool):  [Read-Write] Invert the key (alpha channel).

<a id="unreal.AvaBroadcastRenderTargetMediaOutput.invert_key_output"></a>

#### invert_key_output

```python
@invert_key_output.setter
def invert_key_output(value: bool) -> None
```

<a id="unreal.AvaBroadcastRenderTargetMediaOutput.render_target"></a>

#### render_target

```python
@property
def render_target() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write] Specify the render target to be capturing to.

<a id="unreal.AvaBroadcastRenderTargetMediaOutput.render_target"></a>

#### render_target

```python
@render_target.setter
def render_target(value: TextureRenderTarget2D) -> None
```

<a id="unreal.AvaRenderTargetMediaOutput"></a>