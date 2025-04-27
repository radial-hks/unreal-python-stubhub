## SoundAssetCompressionType Objects

```python
class SoundAssetCompressionType(EnumBase)
```

Sound Asset Compression Type

**C++ Source:**

- **Module**: Engine
- **File**: SoundWave.h

<a id="unreal.SoundAssetCompressionType.BINK_AUDIO"></a>

#### BINK_AUDIO

0: Perceptual-based codec which supports all features across all platforms.

<a id="unreal.SoundAssetCompressionType.ADPCM"></a>

#### ADPCM

1: Will encode the asset using ADPCM, a time-domain codec that has fixed-sized quality and about ~4x compression ratio, but is relatively cheap to decode.

<a id="unreal.SoundAssetCompressionType.PCM"></a>

#### PCM

2: Uncompressed audio. Large memory usage (streamed chunks contain less audio per chunk) but extremely cheap to decode and supports all features.

<a id="unreal.SoundAssetCompressionType.OPUS"></a>

#### OPUS

3: Opus is a highly versatile audio codec. It is primarily designed for interactive speech and music transmission over the Internet, but is also applicable to storage and streaming applications.

<a id="unreal.SoundAssetCompressionType.PLATFORM_SPECIFIC"></a>

#### PLATFORM_SPECIFIC

4: Encodes the asset to a platform specific format and will be different depending on the platform. It does not currently support seeking.

<a id="unreal.SoundAssetCompressionType.PROJECT_DEFINED"></a>

#### PROJECT_DEFINED

5: The project defines the codec used for this asset.

<a id="unreal.SoundAssetCompressionType.RAD_AUDIO"></a>

#### RAD_AUDIO

6: As BinkAudio, except better quality. Comparable CPU usage. Only valid sample rates are: 48000, 44100, 32000, and 24000.

<a id="unreal.TimelineDirection"></a>