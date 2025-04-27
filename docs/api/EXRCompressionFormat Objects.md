## EXRCompressionFormat Objects

```python
class EXRCompressionFormat(EnumBase)
```

Exr compression format options. Exactly matches the exr library Imf::Compression enum.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MoviePipelineEXROutput.h

<a id="unreal.EXRCompressionFormat.NONE"></a>

#### NONE

0: No compression is applied.

<a id="unreal.EXRCompressionFormat.RLE"></a>

#### RLE

1: This compression method is fast, and works well for images with large flat areas but yields worse results for grainy images. Lossless.

<a id="unreal.EXRCompressionFormat.ZIPS"></a>

#### ZIPS

2: This compression method is similar to ZIP but compresses only one image row at a time. Lossless.

<a id="unreal.EXRCompressionFormat.ZIP"></a>

#### ZIP

3: Good compression quality for images with low amounts of noise. This compression method operates in in blocks of 16 scan lines. Lossless.

<a id="unreal.EXRCompressionFormat.PIZ"></a>

#### PIZ

4: Good compression quality for grainy images. Lossless.

<a id="unreal.EXRCompressionFormat.PXR24"></a>

#### PXR24

5: This format only stores 24 bits of the 32 bit data and has subsequently a significant loss of precision. This method is only applied when saving in FLOAT color depth. HALF and UINT remain unchanged. Lossy.

<a id="unreal.EXRCompressionFormat.B44"></a>

#### B44

6: This compression method only applies to images stored in HALF color depth. Blocks of 4×4 pixels are stored with using only 14 byte each (instead of the 32 byte they would normally need). Each block is compressed to the exact same size. Different images with the same dimensions require the same storage space regardless of image content. Lossy.

<a id="unreal.EXRCompressionFormat.B44A"></a>

#### B44A

7: A modified version of B44. If all pixels in a 4*4 block have the same color it will use only 3 instead of 14 byte.

<a id="unreal.EXRCompressionFormat.DWAA"></a>

#### DWAA

8: Lossy DCT-based compression for RGB channels. Alpha and other channels are uncompressed. More efficient than DWAB for partial buffer access on read in 3rd party tools.

<a id="unreal.EXRCompressionFormat.DWAB"></a>

#### DWAB

9: Similar to DWAA but goes in blocks of 256 scanlines instead of 32. More efficient disk space and faster to decode than DWAA.

<a id="unreal.GeometryScriptRGBAChannel"></a>