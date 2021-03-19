import 'package:connectanum/connectanum.dart';
import 'package:connectanum/json.dart';
import 'package:pedantic/pedantic.dart';

void main() async {
  final client1 = Client(
      // The realm to connect to
      realm: 'demo.connectanum.receive',
      // Add the authmethods
      authenticationMethods: [
        CryptosignAuthentication.fromHex('ffaa2233fff22334433231412515')
      ],
      // We choose WebSocket transport
      transport: WebSocketTransport(
        'wss://www.connectanum.com/wamp',
        // if you want to use msgpack instead of JSON just import the serializer
        // from package:connectanum/msgpack.dart and use WebSocketSerialization.SERIALIZATION_MSGPACK
        Serializer(),
        WebSocketSerialization.SERIALIZATION_JSON,
      ));

  Session session1;

  try {
    // connect to the router and start the wamp layer
    session1 = await client1
        .connect(
            options: ClientConnectOptions(
                reconnectCount: 10, // Default is 3
                reconnectTime: Duration(
                    milliseconds: 200) // default is null, so immediately
                // you may add ping pong options here as well
                ))
        .first;
    // if you want to change the options after each reconnect, use this event
    client1.onNextTryToReconnect.listen((passedOptions) {
      // enlarge the time to wait after each reconnect by 500ms
      passedOptions.reconnectTime = Duration(
          milliseconds: passedOptions.reconnectTime.inMilliseconds + 500);
    });
  } on Abort catch (abort) {
    // if the serve does not allow this client to receive a session
    // the server will cancel the initializing process with an abort
    print(abort.message.message);
  }
}
