import 'package:connectanum/connectanum.dart';
import 'package:connectanum/json.dart';
import 'package:pedantic/pedantic.dart';

import 'dart:io';
import 'package:connectanum/src/authentication/cryptosign_authentication.dart';


void main() async {
  final cskey_hex = Platform.environment['CSKEY'];
  print(cskey_hex.length);

  final client1 = Client(
      realm: 'xbrnetwork',
      authenticationMethods: [
        CryptosignAuthentication.fromHex(cskey_hex)
      ],
      transport: WebSocketTransport(
        'ws://thingcloud-box-aws.sthngs.crossbario.com:8090/ws',
        Serializer(),
        WebSocketSerialization.SERIALIZATION_JSON,
      ));

  Session session1;

  try {
    session1 = await client1
        .connect(
            options: ClientConnectOptions(
                reconnectCount: 10,
                reconnectTime: Duration(milliseconds: 200)
                ))
        .first;
  } on Abort catch (abort) {
    print(abort.message.message);
  }
}
