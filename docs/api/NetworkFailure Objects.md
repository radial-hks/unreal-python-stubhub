## NetworkFailure Objects

```python
class NetworkFailure(EnumBase)
```

Types of network failures broadcast from the engine

**C++ Source:**

- **Module**: NetCore
- **File**: NetEnums.h

<a id="unreal.NetworkFailure.NET_DRIVER_ALREADY_EXISTS"></a>

#### NET\_DRIVER\_ALREADY\_EXISTS

0: A relevant net driver has already been created for this service

<a id="unreal.NetworkFailure.NET_DRIVER_CREATE_FAILURE"></a>

#### NET\_DRIVER\_CREATE\_FAILURE

1: The net driver creation failed

<a id="unreal.NetworkFailure.NET_DRIVER_LISTEN_FAILURE"></a>

#### NET\_DRIVER\_LISTEN\_FAILURE

2: The net driver failed its Listen() call

<a id="unreal.NetworkFailure.CONNECTION_LOST"></a>

#### CONNECTION\_LOST

3: A connection to the net driver has been lost

<a id="unreal.NetworkFailure.CONNECTION_TIMEOUT"></a>

#### CONNECTION\_TIMEOUT

4: A connection to the net driver has timed out

<a id="unreal.NetworkFailure.FAILURE_RECEIVED"></a>

#### FAILURE\_RECEIVED

5: The net driver received an NMT_Failure message

<a id="unreal.NetworkFailure.OUTDATED_CLIENT"></a>

#### OUTDATED\_CLIENT

6: The client needs to upgrade their game

<a id="unreal.NetworkFailure.OUTDATED_SERVER"></a>

#### OUTDATED\_SERVER

7: The server needs to upgrade their game

<a id="unreal.NetworkFailure.PENDING_CONNECTION_FAILURE"></a>

#### PENDING\_CONNECTION\_FAILURE

8: There was an error during connection to the game

<a id="unreal.NetworkFailure.NET_GUID_MISMATCH"></a>

#### NET\_GUID\_MISMATCH

9: NetGuid mismatch

<a id="unreal.NetworkFailure.NET_CHECKSUM_MISMATCH"></a>

#### NET\_CHECKSUM\_MISMATCH

10: Network checksum mismatch

<a id="unreal.TravelFailure"></a>