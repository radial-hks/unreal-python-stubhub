## SlateFXSubsystem Objects

```python
class SlateFXSubsystem(EngineSubsystem)
```

Slate FXSubsystem

**C++ Source:**

- **Module**: SlateRHIRenderer
- **File**: SlateFXSubsystem.h

<a id="unreal.SlateFXSubsystem.get_slate_post_processor"></a>

#### get_slate_post_processor

```python
def get_slate_post_processor(
        post_buffer_bit: SlatePostRT) -> SlateRHIPostBufferProcessor
```

x.get_slate_post_processor(post_buffer_bit) -> SlateRHIPostBufferProcessor
Get post processor for a particular post buffer index, if it exists

Args:
    post_buffer_bit (SlatePostRT): 

Returns:
    SlateRHIPostBufferProcessor:

<a id="unreal.SlateRHIPostBufferProcessor"></a>