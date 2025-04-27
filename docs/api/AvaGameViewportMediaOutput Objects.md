## AvaGameViewportMediaOutput Objects

```python
class AvaGameViewportMediaOutput(MediaOutput)
```

Ava Game Viewport Media Output

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaGameViewportMediaOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``number_of_texture_buffers`` (int32):  [Read-Write] Number of texture used to transfer the texture from the GPU to the system memory.
  A smaller number is most likely to block the GPU (wait for the transfer to complete).
  A bigger number is most likely to increase latency.
  note: Some Capture are not are executed on the GPU. If it's the case then no buffer will be needed and no buffer will be created.

<a id="unreal.AvaPlayable"></a>