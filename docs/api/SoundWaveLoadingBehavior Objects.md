## SoundWaveLoadingBehavior Objects

```python
class SoundWaveLoadingBehavior(EnumBase)
```

Only used when stream caching is enabled. Determines how we are going to load or retain a given audio asset.
A USoundWave's loading behavior can be overridden in the USoundWave itself, the sound wave's USoundClass, or by cvars.
The order of priority is defined as:
1) The loading behavior set on the USoundWave
2) The loading behavior set on the USoundWave's USoundClass.
3) The loading behavior set on the nearest parent of a USoundWave's USoundClass.
4) The loading behavior set via the au.streamcache cvars.

**C++ Source:**

- **Module**: Engine
- **File**: SoundWaveLoadingBehavior.h

<a id="unreal.SoundWaveLoadingBehavior.INHERITED"></a>

#### INHERITED

0: If set on a USoundWave, use the setting defined by the USoundClass. If set on the next parent USoundClass, or the default behavior defined via the au.streamcache cvars.

<a id="unreal.SoundWaveLoadingBehavior.RETAIN_ON_LOAD"></a>

#### RETAIN_ON_LOAD

1: the first chunk of audio for this asset will be retained in the audio cache until a given USoundWave is either destroyed or USoundWave::ReleaseCompressedAudioData is called.

<a id="unreal.SoundWaveLoadingBehavior.PRIME_ON_LOAD"></a>

#### PRIME_ON_LOAD

2: the first chunk of audio for this asset will be loaded into the cache from disk when this asset is loaded, but may be evicted to make room for other audio if it isn't played for a while.

<a id="unreal.SoundWaveLoadingBehavior.LOAD_ON_DEMAND"></a>

#### LOAD_ON_DEMAND

3: the first chunk of audio for this asset will not be loaded until this asset is played or primed.

<a id="unreal.SoundWaveLoadingBehavior.FORCE_INLINE"></a>

#### FORCE_INLINE

4: Force all audio data for this audio asset to live outside of the cache and use the non-streaming decode pathways. Only usable if set on the USoundWave.

<a id="unreal.MaxConcurrentResolutionRule"></a>