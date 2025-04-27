## SharedMemoryMediaOutput Objects

```python
class SharedMemoryMediaOutput(MediaOutput)
```

Output information for a SharedMemory media capture.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: SharedMemoryMedia
- **File**: SharedMemoryMediaOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cross_gpu`` (bool):  [Read-Write] If checked, the texture will be shared across different GPUs. Disable if not needed for faster performance
- ``invert_alpha`` (bool):  [Read-Write] If checked, the alpha channel of the texture will be inverted
- ``number_of_texture_buffers`` (int32):  [Read-Write] Number of texture used to transfer the texture from the GPU to the system memory.
  A smaller number is most likely to block the GPU (wait for the transfer to complete).
  A bigger number is most likely to increase latency.
  note: Some Capture are not are executed on the GPU. If it's the case then no buffer will be needed and no buffer will be created.
- ``unique_name`` (str):  [Read-Write] Shared memory will be opened by using this name. Should be unique per media output.

<a id="unreal.SharedMemoryMediaOutput.unique_name"></a>

#### unique_name

```python
@property
def unique_name() -> str
```

(str):  [Read-Write] Shared memory will be opened by using this name. Should be unique per media output.

<a id="unreal.SharedMemoryMediaOutput.unique_name"></a>

#### unique_name

```python
@unique_name.setter
def unique_name(value: str) -> None
```

<a id="unreal.SharedMemoryMediaOutput.invert_alpha"></a>

#### invert_alpha

```python
@property
def invert_alpha() -> bool
```

(bool):  [Read-Write] If checked, the alpha channel of the texture will be inverted

<a id="unreal.SharedMemoryMediaOutput.invert_alpha"></a>

#### invert_alpha

```python
@invert_alpha.setter
def invert_alpha(value: bool) -> None
```

<a id="unreal.SharedMemoryMediaOutput.cross_gpu"></a>

#### cross_gpu

```python
@property
def cross_gpu() -> bool
```

(bool):  [Read-Write] If checked, the texture will be shared across different GPUs. Disable if not needed for faster performance

<a id="unreal.SharedMemoryMediaOutput.cross_gpu"></a>

#### cross_gpu

```python
@cross_gpu.setter
def cross_gpu(value: bool) -> None
```

<a id="unreal.SharedMemoryMediaSource"></a>