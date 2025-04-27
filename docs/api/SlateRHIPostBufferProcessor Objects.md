## SlateRHIPostBufferProcessor Objects

```python
class SlateRHIPostBufferProcessor(Object)
```

Base class for types that can process the backbuffer scene into the slate post buffer.

Implement 'PostProcess' in your derived class. Additionally, you need to create a renderthread proxy that derives from 'FSlateRHIPostBufferProcessorProxy'
For an example see: USlatePostBufferBlur.

**C++ Source:**

- **Module**: SlateRHIRenderer
- **File**: SlateRHIPostBufferProcessor.h

<a id="unreal.SlatePostBufferBlur"></a>